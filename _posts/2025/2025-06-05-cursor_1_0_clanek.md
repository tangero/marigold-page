---
audio_url: null
author: Patrick Zandl
categories:
- AI
- vibecoding
- Cursor
layout: post
sw: cursor
post_excerpt: Nejnovější verze nástroje pro AI programování je jedničkovou verzí. Za více než rok vývoje se od forku VS Code změnilo mnohé, firmě to vyneslo desetimiliardové ohodnocení. Jaké jsou tedy novinky? 
thumbnail: https://www.marigold.cz/assets/cursor-1.jpeg
title: "Cursor 1.0: Nové funkce pro AI programování / vibecoding"
---

Společnost Anysphere vydala verzi 1.0 svého AI editoru kódu Cursor, která přináší automatickou kontrolu kódu, rozšířený přístup k Background Agent a zjednodušenou integraci MCP protokolu. Vydání přichází více než rok po spuštění v roce 2023 a obsahuje sedm hlavních funkcí.

## Automatická kontrola kódu s BugBot

BugBot analyzuje změny v pull requestech pomocí AI modelů dostupných v Cursor. Nástroj identifikuje potenciální problémy v kódu před jeho začleněním do hlavní větve.

Systém nabízí tři režimy práce:
- **Automatické komentáře**: Při aktualizaci pull requestu BugBot znovu prověří kód a přidá komentáře k identifikovaným problémům
- **Manuální spuštění**: Aktivace příkazem `bugbot run` v komentáři
- **Přímá integrace**: Tlačítko "Fix in Cursor" otevře editor s předvyplněným promptem pro opravu

