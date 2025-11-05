#!/usr/bin/env python3
"""
Vypíše všechny segmenty v OneSignal aplikaci
"""
import requests
import json

ONESIGNAL_APP_ID = "00fc3def-70d1-4e7d-a081-984d5e738a75"
ONESIGNAL_REST_API_KEY = input("OneSignal REST API Key: ").strip()

print(f"\n🔍 Načítám segmenty pro App ID: {ONESIGNAL_APP_ID}")
print("=" * 70)

# Získat seznam segmentů
url = f"https://api.onesignal.com/apps/{ONESIGNAL_APP_ID}/segments"
headers = {
    "Authorization": f"Key {ONESIGNAL_REST_API_KEY}"
}

response = requests.get(url, headers=headers, timeout=10)

print(f"Status: {response.status_code}\n")

if response.status_code == 200:
    data = response.json()

    print("📊 DOSTUPNÉ SEGMENTY:")
    print("=" * 70)

    if 'segments' in data:
        segments = data['segments']
    elif isinstance(data, list):
        segments = data
    else:
        segments = [data]

    if not segments:
        print("⚠️  Žádné segmenty nenalezeny!")
        print("\nFull response:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        for i, segment in enumerate(segments, 1):
            print(f"\n{i}. Segment:")
            print(f"   Název: {segment.get('name', 'N/A')}")
            print(f"   ID: {segment.get('id', 'N/A')}")

            # Počet uživatelů
            if 'count' in segment:
                print(f"   Počet uživatelů: {segment.get('count', 'N/A')}")

            # Filters/podmínky
            if 'filters' in segment:
                print(f"   Filtry: {segment.get('filters', 'N/A')}")

            print(f"   Raw data: {json.dumps(segment, ensure_ascii=False)}")

        print("\n" + "=" * 70)
        print("💡 DOPORUČENÍ:")
        print("=" * 70)
        print("\nPokud nevidíte segment 'Total Subscriptions', použijte:")
        print("  - 'All' nebo 'Active Users' (výchozí segmenty)")
        print("\nALEBO zkuste poslat VŠEM bez segmentu:")
        print("  - Odeberte 'included_segments' z payload")
        print("  - Použijte jen 'target_channel': 'push'")

else:
    print(f"❌ Chyba {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 401:
        print("\n💡 TIP: Zkontrolujte REST API Key")

print("\n")
