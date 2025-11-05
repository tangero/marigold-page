#!/usr/bin/env python3
"""
Jednoduchý skript pro okamžité odeslání notifikace
Vyžaduje: pip install requests pyyaml
"""

import requests
import yaml
from pathlib import Path

# NASTAV TYTO HODNOTY Z ONESIGNAL DASHBOARDU
ONESIGNAL_REST_API_KEY = input("OneSignal REST API Key: ").strip()
ONESIGNAL_APP_ID = "00fc3def-70d1-4e7d-a081-984d5e738a75"  # Marigold.cz

# Najít poslední článek
article_path = Path("_posts/2025/2025-10-21-openai-prohlizec-atlas.md")

print(f"\n📰 Načítám článek: {article_path}")

with open(article_path, 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('---', 2)
frontmatter = yaml.safe_load(parts[1])

title = frontmatter.get('title', 'Bez názvu')
summary = frontmatter.get('post_excerpt', frontmatter.get('summary', title))

print(f"   Titulek: {title}")
print(f"   Shrnutí: {summary[:100]}...")

# Poslat notifikaci
url = "https://api.onesignal.com/notifications"  # BEZ query parametru
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Key {ONESIGNAL_REST_API_KEY}"
}

payload = {
    "app_id": ONESIGNAL_APP_ID,
    "included_segments": ["Total Subscriptions"],  # 12 Push Subs podle dashboardu
    "headings": {
        "en": f"🆕 {title}",  # EN je POVINNÝ podle OneSignal API
        "cs": f"🆕 {title}"   # CS jako alternativa
    },
    "contents": {
        "en": summary,  # EN je POVINNÝ
        "cs": summary   # CS jako alternativa
    },
    # Explicitně specifikovat Web Push platformy
    "isAnyWeb": True,
    "isChromeWeb": True,
    "isFirefox": True,
    "isSafari": True,
    # Vypnout mobilní platformy
    "isIos": False,
    "isAndroid": False,
}

print(f"\n📤 Odesílám notifikaci...")
print(f"   URL: {url}")
print(f"   Segment: {payload['included_segments']}")

response = requests.post(url, json=payload, headers=headers, timeout=10)

print(f"\n📡 Response Status: {response.status_code}")

if response.status_code in [200, 201]:
    result = response.json()
    notification_id = result.get('id', 'unknown')
    recipients = result.get('recipients', None)

    print(f"✅ Úspěch!")
    print(f"   Notification ID: {notification_id}")

    if recipients is not None:
        print(f"   Příjemci: {recipients}")
    else:
        print(f"   Příjemci: Počet se zobrazí v OneSignal dashboardu")
        print(f"   Dashboard: https://dashboard.onesignal.com/apps/00fc3def-70d1-4e7d-a081-984d5e738a75/delivery")

    if result.get('errors'):
        print(f"\n⚠️  Varování: {result['errors']}")
    else:
        print(f"\n🎉 Notifikace byla úspěšně odeslána!")
        print(f"   Zkontrolujte výsledky v dashboardu za pár minut.")
else:
    print(f"❌ Chyba {response.status_code}")
    print(f"   Response: {response.text}")

    if response.status_code == 400:
        print(f"\n💡 TIP: Špatný request - zkontrolujte segment name nebo payload")