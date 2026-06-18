---
slug: "prb"
url: "/mobilnisite/slovnik/prb/"
type: "slovnik"
title: "PRB – Physical Resource Block"
date: 2025-01-01
abbr: "PRB"
fullName: "Physical Resource Block"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/prb/"
summary: "PRB je základní jednotkou alokace rádiových zdrojů v LTE a NR, která zahrnuje soubor subnosných a OFDM symbolů. Definuje časově-frekvenční mřížku sloužící k plánování dat uživatelů a řídicích kanálů,"
---

PRB je základní jednotkou alokace rádiových zdrojů v LTE a NR, která definuje časově-frekvenční mřížku subnosných a OFDM symbolů sloužících k plánování dat uživatelů a řídicích kanálů.

## Popis

Fyzický zdrojový blok (PRB) je nejmenším prvkem alokace zdrojů, který může být přidělen uživatelskému zařízení (UE) v downlinku nebo uplinku systémů LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). Představuje souvislý blok zdrojů ve frekvenční a časové doméně. Ve frekvenční doméně se PRB skládá z 12 po sobě jdoucích subnosných. V časové doméně zahrnuje jeden slot, který obsahuje konfigurovatelný počet [OFDM](/mobilnisite/slovnik/ofdm/) symbolů (např. 7 nebo 14 symbolů pro normální a rozšířený cyklický prefix v LTE a flexibilní numerologii v NR). Součin těchto rozměrů definuje celkový počet zdrojových elementů ([RE](/mobilnisite/slovnik/re/)) v rámci jednoho PRB, přičemž každý RE je jedna subnosná na dobu trvání jednoho symbolu.

Z architektonického hlediska je PRB ústředním konstruktem schémat Orthogonal Frequency Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([OFDMA](/mobilnisite/slovnik/ofdma/)) a Single-Carrier [FDMA](/mobilnisite/slovnik/fdma/) ([SC-FDMA](/mobilnisite/slovnik/sc-fdma/)) používaných v LTE a NR. Celková systémová šířka pásma je rozdělena na sadu dostupných PRB. Plánovač v základnové stanici (eNodeB v LTE, gNodeB v NR) dynamicky přiděluje konkrétní PRB různým UE na základě faktorů, jako je kvalita kanálu, požadavky QoS a zatížení provozem. Tato granulární alokace umožňuje diverzitu více uživatelů a frekvenčně-selektivní plánování, kdy jsou uživatelům přidělovány zdroje v těch částech spektra, kde jsou jejich kanálové podmínky nejlepší.

Jak funguje, zahrnuje mapování dat a řídicích informací z vyšších vrstev na mřížku fyzických zdrojů. Transportní bloky z vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) jsou kanálově kódovány, modulovány a následně mapovány na zdrojové elementy přidělených PRB. Řídicí kanály, jako je Physical Downlink Control Channel (PDCCH), a referenční signály (např. Cell-Specific Reference Signals v LTE, Demodulation Reference Signals v NR) jsou také mapovány na specifické RE v rámci struktury PRB. Úroveň výkonu na PRB, jak je definována ve specifikacích, je klíčovým parametrem pro adaptaci spoje a správu interferencí.

V NR se tento koncept vyvinul se zavedením flexibilní numerologie. Rozteč subnosných (SCS) a délka slotu nejsou pevné, ale škálují se s numerologií (μ). Proto se absolutní šířka pásma PRB (12 * SCS) a jeho trvání podle toho mění. To umožňuje NR efektivně podporovat různé typy služeb, od rozšířeného mobilního širokopásmového připojení (eMBB) se širokými PRB až po ultra-spolehlivou komunikaci s nízkou latencí (URLLC) s kratšími a časově početnějšími PRB. PRB zůstává atomární jednotkou plánování, ale jeho rozměry jsou přizpůsobitelné scénáři nasazení.

## K čemu slouží

PRB byl vytvořen, aby poskytl standardizovanou, efektivní a flexibilní jednotku pro správu rádiových zdrojů v buňkových systémech založených na OFDMA. Před LTE používal 3G UMTS mnohonásobný přístup s kódovým dělením (CDMA), kde byly zdroje primárně rozlišovány rozprostíracími kódy, což znemožňovalo jemně odstupňované plánování ve frekvenční doméně. Přechod na OFDMA v LTE vyžadoval nový paradigmat pro dělení a přidělování sdíleného časově-frekvenčního zdroje mezi uživateli.

PRB řeší problém granulární alokace zdrojů. Rozdělením spektra na malé, plánovatelné bloky umožňuje systému využívat frekvenčně-selektivní útlum – přidělovat zdroje uživatelům na jejich nejlepších frekvencích. To ve srovnání s širokopásmovou alokací dramaticky zlepšuje spektrální účinnost a propustnost uživatelů. Také usnadňuje pokročilé techniky, jako je částečné frekvenční využití pro koordinaci interferencí v heterogenních sítích.

PRB navíc poskytuje společný referenční bod pro definování šířek kanálů, úrovní výkonu a požadavků na výkon. Specifikace definují parametry jako 'vysílaný výkon na přidělený RB', aby zajistily konzistentní RF výkon. Mřížka PRB také strukturovaně umisťuje nezbytné signály, jako jsou referenční signály a synchronizační signály, a zajišťuje předvídatelné chování sítě. Jeho návrh v LTE (od Release 8) a následné vylepšení v NR (od Release 15) bylo motivováno potřebou škálovatelné jednotky zdrojů, která by mohla podporovat neustále rostoucí datové toky, různé požadavky na latenci a široké spektrum kmitočtových pásem od pásem pod 1 GHz až po milimetrové vlny.

## Klíčové vlastnosti

- Definován jako 12 po sobě jdoucích subnosných ve frekvenci a jeden slot v čase
- Nejmenší plánovatelná jednotka zdrojů pro data uživatelů a řídicí kanály
- Umožňuje frekvenčně-selektivní plánování a diverzitu více uživatelů
- Rozměry jsou v NR flexibilní na základě škálovatelné numerologie (rozteče subnosných)
- Poskytuje strukturu pro mapování referenčních signálů a řídicích informací
- Základní pro definování šířky kanálu a výkonové spektrální hustoty

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [SC-FDMA – Single Carrier – Frequency Division Multiple Access](/mobilnisite/slovnik/sc-fdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 32.521** (Rel-11) — SON Policy NRM IRP Requirements
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.314** (Rel-19) — E-UTRA Radio Measurements Specification
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements
- … a dalších 41 specifikací

---

📖 **Anglický originál a plná specifikace:** [PRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/prb/)
