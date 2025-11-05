#!/usr/bin/env python3
"""
Zkontroluje počet subscriberů v OneSignal
"""
import requests
import sys

ONESIGNAL_APP_ID = "00fc3def-70d1-4e7d-a081-984d5e738a75"
ONESIGNAL_REST_API_KEY = input("OneSignal REST API Key: ").strip()

print(f"\n🔍 Kontroluji OneSignal App ID: {ONESIGNAL_APP_ID}")
print("=" * 60)

# Získat informace o aplikaci
url = f"https://api.onesignal.com/apps/{ONESIGNAL_APP_ID}"
headers = {
    "Authorization": f"Key {ONESIGNAL_REST_API_KEY}"
}

print(f"\n📡 Dotazuji OneSignal API...")
response = requests.get(url, headers=headers, timeout=10)

print(f"Status: {response.status_code}")

if response.status_code == 200:
    data = response.json()

    print(f"\n✅ ÚSPĚCH - Načteny informace o aplikaci")
    print("=" * 60)

    # App info
    print(f"\n📱 Aplikace:")
    print(f"   Název: {data.get('name', 'N/A')}")
    print(f"   ID: {data.get('id', 'N/A')}")

    # Subscriber counts
    print(f"\n👥 Počet subscriberů:")
    print(f"   Celkem: {data.get('players', 'N/A')}")
    print(f"   Aktivních (messageable): {data.get('messageable_players', 'N/A')}")

    # Platform breakdown
    print(f"\n🌐 Podle platformy:")
    print(f"   Chrome Web: {data.get('chrome_web_players', 'N/A')}")
    print(f"   Firefox: {data.get('firefox_players', 'N/A')}")
    print(f"   Safari: {data.get('safari_players', 'N/A')}")

    # Další statistiky
    if 'created_at' in data:
        print(f"\n📅 Vytvořeno: {data.get('created_at', 'N/A')}")

    # Vyhodnocení
    total_players = data.get('players', 0)
    messageable = data.get('messageable_players', 0)

    print("\n" + "=" * 60)
    if total_players == 0:
        print("⚠️  PROBLÉM: Nemáte ŽÁDNÉ subscribery!")
        print("\nDůvody:")
        print("  1. Nikdo se ještě nepřihlásil k odběru notifikací")
        print("  2. OneSignal SDK možná není správně nakonfigurován")
        print("  3. Slidedown se uživatelům možná nezobrazuje")
        print("\nDoporučení:")
        print("  - Navštivte web a zkuste se přihlásit k odběru")
        print("  - Zkontrolujte browser console na chyby")
        print("  - Zkontrolujte OneSignal dashboard")
    elif messageable == 0:
        print(f"⚠️  VAROVÁNÍ: Máte {total_players} subscriberů, ale 0 je messageable!")
        print("\nTo znamená, že všichni jsou neaktivní nebo unsubscribed")
    else:
        print(f"✅ OK: Máte {messageable} aktivních subscriberů")
        print("\nPokud notifikace stále nejdou, problém je v:")
        print("  - Segmentu (použijte 'All' místo 'Subscribed Users')")
        print("  - Target channel (přidejte 'target_channel': 'push')")

else:
    print(f"\n❌ CHYBA {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 401:
        print("\n💡 TIP: Zkontrolujte, že REST API Key je správný")
    elif response.status_code == 404:
        print("\n💡 TIP: Zkontrolujte, že App ID je správný")

print("\n" + "=" * 60)
