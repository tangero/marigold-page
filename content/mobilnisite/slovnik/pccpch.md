---
slug: "pccpch"
url: "/mobilnisite/slovnik/pccpch/"
type: "slovnik"
title: "PCCPCH – Primary Common Control Physical Channel"
date: 2025-01-01
abbr: "PCCPCH"
fullName: "Primary Common Control Physical Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pccpch/"
summary: "Sestupný fyzický kanál v UMTS (WCDMA), který nepřetržitě vysílá základní systémové informace a slouží jako časová reference pro celou buňku. Nese transportní kanál Broadcast Channel (BCH), který posky"
---

PCCPCH je sestupný fyzický kanál v UMTS, který nepřetržitě vysílá základní systémové informace a slouží jako časová reference buňky pro počáteční přístup uživatelského zařízení (UE).

## Popis

Primární společný řídicí fyzický kanál (PCCPCH) je základní fyzický kanál v rozhraní UMTS [WCDMA](/mobilnisite/slovnik/wcdma/). Je to sestupný, trvale aktivní kanál vysílaný z každé Node B (základnové stanice) v celé její pokryté oblasti. Na rozdíl od vyhrazených kanálů není řízen výkonově a je vysílán na konstantní úrovni výkonu, aby bylo zajištěno spolehlivé přijetí i na okraji buňky. Jeho hlavní úlohou je sloužit jako nosič na fyzické vrstvě pro transportní kanál Broadcast Channel ([BCH](/mobilnisite/slovnik/bch/)), který obsahuje hlavní informační blok ([MIB](/mobilnisite/slovnik/mib/)) a systémové informační bloky ([SIB](/mobilnisite/slovnik/sib/)).

Z pohledu fyzické vrstvy má PCCPCH pevný rozprostírací faktor 256 a používá specifický kanalizační kód (typicky první kód ve stromu kódů). Nepřenáší bity indikátoru kombinace transportního formátu ([TFCI](/mobilnisite/slovnik/tfci/)) ani řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)), protože jeho formát je konstantní. Kanál je vysílán bez uzavřené smyčky řízení výkonu, což činí kvalitu jeho příjmu klíčovým ukazatelem kvality sestupné rádiové cesty pro výběr a převýběr buňky. PCCPCH je rozdělen na dvě odlišné části: Primární synchronizační kanál (P-SCH) a Sekundární synchronizační kanál (S-SCH) jsou s ním časově multiplexovány, ale jedná se o samostatné fyzické kanály používané pro počáteční synchronizaci časového slotu a rámce a identifikaci skupiny skramblovacích kódů.

Fungování PCCPCH je ústřední pro procedury uživatelského zařízení (UE). Když se UE zapne nebo vstoupí do nové oblasti, provede vyhledávání buňky. Nejprve použije kanály [SCH](/mobilnisite/slovnik/sch/) pro synchronizaci slotů/rámců a identifikaci skupiny skramblovacích kódů. Jakmile je synchronizováno, demoduluje PCCPCH, aby přečetlo informace BCH. Tyto informace zahrnují skramblovací kód buňky (umožňující její jednoznačnou identifikaci), úroveň rušení na vzestupné lince, systémové informace přístupové vrstvy a parametry pro náhodný přístup a další společné kanály. Přijatý výkon kódového signálu PCCPCH ([RSCP](/mobilnisite/slovnik/rscp/)) a poměr energie na čip k šumu (Ec/No) jsou primární měření pro rozhodování o převýběru buňky a předávání hovoru (handover). V podstatě je PCCPCH majákem buňky, který poskytuje nezbytné informace a referenci pro jakékoli UE, aby mohlo buňku objevit, synchronizovat se s ní a vyhodnotit její vhodnost.

## K čemu slouží

PCCPCH byl vytvořen jako základní kámen rozhraní WCDMA v UMTS Release 99, aby splnil několik kritických požadavků, které v GSM chyběly. V GSM byly vysílací informace a synchronizace poskytovány různými fyzickými kanály (FCCH, SCH, BCCH). Technologie rozprostřeného spektra WCDMA vyžadovala jednotný a robustní fyzický kanál pro přenos vysílacích systémových informací a zároveň sloužící jako stabilní fázová a časová reference pro všechna UE v buňce.

Jeho konstrukce vyřešila problém počátečního zachycení buňky a jejího nepřetržitého monitorování v širokopásmovém systému s kódovým dělením. Pevný rozprostírací faktor a známý kanalizační kód zjednodušily proceduru vyhledávání buňky v UE. Konstantní vysílací výkon umožňuje UE provádět spolehlivá měření (RSCP, Ec/No) pro procedury řízení rádiových zdrojů, jako je výběr/převýběr buňky a předávání hovoru, které jsou v CDMA složitější než v GSM založeném na TDMA.

Dále PCCPCH poskytuje základní časování pro veškerý sestupný přenos v buňce. Všechny ostatní sestupné fyzické kanály (DPCH, CPICH atd.) jsou časově zarovnány vůči PCCPCH. Tato synchronizace je zásadní pro správnou funkci RAKE přijímače v UE a pro řízení měkkého předání hovoru. Bez stabilního, trvale přítomného primárního společného kanálu, jako je PCCPCH, by byla složitost implementace UE a provozu sítě ve WCDMA systému výrazně vyšší, což by bránilo spolehlivé mobilitě a kontinuitě služeb.

## Klíčové vlastnosti

- Konstantní výkon, trvale aktivní sestupný fyzický kanál pro celobuněčné vysílání
- Nese transportní kanál Broadcast Channel (BCH) se systémovými informacemi
- Používá pevný rozprostírací faktor (256) a primární kanalizační kód
- Poskytuje primární časovou referenci pro všechny sestupné přenosy v buňce
- Slouží jako měřicí reference pro výběr, převýběr buňky a předání hovoru (PCCPCH RSCP/Ec/No)
- Vysílán bez bitů TFCI nebo TPC, protože jeho formát je statický

## Související pojmy

- [BCH – Bose-Chaudhuri-Hocquenghem Code](/mobilnisite/slovnik/bch/)
- [S-CCPCH – Secondary Common Control Physical Channel](/mobilnisite/slovnik/s-ccpch/)
- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)
- [SCH – Synchronization Channel](/mobilnisite/slovnik/sch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.874** (Rel-11) — HSPA Feedback & Signalling Efficiency for LCR TDD
- **TS 34.124** (Rel-19) — EMC Requirements for 3G UTRA Terminals
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [PCCPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pccpch/)
