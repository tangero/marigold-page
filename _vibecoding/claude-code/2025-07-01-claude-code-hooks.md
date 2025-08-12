---
layout: vibecoding-default
summary_points:
- Claude Code představil funkci Hooks pro automatizaci a rozšíření možností nástroje
- Hooks umožňují spouštět skripty před a po použití nástrojů jako jsou Bash, Write nebo Edit
- Systém podporuje validaci příkazů, automatické formátování kódu a vlastní notifikace
- Konfigurace probíhá pomocí JSON souborů s možností nastavení na úrovni uživatele nebo projektu
- Funkce zahrnuje bezpečnostní opatření včetně kontroly vstupu a omezení přístupu k citlivým souborům
- Podporuje také práci s MCP (Model Context Protocol) nástroji
title: "Claude Code Hooks"
---

Anthropic rozšířil svůj nástroj Claude Code o novou funkci nazvanou Hooks, která umožňuje vývojářům automatizovat různé úkoly a rozšířit možnosti tohoto nástroje pro práci s umělou inteligencí v příkazové řádce. Systém umožňuje spouštět vlastní skripty při specifických událostech během používání Claude Code.

## Princip fungování Hooks

Hooks fungují jako automatické spouštěče, které reagují na čtyři základní typy událostí v Claude Code. Systém **PreToolUse** se aktivuje před použitím nástroje a umožňuje například validaci příkazů nebo kontrolu bezpečnosti. **PostToolUse** se spouští po dokončení operace a hodí se pro úkoly jako je formátování kódu nebo zápis do logů. **Notification** slouží pro zasílání upozornění, zatímco **Stop** umožňuje reakci na ukončení procesů.

Každý hook obsahuje matcher (vzor pro rozpoznání nástroje) a samotný příkaz, který se má spustit. Například při použití nástroje Bash může hook automaticky validovat příkaz před jeho spuštěním a zabránit potenciálně nebezpečným operacím.

## Konfigurace a nastavení

Konfigurace Hooks probíhá prostřednictvím JSON souborů, které se ukládají do adresáře `.claude`. Systém podporuje tři úrovně konfigurace: globální nastavení v `~/.claude/settings.json`, projektové nastavení v `.claude/settings.json` a lokální nastavení v `.claude/settings.local.json`.

Základní struktura konfigurace vypadá následovně:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\""
          }
        ]
      }
    ]
  }
}
```

Systém podporuje regulární výrazy pro matchování nástrojů, což umožňuje vytvářet hooks pro skupiny podobných nástrojů. Například `Write|Edit|MultiEdit` zachytí všechny nástroje pro editaci souborů.

## Praktické využití

Hooks nachází uplatnění v několika oblastech. Pro **automatické formátování kódu** můžete nastavit hook, který po každé editaci souboru spustí příslušný formátovač kódu podle typu souboru. **Validace příkazů** umožňuje kontrolovat bash příkazy před jejich spuštěním a například doporučit použití modernějších alternativ.

Další možností je **logování aktivit**, kdy hooks zapisují informace o všech provedených operacích do souboru pro pozdější analýzu. Systém také podporuje **vlastní notifikace**, které mohou informovat o dokončení dlouhotrvajících úloh.

Praktickým příkladem je **kontrola pojmenování souborů**. Hook může zajistit konzistentní pojmenování souborů podle snake_case konvence. Konfigurace vypadá následovně:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/file-naming-validator.py"
          }
        ]
      }
    ]
  }
}
```

Validační skript kontroluje název souboru a pokud neodpovídá snake_case konvenci, vrátí exit kód 2 s návrhem správného názvu. Když Claude Code navrhne vytvoření souboru “gemini-service.py”, hook operaci zablokuje a zobrazí chybu: “Inconsistent file naming detected! Directory convention is snake_case. Suggested filename: gemini_service.py”. Tento přístup pomáhá udržet pořádek v projektech, kde AI často vytváří soubory s různými konvencemi pojmenování.

Na macOS lze využít **zvukové notifikace** pro upozornění na dokončení úloh. Hook typu Notification může spustit příkaz `afplay` pro přehrání zvukového souboru:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command", 
            "command": "afplay /System/Library/Sounds/Blow.aiff"
          }
        ]
      }
    ]
  }
}
```

Tento hook přehraje systémový zvuk při každé notifikaci z Claude Code, což je užitečné při dlouhotrvajících operacích, kdy potřebujete upozornění na dokončení úkolu.

## Výstup a kontrola chování

Hooks mohou ovlivnit chování Claude Code prostřednictvím návratových kódů. **Exit kód 0** označuje úspěšné provedení, **exit kód 2** blokuje provedení nástroje a zobrazí chybovou zprávu uživateli, zatímco ostatní kódy způsobí zobrazení chyby bez blokování.

Pro pokročilejší kontrolu podporuje systém JSON výstup, který umožňuje detailnější řízení chování. Můžete například nastavit `"decision": "block"` pro zablokování operace nebo `"suppressOutput": true` pro skrytí výstupu z transkriptu.

## Bezpečnostní aspekty

Systém obsahuje několik bezpečnostních opatření. Hooks by měly vždy validovat a sanitizovat vstupní data, používat absolutní cesty k souborům a vyhýbat se přístupu k citlivým souborům jako `.env` nebo `.git`. Dokumentace zdůrazňuje, že hooks spouští libovolné příkazy na systému, proto je nutná opatrnost při jejich konfiguraci.

Mezi doporučené postupy patří použití uvozovek u shell proměnných, blokování path traversal útoků pomocí `..` a omezení přístupu k citlivým adresářům. Systém také podporuje debug režim spouštěný pomocí parametru `--debug`.

## Podpora MCP nástrojů

Hooks pracují i s nástroji Model Context Protocol (MCP), které používají specifické pojmenování ve formátu `mcp__<server>__<tool>`. Například `mcp__memory__create_entities` pro nástroje práce s pamětí nebo `mcp__filesystem__read_file` pro práci se soubory.

Tato integrace umožňuje vytvářet hooks pro pokročilé operace s různými službami a rozšířeními Claude Code, což výrazně zvyšuje možnosti automatizace.

## Výhody a omezení

Hooks představují významné rozšíření možností Claude Code, které umožňuje přizpůsobit nástroj specifickým potřebám vývojářů. Systém je flexibilní a podporuje širokou škálu použití od jednoduchého logování po komplexní validaci a formátování.

Omezením je však nutnost ruční konfigurace a potřeba znalosti shell skriptování pro pokročilé využití. Dokumentace také upozorňuje na bezpečnostní rizika spojená se spouštěním vlastních skriptů.

Funkce Hooks je k dispozici v [oficiální dokumentaci Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/claude-code/hooks) spolu s dalšími informacemi o konfiguraci a příklady použití.