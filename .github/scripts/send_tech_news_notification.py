#!/usr/bin/env python3
"""
Odešle push notifikaci přes OneSignal API když jsou přidány nové tech-news články.
"""

import os
import json
import requests
import sys
from datetime import datetime
from pathlib import Path
import yaml


def get_latest_tech_news_articles(limit=3):
    """Najde nejnověji přidané tech-news články."""
    tech_news_dir = Path("_tech_news")

    if not tech_news_dir.exists():
        print("❌ _tech_news adresář nenalezen")
        return []

    # Získat všechny markdown soubory seřazené podle času úpravy (nejnověji první)
    articles = sorted(
        tech_news_dir.glob("*.md"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if not articles:
        print("❌ Žádné články nenalezeny v _tech_news")
        return []

    # Vrátit jen nejnovější články
    return articles[:limit]


def extract_article_metadata(article_path):
    """Extrahuje metadata z tech-news články (title, description, category)."""
    try:
        with open(article_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extrahovat front matter
        if not content.startswith('---'):
            print(f"❌ Neplatný formát článku v {article_path}")
            return None

        # Rozdělit na front matter a obsah
        parts = content.split('---', 2)
        if len(parts) < 2:
            print(f"❌ Nepodařilo se parsovat front matter v {article_path}")
            return None

        # Parsovat YAML front matter
        try:
            frontmatter = yaml.safe_load(parts[1])
        except yaml.YAMLError as e:
            print(f"❌ Chyba parsování YAML v {article_path}: {e}")
            return None

        if not frontmatter:
            print(f"❌ Prázdný front matter v {article_path}")
            return None

        # Extrahovat potřebná pole
        title = frontmatter.get('title', 'Bez názvu')
        description = frontmatter.get('description', frontmatter.get('summary', title))
        category = frontmatter.get('category', 'tech')
        source = frontmatter.get('source', {})
        source_name = source.get('name', 'NewsAPI') if isinstance(source, dict) else 'NewsAPI'
        source_emoji = source.get('emoji', '📰') if isinstance(source, dict) else '📰'

        return {
            'title': title,
            'description': description,
            'category': category,
            'source': source_name,
            'source_emoji': source_emoji,
            'filename': article_path.name
        }
    except Exception as e:
        print(f"❌ Chyba při parsování článku: {e}")
        return None


def send_onesignal_notification(title, message, category="tech", source_emoji="📰"):
    """Pošle notifikaci přes OneSignal REST API."""
    api_key = os.getenv('ONESIGNAL_REST_API_KEY')
    app_id = os.getenv('ONESIGNAL_APP_ID')

    if not api_key or not app_id:
        print("❌ Chybí ONESIGNAL_REST_API_KEY nebo ONESIGNAL_APP_ID v prostředí")
        return False

    # OneSignal API endpoint
    url = "https://onesignal.com/api/v1/notifications"

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {api_key}"
    }

    # Payload pro notifikaci
    payload = {
        "app_id": app_id,
        "included_segments": ["All"],  # Poslat všem subscribovaným uživatelům
        "headings": {"cs": title},
        "contents": {"cs": message},
        "big_picture": "",  # Lze přidat featured image URL
        "chrome_web_icon": "",  # Lze přidat icon URL
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        if response.status_code in [200, 201]:
            result = response.json()
            notification_id = result.get('body', {}).get('id', 'unknown')
            print(f"✅ Notifikace úspěšně poslána! ID: {notification_id}")
            return True
        else:
            print(f"❌ Selhalo odesílání notifikace. Status: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except requests.exceptions.Timeout:
        print("❌ Timeout při odesílání notifikace")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Chyba požadavku: {e}")
        return False
    except json.JSONDecodeError:
        print("❌ Neplatná JSON odpověď z OneSignal API")
        return False


def check_tech_news_changes():
    """Zkontroluje, zda jsou změny v _tech_news adresáři."""
    try:
        # Získat poslední commit změněné soubory
        result = os.popen(
            'git diff --name-only HEAD~1 HEAD 2>/dev/null || git diff --name-only --cached 2>/dev/null'
        ).read()
        changed_files = result.strip().split('\n') if result.strip() else []

        # Filtrovat pro _tech_news soubory
        tech_news_changes = [f for f in changed_files if f.startswith('_tech_news/')]

        if not tech_news_changes:
            print("⚠️ Žádné změny v _tech_news/ adresáři detekovány")
            return False

        print(f"✅ Nalezeny změny v _tech_news/: {len(tech_news_changes)} soubory")
        for file in tech_news_changes:
            print(f"  - {file}")

        return True
    except Exception as e:
        print(f"⚠️ Nepodařilo se zkontrolovat git změny: {e}")
        # Fallback - povolit notifikaci, pokud se nedá zkontrolovat
        return True


def main():
    """Hlavní funkce."""
    print("🔔 OneSignal Tech News Notification Sender")
    print(f"⏰ Čas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    # Zkontrolovat, zda se jedná o změnu v _tech_news
    if not check_tech_news_changes():
        print("⚠️ Přeskakuji notifikaci - žádné změny tech-news")
        return 0

    # Získat nejnovější tech-news články
    latest_articles = get_latest_tech_news_articles(limit=1)
    if not latest_articles:
        print("⚠️ Žádné články k upozornění. Ukončuji.")
        return 0

    print(f"📝 Počet nových článků: {len(latest_articles)}")

    # Zpracovat každý článek a poslat notifikaci
    success_count = 0

    for article_path in latest_articles:
        print(f"\n📰 Zpracovávám článek: {article_path.name}")

        # Extrahovat metadata
        metadata = extract_article_metadata(article_path)
        if not metadata:
            print(f"❌ Selhalo extrahování metadat")
            continue

        print(f"📰 Titulek: {metadata['title']}")
        print(f"📂 Kategorie: {metadata['category']}")
        print(f"🔗 Zdroj: {metadata['source_emoji']} {metadata['source']}")
        print("-" * 50)

        # Zkrátit popis na 200 znaků
        description = metadata['description']
        if len(description) > 200:
            description = description[:197] + "..."

        # Poslat notifikaci
        notification_title = f"🆕 Tech zpráva: {metadata['title'][:40]}"
        notification_message = f"{metadata['source_emoji']} {metadata['category'].upper()}: {description}"

        success = send_onesignal_notification(
            title=notification_title,
            message=notification_message,
            category=metadata['category'],
            source_emoji=metadata['source_emoji']
        )

        if success:
            success_count += 1

    print("\n" + "=" * 50)
    if success_count > 0:
        print(f"✅ Úspěšně odesláno {success_count} notifikací")
        return 0
    else:
        print("❌ Nepodařilo se odeslat žádné notifikace")
        return 1


if __name__ == "__main__":
    sys.exit(main())
