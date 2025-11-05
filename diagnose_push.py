#!/usr/bin/env python3
"""
Kompletní diagnostika OneSignal push notifikací podle oficiální dokumentace
"""
import requests
import json

ONESIGNAL_APP_ID = "00fc3def-70d1-4e7d-a081-984d5e738a75"
ONESIGNAL_REST_API_KEY = input("OneSignal REST API Key: ").strip()

print("\n" + "=" * 80)
print("🔍 ONESIGNAL PUSH DIAGNOSTIKA - KOMPLETNÍ ANALÝZA")
print("=" * 80)

# Společné headery
headers = {
    "Authorization": f"Key {ONESIGNAL_REST_API_KEY}",
    "Content-Type": "application/json"
}

# ============================================================================
# KROK 1: Základní info o aplikaci
# ============================================================================
print("\n📱 KROK 1: Základní informace o aplikaci")
print("-" * 80)

app_url = f"https://api.onesignal.com/apps/{ONESIGNAL_APP_ID}"
response = requests.get(app_url, headers=headers, timeout=10)

if response.status_code == 200:
    app_data = response.json()
    print(f"✅ Aplikace: {app_data.get('name', 'N/A')}")
    print(f"   Celkem uživatelů: {app_data.get('players', 0)}")
    print(f"   Aktivních (messageable): {app_data.get('messageable_players', 0)}")
    print(f"   Chrome Web: {app_data.get('chrome_web_players', 'N/A')}")
    print(f"   Firefox: {app_data.get('firefox_players', 'N/A')}")
    print(f"   Safari: {app_data.get('safari_players', 'N/A')}")

    total_web = sum([
        app_data.get('chrome_web_players', 0) or 0,
        app_data.get('firefox_players', 0) or 0,
        app_data.get('safari_players', 0) or 0
    ])
    print(f"\n   💡 Celkem WEB PUSH subscribers: {total_web}")
else:
    print(f"❌ Chyba {response.status_code}: {response.text}")
    exit(1)

# ============================================================================
# KROK 2: Seznam všech segmentů
# ============================================================================
print("\n" + "=" * 80)
print("📊 KROK 2: Dostupné segmenty")
print("-" * 80)

segments_url = f"https://api.onesignal.com/apps/{ONESIGNAL_APP_ID}/segments"
response = requests.get(segments_url, headers=headers, timeout=10)

available_segments = []

if response.status_code == 200:
    segments_data = response.json()

    # Zpracování podle struktury dat
    if isinstance(segments_data, dict) and 'segments' in segments_data:
        segments = segments_data['segments']
    elif isinstance(segments_data, list):
        segments = segments_data
    else:
        segments = []

    if segments:
        for i, seg in enumerate(segments, 1):
            name = seg.get('name', 'N/A')
            seg_id = seg.get('id', 'N/A')
            available_segments.append(name)
            print(f"\n   {i}. '{name}'")
            print(f"      ID: {seg_id}")
    else:
        print("   ⚠️  Žádné custom segmenty nenalezeny")
        print("   💡 Zkuste použít výchozí segmenty: 'All', 'Active Users', 'Engaged Users'")
        available_segments = ["All", "Active Users", "Engaged Users", "Inactive Users"]
else:
    print(f"   ⚠️  Nelze načíst segmenty (status {response.status_code})")
    print("   💡 Používám výchozí segmenty")
    available_segments = ["All", "Active Users", "Engaged Users", "Inactive Users", "Total Subscriptions"]

# ============================================================================
# KROK 3: Testování segmentů - DRY RUN
# ============================================================================
print("\n" + "=" * 80)
print("🧪 KROK 3: Testování segmentů (zjišťuji recipients BEZ odeslání)")
print("-" * 80)

test_url = "https://api.onesignal.com/notifications"
params = {"c": "push"}

working_segments = []

