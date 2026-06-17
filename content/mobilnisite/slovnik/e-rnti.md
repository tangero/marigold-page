---
slug: "e-rnti"
url: "/mobilnisite/slovnik/e-rnti/"
type: "slovnik"
title: "E-RNTI – E-DCH Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "E-RNTI"
fullName: "E-DCH Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-rnti/"
summary: "Dočasný identifikátor přidělený Node B uživatelskému zařízení (UE) za účelem jeho adresování a identifikace na vylepšeném vyhrazeném kanálu (E-DCH) v UMTS/HSPA. Používá se na sdílených řídicích kanále"
---

E-RNTI je dočasný identifikátor přidělený Node B uživatelskému zařízení (UE) pro jeho adresování a identifikaci na vylepšeném vyhrazeném kanálu (E-DCH) v UMTS/HSPA. Používá se na sdílených řídicích kanálech, jako je E-AGCH a E-RGCH.

## Popis

[E-DCH](/mobilnisite/slovnik/e-dch/) Radio Network Temporary Identifier (E-RNTI) je 16bitový identifikátor používaný v rádiové přístupové síti UMTS/[HSPA](/mobilnisite/slovnik/hspa/) (UTRAN) pro jednoznačné adresování uživatelského zařízení (UE) v kontextu jeho provozu na vylepšeném vyhrazeném kanálu (E-DCH). Na rozdíl od dlouhodobějšího U-RNTI přidělovaného RNC je E-RNTI přiděleno obsluhujícím Node B při zřizování E-DCH a může být Node B změněno, například při změně obsluhující buňky. Jeho primární funkcí je umožnit Node B odesílat řídicí informace určené konkrétnímu UE přes sdílené downlinkové fyzické kanály. Dvěma klíčovými kanály, které pro adresování používají E-RNTI, jsou E-DCH Absolute Grant Channel ([E-AGCH](/mobilnisite/slovnik/e-agch/)) a E-DCH Relative Grant Channel ([E-RGCH](/mobilnisite/slovnik/e-rgch/)). Na E-AGCH, který nese absolutní hodnoty serving grantu, se E-RNTI používá ke skramblování přenášených bitů, což zajišťuje, že pouze cílové UE může grant správně dekódovat. Na E-RGCH, který nese relativní příkazy up/hold/down, E-RNTI určuje konkrétní ortogonální signaturu (kanalizační kód v rámci definované sady) použitou pro přenos. UE nepřetržitě monitoruje tyto sdílené kanály a kontroluje zprávy skramblované nebo signalizované svým přiděleným E-RNTI. Tento mechanismus je vysoce efektivní, protože se vyhýbá potřebě vyhrazených signalizačních spojů pro plánovací příkazy, a umožňuje tak časové multiplexování jednoho sdíleného kanálového zdroje (jako je sada kanalizačních kódů) mezi více UE. E-RNTI je klíčovým prvkem rychlé, na buňku orientované plánovací architektury [HSUPA](/mobilnisite/slovnik/hsupa/), neboť poskytuje nezbytnou adresovací vrstvu mezi plánovačem Node B a entitou MAC-e/es jednotlivého UE.

## K čemu slouží

E-RNTI bylo zavedeno v 3GPP Release 6 spolu s [HSUPA](/mobilnisite/slovnik/hsupa/), aby vyřešilo potřebu efektivního adresování s nízkou latencí v novém paradigmatu rychlého plánování Node B. V architektuře UMTS před HSUPA byla řídicí signalizace primárně mezi RNC a UE s využitím identifikátorů jako U-RNTI, které nebyly navrženy pro plánovací rozhodnutí na úrovni milisekund vyžadovaná pro [E-DCH](/mobilnisite/slovnik/e-dch/). Účelem E-RNTI je poskytnout dočasný identifikátor na úrovni buňky, který umožňuje fyzické vrstvě Node B přímo a jednoznačně komunikovat plánovací příkazy (granty) s konkrétním UE přes sdílené fyzické zdroje. Tím se řeší problém, jak efektivně doručovat řídicí informace pro každé UE bez nutnosti zřizovat četné vyhrazené řídicí kanály, což by plýtvalo vzácnými downlinkovými kódovými zdroji. Použitím krátkého 16bitového identifikátoru pro skramblování a výběr kódu systém dosahuje dobré rovnováhy mezi adresovacím prostorem a signalizační režií. E-RNTI je klíčové pro fungování [E-AGCH](/mobilnisite/slovnik/e-agch/) a E-RGCH a umožňuje rychlé, cílené přidělování zdrojů, které dává HSUPA jeho vysoký výkon v uplinku a zisky kapacity oproti DCH z Release 99.

## Klíčové vlastnosti

- 16bitový dočasný identifikátor přidělený Node B
- Jednoznačně identifikuje UE pro provoz na E-DCH v rámci buňky
- Používá se pro adresování na sdílených řídicích kanálech E-AGCH a E-RGCH
- Umožňuje efektivní multiplexování plánovacích příkazů pro více UE
- Může být změněno Node B (např. při změně obsluhující buňky)
- Nezbytné pro rychlé plánování řízené Node B v HSUPA

## Související pojmy

- [E-AGCH – EDCH – Absolute Grant Channel](/mobilnisite/slovnik/e-agch/)
- [E-RGCH – E-DCH Relative Grant Channel](/mobilnisite/slovnik/e-rgch/)

## Definující specifikace

- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [E-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-rnti/)
