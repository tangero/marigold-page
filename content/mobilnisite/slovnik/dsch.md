---
slug: "dsch"
url: "/mobilnisite/slovnik/dsch/"
type: "slovnik"
title: "DSCH – Downlink Shared Channel"
date: 2025-01-01
abbr: "DSCH"
fullName: "Downlink Shared Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dsch/"
summary: "Transportní kanál v UMTS (WCDMA) používaný pro přenos vyhrazených uživatelských dat a řídicích informací ve směru downlink (ze sítě k uživateli). Je dynamicky sdílen mezi více uživateli v časově multi"
---

DSCH je transportní kanál v UMTS, který se používá pro přenos vyhrazených uživatelských dat a řídicích informací v downlinku tím, že je dynamicky sdílí mezi více uživateli v časově multiplexovaném režimu za účelem efektivního využití rádiových prostředků.

## Popis

Downlink Shared Channel (DSCH) je klíčový transportní kanál v rádiovém rozhraní systému Universal Mobile Telecommunications System (UMTS), standardizovaný organizací 3GPP. Funguje ve směru downlink (z Node B k uživatelskému zařízení) a je v zásadě sdíleným prostředkem. Na rozdíl od vyhrazených kanálů ([DCH](/mobilnisite/slovnik/dch/)), které jsou přiděleny jednomu uživateli na dobu trvání hovoru, je DSCH určen k použití více uživatelskými zařízeními (UE) na principu sdílení času. Jeho hlavním účelem je přenášet uživatelská datová spojení, ale může přenášet i přidružené řídicí informace. DSCH je vždy pro dané UE spojen s jedním nebo více Downlink Dedicated Channels (DCH) nebo Forward Access Channels ([FACH](/mobilnisite/slovnik/fach/)). Přidružený DCH/FACH poskytuje potřebné řídicí signalizace, včetně indikátorů kombinace transportního formátu ([TFCI](/mobilnisite/slovnik/tfci/)), které informují UE, jak dekódovat data vysílaná na DSCH.

Z architektonického hlediska je DSCH mapován na jeden nebo více fyzických kanálů nazývaných Physical Downlink Shared Channels ([PDSCH](/mobilnisite/slovnik/pdsch/)). Sdílení je řízeno vrstvou Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) v Node B, konkrétně entitami MAC-d a MAC-c/sh. Plánovač [UTRAN](/mobilnisite/slovnik/utran/) rozhoduje, kterému UE je v každém přenosovém časovém intervalu ([TTI](/mobilnisite/slovnik/tti/)) přidělen přístup k DSCH, na základě faktorů jako kvalita kanálu, priorita a požadavky QoS. UE identifikuje data určená pro něj pomocí identifikace specifické pro dané UE, která je zahrnuta v řídicích informacích na přidruženém vyhrazeném kanálu. Tento mechanismus umožňuje rychlé a dynamické přerozdělování kapacity bez režijních nákladů na zřizování a rušení spojení, které jsou typické pro vyhrazené kanály.

DSCH umožňuje efektivní podporu přerušovaných (bursty) paketových služeb s vysokou přenosovou rychlostí. Je zvláště vhodný pro interaktivní a background třídy provozu, kde je přenos dat sporadický. Sdílením kanalizačních kódů a výkonu mezi více uživateli zlepšuje celkovou kapacitu buňky ve srovnání s modelem založeným pouze na vyhrazených kanálech. DSCH představuje významný krok směrem k paketově optimalizovaným vzdušným rozhraním a připravil cestu pro pokročilejší koncepty sdílených kanálů v pozdějších technologiích, jako je [HSDPA](/mobilnisite/slovnik/hsdpa/) (které používá HS-DSCH) a LTE (které jako primární datový kanál v downlinku používá PDSCH).

## K čemu slouží

DSCH byl zaveden v UMTS Release 99, aby řešil neefektivitu používání vyhrazených kanálů pro asymetrické, přerušované (bursty) paketové datové služby. V raném WCDMA byl Dedicated Channel (DCH) hlavním prostředkem pro přenos dat, což vyžadovalo trvalé přidělení kódového rozprostření a výkonu, což bylo plýtvání pro přerušovaný provoz, jako je prohlížení webu nebo e-mail.

Jeho zavedení bylo motivováno potřebou zlepšit spektrální účinnost a uživatelskou propustnost pro nehlasové služby. Paradigma sdíleného kanálu umožňuje síti přidělit přenosové záblesky s vysokou datovou rychlostí uživateli pouze tehdy, když má data k odeslání, a rychle tak uvolnit prostředky pro ostatní. Tím se vyřešilo omezení pevného přidělování prostředků podobného okruhovému přepojování, což umožnilo současnou podporu většího počtu uživatelů a lepší uživatelský zážitek pro paketové datové aplikace. DSCH položil základy pro vývoj high-speed downlink packet access (HSDPA), který později koncept sdíleného kanálu nahradil a vylepšil rychlejším plánováním a hybridním ARQ.

## Klíčové vlastnosti

- Časově multiplexované sdílení mezi více uživatelskými zařízeními (UE)
- Vždy je asociován s DCH nebo FACH pro řídicí signalizaci
- Mapován na fyzické kanály Physical Downlink Shared Channels (PDSCH)
- Podporuje proměnné a vysoké datové rychlosti na TTI
- Dynamické plánování vrstvou MAC v Node B
- Efektivní pro přerušovaný (bursty) paketový datový provoz

## Související pojmy

- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)
- [FACH – Forward Access Channel](/mobilnisite/slovnik/fach/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [HS-DSCH – High Speed Downlink Shared Channel](/mobilnisite/slovnik/hs-dsch/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [DSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsch/)
