---
slug: "fifo"
url: "/mobilnisite/slovnik/fifo/"
type: "slovnik"
title: "FIFO – First Input First Output"
date: 2026-01-01
abbr: "FIFO"
fullName: "First Input First Output"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fifo/"
summary: "Základní metoda řazení do fronty, kde jsou pakety zpracovávány přesně v pořadí, v jakém dorazí. V 3GPP se jedná o základní metodu plánování a ukládání do vyrovnávací paměti používanou ve vrstvách prot"
---

FIFO je základní metoda řazení do fronty (disciplína fronty) ve vrstvách protokolů 3GPP, kde jsou pakety zpracovávány a plánovány přesně v pořadí, v jakém dorazí, aby bylo zajištěno doručení ve správném pořadí, což poskytuje jednoduchost a spravedlnost.

## Popis

First Input First Output (FIFO) je klasický algoritmus řazení do fronty používaný v různých vrstvách protokolů zásobníku rádiového přístupu a jádra sítě 3GPP. Funguje na jednoduchém principu: entity (jako datové pakety nebo protokolové datové jednotky) jsou uloženy ve vyrovnávací paměti a entita, která čeká nejdéle (první vložená), je další na řadě ke zpracování nebo přenosu (první vyjmutá). Tím vzniká striktní časové pořadí. Ve specifikacích 3GPP je chování FIFO často výchozím nebo povinným režimem pro určité kanály a přenosy, zejména pro potvrzovací režim ([AM](/mobilnisite/slovnik/am/)) ve vrstvě řízení rádiového spoje (RLC).

Ve vrstvě RLC pro přenos dat v režimu AM udržuje vysílač přenosovou vyrovnávací paměť. PDCP PDU jsou doručeny do RLC a v případě potřeby segmentovány na RLC SDU. Ty jsou ukládány a přenášeny v pořadí FIFO. Také přijímací strana používá principy FIFO ve své vyrovnávací paměti pro opětovné sestavení, aby seřadila přijatá RLC PDU před jejich doručením ve správném pořadí do horní PDCP vrstvy. To zaručuje doručení ve správném pořadí do vyšších vrstev, což je základním požadavkem pro mnoho aplikací založených na TCP. Specifikace (např. TS 36.323, TS 38.323) podrobně popisují postupy, jako je řízení toku založené na okně a opakované přenosy [ARQ](/mobilnisite/slovnik/arq/), které fungují v součinnosti s tímto FIFO ukládáním do vyrovnávací paměti.

Mimo RLC se koncepty FIFO uplatňují u front plánování ve vrstvě [MAC](/mobilnisite/slovnik/mac/), ukládání do vyrovnávací paměti v uživatelských branách a funkcí správy provozu. Zatímco pokročilé plánovače používají složité algoritmy pro prioritu QoS, FIFO zůstává kritickou součástí pro toky určené jako non-GBR (nezaručená přenosová rychlost) nebo výchozí přenosy, kde je jednoduchá spravedlnost přijatelná. Jeho implementace je výpočetně nenáročná a vyžaduje minimální správu stavu ve srovnání s prioritními frontami. Jeho jednoduchost je však také omezením, protože neupřednostňuje provoz citlivý na zpoždění, což jej činí nevhodným pro služby v reálném čase bez dalších mechanismů QoS ve vyšší vrstvě.

## K čemu slouží

FIFO existuje jako základní, spolehlivá metoda pro správu datových front v telekomunikačních systémech. Jeho hlavním účelem je zajistit předvídatelné doručení datových jednotek ve správném pořadí, což je základní požadavek pro komunikaci bez chyb. Před přijetím sofistikovaných plánovačů s ohledem na QoS byla FIFO de facto metodou pro zpracování veškerého provozu, poskytující jednoduchou formu spravedlnosti, kde jsou všechny datové toky obsluhovány postupně na základě času příchodu.

V systémech 3GPP byla standardizována, aby poskytla jasné, interoperabilní základní chování pro protokolové entity, jako je vrstva RLC. Tím se řeší problém, jak spolehlivě rekonstruovat datový proud z potenciálně nesprávně seřazených nebo opakovaně přenášených paketů přes nespolehlivý rádiový spoj. Disciplína FIFO na přijímací straně v kombinaci s pořadovými čísly umožňuje vrstvě RLC doručit dokonalý sekvenční proud do vrstvy PDCP, čímž skrývá složitosti rozhraní rádiového přístupu před protokoly vyšších vrstev.

Jeho pokračující specifikace řeší potřebu mechanismu záložního řešení s nízkou složitostí a robustností. Pro určité typy provozu na pozadí nebo provozu typu best-effort je režie složitého prioritního řazení do front zbytečná. FIFO poskytuje zaručené chování, které je snadné implementovat, testovat a ladit. Slouží jako referenční model, vůči kterému jsou porovnávány a optimalizovány pokročilejší algoritmy plánování (jako Proportional Fair, založené na QoS), což zajišťuje, že i ta nejzákladnější implementace udržuje stabilitu sítě a integritu dat.

## Klíčové vlastnosti

- Zaručuje zpracování a doručení paketů nebo protokolových datových jednotek ve správném pořadí
- Poskytuje vnitřní spravedlnost tím, že obsluhuje pakety na základě času příchodu
- Nízká implementační složitost a minimální režie zpracování
- Tvoří základní operaci pro přenos dat v potvrzovacím režimu (AM) vrstvy RLC
- Používá se při ukládání do vyrovnávací paměti pro výchozí přenosy a provoz typu non-GBR
- Slouží jako referenční model pro návrh a testování protokolů

## Související pojmy

- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)

## Definující specifikace

- **TS 22.104** (Rel-19) — Service requirements for cyber-physical control apps
- **TS 22.179** (Rel-20) — MCPTT Service Requirements
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TS 26.448** (Rel-19) — EVS Jitter Buffer Management Specification
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)

---

📖 **Anglický originál a plná specifikace:** [FIFO na 3GPP Explorer](https://3gpp-explorer.com/glossary/fifo/)
