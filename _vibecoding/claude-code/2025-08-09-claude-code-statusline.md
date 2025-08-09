---
author: Patrick Zandl
categories:
- AI
- Claude Code
- Anthropic
- vývojové nástroje
- terminál
layout: post
post_excerpt: Anthropic přidal do nástroje Claude Code možnost vytvářet přizpůsobitelné stavové řádky v terminálu pro zobrazení kontextových informací během programování.
summary_points:
- Claude Code získal funkci přizpůsobitelných stavových řádků v terminálu
- Stavové řádky se aktivují příkazem /statusline s popisem požadovaného zobrazení
- Funkce umožňuje zobrazovat git větve, pracovní adresář nebo aktuální počasí
- Stavové řádky dynamicky zobrazují informace relevantní pro aktuální pracovní kontext
title: Claude Code získal přizpůsobitelné stavové řádky pro terminál
---

Společnost Anthropic rozšířila 8. srpna 2025 možnosti svého nástroje Claude Code o funkci přizpůsobitelných stavových řádků přímo v terminálu. Novinka umožňuje vývojářům zobrazovat kontextové informace relevantní pro jejich práci bez nutnosti přepínat mezi okny nebo zadávat diagnostické příkazy.

## Aktivace a základní použití

Funkce se aktivuje příkazem `/statusline` následovaným popisem požadovaného zobrazení. Claude Code automaticky vygeneruje stavový řádek s požadovanými informacemi a dynamicky jej aktualizuje podle kontextu práce.

### Příklady použití

```bash
# Zobrazení základních informací o prostředí
/statusline show git branch and current directory

# Komplexní stavový řádek s více informacemi
/statusline display hostname, active Claude model, git branch, and full path

# Kreativní využití
/statusline add a digital buddy that keeps me company while coding

# Zobrazení času a systémových informací
/statusline show current time, username, and project status
```

Stavový řádek zobrazuje například aktuální větev v systému Git, pracovní adresář, název počítače, uživatelské jméno nebo stav repozitáře. Systém dokáže interpretovat požadavky v přirozeném jazyce a vytvořit funkční zobrazení včetně kreativních prvků jako “digitální společník” pro zpříjemnění práce.

## Technická implementace a praktické využití

Stavové řádky se aktualizují v reálném čase - při přepnutí větve v Gitu se automaticky zobrazí nový název, při změně adresáře se aktualizuje cesta. Systém využívá standardní terminálové sekvence, což zajišťuje kompatibilitu s většinou moderních emulátorů.

Příklad zobrazení ve stavovém řádku:

```
🕐 23:12:20 | 💻 Patrick-Zandl-MacBook | 🐙 Opus 4.1 | 🌿 anthropic | 📁 master |
```

Vývojáři tak mají neustále k dispozici informace o kontextu své práce bez opakovaného zadávání příkazů jako `git branch` nebo `pwd`. Namísto složitých konfigurací stačí popsat požadovanou funkcionalitu v přirozeném jazyce.

## Dostupnost

Funkce je dostupná ve všech aktuálních verzích [Claude Code](https://docs.anthropic.com/en/docs/claude-code), terminálového rozhraní pro práci s modelem Claude při programování. Pro využití není potřeba dodatečná konfigurace - stačí mít aktivní přístup k Claude Code a zadat příslušný příkaz.

Přizpůsobitelné stavové řádky představují další krok v integraci umělé inteligence do vývojářského pracovního postupu a součást průběžného rozšiřování možností nástroje Claude Code.