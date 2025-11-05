#!/usr/bin/env python3
"""
Pošle notifikaci VŠEM push odběratelům bez použití segmentů
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

# METODA 1: Jen target_channel bez segmentů
print("\n" + "=" * 70)
print("🧪 TEST 1: Posílám VŠEM s target_channel (bez segmentů)")
print("=" * 70)

url = "https://api.onesignal.com/notifications?c=push"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Key {ONESIGNAL_REST_API_KEY}"
}

payload1 = {
    "app_id": ONESIGNAL_APP_ID,
    "target_channel": "push",
    # BEZ included_segments - pošle všem push subscribers
    "headings": {"cs": f"🆕 {title}"},
    "contents": {"cs": summary},
    "isAnyWeb": True,
}

print(f"Payload: {payload1}\n")

response1 = requests.post(url, json=payload1, headers=headers, timeout=10)
print(f"Status: {response1.status_code}")

if response1.status_code in [200, 201]:
    result1 = response1.json()
    recipients1 = result1.get('recipients', 0)
    print(f"✅ Metoda 1: {recipients1} příjemců")
    print(f"   Full response: {result1}")
else:
    print(f"❌ Chyba: {response1.text}")

# METODA 2: Segment "All" s target_channel
print("\n" + "=" * 70)
print("🧪 TEST 2: Segment 'All' + target_channel")
print("=" * 70)

payload2 = {
    "app_id": ONESIGNAL_APP_ID,
    "included_segments": ["All"],
    "target_channel": "push",
    "headings": {"cs": f"🆕 {title}"},
    "contents": {"cs": summary},
    "isAnyWeb": True,
}

response2 = requests.post(url, json=payload2, headers=headers, timeout=10)
print(f"Status: {response2.status_code}")

if response2.status_code in [200, 201]:
    result2 = response2.json()
    recipients2 = result2.get('recipients', 0)
    print(f"✅ Metoda 2: {recipients2} příjemců")
    print(f"   Full response: {result2}")
else:
    print(f"❌ Chyba: {response2.text}")

# METODA 3: Subscribed Users segment
print("\n" + "=" * 70)
print("🧪 TEST 3: Segment 'Subscribed Users' + target_channel")
print("=" * 70)

payload3 = {
    "app_id": ONESIGNAL_APP_ID,
    "included_segments": ["Subscribed Users"],
    "target_channel": "push",
    "headings": {"cs": f"🆕 {title}"},
    "contents": {"cs": summary},
    "isAnyWeb": True,
}

response3 = requests.post(url, json=payload3, headers=headers, timeout=10)
print(f"Status: {response3.status_code}")

if response3.status_code in [200, 201]:
    result3 = response3.json()
    recipients3 = result3.get('recipients', 0)
    print(f"✅ Metoda 3: {recipients3} příjemců")
    print(f"   Full response: {result3}")
else:
    print(f"❌ Chyba: {response3.text}")

# Shrnutí
print("\n" + "=" * 70)
print("📊 SHRNUTÍ")
print("=" * 70)
print(f"\nMetoda 1 (bez segmentů): {recipients1 if 'recipients1' in locals() else 0} příjemců")
print(f"Metoda 2 (All): {recipients2 if 'recipients2' in locals() else 0} příjemců")
print(f"Metoda 3 (Subscribed Users): {recipients3 if 'recipients3' in locals() else 0} příjemců")

print("\n💡 Použijte metodu s nejvíce příjemci!")
print("\n")
