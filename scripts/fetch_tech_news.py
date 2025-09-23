#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import requests
import time
import re
from datetime import datetime, timezone
from pathlib import Path
import logging

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Mapování technologických zdrojů na emoji
SOURCE_EMOJIS = {
    'techcrunch': '🚀',
    'the-verge': '⚡',
    'wired': '🔧',
    'ars-technica': '🔬',
    'engadget': '📱',
    'hacker-news': '💻',
    'the-next-web': '🌐',
    'reddit-r-technology': '👽'
}

# Kategorie technologických zpráv
TECH_CATEGORIES = {
    'ai': {'emoji': '🤖', 'name': 'AI & ML', 'cs_name': 'Umělá inteligence'},
    'programming': {'emoji': '💻', 'name': 'Programming', 'cs_name': 'Programování'},
    'hardware': {'emoji': '🖥️', 'name': 'Hardware', 'cs_name': 'Hardware'},
    'startup': {'emoji': '🚀', 'name': 'Startups', 'cs_name': 'Startupy'},
    'security': {'emoji': '🔒', 'name': 'Security', 'cs_name': 'Bezpečnost'},
    'mobile': {'emoji': '📱', 'name': 'Mobile', 'cs_name': 'Mobilní'},
    'web': {'emoji': '🌐', 'name': 'Web', 'cs_name': 'Web'},
    'gaming': {'emoji': '🎮', 'name': 'Gaming', 'cs_name': 'Hry'},
    'crypto': {'emoji': '₿', 'name': 'Crypto', 'cs_name': 'Kryptoměny'},
    'science': {'emoji': '🔬', 'name': 'Science', 'cs_name': 'Věda a výzkum'}
}

def check_environment():
    """Zkontroluje nutné proměnné prostředí"""
    news_key = os.environ.get('NEWS_API_KEY')
    openrouter_key = os.environ.get('OPENROUTER_API_KEY')

    if not news_key:
        logger.error("NEWS_API_KEY není nastaven. Nastavte ho v GitHub Secrets.")
        raise ValueError("Chybí NEWS_API_KEY")

    if not openrouter_key:
        logger.error("OPENROUTER_API_KEY není nastaven. Nastavte ho v GitHub Secrets.")
        raise ValueError("Chybí OPENROUTER_API_KEY")

    logger.info("✅ API klíče jsou nastaveny")
    return news_key, openrouter_key

def detect_category(title, description):
    """Detekuje kategorii článku podle klíčových slov"""
    text = f"{title} {description}".lower()

    category_keywords = {
        'ai': ['ai', 'artificial intelligence', 'machine learning', 'ml', 'neural', 'gpt', 'chatgpt', 'openai', 'anthropic', 'llm', 'deep learning'],
        'programming': ['javascript', 'python', 'rust', 'golang', 'typescript', 'react', 'vue', 'angular', 'framework', 'library', 'code', 'developer', 'programming'],
        'hardware': ['cpu', 'gpu', 'processor', 'intel', 'amd', 'nvidia', 'chip', 'semiconductor', 'hardware', 'motherboard', 'ram'],
        'startup': ['startup', 'funding', 'investment', 'venture', 'unicorn', 'ipo', 'acquisition', 'founder', 'entrepreneur'],
        'security': ['security', 'hack', 'breach', 'vulnerability', 'cyber', 'password', 'encryption', 'privacy', 'malware', 'ransomware'],
        'mobile': ['android', 'ios', 'iphone', 'smartphone', 'mobile', 'app store', 'google play', 'samsung', 'apple'],
        'web': ['web', 'browser', 'chrome', 'firefox', 'safari', 'html', 'css', 'frontend', 'backend', 'fullstack'],
        'gaming': ['gaming', 'game', 'playstation', 'xbox', 'nintendo', 'steam', 'epic', 'esports', 'console'],
        'crypto': ['crypto', 'bitcoin', 'ethereum', 'blockchain', 'nft', 'defi', 'web3', 'mining', 'wallet'],
        'science': ['quantum', 'space', 'nasa', 'research', 'discovery', 'experiment', 'study', 'scientific', 'physics']
    }

    for category, keywords in category_keywords.items():
        if any(keyword in text for keyword in keywords):
            return category

    return 'web'  # Default kategorie

