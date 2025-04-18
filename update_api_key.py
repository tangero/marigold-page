#!/usr/bin/env python3
import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv
import sys

def main():
    print("\n=== OpenRouter API Key Setup ===\n")
    
    # Zkontrolujeme existující API klíč
    try:
        load_dotenv()
        existing_key = os.getenv("OPENROUTER_API_KEY")
        if existing_key:
            print(f"Existující API klíč nalezen: {existing_key[:10]}...")
            print("\nChcete nahradit stávající API klíč? (a/n): ", end='')
            if input().lower() != 'a':
                print("Zachovávám existující API klíč.")
                return
    except Exception as e:
        print(f"Chyba při načítání existujícího klíče: {e}")

    # Získání nového API klíče
    print("\nZpůsoby získání API klíče:\n")
    print("1. Zadat API klíč ručně (pokud již máte účet na OpenRouter)")
    print("2. Vytvořit nový účet a API klíč přes webový prohlížeč")
    print("\nVyberte možnost (1/2): ", end='')
    choice = input().strip()
    
    if choice == '1':
        print("\nZadejte váš OpenRouter API klíč: ", end='')
        api_key = input().strip()
    else:
        print("\nOtevřete tuto URL ve webovém prohlížeči a vytvořte účet/přihlaste se:")
        print("https://openrouter.ai/keys")
        print("\nPo přihlášení zkopírujte váš API klíč a vložte ho sem: ", end='')
        api_key = input().strip()
    
    if not api_key.startswith("sk-or-"):
        print("\n⚠️ Varování: Klíč nevypadá jako validní OpenRouter API klíč (měl by začínat 'sk-or-').")
        print("Chcete pokračovat i přesto? (a/n): ", end='')
        if input().lower() != 'a':
            print("Operace zrušena.")
            return
    
    # Otestujeme API klíč
    print("\nTestuji API klíč...")
    test_result, message = test_api_key(api_key)
    
    if test_result:
        print(f"✅ Test úspěšný: {message}")
        save_api_key(api_key)
        print("\n✅ API klíč byl úspěšně uložen do .env souboru.")
    else:
        print(f"❌ Test selhal: {message}")
        print("\nChcete i přesto uložit tento klíč? (a/n): ", end='')
        if input().lower() == 'a':
            save_api_key(api_key)
            print("\n⚠️ API klíč byl uložen, ale test selhal.")
        else:
            print("Operace zrušena.")

def test_api_key(api_key):
    """Otestuje API klíč zasláním jednoduchého požadavku."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://www.marigold.cz/",
        "X-Title": "Marigold.cz Test"
    }
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Řekni 'Test API klíče úspěšný!' velmi stručně."
            }
        ],
        "model": "google/gemini-2.0-flash-001",
        "max_tokens": 10,
        "temperature": 0.1
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            return True, "API klíč je funkční."
        else:
            return False, f"API vrátilo chybu: {response.status_code} - {response.text}"
    except Exception as e:
        return False, f"Chyba při testování: {str(e)}"

def save_api_key(api_key):
    """Uloží API klíč do .env souboru."""
    env_path = Path(".env")
    
    if env_path.exists():
        # Načteme existující obsah
        with open(env_path, 'r') as f:
            content = f.read()
        
        # Nahradíme nebo přidáme API klíč
        if "OPENROUTER_API_KEY=" in content:
            # Nahradíme existující klíč
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith("OPENROUTER_API_KEY="):
                    lines[i] = f"OPENROUTER_API_KEY={api_key}"
            
            new_content = '\n'.join(lines)
        else:
            # Přidáme nový klíč
            new_content = content.rstrip() + f"\nOPENROUTER_API_KEY={api_key}\n"
        
        with open(env_path, 'w') as f:
            f.write(new_content)
    else:
        # Vytvoříme nový .env soubor
        with open(env_path, 'w') as f:
            f.write(f"# OpenRouter API Key\nOPENROUTER_API_KEY={api_key}\n")
    
    # Nastavíme správná oprávnění
    try:
        env_path.chmod(0o600)  # Čtení a zápis pouze pro vlastníka
    except Exception as e:
        print(f"Varování: Nepodařilo se nastavit správná oprávnění: {e}")

if __name__ == "__main__":
    main() 