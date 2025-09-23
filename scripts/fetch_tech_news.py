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
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Načíst .env soubor pokud existuje (pro lokální development)
load_dotenv()

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

# Mapování důležitosti na emoji a názvy
IMPORTANCE_LEVELS = {
    5: {'emoji': '🔥', 'name': 'KRITICKÁ', 'color': '#dc2626', 'bg_color': '#fef2f2'},
    4: {'emoji': '⚡', 'name': 'VYSOKÁ', 'color': '#ea580c', 'bg_color': '#fff7ed'},
    3: {'emoji': '📢', 'name': 'STŘEDNÍ', 'color': '#2563eb', 'bg_color': '#eff6ff'},
    2: {'emoji': '📝', 'name': 'NÍZKÁ', 'color': '#059669', 'bg_color': '#ecfdf5'},
    1: {'emoji': '💬', 'name': 'INFO', 'color': '#6b7280', 'bg_color': '#f9fafb'}
}

# Kategorie technologických zpráv
TECH_CATEGORIES = {
    'ai': {'emoji': '🤖', 'name': 'AI & ML', 'cs_name': 'Umělá inteligence'},
    'programming': {'emoji': '💻', 'name': 'Programming', 'cs_name': 'Programování'},
    'hardware': {'emoji': '🖥️', 'name': 'Hardware', 'cs_name': 'Hardware'},
    'startups': {'emoji': '🚀', 'name': 'Startups', 'cs_name': 'Startupy'},
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
        logger.warning("⚠️ OPENROUTER_API_KEY není nastaven - články nebudou přeloženy do češtiny")
        openrouter_key = "skip"  # Použít původní texty bez překladu

    logger.info("✅ API klíče jsou nastaveny")
    return news_key, openrouter_key

def detect_category(title, description):
    """Detekuje kategorii článku podle klíčových slov"""
    # Ošetření None hodnot
    title = title or ""
    description = description or ""
    text = f"{title} {description}".lower()

    category_keywords = {
        'ai': [
            # Základní AI termíny
            'ai', 'artificial intelligence', 'machine learning', 'ml', 'neural', 'deep learning', 'llm', 'nlp',
            # Konkrétní modely a firmy (podle marigold.cz obsahu)
            'gpt', 'chatgpt', 'openai', 'anthropic', 'claude', 'gemini', 'mistral', 'deepseek', 'llama', 'grok',
            # AI aplikace
            'reasoning', 'agents', 'automation', 'computer vision', 'robotics', 'humanoid'
        ],
        'programming': [
            # Jazyky a technologie
            'javascript', 'python', 'rust', 'golang', 'typescript', 'java', 'react', 'vue', 'angular',
            # Vývojové nástroje (podle obsahu blogu)
            'framework', 'library', 'code', 'developer', 'programming', 'github', 'cursor', 'copilot',
            'open-source', 'api', 'software development'
        ],
        'hardware': [
            # Procesory a komponenty
            'cpu', 'gpu', 'processor', 'intel', 'amd', 'nvidia', 'chip', 'semiconductor', 'arm', 'quantum computing',
            # Automotive (silná kategorie na blogu)
            'automotive', 'electric vehicle', 'ev', 'tesla', 'autonomous driving', 'lidar'
        ],
        'startups': [
            # Startup ekosystém
            'startup', 'funding', 'investment', 'venture', 'unicorn', 'ipo', 'acquisition', 'founder', 'entrepreneur',
            'crowdfunding', 'kickstarter', 'series a', 'series b', 'exit', 'valuation'
        ],
        'security': [
            # Bezpečnost a soukromí
            'security', 'hack', 'breach', 'vulnerability', 'cyber', 'password', 'encryption', 'privacy',
            'malware', 'ransomware', 'phishing', 'data protection', 'gdpr', 'surveillance'
        ],
        'mobile': [
            # Mobilní technologie (specialita blogu)
            'android', 'ios', 'iphone', 'smartphone', 'mobile', 'app store', 'google play', 'samsung', 'apple',
            # Mobilní sítě (časté téma)
            '5g', '4g', 'lte', 'cellular', 'carrier', 'telecom', 'spectrum', 'antenna'
        ],
        'web': [
            # Web technologie
            'web', 'browser', 'chrome', 'firefox', 'safari', 'html', 'css', 'frontend', 'backend',
            'internet', 'website', 'domain', 'hosting', 'cdn', 'apis', 'cloud'
        ],
        'gaming': [
            # Gaming a zábava
            'gaming', 'game', 'playstation', 'xbox', 'nintendo', 'steam', 'epic', 'esports', 'console',
            'vr', 'ar', 'metaverse', 'virtual reality', 'augmented reality'
        ],
        'crypto': [
            # Kryptoměny a blockchain
            'crypto', 'bitcoin', 'ethereum', 'blockchain', 'nft', 'defi', 'web3', 'mining', 'wallet',
            'stablecoin', 'altcoin', 'dao', 'smart contract'
        ],
        'science': [
            # Věda a výzkum
            'quantum', 'space', 'nasa', 'research', 'discovery', 'experiment', 'study', 'scientific', 'physics',
            'spacex', 'satellite', 'mars', 'climate', 'energy', 'renewable', 'nuclear'
        ]
    }

    for category, keywords in category_keywords.items():
        if any(keyword in text for keyword in keywords):
            return category

    return 'web'  # Default kategorie

def detect_importance(title, description, category):
    """Detekuje důležitost článku na škále 1-5"""
    # Ošetření None hodnot
    title = title or ""
    description = description or ""
    text = f"{title} {description}".lower()

    # Kritická důležitost (5) - průlomy, velké akvizice, bezpečnostní incidenty
    critical_keywords = [
        # Zásadní události
        'breakthrough', 'major', 'massive', 'revolutionary', 'groundbreaking', 'historic',
        'billion', 'acquisition', 'merger', 'ipo', 'goes public', 'bankrupt', 'shutdown', 'discontinued',
        # Bezpečnostní incidenty
        'hack', 'data breach', 'vulnerability', 'cyber attack', 'ransomware attack',
        # AI průlomy (podle obsahu blogu)
        'quantum computing', 'artificial general intelligence', 'agi', 'superintelligence',
        'reasoning breakthrough', 'autonomous', 'humanoid robot'
    ]

    # Vysoká důležitost (4) - významné novinky
    high_keywords = [
        # Nové produkty a verze
        'new', 'first', 'latest', 'update', 'release', 'version', 'launches', 'announces', 'reveals',
        # Byznys
        'investment', 'funding', 'partnership', 'deal', 'series a', 'series b', 'unicorn',
        # Klíčové firmy (podle četnosti na blogu)
        'apple', 'google', 'microsoft', 'meta', 'tesla', 'nvidia', 'amazon', 'spacex',
        'openai', 'anthropic', 'deepseek', 'mistral', 'claude', 'gemini'
    ]

    # Nízká důležitost (2) - spekulace, germy
    low_keywords = [
        'rumors', 'speculation', 'might', 'could', 'reportedly',
        'allegedly', 'sources say', 'leak', 'hint', 'suggests',
        'beta', 'preview', 'concept'
    ]

    # Počet kritických klíčových slov
    critical_count = sum(1 for keyword in critical_keywords if keyword in text)
    high_count = sum(1 for keyword in high_keywords if keyword in text)
    low_count = sum(1 for keyword in low_keywords if keyword in text)

    # Kategorie-specifické váhy (podle analýzy marigold.cz kategorií)
    category_weights = {
        'ai': 1.4,          # AI (234 článků) - nejpopulárnější téma, vysoká váha
        'security': 1.3,    # Bezpečnost (17 článků) - kritické pro tech
        'startups': 1.2,    # Startupy (36 článků) - důležité pro ekosystém
        'mobile': 1.1,      # Mobilní (44+39+20 článků) - specialita autora
        'hardware': 1.1,    # Hardware/Automotive (109 článků) - tech focus
        'programming': 1.0, # Programování (7 článků) - střední váha
        'web': 1.0,         # Web/Internet (112 článků) - základní tech
        'science': 1.2,     # Věda/výzkum - důležité objevy
        'crypto': 0.8,      # Kryptoměny (méně obsahu na blogu)
        'gaming': 0.7       # Gaming (nejméně relevantní pro Marigold)
    }

    # Základní skóre
    if critical_count >= 2:
        base_score = 5
    elif critical_count >= 1:
        base_score = 4
    elif high_count >= 2:
        base_score = 4
    elif high_count >= 1:
        base_score = 3
    elif low_count >= 1:
        base_score = 2
    else:
        base_score = 3  # Střední důležitost

    # Aplikovat kategorijní váhu
    weighted_score = base_score * category_weights.get(category, 1.0)

    # Zaokrouhlit a omezit na rozsah 1-5
    final_score = max(1, min(5, round(weighted_score)))

    return final_score

def fetch_og_image(article_url, timeout=5):
    """Stáhne Open Graph obrázek ze stránky článku"""
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

            # Schema.org image
            schema_image = soup.find('meta', attrs={'itemprop': 'image'})
            if schema_image:
                return schema_image.get('content')

    except Exception as e:
        logger.debug(f"Nelze získat OG image z {article_url}: {e}")

    return None

def translate_with_openrouter(text, api_key, max_retries=3):
    """Přeloží text pomocí OpenRouter API"""
    if not text or not text.strip():
        logger.warning("Prázdný text pro překlad")
        return text

    # Pokud není API klíč nebo je test klíč, vrátit původní text
    if not api_key or api_key == "test-key" or api_key == "skip":
        logger.info("⚠️ OpenRouter překlad přeskočen - použit originální text")
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
    """Získá technologické zprávy z NewsAPI pomocí category=technology"""

    logger.info("🔄 Stahuji zprávy z kategorie technology")

    try:
        response = requests.get('https://newsapi.org/v2/top-headlines',
            params={
                'category': 'technology',
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
        logger.info(f"✅ Načteno {len(articles)} článků z kategorie technology")

        return articles

    except Exception as e:
        logger.error(f"Stahování technologických zpráv selhalo: {e}")
        raise

def create_markdown_file(article, category_info, source_emoji, importance_info, output_dir, article_index):
    """Vytvoří Markdown soubor pro článek"""

    # Vytvoř slug z titulku
    slug = re.sub(r'[^\w\s-]', '', article['czech_title'].lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    slug = slug[:50]  # Omezit délku

    # Datum pro filename
    pub_date = datetime.fromisoformat(article['published_at'].replace('Z', '+00:00'))
    date_str = pub_date.strftime('%Y-%m-%d')

    filename = f"{date_str}-{article_index:02d}-{slug}.md"
    filepath = output_dir / filename

    # Front matter podle tech_news_article layoutu
    front_matter = {
        'layout': 'tech_news_article',
        'title': article['czech_title'],
        'original_title': article['title'],
        'description': article['czech_description'],
        'publishedAt': article['published_at'],
        'date': pub_date.strftime('%Y-%m-%d %H:%M:%S'),
        'url': article['url'],
        'urlToImage': article.get('url_to_image'),
        'category': category_info['name'].lower(),
        'importance': article['importance'],
        'source': {
            'name': article['source']['name'],
            'id': article['source'].get('id', ''),
            'emoji': source_emoji
        }
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

                # Detekce důležitosti
                importance_level = detect_importance(article['title'], article.get('description', ''), category_key)
                importance_info = IMPORTANCE_LEVELS[importance_level]

                logger.info(f"🎯 Důležitost: {importance_info['emoji']} {importance_info['name']} ({importance_level}/5)")

                # Emoji pro zdroj
                source_id = article.get('source', {}).get('id', '').lower()
                source_emoji = SOURCE_EMOJIS.get(source_id, '💡')

                # Překlad
                czech_title = translate_with_openrouter(article['title'], openrouter_api_key)
                czech_description = ''

                # Ověření a překlad description
                description = article.get('description')
                if description and description != '[Removed]':
                    czech_description = translate_with_openrouter(description, openrouter_api_key)
                else:
                    # Použít content jako náhradní description
                    content = article.get('content', '')
                    if content and content != '[Removed]':
                        # Zkrátit content na první větu
                        short_content = content.split('.')[0] + '.' if '.' in content else content[:200]
                        czech_description = translate_with_openrouter(short_content, openrouter_api_key)
                    else:
                        czech_description = ''

                # Získat obrázek - nejdříve z NewsAPI, pak OG jako fallback
                image_url = article.get('urlToImage')
                if not image_url and article['url']:
                    logger.info(f"🖼️ Získávám OG obrázek z {article['url'][:50]}...")
                    image_url = fetch_og_image(article['url'])

                # Příprava článku
                processed_article = {
                    'title': article['title'] or 'Bez názvu',
                    'czech_title': czech_title or article['title'] or 'Bez názvu',
                    'description': description or '',
                    'czech_description': czech_description or description or '',
                    'url': article['url'],
                    'source': article['source'],
                    'published_at': article['publishedAt'],
                    'url_to_image': image_url,
                    'importance': importance_level
                }

                # Vytvoření Markdown souboru
                create_markdown_file(processed_article, category_info, source_emoji, importance_info, output_dir, processed_count + 1)
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