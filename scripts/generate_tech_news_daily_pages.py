#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generátor denních archivních stránek pro tech-news
Vytvoří stránku pro každý den, kde existují články
"""

import os
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def generate_daily_pages():
    """Generuje stránky pro každý den s články"""

    # Cesty
    tech_news_dir = Path('_tech_news')
    pages_dir = Path('tech-news')

    if not tech_news_dir.exists():
        print("⚠️ Adresář _tech_news neexistuje")
        return

    # Smazat staré denní stránky
    if pages_dir.exists():
        # Smazat pouze denní stránky (formát YYYY-MM-DD)
        for file in pages_dir.glob('*/index.md'):
            parent = file.parent.name
            if len(parent) == 10 and parent[4] == '-' and parent[7] == '-':
                try:
                    file.unlink()
                    file.parent.rmdir()
                    print(f"🗑️ Smazána stará stránka: {parent}")
                except:
                    pass

    # Načíst všechny články a seskupit podle data
    articles_by_date = defaultdict(list)

    for article_file in tech_news_dir.glob('*.md'):
        with open(article_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extrahovat front matter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    front_matter = yaml.safe_load(parts[1])

                    # Získat datum z publishedAt nebo date
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
                    print(f"⚠️ Chyba při zpracování {article_file.name}: {e}")

    # Vytvořit stránku pro každý den
    created_count = 0
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
<!-- Layout tech_news_day se postará o zobrazení článků -->
"""

        # Zapsat soubor
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)

        created_count += 1
        print(f"✅ Vytvořena stránka pro {date_str} ({len(articles)} článků)")

    print(f"\n🎉 Celkem vytvořeno {created_count} denních stránek")

    # Vytvořit hlavní index.md pokud neexistuje
    main_index = pages_dir / 'index.md'
    if not main_index.exists():
        main_content = """---
layout: tech_news_index
title: Technologické zprávy
permalink: /tech-news/
---

<!-- Hlavní stránka tech-news zobrazující nejnovější články -->
"""
        with open(main_index, 'w', encoding='utf-8') as f:
            f.write(main_content)
        print("✅ Vytvořena hlavní index stránka")

if __name__ == "__main__":
    generate_daily_pages()