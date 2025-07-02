---
author: Patrick Zandl
categories:

- AI
- Claude Code
- Anthropic
- programování
- vývojové nástroje
layout: post
post_excerpt: Komplexní průvodce Claude Code - terminálový nástroj pro programátory od Anthropic. Od instalace po pokročilé techniky práce s hooks a MCP servery.
summary_points:
- Claude Code je terminálový nástroj umělé inteligence od Anthropic pro programátory
- Nabízí různé způsoby instalace včetně NPM, Homebrew a Docker kontejnerů
- Hooks umožňují automatizaci a kontrolu činností před a po spuštění nástrojů
- MCP protokol rozšiřuje možnosti o externí služby a databáze
- Bezpečnostní nastavení vyžaduje pečlivou konfiguraci oprávnění
- Komunita vytváří rozsáhlé kolekce příkazů a pracovních postupů
title: Claude Code - Komplexní průvodce AI nástrojem pro programátory
sw: claude-code
---


Claude Code společnosti Anthropic představuje pokročilý terminálový nástroj umělé inteligence určený přímo pro vývojáře. Tento nástroj představuje posun od tradičních chatových rozhraní k plnohodnotné integraci AI do vývojového prostředí. Claude Code umožňuje programátorům pracovat s AI asistentem přímo z příkazové řádky a automatizovat komplexní vývojové úlohy. Pojďme se podívat na to, jak s ním začít pracovat.

## Instalace a základní nastavení

Claude Code nabízí několik způsobů instalace podle platformy a preferencí vývojáře.

### Metody instalace

**NPM instalace (oficiální způsob)**

```bash
npm install -g @anthropic-ai/claude-code
```

Vyžaduje Node.js verzi 18 nebo vyšší na macOS, Linux nebo WSL.

**Homebrew na macOS a Linux**

```bash
brew install anthropic/tap/claude-code
```

**Arch Linux pomocí AUR**

```bash
yay -S claude-code
```

**Docker kontejner**

```bash
docker pull ghcr.io/rchgrav/claudebox:latest
docker run -it -v "$PWD":"$PWD" -w "$PWD" ghcr.io/rchgrav/claudebox:latest
```

**Windows přes WSL**
Anthropic doporučuje použití WSL2 s Ubuntu distribucí:

```bash
sudo apt update && sudo apt install -y nodejs npm
npm install -g @anthropic-ai/claude-code
```

### Systémové požadavky

Claude Code vyžaduje minimálně Node.js 16+, API klíč od Anthropic, 4GB RAM (doporučeno 8GB+ pro velké projekty) a internetové připojení pro API volání.

## Konfigurace API klíče

Po instalaci je nutné nastavit API klíč z [Anthropic konzole](https://console.anthropic.com) nebo se přihlásit přes svůj Anthropic placený účet. U účtu Pro a vyšší máte určité množství práce s Code zdarma (či spíše v ceně).
```bash
export ANTHROPIC_API_KEY="sk-your-key-here"
```

Pro trvalé nastavení v Bash:

```bash
echo 'export ANTHROPIC_API_KEY="sk-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## Základní použití

Claude Code nabízí několik režimů práce:

**Interaktivní režim**

```bash
claude
```

Spustí interaktivní REPL pro konverzaci s AI.

**Jednorázový dotaz**

```bash
claude -p "analyzuj tento kód na bezpečnostní chyby"
```

**Pokračování předchozí session**

```bash
claude -c
```

## Správa oprávnění

Claude Code implementuje víceúrovňový systém oprávnění pro bezpečnou prácu:

### Úrovně oprávnění

**Interaktivní režim** - Dotazuje se na každou operaci, vhodný pro vývojovou práci
**Whitelist režim** - Předem schválené nástroje, vhodný pro automatizační skripty  
**Nebezpečný režim** - Přeskakuje všechna oprávnění, pouze pro izolované prostředí

```bash
# Specifická oprávnění
claude --allowedTools "Edit,View"

# Kategorické oprávnění
claude --allowedTools "Edit,View,Bash"

# Omezená bash oprávnění
claude --allowedTools "Bash(git:*)"
```

**Kritické upozornění:** Nebezpečný režim `--dangerously-skip-permissions` používejte pouze v izolovaných Docker kontejnerech, nikdy na produkčních systémech.

## MCP - Model Context Protocol

MCP rozšiřuje možnosti Claude Code o připojení k externím službám, databázím a API. Protokol umožňuje integraci s:

- **Databáze** - PostgreSQL, MySQL, SQLite
- **Verzovací systémy** - Git, GitHub
- **Souborové systémy** - Lokální i vzdálené
- **Vyhledávání** - Brave Search, další vyhledávače

### Konfigurace MCP serverů

MCP servery se konfigurují v souboru `~/.claude.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"],
      "env": {}
    },
    "github": {
      "type": "stdio", 
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token-here"
      }
    }
  }
}
```

### Správa MCP

```bash
claude mcp                    # Interaktivní konfigurace
claude mcp list              # Seznam nakonfigurovaných serverů
claude mcp add <name> <cmd>  # Přidání nového serveru
```

## Hooks - Automatizace a kontrola

Hooks představují pokročilou funkcionalnost pro automatizaci a kontrolu operací Claude Code. Umožňují spouštění vlastních skriptů před nebo po použití nástrojů.

### Typy hooks

**PreToolUse** - Spouští se před použitím nástroje, umožňuje validaci a blokování
**PostToolUse** - Spouští se po dokončení nástroje, vhodný pro formátování kódu
**Notification** - Reaguje na oznámení systému
**Stop** - Spouští se při ukončování Claude Code

### Konfigurace hooks

Hooks se konfigurují pomocí příkazu `/hooks` nebo přímo v konfiguračních souborech:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/scripts/validate-command.py"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command", 
            "command": "/usr/local/bin/prettier --write"
          }
        ]
      }
    ]
  }
}
```

