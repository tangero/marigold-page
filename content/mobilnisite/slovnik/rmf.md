---
slug: "rmf"
url: "/mobilnisite/slovnik/rmf/"
type: "slovnik"
title: "RMF – Recommended Modulation Format"
date: 2025-01-01
abbr: "RMF"
fullName: "Recommended Modulation Format"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rmf/"
summary: "Standardizované doporučení pro modulační schéma používané na fyzickém kanálu v UMTS. Definuje mapování mezi transportními a fyzickými kanály a specifikuje typ modulace (např. QPSK), aby zajistilo spol"
---

RMF je standardizované doporučení 3GPP, které specifikuje modulační schéma (např. QPSK) používané na fyzickém kanálu UMTS, aby zajistilo spolehlivý přenos dat a interoperabilitu.

## Popis

Doporučený modulační formát (RMF) je klíčový parametr definovaný ve specifikacích 3GPP pro UMTS, konkrétně v TS 25.222, která detailně popisuje multiplexování a kanálové kódování pro režim s frekvenčním duplexem ([FDD](/mobilnisite/slovnik/fdd/)). Působí na fyzické vrstvě a určuje modulační schéma aplikované na vyhrazený fyzický kanál ([DPCH](/mobilnisite/slovnik/dpch/)) nebo jiné fyzické kanály po dokončení procesů kanálového kódování a prokládání. RMF není dynamický příkaz, ale statický konfigurační parametr, který je součástí definice kanálu a zajišťuje, že jak Node B (základnová stanice), tak uživatelské zařízení (UE) používají vzájemně srozumitelnou metodu pro modulaci digitálních bitů na rádiovou nosnou vlnu. To je zásadní pro správnou demodulaci a dekódování přenášeného signálu.

Technicky je RMF signalizováno z řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) k Node B a k UE jako součást procedur nastavení nebo rekonfigurace rádiového přenosového kanálu. Je vloženo do zpráv vyšší vrstvy pro řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)). Specifikace definuje sadu možných formátů, přičemž každý formát odpovídá konkrétní kombinaci parametrů, včetně činitele rozprostření a, což je klíčové, modulačního schématu. Pro UMTS Release 99 a následující verze jsou primárními modulačními schématy kvadraturní fázová manipulace ([QPSK](/mobilnisite/slovnik/qpsk/)) pro downlink a binární fázová manipulace ([BPSK](/mobilnisite/slovnik/bpsk/)) pro uplink v základním provozu. RMF zajišťuje, že pro danou kombinaci transportních formátů je zpracování na fyzické vrstvě předvídatelné a standardizované.

Role RMF přesahuje pouhý výběr modulace; je nedílnou součástí mapování indikátoru kombinace transportních formátů ([TFCI](/mobilnisite/slovnik/tfci/)). TFCI informuje přijímač o transportním formátu používaném na paralelních transportních kanálech multiplexovaných na jediný fyzický kanál. RMF, definováním charakteristik fyzického kanálu, zajišťuje, že TFCI může být správně interpretováno. Jeho implementace je klíčovým aspektem stability rádiového rozhraní UMTS, neboť zaručuje, že všechny entity v komunikačním řetězci jsou sladěny v základní metodě reprezentace dat na rádiovém rozhraní, čímž předchází selhání spojení v důsledku neshody v modulaci a tvoří základ pro dosažitelné přenosové rychlosti a spektrální účinnost.

## K čemu slouží

Doporučený modulační formát byl vytvořen, aby poskytl standardizovanou a jednoznačnou metodu pro konfiguraci fyzické vrstvy rádiového rozhraní UMTS. Před standardizací 3GPP mohly proprietární systémy používat různá modulační schémata, což vedlo k nekompatibilitě mezi síťovou infrastrukturou od různých dodavatelů a uživatelskými zařízeními. RMF tento problém interoperability řeší definováním jasného, sítí řízeného parametru, který přesně určuje, jak mají být data modulována na rádiovou nosnou pro konkrétní fyzický kanál.

Jeho zavedení v UMTS Release 5, jako součást kontinuálního vývoje rádiového rozhraní založeného na [WCDMA](/mobilnisite/slovnik/wcdma/), bylo motivováno potřebou robustního a efektivního řízení rádiového spoje. Tím, že síť (RNC) doporučuje modulační formát, centralizuje řízení a optimalizuje využití prostředků na základě rádiových podmínek a požadavků služby. Tento přístup řeší omezení ad-hoc nebo pevných modulačních schémat a umožňuje konfigurovat systém pro různé scénáře (např. hlas vs. data) při zachování zaručené úrovně výkonu a spolehlivosti. Tvoří základní prvek protokolového zásobníku fyzické vrstvy a zajišťuje, že složité procesy kanálového kódování, prokládání a rozprostření vyústí v dobře definovaný modulační krok, který mohou vysílač i přijímač správně provést.

## Klíčové vlastnosti

- Standardizovaná definice parametrů modulace fyzického kanálu
- Síťově řízená konfigurace prostřednictvím signalizace RRC
- Zajišťuje interoperabilitu mezi UE a Node B
- Nedílná součást specifikace kombinace transportních formátů
- Definuje modulační schéma (např. QPSK pro downlink)
- Propojeno s činitelem rozprostření a dalšími atributy fyzického kanálu

## Definující specifikace

- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding

---

📖 **Anglický originál a plná specifikace:** [RMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/rmf/)
