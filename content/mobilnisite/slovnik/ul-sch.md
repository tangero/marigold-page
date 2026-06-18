---
slug: "ul-sch"
url: "/mobilnisite/slovnik/ul-sch/"
type: "slovnik"
title: "UL-SCH – Uplink Shared Channel"
date: 2025-01-01
abbr: "UL-SCH"
fullName: "Uplink Shared Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ul-sch/"
summary: "Hlavní transportní kanál pro přenos dat a řídicích informací z uživatelského zařízení (UE) do síťové infrastruktury v LTE a NR. Umožňuje dynamické a efektivní sdílení radiofrekvenčních zdrojů mezi víc"
---

UL-SCH je hlavní transportní kanál v LTE a NR pro přenos dat a řídicích informací z UE do síťové infrastruktury, který umožňuje dynamické sdílení radiofrekvenčních zdrojů pro přenos paketových dat.

## Popis

Uplink Shared Channel (UL-SCH) je základní transportní kanál definovaný ve standardech LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) i NR (New Radio). Je hlavním prostředkem pro přenos uživatelských dat, řídicích informací vyšších vrstev (např. [RRC](/mobilnisite/slovnik/rrc/) zpráv, [NAS](/mobilnisite/slovnik/nas/) zpráv) a některých řídicích informací fyzické vrstvy z UE do gNB (v NR) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE). Kanál je charakteristický svým sdíleným charakterem – jeho fyzické zdroje jsou dynamicky přidělovány různým UE prostřednictvím síťového plánovače na základě každého podrámce nebo slotu. Tato dynamická plánování, signalizovaná přes Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)), umožňuje vysokou efektivitu statistického multiplexování uplinkového provozu a adaptaci na nárazový charakter datových aplikací.

Z procesního hlediska zpracování transportního bloku UL-SCH zahrnuje několik klíčových kroků fyzické vrstvy. Pro plánovaný přenos vrstva [MAC](/mobilnisite/slovnik/mac/) předá transportní blok fyzické vrstvě. Tento blok podstupuje procesy, které zahrnují přidání [CRC](/mobilnisite/slovnik/crc/) transportního bloku, segmentaci kódových bloků a přidání CRC, kanálové kódování (typicky [LDPC](/mobilnisite/slovnik/ldpc/) v NR, Turbo kódování v LTE), rate matching a spojení kódových bloků. Výsledné kódové slovo je pak namapováno na Physical Uplink Shared Channel (PUSCH) pro přenos. Kritickou vlastností UL-SCH je podpora Hybrid Automatic Repeat Request (HARQ). Každý přenos je asociován s HARQ procesem, což umožňuje rychlé retransmise při dekódování selhání na přijímací straně, což je klíčové pro dosažení vysoké spolehlivosti a nízké latence.

Role UL-SCH přesahuje pouhé doručení dat. Je pevně integrován s řídicím signalizováním uplinku. Například Uplink Control Information (UCI), jako HARQ potvrzení pro downlinková data (ACK/NACK) a reporty Channel State Information (CSI), může být multiplexováno s uplinkovými datami na PUSCH, když UE má platný UL-SCH grant. Toto přibalení zvyšuje efektivitu využití zdrojů. Dále UL-SCH podporuje adaptivní modulaci a kódování (AMC), kde modulační schéma (např. QPSK, 16QAM, 64QAM, 256QAM) a kódovací rychlost jsou upraveny na základě aktuální kvality uplinkového kanálu reportované UE nebo odhadované prostřednictvím sounding reference signals (SRS). Toto zajišťuje optimální spektrální efektivitu při různých radiofrekvenčních podmínkách.

## K čemu slouží

UL-SCH byl vytvořen k řešení potřeb flexibilního, efektivního a vysokokapacitního uplinkového transportního mechanismu pro paketově-switched služby v 3GPP systémech 4G LTE a 5G NR. Předchozí 3G systémy jako UMTS závisely na dedikovaných kanálech (DCH) pro uživatelská data, které byly neefektivní pro nárazový internetový provoz, protože rezervovaly zdroje pro uživatele i během idle period. Paradigma sdíleného kanálu, představené s High-Speed Uplink Packet Access (HSUPA) Enhanced Dedicated Channel (E-DCH), bylo plně realizované a optimalizované v LTE s UL-SCH.

Primární motivací bylo maximalizovat spektrální efektivitu a kapacitu systému v uplinkovém směru, který je často limitujícím faktorem kvůli omezenému výkonu UE a potřebě ortogonálního multiple accessu. Díky možnosti plánovače základové stanice dynamicky přidělovat čas-frekvenční zdroje UE přesně, když mají data k odeslání, UL-SCH eliminuje ztráty spojené s permanentně přidělenými okruhy. Tato dynamická alokace také umožňuje pokročilé techniky jako frekvenčně-selektivní plánování, kde plánovač může přidělit zdroje ve frekvenčních pásmech, kde konkrétní UE má dobré kanálové podmínky, což zvyšuje robustnost linky a datové rychlosti.

Dále, design UL-SCH s podporou rychlého HARQ a AMC byl klíčový pro splnění nízké latence a vysoké spolehlivosti požadavků real-time služeb plánovaných pro LTE a následně vylepšených pro NR. Poskytuje základní transportní vrstvu, na které jsou vybudované všechny uplink-centrické služby – od webového browsingu a uploadu souborů až po VoIP a ultra-reliable low-latency communications (URLLC) – což ho staví jako základní pilíř moderní uplinkové architektury mobilních sítí.

## Klíčové vlastnosti

- Dynamická alokace zdrojů prostřednictvím síťového plánování (grant-based přístup)
- Podpora Hybrid ARQ (HARQ) s více paralelními procesy pro retransmise s nízkou latencí
- Adaptivní modulace a kódování (AMC) na základě kanálových podmínek
- Multiplexování uživatelských dat a Uplink Control Information (UCI) na stejný fyzický zdroj
- Podpora contention-free přenosu a, v NR, configured grant (grant-free) přenosu pro nízkou latenci
- Zpracování transportního bloku zahrnující kanálové kódování (LDPC v NR, Turbo v LTE), scrambling a modulaci

## Související pojmy

- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [UCI – Uplink Control Information](/mobilnisite/slovnik/uci/)
- [SRS – Space Radiocommunication Stations](/mobilnisite/slovnik/srs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [UL-SCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ul-sch/)
