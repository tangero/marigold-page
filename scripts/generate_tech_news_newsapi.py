#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import json
import os
import re
import requests
from datetime import datetime, timezone
from pathlib import Path
import logging
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from llm_cost_tracker import LLMCostTracker, track_llm_call

# Načíst .env soubor
load_dotenv()

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class NewsAPITechNewsGenerator:
    """Generátor tech-news z NewsAPI s překlady a detekcí"""

    def __init__(self):
        self.output_dir = Path('_tech_news')
        self.output_dir.mkdir(exist_ok=True)
        self.news_api_key = os.getenv('NEWS_API_KEY', '')
        self.openrouter_api_key = os.getenv('OPENROUTER_API_KEY', '')
        self.translation_enabled = self.openrouter_api_key and self.openrouter_api_key != 'skip'

        # Inicializovat LLM cost tracker
        self.cost_tracker = LLMCostTracker() if self.translation_enabled else None
        if self.cost_tracker:
            logger.info("💰 LLM Cost Tracker aktivován")

    def fetch_article_content(self, url, max_length=2000):
        """Stáhne a parsuje plný text článku z URL"""
        try:
            logger.debug(f"📄 Stahuji obsah článku: {url[:50]}...")

            headers = {
                'User-Agent': 'Mozilla/5.0 (Marigold.cz Tech News Bot; +https://marigold.cz)'
            }

            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code != 200:
                logger.warning(f"⚠️ HTTP {response.status_code} pro {url}")
                return None

            soup = BeautifulSoup(response.text, 'html.parser')

            # Odstranit skripty, styly a navigaci
            for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                element.decompose()

            # Pokusit se najít hlavní obsah článku
            article_content = None

            # Zkusit běžné selektory pro obsah článku
            for selector in ['article', 'main', '.article-content', '.post-content', '.entry-content']:
                content = soup.select_one(selector)
                if content:
                    article_content = content
                    break

            # Pokud nenalezeno, použít celý body
            if not article_content:
                article_content = soup.body

            if not article_content:
                logger.warning(f"⚠️ Nepodařilo se extrahovat obsah z {url}")
                return None

            # Získat text a vyčistit
            text = article_content.get_text(separator=' ', strip=True)

            # Vyčistit whitespace
            text = re.sub(r'\s+', ' ', text)

            # Omezit délku
            if len(text) > max_length:
                text = text[:max_length] + '...'

            logger.debug(f"✅ Extrahováno {len(text)} znaků")
            return text

        except Exception as e:
            logger.warning(f"⚠️ Chyba při stahování článku {url}: {e}")
            return None

    def analyze_and_enhance_article(self, url, title, description, category):
        """Kombinovaná LLM analýza: detekce důležitosti + generování rozšířeného obsahu"""
        if not self.translation_enabled:
            # Fallback bez LLM
            return {
                'importance': 3,
                'czech_title': title,
                'czech_description': description,
                'enhanced_content': description
            }

        try:
            # Stáhnout plný článek
            full_text = self.fetch_article_content(url)

            # Připravit kontext pro LLM
            article_context = f"""
NADPIS: {title}
POPIS: {description}
KATEGORIE: {category}
"""

            if full_text:
                article_context += f"\nPLNÝ TEXT (zkráceno): {full_text}\n"

            # Kombinovaný prompt pro důležitost + obsah
            prompt = f"""Analyzuj tento technologický článek a vytvoř český obsah.

{article_context}

ÚKOL 1 - DŮLEŽITOST (1-5):
5 = Průlomové (AGI, kvantové počítače, akvizice $1B+, bezpečnostní krize, shutdown velkých služeb)
4 = Velmi důležité (nové produkty Apple/Google/Microsoft/Meta/OpenAI, významná partnerství, IPO, funding $100M+)
3 = Zajímavé (běžné novinky, updaty, zajímavé technologie, novinky od známých firem)
2 = Spekulace (rumors, leaky, "možná", "údajně", "sources say")
1 = Nedůležité (triviální novinky, clickbait)

ÚKOL 2 - ČESKÝ OBSAH:
- Pokud důležitost ≥ 3: Vytvoř strukturovaný článek (400-600 slov)
- Pokud důležitost < 3: Vytvoř pouze krátké shrnutí (100-150 slov)

Pro důležité články (≥3) použij strukturu:
## Souhrn
[2-3 věty s podstatou novinky]

## Klíčové body
- [3-5 nejdůležitějších bodů]

## Podrobnosti
[200-300 slov s detaily, kontextem a souvislostmi. Vysvětli, co to znamená pro uživatele/průmysl.]

## Proč je to důležité
[Dopady, kontext v širším technologickém ekosystému]

STYLISTICKÉ ZÁSADY:
- Piš česky, čitelně, jasně, konkrétně a střízlivě
- Vyvaruj se superlativů a nadšených výrazů
- Vynechej preambuli, jdi přímo k věci
- Buď kritický expert na umělou inteligenci, IT a robotiku
- Používej co nejvíce detailů a konkrétních informací
- Preferuj delší souvislý text před bodovými odrážkami
- Vyvaruj se anglicismů, používej české výrazy
- U každého nového software či funkce zmiň, k čemu slouží a k čemu je možné je použít
- U méně známých firem uveď, čím se zabývají
- Úvodní odstavec by měl obsahovat shrnutí toho, o čem článek je

FORMÁT ODPOVĚDI (JSON):
{{
  "importance": 3,
  "czech_title": "Přeložený titulek",
  "czech_description": "Přeložený krátký popis (1-2 věty)",
  "enhanced_content": "Rozšířený obsah v markdown formátu"
}}

DŮLEŽITÉ:
- Technické termíny zachovej v angličtině (AI, API, GPU, atd.)
- Buď konkrétní, ne obecný
- Odpověz POUZE validním JSON, bez jakéhokoli dalšího textu
"""

            headers = {
                'Authorization': f'Bearer {self.openrouter_api_key}',
                'Content-Type': 'application/json'
            }

            data = {
                'model': 'openrouter/polaris-alpha',
                'messages': [
                    {'role': 'user', 'content': prompt}
                ],
                'max_tokens': 2000,  # Dostatek pro dlouhý obsah
                'temperature': 0.3
            }

            logger.debug(f"🤖 Volám LLM pro analýzu článku: {title[:50]}...")

            # API volání s cost trackingem
            response, usage = track_llm_call(
                url='https://openrouter.ai/api/v1/chat/completions',
                headers=headers,
                data=data,
                operation='analyze_and_enhance',
                article_slug=None,  # Slug není v tomto bodě dostupný
                article_title=title[:100],  # Omezit délku
                timeout=30,
                tracker=self.cost_tracker
            )

            if response and response.status_code == 200:
                result = response.json()
                if result.get('choices') and len(result['choices']) > 0:
                    content = result['choices'][0]['message']['content'].strip()

                    # Odstranit případné markdown code bloky
                    content = re.sub(r'^```json\s*', '', content)
                    content = re.sub(r'\s*```$', '', content)

                    # Parsovat JSON
                    try:
                        analysis = json.loads(content)

                        importance = analysis.get('importance', 3)
                        logger.info(f"✅ LLM analýza: důležitost={importance}, délka obsahu={len(analysis.get('enhanced_content', ''))} znaků")

                        return {
                            'importance': importance,
                            'czech_title': analysis.get('czech_title', title),
                            'czech_description': analysis.get('czech_description', description),
                            'enhanced_content': analysis.get('enhanced_content', description)
                        }
                    except json.JSONDecodeError as e:
                        logger.warning(f"⚠️ Chyba parsování JSON z LLM: {e}")
                        logger.warning(f"Odpověď LLM: {content[:200]}...")
                        # Fallback při chybě parsování
                        return {
                            'importance': self.detect_importance(title, description, category),
                            'czech_title': self.translate_title(title),
                            'czech_description': self.translate_description(description),
                            'enhanced_content': self.translate_description(description)
                        }
            else:
                logger.warning(f"⚠️ LLM API selhalo (HTTP {response.status_code})")

        except Exception as e:
            logger.warning(f"⚠️ Chyba při LLM analýze: {e}")

        # Fallback - použít staré metody
        return {
            'importance': self.detect_importance(title, description, category),
            'czech_title': self.translate_title(title),
            'czech_description': self.translate_description(description),
            'enhanced_content': self.translate_description(description)
        }

    def fetch_newsapi_articles(self):
        """Stáhne články z NewsAPI"""
        if not self.news_api_key:
            logger.error("❌ NEWS_API_KEY není nastaven!")
            return []

        url = "https://newsapi.org/v2/top-headlines"
        params = {
            'category': 'technology',
            'apiKey': self.news_api_key,
            'pageSize': 40,  # Max 40 článků
            'language': 'en'
        }

        try:
            logger.info("📡 Stahuji články z NewsAPI...")
            response = requests.get(url, params=params, timeout=30)

            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'ok':
                    articles = data.get('articles', [])
                    logger.info(f"✅ Staženo {len(articles)} článků z NewsAPI")

                    # Vyčistit a připravit články
                    processed_articles = []
                    for article in articles:
                        # Přeskočit články bez podstatných dat
                        if not article.get('title') or article['title'] == '[Removed]':
                            continue
                        if not article.get('url'):
                            continue

                        # Připravit zdroj
                        source_info = {
                            'id': article['source'].get('id', 'unknown'),
                            'name': article['source'].get('name', 'Unknown'),
                            'emoji': self.get_source_emoji(article['source'].get('name', ''))
                        }

                        processed_article = {
                            'title': article['title'],
                            'description': article.get('description', ''),
                            'url': article['url'],
                            'urlToImage': article.get('urlToImage'),
                            'publishedAt': article['publishedAt'],
                            'source': source_info,
                            'content': article.get('content', '')
                        }

                        processed_articles.append(processed_article)

                    return processed_articles
                else:
                    logger.error(f"❌ NewsAPI error: {data.get('message', 'Unknown')}")
            else:
                logger.error(f"❌ HTTP {response.status_code}: {response.text}")

        except Exception as e:
            logger.error(f"❌ Chyba při stahování z NewsAPI: {e}")

        return []

    def get_source_emoji(self, source_name):
        """Vrátí emoji pro zdroj"""
        emoji_map = {
            'TechCrunch': '🚀',
            'The Verge': '⚡',
            'Wired': '🔧',
            'Ars Technica': '🔬',
            'MIT Technology Review': '🎓',
            'OpenAI': '🤖',
            'Associated Press': '📰',
            'Bloomberg': '💹',
            'Forbes': '💼',
            'Axios': '📡',
            'CBS News': '📺',
            'The Wall Street Journal': '📈',
        }

        for name, emoji in emoji_map.items():
            if name.lower() in source_name.lower():
                return emoji

        return '📰'  # Default

    def create_jekyll_article(self, article, article_index):
        """Vytvoří Jekyll článek s optimalizovaným front matter"""

        # Vytvořit slug z titulku
        slug = self.create_slug(article['title'])

        # Datum pro filename - převést na UTC
        pub_date_str = article['publishedAt']
        if pub_date_str.endswith('Z'):
            pub_date = datetime.fromisoformat(pub_date_str.replace('Z', '+00:00'))
        elif '+' in pub_date_str or pub_date_str.endswith('00:00'):
            pub_date = datetime.fromisoformat(pub_date_str)
        else:
            pub_date = datetime.fromisoformat(pub_date_str).replace(tzinfo=timezone.utc)

        # Zajistit UTC
        if pub_date.tzinfo is None:
            pub_date = pub_date.replace(tzinfo=timezone.utc)
        else:
            pub_date = pub_date.astimezone(timezone.utc)

        date_str = pub_date.strftime('%Y-%m-%d')

        filename = f"{date_str}-{slug}.md"
        filepath = self.output_dir / filename

        # Detekce kategorie nejdřív (potřebujeme pro LLM analýzu)
        category = self.detect_category(article['title'], article.get('description', ''))

        # Kombinovaná LLM analýza: důležitost + český obsah
        analysis = self.analyze_and_enhance_article(
            article['url'],
            article['title'],
            article.get('description', ''),
            category
        )

        czech_title = analysis['czech_title']
        czech_description = analysis['czech_description']
        importance = analysis['importance']
        enhanced_content = analysis['enhanced_content']

        # Detekce firem a osobností (zachováme pro metadata)
        companies = self.detect_companies(article['title'], article.get('description', ''))
        people = self.detect_people(article['title'], article.get('description', ''))

        # Front matter podle tech_news_article layoutu
        front_matter = {
            'layout': 'tech_news_article',
            'title': czech_title,
            'original_title': article['title'],
            'slug': slug,
            'description': czech_description,
            'publishedAt': pub_date.isoformat(),
            'date': pub_date.strftime('%Y-%m-%d %H:%M:%S'),
            'url': article['url'],
            'category': category,
            'importance': importance,
            'source': article['source']
        }

        # Přidat autora pro důležité články (delší rozšířené verze)
        if importance >= 3:
            front_matter['author'] = 'Marisa Aigen'

        # Přidat firmy a osobnosti pouze pokud existují
        if companies:
            front_matter['companies'] = companies
        if people:
            front_matter['people'] = people

        # Přidat urlToImage a urlToImageBackup pro fallback mechanismus
        if article.get('urlToImage'):
            front_matter['urlToImage'] = article['urlToImage']
            front_matter['urlToImageBackup'] = article['urlToImage']  # Backup URL pro případ lokálního selhání

        # Vytvořit obsah
        content = f"""---
{yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)}---

{enhanced_content}

---

[Číst původní článek]({article['url']})

**Zdroj:** {article['source']['emoji']} {article['source']['name']}
"""

        # Zapsat soubor
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"✅ Vytvořen: {filename}")
        return filepath

    def create_slug(self, title):
        """Vytvoří URL-friendly slug z titulku"""
        slug = re.sub(r'[^\w\s-]', '', title.lower())
        slug = re.sub(r'[-\s]+', '-', slug).strip('-')

        # Pokud slug začíná číslicí, přidat prefix "A-"
        if slug and slug[0].isdigit():
            slug = 'A-' + slug

        # Pokud je slug prázdný, použít fallback
        if not slug:
            slug = 'article'

        return slug[:50]  # Omezit délku

    def translate_text(self, text, text_type="text"):
        """Přeloží text pomocí OpenRouter API"""
        if not self.translation_enabled or not text or text.strip() == '':
            return text

        try:
            # Různé systémové prompty podle typu textu
            system_prompts = {
                "title": "Překládej technologické nadpisy článků z angličtiny do češtiny. Zachovej technické termíny v angličtině, pokud jsou běžně používané. Odpověz POUZE přeloženým nadpisem, bez jakýchkoli dodatečných textů jako 'Nadpis článku v češtině:' nebo uvozovek.",
                "description": "Překládej perex/popis technologických článků z angličtiny do češtiny. Zachovej technické termíny v angličtině, pokud jsou běžně používané. Odpověz POUZE přeloženým textem, bez jakýchkoli dodatečných komentářů nebo uvozovek."
            }

            system_prompt = system_prompts.get(text_type, system_prompts["description"])

            headers = {
                'Authorization': f'Bearer {self.openrouter_api_key}',
                'Content-Type': 'application/json'
            }

            data = {
                'model': 'openrouter/polaris-alpha',
                'messages': [
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': text}
                ],
                'max_tokens': 200 if text_type == "title" else 500,
                'temperature': 0.3
            }

            # API volání s cost trackingem
            response, usage = track_llm_call(
                url='https://openrouter.ai/api/v1/chat/completions',
                headers=headers,
                data=data,
                operation=f'translate_{text_type}',
                article_slug=None,
                article_title=text[:50],  # Náhled textu
                timeout=10,
                tracker=self.cost_tracker
            )

            if response and response.status_code == 200:
                result = response.json()
                if result.get('choices') and len(result['choices']) > 0:
                    translated = result['choices'][0]['message']['content'].strip()
                    translated = translated.strip('"\'')
                    logger.debug(f"Překlad {text_type}: {text[:30]}... → {translated[:30]}...")
                    return translated

            if response:
                logger.warning(f"Překlad selhal (HTTP {response.status_code}), používám originál")
            else:
                logger.warning(f"Překlad selhal (API error), používám originál")

        except Exception as e:
            logger.warning(f"Chyba překladu: {e}, používám originál")

        return text

    def translate_title(self, title):
        """Přeloží titulek"""
        return self.translate_text(title, "title")

    def translate_description(self, description):
        """Přeloží popis"""
        return self.translate_text(description or '', "description")

    def detect_category(self, title, description):
        """Detekuje kategorii článku pomocí LLM"""
        if not self.translation_enabled:
            return 'tech'

        try:
            prompt = f"""Přiřaď tomuto technologickému článku jednu přesnou kategorii (1-2 slova v češtině).

Nadpis: {title}
Popis: {description or 'Není k dispozici'}

Kategorie by měla být:
- Stručná (1-2 slova)
- V češtině
- Specifická pro obsah článku
- Bez emoji

Příklady kategorií: AI, hardware, startupy, programování, mobilní aplikace, kybernetika, kosmonautika, elektromobilita, herní průmysl, kryptoměny, jídlo, zdraví atd.

Odpověz POUZE názvem kategorie, nic jiného."""

            headers = {
                'Authorization': f'Bearer {self.openrouter_api_key}',
                'Content-Type': 'application/json'
            }

            data = {
                'model': 'openrouter/polaris-alpha',
                'messages': [
                    {'role': 'user', 'content': prompt}
                ],
                'max_tokens': 20,
                'temperature': 0.1
            }

            # API volání s cost trackingem
            response, usage = track_llm_call(
                url='https://openrouter.ai/api/v1/chat/completions',
                headers=headers,
                data=data,
                operation='detect_category',
                article_slug=None,
                article_title=title[:100],
                timeout=10,
                tracker=self.cost_tracker
            )

            if response and response.status_code == 200:
                result = response.json()
                if result.get('choices') and len(result['choices']) > 0:
                    category = result['choices'][0]['message']['content'].strip()
                    category = category.lower().strip('"\'.,!?')
                    if len(category) > 20:
                        category = category[:20]

                    logger.debug(f"LLM kategorie: {title[:30]}... → {category}")
                    return category

            logger.warning(f"LLM kategorie selhala, používám fallback")

        except Exception as e:
            logger.warning(f"Chyba LLM kategorie: {e}")

        return 'tech'

    def detect_companies(self, title, description):
        """Detekuje významné firmy zmíněné v článku pomocí LLM"""
        if not self.translation_enabled:
            return []

        try:
            prompt = f"""Identifikuj všechny významné technologické firmy zmíněné v tomto článku.

Nadpis: {title}
Popis: {description or 'Není k dispozici'}

Zaměř se na:
- Technologické firmy (Apple, Google, Microsoft, Tesla, SpaceX, OpenAI, atd.)
- Startupy a scale-upy
- Významné instituce (NASA, MIT, atd.)

Ignoruj:
- Obecné termíny
- Produkty nebo služby (místo firem)
- Nezávažné zmínky

Odpověz POUZE seznam názvů firem oddělených čárkami, nic jiného.
Pokud nejsou žádné významné firmy, odpověz "žádné"."""

            headers = {
                'Authorization': f'Bearer {self.openrouter_api_key}',
                'Content-Type': 'application/json'
            }

            data = {
                'model': 'openrouter/polaris-alpha',
                'messages': [
                    {'role': 'user', 'content': prompt}
                ],
                'max_tokens': 100,
                'temperature': 0.1
            }

            # API volání s cost trackingem
            response, usage = track_llm_call(
                url='https://openrouter.ai/api/v1/chat/completions',
                headers=headers,
                data=data,
                operation='detect_companies',
                article_slug=None,
                article_title=title[:100],
                timeout=10,
                tracker=self.cost_tracker
            )

            if response and response.status_code == 200:
                result = response.json()
                if result.get('choices') and len(result['choices']) > 0:
                    companies_text = result['choices'][0]['message']['content'].strip()

                    if companies_text.lower() in ['žádné', 'zadne', 'none', '']:
                        return []

                    companies = [
                        company.strip().strip('"\'.,!?')
                        for company in companies_text.split(',')
                        if company.strip() and len(company.strip()) > 1
                    ]

                    logger.debug(f"LLM firmy: {title[:30]}... → {companies}")
                    return companies[:5]

        except Exception as e:
            logger.warning(f"Chyba LLM firem: {e}")

        return []

    def detect_people(self, title, description):
        """Detekuje významné osobnosti zmíněné v článku pomocí LLM"""
        if not self.translation_enabled:
            return []

        try:
            prompt = f"""Identifikuj všechny významné osobnosti zmíněné v tomto článku.

Nadpis: {title}
Popis: {description or 'Není k dispozici'}

Zaměř se na:
- CEO a zakladatele tech firem (Elon Musk, Tim Cook, Satya Nadella, atd.)
- Významné investory a podnikatele
- Vědce a výzkumníky
- Politiky související s technologiemi

Ignoruj:
- Obecné role bez jmen
- Fiktivní postavy
- Nezávažné zmínky

Odpověz POUZE seznam jmen oddělených čárkami, nic jiného.
Pokud nejsou žádné významné osobnosti, odpověz "žádné"."""

            headers = {
                'Authorization': f'Bearer {self.openrouter_api_key}',
                'Content-Type': 'application/json'
            }

            data = {
                'model': 'openrouter/polaris-alpha',
                'messages': [
                    {'role': 'user', 'content': prompt}
                ],
                'max_tokens': 100,
                'temperature': 0.1
            }

            # API volání s cost trackingem
            response, usage = track_llm_call(
                url='https://openrouter.ai/api/v1/chat/completions',
                headers=headers,
                data=data,
                operation='detect_people',
                article_slug=None,
                article_title=title[:100],
                timeout=10,
                tracker=self.cost_tracker
            )

            if response and response.status_code == 200:
                result = response.json()
                if result.get('choices') and len(result['choices']) > 0:
                    people_text = result['choices'][0]['message']['content'].strip()

                    if people_text.lower() in ['žádné', 'zadne', 'none', '']:
                        return []

                    people = [
                        person.strip().strip('"\'.,!?')
                        for person in people_text.split(',')
                        if person.strip() and len(person.strip()) > 2
                    ]

                    logger.debug(f"LLM osobnosti: {title[:30]}... → {people}")
                    return people[:3]

        except Exception as e:
            logger.warning(f"Chyba LLM osobností: {e}")

        return []

    def should_skip_article(self, title, description):
        """Detekuje články, které by měly být přeskočeny (hry, sport, zábava)"""
        text = f"{title} {description}".lower()

        # === HERNÍ KLÍČOVÁ SLOVA ===
        gaming_keywords = [
            # Obecné herní termíny
            'game', 'games', 'gaming', 'gamer', 'gameplay', 'playthrough',
            'esports', 'e-sports', 'speedrun', 'streamer', 'streaming game',
            # Herní platformy
            'steam', 'playstation', 'ps4', 'ps5', 'xbox', 'nintendo', 'switch',
            'game pass', 'epic games store',
            # Herní engine a nástroje
            'unreal engine', 'unity engine', 'game engine',
            # Herní společnosti
            'activision', 'ubisoft', 'ea sports', 'electronic arts', 'rockstar',
            'take-two', 'square enix', 'bandai namco', 'konami', 'capcom', 'sega',
            'blizzard', 'valve', 'bungie', 'bethesda', 'bioware',
            # Populární herní série a hry
            'call of duty', 'fortnite', 'valorant', 'counter-strike', 'cs:go', 'cs2',
            'dota', 'league of legends', 'lol', 'world of warcraft', 'wow',
            'elden ring', 'dark souls', 'zelda', 'minecraft', 'roblox',
            'gta', 'grand theft auto', 'red dead', 'assassin\'s creed',
            'final fantasy', 'borderlands', 'destiny', 'halo', 'spider-man',
            'god of war', 'horizon', 'the last of us', 'uncharted',
            'pokemon', 'mario', 'sonic', 'yakuza', 'resident evil',
            'street fighter', 'mortal kombat', 'overwatch', 'apex legends',
            'pubg', 'battlefield', 'fifa', 'nba 2k', 'madden',
            'diablo', 'starcraft', 'hearthstone', 'witcher', 'cyberpunk',
            'fallout', 'skyrim', 'elder scrolls', 'doom', 'wolfenstein',
            'marathon', 'ananta',
            # Herní žánry a termíny
            'rpg', 'mmorpg', 'fps', 'battle royale', 'roguelike', 'metroidvania',
            'souls-like', 'open world', 'sandbox', 'moba', 'rts',
            'loot box', 'battle pass', 'microtransaction', 'dlc', 'season pass',
            'gacha game', 'mobile game',
            # Herní události a média
            'gamescom', 'e3', 'pax', 'game developers conference', 'gdc',
            'state of play', 'nintendo direct', 'xbox showcase',
            'game awards', 'ign', 'gamespot', 'polygon', 'kotaku',
            'rock paper shotgun',
            # VR/AR hry
            'vr game', 'virtual reality game', 'oculus', 'quest',
            # Streamování
            'twitch', 'youtube gaming', 'mixer',
        ]

        # === SPORTOVNÍ KLÍČOVÁ SLOVA ===
        sports_keywords = [
            # Obecné sportovní termíny
            'sport', 'sports', 'athlete', 'championship', 'tournament',
            'league', 'season', 'playoffs', 'finals', 'match', 'game score',
            # Konkrétní sporty
            'football', 'soccer', 'basketball', 'baseball', 'hockey',
            'tennis', 'golf', 'cricket', 'rugby', 'boxing', 'ufc', 'mma',
            'formula 1', 'f1', 'nascar', 'racing', 'motorsport',
            # Sportovní organizace
            'nfl', 'nba', 'mlb', 'nhl', 'fifa world cup', 'premier league',
            'champions league', 'olympics', 'super bowl',
            # Wrestling a zábavní sport
            'wwe', 'wrestling', 'wrestler', 'smackdown', 'raw', 'wrestlemania',
            'aew', 'impact wrestling',
        ]

        # === ZÁBAVNÍ KLÍČOVÁ SLOVA ===
        entertainment_keywords = [
            # Filmy a seriály (pokud nejsou o technologii)
            'movie review', 'film review', 'tv series', 'netflix show',
            'season finale', 'episode', 'actor', 'actress', 'director',
            'box office', 'trailer review',
            # Reality show a celebritní zprávy
            'reality show', 'celebrity news', 'gossip',
        ]

        # Zkombinovat všechny klíčové slova
        all_skip_keywords = gaming_keywords + sports_keywords + entertainment_keywords

        # Spočítat shody
        matches = sum(1 for keyword in all_skip_keywords if keyword in text)

        # Agresivnější detekce - stačí 1 shoda
        if matches > 0:
            # Extra kontrola - některá slova mohou být falešně pozitivní
            # Pokud je to o technologii (ne o samotné hře), nepřeskakovat
            tech_indicators = [
                'ai in gaming', 'machine learning', 'artificial intelligence',
                'cloud gaming technology', 'game streaming technology',
                'graphics card', 'gpu', 'processor', 'chip',
                'nvidia', 'amd', 'intel' # pokud není přímo o herním hardware
            ]

            has_tech_context = any(indicator in text for indicator in tech_indicators)

            if not has_tech_context:
                logger.debug(f"🚫 Přeskakuji článek (nalezeno {matches} klíčových slov pro přeskočení): {title[:50]}...")
                return True

        return False

    def detect_importance(self, title, description, category):
        """Detekuje důležitost článku"""
        text = f"{title} {description}".lower()

        # Vysoká důležitost
        if any(word in text for word in ['breakthrough', 'major', 'billion', 'acquisition', 'merge']):
            return 5

        # Střední-vysoká důležitost
        if any(word in text for word in ['new', 'launches', 'announces', 'first', 'partnership']):
            return 4

        # Nízká důležitost
        if any(word in text for word in ['rumors', 'might', 'reportedly', 'could']):
            return 2

        return 3  # Default

    def clean_duplicates(self, new_articles):
        """Smaže pouze články s duplicitním slug, zachová archiv"""
        if not new_articles:
            logger.info("🧹 Žádné nové články - přeskakuji čištění duplicitů")
            return

        # Získat slugy nových článků
        new_slugs = set()
        for article in new_articles:
            slug = self.create_slug(article.get('title', ''))
            new_slugs.add(slug)

        logger.info(f"🧹 Kontroluji duplicity pro {len(new_slugs)} nových článků...")

        removed_count = 0
        for old_file in self.output_dir.glob('*.md'):
            if old_file.name == 'index.md':
                continue

            try:
                # Extrahovat slug ze jména souboru
                # Formát: YYYY-MM-DD-slug.md
                file_parts = old_file.stem.split('-', 3)
                if len(file_parts) >= 4:
                    file_slug = file_parts[3]

                    if file_slug in new_slugs:
                        logger.debug(f"🗑️ Mažu duplicitní článek: {old_file.name}")
                        old_file.unlink()
                        removed_count += 1
                    else:
                        logger.debug(f"✅ Zachovávám archivní článek: {old_file.name}")

            except Exception as e:
                logger.warning(f"⚠️ Problém při kontrole souboru {old_file.name}: {e}")

        if removed_count > 0:
            logger.info(f"🧹 Smazáno {removed_count} duplicitních článků, archiv zachován")
        else:
            logger.info("🧹 Žádné duplicity nenalezeny")

    def generate_tech_news(self):
        """Hlavní funkce pro generování tech-news z NewsAPI"""
        logger.info("🚀 Spouští se generování tech-news z NewsAPI")

        # Získat články z NewsAPI
        articles = self.fetch_newsapi_articles()

        if not articles:
            logger.error("❌ Žádné články nenalezeny z NewsAPI")
            return False

        logger.info(f"📰 Zpracovávám {len(articles)} článků...")

        # Chytré smazání duplicitů
        self.clean_duplicates(articles)

        processed_count = 0
        skipped_count = 0

        for i, article in enumerate(articles, 1):
            try:
                # Přeskočit články bez obsahu
                if not article.get('title'):
                    logger.warning(f"⏭️ Přeskakuji článek {i} - chybí titulek")
                    continue

                # Přeskočit články o hrách, sportu a zábavě
                if self.should_skip_article(article['title'], article.get('description', '')):
                    logger.info(f"🚫 Přeskakuji nerelevantní článek {i}: {article['title'][:50]}...")
                    skipped_count += 1
                    continue

                logger.info(f"📝 Zpracovávám článek {i}: {article['title'][:50]}...")

                # Kontrola obrázku
                if article.get('urlToImage'):
                    logger.info(f"🖼️ Obrázek nalezen: {article['urlToImage'][:50]}...")
                else:
                    logger.warning("🖼️ Obrázek chybí")

                # Vytvoření Jekyll souboru
                self.create_jekyll_article(article, processed_count + 1)
                processed_count += 1

            except Exception as e:
                logger.error(f"❌ Chyba při zpracování článku {i}: {e}")
                continue

        logger.info(f"✅ Úspěšně zpracováno {processed_count} článků")
        if skipped_count > 0:
            logger.info(f"🚫 Přeskočeno {skipped_count} nerelevantních článků (hry, sport, zábava)")

        # POZNÁMKA: Index stránka se již nevytváří - používáme _pages/tech-news-new.html s JSON manifestem
        # self.create_index_page(processed_count)

        return True

    def create_index_page(self, article_count):
        """Vytvoří index stránku tech-news"""
        index_content = f"""---
layout: tech_news_index
title: Technologické zprávy
permalink: /tech-news/
description: Nejnovější zprávy ze světa technologií z NewsAPI s překlady do češtiny
---

# Technologické zprávy

Automaticky aktualizované zprávy ze světa technologií z NewsAPI, přeložené do češtiny.

**Celkem článků:** {article_count}
**Poslední aktualizace:** {datetime.now(timezone.utc).strftime('%d.%m.%Y %H:%M UTC')}

## Zdroje

Články jsou získávány z NewsAPI Technology kategorie, včetně zdrojů jako:
- 📰 **Associated Press** - zpravodajství
- 🚀 **TechCrunch** - startupy a technologie
- 💹 **Bloomberg** - business a finance
- 💼 **Forbes** - podnikání a investice
- 📡 **Axios** - technologie a politika
- 🤖 **OpenAI** - AI průlomy
"""

        index_path = self.output_dir / 'index.md'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)

        logger.info("✅ Index stránka vytvořena")

    def generate_daily_pages(self):
        """Generuje stránky pro každý den s články"""
        from collections import defaultdict

        # Cesty
        pages_dir = Path('tech-news')

        # Načíst všechny články a seskupit podle data
        articles_by_date = defaultdict(list)

        for article_file in self.output_dir.glob('*.md'):
            with open(article_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extrahovat front matter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    try:
                        front_matter = yaml.safe_load(parts[1])

                        # Získat datum
                        date_str = None
                        if 'publishedAt' in front_matter:
                            date_obj = datetime.fromisoformat(front_matter['publishedAt'].replace('Z', '+00:00'))
                            date_str = date_obj.strftime('%Y-%m-%d')
                        elif 'date' in front_matter:
                            if isinstance(front_matter['date'], str):
                                date_obj = datetime.fromisoformat(front_matter['date'].split(' ')[0])
                            else:
                                date_obj = front_matter['date']
                            date_str = date_obj.strftime('%Y-%m-%d')

                        if date_str:
                            articles_by_date[date_str].append(article_file.name)

                    except Exception as e:
                        logger.warning(f"⚠️ Chyba při zpracování {article_file.name}: {e}")

        # Vytvořit stránku pro každý den
        for date_str, articles in articles_by_date.items():
            # Vytvořit adresář pro tento den
            day_dir = pages_dir / date_str
            day_dir.mkdir(parents=True, exist_ok=True)

            # Vytvořit index.md pro tento den
            index_file = day_dir / 'index.md'

            # Front matter pro denní stránku
            front_matter = {
                'layout': 'tech_news_day',
                'title': f'Technologické zprávy - {date_str}',
                'date': date_str,
                'permalink': f'/tech-news/{date_str}/'
            }

            # Vytvořit obsah stránky
            content = f"""---
{yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)}---

<!-- Tato stránka automaticky zobrazuje články z kolekce _tech_news pro datum {date_str} -->
"""

            # Zapsat soubor
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)

            logger.debug(f"📅 Vytvořena denní stránka pro {date_str}")