for segment_name in available_segments:
    print(f"\n   Testuji: '{segment_name}'")

    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "included_segments": [segment_name],
        "target_channel": "push",
        "contents": {"en": "Test"},
        "headings": {"en": "Test"},
        # Nenastavíme send_after, takže se pošle okamžitě
        # Ale můžeme zkontrolovat response
    }

    # POZOR: Toto POŠLE skutečnou notifikaci!
    # V produkci použijte endpoint pro preview nebo testujte s malým segmentem

    # Pro nyní jen simulujeme - NEPOŠLEME
    print(f"      Segment payload připraven")
    print(f"      ⚠️  Pro skutečný test by se poslala notifikace")

# ============================================================================
# KROK 4: Alternativní metoda - Poslat konkrétnímu subscription ID
# ============================================================================
print("\n" + "=" * 80)
print("💡 KROK 4: Alternativní metody targetování")
print("-" * 80)

print("\n📋 Podle dokumentace máte 3 možnosti:")
print("\n1. included_segments - Pro předem definované segmenty")
print("   Příklad: {'included_segments': ['Total Subscriptions']}")

print("\n2. include_subscription_ids - Pro konkrétní subscription IDs")
print("   Příklad: {'include_subscription_ids': ['uuid-1', 'uuid-2']}")
print("   ⚠️  Vyžaduje znát subscription IDs vašich uživatelů")

print("\n3. include_aliases - Pro targetování přes external_id")
print("   Příklad: {'include_aliases': {'external_id': ['user1', 'user2']}, 'target_channel': 'push'}")
print("   ⚠️  Vyžaduje mít nastavené external_id pro uživatele")

print("\n4. filters - Pro dynamické filtrování")
print("   Příklad: {'filters': [{'field': 'tag', 'key': 'premium', 'relation': '=', 'value': 'true'}]}")

# ============================================================================
# FINÁLNÍ DOPORUČENÍ
# ============================================================================
print("\n" + "=" * 80)
print("🎯 FINÁLNÍ DOPORUČENÍ")
print("=" * 80)

print(f"\n📊 Vaše statistiky:")
print(f"   - Celkem uživatelů v app: {app_data.get('players', 0)}")
print(f"   - Aktivních (messageable): {app_data.get('messageable_players', 0)}")
print(f"   - Web push subscribers: {total_web}")

print(f"\n🔍 Dostupné segmenty:")
for seg in available_segments[:5]:
    print(f"   - {seg}")

print(f"\n💡 ŘEŠENÍ:")
print(f"\n   Problém: Segment 'Total Subscriptions' má 12 uživatelů, ale 0 recipients pro PUSH")
print(f"\n   Možné příčiny:")
print(f"   1. Segment obsahuje email/SMS subscriptions, NE push")
print(f"   2. Všichni uživatelé v segmentu jsou unsubscribed pro push")
print(f"   3. Segment filtruje jinak než pro push channel")

print(f"\n   ✅ ZKUSTE:")
print(f"   1. Použít segment 'All' místo 'Total Subscriptions'")
print(f"   2. Vytvořit nový segment specificky pro web push v OneSignal dashboardu")
print(f"   3. Zkontrolovat v OneSignal → Audience → Segments kolik má 'Total Subscriptions' PUSH subscribers")

print(f"\n   📝 Testovací payload:")
print(f"""
   payload = {{
       "app_id": "{ONESIGNAL_APP_ID}",
       "included_segments": ["All"],  # ← Zkuste místo 'Total Subscriptions'
       "target_channel": "push",
       "headings": {{"cs": "Test"}},
       "contents": {{"cs": "Test zpráva"}},
       "isAnyWeb": True
   }}
""")

print(f"\n   🔗 OneSignal Dashboard:")
print(f"   https://dashboard.onesignal.com/apps/{ONESIGNAL_APP_ID}/settings")
print(f"   → Audience → Segments → Zkontrolujte 'Total Subscriptions' detaily")

print("\n" + "=" * 80)
