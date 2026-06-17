---
slug: "dpch"
url: "/mobilnisite/slovnik/dpch/"
type: "slovnik"
title: "DPCH – Dedicated Physical Channel"
date: 2025-01-01
abbr: "DPCH"
fullName: "Dedicated Physical Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dpch/"
summary: "Downlinkový fyzický kanál v UMTS, který přenáší jak vyhrazená uživatelská data, tak s nimi spojené řídicí informace pro konkrétní UE. Jedná se o časově multiplexovaný kanál kombinující Dedicated Physi"
---

DPCH je primární fyzický downlinkový kanál v UMTS/WCDMA, který přenáší časově multiplexovaná vyhrazená uživatelská data a řídicí informace pro konkrétní UE.

## Popis

Dedicated Physical Channel (DPCH) je klíčový downlinkový fyzický kanál v rádiovém rozhraní UMTS/WCDMA. Na rozdíl od uplinku, kde jsou data ([DPDCH](/mobilnisite/slovnik/dpdch/)) a řídicí informace ([DPCCH](/mobilnisite/slovnik/dpcch/)) odděleny pomocí I/Q kódového multiplexování, downlinkový DPCH je kombinuje pomocí časového multiplexu (TDM) v rámci každého slotu. DPCH je fyzickou vrstvou realizace vyhrazeného transportního kanálu ([DCH](/mobilnisite/slovnik/dch/)) a je přidělen jednomu uživatelskému zařízení (UE) po dobu hovoru nebo datové relace. Přenáší uživatelská vyhrazená přenosová data spolu s řídicími informacemi vrstvy 1 nezbytnými pro UE k demodulaci a dekódování těchto dat.

Každý 10ms rádiový rámec DPCH je rozdělen na 15 slotů. Každý slot obsahuje dvě hlavní části: datovou část (pocházející z DPDCH) a řídicí část (pocházející z DPCCH). Datová část obsahuje uživatelská data z vyhrazeného transportního kanálu po kanálovém kódování, prokládání a přizpůsobení rychlosti. Řídicí část obsahuje známé pilotní bity pro odhad kanálu, indikátor kombinace transportního formátu (TFCI) a příkazy řízení výkonu vysílání (TPC) pro uplink. Pole zpětnovazební informace ([FBI](/mobilnisite/slovnik/fbi/)), přítomné v uplinkovém DPCCH, není součástí downlinkového DPCH. Poměr výkonu přiděleného datové a řídicí části lze dynamicky upravovat, což je funkce známá jako posun výkonu (power offset), pro optimalizaci výkonu v závislosti na podmínkách kanálu.

Z architektonického hlediska je DPCH definován konkrétním kanalizačním kódem (rozprostíracím kódem) a v případě použití diverzity vysílání může zahrnovat také konkrétní scramblingový kód. Node B vysílá DPCH nepřetržitě a UE používá pilotní symboly v něm obsažené k odhadu rádiového kanálu, což umožňuje koherentní detekci. TFCI informuje UE o transportním formátu použitém v aktuálním rámci, což je nezbytné pro služby s proměnnou rychlostí, jako je hlas [AMR](/mobilnisite/slovnik/amr/) nebo paketová data. Bity TPC poskytují příkazy pro uzavřené smyčkové řízení výkonu pro UE, nařizující mu upravit svůj uplinkový vysílací výkon. DPCH je hlavním pracovním kanálem pro všechny vyhrazené služby s přepojováním okruhů i paketů v UMTS a tvoří přímý fyzický spoj mezi sítí a konkrétním uživatelem.

## K čemu slouží

DPCH byl navržen jako primární downlinkový vyhrazený kanál pro WCDMA k doručování uživatelsky specifických dat a řídicích informací s vysokou spolehlivostí a flexibilitou. V systému [CDMA](/mobilnisite/slovnik/cdma/) je zvládání interference a výkonu prvořadé. TDM struktura DPCH kombinující data a řídicí informace v rámci jednoho kanalizačního kódu zjednodušuje návrh přijímače UE ve srovnání s potřebou samostatných kódových kanálů pro data a řízení. Zajišťuje, že řídicí informace (piloty, TFCI, TPC) jsou vždy vysílány v těsném časovém souladu s uživatelskými daty, která popisují.

Tento návrh řeší několik problémů: zaručuje, že UE přijímá nezbytné řídicí informace (jako je datová rychlost prostřednictvím TFCI) pro každý rámec bez nutnosti samostatného odhadu kanálu pro řídicí kanál, protože piloty jsou vloženy přímo. Také umožňuje velmi rychlé (1500 Hz) downlinkové řízení výkonu uplinkového vysílání UE prostřednictvím bitů TPC. Struktura DPCH plynule podporuje proměnné datové rychlosti, což byl klíčový pokrok oproti kanálům s pevnou rychlostí v systémech 2G, a umožňuje tak efektivní podporu multimediálních služeb. Jeho vytvoření bylo motivováno potřebou robustního, flexibilního a efektivního fyzického kanálu, který by mohl podporovat širokou škálu služeb plánovaných pro 3G, od hlasu po vysokorychlostní data, vše v rámci technologie rozprostřeného spektra WCDMA.

## Klíčové vlastnosti

- Downlinkový fyzický kanál kombinující uživatelská data (DPDCH) a řídicí informace (DPCCH) pomocí časového multiplexu.
- Přenáší pilotní symboly, TFCI a příkazy TPC v řídicí části každého slotu.
- Používá jeden kanalizační kód na uživatele, což zjednodušuje návrh přijímače.
- Podporuje proměnné datové rychlosti prostřednictvím použití TFCI.
- Umožňuje rychlé downlinkem řízené řízení výkonu uplinku (1500 Hz).
- Primární kanál pro vyhrazený provoz (DCH) v UMTS.

## Související pojmy

- [DPCCH – Dedicated Physical Control Channel](/mobilnisite/slovnik/dpcch/)
- [DPDCH – Dedicated Physical Data Channel](/mobilnisite/slovnik/dpdch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [DPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpch/)
