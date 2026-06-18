---
slug: "p-ccpch"
url: "/mobilnisite/slovnik/p-ccpch/"
type: "slovnik"
title: "P-CCPCH – Primary Common Control Physical Channel"
date: 2025-01-01
abbr: "P-CCPCH"
fullName: "Primary Common Control Physical Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/p-ccpch/"
summary: "P-CCPCH je downlinkový fyzický kanál v UMTS (WCDMA), který přenáší transportní kanál Broadcast Channel (BCH). Je to kritický, nepřetržitě vysílaný kanál, který uživatelské zařízení (UE) používá k získ"
---

P-CCPCH je downlinkový fyzický kanál v UMTS, který přenáší Broadcast Channel, což umožňuje uživatelskému zařízení získat systémové informace, synchronizovat se se sítí a měřit kvalitu buňky.

## Popis

Primary Common Control Physical Channel (P-CCPCH) je základní downlinkový fyzický kanál v rádiovém rozhraní UMTS (Universal Mobile Telecommunications System), založený na technologii [WCDMA](/mobilnisite/slovnik/wcdma/) (Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)). Jeho hlavní úlohou je sloužit jako nosič na fyzické vrstvě pro transportní kanál Broadcast Channel ([BCH](/mobilnisite/slovnik/bch/)). Na rozdíl od vyhrazených nebo sdílených kanálů je P-CCPCH společný kanál, což znamená, že je každou UMTS Node B (základnovou stanicí) nepřetržitě vysílán všem uživatelským zařízením (UE) ve své pokryté oblasti a nepodléhá řízení výkonu. Je vysílán s pevným, vysokým výkonem, aby byla zajištěna spolehlivá recepce na okraji buňky.

Z technického pohledu je P-CCPCH charakterizován pevným spreading faktorem ([SF](/mobilnisite/slovnik/sf/)=256) a použitím specifického, rezervovaného kanalizačního kódu. Je mapován na specifické časové sloty v rámci struktury rádiového rámce. Klíčovým provozním detailem je, že P-CCPCH nepřenáší bity Transport Format Combination Indicator ([TFCI](/mobilnisite/slovnik/tfci/)) ani Transmit Power Control ([TPC](/mobilnisite/slovnik/tpc/)), protože jeho formát je pevný a UE jej zná předem. Data na P-CCPCH nejsou přenášena během prvních 256 čipů každého časového slotu; toto období je rezervováno pro Primary Synchronisation Channel (P-SCH) a Secondary Synchronisation Channel (S-SCH). Tato struktura umožňuje UE nejprve se synchronizovat pomocí [SCH](/mobilnisite/slovnik/sch/) a následně dekódovat systémové informace z P-CCPCH.

Informace přenášené na BCH, a tedy i na P-CCPCH, jsou Master Information Block ([MIB](/mobilnisite/slovnik/mib/)) a případně System Information Blocks (SIBs). MIB obsahuje nejkritičtější parametry pro počáteční přístup k buňce, včetně identity PLMN, plánovacích informací pro další SIBs a referenčních informací pro Common Pilot Channel (CPICH) buňky. Při zapnutí nebo vstupu do nové oblasti provádí UE procedury hledání buňky: nejprve dosáhne synchronizace slotu a rámce pomocí SCH, poté čte P-CCPCH, aby získalo systémové informace potřebné k identifikaci sítě, pochopení schopností buňky a pokračování v procedurách, jako je náhodný přístup, registrace a případně navázání vyhrazených spojení. Dále je kvalita přijímaného signálu P-CCPCH (často měřená jako CPICH Ec/Io nebo RSCP, s využitím P-CCPCH jako fázové reference) primární metrikou pro rozhodování o výběru buňky, převýběru a předávání hovoru v UMTS.

## K čemu slouží

P-CCPCH byl vytvořen jako nezbytná součást rádiového rozhraní UMTS WCDMA, aby vyřešil základní problém, jak mobilní zařízení zpočátku objeví, synchronizuje se a získá kritická konfigurační data z mobilní sítě. V každém buněčném systému je vyžadován společný, vždy dostupný vysílací kanál k inicializaci komunikačního procesu. Než může být P-CCPCH dekódován, se musí UE časově synchronizovat; to je úloha synchronizačních kanálů (SCHs) vysílaných ve stejných časových slotech.

Konstrukce P-CCPCH řešila specifické požadavky systému WCDMA. Jeho pevný, vysokovýkonný přenos zajišťuje spolehlivé pokrytí pro vysílané informace, což je zásadní pro procedury získání sítě a mobility. Rezervací specifického kanalizačního kódu a časové struktury poskytuje předvídatelný a stabilní referenční bod pro všechna UE v buňce. Tato stabilita je klíčová pro měření jako Received Signal Code Power (RSCP), která se používají pro rozhodování o předávání hovoru. Oddělení funkcí synchronizace (SCH) a vysílání systémových informací (P-CCPCH) do stejného časového slotu, ale různých období čipů, je efektivním využitím rádiového rámce, minimalizuje režii a zároveň zajišťuje, že obě funkce jsou vždy dostupné. P-CCPCH je tedy základním kamenem 'majákového' signálu UMTS buňky, umožňujícím autonomní hledání buňky, identifikaci sítě a poskytnutí základních 'pravidel provozu', která musí každé UE znát, než může požadovat jakoukoli vyhrazenou službu od sítě.

## Klíčové vlastnosti

- Přenáší transportní kanál Broadcast Channel (BCH) obsahující systémové informace (MIB/SIBs)
- Používá pevný spreading faktor (SF=256) a rezervovaný primární kanalizační kód
- Vysílán nepřetržitě s vysokým, konstantním výkonem bez rychlého řízení výkonu
- Časově multiplexován v rámci slotu; přenos dat začíná po 256-čipovém období využívaném pro synchronizační kanály (SCHs)
- Slouží jako fázová reference pro Common Pilot Channel (CPICH) a používá se pro měření kvality buňky (RSCP)
- Základní pro počáteční hledání buňky, synchronizaci, identifikaci sítě a procedury mobility v UMTS

## Související pojmy

- [BCH – Bose-Chaudhuri-Hocquenghem Code](/mobilnisite/slovnik/bch/)
- [S-CCPCH – Secondary Common Control Physical Channel](/mobilnisite/slovnik/s-ccpch/)
- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)
- [SCH – Synchronization Channel](/mobilnisite/slovnik/sch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B
- **TR 25.929** (Rel-19) — Continuous Connectivity for Packet Data Users
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [P-CCPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-ccpch/)
