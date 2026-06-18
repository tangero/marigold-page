---
slug: "hsdpa"
url: "/mobilnisite/slovnik/hsdpa/"
type: "slovnik"
title: "HSDPA – High Speed Downlink Packet Access"
date: 2025-01-01
abbr: "HSDPA"
fullName: "High Speed Downlink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hsdpa/"
summary: "Vylepšení standardu 3GPP pro UMTS/WCDMA, které výrazně zvyšuje přenosové rychlosti ve směru downlink, často označované jako 3.5G. Zavádí nové fyzické kanály, adaptivní modulaci a kódování, hybridní AR"
---

HSDPA je vylepšení standardu 3GPP pro UMTS/WCDMA, které výrazně zvyšuje přenosové rychlosti ve směru downlink zavedením nových fyzických kanálů, adaptivní modulace, hybridního ARQ a rychlého plánování.

## Popis

High Speed Downlink Packet Access (HSDPA) je vylepšení rádiového rozhraní 3GPP pro UMTS (Universal Mobile Telecommunications System), které dramaticky zvyšuje propustnost paketových dat ve směru downlink a snižuje latenci. Z architektonického hlediska zavádí nové funkce primárně v Node B (základnové stanici) a v uživatelském zařízení (UE), čímž přesouvá klíčové plánování na vrstvě [MAC](/mobilnisite/slovnik/mac/) a řízení retransmisí z řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) do Node B. Tím se snižují zpracovatelské zpoždění. Klíčovým přidaným fyzickým kanálem je High-Speed Downlink Shared Channel ([HS-DSCH](/mobilnisite/slovnik/hs-dsch/)), což je sdílený transportní kanál používaný pro přenos uživatelských dat. Je asociován s několika řídicími kanály pro downlink a uplink: High-Speed Shared Control Channel ([HS-SCCH](/mobilnisite/slovnik/hs-scch/)) pro signalizaci ve směru downlink a High-Speed Dedicated Physical Control Channel ([HS-DPCCH](/mobilnisite/slovnik/hs-dpcch/)) pro zpětnou vazbu ve směru uplink.

HSDPA funguje za použití několika klíčových technik. Rychlá adaptace spojení (Fast Link Adaptation) upravuje schéma modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) každý 2ms přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/)) na základě hlášení indikátoru kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) od UE. Používá vyšší řád modulace (16-QAM vedle QPSK) pro dosažení špičkových rychlostí. Rychlý hybridní ARQ (HARQ) umožňuje rychlé retransmise na fyzické vrstvě, řízené Node B, což zlepšuje spolehlivost a efektivitu. Rychlé paketové plánování (Fast Packet Scheduling), také v Node B, rozhoduje, kterým uživatelům bude v každém TTI obsluha přidělena, na základě stavu kanálu a algoritmů spravedlivosti, čímž maximalizuje propustnost buňky. UE používá buffer pro přeřazení paketů přijatých mimo pořadí kvůli procesům HARQ.

V síti HSDPA koexistuje s legacy službami na vyhrazeném kanálu (DCH). RNC si zachovává kontrolu nad správou rádiových zdrojů, řízením přístupu a správou mobility (předávání hovorů), ale uživatelská rovina pro HSDPA je směrována přímo z Node B. Tato rozdělená architektura umožňuje plynulý upgrade z UMTS Release 99. HSDPA byl základním kamenem mobilního broadbandu, umožňujícím teoretické špičkové rychlosti od 1,8 Mbps v raných releasech až po více než 42 Mbps s pozdějšími vylepšeními multi-carrier a MIMO. Sloužil jako výkonnostní benchmark před nástupem LTE.

## K čemu slouží

HSDPA byl vytvořen, aby vyřešil nedostatečné datové rychlosti a vysokou latenci počátečních sítí UMTS Release 99, které byly nevyhovující pro nově se objevující internetové aplikace, jako je prohlížení webu s bohatým obsahem, e-maily s přílohami a rané streamování videa. Hlavním problémem byla centralizovaná architektura, kde RNC zpracovával veškeré plánování a retransmise, což zavádělo významné zpoždění (kolem 80-100 ms RTT) a omezovalo spektrální účinnost a špičkovou propustnost pro uživatele.

Motivací pro HSDPA, zavedené v Release 5, bylo přinést uživatelům internetové rychlosti a učinit 3G konkurenceschopnou širokopásmovou technologií. Vyřešil omezení přesunutím inteligence do Node B, což umožnilo rychlejší reakci na změny rádiového kanálu. Techniky jako adaptivní modulace, rychlé plánování a HARQ byly inspirovány koncepty z pevného broadbandu, ale přizpůsobeny pro mobilní prostředí. Tento vývoj byl hnání poptávkou operátorů po vyšší kapacitě a lepším uživatelském zážitku za účelem zvýšení příjmů z dat. HSDPA, často označovaný jako 3.5G, úspěšně prodloužil životní cyklus sítí UMTS a připravil cestu pro principy optimalizovaného paketového designu, které byly později plně realizovány v LTE.

## Klíčové vlastnosti

- High-Speed Downlink Shared Channel (HS-DSCH) s 2ms TTI
- Rychlé paketové plánování a adaptace spojení založené v Node B
- Podpora modulačních schémat QPSK a 16-QAM
- Rychlý hybridní ARQ (HARQ) s inkrementální redundancí
- Hlášení indikátoru kvality kanálu (CQI) od UE
- Vývoj k více-nosnému HSDPA (multi-carrier) a MIMO v pozdějších releasech

## Související pojmy

- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- … a dalších 26 specifikací

---

📖 **Anglický originál a plná specifikace:** [HSDPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/hsdpa/)
