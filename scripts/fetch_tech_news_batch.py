#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
import yaml
import json
import os
import requests
import time
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path
import logging
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import hashlib
import unicodedata
from typing import List, Dict, Optional, Tuple

# Načíst .env soubor
load_dotenv()

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BatchTechNewsManager:
    """Pokročilý správce tech news s batch překladem a LLM vyhodnocením"""

    def __init__(self, config_file='_data/tech_news_sources.yaml'):
        """Inicializace s konfiguračním souborem"""
        self.config_file = Path(config_file)
        self.config = self.load_config()
        self.cache_dir = Path('_cache')
        self.cache_dir.mkdir(exist_ok=True)

        # API klíče
        self.openrouter_key = os.environ.get('OPENROUTER_API_KEY')
        if not self.openrouter_key or self.openrouter_key == "skip":
            logger.warning("⚠️ OpenRouter API klíč není nastaven - překlady budou přeskočeny")
            self.openrouter_key = None

    def load_config(self):
        """Načte konfiguraci ze YAML souboru"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                logger.info(f"✅ Načtena konfigurace: {len(config['sources'])} zdrojů")
                return config
        except Exception as e:
            logger.error(f"❌ Chyba při načítání konfigurace: {e}")
            return {'sources': {}, 'settings': {}}

    def extract_image_from_content(self, entry):
        """Extrahuje obrázek z různých RSS formátů"""
        image_url = None

        # 1. Media thumbnail (nejčastější)
        if hasattr(entry, 'media_thumbnail') and entry.media_thumbnail:
            image_url = entry.media_thumbnail[0].get('url')

        # 2. Media content
        elif hasattr(entry, 'media_content') and entry.media_content:
            for media in entry.media_content:
                if media.get('type', '').startswith('image'):
                    image_url = media.get('url')
                    break

        # 3. Enclosure
        elif hasattr(entry, 'enclosures') and entry.enclosures:
            for enc in entry.enclosures:
                if enc.get('type', '').startswith('image'):
                    image_url = enc.get('href')
                    break

        # 4. Content HTML parsing
        if not image_url:
            content = entry.get('content', [{}])[0].get('value', '') if hasattr(entry, 'content') else ''
            if not content:
                content = entry.get('summary', '')

            if content:
                soup = BeautifulSoup(content, 'html.parser')
                img = soup.find('img')
                if img:
                    image_url = img.get('src')

        return image_url

    def clean_text(self, text, max_length=500):
        """Vyčistí text od HTML a zkrátí"""
        if not text:
            return ""

        # Odstranit HTML
        soup = BeautifulSoup(text, 'html.parser')
        clean = soup.get_text().strip()

        # Odstranit extra mezery
        clean = ' '.join(clean.split())

        # Zkrátit na max délku
        if len(clean) > max_length:
            clean = clean[:max_length] + "..."

        return clean

    def transliterate_to_ascii(self, text):
        """Převede text s diakritikou na ASCII-only verzi pro URL"""
        if not text:
            return ""

        # Normalize unicode characters
        nfkd_form = unicodedata.normalize('NFKD', text)
        # Filter out non-ASCII characters
        ascii_text = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

        # Replace remaining non-ASCII chars with safe alternatives
        replacements = {
            'č': 'c', 'ď': 'd', 'ě': 'e', 'ň': 'n', 'ř': 'r', 'š': 's', 'ť': 't', 'ů': 'u', 'ž': 'z',
            'Č': 'C', 'Ď': 'D', 'Ě': 'E', 'Ň': 'N', 'Ř': 'R', 'Š': 'S', 'Ť': 'T', 'Ů': 'U', 'Ž': 'Z',
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ý': 'y',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ý': 'Y'
        }

        for czech_char, ascii_char in replacements.items():
            ascii_text = ascii_text.replace(czech_char, ascii_char)

        return ascii_text

    def fetch_articles_from_all_sources(self) -> List[Dict]:
        """Stáhne články ze všech RSS zdrojů"""
        all_articles = []

        for source_id, source_config in self.config['sources'].items():
            if not source_config.get('enabled', True):
                logger.debug(f"⏭️ Přeskakuji vypnutý zdroj: {source_config['name']}")
                continue

            try:
                logger.info(f"📡 Stahuji RSS: {source_config['name']}...")

                feed = feedparser.parse(source_config['url'])

                if feed.bozo and not feed.entries:
                    logger.warning(f"⚠️ Problém s {source_config['name']}: {feed.bozo_exception}")
                    continue

                max_articles = source_config.get('max_articles', 5)
                max_age_days = self.config['settings']['filters'].get('max_age_days', 7)
                cutoff_date = datetime.now(timezone.utc) - timedelta(days=max_age_days)

                for entry in feed.entries[:max_articles * 2]:
                    try:
                        title = entry.get('title', '').strip()
                        link = entry.get('link', '')

                        if len(title) < self.config['settings']['filters'].get('min_title_length', 10):
                            continue

                        exclude = self.config['settings']['filters'].get('exclude_keywords', [])
                        if any(kw.lower() in title.lower() for kw in exclude):
                            continue

                        # Datum
                        published = entry.get('published_parsed') or entry.get('updated_parsed')
                        if published:
                            pub_date = datetime.fromtimestamp(time.mktime(published), tz=timezone.utc)
                        else:
                            pub_date = datetime.now(timezone.utc)

                        if pub_date < cutoff_date:
                            continue

                        # Popis
                        description = entry.get('description') or entry.get('summary') or ''
                        description = self.clean_text(description)

                        # Obrázek
                        image_url = self.extract_image_from_content(entry)

                        article = {
                            'title': title,
                            'description': description,
                            'url': link,
                            'source': {
                                'name': source_config['name'],
                                'id': source_id,
                                'emoji': source_config.get('emoji', '📰')
                            },
                            'publishedAt': pub_date.isoformat(),
                            'urlToImage': image_url,
                            'priority': source_config.get('priority', 3),
                            'language': source_config.get('language', 'en'),
                            'categories': source_config.get('category_focus', [])
                        }

                        all_articles.append(article)

                        if len(all_articles) >= max_articles:
                            break

                    except Exception as e:
                        logger.error(f"Chyba při zpracování článku z {source_config['name']}: {e}")
                        continue

                logger.info(f"✅ {source_config['name']}: {len([a for a in all_articles if a['source']['id'] == source_id])} článků")

            except Exception as e:
                logger.error(f"❌ Selhalo stahování {source_config['name']}: {e}")

        return all_articles

    def batch_translate_and_evaluate(self, articles: List[Dict]) -> List[Dict]:
        """Batch překladá články a vyhodnocuje jejich důležitost pomocí LLM"""
        if not self.openrouter_key:
            logger.warning("⚠️ Přeskakuji překlad - API klíč není nastaven")
            return articles

        # Připravit batch data pro LLM
        batch_data = []
        for i, article in enumerate(articles):
            batch_data.append({
                "id": i,
                "title": article['title'],
                "description": article['description']
            })

        # Strukturovaný prompt pro batch zpracování
        system_prompt = """Jsi expert na technologické zprávy. Tvým úkolem je:
