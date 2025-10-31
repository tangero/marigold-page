#!/usr/bin/env python3
"""
Generate tech-news manifest JSON

Vytvoří kompaktní JSON soubor s metadaty článků pro rychlé načítání
hlavní stránky /tech-news/. Jekyll není potřeba načítat všechny články.

Output: tech-news/manifest.json
"""

import json
import yaml
import re
from pathlib import Path
from datetime import datetime, timezone
import sys


def extract_front_matter(file_path):
    """Extrahuje jen front matter z markdown souboru (bez načítání celého obsahu)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Zkontrolovat, že začína s ---
        if not content.startswith('---'):
            return None

        # Rozdělit podle ---
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None

        # Parsovat YAML front matter
        front_matter = yaml.safe_load(parts[1])
        return front_matter

    except Exception as e:
        print(f"⚠️  Chyba při čtení {file_path.name}: {e}", file=sys.stderr)
        return None


def generate_manifest(limit=200):
    """
    Generuje manifest.json s metadaty tech-news článků

    Args:
        limit (int): Maximální počet článků v manifestu (nejnovější)

    Returns:
        dict: Manifest data
    """
    tech_news_dir = Path('_tech_news')

    if not tech_news_dir.exists():
        print(f"❌ Adresář {tech_news_dir} neexistuje", file=sys.stderr)
        return None

    print(f"📁 Načítám články z: {tech_news_dir}")

    articles = []
    skipped = 0

    # Seřadit soubory podle jména (obsahuje datum) - nejnovější první
    md_files = sorted(tech_news_dir.glob('*.md'), reverse=True)

    for article_file in md_files:
        # Přeskočit index.md
        if article_file.name == 'index.md':
            continue

        # Extrahovat front matter
        front_matter = extract_front_matter(article_file)
        if not front_matter:
            skipped += 1
            continue

        # Sestavit URL k článku
        # _tech_news/ články mají layout tech_news_article s vlastním permalink
        article_url = front_matter.get('permalink')
        if not article_url:
            # Fallback na generované URL z collection
            # Format: /tech-news/YYYY-MM-DD/slug/
            date_match = re.match(r'(\d{4}-\d{2}-\d{2})-', article_file.name)
            if date_match:
                date_str = date_match.group(1)
                slug = front_matter.get('slug', article_file.stem)
                article_url = f"/tech-news/{date_str}/{slug}/"
            else:
                print(f"⚠️  Nelze určit URL pro: {article_file.name}", file=sys.stderr)
                skipped += 1
                continue

        # Vytvoří záznam článku
        article_data = {
            'title': front_matter.get('title', 'Bez názvu'),
            'description': front_matter.get('description', ''),
            'slug': front_matter.get('slug', article_file.stem),
            'publishedAt': front_matter.get('publishedAt'),
            'date': front_matter.get('date'),
            'importance': front_matter.get('importance', 3),
            'category': front_matter.get('category', 'technology'),
            'urlToImage': front_matter.get('urlToImage'),
            'url': article_url,
            'source': front_matter.get('source', {}),
            'companies': front_matter.get('companies', []),
            'people': front_matter.get('people', [])
        }

        articles.append(article_data)

        # Omezit na limit
        if len(articles) >= limit:
            break

    print(f"✅ Načteno: {len(articles)} článků")
    if skipped > 0:
        print(f"⚠️  Přeskočeno: {skipped} souborů")

    # Seřadit podle publishedAt (nejnovější první)
    articles.sort(key=lambda x: x.get('publishedAt', ''), reverse=True)

    # Vytvořit manifest
    manifest = {
        'generated': datetime.now(timezone.utc).isoformat(),
        'count': len(articles),
        'articles': articles
    }

    return manifest


def save_manifest(manifest, output_path='tech-news/manifest.json'):
    """Uloží manifest do JSON souboru"""
    output_file = Path(output_path)

    # Vytvořit adresář pokud neexistuje
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Zapsat JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    # Vypsat statistiky
    file_size = output_file.stat().st_size
    file_size_kb = file_size / 1024

    print(f"\n📄 Manifest uložen: {output_file}")
    print(f"   Velikost: {file_size_kb:.1f} KB")
    print(f"   Články: {manifest['count']}")

    return output_file


def main():
    """Hlavní funkce"""
    print("🔧 Tech-News Manifest Generator")
    print("=" * 60)

    # Generovat manifest (posledních 200 článků)
    manifest = generate_manifest(limit=200)

    if not manifest:
        print("\n❌ Chyba při generování manifestu", file=sys.stderr)
        return 1

    # Uložit do souboru
    output_file = save_manifest(manifest)

    print("\n" + "=" * 60)
    print("✅ Hotovo!")
    print("\nManifest je připraven pro použití na /tech-news/")
    print(f"Jekyll NEPOTŘEBUJE načítat {manifest['count']} článků - použije jen tento JSON.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
