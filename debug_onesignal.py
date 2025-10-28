#!/usr/bin/env python3
"""
Debug skript pro OneSignal - ukáže přesnou response strukturu
"""

import os
import sys
import requests
import yaml
import json
from pathlib import Path

def main():
    print("🔍 OneSignal DEBUG Script")
    print("=" * 60)

    # Načíst API credentials
    api_key = os.getenv('ONESIGNAL_REST_API_KEY')
    app_id = os.getenv('ONESIGNAL_APP_ID') or os.getenv('ONESIGNAL_MARIGOLD_APP_ID')

    if not api_key:
        api_key = input("OneSignal REST API Key: ").strip()

    if not app_id:
        app_id = "00fc3def-70d1-4e7d-a081-984d5e738a75"  # Marigold.cz

    print(f"\n✅ API Key: {'*' * 20}{api_key[-4:]}")
    print(f"✅ App ID: {app_id}")

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

    # Připravit payload
    url = "https://onesignal.com/api/v1/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {api_key}"
    }

    payload = {
        "app_id": app_id,
        "included_segments": ["Subscribed Users"],
        "headings": {"en": f"🆕 {title}", "cs": f"🆕 {title}"},
        "contents": {"en": summary, "cs": summary},
    }

    print("\n" + "=" * 60)
    print("📤 PAYLOAD (co posíláme):")
    print("=" * 60)
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    print("\n" + "=" * 60)
    print("📡 Odesílám request na OneSignal API...")
    print("=" * 60)

    # Poslat request
    response = requests.post(url, json=payload, headers=headers, timeout=10)

    print(f"\n🔢 STATUS CODE: {response.status_code}")

    print("\n" + "=" * 60)
    print("📥 RAW RESPONSE TEXT:")
    print("=" * 60)
    print(response.text)

    print("\n" + "=" * 60)
    print("📋 RESPONSE HEADERS:")
    print("=" * 60)
    for key, value in response.headers.items():
        print(f"   {key}: {value}")

    # Zkusit parsovat JSON
    try:
        result = response.json()

        print("\n" + "=" * 60)
        print("🗂️  PARSED JSON (formátováno):")
        print("=" * 60)
        print(json.dumps(result, indent=2, ensure_ascii=False))

        print("\n" + "=" * 60)
        print("🔑 VŠECHNY KLÍČE v response:")
        print("=" * 60)
        print(f"   Top-level keys: {list(result.keys())}")

        # Projít všechny klíče
        for key, value in result.items():
            print(f"\n   '{key}': {type(value).__name__}")
            if isinstance(value, dict):
                print(f"      → Sub-keys: {list(value.keys())}")
            else:
                print(f"      → Value: {value}")

        print("\n" + "=" * 60)
        print("🎯 EXTRAKCE DAT:")
        print("=" * 60)

        # Zkusit různé cesty k ID
        paths = [
            ("result.get('id')", result.get('id')),
            ("result.get('body', {}).get('id')", result.get('body', {}).get('id')),
            ("result.get('notification', {}).get('id')", result.get('notification', {}).get('id')),
            ("result.get('recipients')", result.get('recipients')),
            ("result.get('body', {}).get('recipients')", result.get('body', {}).get('recipients')),
        ]

        for path, value in paths:
            print(f"   {path}: {value}")

    except json.JSONDecodeError as e:
        print(f"\n❌ Chyba parsování JSON: {e}")

    print("\n" + "=" * 60)
    print("✅ Debug dokončen!")
    print("=" * 60)

if __name__ == "__main__":
    main()
