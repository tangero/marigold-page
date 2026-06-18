---
slug: "cfn"
url: "/mobilnisite/slovnik/cfn/"
type: "slovnik"
title: "CFN – Connection Frame Number"
date: 2025-01-01
abbr: "CFN"
fullName: "Connection Frame Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cfn/"
summary: "CFN je 12bitový čítač používaný pro číslování rádiových rámců v rámci vyhrazeného transportního kanálového spojení v UMTS. Poskytuje společný časový referenční bod mezi Node B a RNC pro synchronizaci,"
---

CFN je 12bitový čítač používaný v UMTS pro číslování rádiových rámců, který poskytuje společný časový referenční bod mezi Node B a RNC pro synchronizaci přes rozhraní UTRAN.

## Popis

Connection Frame Number (CFN) je základní synchronizační mechanismus v rádiové přístupové síti UMTS ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně pro vyhrazené kanály ([DCH](/mobilnisite/slovnik/dch/)). Jde o 12bitový čítač s cyklem od 0 do 4095, který jednoznačně čísluje každý 10ms rádiový rámec asociovaný s konkrétním transportním kanálovým spojením. CFN přiřadí řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) při zřízení rádiového spoje a sdělí jej uživatelskému zařízení (UE) a Node B. Jeho hlavní rolí je vytvořit sdílenou, jednoznačnou časovou referenci po dobu trvání spojení, což je nezbytné, protože RNC a Node B mohou mít nezávislé časové osy systémového čísla rámce ([SFN](/mobilnisite/slovnik/sfn/)).

Z architektonického hlediska CFN funguje na úrovni Transportního kanálu, mezi vrstvou [MAC](/mobilnisite/slovnik/mac/) a fyzickou vrstvou. RNC namapuje CFN na SFN Node B v okamžiku vysílání, což je proces definovaný parametry Frame Offset a Chip Offset. Toto mapování zajišťuje, že datové bloky naplánované k vysílání RNC jsou správně zarovnány s fyzickou strukturou rádiových rámců Node B. CFN je přenášen v klíčových signalizačních zprávách přes rozhraní Iub a Iur, například v proceduře Radio Link Setup a v rámci datových rámců Frame Protocol ([FP](/mobilnisite/slovnik/fp/)), aby byla zachována synchronizace mezi těmito síťovými prvky.

Během provozu CFN řídí několik kritických procedur. Používá se pro časování vzorů komprimovaného režimu (compressed mode), kde jsou přenosové mezery plánovány na základě CFN. Při měkkém předání spojení (soft handover) umožňuje CFN RNC koordinovat identický přenos dat z více Node B k UE, čímž zajišťuje správné fungování makrodiverzitního kombinování. Hraje také zásadní roli v synchronizačních procedurách (např. synchronizace rádiového spoje) a při výpočtu časových úprav pro příchod dat v Node B. Bez CFN by koordinace časově citlivých operací v distribuované architektuře UTRAN byla výrazně složitější a náchylnější k chybám.

## K čemu slouží

CFN byl zaveden, aby vyřešil základní problém časové koordinace mezi řídicím [RNC](/mobilnisite/slovnik/rnc/) a bodem rádiového přenosu, Node B, v asynchronní architektuře [UTRAN](/mobilnisite/slovnik/utran/). V GSM bylo časování centralizovanější přes Base Station Controller (BSC). UMTS však zavedlo distribuovanější, paketově orientovanou RAN, kde RNC a Node B mohly mít nezávislé zdroje hodin. To vytvořilo potřebu spojení-specifické časové reference, která byla oddělena od absolutního časování buňky (SFN).

Před zavedením CFN neexistovala standardizovaná metoda, jak zajistit, aby datové bloky odeslané z RNC byly vysílány Node B ve správný okamžik vzhledem k časování rádiového rozhraní. CFN tuto abstraktní vrstvu poskytuje. Umožňuje RNC plánovat a řídit přenos dat (včetně příkazů pro handover a řízení výkonu) pomocí jednoduchého, předvídatelného čítače, který je následně lokálně namapován každým Node B na jeho vlastní časovou osu SFN. Tím se řeší problémy časového driftu a nesouladu mezi síťovými prvky.

Jeho vytvoření bylo motivováno požadavky pokročilých funkcí UMTS, jako je měkké předání spojení (soft handover) a komprimovaný režim (compressed mode). Pro měkké předání spojení musí být stejná data vysílána z více buněk přesně ve stejný okamžik, aby je UE mohla kombinovat. CFN, společný pro všechny rádiové spoje v aktivní sadě, poskytuje tento přesný koordinační bod. Pro komprimovaný režim, který vytváří mezery pro měření na jiných frekvencích nebo v jiných systémech, je vzor definován vzhledem k CFN, což zajišťuje, že se UE a síť shodnou na tom, kdy k těmto přenosovým mezerám dojde, bez ohledu na SFN podkladové buňky.

## Klíčové vlastnosti

- 12bitový čítač poskytující spojení-specifické číslování rámců (0-4095)
- Slouží jako společný časový referenční bod mezi RNC a Node B, nezávislý na SFN buňky
- Nezbytný pro časovou koordinaci během procedur měkkého předání spojení (soft handover)
- Používá se pro plánování a definici vzorů přenosu v komprimovaném režimu (compressed mode)
- Přenášen v rámci Frame Protocol a signalizačních zpráv NBAP/RNSAP
- Namapován na SFN Node B pomocí parametrů Frame Offset a Chip Offset

## Související pojmy

- [SFN – System Frame Number](/mobilnisite/slovnik/sfn/)
- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- **TS 25.706** (Rel-13) — Downlink Enhancements for UMTS Study
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [CFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfn/)
