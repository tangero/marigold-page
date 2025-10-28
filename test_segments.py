#!/usr/bin/env python3
"""
Test script - zjistí dostupné segmenty a zkusí poslat na konkrétní Player IDs
"""

import os
import requests
import json

def main():
    print("🔍 OneSignal Segments Test")
    print("=" * 60)

    api_key = os.getenv('ONESIGNAL_REST_API_KEY')
    app_id = "00fc3def-70d1-4e7d-a081-984d5e738a75"

    if not api_key:
        api_key = input("OneSignal REST API Key: ").strip()

    print(f"\n✅ App ID: {app_id}")

    # 1. Zjistit dostupné segmenty
    print("\n" + "=" * 60)
    print("📋 ZJIŠŤUJI DOSTUPNÉ SEGMENTY:")
    print("=" * 60)

    segments_url = f"https://onesignal.com/api/v1/apps/{app_id}/segments"
    headers = {
        "Authorization": f"Basic {api_key}"
    }

    response = requests.get(segments_url, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")

    if response.status_code == 200:
        segments = response.json()
        print("\n📊 Dostupné segmenty:")
        print(json.dumps(segments, indent=2, ensure_ascii=False))

        if isinstance(segments, list):
            for segment in segments:
                if isinstance(segment, dict):
                    print(f"\n   Segment: {segment.get('name', 'N/A')}")
                    print(f"      ID: {segment.get('id', 'N/A')}")
    else:
        print(f"❌ Chyba: {response.text}")

    # 2. Zkusit poslat notifikaci s ALL segments
    print("\n" + "=" * 60)
    print("🧪 TEST 1: Posílám na 'All' segment:")
    print("=" * 60)

    notification_url = "https://onesignal.com/api/v1/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {api_key}"
    }

    payload1 = {
        "app_id": app_id,
        "included_segments": ["All"],
        "headings": {"en": "🧪 Test 1: All segment"},
        "contents": {"en": "Test s 'All' segmentem"},
    }

    response1 = requests.post(notification_url, json=payload1, headers=headers, timeout=10)
    print(f"Status: {response1.status_code}")
    result1 = response1.json()
    print(json.dumps(result1, indent=2, ensure_ascii=False))

    # 3. Zkusit poslat notifikaci na Active Users
    print("\n" + "=" * 60)
    print("🧪 TEST 2: Posílám na 'Active Users' segment:")
    print("=" * 60)

    payload2 = {
        "app_id": app_id,
        "included_segments": ["Active Users"],
        "headings": {"en": "🧪 Test 2: Active Users"},
        "contents": {"en": "Test s 'Active Users' segmentem"},
    }

    response2 = requests.post(notification_url, json=payload2, headers=headers, timeout=10)
    print(f"Status: {response2.status_code}")
    result2 = response2.json()
    print(json.dumps(result2, indent=2, ensure_ascii=False))

    # 4. Zkusit bez segments - poslat všem
    print("\n" + "=" * 60)
    print("🧪 TEST 3: Posílám VŠEM (bez segmentů):")
    print("=" * 60)

    payload3 = {
        "app_id": app_id,
        "filters": [
            {"field": "tag", "key": "subscription_status", "relation": "exists"}
        ],
        "headings": {"en": "🧪 Test 3: Filters"},
        "contents": {"en": "Test s filters místo segmentů"},
    }

    response3 = requests.post(notification_url, json=payload3, headers=headers, timeout=10)
    print(f"Status: {response3.status_code}")
    result3 = response3.json()
    print(json.dumps(result3, indent=2, ensure_ascii=False))

    # 5. Zkusit channel targeting (jen Web Push)
    print("\n" + "=" * 60)
    print("🧪 TEST 4: Targeting jen Web Push channel:")
    print("=" * 60)

    payload4 = {
        "app_id": app_id,
        "included_segments": ["All"],
        "channel_for_external_user_ids": "push",
        "headings": {"en": "🧪 Test 4: Web Push"},
        "contents": {"en": "Test s web push channel"},
    }

    response4 = requests.post(notification_url, json=payload4, headers=headers, timeout=10)
    print(f"Status: {response4.status_code}")
    result4 = response4.json()
    print(json.dumps(result4, indent=2, ensure_ascii=False))

    print("\n" + "=" * 60)
    print("✅ Všechny testy dokončeny!")
    print("=" * 60)

if __name__ == "__main__":
    main()
