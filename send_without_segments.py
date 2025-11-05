#!/usr/bin/env python3
"""
Pošle notifikaci BEZ použití segmentů - jen pomocí filtrů
"""
import requests
import yaml
from pathlib import Path

ONESIGNAL_REST_API_KEY = input("OneSignal REST API Key: ").strip()
ONESIGNAL_APP_ID = "00fc3def-70d1-4e7d-a081-984d5e738a75"

# Načíst článek
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

# Poslat VŠEM pomocí filtru "last_session exists"
url = "https://api.onesignal.com/notifications"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Key {ONESIGNAL_REST_API_KEY}"
}

payload = {
    "app_id": ONESIGNAL_APP_ID,
    # BEZ included_segments - použijeme filtry
    "filters": [
        {"field": "last_session", "relation": "exists"}  # Všichni co měli alespoň 1 session
    ],
    "headings": {"cs": f"🆕 {title}"},
    "contents": {"cs": summary},
}

print(f"\n📤 Odesílám notifikaci POMOCÍ FILTRŮ (bez segmentů)...")
print(f"   URL: {url}")
print(f"   Filtry: last_session exists")

response = requests.post(url, json=payload, headers=headers, timeout=10)

print(f"\n📡 Response Status: {response.status_code}")

if response.status_code in [200, 201]:
    result = response.json()
    recipients = result.get('recipients', 0)
    notification_id = result.get('id', 'unknown')

    print(f"✅ Úspěch!")
    print(f"   Notification ID: {notification_id}")
    print(f"   Příjemci: {recipients}")
    print(f"   Full response: {result}")

    if recipients > 0:
        print(f"\n🎉 FUNGUJE! Toto je řešení - používejte filtry místo segmentů!")
    else:
        print(f"\n⚠️  Stále 0 příjemců")
else:
    print(f"❌ Chyba {response.status_code}")
    print(f"   Response: {response.text}")
