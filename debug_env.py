#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import requests
from dotenv import load_dotenv

# Funkce pro výpis informací o prostředí
def print_env_info():
    print("\n=== Informace o prostředí ===")
    print(f"Pracovní adresář: {os.getcwd()}")
    env_paths = [
        ".env",
        os.path.expanduser("~/.env"),
        os.path.join(os.getcwd(), ".env"),
        "/Users/imac/Documents/GitHub/zastupitelstvo/.env"
    ]
    
    print("\nHledání .env souborů:")
    for path in env_paths:
        exists = os.path.exists(path)
        print(f"  {path}: {'✅ existuje' if exists else '❌ neexistuje'}")
        if exists:
            try:
                with open(path, 'r') as f:
                    lines = f.readlines()
                print(f"  Obsah (prvních {min(5, len(lines))} řádků):")
                for i, line in enumerate(lines[:5]):
                    if "API_KEY" in line:
                        # Zobrazíme pouze prvních 10 znaků klíče
                        key_parts = line.split('=')
                        if len(key_parts) > 1:
                            key_name = key_parts[0].strip()
                            key_value = key_parts[1].strip()
                            if len(key_value) > 10:
                                key_value = key_value[:10] + "..."
                            print(f"    {key_name}={key_value}")
                    else:
                        print(f"    {line.strip()}")
            except Exception as e:
                print(f"  Chyba při čtení souboru: {e}")

# Funkce pro testování API
def test_api():
    print("\n=== Test OpenRouter API ===")
    
    # Nejprve zkusíme načíst z konkrétní cesty
    specific_path = "/Users/imac/Documents/GitHub/zastupitelstvo/.env"
    print(f"Načítám .env z: {specific_path}")
    load_dotenv(specific_path)
    
    # Pak zkusíme načíst z aktuálního adresáře
    local_env = os.path.join(os.getcwd(), ".env")
    print(f"Načítám .env z: {local_env}")
    load_dotenv(local_env)
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ API klíč OPENROUTER_API_KEY nebyl nalezen v proměnných prostředí!")
        return False
    
    # Zobrazíme část klíče pro kontrolu
    print(f"Nalezen API klíč OPENROUTER_API_KEY: {api_key[:10]}... (délka: {len(api_key)})")
    
    # Testové volání OpenRouter API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://www.marigold.cz/",
        "X-Title": "Marigold.cz Test",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Řekni 'Test API funguje!' česky a velmi stručně."
            }
        ],
        "model": "google/gemini-2.0-flash-001",
        "max_tokens": 50,
        "temperature": 0.3
    }
    
    print("\nOdesílám testovací požadavek na OpenRouter API...")
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        print(f"Status kód odpovědi: {response.status_code}")
        response_json = response.json()
        print(f"Odpověď API: {response_json}")
        
        if response.status_code == 200 and "choices" in response_json:
            print("\n✅ Test API byl úspěšný!")
            return True
        else:
            print("\n❌ Test API selhal!")
            return False
    except Exception as e:
        print(f"\n❌ Chyba při komunikaci s API: {e}")
        return False

# Hlavní funkce
def main():
    print("=== Diagnostický nástroj pro .env a API ===")
    print_env_info()
    test_api()
    
    print("\nPro řešení problémů zkuste:")
    print("1. Vytvořit .env soubor v pracovním adresáři se správným API klíčem")
    print("2. Zkontrolovat, zda API klíč není exspirovaný")
    print("3. Zkontrolovat připojení k internetu")

if __name__ == "__main__":
    main() 