def main():
    """Hlavní funkce"""
    generator = NewsAPITechNewsGenerator()

    # Kontrola API klíčů
    if not generator.news_api_key:
        logger.error("❌ NEWS_API_KEY není nastaven v .env souboru!")
        return 1

    logger.info(f"📊 NewsAPI generator připraven")
    if generator.translation_enabled:
        logger.info("✅ Překlady povoleny (OpenRouter API)")
    else:
        logger.info("⚠️ Překlady zakázány (chybí OPENROUTER_API_KEY)")

    # Generovat tech-news
    success = generator.generate_tech_news()

    if success:
        # Generovat denní archivní stránky
        generator.generate_daily_pages()
        logger.info("🎉 Generování tech-news z NewsAPI dokončeno")

        # Zobrazit LLM cost statistiky
        if generator.cost_tracker:
            try:
                stats = generator.cost_tracker.get_stats(days=1)
                logger.info("💰 LLM Cost Statistics (today):")
                logger.info(f"   • Total calls: {stats['total_calls']}")
                logger.info(f"   • Total tokens: {stats['total_tokens']:,}")
                logger.info(f"   • Total cost: ${stats['total_cost_usd']:.4f}")
                logger.info(f"   • Avg cost per call: ${stats['avg_cost_per_call']:.6f}")
                generator.cost_tracker.close()
            except Exception as e:
                logger.warning(f"⚠️ Chyba při zobrazení cost statistik: {e}")
    else:
        logger.error("💥 Generování tech-news z NewsAPI selhalo")
        if generator.cost_tracker:
            generator.cost_tracker.close()
        return 1

    return 0

if __name__ == "__main__":
    exit(main())