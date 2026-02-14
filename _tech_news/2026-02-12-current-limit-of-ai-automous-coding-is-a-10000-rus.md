---
author: Marisa Aigen
category: ai programování
companies:
- Anthropic
date: '2026-02-12 23:34:20'
description: Výzkumník Anthropic Nicholas Carlini nechal 16 instancí modelu Claude
  Opus 4.6 s minimálním dohledem vyvinout C kompilátor od nuly. Za dva týdny a přes
  2000 relací Claude Code za 20 000 USD vznikl funkční kompilátor v Rustu schopný
  zkompilovat bootovatelný Linux 6.9 kernel na x86, ARM a RISC-V.
importance: 4
layout: tech_news_article
original_title: Current Limit of AI Automous Coding is a 100,00 Rust Based C Compiler
  Built in 2 Weeks
people:
- Nicholas Carlini
publishedAt: '2026-02-12T23:34:20+00:00'
slug: current-limit-of-ai-automous-coding-is-a-10000-rus
source:
  emoji: 📰
  id: next-big-future
  name: Next Big Future
title: 'Současná hranice autonomního kódování AI: 100 000řádkový kompilátor C v Rustu
  postavený za 2 týdny'
url: https://www.nextbigfuture.com/2026/02/current-limit-of-ai-automous-coding-is-a-10000-rust-based-c-compiler-built-in-2-weeks.html
urlToImage: https://nextbigfuture.s3.amazonaws.com/uploads/2026/02/Screenshot-2026-02-12-at-3.33.12-PM.jpg
urlToImageBackup: https://nextbigfuture.s3.amazonaws.com/uploads/2026/02/Screenshot-2026-02-12-at-3.33.12-PM.jpg
---

## Souhrn
Výzkumník Anthropic Nicholas Carlini publikoval blogový příspěvek, ve kterém popsal, jak nasadil 16 instancí modelu Claude Opus 4.6 k autonomnímu vývoji C kompilátoru v jazyce Rust. S minimálním lidským zásahy a koordinací přes Git repo repozitář agentů vyrobili za dva týdny 100 000 řádků kódu, který zkompiluje bootovatelný Linux 6.9 kernel na architekturách x86, ARM i RISC-V. Experiment odhaluje praktickou hranici současného autonomního kódování AI kolem 100 000 řádků.

## Klíčové body
- 16 paralelních instancí Claude Opus 4.6 v samostatných Docker kontejnerech koordinovaných přes sdílený Git repozitář bez centrálního řízení.
- Celkové náklady přes 20 000 USD na API volání během téměř 2000 relací Claude Code.
- Výsledný kompilátor v Rustu zvládá multi-architekturový Linux kernel, což před rokem žádný model nezvládl ani s rozsáhlým dohledem.
- Klíčové inženýrské triky: kontextově závislé testování, časové limity úkolů a GCC oracle pro paralelizaci.
- Použití nové funkce „agent teams“ v Claude Opus 4.6 pro týmovou spolupráci agentů.

## Podrobnosti
Každá instance modelu Claude Opus 4.6 běžela v izolovaném Docker kontejneru, kde si agenti klonovali společný Git repozitář. Úkoly si nárokovali vytvořením lock souborů, implementovali kód a pushovali změny zpět. Bez centrálního orchestrátoru se agenti sami rozhodovali o prioritách na základě stavu repozitáře – například vybírali největší nevyřešené problémy. Konflikty při merge se řešily autonomně mezi agenty. Tento přístup minimalizoval lidský zásah na úrovni údržby infrastruktury a občasného řešení deadlocků.

Projekt C kompilátoru byl ideální testem díky stabilní specifikaci jazyka C, která je definována desetiletími a podpořena rozsáhlými testovými sadami. Kompilátor v Rustu – jazyce známém svou bezpečností paměti – musel zpracovat parsing, semantickou analýzu, optimalizace a generování strojového kódu pro tři architektury. Carlini, vědec z Anthropic Safeguards týmu (dříve sedm let v Google Brain a DeepMind), vyvinul triky jako context-aware test output (zobrazuje relevantní chyby v kontextu), time-boxing (omezení času na úkol pro prevenci zacyklení) a GCC oracle (použití referenčního GCC pro validaci a paralelizaci testů). Tyto metody udržovaly produktivitu agentů při složitých úkolech. Před rokem by takový výkon vyžadoval intenzivní lidskou supervizi; nyní stačil experiment s rozpočtem 20 000 USD.

## Proč je to důležité
Tento experiment demonstruje rychlý pokrok v agentických systémech AI pro software development, kde modely jako Claude Opus 4.6 zvládají komplexní projekty s minimálním dohledem. Zároveň odhaluje strop kolem 100 000 řádků, kde selhává koordinace a debugging bez lidského zásahu – klíčový limit pro průmyslové nasazení. Metodologie paralelních agentů přes Git a inženýrské triky představují příspěvek k širšímu ekosystému nástrojů pro autonomní kódování, jako jsou Devin nebo Cursor. Pro průmysl znamená potenciál akcelerace vývoje open-source projektů, ale vyžaduje investice do infrastruktury (Docker, Git) a náklady na API. V kontextu Anthropic, firmy zaměřené na bezpečné AI, podtrhuje to výzvy v bezpečnosti agentických systémů při velkém měřítku. Dlouhodobě to posouvá hranice směrem k AGI, ale aktuálně zůstává na úrovni semi-autonomních týmů.

---

[Číst původní článek](https://www.nextbigfuture.com/2026/02/current-limit-of-ai-automous-coding-is-a-10000-rust-based-c-compiler-built-in-2-weeks.html)

**Zdroj:** 📰 Next Big Future