### Pokročilé hooks s JSON výstupem

Hooks mohou vracet JSON pro detailní kontrolu:

```json
{
  "continue": true,
  "stopReason": "Důvod zastavení",
  "suppressOutput": false,
  "decision": "approve",
  "reason": "Vysvětlení rozhodnutí"
}
```

## Správa projektů a kontextu

### CLAUDE.md soubory

Soubory `CLAUDE.md` v kořenovém adresáři projektu poskytují Claude Code důležité informace o projektu:

```markdown
# Projekt: Webová aplikace

## Architektura
- Frontend: React 18 s TypeScript
- Backend: Node.js s Express
- Databáze: PostgreSQL 14

## Vývojové pokyny
- Používej TypeScript pro veškerý nový kód
- Dodržuj ESLint konfiguraci
- Piš testy pro nové funkce
```

### Slash příkazy

Claude Code podporuje systém slash příkazů pro rychlé akce:

```bash
/help       # Zobrazení nápovědy
/clear      # Vymazání konverzace  
/exit       # Bezpečné ukončení
/doctor     # Diagnostika systému
/config     # Správa konfigurace
/memory     # Editace paměti projektu
```

## Komunita a rozšíření

Kolem Claude Code se rychle formuje aktivní komunita vývojářů. Existují rozsáhlé kolekce příkazů a pracovních postupů:

### Awesome Claude Code

Projekt [awesome-claude-code](https://github.com/awesome-claude-code) obsahuje kurátorovaný seznam zdrojů:

- **Pracovní postupy** - Kompletní řešení pro specifické úlohy
- **Slash příkazy** - Přes 80 specializovaných příkazů
- **CLAUDE.md soubory** - Šablony pro různé typy projektů
- **Nástroje třetích stran** - Rozšíření a integrace

### Příklady specializovaných příkazů

**Verzování a Git**

- `/commit` - Vytváří Git commity s konvenčním formátem
- `/create-pr` - Automatizuje vytváření pull requestů
- `/bug-fix` - Systematický přístup k opravě chyb

**Analýza kódu a testování**

- `/tdd-implement` - Implementace metodologie Test-Driven Development
- `/code_analysis` - Pokročilá analýza kódu včetně optimalizací
- `/check` - Komplexní kontrola kvality a bezpečnosti

**Dokumentace**

- `/create-docs` - Generování dokumentace z kódu
- `/update-docs` - Aktualizace existující dokumentace
- `/add-to-changelog` - Správa changelogů

## Bezpečnostní doporučení

### Osvědčené postupy

**Validace vstupů** - Vždy validujte a sanitizujte vstupy do hooks
**Citování proměnných** - V shell skriptech používejte `"$VAR"` místo `$VAR`
**Absolutní cesty** - Vyhněte se relativním cestám v kritických operacích
**Ochrana citlivých souborů** - Vylučte `.env`, `.git/` a další citlivé adresáře

### Konfigurace oprávnění

```bash
# Doporučené minimální oprávnění
claude --allowedTools "View"

# Postupné rozšiřování
claude --allowedTools "Edit,View"

# Omezený bash přístup
claude --allowedTools "Edit,View,Bash(git:*)"
```

## Řešení problémů

### Časté problémy

**Chyby autentifikace**

```bash
echo $ANTHROPIC_API_KEY  # Kontrola API klíče
claude -p "test" --verbose  # Test připojení
```

**Problémy s instalací**

```bash
npm uninstall -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code
node --version  # Ověření verze Node.js 16+
```

**MCP servery nefungují**

```bash
claude mcp status          # Stav serverů
claude mcp restart --all   # Restart všech serverů
claude --mcp-debug        # Debug režim
```

### Diagnostické nástroje

```bash
claude --version    # Verze Claude Code
claude --help       # Nápověda
claude config list  # Seznam nastavení  
claude /doctor      # Komplexní diagnostika
```

## Automatizace a CI/CD integrace

Claude Code lze integrovat do CI/CD pipeline pro automatizované úlohy:

### GitHub Actions příklad

```yaml
name: Claude Code Review
on:
  pull_request:
    branches: [main]

jobs:
  claude-review:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '18'
    - name: Install Claude Code
      run: npm install -g @anthropic-ai/claude-code
    - name: Run Review
      env:
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      run: |
        claude -p "Zkontroluj změny na bezpečnostní problémy" \
        --allowedTools "View" \
        --output-format json > review-results.json
```

### Pre-commit hooks

```bash
#!/bin/bash
# .git/hooks/pre-commit

staged_files=$(git diff --cached --name-only)
if [ -n "$staged_files" ]; then
  echo "$staged_files" | xargs cat | \
  claude -p "Zkontroluj tyto změny před commitem" \
  --allowedTools "View"
fi
```

## Budoucnost a vývoj

Claude Code představuje významný posun ve způsobu, jak vývojáři pracují s umělou inteligencí. Místo izolovaných chatových rozhraní nabízí hlubokou integraci do vývojového workflow. Očekává se rychlý vývoj ekosystému s novými MCP servery, hooks a komunitními nástroji.

Klíčové trendy zahrnují rozšíření MCP protokolu o další služby, vývoj vizuálních nástrojů pro konfiguraci, integraci s populárními IDE a vznik specializovaných distribucí pro konkrétní vývojové scénáře.

Claude Code tak nereprezentuje pouze nový nástroj, ale základ pro budoucnost AI-asistované softwarové výroby, kde umělá inteligence není externí pomocník, ale integrovaná součást vývojového prostředí.