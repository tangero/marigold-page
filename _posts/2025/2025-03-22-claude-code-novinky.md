---
audio_url: null
author: Patrick Zandl
categories:
- Claude
- Anthropic
- vibe code
- AI
date: 2025-03-22 22:00:00
layout: post
summary_points:
- Claude Code podporuje rozšířené myšlení aktivované příkazy "think" pro plánování
  úkolů.
- Vim mód umožňuje zkušeným vývojářům úpravu promptů pomocí slash příkazu `/vim`.
- Vlastní slash příkazy se vytvářejí Markdown soubory v adresářích `.claude/commands/`.
- Claude Code nabízí web fetch, auto-accept, automatické doplňování cest a auto-compact.
thumbnail: https://www.marigold.cz/assets/claude-code-user.png
title: Nové funkce v Claude Code pro programování s AI
---

Svůj nástroj [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) pro "[vibe coding](/item/programovani-s-ai/)" představil Anthropic vcelku nedávno a zjevně nad ním dosti intenzivně vyšívá. Tento týden Anthropic představil několik zajímavých nových funkcí, které vývojářům pomohou pracovat rychleji a efektivněji. Takže se na to pojďme podívat. 

> 💡 Nevíte, co je [Claude Code](/ai/claude-code/)? Detailnější popis [jsme si přinesli zde](/ai/claude-code/). 

A co je nového?
* Obsah
{:toc}


## 1. Rozšířené myšlení (Extended thinking)

[Claude Code](/ai/claude-code/) nyní podporuje mód "rozšířeného myšlení", který je poháněn modelem Claude 3.7 Sonnet. Stačí požádat Claude, aby "přemýšlel" (například příkazy "think", "think more" nebo "think harder"), a aktivujete tuto schopnost.

**Tip pro praxi:** Nejprve informujte Claude o vašem úkolu a nechte ho získat kontext z vašeho projektu. Poté ho požádejte, aby "přemýšlel" a vytvořil plán. Intenzita přemýšlení se liší podle použitých slov - například "think hard" spustí intenzivnější proces přemýšlení než samotné "think".

Tato funkce je zvláště užitečná pro větší úkoly vyžadující plánování, jako jsou refaktorizace kódu.

## 2. Vim mód

Pro zkušené vývojáře, kteří rádi používají Vim, nabízí [Claude Code](/ai/claude-code/) novou funkci Vim módu. Použijte slash příkaz `/vim` k aktivaci insert/command módů pro úpravu promptů.

![Claude code vim](/assets/claude-code-vim.png)

## 3. Vlastní slash příkazy

Nyní si můžete vytvořit vlastní pracovní postupy (jako například "třídění GitHub issues") přidáním souborů do adresářů `.claude/commands/` nebo `~/.claude/commands/`.

Vytvořte personalizované workflow, které lze kdykoliv vyvolat jako slash příkazy. Jednoduše přidejte Markdown soubory do těchto adresářů a obsah těchto souborů se stane novými příkazy.

Můžete vytvářet příkazy pro běžné workflow jako "kontrola pravopisu kódu" nebo "dotaz na Sentry logy a následně bisect ke git commitu". Představte si je jako uložené postupy pro úkoly, které chcete provádět častěji.

Vlastní slash příkazy jsou v podstatě způsob, jak si vytvořit vaše vlastní přizpůsobené workflow nebo často používané instrukce, které můžete v [Claude Code](/ai/claude-code/) rychle vyvolat pomocí příkazu začínajícího lomítkem (/).

![Claude Code user](/assets/claude-code-user.png)

Funguje to takto:

1. **Vytvoření vlastního příkazu**:
   - Vytvořte Markdown soubor (soubor s příponou `.md`)
   - Tento soubor umístěte do jednoho ze dvou adresářů:
     - `.claude/commands/` (lokální adresář v projektu)
     - `~/.claude/commands/` (globální adresář ve vašem domovském adresáři)

