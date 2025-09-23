#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
import json
import os
import requests
import time
import re
from datetime import datetime, timezone
from pathlib import Path
import logging
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Načíst .env soubor
load_dotenv()

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# RSS zdroje technologických zpráv
RSS_FEEDS = {
    'TechCrunch': {
        'url': 'https://techcrunch.com/feed/',
        'emoji': '🚀',
        'priority': 5
    },
    'The Verge': {
        'url': 'https://www.theverge.com/rss/index.xml',
        'emoji': '⚡',
        'priority': 5
    },
    'Ars Technica': {
        'url': 'https://feeds.arstechnica.com/arstechnica/technology',
        'emoji': '🔬',
        'priority': 4
    },
    'Wired': {
        'url': 'https://www.wired.com/feed/rss',
        'emoji': '🔧',
        'priority': 4
    },
    'Hacker News': {
        'url': 'https://hnrss.org/frontpage',
        'emoji': '💻',
        'priority': 3
    },
    'MIT Technology Review': {
        'url': 'https://www.technologyreview.com/feed/',
        'emoji': '🎓',
        'priority': 4
    }
}

def clean_html(html_text):
    """Odstraní HTML tagy z textu"""
    if not html_text:
        return ""
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.get_text().strip()

def fetch_rss_articles(max_articles_per_feed=5):
    """Stáhne články z RSS feedů"""
    all_articles = []

    for source_name, source_info in RSS_FEEDS.items():
        try:
            logger.info(f"📡 Stahuji RSS z {source_name}...")

            # Parsovat RSS
            feed = feedparser.parse(source_info['url'])

            if feed.bozo:
                logger.warning(f"⚠️ Problém s parsováním {source_name}: {feed.bozo_exception}")
                continue

            # Zpracovat články
            articles_count = 0
            for entry in feed.entries[:max_articles_per_feed]:
                try:
                    # Získat základní data
                    title = entry.get('title', '')
                    link = entry.get('link', '')

                    # Získat popis (různé RSS formáty)
                    description = entry.get('description') or entry.get('summary') or ''
                    description = clean_html(description)[:500]  # Max 500 znaků

                    # Získat datum publikace
                    published = entry.get('published_parsed') or entry.get('updated_parsed')
                    if published:
                        pub_date = datetime.fromtimestamp(time.mktime(published), tz=timezone.utc)
                    else:
                        pub_date = datetime.now(timezone.utc)

                    # Získat obrázek (pokud existuje)
                    image = None
                    if hasattr(entry, 'media_thumbnail'):
                        image = entry.media_thumbnail[0]['url']
                    elif hasattr(entry, 'media_content'):
                        image = entry.media_content[0]['url']

                    article = {
                        'title': title,
                        'description': description,
                        'url': link,
                        'source': {'name': source_name, 'id': source_name.lower().replace(' ', '-')},
                        'publishedAt': pub_date.isoformat(),
                        'urlToImage': image,
                        'source_priority': source_info['priority'],
                        'source_emoji': source_info['emoji']
                    }

                    all_articles.append(article)
                    articles_count += 1

                except Exception as e:
                    logger.error(f"Chyba při zpracování článku z {source_name}: {e}")
                    continue

            logger.info(f"✅ Načteno {articles_count} článků z {source_name}")

        except Exception as e:
            logger.error(f"❌ Selhalo stahování {source_name}: {e}")
            continue

    # Seřadit podle priority a data
    all_articles.sort(key=lambda x: (x['source_priority'], x['publishedAt']), reverse=True)

    logger.info(f"📚 Celkem načteno {len(all_articles)} článků ze všech zdrojů")
    return all_articles

def hybrid_fetch(use_rss=True, use_newsapi=False):
    """Hybridní přístup - RSS + NewsAPI fallback"""
    articles = []

    # Primárně RSS
    if use_rss:
        try:
            articles = fetch_rss_articles()
        except Exception as e:
            logger.error(f"RSS selhalo: {e}")

    # Fallback na NewsAPI pokud málo článků
    if use_newsapi and len(articles) < 10:
        logger.info("📰 Používám NewsAPI jako doplněk...")
        try:
            news_key = os.environ.get('NEWS_API_KEY')
            if news_key:
                response = requests.get(
                    'https://newsapi.org/v2/top-headlines',
                    params={
                        'category': 'technology',
                        'pageSize': 20,
                        'apiKey': news_key
                    },
                    timeout=30
                )
                if response.ok:
                    data = response.json()
                    newsapi_articles = data.get('articles', [])

                    # Přidat pouze unikátní články
                    existing_urls = {a['url'] for a in articles}
                    for article in newsapi_articles:
                        if article.get('url') not in existing_urls:
                            articles.append(article)

                    logger.info(f"✅ Přidáno {len(newsapi_articles)} článků z NewsAPI")
        except Exception as e:
            logger.error(f"NewsAPI fallback selhal: {e}")

    return articles

if __name__ == "__main__":
    # Test RSS fetcheru
    logger.info("🚀 Testování RSS Fetcher")

    articles = hybrid_fetch(use_rss=True, use_newsapi=False)

    # Vypsat první 3 články
    for i, article in enumerate(articles[:3], 1):
        print(f"\n📰 Článek {i}:")
        print(f"  Titulek: {article['title'][:80]}...")
        print(f"  Zdroj: {article['source']['name']} {article.get('source_emoji', '')}")
        print(f"  Popis: {article['description'][:150]}...")
        print(f"  URL: {article['url']}")