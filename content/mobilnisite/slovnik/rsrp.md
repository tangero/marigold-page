---
slug: "rsrp"
url: "/mobilnisite/slovnik/rsrp/"
type: "slovnik"
title: "RSRP – Reference Signal Received Power"
date: 2026-01-01
abbr: "RSRP"
fullName: "Reference Signal Received Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rsrp/"
summary: "RSRP je klíčové měření fyzické vrstvy v LTE a 5G NR, které představuje průměrný přijímaný výkon buněčně specifických referenčních signálů. Je to primární metrika pro výběr buňky, rozhodování o předání"
---

RSRP je primární metrika 3GPP pro LTE a 5G NR, která představuje průměrný přijímaný výkon buněčně specifických referenčních signálů, používaná pro výběr buňky, předávání hovoru (handover) a správu rádiových prostředků.

## Popis

Reference Signal Received Power (RSRP) je základní měření v rádiových systémech LTE a 5G NR, které kvantifikuje úroveň výkonu přijímaného z referenčních signálů konkrétní buňky. V LTE se jedná o Cell-specific Reference Signals ([CRS](/mobilnisite/slovnik/crs/)) a v NR o Synchronization Signal Blocks (SSB) nebo Channel State Information Reference Signals ([CSI-RS](/mobilnisite/slovnik/csi-rs/)). RSRP měří uživatelské zařízení (UE) na downlinku a představuje lineární průměr přes příspěvky výkonu (ve wattech) zdrojových prvků nesoucích referenční signály v uvažované měřicí šířce pásma. Udává se v dBm a poskytuje stabilní, na rušení nezávislou indikaci síly signálu z buňky.

Proces měření zahrnuje synchronizaci UE s buňkou a identifikaci konkrétních zdrojových prvků vyhrazených pro referenční signály. Přijímač měří výkon těchto známých symbolů. Pro přesnost se měření typicky průměrují v čase a frekvenci, aby se zmírnilo rychlé úniky. V 5G NR lze kvůli beamformingu měřit RSRP pro každý paprsek (SSB nebo CSI-RS paprsek) a síť může nakonfigurovat UE tak, aby hlásilo RSRP na úrovni paprsku nebo na úrovni buňky (odvozené z nejlepších paprsků). Měření provádí fyzická vrstva a výsledky jsou hlášeny vyšším vrstvám ([RRC](/mobilnisite/slovnik/rrc/)) pro použití v procedurách jako je výběr/převýběr buňky a předání hovoru.

Role RSRP je klíčová pro správu rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)). Je to primární vstup pro kritérium 'S' při výběru buňky (Srxlev) a kritéria 'R' pro převýběr buňky. Síť využívá měření RSRP hlášená zařízeními UE k rozhodování o předání hovoru, správě mobility a optimalizaci pokrytí. Používá se také spolu s dalšími metrikami, jako je [RSRQ](/mobilnisite/slovnik/rsrq/) (Reference Signal Received Quality) a [SINR](/mobilnisite/slovnik/sinr/) (Signal-to-Interference-plus-Noise Ratio), aby poskytla komplexní pohled na kvalitu rádiového spoje. Díky poskytování konzistentního měření síly signálu umožňuje RSRP sítím udržovat spolehlivé připojení, vyvažovat zatížení mezi buňkami a zajistit, aby uživatele obsluhovala nejvhodnější buňka.

## K čemu slouží

RSRP bylo zavedeno ve 3GPP Release 8 s LTE za účelem poskytnutí standardizované, přesné míry síly downlink signálu pro správu mobility. Předchozí buněčné systémy používaly metriky jako Received Signal Strength Indicator ([RSSI](/mobilnisite/slovnik/rssi/)), která zahrnuje veškerý přijímaný výkon (požadovaný signál, rušení a šum), což ji činí méně přesnou pro buněčně specifické hodnocení kvality. Motivací pro RSRP bylo definovat měření specifické pro referenční signály konkrétní buňky, a tím poskytnout čistou indikaci výkonu signálu této buňky, která je z velké části nezávislá na rušení a provozní zátěži.

Řeší problém spolehlivého výběru buňky a předání hovoru v moderních sítích založených na [OFDMA](/mobilnisite/slovnik/ofdma/). Přesná měření RSRP umožňují zařízení UE a síti určit, kdy přepojit spojení mezi buňkami, což je klíčové pro udržení kontinuity hovoru a kvality datové relace. Jak se sítě vyvíjely přes LTE-Advanced až k 5G NR, RSRP zůstalo základním měřením. Jeho účel se rozšířil o podporu nových funkcí, jako je agregace nosných (kde se sekundární buňky přidávají na základě RSRP), duální konektivita a v 5G správa paprsků. Vývoj k měřením na úrovni paprsků v NR řešil výzvy vysokofrekvenčních pásem (mmWave), kde jsou směrové paprsky nezbytné, což vyžaduje měření RSRP na paprsek k identifikaci nejlepšího směru přenosu. Trvalá role RSRP je způsobena jeho jednoduchostí, stabilitou a účinností jako základního ukazatele síly rádiového spoje.

## Klíčové vlastnosti

- Měří průměrný přijímaný výkon buněčně specifických referenčních signálů (CRS v LTE, SSB/CSI-RS v NR)
- Hlášeno v dBm, poskytuje stabilní metriku síly signálu
- Primární vstup pro algoritmy výběru buňky, převýběru buňky a předání hovoru
- Podporuje měření na úrovni paprsků v 5G NR pro správu paprsků
- Používá se při správě rádiových prostředků pro vyvažování zátěže a optimalizaci pokrytí
- Standardizované měření zajišťující interoperabilitu mezi dodavateli a sítěmi

## Související pojmy

- [RSRQ – Reference Signal Receiving Quality](/mobilnisite/slovnik/rsrq/)
- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)
- [RSSI – Received Signal Strength Indication](/mobilnisite/slovnik/rssi/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- … a dalších 38 specifikací

---

📖 **Anglický originál a plná specifikace:** [RSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsrp/)