def translate_with_openrouter(text, api_key, max_retries=3):
    """Přeloží text pomocí OpenRouter API"""
    if not text or not text.strip():
        logger.warning("Prázdný text pro překlad")
        return text

    logger.info(f"🔄 Překládám: {text[:50]}...")

    for attempt in range(max_retries):
        try:
            # Rate limiting
            if attempt > 0:
                time.sleep(2 ** attempt)  # Exponential backoff

            prompt = f"""Přelož následující anglický text do češtiny. Zachovej technické termíny, které jsou v češtině běžně používané v originále (např. AI, API, framework, startup). Odpověz pouze přeloženým textem, bez komentářů.

Text: "{text}"

Překlad:"""

            response = requests.post('https://openrouter.ai/api/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json',
                    'HTTP-Referer': 'https://www.marigold.cz',
                    'X-Title': 'Marigold Tech News Translation'
                },
                json={
                    'model': 'deepseek/deepseek-chat-v3.1:free',
                    'messages': [{'role': 'user', 'content': prompt}],
                    'max_tokens': 200,
                    'temperature': 0.3
                },
                timeout=30
            )

            logger.info(f"OpenRouter response: {response.status_code}")

            if response.status_code == 429:  # Rate limit
                logger.warning(f"Rate limit, pokus {attempt + 1}/{max_retries}")
                if attempt < max_retries - 1:
                    time.sleep(10)  # Čekat 10 sekund
                    continue

            if not response.ok:
                error_text = response.text
                logger.error(f"OpenRouter API chyba {response.status_code}: {error_text}")
                raise requests.RequestException(f"API chyba {response.status_code}: {error_text}")

            data = response.json()
            translated = data.get('choices', [{}])[0].get('message', {}).get('content', '').strip()

            if not translated:
                logger.error(f"Prázdná odpověď z OpenRouter: {data}")
                raise ValueError("OpenRouter nevrátil překlad")

            # Odstranit uvozovky
            translated = re.sub(r'^["\'"]|["\'"]$', '', translated)

            logger.info(f"✅ Překlad úspěšný: {translated[:50]}...")
            return translated

        except Exception as e:
            logger.error(f"Pokus {attempt + 1} selhal: {e}")
            if attempt == max_retries - 1:
                logger.error(f"Všechny pokusy selhaly pro text: {text[:50]}...")
                raise

    return text  # Fallback - toto by se nikdy nemělo stát

def fetch_tech_news(api_key):
    """Získá technologické zprávy z NewsAPI"""

    # Zkusit nejprve specifické zdroje
    sources = 'techcrunch,the-verge,wired,ars-technica,engadget,hacker-news,the-next-web'

    try:
        logger.info(f"🔄 Stahuji zprávy ze zdrojů: {sources}")

        response = requests.get('https://newsapi.org/v2/everything',
            params={
                'sources': sources,
                'language': 'en',
                'sortBy': 'publishedAt',
                'pageSize': 30,
                'apiKey': api_key
            },
            timeout=30
        )

        logger.info(f"NewsAPI response: {response.status_code}")

        if not response.ok:
            error_text = response.text
            logger.error(f"NewsAPI chyba {response.status_code}: {error_text}")
            raise requests.RequestException(f"NewsAPI chyba {response.status_code}: {error_text}")

        data = response.json()

        if data.get('status') != 'ok':
            logger.error(f"NewsAPI neúspěšný status: {data}")
            raise ValueError(f"NewsAPI chyba: {data.get('message', 'Neznámá chyba')}")

        articles = data.get('articles', [])
        logger.info(f"✅ Načteno {len(articles)} článků ze zdrojů")

        if articles:
            return articles

    except Exception as e:
        logger.warning(f"Stahování ze zdrojů selhalo: {e}")

    # Fallback na kategorii technology
    try:
        logger.info("🔄 Fallback - používám kategorii technology")

        response = requests.get('https://newsapi.org/v2/top-headlines',
            params={
                'category': 'technology',
                'country': 'us',
                'pageSize': 30,
                'apiKey': api_key
            },
            timeout=30
        )

        logger.info(f"NewsAPI fallback response: {response.status_code}")

        if not response.ok:
            error_text = response.text
            logger.error(f"NewsAPI fallback chyba {response.status_code}: {error_text}")
            raise requests.RequestException(f"NewsAPI fallback chyba {response.status_code}: {error_text}")

        data = response.json()

        if data.get('status') != 'ok':
            logger.error(f"NewsAPI fallback neúspěšný: {data}")
            raise ValueError(f"NewsAPI fallback chyba: {data.get('message', 'Neznámá chyba')}")

        articles = data.get('articles', [])
        logger.info(f"✅ Fallback načteno {len(articles)} článků")

        return articles

    except Exception as e:
        logger.error(f"I fallback selhal: {e}")
        raise

