---
author: Patrick Zandl
date: 2025-06-13
layout: post
post_excerpt: Anthropic představil vývojářskou sadu pro Claude Code, která umožňuje začlenění AI asistenta do aplikací. Sada podporuje neinteraktivní režim, vícekrokové rozhovory a MCP protokol.
summary_points:
- Vývojářská sada Claude Code umožňuje začlenění AI asistenta do aplikací
- Podporuje neinteraktivní režim, vícekrokové rozhovory a vlastní systémové výzvy
- Nabízí tři výstupní formáty: text, JSON a proudový JSON
- Protokol Model Context rozšiřuje funkce o externí nástroje
- Sada momentálně podporuje příkazovou řádku, verze pro TypeScript a Python jsou v přípravě
- Praktické využití zahrnuje automatizaci pracovních postupů GitHub a kontrolu kódu
title: "Anthropic vydal SDK pro Claude Code pro začlenění AI vývoje do aplikací třetích stran"
---

Anthropic vydal vývojářskou sadu pro Claude Code, která vývojářům umožňuje začlenit AI asistenta do vlastních aplikací. Sada zpřístupňuje funkce Claude Code jako podproces a poskytuje základ pro vytváření vývojářských nástrojů s umělou inteligencí využívajících schopnosti modelu Claude.

## Základní funkcionalita

Vývojářská sada Claude Code umožňuje používat Claude Code v neinteraktivním režimu z aplikací. Sada momentálně podporuje použití přes rozhraní příkazové řádky, zatímco verze pro TypeScript a Python jsou ve vývoji. Základní použití spočívá v zavolání Claude s konkrétním dotazem a získání odpovědi.

Vývojáři mohou využít všechny možnosti příkazové řádky dostupné v Claude Code. Klíčové parametry zahrnují `--print` pro neinteraktivní režim, `--output-format` pro specifikaci výstupního formátu, `--resume` pro obnovení rozhovoru podle identifikátoru relace a `--continue` pro pokračování nejnovějšího rozhovoru. Parametr `--max-turns` omezuje počet agentních tahů v neinteraktivním režimu.

## Vícekrokové rozhovory a správa relací

Sada podporuje pokračování rozhovorů napříč více interakcemi. Vývojáři mohou obnovit konkrétní rozhovor pomocí identifikátoru relace nebo automaticky pokračovat v nejnovější relaci. Tato funkcionalita umožňuje vytváření komplexnějších AI asistentů, kteří si pamatují kontext předchozích interakcí.

Pro řízení chování Claude lze definovat vlastní systémové výzvy pomocí parametru `--system-prompt`, který kompletně přepíše výchozí výzvu. Alternativně `--append-system-prompt` přidá instrukce k výchozí výzvě, což je vhodnější pro většinu případů použití.

## Podpora MCP

Významnou funkcí je podpora MCP, který rozšiřuje Claude Code o dodatečné nástroje a zdroje z externích serverů. Protokol umožňuje začlenění s databázemi, rozhraními aplikací či vlastními nástroji prostřednictvím konfiguračního souboru JSON.

Nastavení protokolu vyžaduje definování serverů ve formátu JSON a následné načtení pomocí parametru `--mcp-config`. Z bezpečnostních důvodů musí být nástroje protokolu výslovně povoleny pomocí `--allowedTools`. Názvy nástrojů následují vzor `mcp__<názevServeru>__<názevNástroje>`, kde názevServeru odpovídá klíči z konfiguračního souboru.

## Výstupní formáty

Sada nabízí tři výstupní formáty přizpůsobené různým potřebám začlenění:

**Textový výstup** představuje výchozí formát vracející pouze samotnou odpověď bez dodatečných metadat. Tento formát je vhodný pro jednoduché začlenění, kde stačí pouze obsah odpovědi.

**Výstup JSON** poskytuje strukturovaná data včetně metadat jako jsou statistiky rozhovoru, identifikátor relace a další informace užitečné pro strojové zpracování. Odpověď obsahuje pole `messages` s historií rozhovoru a pole `stats` s informacemi o průběhu.

**Proudový výstup JSON** proudí každou zprávu při jejím přijetí, což umožňuje zpracování v reálném čase u dlouhých odpovědí. Rozhovor začíná inicializační systémovou zprávou, pokračuje uživatelskými a asistenčními zprávami a končí závěrečnou systémovou zprávou se statistikami.

## Schéma zpráv a typování

Zprávy vrácené z rozhraní JSON jsou přísně typované podle definovaného schématu. Anthropic plánuje publikovat tyto typy ve formátu kompatibilním s JSONSchema a využívá sémantické verzování pro komunikaci zásadních změn v tomto formátu.

## Praktické využití a osvědčené postupy

Sada umožňuje jednoduché skriptování, zpracování souborů a správu relací. Pro strojovou analýzu odpovědí se doporučuje používat výstupní formát JSON. Vývojáři by měli implementovat řádné zpracování chyb kontrolou návratových kódů a chybového výstupu.

Při práci s vícekrokovými rozhovory je důležité využívat správu relací pro udržení kontextu. Pro dlouho běžící operace se doporučuje implementovat časové limity a při vícenásobných požadavcích respektovat omezení rychlosti přidáním zpoždění mezi volání.

## Reálné aplikace

Významným příkladem využití sady je začlenění Claude Code GitHub Actions, která poskytuje automatizované kontroly kódu, vytváření žádostí o sloučení a třídění problémů přímo v pracovním postupu GitHub. Tato integrace demonstruje potenciál sady pro automatizaci vývojářských procesů.

Sada otevírá možnosti pro vytváření vlastních vývojářských nástrojů s umělou inteligencí, automatizaci kódových kontrol, generování dokumentace nebo implementaci chatbotů pro technickou podporu. Pružnost formátů a podpora protokolu Model Context umožňuje začlenění s existujícími systémy a pracovními postupy.

Anthropic poskytuje kompletní [dokumentaci použití příkazové řádky](https://docs.anthropic.com/en/docs/claude-code/cli-usage), [začlenění GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions) a [návody](https://docs.anthropic.com/en/docs/claude-code/tutorials) pro běžné případy použití. Vývojářská sada představuje významný krok k dostupnosti pokročilých schopností umělé inteligence pro vývojářskou komunitu.