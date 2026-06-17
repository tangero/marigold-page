---
slug: "e-dch"
url: "/mobilnisite/slovnik/e-dch/"
type: "slovnik"
title: "E-DCH – Enhanced Dedicated Channel"
date: 2025-01-01
abbr: "E-DCH"
fullName: "Enhanced Dedicated Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-dch/"
summary: "Transportní kanál v síti UMTS/HSPA pro uplink, který ve srovnání s původním DCH výrazně zvyšuje přenosové rychlosti a snižuje latenci. Tvoří základ pro High-Speed Uplink Packet Access (HSUPA) a zavádí"
---

E-DCH je Enhanced Dedicated Channel (rozšířený vyhrazený kanál), což je transportní kanál v síti UMTS/HSPA pro uplink, který umožňuje High-Speed Uplink Packet Access (HSUPA) pro zvýšení přenosových rychlostí a snížení latence.

## Popis

Enhanced Dedicated Channel (E-DCH) je transportní kanál definovaný v UMTS a rozšířený jako součást [HSPA](/mobilnisite/slovnik/hspa/) (High-Speed Packet Access), konkrétně pro směr uplink (z uživatelského zařízení do sítě). Představuje významný vývoj oproti původnímu Dedicated Channel ([DCH](/mobilnisite/slovnik/dch/)). E-DCH není jediným fyzickým zdrojem, ale logickým kanálem mapovaným na sadu vyhrazených fyzických kanálů: [E-DPDCH](/mobilnisite/slovnik/e-dpdch/) (Enhanced Dedicated Physical Data Channel) pro přenos vlastních uživatelských dat a [E-DPCCH](/mobilnisite/slovnik/e-dpcch/) (Enhanced Dedicated Physical Control Channel) pro přenos řídicích informací nezbytných pro demodulaci a dekódování.

Provoz E-DCH je centrálně řízen rychlým plánovačem umístěným v NodeB, což je klíčový pokrok oproti plánování řízenému RNC u DCH. UE odesílá požadavky na plánování (přes E-DPCCH), které udávají jeho dostupnou rezervu výkonu a stav datové fronty. NodeB, které má mnohem rychlejší reakční dobu než RNC, přiděluje přenosové zdroje odesíláním absolutních povolení (nastavení maximální povolené výkonové odchylky) a relativních povolení (příkazů pro zvýšení/snížení) do UE. To umožňuje velmi rychlou adaptaci na měnící se rádiové podmínky a požadavky provozu a maximalizuje kapacitu uplinku.

E-DCH dále využívá hybridní automatické opakování žádosti ([HARQ](/mobilnisite/slovnik/harq/)) na fyzické vrstvě s více paralelními procesy typu stop-and-wait. To umožňuje rychlé retransmise na fyzické vrstvě mezi UE a NodeB bez zapojení vyšších vrstev, což drasticky snižuje latenci a zlepšuje spolehlivost. Data se přenášejí v 2ms podrámcích (nebo volitelně 10 ms), což je mnohem kratší přenosový časový interval (TTI) než 10/20/40/80 ms původního DCH, a umožňuje tak rychlejší doručení a podrobnější plánování. Kombinace plánování v NodeB, rychlého HARQ a krátkého TTI je tím, co umožňuje vysoké špičkové přenosové rychlosti (teoreticky až 5,76 Mbps) a nízkou latenci charakteristickou pro [HSUPA](/mobilnisite/slovnik/hsupa/).

## K čemu slouží

E-DCH byl vyvinut k řešení kritického omezení výkonu uplinku v sítích UMTS. Zatímco [HSDPA](/mobilnisite/slovnik/hsdpa/) (High-Speed Downlink Packet Access) dramaticky zlepšila rychlosti na downlinku, uplink zůstal založen na relativně pomalém a neefektivním [DCH](/mobilnisite/slovnik/dch/), který byl řízen RNC s vysokou latencí. Tato asymetrie byla nevhodná pro nově vznikající symetrické a interaktivní aplikace, jako je videokonferencing, nahrávání velkých souborů, hraní her v reálném čase a sociální média s obsahem vytvářeným uživateli.

Jeho vytvoření bylo motivováno potřebou přinést vylepšení výkonu HSPA i na uplink, čímž vznikne vyvážený systém vysokorychlostního paketového přístupu. E-DCH řešil omezení DCH přesunutím rychlých rozhodnutí o plánování do NodeB (snížení latence řídicí smyčky), zavedením HARQ na fyzické vrstvě pro rychlé zotavení z chyb a zkrácením TTI pro citlivější přenos. To umožnilo mobilním sítím nabízet skutečně širokopásmový zážitek v obou směrech, umožnit nové služby a zlepšit odezvu stávajících, což bylo klíčové pro udržení konkurenceschopnosti vůči jiným širokopásmovým technologiím.

## Klíčové vlastnosti

- Základ pro High-Speed Uplink Packet Access (HSUPA).
- Obsahuje rychlé plánování řízené NodeB (na rozdíl od plánování řízeného RNC).
- Využívá hybridní ARQ (HARQ) na fyzické vrstvě s více paralelními procesy pro retransmise s nízkou latencí.
- Používá krátký 2ms přenosový časový interval (TTI) pro rychlé doručování dat.
- Využívá vyhrazené fyzické kanály: E-DPDCH pro data a E-DPCCH pro řídicí signalizaci.
- Podporuje pokročilé techniky jako modulace 16QAM (v pozdějších vydáních) a vylepšené procedury změny obsluhující buňky.

## Související pojmy

- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)
- [E-DPCCH – E-DCH Dedicated Physical Control Channel](/mobilnisite/slovnik/e-dpcch/)
- [E-DPDCH – E-DCH Dedicated Physical Data Channel](/mobilnisite/slovnik/e-dpdch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- … a dalších 21 specifikací

---

📖 **Anglický originál a plná specifikace:** [E-DCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-dch/)