1. Přeložit každý článek do češtiny (zachovat faktickou přesnost)
2. Vyhodnotit důležitost článku na škále 1-5:
   - 1: Běžné novinky, drobné aktualizace
   - 2: Zajímavé, ale ne kritické informace
   - 3: Významné novinky v oboru
   - 4: Velmi důležité události (velké akvizice, průlomy)
   - 5: Převratné události (zásadní průlomy, mega-akvizice, bezpečnostní krizí)

3. Identifikovat primární kategorii článku:
   - ai: Umělá inteligence a machine learning
   - startups: Startupy, investice, podnikání
   - hardware: Hardware, čipy, zařízení
   - mobile: Mobilní technologie, aplikace
   - security: Kybernetická bezpečnost, soukromí
   - science: Výzkum, věda, technologie
   - programming: Vývoj software, programování
   - gaming: Herní průmysl
   - social: Sociální sítě, platformy
   - business: Obchodní dohody, firemní strategie

Vrať odpověď jako JSON array, kde každý objekt obsahuje:
{
  "id": číslo_článku,
  "title_cs": "český_překlad_titulku",
  "description_cs": "český_překlad_popisu",
  "importance": číslo_1_až_5,
  "category": "kategorie"
}"""

        user_prompt = f"""Zpracuj tyto technologické články:

{json.dumps(batch_data, ensure_ascii=False, indent=2)}

