---
slug: "shcch"
url: "/mobilnisite/slovnik/shcch/"
type: "slovnik"
title: "SHCCH – Shared Channel Control Channel"
date: 2025-01-01
abbr: "SHCCH"
fullName: "Shared Channel Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/shcch/"
summary: "SHCCH je logický kanál v UMTS (UTRAN) používaný k přenosu řídicích informací pro sdílené transportní kanály, konkrétně Downlink Shared Channel (DSCH) a Uplink Shared Channel (USCH). Umožňuje efektivní"
---

SHCCH je logický kanál v UMTS, který přenáší řídicí informace pro sdílené sdílené kanály v downlinku a uplinku, signalizuje příkazy pro plánování a řízení výkonu ke správě rádiových zdrojů.

## Popis

Shared Channel Control Channel (SHCCH) je logický kanál definovaný v architektuře UMTS Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)) podle specifikací 3GPP, jako jsou TS 25.301 a TS 25.321. Funguje mezi vrstvami Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a slouží jako vyhrazená řídicí cesta pro sdílené transportní kanály. SHCCH je jednosměrný: v downlinku přenáší řídicí informace z Node B do User Equipment (UE) pro Downlink Shared Channel ([DSCH](/mobilnisite/slovnik/dsch/)); v uplinku přenáší řídicí informace z UE do Node B pro Uplink Shared Channel ([USCH](/mobilnisite/slovnik/usch/)). Tento kanál je klíčový pro dynamické plánování, kde jsou rádiové zdroje přidělovány více uživatelům na základě každého přenosového časového intervalu ([TTI](/mobilnisite/slovnik/tti/)).

Funkčně SHCCH přenáší specifické řídicí zprávy, včetně příkazů Transport Format Combination ([TFC](/mobilnisite/slovnik/tfc/)), aktualizací řízení výkonu a povolení pro plánování. Pro DSCH používá Node B SHCCH k informování UE o kódovacím schématu, modulaci a přiřazení zdrojových bloků pro nadcházející přenosy dat. Pro USCH signalizují UE prostřednictvím SHCCH svůj stav vyrovnávací paměti a požadované zdroje, což Node B umožňuje spravovat rušení a kapacitu v uplinku. Kanál je mapován na fyzické kanály, jako je Secondary Common Control Physical Channel ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)) v downlinku a Physical Uplink Shared Channel (PUSCH) v uplinku, v závislosti na verzi UMTS a konfiguraci.

Architektonicky je SHCCH součástí řídicí roviny ve vrstvě 2 UTRAN a rozhraní s entitami MAC-d a MAC-c/sh. Podporuje proměnné přenosové rychlosti a je charakterizován nízkou latencí, aby zajistil včasná rozhodnutí o plánování. Návrh kanálu optimalizuje efektivitu spektra u paketově orientovaných služeb, jako jsou vylepšení HSDPA a HSUPA, snížením režie řízení ve srovnání s vyhrazenými kanály. Jeho provoz je úzce spojen s protokolem Radio Resource Control (RRC) pro správu spojení a s Packet Data Convergence Protocol (PDCP) pro kompresi hlaviček v tocích uživatelských dat.

## K čemu slouží

SHCCH byl zaveden v UMTS Release 4, aby řešil neefektivitu používání vyhrazených kanálů pro přerušovaný, paketově orientovaný datový provoz. Předchozí přístupy, jako Dedicated Channels (DCH), přidělovaly pevné zdroje na uživatele, což vedlo ke špatnému využití rádiových zdrojů, když byl přenos dat přerušovaný. Koncept sdíleného kanálu, umožněný SHCCH, dovolil více uživatelům dynamicky sdílet společný transportní kanál, což výrazně zlepšilo spektrální účinnost a podpořilo vyšší datové rychlosti pro nereálné služby.

Vznik SHCCH byl motivován rostoucí poptávkou po mobilním přístupu k internetu a potřebou řídicího mechanismu, který by zvládal rychlé změny plánování. Vyřešil problém koordinace přístupu ke sdílenému médiu poskytnutím signalizační cesty s nízkou latencí pro povolení a příkazy, což bylo klíčové pro technologie jako High-Speed Downlink Packet Access (HSDPA) v Release 5. SHCCH umožnil pokročilé funkce, jako je rychlé paketové plánování, hybridní ARQ a adaptivní modulace a kódování, a položil základy pro vývoj směrem k integrovanějšímu návrhu řídicích kanálů v LTE. Jeho role se v pozdějších verzích zmenšila, protože LTE pro podobné funkce přijalo Physical Downlink Control Channel (PDCCH), ale zůstává klíčovou součástí sítí UMTS pro zpětnou kompatibilitu a efektivní správu zdrojů.

## Klíčové vlastnosti

- Logický kanál pro řídicí signalizaci sdílených transportních kanálů (DSCH/USCH)
- Jednosměrný: downlink pro řízení DSCH, uplink pro řízení USCH
- Přenáší informace Transport Format Combination (TFC) a plánování
- Mapován na fyzické kanály jako S-CCPCH (downlink) a PUSCH (uplink)
- Podporuje dynamické přidělování zdrojů a řízení výkonu
- Nedílná součást vylepšení paketového přepínání UMTS, jako jsou HSDPA/HSUPA

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [SHCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/shcch/)
