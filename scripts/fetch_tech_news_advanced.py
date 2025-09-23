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

# Načíst .env soubor
load_dotenv()

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RSSNewsManager:
    """Správce RSS zdrojů s podporou obrázků a pokročilými funkcemi"""

    def __init__(self, config_file='_data/tech_news_sources.yaml'):
        """Inicializace s konfiguračním souborem"""
        self.config_file = Path(config_file)
        self.config = self.load_config()
        self.cache_dir = Path('_cache')
        self.cache_dir.mkdir(exist_ok=True)

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

    def get_cache_path(self, source_id):
        """Vrátí cestu k cache souboru pro zdroj"""
        return self.cache_dir / f"{source_id}.json"

    def is_cache_valid(self, cache_path):
        """Zkontroluje, zda je cache platná"""
        if not cache_path.exists():
            return False

        cache_age = time.time() - cache_path.stat().st_mtime
        max_age = self.config['settings'].get('cache_hours', 1) * 3600

        return cache_age < max_age

    def save_to_cache(self, source_id, articles):
        """Uloží články do cache"""
        cache_path = self.get_cache_path(source_id)
        try:
            with open(cache_path, 'w', encoding='utf-8') as f:
                json.dump(articles, f, ensure_ascii=False, indent=2)
            logger.debug(f"💾 Uloženo do cache: {source_id}")
        except Exception as e:
            logger.error(f"Chyba při ukládání cache {source_id}: {e}")

    def load_from_cache(self, source_id):
        """Načte články z cache"""
        cache_path = self.get_cache_path(source_id)
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                articles = json.load(f)
                logger.info(f"📦 Načteno z cache: {source_id} ({len(articles)} článků)")
                return articles
        except Exception as e:
            logger.error(f"Chyba při čtení cache {source_id}: {e}")
            return []

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

        # 3. Enclosure (podcasts, ale někdy i obrázky)
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

        # 5. Link parsing pro některé RSS (např. 9to5mac)
        if not image_url and hasattr(entry, 'links'):
            for link in entry.links:
                if link.get('type', '').startswith('image'):
                    image_url = link.get('href')
                    break

        return image_url

    def fetch_og_image(self, article_url, timeout=5):
        """Stáhne Open Graph obrázek ze stránky článku"""
        if not self.config['settings']['image_handling'].get('fetch_og_images'):
            return None

        try:
            response = requests.get(article_url, timeout=timeout, headers={
                'User-Agent': 'Mozilla/5.0 (Marigold.cz Tech News Bot)'
            })

            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Open Graph image
                og_image = soup.find('meta', property='og:image')
                if og_image:
                    return og_image.get('content')

                # Twitter card image
                twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
                if twitter_image:
                    return twitter_image.get('content')

        except Exception as e:
            logger.debug(f"Nelze získat OG image z {article_url}: {e}")

        return None

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

    def fetch_articles_from_source(self, source_id, source_config):
        """Stáhne články z jednoho RSS zdroje"""
        articles = []

        # Zkontrolovat cache
        cache_path = self.get_cache_path(source_id)
        if self.is_cache_valid(cache_path):
            return self.load_from_cache(source_id)

        try:
            logger.info(f"📡 Stahuji RSS: {source_config['name']}...")

            # Parsovat RSS
            feed = feedparser.parse(source_config['url'])

            if feed.bozo and not feed.entries:
                logger.warning(f"⚠️ Problém s {source_config['name']}: {feed.bozo_exception}")
                return []

            # Limity
            max_articles = source_config.get('max_articles', 5)
            max_age_days = self.config['settings']['filters'].get('max_age_days', 7)
            cutoff_date = datetime.now(timezone.utc) - timedelta(days=max_age_days)

            # Zpracovat články
            for entry in feed.entries[:max_articles * 2]:  # Vezmi víc, vyfiltrujeme
                try:
                    # Základní data
                    title = entry.get('title', '').strip()
                    link = entry.get('link', '')

                    # Filtr - minimální délka titulku
                    min_title = self.config['settings']['filters'].get('min_title_length', 10)
                    if len(title) < min_title:
                        continue

                    # Filtr - vyloučená klíčová slova
                    exclude = self.config['settings']['filters'].get('exclude_keywords', [])
                    if any(kw.lower() in title.lower() for kw in exclude):
                        logger.debug(f"⛔ Vyloučen (keyword): {title}")
                        continue

                    # Datum
                    published = entry.get('published_parsed') or entry.get('updated_parsed')
                    if published:
                        pub_date = datetime.fromtimestamp(time.mktime(published), tz=timezone.utc)
                    else:
                        pub_date = datetime.now(timezone.utc)

                    # Filtr - stáří
                    if pub_date < cutoff_date:
                        logger.debug(f"⏰ Příliš starý: {title}")
                        continue

                    # Popis
                    description = entry.get('description') or entry.get('summary') or ''
                    description = self.clean_text(description)

                    # Obrázek - pokusit se získat z RSS
                    image_url = self.extract_image_from_content(entry)

                    # Fallback - získat Open Graph image
                    if not image_url and link:
                        image_url = self.fetch_og_image(link)

                    # Vytvořit článek
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

                    articles.append(article)

                    if len(articles) >= max_articles:
                        break

                except Exception as e:
                    logger.error(f"Chyba při zpracování článku z {source_config['name']}: {e}")
                    continue

            logger.info(f"✅ {source_config['name']}: {len(articles)} článků")

            # Uložit do cache
            if articles:
                self.save_to_cache(source_id, articles)

        except Exception as e:
            logger.error(f"❌ Selhalo stahování {source_config['name']}: {e}")

        return articles

    def fetch_all_articles(self):
        """Stáhne články ze všech povolených zdrojů"""
        all_articles = []

        # Projít všechny zdroje
        for source_id, source_config in self.config['sources'].items():
            # Přeskočit vypnuté zdroje
            if not source_config.get('enabled', True):
                logger.debug(f"⏭️ Přeskakuji vypnutý zdroj: {source_config['name']}")
                continue

            # Stáhnout články
            articles = self.fetch_articles_from_source(source_id, source_config)
            all_articles.extend(articles)

        # Seřadit podle priority a data
        all_articles.sort(key=lambda x: (-x['priority'], x['publishedAt']), reverse=True)

        # Omezit celkový počet
        max_total = self.config['settings'].get('total_max_articles', 30)
        all_articles = all_articles[:max_total]

        logger.info(f"📚 Celkem {len(all_articles)} článků ze všech zdrojů")
        return all_articles

    def get_stats(self):
        """Vrátí statistiky o zdrojích"""
        stats = {
            'total_sources': len(self.config['sources']),
            'enabled_sources': sum(1 for s in self.config['sources'].values() if s.get('enabled', True)),
            'sources_by_priority': {},
            'sources_by_language': {}
        }

        for source_id, source in self.config['sources'].items():
            if not source.get('enabled', True):
                continue

            # Priority
            priority = source.get('priority', 3)
            if priority not in stats['sources_by_priority']:
                stats['sources_by_priority'][priority] = []
            stats['sources_by_priority'][priority].append(source['name'])

            # Language
            lang = source.get('language', 'en')
            if lang not in stats['sources_by_language']:
                stats['sources_by_language'][lang] = []
            stats['sources_by_language'][lang].append(source['name'])

        return stats

def main():
    """Test správce RSS zdrojů"""
    logger.info("🚀 Testování Advanced RSS Manager")

    # Inicializovat správce
    manager = RSSNewsManager()

    # Zobrazit statistiky
    stats = manager.get_stats()
    logger.info(f"📊 Statistiky:")
    logger.info(f"  - Celkem zdrojů: {stats['total_sources']}")
    logger.info(f"  - Aktivních: {stats['enabled_sources']}")
    logger.info(f"  - České zdroje: {stats['sources_by_language'].get('cs', [])}")

    # Stáhnout články
    articles = manager.fetch_all_articles()

    # Zobrazit první 3 články s obrázky
    logger.info("\n📰 Ukázka článků:")
    for i, article in enumerate(articles[:3], 1):
        print(f"\n{i}. {article['source']['emoji']} {article['title'][:60]}...")
        print(f"   Zdroj: {article['source']['name']}")
        print(f"   Popis: {article['description'][:100]}...")
        print(f"   Obrázek: {'✅ Ano' if article['urlToImage'] else '❌ Ne'}")
        if article['urlToImage']:
            print(f"   URL obrázku: {article['urlToImage'][:50]}...")

if __name__ == "__main__":
    main()