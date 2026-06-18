---
slug: "pusch"
url: "/mobilnisite/slovnik/pusch/"
type: "slovnik"
title: "PUSCH – Physical Uplink Shared Channel"
date: 2025-01-01
abbr: "PUSCH"
fullName: "Physical Uplink Shared Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pusch/"
summary: "Physical Uplink Shared Channel (PUSCH) je hlavní transportní kanál pro uplink v 3GPP technologiích rádiového přístupu, používaný k přenosu uživatelských dat a řídicích informací z uživatelského zaříze"
---

PUSCH je hlavní dynamicky naplánovaný kanál pro uplink v sítích 3GPP, který uživatelské zařízení (UE) využívá jako sdílený zdroj k vysílání uživatelských dat i řídicích informací k základnové stanici.

## Popis

Physical Uplink Shared Channel (PUSCH) je základní fyzický kanál definovaný ve specifikacích 3GPP pro uplinkový přenos z uživatelského zařízení (UE) k síťové základnové stanici (NodeB v UMTS, eNodeB v LTE, gNB v NR). Slouží jako hlavní cesta pro uplinková data uživatelské roviny, jako jsou aplikační data ze smartphonu, a může také přenášet uplinkové řídicí informace ([UCI](/mobilnisite/slovnik/uci/)), je-li tak nakonfigurován. Kanál je označován jako „sdílený“, protože jeho časově-frekvenční zdroje jsou dynamicky přidělovány síťovým plánovačem různým UE, což umožňuje statistický multiplex a efektivní využití dostupného rádiového spektra. Toto dynamické plánování je základním kamenem moderních celulárních systémů, umožňujícím jejich adaptaci na proměnlivou zátěž a podmínky na rádiovém kanálu.

Z technického pohledu je provoz PUSCH řízen mechanismem přístupu na základě povolení. UE musí před vysíláním od sítě obdržet povolení pro uplink, typicky prostřednictvím zprávy Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). Toto povolení specifikuje klíčové parametry přenosu, jako jsou přidělené zdrojové bloky (čas a frekvence), schéma modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)), povely pro řízení výkonu a informace o předkódování pro [MIMO](/mobilnisite/slovnik/mimo/). Po obdržení platného povolení UE zpracuje svůj transportní blok (data) prostřednictvím řady procedur fyzické vrstvy včetně kanálového kódování (např. Turbo kód v LTE, [LDPC](/mobilnisite/slovnik/ldpc/) v NR), skramblování, modulace (např. [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), 64QAM, 256QAM), mapování vrstev pro MIMO, předkódování a nakonec mapování na přidělené zdrojové elementy na vlnovém tvaru OFDM (v LTE) nebo DFT-s-OFDM/CP-OFDM (v NR).

Architektura PUSCH je úzce propojena s ostatními fyzickými kanály a signály. Například Demodulation Reference Signal (DM-RS) je vysílán společně s PUSCH ve stejných přidělených zdrojích, aby umožnil základnové stanici odhadnout rádiový kanál pro koherentní demodulaci. Sounding Reference Signal (SRS), vysílaný samostatně, pomáhá síťovému plánovači pochopit kvalitu uplinkového kanálu pro informovaná rozhodnutí o plánování. Dále PUSCH podporuje hybridní automatické opakování na vyžádání (HARQ) s více paralelními procesy, což umožňuje rychlé retransmise v případě chyb dekódování, což je klíčové pro dosažení vysoké spolehlivosti a nízké latence. V 5G NR přinesl návrh PUSCH větší flexibilitu, podporuje více numerologií (rozestupy podnosných), přenosy založené na mini-time slotech pro ultra-spolehlivou komunikaci s nízkou latencí (URLLC) a vylepšenou podporu pro přenosy bez povolení (configured grant) za účelem snížení latence pro periodický provoz.

## K čemu slouží

PUSCH byl vytvořen, aby poskytl efektivní, flexibilní a vysokokapacitní mechanismus pro přenos dat v uplinku v systémech 3GPP, což představuje posun oproti přepojování okruhů a paradigmatu vyhrazených kanálů starších 2G systémů. Před vznikem sdílených kanálů byly uplinkové zdroje často přidělovány staticky, což vedlo k neefektivnímu využití spektra, když byl datový provoz uživatele dávkový nebo přerušovaný. Zavedení konceptu sdíleného kanálu, počínaje vylepšením High-Speed Uplink Packet Access (HSUPA) v UMTS a plně realizovaného v LTE, toto řešilo tím, že umožnilo síti dynamicky přidělovat zdroje ve velmi krátkých časových intervalech (např. každý 1 ms subrámec v LTE) pouze těm uživatelům, kteří mají v danou chvíli skutečně data k odeslání.

Toto dynamické přidělování řeší základní problém nedostatku rádiových zdrojů. Sdílením kanálu mezi mnoho uživatelů na základě okamžité potřeby PUSCH maximalizuje celkovou propustnost a kapacitu systému. Také umožňuje pokročilé rádiové funkce, jako je adaptace spojení, kde se schéma modulace a kódování přizpůsobuje podle hlášené kvality kanálu, a víceuživatelský MIMO, kde jsou prostorové vrstvy použity k obsluze více uživatelů současně na stejných časově-frekvenčních zdrojích. Evoluce do 5G NR dále zdokonalila jeho účel, aby podporoval mnohem širší škálu služeb, od rozšířeného mobilního širokopásmového přístupu (eMBB) s velmi vysokými datovými rychlostmi až po hromadnou komunikaci mezi stroji (mMTC) a ultra-spolehlivou komunikaci s nízkou latencí (URLLC), což vyžaduje funkce jako přístup bez povolení a podpora různých numerologií.

## Klíčové vlastnosti

- Dynamické plánování prostřednictvím povolení pro uplink přenášených v DCI
- Podpora více modulačních schémat (od QPSK po 256QAM) a adaptivního kódování
- Integrace s DM-RS pro odhad kanálu a koherentní demodulaci
- Hybridní ARQ (HARQ) s více paralelními procesy pro spolehlivost
- Podpora přenosů pro jednoho uživatele (SU-MIMO) i pro více uživatelů (MU-MIMO)
- V 5G NR podpora jak vlnových tvarů CP-OFDM a DFT-s-OFDM, tak konfigurovatelného provozu bez okamžitého povolení (grant-free)

## Související pojmy

- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)
- [SRS – Space Radiocommunication Stations](/mobilnisite/slovnik/srs/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [PUSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pusch/)
