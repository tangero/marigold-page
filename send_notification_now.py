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
url = "https://onesignal.com/api/v1/notifications"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Basic {ONESIGNAL_REST_API_KEY}"
}

payload = {
    "app_id": ONESIGNAL_APP_ID,
    "included_segments": ["Total Subscriptions"],
    "headings": {"en": f"🆕 {title}", "cs": f"🆕 {title}"},
    "contents": {"en": summary, "cs": summary},
    # Platform targeting - pouze Web Push
    "isAnyWeb": True,
    "isChromeWeb": True,
    "isFirefox": True,
    "isSafari": True,
}

print(f"\n📤 Odesílám notifikaci...")
response = requests.post(url, json=payload, headers=headers, timeout=10)

if response.status_code in [200, 201]:
    result = response.json()
    recipients = result.get('recipients', 0)
    notification_id = result.get('id', 'unknown')
    print(f"✅ Úspěch!")
    print(f"   Notification ID: {notification_id}")
    print(f"   Příjemci: {recipients}")
else:
    print(f"❌ Chyba {response.status_code}")
    print(f"   Response: {response.text}")