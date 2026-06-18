---
slug: "tfri"
url: "/mobilnisite/slovnik/tfri/"
type: "slovnik"
title: "TFRI – Transport Format and Resource Indicator"
date: 2025-01-01
abbr: "TFRI"
fullName: "Transport Format and Resource Indicator"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tfri/"
summary: "Parametr v UMTS, který dynamicky signalizuje vybraný transportní formát (TF) a přidělení fyzických zdrojů pro transportní kanál (TrCH) od Node B k UE. Je klíčový pro efektivní správu rádiových zdrojů"
---

TFRI je parametr v UMTS, který signalizuje vybraný transportní formát a přidělení fyzických zdrojů od Node B k UE pro efektivní správu rádiových zdrojů.

## Popis

Transport Format and Resource Indicator (TFRI) je základní řídicí prvek v rádiové přístupové síti UMTS ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně v kontextu High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) a Enhanced Uplink (EUL/[HSUPA](/mobilnisite/slovnik/hsupa/)). Funguje jako součást signalizace fyzické vrstvy na High-Speed Shared Control Channel ([HS-SCCH](/mobilnisite/slovnik/hs-scch/)) v downlinku a na [E-DCH](/mobilnisite/slovnik/e-dch/) Absolute Grant Channel ([E-AGCH](/mobilnisite/slovnik/e-agch/)) nebo E-DCH Relative Grant Channel ([E-RGCH](/mobilnisite/slovnik/e-rgch/)) v uplinku. TFRI přenáší kompaktní zakódovanou zprávu, která uživatelskému zařízení (UE) přesně sděluje, který transportní formát ([TF](/mobilnisite/slovnik/tf/)) z předdefinované sady transportních formátů (TFS) je použit pro aktuální interval přenosového času (TTI), spolu s podrobnostmi o přidělených fyzických zdrojích, jako jsou kanalizační kódy a modulační schéma.

Z architektonického hlediska je TFRI generován entitou MAC-hs (pro HSDPA) nebo MAC-e/es (pro EUL) v Node B na základě rozhodnutí o plánování, která zohledňují kvalitu kanálu, stav vyrovnávací paměti a požadavky QoS. Tyto informace jsou pak namapovány do specifických polí přidruženého řídicího kanálu fyzické vrstvy. Pro UE je přijetí a dekódování TFRI předpokladem pro správnou demodulaci a dekódování odpovídajícího datového přenosu na High-Speed Physical Downlink Shared Channel (HS-PDSCH) nebo na E-DCH Dedicated Physical Data Channel (E-DPDCH). TFRI v podstatě poskytuje 'klíč' k interpretaci surových bitů přijatých přes rozhraní vzduchu, specifikuje velikost bloku, počet transportních bloků a kódovací poměr.

Jeho role je ústřední pro rychlé plánování řízené Node B, zavedené s HSDPA a EUL, které přesunulo odpovědnost za plánování z Radio Network Controller (RNC) na Node B za účelem snížení latence. TFRI to umožňuje tím, že Node B může činit a signalizovat rozhodnutí o přenosu na bázi každého TTI (2 ms pro HSDPA) a rychle se přizpůsobovat měnícím se rádiovým podmínkám. Tento mechanismus je základním kamenem pro dosažení vysoké spektrální účinnosti a špičkových přenosových rychlostí v sítích 3G UMTS a tvoří základ schopností přepojování paketů, které předcházely 4G LTE.

## K čemu slouží

TFRI byl vytvořen, aby řešil omezení UMTS Release 99, kde byl výběr transportního formátu (TF) polo-statický a řízený RNC prostřednictvím signalizace Radio Resource Control (RRC). Tento přístup, ač spolehlivý, byl pro efektivní paketové datové služby s vysoce proměnlivými vzory provozu a podmínkami kanálu příliš pomalý. Latence spojená s rozhodováním založeným na RNC bránila optimálnímu využití rádiových zdrojů a omezovala špičkové přenosové rychlosti a kapacitu systému pro přerušované, interaktivní datové služby, jako je prohlížení webu.

Zavedení HSDPA v Release 5 a Enhanced Uplink v Release 6 si vyžádalo přechod k rychlé signalizaci fyzické vrstvy (L1), aby podpořilo intervaly přenosového času (TTI) krátké až 2 ms. TFRI byl navržen jako nezbytný řídicí signál s nízkou latencí, který to umožňuje. Řeší problém, jak dynamicky a efektivně informovat UE o přesných parametrech přenosu pro každé TTI bez nutnosti signalizace na vyšší vrstvě. To umožňuje plánovači v Node B činit okamžitá rozhodnutí na základě aktuálních hlášení indikátoru kvality kanálu (CQI) a stavu fronty, což dramaticky zlepšuje adaptaci spoje, zisk z diverzity více uživatelů a celkovou propustnost systému pro paketová data.

## Klíčové vlastnosti

- Dynamická signalizace výběru transportního formátu pro každé TTI
- Indikuje přidělení fyzických zdrojů (např. kanalizační kódy, modulace)
- Umožňuje rychlé plánování řízené Node B v HSDPA a EUL
- Přenášen na řídicích kanálech fyzické vrstvy (HS-SCCH, E-AGCH/E-RGCH)
- Nezbytný pro správnou demodulaci a dekódování přidruženého datového kanálu
- Podporuje procesy adaptivní modulace a kódování (AMC) a hybridního ARQ (HARQ)

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)

## Definující specifikace

- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.308** (Rel-19) — HSDPA Overall Description

---

📖 **Anglický originál a plná specifikace:** [TFRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfri/)
