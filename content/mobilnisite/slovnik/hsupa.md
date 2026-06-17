---
slug: "hsupa"
url: "/mobilnisite/slovnik/hsupa/"
type: "slovnik"
title: "HSUPA – High Speed Uplink Packet Access"
date: 2025-01-01
abbr: "HSUPA"
fullName: "High Speed Uplink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hsupa/"
summary: "HSUPA je vylepšení 3GPP UMTS/WCDMA, které výrazně zvyšuje přenosové rychlosti v uplinku a snižuje latenci pro uživatelské zařízení (UE). Zavedlo nové fyzické kanály, rychlejší mechanismus plánování a"
---

HSUPA je vylepšení 3GPP UMTS/WCDMA, které zvyšuje přenosové rychlosti v uplinku a snižuje latenci zavedením nových fyzických kanálů, rychlejšího plánování a Hybrid ARQ.

## Popis

High Speed Uplink Packet Access (HSUPA), standardizovaný jako součást 3GPP Release 6, je uplinková protiváha k [HSDPA](/mobilnisite/slovnik/hsdpa/) (High Speed Downlink Packet Access). Vylepšuje rádiové rozhraní WCDMA (Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)) pro výrazně lepší výkon v uplinku pro paketová data. Klíčovou technickou inovací je zavedení nového transportního kanálu, Enhanced Dedicated Channel ([E-DCH](/mobilnisite/slovnik/e-dch/)), který nahrazuje starší Dedicated Channel ([DCH](/mobilnisite/slovnik/dch/)) pro přenos dat v uplinku. E-DCH pracuje s kratším Transmission Time Interval (TTI) 2 ms (nebo volitelně 10 ms) ve srovnání s TTI 10, 20, 40 nebo 80 ms u DCH, což drasticky snižuje latenci.

Architektura zavádí dva nové síťové prvky v Node B (základnové stanici): plánovač E-DCH a entitu Hybrid [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)). Na rozdíl od downlinku, kde je plánování centralizováno v Node B (pro HSDPA), HSUPA využívá pro uplink rychlý mechanismus plánování *řízený Node B*. Node B průběžně monitoruje zatížení uplinku a posílá uživatelským zařízením (UE) plánovací povolení (grants) prostřednictvím nových řídicích kanálů v downlinku ([E-AGCH](/mobilnisite/slovnik/e-agch/) pro absolutní grants a [E-RGCH](/mobilnisite/slovnik/e-rgch/) pro relativní grants). Tato povolení určují maximální výkon, který může UE použít pro svůj přenos přes E-DCH, čímž řídí jeho datovou rychlost a zabraňují zahlcení uplinku. UE poté na základě tohoto povolení a svých dostupných dat vybere vhodný transportní formát.

Pro opravu chyb implementuje HSUPA HARQ s měkkým kombinováním (soft combining) v Node B. Když UE vysílá datový blok, spustí časovač a čeká na potvrzení (ACK) nebo negativní potvrzení (NACK) na novém kanálu E-HICH (E-DCH HARQ Acknowledgement Indicator Channel). Pokud je přijat NACK nebo časovač vyprší, UE provede retransmisi. Tato rychlá retransmise na fyzické vrstvě (Layer 1) je mnohem rychlejší než spoléhání se na retransmise vrstvy RLC, což zlepšuje propustnost a latenci. Novým fyzickým datovým kanálem v uplinku je E-DPDCH (E-DCH Dedicated Physical Data Channel), který může být kódově multiplexován se stávajícím DPCCH. Špičkové teoretické rychlosti v uplinku s HSUPA dosahovaly až 5,76 Mbps.

## K čemu slouží

HSUPA byla vyvinuta k řešení kritické nerovnováhy v raných 3G sítích. Zatímco HSDPA (Release 5) poskytovala vysoké rychlosti v downlinku vhodné pro stahování obsahu, uplink zůstal úzkým hrdlem, spoléhajícím se na pomalejší DCH s vyšší latencí. Tato asymetrie omezovala uživatelský zážitek u nových interaktivních a peer-to-peer aplikací, jako je videokonferencing, online hry, nahrávání velkých souborů (např. fotek, videí na sociální sítě) a nástroje pro spolupráci v reálném čase. Starší DCH s dlouhými TTI a plánováním centrickým k RNC byl pro burstový uplinkový provoz s nízkou latencí neefektivní.

Vytvoření HSUPA tyto problémy vyřešilo přenesením klíčových inovací HSDPA – kratších TTI, rychlého plánování a HARQ – do uplinku. Implementace se však lišila kvůli distribuované povaze uplinkových přenosů z více UE. Zavedení rychlého plánování řízeného Node B umožnilo dynamickou kontrolu rušení v uplinku, což je hlavní problém v uplinku WCDMA omezeném rušením, čímž se zvýšila celková kapacita buňky a zároveň se jednotlivým uživatelům poskytly vyšší špičkové rychlosti, když je potřebovali. Tím, že HSUPA umožnila symetričtější vysokorychlostní zážitek, byl to klíčový krok k tomu, aby se UMTS stalo skutečnou mobilní širokopásmovou platformou, schopnou podporovat bohaté obousměrné komunikační služby a připravit cestu pro plně IP sítě, které následovaly s LTE.

## Klíčové vlastnosti

- Zavádí Enhanced Dedicated Channel (E-DCH) s TTI 2 ms pro přenos v uplinku s nízkou latencí
- Používá rychlé plánování řízené Node B prostřednictvím E-AGCH a E-RGCH pro dynamické řízení rychlosti v uplinku
- Implementuje Hybrid ARQ (HARQ) s měkkým kombinováním (soft combining) na fyzické vrstvě pro rychlé zotavení z chyb
- Používá nové fyzické kanály: E-DPDCH (data v uplinku), E-DPCCH (řízení), E-AGCH, E-RGCH a E-HICH (řízení/potvrzení v downlinku)
- Umožňuje špičkové teoretické rychlosti v uplinku až 5,76 Mbps (s 2x2 multiplexováním)
- Zlepšuje kapacitu uplinku a snižuje latenci ve srovnání se starším DCH, čímž vylepšuje interaktivní aplikace

## Související pojmy

- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.707** (Rel-14) — Multi-Carrier Enhancements for UMTS Study
- **TS 25.823** (Rel-8) — Synchronised E-DCH Study for UTRA FDD
- **TS 25.874** (Rel-11) — HSPA Feedback & Signalling Efficiency for LCR TDD
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [HSUPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/hsupa/)