Nastavení vyžaduje administrátorská oprávnění pro Cursor i GitHub organizaci. Konfigurace probíhá na [cursor.com/settings](https://cursor.com/settings) v sekci Integrations. Uživatelé mohou nastavit čtyři různé režimy aktivace: automatické spouštění, pouze při zmínce, jednorázové spuštění na pull request, nebo skrytí komentářů když nejsou nalezeny problémy.

BugBot nabízí sedmidenní zkušební období s možností nastavení měsíčního limitu nákladů.

## Background Agent pro všechny uživatele

Funkce Background Agent, dříve omezená na early access, je nyní dostupná všem uživatelům. Umožňuje spouštění AI agentů v cloudu, kteří provádějí změny v kódu na pozadí.

Aktivace probíhá kliknutím na ikonu cloudu v chatu nebo zkratkou Cmd/Ctrl+E. Funkce není kompatibilní s režimem soukromí (Privacy mode), který je nutné před použitím deaktivovat.

Background Agent přináší několik bezpečnostních aspektů, které je třeba zvážit:
- Vyžaduje udělení read-write oprávnění GitHub aplikaci pro práci s repozitáři
- Kód se spouští v AWS infrastruktuře Anysphere
- Automaticky spouští všechny příkazy, což může vystavit systém prompt injection útokům
- Při vypnutém privacy módu se ukládají prompty a vývojová prostředí pro zlepšování produktu
- Citlivé údaje se ukládají šifrovaně pomocí KMS do databáze

Anysphere upozorňuje, že infrastruktura zatím nebyla auditována třetími stranami. Pro projekty s citlivými daty doporučuje zvážit použití této funkce.

## Podpora Jupyter notebooků

Cursor může nyní provádět změny přímo v Jupyter noteboocích. Agent dokáže vytvářet a upravovat více buněk současně. Funkce je omezena na modely řady Sonnet.

Jupyter notebooky jsou interaktivní vývojové prostředí používané především v datové vědě a machine learningu pro kombinování kódu, vizualizací a dokumentace.

## Memories - projektová paměť

Funkce Memories umožňuje Cursor zapamatovat si informace z konverzací pro budoucí použití. Paměť je uložena na úrovni jednotlivých projektů a spravuje se v nastavení editoru.

Systém funguje pomocí příkazu "@Memory" (například "Please remember ___ @Memory"), který vytvoří projektové pravidlo a uloží data do adresáře .cursor/rules/. Memories jsou ve fázi beta testování a aktivují se v Settings → Rules.

## MCP protokol s jedním kliknutím

Model Context Protocol (MCP) představuje standardizovaný způsob připojení AI agentů k externím zdrojům dat. MCP funguje jako vrstva mezi jazykovými modely a API různých služeb, což eliminuje nutnost psát vlastní kód pro každou integraci.

Cursor 1.0 zjednodušuje instalaci MCP serverů. Místo manuálního nastavování přes "Add Custom MCP" nyní uživatelé navštíví stránku MCP tools, vyberou požadovaný nástroj a kliknou na "Add app to Cursor".

Aktuálně jsou podporovány servery pro GitHub, Stripe a Figma. Přibyla také OAuth podpora pro autentizaci serverů, které ji podporují.

## Bohatší odpovědi v chatu

Cursor nyní zobrazuje vizualizace přímo v konverzacích. Editor umí generovat a zobrazovat Mermaid diagramy a Markdown tabulky na jednom místě.

Mermaid je textový jazyk pro tvorbu diagramů a schémat, který umožňuje rychlé vytváření flowchartů a dalších vizualizací pomocí textové syntaxe.

## Nový dashboard a nastavení

Stránky nastavení a dashboardu byly přepracovány. Nový dashboard zobrazuje individuální nebo týmové analytiky využití, umožňuje změnu zobrazovaného jména a poskytuje detailní statistiky podle nástrojů nebo modelů.

Dashboard nabízí nastavení časového rozsahu pro zobrazení trendů využití. V nastavení IDE lze upravit vzhled chatu a kontextového rozhraní.

## Další změny

Verze 1.0 obsahuje také menší vylepšení:

**Klávesové zkratky**:
- Cmd/Ctrl+E pro Background Agent

**Funkční rozšíření**:
- @Link a webové vyhledávání parsuje PDF soubory
- Síťová diagnostika v nastavení
- Paralelní volání nástrojů pro rychlejší odpovědi
- Možnost skládání nástrojů v chatu

**Správa účtů**:
- Podnikoví uživatelé mají přístup pouze ke stabilním verzím
- Týmoví administrátoři mohou zakázat Privacy Mode
- Admin API pro přístup k metrikám a výdajům

**Modely**:
- Max režim pro Gemini 2.5 Flash

## Technické pozadí a hodnocení

Cursor využívá různé jazykové modely pro analýzu kódu a generování návrhů. Mateřská společnost Anysphere je oceněna na 10 miliard dolarů. Background Agent běží na AWS infrastruktuře, což umožňuje zpracování bez zatížení lokálního počítače.

Významným přínosem verze 1.0 je automatizace kontroly kódu a rozšíření cloudových funkcí. Zjednodušená integrace MCP protokolu může urychlit adopci externích nástrojů. Nicméně některé funkce, jako Background Agent, vyžadují pečlivé zvážení bezpečnostních rizik, zejména pro organizace s citlivými daty.

Omezení na modely Sonnet u Jupyter notebooků a beta status funkcí jako Memories ukazují, že některé funkce jsou stále ve vývoji. Chybějící audit infrastruktury třetí stranou může být překážkou pro adoption v některých podnikových prostředích.

Uživatelé místy vyjadřují obavy ohledně technických problémů, jako je absence sdílených MCP serverů, což vede k vysoké paměťové náročnosti, a zastaralé verze VSCode používané Cursorem, což způsobuje problémy s rozšířeními. Tyto body naznačují, že i přes pozitivní odezvy existují výzvy, které mohou ovlivnit uživatelský zážitek.

Další feedback zahrnuje srovnání s konkurencí, například s Claude Code, kde někteří uživatelé považují Cursor za levnější ($20/měsíc oproti $200/měsíc u Claude Code), ale vyjádřili nespokojenost s výkonem, například „Podpora Pythonu byla minulý týden katastrofální, odinstaloval jsem to před měsíci kvůli tomu“ (Hacker News). Jiní uživatelé ocenili nové funkce, jako BugBot a rozšíření Background Agentů, ale přáli si vylepšení, například dostupnost Background Agentů i v režimu soukromí.

[Oficiální changelog](https://www.cursor.com/en/changelog)  poskytuje detailní přehled nových funkcí, včetně automatických kontrol kódu s BugBotem, rozšíření Background Agentů pro všechny uživatele a podpory Jupyter Notebooks, což odpovídá oznámení v X příspěvku a video.