Vrať odpověď jako JSON array s překlady a vyhodnocením."""

        try:
            logger.info(f"🤖 Posílám {len(articles)} článků na batch zpracování...")

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.openrouter_key}",
                    "HTTP-Referer": "https://marigold.cz",
                    "X-Title": "Marigold Tech News",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "qwen/qwen3-max",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "temperature": 0.3,
                    "max_tokens": 8000
                },
                timeout=60
            )

            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content'].strip()

                # Extrahovat JSON z odpovědi
                if content.startswith('```json'):
                    content = content[7:-3].strip()
                elif content.startswith('```'):
                    content = content[3:-3].strip()

                processed_data = json.loads(content)

                logger.info(f"✅ Úspěšně zpracováno {len(processed_data)} článků")

                # Aplikovat výsledky na články
                for item in processed_data:
                    article_id = item['id']
                    if article_id < len(articles):
                        articles[article_id].update({
                            'title_cs': item.get('title_cs', articles[article_id]['title']),
                            'description_cs': item.get('description_cs', articles[article_id]['description']),
                            'importance': item.get('importance', 3),
                            'category': item.get('category', 'tech')
                        })

                return articles

            elif response.status_code == 429:
                logger.error("❌ Rate limit překročen - zkus později")
                wait_time = int(response.headers.get('retry-after', 300))
                logger.info(f"⏰ Čekám {wait_time} sekund...")
                time.sleep(wait_time)
                return articles
            else:
                logger.error(f"❌ API chyba: {response.status_code} - {response.text}")
                return articles

        except json.JSONDecodeError as e:
            logger.error(f"❌ Chyba při parsování JSON odpovědi: {e}")
            return articles
        except Exception as e:
            logger.error(f"❌ Chyba při batch zpracování: {e}")
            return articles

    def save_articles_to_jekyll(self, articles: List[Dict]):
        """Uloží články do Jekyll collections"""
        output_dir = Path('_tech_news')
        output_dir.mkdir(exist_ok=True)

        # Vyčistit staré články
        for old_file in output_dir.glob('*.md'):
            old_file.unlink()

        for i, article in enumerate(articles, 1):
            try:
                # Použít český překlad pokud existuje
                title = article.get('title_cs', article['title'])
                description = article.get('description_cs', article['description'])

                # Vytvořit filename safe název bez diakritiky
                ascii_title = self.transliterate_to_ascii(title)
                safe_title = re.sub(r'[^\w\s-]', '', ascii_title).strip()
                safe_title = re.sub(r'[-\s]+', '-', safe_title)[:50]

                date_str = datetime.now().strftime('%Y-%m-%d')
                filename = f"{date_str}-{i:02d}-{safe_title}.md"

                # Front matter
                front_matter = {
                    'layout': 'tech_news_article',
                    'title': title,
                    'description': description,
                    'original_title': article['title'],
                    'url': article['url'],
                    'source': article['source'],
                    'publishedAt': article['publishedAt'],
                    'importance': article.get('importance', 3),
                    'category': article.get('category', 'tech'),
                    'urlToImage': article.get('urlToImage'),
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }

                # Generovat markdown soubor
                content = f"""---
{yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)}---

{description}

[Číst původní článek]({article['url']})

**Zdroj:** {article['source']['emoji']} {article['source']['name']}
"""

                file_path = output_dir / filename
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                logger.debug(f"💾 Uložen článek: {filename}")

            except Exception as e:
                logger.error(f"❌ Chyba při ukládání článku {i}: {e}")

    def run_full_pipeline(self):
        """Spustí celý pipeline: stažení -> batch zpracování -> uložení"""
        logger.info("🚀 Spouštím kompletní tech news pipeline...")

        # 1. Stáhnout články
        articles = self.fetch_articles_from_all_sources()
        if not articles:
            logger.warning("⚠️ Žádné články k zpracování")
            return

        logger.info(f"📚 Celkem načteno {len(articles)} článků")

        # 2. Batch zpracování (překlad + vyhodnocení)
        processed_articles = self.batch_translate_and_evaluate(articles)

        # 3. Seřadit podle důležitosti a data
        processed_articles.sort(key=lambda x: (-x.get('importance', 3), x['publishedAt']), reverse=True)

        # 4. Omezit počet článků
        max_total = self.config['settings'].get('total_max_articles', 30)
        processed_articles = processed_articles[:max_total]

        # 5. Uložit do Jekyll
        self.save_articles_to_jekyll(processed_articles)

        logger.info(f"✅ Pipeline dokončen: {len(processed_articles)} článků uloženo")

        # Statistiky
        importance_stats = {}
        category_stats = {}
        for article in processed_articles:
            imp = article.get('importance', 3)
            cat = article.get('category', 'tech')
            importance_stats[imp] = importance_stats.get(imp, 0) + 1
            category_stats[cat] = category_stats.get(cat, 0) + 1

        logger.info(f"📊 Statistiky důležitosti: {importance_stats}")
        logger.info(f"📊 Statistiky kategorií: {category_stats}")

def main():
    """Hlavní funkce"""
    manager = BatchTechNewsManager()
    manager.run_full_pipeline()

if __name__ == "__main__":
    main()