---
slug: "e-dpcch"
url: "/mobilnisite/slovnik/e-dpcch/"
type: "slovnik"
title: "E-DPCCH – E-DCH Dedicated Physical Control Channel"
date: 2025-01-01
abbr: "E-DPCCH"
fullName: "E-DCH Dedicated Physical Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-dpcch/"
summary: "Fyzický řídicí kanál v UMTS/HSPA (režim FDD), který doprovází kanál E-DPDCH a přenáší klíčové řídicí informace pro vysílací přenos po kanálu E-DCH. Přenáší data jako indikátor kombinace transportního"
---

E-DPCCH je v systémech UMTS/HSPA vysílací fyzický řídicí kanál, který doprovází kanál E-DPDCH a přenáší řídicí informace, jako je transportní formát a data pro opakovaný přenos, což umožňuje NodeB dekódovat přenos po kanálu E-DCH.

## Popis

[E-DCH](/mobilnisite/slovnik/e-dch/) Dedicated Physical Control Channel (E-DPCCH) je vyhrazený vysílací fyzický kanál používaný výhradně v systémech UMTS a [HSPA](/mobilnisite/slovnik/hspa/) s duplexem s dělením kmitočtů ([FDD](/mobilnisite/slovnik/fdd/)). Vždy se vysílá současně s Enhanced Dedicated Physical Data Channel ([E-DPDCH](/mobilnisite/slovnik/e-dpdch/)), když uživatelské zařízení (UE) provádí přenos po kanálu E-DCH (Enhanced Dedicated Channel). Jeho jediným účelem je přenášet nezbytné řídicí signalizování mimo pásmo, které přijímač NodeB potřebuje k úspěšné demodulaci, dekódování a zpracování uživatelských dat přicházejících po paralelních kanálech E-DPDCH.

E-DPCCH přenáší pro každý 2ms podrámec (nebo v nepovinných konfiguracích 10ms rámec) řídicí rámec pevné velikosti. Tyto řídicí informace obsahují několik klíčových polí: Transport Format Combination Indicator (TFCI), který informuje NodeB o přesném transportním formátu (např. velikost datového bloku, parametry kódování kanálu) použitém na kanálech E-DPDCH v daném podrámci. Retransmission Sequence Number (RSN) udává, zda data v přidruženém podrámci představují nový přenos nebo opakovaný přenos, a pokud ano, ke kterému procesu [HARQ](/mobilnisite/slovnik/harq/) patří, což je zásadní pro operaci měkkého kombinování v rámci Hybrid [ARQ](/mobilnisite/slovnik/arq/).

Dalším klíčovým polem je Happy Bit. Jde o jednobitový indikátor vysílaný UE, kterým informuje plánovač NodeB o své spokojenosti s aktuálně přidělenou rychlostí vysílání dat. Pokud má UE ve své vyrovnávací paměti více dat, než může přenést s aktuálním přidělením, a její rezerva výkonu umožňuje vyšší přidělení, nastaví Happy Bit na hodnotu ‚nespokojený‘, čímž signalizuje žádost o více prostředků. Plánovač NodeB využívá tuto zpětnou vazbu spolu s měřeními výkonu a dalšími hlášeními UE k dynamickému přizpůsobování přidělení vysílaných UE na sestupných kanálech [E-AGCH](/mobilnisite/slovnik/e-agch/) a [E-RGCH](/mobilnisite/slovnik/e-rgch/). E-DPCCH je rozprostřen pomocí vyhrazeného kanalizačního kódu a vysílán s výkonovým posunem vůči přidruženému DPCCH, což zajišťuje spolehlivý příjem těchto kritických řídicích dat i při kolísání výkonu datového kanálu.

## K čemu slouží

E-DPCCH byl vytvořen jako nezbytný doprovod kanálu E-DPDCH, aby umožnil vysokovýkonný provoz kanálu E-DCH (HSUPA). Pokročilé funkce E-DCH, jako je rychlé plánování NodeB a HARQ na fyzické vrstvě s inkrementální redundancí, vyžadují, aby NodeB měl okamžitý a spolehlivý přehled o přenosových parametrech pro každý podrámec. Tyto řídicí informace nelze efektivně ani robustně multiplexovat s uživatelskými daty na samotném kanálu E-DPDCH.

Jeho účelem je poskytnout vyhrazenou signalizační cestu s nízkou latencí a vysokou spolehlivostí pro tato kritická řídicí data. Přenosem TFCI umožňuje adaptivní modulaci a kódování na úrovni jednotlivých podrámců. Přenosem RSN umožňuje správné fungování mechanismu HARQ. Přenosem Happy Bitu uzavírá rychlou zpětnovazební smyčku pro plánovač NodeB. Bez E-DPCCH by NodeB nebyl schopen dekódovat vysokorychlostní data na kanálu E-DPDCH, čímž by se HSUPA stala nefunkční. Řeší problém oddělení řídicí signalizace s vysokou spolehlivostí od uživatelských dat s proměnnou rychlostí v rychlém plánovaném vysílacím prostředí, což byl klíčový předpoklad pro dosažení nízké latence a vysoké účinnosti, které si kladla HSUPA za cíl.

## Klíčové vlastnosti

- Vysílá se paralelně s E-DPDCH během vysílacích přenosů po E-DCH.
- Přenáší Transport Format Combination Indicator (TFCI) pro dekódování E-DPDCH.
- Přenáší Retransmission Sequence Number (RSN) pro správu procesů HARQ.
- Obsahuje Happy Bit pro zpětnou vazbu UE k plánování v NodeB.
- Používá pevný rozprostírací faktor (SF) 256 pro robustní přenos.
- Vysílá se s konfigurovatelným výkonovým posunem vůči vysílacímu DPCCH.

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [E-DPDCH – E-DCH Dedicated Physical Data Channel](/mobilnisite/slovnik/e-dpdch/)
- [DPCCH – Dedicated Physical Control Channel](/mobilnisite/slovnik/dpcch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [FDD – Frequency Division Duplexing](/mobilnisite/slovnik/fdd/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 25.823** (Rel-8) — Synchronised E-DCH Study for UTRA FDD
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [E-DPCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-dpcch/)
