---
author: Patrick Zandl
categories:
- AI
- Claude Code
- Anthropic
- Vývojářské nástroje
- Agentic coding
layout: post
post_excerpt: Léto s Claude Code bylo docela hutné. Pojďme si shrnout, co se objevilo ve verzích 1.0.82 až 1.0.123 za zásadní novinky. Vlastní agenti, vylepšené styly výstupu, pokročilou správu oprávnění a lepší integraci s vývojářskými workflow.
summary_points:
- Zavedení vlastních agentů pro specializované úkoly s příkazem /agents
- Nové výstupní styly Explanatory a Learning pro vzdělávací účely
- Vylepšená správa oprávnění s příkazem /permissions a automatická potvrzování
- Podpora pozadových příkazů (Ctrl-b) pro běžící servery a sledování logů
- Nativní integrace ripgrep pro rychlejší vyhledávání v kódu
- Pokročilá diagnostika s příkazem /context pro optimalizaci výkonu
title: Co je nového v Claude Code od léta do podzimu?
---

Claude Code od společnosti Anthropic zaznamenal mezi verzemi 1.0.82 až 1.0.123 významný vývoj s důrazem na zvýšení produktivity vývojářů prostřednictvím pokročilých funkcí pro správu projektů a automatizaci. Nejnovější verze 1.0.123 byla vydána před pouhými 17 hodinami, což dokládá aktivní vývoj tohoto nástroje pro agentic coding v terminálu.

Claude Code slouží jako agentic coding nástroj pracující přímo v terminálu, který dokáže porozumět celé struktuře kódu, editovat soubory, spouštět terminálové příkazy a řídit kompletní workflow vývojářských procesů prostřednictvím přirozených jazykových příkazů. Nástroj je dostupný pro systémy macOS, Linux i Windows a integruje se s populárními IDE jako VS Code nebo JetBrains.

## Vlastní agenti pro specializované úkoly

Nejvýznamnější novinkou byla implementace vlastních agentů ve verzi kolem července 2025. Vývojáři nyní mohou vytvářet specializované podagenty pro konkrétní úkoly pomocí příkazu `/agents`. Tato funkcionalita umožňuje definovat agenty s vlastními instrukcemi, který se zaměřují například na testování, dokumentaci nebo specifické programovací jazyky.

Agenty lze vyvolávat pomocí @-mentions s automatickým doplňováním (`@<název-agenta>`). Systém také podporuje typeahead pro snazší správu a editaci agentů prostřednictvím souborů v adresáři `~/.claude/*`. Pro vývojáře, kteří pracují v týmech, je k dispozici funkce ukládání nastavení agentů do `.claude/settings.json` pro sdílení mezi členy projektu.

[Agenty detailněji rozebíráme zde.](https://www.vibecoding.cz/claude_code_subagenti/) 

## Vylepšené styly výstupu a vzdělávací funkce

Verze přinesly nové vestavěné výstupní styly "Explanatory" a "Learning", které jsou určeny pro vzdělávací účely. Tyto styly přizpůsobují způsob, jakým Claude prezentuje informace - explanatory styl poskytuje podrobnější vysvětlení procesů, zatímco learning styl se zaměřuje na postupné učení s praktickými příklady.

Vývojáři mohou tyto styly kombinovat s vlastními agenty pro vytváření specializovaných vzdělávacích asistentů, například pro onboarding nových členů týmu nebo vysvětlování složitých částí kódové základny.

## Pokročilá správa oprávnění a bezpečnost

Systém správy oprávnění prošel zásadním přepracováním. Příkaz `/allowed-tools` byl přejmenován na `/permissions`, který nyní poskytuje granulární kontrolu nad tím, které nástroje může Claude používat. Nová funkcionalita "Ask permissions" zajišťuje, že Claude vždy požádá o potvrzení před použitím specifických nástrojů.

Pro pokročilejší uživatele je k dispozici auto-accept režim s možností okamžitého přerušení pomocí klávesy ESC. Windows uživatelé získali vylepšené kontroly oprávnění pro allow/deny nástroje a project trust, s lepším zpracováním cest ve formátu POSIX.

## Příkazy na pozadí a workflow

Implementace příkazů běžících na pozadí prostřednictvím Ctrl-b představuje významné zlepšení produktivity. Vývojáři mohou spouštět dlouhotrvající procesy jako development servery nebo sledování logů na pozadí, zatímco Claude pokračuje v práci na dalších úkolech. Tato funkce řeší častý problém při vývoji, kdy je potřeba udržovat běžící procesy při současné práci na kódu.

Doplňuje to customizovatelný status řádek (`/statusline`), který umožňuje přidat terminálový prompt přímo do Claude Code pro lepší přehled o aktuálním stavu systému.

## Nativní ripgrep a výkonnostní optimalizace

Významnou novinkou je použití vestavěného ripgrep jako výchozího nástroje pro vyhledávání. Ripgrep je extrémně rychlý nástroj pro vyhledávání v textu, který výrazně zrychluje práci s velkými kódovými základnami. Uživatelé mogeou toto chování vypnout nastavením `USE_BUILTIN_RIPGREP=0`.

Linux uživatelé získali podporu pro Alpine a musl-based distribuce, i když vyžadují samostatnou instalaci ripgrep. Výkonnostní optimalizace se dotkly také renderování zpráv při práci s velkými kontexty.

## Diagnostika a optimalizace kontextu

Verze 1.0.86 představila příkaz `/context`, který poskytuje detailní breakdown tokenů napříč MCP nástroji, vlastními agenty a memory soubory. Tato funkcionalita je klíčová pro "Context Engineers" - vývojáře, kteří potřebují optimalizovat výkon Claude Code při práci s velkými projekty.

Příkaz zobrazuje, kolik tokenů spotřebovávají jednotlivé komponenty systému, což umožňuje identifikovat a řešit úzká místa ve výkonu. Doplňuje to vylepšený `/doctor` příkaz s kontextem CLAUDE.md a MCP nástrojů pro samostatnou diagnostiku problémů.

## Podpora pro MCP a integrační možnosti

Model Context Protocol (MCP) servery získaly rozšířenou funkcionalitu včetně podpory pro OAuth autorizaci, streamovací HTTP servery a vzdálené servery přes SSE a HTTP. MCP resources lze nyní zmínit pomocí @-mentions, což zlepšuje integraci externích služeb do workflow.

SDK podpora byla rozšířena o TypeScript (`npm install @anthropic-ai/claude-code`) a Python (`pip install claude-code-sdk`) varianty s callbackem `canUseTool` pro potvrzování nástrojů. Tato rozšíření umožňují vývojářům integrovat Claude Code do vlastních aplikací a workflow.

## Vylepšení pro enterprise používání

Pro enterprise zákazníky přibyly OTEL (OpenTelemetry) metriky zahrnující informace o typu operačního systému, verzi, architektuře hostitele a WSL verzi pro Windows Subsystem for Linux. To umožňuje lepší monitoring a diagnostiku v enterprise prostředích.

Konfigurace byla rozšířena o `ANTHROPIC_DEFAULT_SONNET_MODEL` a `ANTHROPIC_DEFAULT_OPUS_MODEL` pro kontrolu aliasů modelů, což je užitečné pro organizace s vlastními preferencemi modelů nebo compliance požadavky.

_Tak co se vám z toho nejvíce líbí? Mě hodně bodly ty příkazy běžící na pozadí!_