#!/usr/bin/env python3
"""
Test OneSignal notifikací
"""

import os
import requests
from pathlib import Path

def test_onesignal_credentials():
    """Zkontrolovat OneSignal přihlašovací údaje"""
    print("🔐 Kontrola OneSignal přihlašovacích údajů")
    print("=" * 60)

    # Zkontrolovat proměnné prostředí
    api_key = os.getenv('ONESIGNAL_REST_API_KEY')
    marigold_app_id = os.getenv('ONESIGNAL_MARIGOLD_APP_ID') or os.getenv('ONESIGNAL_APP_ID')
    vibecoding_app_id = os.getenv('ONESIGNAL_VIBECODING_APP_ID')

    print(f"ONESIGNAL_REST_API_KEY: {'✅ Nastaveno' if api_key else '❌ Chybí'}")
    print(f"ONESIGNAL_MARIGOLD_APP_ID: {'✅ ' + marigold_app_id if marigold_app_id else '❌ Chybí'}")
    print(f"ONESIGNAL_VIBECODING_APP_ID: {'✅ ' + vibecoding_app_id if vibecoding_app_id else '❌ Chybí'}")

    if not api_key:
        print("\n⚠️ ONESIGNAL_REST_API_KEY není nastaven!")
        print("Najdi ho v OneSignal dashboardu:")
        print("  1. Jdi na https://onesignal.com/")
        print("  2. Settings → Keys & IDs")
        print("  3. Zkopíruj 'REST API Key'")
        print("  4. Nastav: export ONESIGNAL_REST_API_KEY='...'")
        return False

    if not marigold_app_id:
        print("\n⚠️ ONESIGNAL_MARIGOLD_APP_ID není nastaven!")
        print("Použij z dokumentace: 00fc3def-70d1-4e7d-a081-984d5e738a75")
        print("Nastav: export ONESIGNAL_MARIGOLD_APP_ID='00fc3def-70d1-4e7d-a081-984d5e738a75'")
        return False

    return True

def send_test_notification(app_id, app_name):
    """Poslat testovací notifikaci"""
    api_key = os.getenv('ONESIGNAL_REST_API_KEY')

    url = "https://onesignal.com/api/v1/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {api_key}"
    }

    payload = {
        "app_id": app_id,
        "included_segments": ["Subscribed Users"],
        "headings": {"en": f"🧪 Test z Claude Code"},
        "contents": {"en": f"Test notifikace pro {app_name} - funguje! ✅"},
    }

    print(f"\n📤 Odesílám testovací notifikaci do {app_name}...")
    print(f"   App ID: {app_id}")

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        if response.status_code in [200, 201]:
            result = response.json()
            recipients = result.get('recipients', 0)
            notification_id = result.get('id', 'unknown')
            print(f"✅ Úspěch!")
            print(f"   Notification ID: {notification_id}")
            print(f"   Příjemci: {recipients}")
            return True
        else:
            print(f"❌ Chyba {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def find_latest_article():
    """Najít poslední článek v _posts/"""
    posts_dir = Path('_posts')

    if not posts_dir.exists():
        print("❌ Adresář _posts/ neexistuje")
        return None

    # Najít nejnovější .md soubor
    md_files = list(posts_dir.glob('**/*.md'))
    if not md_files:
        print("❌ Žádné články v _posts/")
        return None

    # Seřadit podle data modifikace
    md_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)

    return md_files[0]

def send_article_notification():
    """Poslat notifikaci o posledním článku"""
    import yaml

    article_path = find_latest_article()
    if not article_path:
        return False

    print(f"\n📰 Nalezen poslední článek: {article_path.name}")

    # Načíst metadata
    try:
        with open(article_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            print("❌ Článek nemá front matter")
            return False

        parts = content.split('---', 2)
        if len(parts) < 3:
            print("❌ Neplatný front matter")
            return False

        frontmatter = yaml.safe_load(parts[1])
        title = frontmatter.get('title', 'Bez názvu')
        summary = frontmatter.get('summary', frontmatter.get('post_excerpt', title))

        print(f"   Titulek: {title}")
        print(f"   Shrnutí: {summary[:100]}...")

        # Poslat notifikaci
        app_id = os.getenv('ONESIGNAL_MARIGOLD_APP_ID') or os.getenv('ONESIGNAL_APP_ID')
        api_key = os.getenv('ONESIGNAL_REST_API_KEY')

        url = "https://onesignal.com/api/v1/notifications"
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Basic {api_key}"
        }

        payload = {
            "app_id": app_id,
            "included_segments": ["Subscribed Users"],
            "headings": {"en": f"🆕 {title}"},
            "contents": {"en": summary},
        }

        print(f"\n📤 Odesílám notifikaci o článku...")

        response = requests.post(url, json=payload, headers=headers, timeout=10)

        if response.status_code in [200, 201]:
            result = response.json()
            recipients = result.get('recipients', 0)
            notification_id = result.get('id', 'unknown')
            print(f"✅ Úspěch!")
            print(f"   Notification ID: {notification_id}")
            print(f"   Příjemci: {recipients}")
            return True
        else:
            print(f"❌ Chyba {response.status_code}")
            print(f"   Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Chyba: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("🔔 OneSignal Test Script")
    print("=" * 60)

    # Zkontrolovat přihlašovací údaje
    if not test_onesignal_credentials():
        print("\n❌ Chybí přihlašovací údaje. Nastav je a zkus znovu.")
        return 1

    print("\n" + "=" * 60)
    print("Co chceš udělat?")
    print("1. Poslat testovací notifikaci (Marigold)")
    print("2. Poslat testovací notifikaci (Vibecoding)")
    print("3. Poslat notifikaci o posledním článku")
    print("=" * 60)

    choice = input("\nVolba (1-3): ").strip()

    if choice == "1":
        app_id = os.getenv('ONESIGNAL_MARIGOLD_APP_ID') or os.getenv('ONESIGNAL_APP_ID')
        send_test_notification(app_id, "Marigold.cz")
    elif choice == "2":
        app_id = os.getenv('ONESIGNAL_VIBECODING_APP_ID')
        if not app_id:
            print("❌ ONESIGNAL_VIBECODING_APP_ID není nastaven")
            return 1
        send_test_notification(app_id, "Vibecoding.cz")
    elif choice == "3":
        send_article_notification()
    else:
        print("❌ Neplatná volba")
        return 1

    print("\n" + "=" * 60)
    print("✅ Hotovo!")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
