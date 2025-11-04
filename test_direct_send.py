#!/usr/bin/env python3
"""
Test notifikace bez segmentů - pošle všem Web Push subscriberům
"""
import requests

api_key = input("OneSignal REST API Key: ").strip()
app_id = "00fc3def-70d1-4e7d-a081-984d5e738a75"

url = "https://onesignal.com/api/v1/notifications"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Basic {api_key}"
}

# Zkusit různé přístupy
tests = [
    {
        "name": "Test 1: Total Subscriptions (původní)",
        "payload": {
            "app_id": app_id,
            "included_segments": ["Total Subscriptions"],
            "headings": {"en": "Test 1", "cs": "Test 1"},
            "contents": {"en": "Test", "cs": "Test"},
        }
    },
    {
        "name": "Test 2: Active Subscriptions",
        "payload": {
            "app_id": app_id,
            "included_segments": ["Active Subscriptions"],
            "headings": {"en": "Test 2", "cs": "Test 2"},
            "contents": {"en": "Test", "cs": "Test"},
        }
    },
    {
        "name": "Test 3: Jen Web Push kanál",
        "payload": {
            "app_id": app_id,
            "included_segments": ["Total Subscriptions"],
            "channel_for_external_user_ids": "push",
            "headings": {"en": "Test 3", "cs": "Test 3"},
            "contents": {"en": "Test", "cs": "Test"},
        }
    },
    {
        "name": "Test 4: Filters místo segmentů",
        "payload": {
            "app_id": app_id,
            "filters": [
                {"field": "tag", "key": "test", "relation": "exists"}
            ],
            "headings": {"en": "Test 4", "cs": "Test 4"},
            "contents": {"en": "Test", "cs": "Test"},
        }
    }
]

print("🧪 OneSignal Segment Testing")
print("=" * 70)

for test in tests:
    print(f"\n{test['name']}")
    print("-" * 70)
    
    response = requests.post(url, json=test['payload'], headers=headers, timeout=10)
    
    if response.status_code in [200, 201]:
        result = response.json()
        recipients = result.get('recipients', 0)
        notification_id = result.get('id', 'unknown')
        
        print(f"✅ Status: {response.status_code}")
        print(f"   Notification ID: {notification_id}")
        print(f"   Recipients: {recipients}")
        
        if recipients > 0:
            print(f"   🎯 TENTO ZPŮSOB FUNGUJE!")
    else:
        print(f"❌ Chyba {response.status_code}")
        error = response.json()
        print(f"   Error: {error.get('errors', [response.text])}")

print("\n" + "=" * 70)
print("✅ Test dokončen")
