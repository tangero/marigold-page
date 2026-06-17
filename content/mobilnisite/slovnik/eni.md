---
slug: "eni"
url: "/mobilnisite/slovnik/eni/"
type: "slovnik"
title: "ENI – E-UCCH Number Indication"
date: 2025-01-01
abbr: "ENI"
fullName: "E-UCCH Number Indication"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eni/"
summary: "ENI je specifický parametr řídicího kanálu používaný v režimu 1,28 Mcps TDD systému 3G UTRA (TD-SCDMA). Udává počet kódů Enhanced Uplink Control Channel (E-UCCH) přidělených pro signalizaci v uplinku,"
---

ENI je parametr řídicího kanálu TD-SCDMA, který udává počet kódů Enhanced Uplink Control Channel (E-UCCH) přidělených pro signalizaci v uplinku.

## Popis

[E-UCCH](/mobilnisite/slovnik/e-ucch/) Number Indication (ENI) je technický parametr definovaný ve specifikacích 3GPP pro rádiové rozhraní Time Division-Synchronous Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (TD-SCDMA), konkrétně pro jeho režim 1,28 Mcps TDD (Time Division Duplex). Působí v kontextu funkce Enhanced Uplink (EUL), známé jako [HSUPA](/mobilnisite/slovnik/hsupa/) ve [FDD](/mobilnisite/slovnik/fdd/) WCDMA, která byla adaptována pro TDD systém. ENI je kritická informace vysílaná sítí, která informuje všechna uživatelská zařízení (UE) v buňce o konfiguraci Enhanced Uplink Control Channel (E-UCCH).

E-UCCH je fyzický kanál, který UE používá k přenosu řídicích informací nezbytných pro Node B k úspěšné dekódaci přidruženého přenosu dat na Enhanced Dedicated Channel ([E-DCH](/mobilnisite/slovnik/e-dch/)). Tyto řídicí informace zahrnují Retransmission Sequence Number (RSN) a Happy Bit. Parametr ENI konkrétně udává počet kanalizačních kódů (tj. spreadingových kódů), které jsou přiděleny pro přenosy E-UCCH v uplink timeslotu. UE musí tento počet znát, aby mohlo správně monitorovat a interpretovat kódy E-UCCH od ostatních uživatelů, protože tuto informaci používá pro odhad interference a pro určení přesné sady kódů použitých pro svůj vlastní potenciální přenos na E-UCCH.

Z procedurálního hlediska je hodnota ENI součástí systémové informace vysílané na Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)). Je předávána v rámci specifických zpráv Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), jako je System Information Block 5 (SIB5) nebo SIB5bis v TD-SCDMA. Scheduler v Node B určuje hodnotu ENI na základě očekávaného zatížení v uplinku a potřeby zdrojů pro E-UCCH. UE tuto hodnotu čte během výběru/reselekce buňky nebo po přijetí aktualizace systémové informace. Správná interpretace ENI je nezbytná pro zpracování na fyzické vrstvě v UE, aby bylo v souladu s alokací zdrojů sítě, což zajišťuje spolehlivou dekódaci řídicí signalizace v uplinku a udržuje stabilitu a výkon funkce enhanced uplink.

## K čemu slouží

ENI byl zaveden pro podporu funkce Enhanced Uplink ve standardu TD-SCDMA (UTRA TDD 1.28 Mcps). Před zavedením EUL byly přenosové rychlosti a efektivita v uplinku TDD omezené. Funkce Enhanced Uplink, inspirovaná [HSUPA](/mobilnisite/slovnik/hsupa/) ve FDD, si kladla za cíl výrazně zlepšit výkon v uplinku pomocí technik jako je Node B řízené plánování, hybridní ARQ (HARQ) s měkkým kombinováním a kratší Transmission Time Intervals (TTI).

Klíčovou výzvou při implementaci této funkce ve sdílené struktuře timeslotů/kódů TD-SCDMA bylo efektivní řízení režie řídicí signalizace. E-UCCH byl definován pro přenos nezbytné zpětné vazby HARQ a plánování. Parametr ENI byl vytvořen, aby dynamicky informoval UE o velikosti kódového prostoru vyhrazeného pro tento řídicí kanál. Tato dynamická indikace byla nutná, protože pevná alokace by byla při proměnném síťovém zatížení neefektivní. Vysíláním ENI může síť pružně upravovat kapacitu řídicího kanálu, optimalizovat využití zdrojů mezi uživatelskými daty (E-DCH) a požadovanou řídicí signalizací (E-UCCH), čímž maximalizuje celkovou propustnost v uplinku a zisky kapacity, které funkce Enhanced Uplink nabízí.

## Klíčové vlastnosti

- Parametr specifický pro Enhanced Uplink v UTRA TDD 1,28 Mcps (TD-SCDMA).
- Udává počet kanalizačních kódů přidělených pro fyzický kanál E-UCCH.
- Vysílán jako část systémové informace (např. v SIB5) všem UE v buňce.
- Umožňuje UE správně identifikovat sadu kódů použitých pro řídicí signalizaci v uplinku.
- Nezbytný pro procedury fyzické vrstvy v UE související s monitorováním a přenosem na E-UCCH.
- Umožňuje síti dynamicky řídit alokaci zdrojů pro řídicí kanál v uplinku.

## Související pojmy

- [E-UCCH – E-DCH Uplink Control Channel](/mobilnisite/slovnik/e-ucch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)

## Definující specifikace

- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN

---

📖 **Anglický originál a plná specifikace:** [ENI na 3GPP Explorer](https://3gpp-explorer.com/glossary/eni/)