def create_markdown_file(article, category_info, source_emoji, output_dir):
    """Vytvoří Markdown soubor pro článek"""

    # Vytvoř slug z titulku
    slug = re.sub(r'[^\w\s-]', '', article['czech_title'].lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    slug = slug[:50]  # Omezit délku

    # Datum pro filename
    pub_date = datetime.fromisoformat(article['published_at'].replace('Z', '+00:00'))
    date_str = pub_date.strftime('%Y-%m-%d')

    filename = f"{date_str}-{slug}.md"
    filepath = output_dir / filename

    # Front matter
    front_matter = {
        'layout': 'tech_news',
        'title': article['czech_title'],
        'original_title': article['title'],
        'date': pub_date.strftime('%Y-%m-%d %H:%M:%S %z'),
        'categories': ['tech-news', category_info['name'].lower()],
        'tags': [category_info['cs_name']],
        'source': article['source']['name'],
        'source_url': article['url'],
        'image': article.get('url_to_image'),
        'emoji': f"{source_emoji} {category_info['emoji']}",
        'category_emoji': category_info['emoji'],
        'category_cs': category_info['cs_name'],
        'description': article['czech_description']
    }

    # Vytvořit obsah
    content = f"""---
{chr(10).join(f"{key}: {json.dumps(value, ensure_ascii=False) if isinstance(value, (str, list, dict)) else value}" for key, value in front_matter.items())}
---

{article['czech_description']}

[Přečíst celý článek na {article['source']['name']}]({article['url']})
"""

    # Zapsat soubor
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    logger.info(f"✅ Vytvořen: {filename}")

def main():
    """Hlavní funkce"""
    try:
        logger.info("🚀 Spouští se Tech News Fetcher")

        # Kontrola prostředí
        news_api_key, openrouter_api_key = check_environment()

        # Vytvořit výstupní adresář
        output_dir = Path('_tech_news')
        output_dir.mkdir(exist_ok=True)

        # Vyčistit starý obsah
        for old_file in output_dir.glob('*.md'):
            old_file.unlink()
        logger.info("🧹 Vyčištěn starý obsah")

        # Stáhnout zprávy
        articles = fetch_tech_news(news_api_key)

        if not articles:
            logger.error("❌ Žádné články nenalezeny")
            return

        logger.info(f"🔄 Zpracovávám {len(articles)} článků...")

        processed_count = 0

        for i, article in enumerate(articles[:20], 1):  # Omezit na 20
            try:
                # Přeskočit články bez obsahu
                if not article.get('title') or article['title'] == '[Removed]':
                    logger.warning(f"Přeskakuji článek {i} - chybí titulek")
                    continue

                logger.info(f"📰 Zpracovávám článek {i}/20: {article['title'][:50]}...")

                # Detekce kategorie
                category_key = detect_category(article['title'], article.get('description', ''))
                category_info = TECH_CATEGORIES[category_key]

                # Emoji pro zdroj
                source_id = article.get('source', {}).get('id', '').lower()
                source_emoji = SOURCE_EMOJIS.get(source_id, '💡')

                # Překlad
                czech_title = translate_with_openrouter(article['title'], openrouter_api_key)
                czech_description = ''

                if article.get('description'):
                    czech_description = translate_with_openrouter(article['description'], openrouter_api_key)

                # Příprava článku
                processed_article = {
                    'title': article['title'],
                    'czech_title': czech_title,
                    'description': article.get('description', ''),
                    'czech_description': czech_description,
                    'url': article['url'],
                    'source': article['source'],
                    'published_at': article['publishedAt'],
                    'url_to_image': article.get('urlToImage')
                }

                # Vytvoření Markdown souboru
                create_markdown_file(processed_article, category_info, source_emoji, output_dir)
                processed_count += 1

                # Rate limiting mezi články
                time.sleep(1)

            except Exception as e:
                logger.error(f"❌ Chyba při zpracování článku {i}: {e}")
                continue

        logger.info(f"✅ Úspěšně zpracováno {processed_count} článků")

        # Vytvoří index soubor
        index_content = f"""---
layout: tech_news_index
title: Technologické zpravodajství
description: Nejnovější zprávy ze světa technologií přeložené do češtiny
permalink: /tech-news/
---

Automaticky aktualizované technologické zprávy ze světových zdrojů jako TechCrunch, The Verge, Wired a dalších.

Poslední aktualizace: {datetime.now(timezone.utc).strftime('%d.%m.%Y %H:%M UTC')}
"""

        with open(output_dir / 'index.md', 'w', encoding='utf-8') as f:
            f.write(index_content)

        logger.info("✅ Tech News Fetcher úspěšně dokončen")

    except Exception as e:
        logger.error(f"💥 Kritická chyba: {e}")
        raise

if __name__ == "__main__":
    main()