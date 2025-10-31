#!/usr/bin/env python3
"""
Cleanup starých tech-news článků

Ponechá pouze články za posledních N dní (výchozí: 7).
Starší články jsou smazány, aby se snížila velikost kolekce
a zrychlil Jekyll build.

Usage:
    python cleanup_old_tech_news.py                 # Ponechá 7 dní
    python cleanup_old_tech_news.py --days 14       # Ponechá 14 dní
"""

import sys
import re
from pathlib import Path
from datetime import datetime, timedelta, timezone
import argparse


def cleanup_old_articles(days_to_keep=7, dry_run=False):
    """
    Smaže tech-news články starší než N dní

    Args:
        days_to_keep (int): Počet dní, které se mají ponechat
        dry_run (bool): Pokud True, jen vypíše co by se smazalo (nemazat)

    Returns:
        tuple: (počet_smazaných, počet_ponechaných)
    """
    tech_news_dir = Path('_tech_news')

    if not tech_news_dir.exists():
        print(f"❌ Adresář {tech_news_dir} neexistuje")
        return 0, 0

    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_to_keep)

    print(f"🗓️  Cutoff datum: {cutoff_date.strftime('%Y-%m-%d')}")
    print(f"📁 Prohledávám: {tech_news_dir}")
    print("-" * 60)

    removed_count = 0
    kept_count = 0
    skipped_count = 0

    for article_file in sorted(tech_news_dir.glob('*.md')):
        # Přeskočit index.md
        if article_file.name == 'index.md':
            skipped_count += 1
            continue

        # Extrahovat datum z názvu souboru (YYYY-MM-DD-...)
        match = re.match(r'(\d{4}-\d{2}-\d{2})-', article_file.name)
        if not match:
            print(f"⚠️  Přeskakuji (neplatný formát): {article_file.name}")
            skipped_count += 1
            continue

        try:
            article_date = datetime.fromisoformat(match.group(1)).replace(tzinfo=timezone.utc)
        except ValueError:
            print(f"⚠️  Přeskakuji (chybné datum): {article_file.name}")
            skipped_count += 1
            continue

        if article_date < cutoff_date:
            if dry_run:
                print(f"🗑️  Smazal bych: {article_file.name} ({article_date.strftime('%Y-%m-%d')})")
            else:
                article_file.unlink()
                print(f"🗑️  Smazáno: {article_file.name}")
            removed_count += 1
        else:
            kept_count += 1

    print("-" * 60)
    print(f"✅ Cleanup {'simulace' if dry_run else 'dokončen'}")
    print(f"   📊 Statistiky:")
    print(f"      Smazáno: {removed_count} článků")
    print(f"      Ponecháno: {kept_count} článků")
    print(f"      Přeskočeno: {skipped_count} souborů")
    print(f"   📏 Redukce: {removed_count / (removed_count + kept_count) * 100:.1f}%" if (removed_count + kept_count) > 0 else "")

    return removed_count, kept_count


def main():
    parser = argparse.ArgumentParser(
        description='Cleanup starých tech-news článků',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Příklady:
  python cleanup_old_tech_news.py                    # Ponechá 7 dní
  python cleanup_old_tech_news.py --days 14          # Ponechá 14 dní
  python cleanup_old_tech_news.py --days 7 --dry-run # Simulace (nemazat)
        """
    )

    parser.add_argument(
        '--days',
        type=int,
        default=7,
        help='Počet dní, které se mají ponechat (výchozí: 7)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simulace - vypsat co by se smazalo, ale nemazat'
    )

    args = parser.parse_args()

    if args.days < 1:
        print("❌ Počet dní musí být alespoň 1")
        return 1

    if args.dry_run:
        print("🔍 DRY RUN - žádné soubory nebudou smazány")
        print()

    removed, kept = cleanup_old_articles(days_to_keep=args.days, dry_run=args.dry_run)

    # Exit code pro CI/CD
    if not args.dry_run and removed == 0 and kept == 0:
        print("\n⚠️  Žádné články nenalezeny!")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