2. **Struktura souboru**:
   - Název souboru určuje název příkazu. Například soubor pojmenovaný `triage-issues.md` vytvoří příkaz, který můžete vyvolat pomocí `/triage-issues`.
   - Obsah souboru obsahuje instrukce nebo kroky, které chcete, aby [Claude Code](/ai/claude-code/) provedl.

3. **Použití příkazu**:
   - Když pracujete v [Claude Code](/ai/claude-code/), jednoduše napíšete `/` následované názvem vašeho příkazu (bez přípony `.md`).
   - Claude Code automaticky načte obsah příslušného souboru a provede instrukce v něm obsažené.

4. **Příklady možných použití**:
   - `/triage-issues` - Mohlo by zkontrolovat všechny otevřené GitHub issues, kategorizovat je podle priority a navrhnout akční plány.
   - `/code-review` - Mohlo by provést automatickou kontrolu kódu podle vašich standardů.
   - `/deploy-checklist` - Mohlo by projít seznam kontrolních bodů před nasazením.
   - `/analyze-logs` - Mohlo by načíst a analyzovat logy z vašeho systému.
   - `/document-function` - Mohlo by automaticky generovat dokumentaci pro vybranou funkci.

5. **Výhody**:
   - Ušetří čas při opakujících se úkolech
   - Zajistí konzistenci při provádění běžných postupů
   - Umožňuje sdílet užitečné workflow s týmem (pokud jsou v repozitáři projektu)
   - Redukuje potřebu pamatovat si složité příkazy nebo postupy

Tyto vlastní příkazy jsou obzvláště užitečné pro opakující se úkoly specifické pro váš projekt nebo osobní workflow. Můžete je chápat jako "makra" nebo "automatizované skripty", které Claude Code provede místo vás, ale s inteligencí a schopností adaptace AI asistenta.


## 4. Zlepšená latence nástrojů

Běžné operace (včetně Git operací) jsou nyní mnohem svižnější, což zlepšuje celkový zážitek z používání.

## 5. Režim auto-accept

Použijte Shift+Tab k zapnutí tohoto režimu, ve kterém Claude vytváří změny bez zastavování a žádání o povolení v každém kroku.

To je zvláště užitečné pro opakující se úlohy, kde Claude postupuje správným směrem. Vždy můžete režim auto-accept ukončit, pokud potřebujete konkrétní změnu důkladněji zkontrolovat.

## 6. Automatické doplňování cest k souborům

Stiskněte Tab při psaní a Claude Code navrhne soubory/cesty k souborům odpovídající vašemu vstupu.

Jde o významné vylepšení kvality života při hledání souborů, které chcete explicitně odkazovat.

## 7. Auto-compact pro správu kontextu

Claude Code automaticky kompaktuje historii konverzace při zachování důležitých informací, takže můžete pracovat na složitějších problémech bez obav o limity kontextu.

## 8. Web fetch

Vložte URL do Claude Code a on načte obsah z této webové stránky jako kontext.

![Claude Code web fetch](/assets/claude-code-web-fetch.png)

To je velmi užitečné pro omezení přepínání mezi Claude Code a prohlížečem. Tato funkce je ideální pro načítání dokumentace, specifikací nebo referenčních implementací bez nutnosti opustit terminál.

---

Všechny tyto funkce jsou dostupné nyní, stačí restartovat aplikaci, abyste měli jistotu, že používáte nejnovější verzi.

A pokud jste Claude Code ještě nenainstalovali, můžete ho stáhnout pomocí:
```
npm install -g @anthropic-ai/claude-code
```

Claude Code se stále vyvíjí a tým za ním slibuje v nadcházejících týdnech další nové funkce. S těmito vylepšeními se Claude Code stává ještě silnějším nástrojem pro vývojáře, kteří chtějí využít sílu AI při svém každodenním vývoji.

> 💡 Co je Claude Code a jak vám pomůže při vývoji software? Detailnější popis [jsme si přinesli zde](/ai/claude-code/).