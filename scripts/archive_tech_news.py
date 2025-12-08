#!/usr/bin/env python3
"""
Archivační skript pro tech_news - převádí staré články na statické HTML.

Použití:
    python scripts/archive_tech_news.py [--days 50] [--dry-run]

Články starší než zadaný počet dní jsou:
1. Převedeny na statické HTML s inline CSS
2. Přesunuty do tech-news-archive/
3. Smazány z _tech_news/ (Jekyll kolekce)

Výsledek: Jekyll zpracovává jen čerstvé články, build je rychlejší.
"""

import os
import sys
import yaml
import shutil
import argparse
import markdown
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Tuple, Dict, List

# Absolutní cesta k rootu projektu
PROJECT_ROOT = Path(__file__).parent.parent
TECH_NEWS_DIR = PROJECT_ROOT / "_tech_news"
ARCHIVE_DIR = PROJECT_ROOT / "tech-news-archive"

# HTML šablona pro archivované články
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Marigold.cz Tech News</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://www.marigold.cz/tech-news/{date_path}/{slug}/">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #374151; background: #f3f4f6; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 2rem; }}
        .tech-news-article {{ background: white; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); padding: 2rem; margin: 2rem 0; }}
        .source-info {{ display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem; flex-wrap: wrap; }}
        .source-emoji {{ font-size: 1.5rem; }}
        .source-name {{ font-weight: 600; color: #374151; }}
        .importance-indicator {{ display: flex; gap: 2px; margin-left: auto; }}
        .star {{ color: #fbbf24; font-size: 1.2rem; }}
        .star.empty {{ color: #d1d5db; }}
        .article-title {{ font-size: 2rem; font-weight: 700; line-height: 1.2; margin-bottom: 1rem; color: #111827; }}
        .article-meta {{ display: flex; align-items: center; gap: 1rem; font-size: 0.875rem; color: #6b7280; margin-bottom: 1.5rem; }}
        .category {{ padding: 0.25rem 0.75rem; border-radius: 1rem; font-weight: 500; font-size: 0.75rem; text-transform: uppercase; background: #e5e7eb; color: #374151; }}
        .article-image {{ margin: 1.5rem 0; border-radius: 8px; overflow: hidden; }}
        .article-image img {{ width: 100%; height: auto; display: block; }}
        .article-content {{ font-size: 1.125rem; line-height: 1.7; margin-bottom: 2rem; }}
        .article-content h2 {{ font-size: 1.5rem; margin: 1.5rem 0 1rem; color: #111827; }}
        .article-content p {{ margin-bottom: 1rem; }}
        .article-footer {{ border-top: 1px solid #e5e7eb; padding-top: 1.5rem; }}
        .read-more-btn {{ display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.75rem 1.5rem; background: #3b82f6; color: white; text-decoration: none; border-radius: 8px; font-weight: 500; }}
        .read-more-btn:hover {{ background: #2563eb; }}
        .original-title {{ margin-top: 1rem; color: #6b7280; font-size: 0.875rem; }}
        .back-link {{ display: inline-block; margin-bottom: 1rem; color: #3b82f6; text-decoration: none; }}
        .back-link:hover {{ text-decoration: underline; }}
        .archive-notice {{ background: #fef3c7; border: 1px solid #f59e0b; border-radius: 8px; padding: 1rem; margin-bottom: 1rem; font-size: 0.875rem; color: #92400e; }}
        @media (max-width: 640px) {{
            .container {{ padding: 1rem; }}
            .tech-news-article {{ padding: 1.5rem; margin: 1rem 0; }}
            .article-title {{ font-size: 1.5rem; }}
            .source-info {{ flex-direction: column; align-items: flex-start; }}
            .importance-indicator {{ margin-left: 0; margin-top: 0.5rem; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="/tech-news/" class="back-link">&larr; Zpět na Tech News</a>

        <div class="archive-notice">
            Tento článek je z archivu. Byl publikován {published_date}.
        </div>

        <article class="tech-news-article">
            <header>
                <div class="source-info">
                    <span class="source-emoji">{source_emoji}</span>
                    <span class="source-name">{source_name}</span>
                    <div class="importance-indicator">
                        {stars}
                    </div>
                </div>

                <h1 class="article-title">{title}</h1>

                <div class="article-meta">
                    <time datetime="{published_at}">{published_date}</time>
                    <span class="category">{category}</span>
                </div>
            </header>

            {image_html}

            <div class="article-content">
                {content}
            </div>

            <footer class="article-footer">
                <a href="{original_url}" target="_blank" rel="noopener" class="read-more-btn">
                    Číst původní článek &rarr;
                </a>

                {original_title_html}
            </footer>
        </article>

        <p style="text-align: center; color: #6b7280; font-size: 0.875rem; margin-top: 2rem;">
            &copy; {year} <a href="https://www.marigold.cz" style="color: #3b82f6;">Marigold.cz</a>
        </p>
    </div>
</body>
</html>
"""


def parse_frontmatter(content: str) -> Tuple[dict, str]:
    """Parsuje YAML front matter z markdown souboru."""
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    try:
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2].strip()
        return frontmatter or {}, body
    except yaml.YAMLError:
        return {}, content


def generate_stars(importance: int) -> str:
    """Generuje HTML pro hvězdičky důležitosti."""
    stars = []
    for i in range(1, 6):
        if i <= importance:
            stars.append('<span class="star">★</span>')
        else:
            stars.append('<span class="star empty">☆</span>')
    return ''.join(stars)


def convert_to_html(md_path: Path) -> Tuple[str, str, str]:
    """
    Převede markdown článek na statické HTML.
    Vrací (html_content, date_path, slug).
    """
    content = md_path.read_text(encoding='utf-8')
    frontmatter, body = parse_frontmatter(content)

    # Extrahuj metadata
    title = frontmatter.get('title', 'Bez názvu')
    description = frontmatter.get('description', '')[:160]
    category = frontmatter.get('category', 'tech')
    importance = frontmatter.get('importance', 3)
    original_title = frontmatter.get('original_title', '')
    original_url = frontmatter.get('url', '#')
    published_at = frontmatter.get('publishedAt', '')
    url_to_image = frontmatter.get('urlToImage', '')
    source = frontmatter.get('source', {})
    source_emoji = source.get('emoji', '📰') if isinstance(source, dict) else '📰'
    source_name = source.get('name', 'Unknown') if isinstance(source, dict) else 'Unknown'
    slug = frontmatter.get('slug', md_path.stem)

    # Parsuj datum
    date_str = frontmatter.get('date', '')
    if isinstance(date_str, str):
        try:
            date_obj = datetime.strptime(date_str.split()[0], '%Y-%m-%d')
        except ValueError:
            date_obj = datetime.now()
    else:
        date_obj = date_str if isinstance(date_str, datetime) else datetime.now()

    date_path = date_obj.strftime('%Y-%m-%d')
    published_date = date_obj.strftime('%d.%m.%Y')

    # Konvertuj markdown na HTML
    md = markdown.Markdown(extensions=['extra', 'smarty'])
    content_html = md.convert(body)

    # Obrázek
    image_html = ''
    if url_to_image:
        image_html = f'''
            <div class="article-image">
                <img src="{url_to_image}" alt="{title}" loading="lazy">
            </div>
        '''

    # Původní název
    original_title_html = ''
    if original_title and original_title != title:
        original_title_html = f'<div class="original-title"><small>Původní název: {original_title}</small></div>'

    # Sestavení HTML
    html = HTML_TEMPLATE.format(
        title=title,
        description=description,
        date_path=date_path,
        slug=slug,
        source_emoji=source_emoji,
        source_name=source_name,
        stars=generate_stars(importance),
        published_at=published_at,
        published_date=published_date,
        category=category,
        image_html=image_html,
        content=content_html,
        original_url=original_url,
        original_title_html=original_title_html,
        year=datetime.now().year
    )

    return html, date_path, slug


def get_article_date(md_path: Path) -> Optional[datetime]:
    """Extrahuje datum článku z front matter."""
    try:
        content = md_path.read_text(encoding='utf-8')
        frontmatter, _ = parse_frontmatter(content)
        date_str = frontmatter.get('date', '')

        if isinstance(date_str, str):
            return datetime.strptime(date_str.split()[0], '%Y-%m-%d')
        elif isinstance(date_str, datetime):
            return date_str
    except Exception:
        pass

    # Fallback: parsuj z názvu souboru
    try:
        date_part = md_path.name[:10]  # 2025-10-19
        return datetime.strptime(date_part, '%Y-%m-%d')
    except ValueError:
        return None


def archive_old_articles(days: int = 50, dry_run: bool = False) -> dict:
    """
    Archivuje články starší než zadaný počet dní.

    Args:
        days: Počet dní - starší články budou archivovány
        dry_run: Pokud True, pouze simuluje bez změn

    Returns:
        Statistiky archivace
    """
    cutoff_date = datetime.now() - timedelta(days=days)

    stats = {
        'total_articles': 0,
        'archived': 0,
        'kept': 0,
        'errors': 0,
        'archived_files': []
    }

    if not TECH_NEWS_DIR.exists():
        print(f"Chyba: Adresář {TECH_NEWS_DIR} neexistuje!")
        return stats

    # Vytvoř archivní adresář
    if not dry_run:
        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Projdi všechny markdown soubory
    md_files = list(TECH_NEWS_DIR.glob('*.md'))
    stats['total_articles'] = len(md_files)

    print(f"Nalezeno {len(md_files)} článků v _tech_news/")
    print(f"Archivuji články starší než {days} dní (před {cutoff_date.strftime('%Y-%m-%d')})")
    print("-" * 60)

    for md_path in md_files:
        article_date = get_article_date(md_path)

        if article_date is None:
            print(f"⚠️  Nelze určit datum: {md_path.name}")
            stats['errors'] += 1
            continue

        if article_date >= cutoff_date:
            # Článek je čerstvý, necháme v Jekyll kolekci
            stats['kept'] += 1
            continue

        # Článek je starý, archivujeme
        try:
            html_content, date_path, slug = convert_to_html(md_path)

            # Cílový adresář: tech-news-archive/2025-10-19/slug/
            target_dir = ARCHIVE_DIR / date_path / slug
            target_file = target_dir / "index.html"

            if dry_run:
                print(f"📦 [DRY-RUN] Archivoval bych: {md_path.name} -> {target_file.relative_to(PROJECT_ROOT)}")
            else:
                target_dir.mkdir(parents=True, exist_ok=True)
                target_file.write_text(html_content, encoding='utf-8')
                md_path.unlink()  # Smaž původní .md soubor
                print(f"✅ Archivováno: {md_path.name}")

            stats['archived'] += 1
            stats['archived_files'].append(str(md_path.name))

        except Exception as e:
            print(f"❌ Chyba při archivaci {md_path.name}: {e}")
            stats['errors'] += 1

    return stats


def main():
    parser = argparse.ArgumentParser(
        description='Archivuje staré tech_news články do statického HTML'
    )
    parser.add_argument(
        '--days',
        type=int,
        default=50,
        help='Články starší než tento počet dní budou archivovány (default: 50)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Pouze simulace - nezapisuje žádné změny'
    )

    args = parser.parse_args()

    print("=" * 60)
    print("ARCHIVACE TECH NEWS")
    print("=" * 60)

    if args.dry_run:
        print("🔍 REŽIM DRY-RUN - žádné změny nebudou provedeny\n")

    stats = archive_old_articles(days=args.days, dry_run=args.dry_run)

    print("\n" + "=" * 60)
    print("SOUHRN")
    print("=" * 60)
    print(f"Celkem článků:    {stats['total_articles']}")
    print(f"Archivováno:      {stats['archived']}")
    print(f"Ponecháno:        {stats['kept']}")
    print(f"Chyby:            {stats['errors']}")

    if stats['archived'] > 0:
        remaining = stats['total_articles'] - stats['archived']
        print(f"\nPo archivaci bude v _tech_news/ pouze {remaining} článků.")
        print("Jekyll build by měl být výrazně rychlejší.")


if __name__ == '__main__':
    main()
