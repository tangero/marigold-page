# OpenRouter Chat

Jednoduchá desktopová aplikace pro chatování s různými AI modely přes OpenRouter API.

## Funkce

- Podpora mnoha AI modelů (Claude, GPT-4, LLaMA, Mistral atd.)
- Jednoduchý přepínač mezi modely
- Uchovávání historie konverzace
- Jednoduché GUI rozhraní

## Instalace

1. Nainstalujte Python 3.8 nebo novější
2. Nainstalujte potřebné knihovny:

```bash
pip install -r chat_requirements.txt
```

3. Vytvořte `.env` soubor v kořenové složce projektu a přidejte svůj OpenRouter API klíč:

```
OPENROUTER_API_KEY=váš_api_klíč_zde
```

## Získání OpenRouter API klíče

1. Zaregistrujte se na [OpenRouter](https://openrouter.ai/)
2. Přejděte do sekce Dashboard a vygenerujte API klíč
3. Zkopírujte klíč do vašeho `.env` souboru

## Spuštění aplikace

```bash
python chat_app.py
```

## Použití

1. Vyberte AI model z rozbalovací nabídky
2. Napište zprávu do textového pole ve spodní části okna
3. Stiskněte Enter nebo tlačítko "Odeslat" pro odeslání zprávy
4. Pro nový řádek ve zprávě použijte Shift+Enter

## Poznámky

- Aplikace vyžaduje aktivní internetové připojení
- Použití OpenRouter API může být zpoplatněno podle vašeho tarifu
- Některé modely mohou mít omezení nebo specifické požadavky 