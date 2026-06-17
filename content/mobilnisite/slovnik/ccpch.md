---
slug: "ccpch"
url: "/mobilnisite/slovnik/ccpch/"
type: "slovnik"
title: "CCPCH – Common Control Physical Channel"
date: 2025-01-01
abbr: "CCPCH"
fullName: "Common Control Physical Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ccpch/"
summary: "CCPCH je downlinkový fyzický kanál v UMTS (WCDMA), který přenáší základní broadcastové a společné řídicí informace pro všechna UE v buňce. Je klíčový pro počáteční vyhledání buňky, získávání systémový"
---

CCPCH je downlinkový fyzický kanál v UMTS, který vysílá základní řídicí informace všem uživatelským zařízením v buňce pro počáteční přístup, získávání systémových informací a paging.

## Popis

Common Control Physical Channel (CCPCH) je základní downlinkový fyzický kanál definovaný v rádiovém rozhraní Universal Mobile Telecommunications System (UMTS), konkrétně pro Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (WCDMA). Funguje jako transportní mechanismus pro logické kanály vyšší vrstvy, které obsahují informace určené pro všechna uživatelská zařízení (UE) v pokrytí buňky. Na rozdíl od vyhrazených kanálů přiřazených konkrétním UE je CCPCH sdílený zdroj, který Node B nepřetržitě vysílá a který UE v klidovém nebo připojeném stavu monitorují, aby udržovala synchronizaci a přijímala kritické síťové instrukce.

Architektonicky je CCPCH mapován ze dvou odlišných logických kanálů: Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) a Paging Control Channel (PCCH). Toto mapování je fyzicky realizováno prostřednictvím dvou samostatných podtypů kanálu: Primary CCPCH ([P-CCPCH](/mobilnisite/slovnik/p-ccpch/)) a Secondary CCPCH (S-CCPCH). P-CCPCH je kanál s pevnou přenosovou rychlostí bez řízení výkonu, který nepřetržitě vysílá Master Information Block ([MIB](/mobilnisite/slovnik/mib/)) a System Information Blocks (SIBs) přenášené přes BCCH. Používá předdefinovaný, pro buňku specifický spreading kód a je vysílán bez příkazů Transmit Power Control (TPC), což zajišťuje jeho konstantní přítomnost a předvídatelný příjem pro procedury vyhledávání a výběru buňky.

S-CCPCH naopak přenáší Paging Channel (PCH) a Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)), které jsou mapovány z PCCH a Common Traffic Channel ([CTCH](/mobilnisite/slovnik/ctch/)). Na rozdíl od P-CCPCH může S-CCPCH podporovat proměnné datové rychlosti a může zahrnovat řízení vysílacího výkonu. Buňka může nakonfigurovat více S-CCPCH pro zpracování pagingových zpráv a společného řídicího signalizace nebo malého množství uživatelských dat. Vysílání S-CCPCH může být nespojité, což umožňuje úsporu výkonu v Node B.

Fungování CCPCH je nedílnou součástí interakce UE se sítí. Během počátečního vyhledávání buňky se UE nejprve synchronizuje s Primary Synchronization Channel (P-SCH) a Secondary Synchronization Channel (S-SCH), aby identifikovala časování slotu a rámce, a poté extrahuje skupinu scrambling kódu z Common Pilot Channel ([CPICH](/mobilnisite/slovnik/cpich/)). Následně demoduluje P-CCPCH, aby přečetla kritické systémové informace, včetně identity buňky, přístupových parametrů a seznamu sousedních buněk. S-CCPCH je poté monitorován kvůli pagingovým indikacím, které upozorňují UE na příchozí hovory nebo síťově iniciované procedury. Soubor CCPCH tedy tvoří základní páteř řídicí roviny pro broadcast buňky, paging a společnou signalizaci v rádiovém rozhraní UMTS.

## K čemu slouží

CCPCH byl vytvořen, aby řešil základní požadavek v celulárních sítích na efektivní a spolehlivé broadcastové a společné řídicí signalizaci. Před 3G používaly systémy 2G, jako je GSM, vyhrazené časové sloty a frekvence pro broadcastové kanály (např. [BCCH](/mobilnisite/slovnik/bcch/)). Přechod na spread-spectrum technologii WCDMA s kódovým dělením si vyžádal novou strukturu fyzických kanálů, která by mohla integrovat broadcastové a společné řídicí funkce do kódové domény při zachování robustního výkonu v prostředí s multipath fadingem.

Hlavním problémem, který CCPCH řeší, je poskytnutí jednotné, vždy dostupné downlinkové cesty pro informace společné všem uživatelům. Bez vyhrazeného společného řídicího fyzického kanálu by UE nebyla schopna efektivně objevit síť, získat potřebné parametry pro registraci a přístup nebo být informována o příchozích službách. Oddělení na P-CCPCH a S-CCPCH umožňuje optimalizaci pro různé účely: P-CCPCH je optimalizován pro maximální spolehlivost a konstantní příjem systémových informací pomocí pevného formátu. S-CCPCH poskytuje flexibilitu pro paging a společný provoz, podporuje proměnné rychlosti a umožňuje optimalizaci síťových zdrojů. Tento design byl motivován potřebou škálovatelného řídicího mechanismu, který podporuje paging s vysokou kapacitou, efektivní využití downlinkových kódových zdrojů a spolehlivé doručování systémových informací, což je základ pro jakoukoli celulární síť velkého rozsahu.

## Klíčové vlastnosti

- Přenáší broadcastové systémové informace (BCCH) prostřednictvím Primary CCPCH (P-CCPCH)
- Přenáší pagingové zprávy (PCH) a společná uživatelská data (FACH) prostřednictvím Secondary CCPCH (S-CCPCH)
- Pro usnadnění vyhledávání buňky používá pro P-CCPCH pevné, předdefinované kanalizační kódy
- Podporuje jak pevné (P-CCPCH), tak proměnné (S-CCPCH) datové rychlosti
- Umožňuje nespojité vysílání (DTX) na S-CCPCH pro úsporu výkonu Node B
- Poskytuje fyzickou vrstvu jako základ pro procedury UE v klidovém režimu a dostupnost sítě

## Související pojmy

- [BCH – Bose-Chaudhuri-Hocquenghem Code](/mobilnisite/slovnik/bch/)
- [FACH – Forward Access Channel](/mobilnisite/slovnik/fach/)
- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [CCPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccpch/)
