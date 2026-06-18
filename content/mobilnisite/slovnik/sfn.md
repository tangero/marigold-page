---
slug: "sfn"
url: "/mobilnisite/slovnik/sfn/"
type: "slovnik"
title: "SFN – System Frame Number"
date: 2025-01-01
abbr: "SFN"
fullName: "System Frame Number"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sfn/"
summary: "Čítač, který čísluje rádiové rámce v buňce, s rozsahem 0 až 1023 v LTE a 0 až 1023 nebo 4095 v 5G NR. Poskytuje časovou synchronizaci pro plánování systémových informací, cykly vyvolávání, hlášení měř"
---

SFN je čítač, který čísluje rádiové rámce v buňce a poskytuje časovou synchronizaci pro klíčové rádiové procedury, jako je plánování systémových informací a vyvolávání.

## Popis

System Frame Number (SFN) je základní časový parametr v mobilních sítích, který slouží jako modulo čítač jednoznačně identifikující každý rádiový rámec v časové ose přenosu buňky. V LTE se SFN cykluje od 0 do 1023, což odpovídá periodě 10,24 sekundy (1024 rámců * 10 ms/rámec). V 5G NR jsou definovány dva rozsahy: 10bitový SFN (0-1023) pro základní časování a 12bitový Hyper-SFN ([H-SFN](/mobilnisite/slovnik/h-sfn/), 0-4095) pro rozšířené časovací procedury, zejména pro IoT a zařízení s redukovanými schopnostmi. SFN je vysílán v rámci Master Information Block ([MIB](/mobilnisite/slovnik/mib/)) na Physical Broadcast Channel ([PBCH](/mobilnisite/slovnik/pbch/)). V LTE je 8 nejvýznamnějších bitů SFN přenášeno v MIB, zatímco 2 nejméně významné bity jsou odvozeny z časování dekódování PBCH. V NR přenáší payload PBCH část SFN a celá hodnota se získá kombinací této informace s údaji z Demodulation Reference Signals ([DM-RS](/mobilnisite/slovnik/dm-rs/)) PBCH a časováním rádiového rámce. SFN je klíčový pro časově synchronizované síťové operace. Určuje plánování System Information Blocks (SIBs), které jsou vysílány v konkrétních rádiových rámcích a podrámcích podle vzorců založených na SFN. Řídí příležitosti pro vyvolávání (paging occasions), kdy se UE probouzejí, aby zkontrolovaly vyvolání pouze v rámcích, kde SFN mod T = T_Offset, přičemž T je cyklus vyvolávání. Pro měření používají UE SFN k časovému značkování hlášení měření (např. pro předávání spojení) a k synchronizaci cyklů nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)). V polohovacích protokolech, jako je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) a NR Positioning Protocol (NRPP), se SFN používá jako společný časový referenční bod pro měření Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)). SFN v podstatě poskytuje buňce specifické 'hodiny', které synchronizují všechny aktivity UE a sítě v rámci mřížky rádiových zdrojů buňky.

## K čemu slouží

SFN byl zaveden od nejranějších verzí 3GPP ([R99](/mobilnisite/slovnik/r99/)), aby poskytl standardizovanou časovou referenci na úrovni buňky, čímž řešil potřebu deterministického plánování a synchronizace v digitálních mobilních systémech. Předchozí analogové systémy takový jednotný, vysílaný časovací čítač postrádaly, což ztěžovalo koordinovaný přístup k kanálu a mechanismy úspory energie. SFN řeší několik kritických problémů: umožňuje efektivní režimy spánku (DRX/vyvolávání) tím, že UE mohou přesně předpovědět, kdy se probudit na základě známého cyklu, což výrazně šetří životnost baterie. Umožňuje periodické a předvídatelné vysílání systémových informací, což zajišťuje, že všechny UE mohou získat klíčové síťové parametry bez nepřetržitého monitorování. Poskytuje společnou časovou základnu pro měření a hlášení při předávání spojení, což zajišťuje, že síť může přesně porovnávat měření z různých UE nebo z různých časů. Dále podporuje pokročilé funkce, jako je Multimedia Broadcast Multicast Service (MBMS), kde synchronizovaný přenos z více buněk (MBSFN) vyžaduje přesné zarovnání rámců. Zavedení H-SFN v pozdějších verzích (pro LTE-M, NB-IoT a NR) bylo motivováno potřebou ještě delších časovacích cyklů pro zařízení IoT s ultranízkou spotřebou, což umožňuje rozšířené DRX cykly přesahující 10,24 sekundy a efektivnější plánování pro malé, nepravidelné přenosy dat.

## Klíčové vlastnosti

- Jednoznačně identifikuje rádiové rámce (0-1023 v LTE, také 0-4095 H-SFN v NR)
- Vysílán v MIB prostřednictvím PBCH
- Řídí deterministické plánování SIBs a příležitostí pro vyvolávání (paging occasions)
- Slouží jako časová reference pro měření a hlášení UE
- Základní pro zarovnání DRX cyklů a úsporu energie UE
- Používá se jako časová reference v polohovacích protokolech (OTDOA)

## Související pojmy

- [H-SFN – Hyper System Frame Number](/mobilnisite/slovnik/h-sfn/)
- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [PBCH – Physical Broadcast Channel](/mobilnisite/slovnik/pbch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- … a dalších 25 specifikací

---

📖 **Anglický originál a plná specifikace:** [SFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/sfn/)
