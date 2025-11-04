#!/usr/bin/env python3
"""
Přímý test OneSignal segmentů - použije API klíč z environment nebo přímo
"""
import requests
import json
import sys

# POUŽIJTE VÁŠ API KLÍČ
api_key = "os_v2_app_ad6d333q2fhh3iebtbgv444koxxkdsmkdtsuf74z64vbww6o723h6fs5on5m4goyub5vw5fwjk2ec67cdyadhqd4u6xwjjc66bafndi"
app_id = "00fc3def-70d1-4e7d-a081-984d5e738a75"

print("🔍 OneSignal Segment Diagnostic Tool")
print("=" * 70)

# 1. Zjistit celkové statistiky aplikace
print("\n📊 KROK 1: Celkové statistiky")
print("-" * 70)

app_url = f"https://onesignal.com/api/v1/apps/{app_id}"
headers = {"Authorization": f"Basic {api_key}"}

response = requests.get(app_url, headers=headers, timeout=10)

if response.status_code == 200:
    data = response.json()
    print(f"✅ App Name: {data.get('name', 'N/A')}")
    print(f"   Celkem subscriberů: {data.get('players', 0)}")
    print(f"   Aktivních (7 dní): {data.get('messageable_players', 0)}")
    
    total_subs = data.get('players', 0)
    active_subs = data.get('messageable_players', 0)
    
    if total_subs == 0:
        print("\n⚠️  PROBLÉM: Žádní subscribeři!")
        sys.exit(1)
else:
    print(f"❌ Chyba {response.status_code}: {response.text}")
    sys.exit(1)

# 2. Zjistit dostupné segmenty
print("\n" + "=" * 70)
print("📋 KROK 2: Dostupné segmenty v OneSignal")
print("-" * 70)

segments_url = f"https://onesignal.com/api/v1/apps/{app_id}/segments"
response = requests.get(segments_url, headers=headers, timeout=10)

available_segments = []
if response.status_code == 200:
    segments = response.json()
    for segment in segments:
        if isinstance(segment, dict):
            seg_name = segment.get('name', 'N/A')
            seg_id = segment.get('id', 'N/A')
            available_segments.append(seg_name)
            print(f"   • {seg_name} (ID: {seg_id})")
else:
    print(f"❌ Chyba: {response.text}")

# 3. Otestovat každý segment
print("\n" + "=" * 70)
print("🧪 KROK 3: Testování segmentů")
print("-" * 70)

segments_to_test = ["All", "Active Users", "Engaged Users", "Subscribed Users", "Inactive Users"]

notification_url = "https://onesignal.com/api/v1/notifications"
headers_post = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Basic {api_key}"
}

working_segments = []

for segment_name in segments_to_test:
    print(f"\n🔍 Testuji: '{segment_name}'")
    
    payload = {
        "app_id": app_id,
        "included_segments": [segment_name],
        "headings": {"en": f"Test: {segment_name}"},
        "contents": {"en": "Test"},
        "send_after": "2030-01-01 00:00:00 GMT+0000"  # Neplánuje se skutečně
    }
    
    response = requests.post(notification_url, json=payload, headers=headers_post, timeout=10)
    
    if response.status_code in [200, 201]:
        result = response.json()
        recipients = result.get('recipients', 0)
        
        if recipients > 0:
            print(f"   ✅ Recipients: {recipients} 🎯 FUNGUJE!")
            working_segments.append((segment_name, recipients))
        else:
            print(f"   ⚠️  Recipients: {recipients} (prázdný segment)")
    else:
        print(f"   ❌ Chyba {response.status_code}")
        error_msg = response.json().get('errors', [response.text])
        print(f"      {error_msg}")

# 4. Závěr
print("\n" + "=" * 70)
print("📋 ZÁVĚR")
print("=" * 70)

print(f"\n📊 Celkem subscriberů: {total_subs}")
print(f"📊 Aktivních: {active_subs}")

if working_segments:
    print(f"\n✅ FUNKČNÍ SEGMENTY ({len(working_segments)}):")
    for seg_name, count in working_segments:
        print(f"   🎯 '{seg_name}' → {count} příjemců")
    
    best_segment = max(working_segments, key=lambda x: x[1])
    print(f"\n💡 DOPORUČENÍ: Použijte segment '{best_segment[0]}' ({best_segment[1]} příjemců)")
else:
    print("\n❌ ŽÁDNÝ SEGMENT NEFUNGUJE!")
    print("   Možné příčiny:")
    print("   1. Subscribeři nejsou 'aktivní' (nebyli online v posledních dnech)")
    print("   2. Subscribeři mají vypnuté notifikace")
    print("   3. OneSignal cache - zkuste za pár minut")

print("\n" + "=" * 70)
