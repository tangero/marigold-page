#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test hotlinking obrázků z různých serverů
"""

import requests
from urllib.parse import urlparse

def test_hotlinking(image_url, referer_url="https://www.marigold.cz/tech-news/"):
    """
    Testuje, zda můžeme zobrazit obrázek s různými referer hlavičkami
    """
    domain = urlparse(image_url).netloc

    print(f"\n🔍 Testování: {domain}")
    print(f"📸 URL: {image_url[:80]}...")

    tests = [
        {
            'name': 'Bez Referer',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        },
        {
            'name': 'S Referer (marigold.cz)',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Referer': referer_url
            }
        },
        {
            'name': 'S Referer (stejná doména)',
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Referer': f'https://{domain}/'
            }
        },
        {
            'name': 'Jako bot',
            'headers': {
                'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'
            }
        }
    ]

    for test in tests:
        try:
            response = requests.get(image_url, headers=test['headers'], timeout=5, stream=True)

            # Kontrola status kódu
            if response.status_code == 200:
                content_type = response.headers.get('Content-Type', '')
                content_length = response.headers.get('Content-Length', 'unknown')

                if 'image' in content_type:
                    print(f"✅ {test['name']}: OK (200, {content_type}, {content_length} bytes)")
                else:
                    print(f"⚠️ {test['name']}: 200 ale není obrázek ({content_type})")
            elif response.status_code == 403:
                print(f"🚫 {test['name']}: BLOKOVÁNO (403 Forbidden)")
            elif response.status_code == 301 or response.status_code == 302:
                print(f"↗️ {test['name']}: Redirect na {response.headers.get('Location', 'unknown')}")
            else:
                print(f"❌ {test['name']}: HTTP {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"💥 {test['name']}: Chyba - {str(e)[:50]}")

    return True

def test_cors_headers(image_url):
    """
    Testuje CORS hlavičky
    """
    try:
        response = requests.options(image_url, headers={
            'Origin': 'https://www.marigold.cz',
            'Access-Control-Request-Method': 'GET'
        }, timeout=5)

        cors_headers = {
            'Access-Control-Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
            'Access-Control-Allow-Methods': response.headers.get('Access-Control-Allow-Methods'),
        }

        print("\n🌐 CORS hlavičky:")
        for key, value in cors_headers.items():
            if value:
                print(f"  {key}: {value}")

        if not any(cors_headers.values()):
            print("  ❌ Žádné CORS hlavičky (může být problém pro JS)")
    except:
        print("\n🌐 CORS test selhal")

def main():
    # Test různých zdrojů
    test_cases = [
        # TechCrunch
        "https://techcrunch.com/wp-content/uploads/2025/09/TELO-All-Electric-Mini-Truck-3.jpg?w=1200",

        # The Verge
        "https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/27149513/247298_Q3_Earnings_K_Radtke.jpg?w=1200",

        # Wired
        "https://media.wired.com/photos/68d2ce70a8e62baa797e5e45/191:100/w_1280,c_limit/Salim-Ismail-Business-Source-Courtesy-of-Salim-Ismail.jpg",

        # 9to5Mac
        "https://9to5mac.com/wp-content/uploads/sites/6/2025/09/9to5Mac-Daily-1.webp?w=1500",
    ]

    print("=" * 80)
    print("🧪 TEST HOTLINKING OBRÁZKŮ PRO MARIGOLD.CZ")
    print("=" * 80)

    for image_url in test_cases:
        test_hotlinking(image_url)
        test_cors_headers(image_url)
        print("-" * 80)

    print("\n📊 SOUHRN:")
    print("• Pokud všechny testy selhávají → server blokuje hotlinking")
    print("• Pokud funguje jen 'Stejná doména' → kontrola Referer hlavičky")
    print("• Pokud funguje jen 'Bot' → detekce User-Agent")
    print("• Pokud chybí CORS → problém pro dynamické načítání v JS")

if __name__ == "__main__":
    main()