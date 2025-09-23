#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
import logging
from dotenv import load_dotenv
from fetch_tech_news_advanced import RSSNewsManager

# Načíst .env soubor
load_dotenv()

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TechNewsWithImagesGenerator:
    """Generátor tech-news s robustním získáváním obrázků"""

    def __init__(self):
        self.rss_manager = RSSNewsManager()
        self.output_dir = Path('_tech_news')
        self.output_dir.mkdir(exist_ok=True)

    def create_jekyll_article(self, article, article_index):
        """Vytvoří Jekyll článek s optimalizovaným front matter"""

        # Vytvořit slug z titulku
        slug = self.create_slug(article['title'])

        # Datum pro filename
        pub_date = datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00'))
        date_str = pub_date.strftime('%Y-%m-%d')

        filename = f"{date_str}-{slug}.md"
        filepath = self.output_dir / filename

        # Převést na český titulek a popis (pokud možno)
        czech_title = self.translate_title(article['title'])
        czech_description = self.translate_description(article.get('description', ''))

        # Detekce kategorie a důležitosti
        category = self.detect_category(article['title'], article.get('description', ''))
        importance = self.detect_importance(article['title'], article.get('description', ''), category)

        # Front matter podle tech_news_article layoutu
        front_matter = {
            'layout': 'tech_news_article',
            'title': czech_title,
            'original_title': article['title'],
            'slug': slug,  # Explicitní slug bez číslování
            'description': czech_description,
            'publishedAt': article['publishedAt'],
            'date': pub_date.strftime('%Y-%m-%d %H:%M:%S'),
            'url': article['url'],
            'urlToImage': article.get('urlToImage'),  # Nyní by měl být naplněn
            'category': category,
            'importance': importance,
            'source': article['source']
        }

        # Vytvořit obsah
        content = f"""---
{yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)}---

{czech_description}

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
        return slug[:50]  # Omezit délku

    def translate_title(self, title):
        """Přeloží titulek (placeholder - implementovat později)"""
        # Pro nyní jen vrátíme originální
        return title

    def translate_description(self, description):
        """Přeloží popis (placeholder - implementovat později)"""
        # Pro nyní jen vrátíme originální
        return description or ''

    def detect_category(self, title, description):
        """Detekuje kategorii článku"""
        text = f"{title} {description}".lower()

        category_keywords = {
            'ai': ['ai', 'artificial intelligence', 'machine learning', 'gpt', 'chatgpt', 'openai', 'claude'],
            'startups': ['startup', 'funding', 'investment', 'venture', 'unicorn', 'ipo'],
            'programming': ['javascript', 'python', 'code', 'developer', 'programming', 'github'],
            'hardware': ['cpu', 'gpu', 'processor', 'chip', 'semiconductor'],
            'security': ['security', 'hack', 'breach', 'vulnerability', 'cyber'],
            'mobile': ['android', 'ios', 'iphone', 'smartphone', 'mobile', '5g'],
        }

        for category, keywords in category_keywords.items():
            if any(keyword in text for keyword in keywords):
                return category

        return 'web'  # Default

    def detect_importance(self, title, description, category):
        """Detekuje důležitost článku"""
        text = f"{title} {description}".lower()

        # Vysoká důležitost
        if any(word in text for word in ['breakthrough', 'major', 'billion', 'acquisition']):
            return 5

        # Střední-vysoká důležitost
        if any(word in text for word in ['new', 'launches', 'announces', 'first']):
            return 4

        # Nízká důležitost
        if any(word in text for word in ['rumors', 'might', 'reportedly']):
            return 2

        return 3  # Default

    def clean_old_articles(self):
        """Vyčistí staré články"""
        for old_file in self.output_dir.glob('*.md'):
            if old_file.name != 'index.md':  # Zachovat index
                old_file.unlink()
        logger.info("🧹 Vyčištěn starý obsah")

    def generate_tech_news(self):
        """Hlavní funkce pro generování tech-news"""
        logger.info("🚀 Spouští se generování tech-news s obrázky")

        # Vyčistit starý obsah
        self.clean_old_articles()

        # Získat články z RSS
        articles = self.rss_manager.fetch_all_articles()

        if not articles:
            logger.error("❌ Žádné články nenalezeny")
            return False

        logger.info(f"📰 Zpracovávám {len(articles)} článků...")

        processed_count = 0

        for i, article in enumerate(articles, 1):
            try:
                # Přeskočit články bez obsahu
                if not article.get('title'):
                    logger.warning(f"⏭️ Přeskakuji článek {i} - chybí titulek")
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

        # Vytvoření index stránky
        self.create_index_page(processed_count)

        return True

    def create_index_page(self, article_count):
        """Vytvoří index stránku tech-news"""
        index_content = f"""---
layout: tech_news_index
title: Technologické zprávy
permalink: /tech-news/
description: Nejnovější zprávy ze světa technologií s obrázky z předních světových zdrojů
---

# Technologické zprávy

Automaticky aktualizované zprávy ze světa technologií z předních světových zdrojů, s obrázky a přeložené do češtiny.

**Celkem článků:** {article_count}
**Poslední aktualizace:** {datetime.now(timezone.utc).strftime('%d.%m.%Y %H:%M UTC')}

## Zdroje

Články jsou získávány z RSS feedů těchto zdrojů:
- 🚀 **TechCrunch** - startupy a investice
- ⚡ **The Verge** - technologie a hardware
- 🔬 **Ars Technica** - hloubkové analýzy
- 🔧 **Wired** - technologie a společnost
- 🤖 **OpenAI Blog** - AI průlomy
"""

        index_path = self.output_dir / 'index.md'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)

        logger.info("✅ Index stránka vytvořena")

def main():
    """Hlavní funkce"""
    generator = TechNewsWithImagesGenerator()

    # Zkontrolovat, zda je RSS manager správně nakonfigurován
    stats = generator.rss_manager.get_stats()
    logger.info(f"📊 RSS Manager - aktivní zdroje: {stats['enabled_sources']}/{stats['total_sources']}")

    # Generovat tech-news
    success = generator.generate_tech_news()

    if success:
        logger.info("🎉 Generování tech-news dokončeno")
    else:
        logger.error("💥 Generování tech-news selhalo")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())