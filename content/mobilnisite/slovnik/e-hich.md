---
slug: "e-hich"
url: "/mobilnisite/slovnik/e-hich/"
type: "slovnik"
title: "E-HICH – EDCH HARQ Acknowledgement Indicator Channel"
date: 2025-01-01
abbr: "E-HICH"
fullName: "EDCH HARQ Acknowledgement Indicator Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-hich/"
summary: "Sestupný fyzický kanál v UMTS/HSPA používaný v Node B k odesílání hybridních ARQ (HARQ) potvrzení pro sestupná data přenášená na E-DCH. Informuje UE, zda byl jeho přenesený datový paket úspěšně přijat"
---

E-HICH je sestupný kanál UMTS/HSPA, který Node B používá k odesílání HARQ potvrzení pro sestupná data E-DCH, čímž informuje UE, zda byl paket úspěšně přijat nebo je vyžadován jeho opakovaný přenos.

## Popis

EDCH [HARQ](/mobilnisite/slovnik/harq/) Acknowledgement Indicator Channel (E-HICH) je vyhrazený sestupný fyzický řídicí kanál definovaný v rámci specifikací 3GPP UMTS a High-Speed Packet Access ([HSPA](/mobilnisite/slovnik/hspa/)), konkrétně pro Enhanced Uplink (EUL), známý také jako [HSUPA](/mobilnisite/slovnik/hsupa/). Funguje na fyzické vrstvě (vrstva 1) rozhraní. E-HICH je přenášen z Node B (základnová stanice) ke konkrétnímu uživatelskému zařízení (UE) za účelem poskytnutí zpětné vazby pro proces Hybrid Automatic Repeat Request (HARQ) používaný na sestupném Enhanced Dedicated Channel ([E-DCH](/mobilnisite/slovnik/e-dch/)). Jeho jedinou funkcí je přenášet indikátor HARQ Acknowledgement ([ACK](/mobilnisite/slovnik/ack/)) nebo Negative Acknowledgement ([NACK](/mobilnisite/slovnik/nack/)) pro dříve přijatý transportní blok E-DCH. Technicky kanál používá sekvenci [QPSK](/mobilnisite/slovnik/qpsk/) symbolů k reprezentaci signálu ACK/NACK. K rozlišení přenosů E-HICH určených pro různá UE nebo různé procesy HARQ se používá specifická signaturní sekvence odvozená z parametrů, jako je E-DCH Radio Network Temporary Identifier ([E-RNTI](/mobilnisite/slovnik/e-rnti/)) a identifikátor procesu HARQ. UE kontinuálně monitoruje svůj přidělený E-HICH během příslušného časového intervalu poté, co přenese paket E-DCH. Pokud je detekován ACK, UE ví, že paket byl úspěšně dekódován Node B, a může pokračovat v odesílání nových dat. Pokud je detekován NACK (nebo pokud není detekováno nic, což implikuje scénář DTX), UE naplánuje opakovaný přenos stejného datového paketu s využitím inkrementální redundance jako součásti procesu HARQ. Tato rychlá smyčka zpětné vazby, probíhající v mnoha konfiguracích během 2ms Transmission Time Interval (TTI), je tím, co umožňuje nízkou latenci a vysokou spolehlivost charakteristické pro HSUPA. E-HICH je vždy spárován s E-RGCH (Relative Grant Channel) na stejném sestupném kanalizačním kódu a jejich signály jsou kódově multiplexovány.

## K čemu slouží

E-HICH byl vytvořen speciálně pro podporu funkce Enhanced Uplink (E-DCH) zavedené v 3GPP Release 6 (HSUPA). Před HSUPA spoléhala sestupná paketová data na Dedicated Channel (DCH) na opakovaných přenosech na vrstvě RLC řízených RNC, což přinášelo významnou latenci. Účelem E-HICH je umožnit rychlé opakované přenosy Hybrid ARQ (HARQ) na fyzické vrstvě řízené přímo Node B. Tím se řeší problém pomalé opravy chyb v sestupném směru a neefektivního využití spektra. Poskytnutím zpětné vazby ACK/NACK během milisekund přímo od přijímající entity (Node B) umožňuje velmi rychlé opakované přenosy chybných datových paketů, což dramaticky zlepšuje propustnost v sestupném směru, snižuje latenci a zvyšuje celkovou spektrální účinnost. Motivací bylo učinit sestupný směr UMTS konkurenceschopným vůči vylepšením sestupného směru poskytovaným HSDPA a vytvořit tak symetrický zážitek z vysokorychlostního přístupu k paketovým datům. E-HICH je základním prvkem umožňujícím řízení plánování a rychlý HARQ řízený Node B, které definují výkonnostní zisky HSUPA oproti předchozím verzím UMTS.

## Klíčové vlastnosti

- Přenáší zpětnou vazbu HARQ ACK/NACK pro sestupné přenosy E-DCH
- Funguje s krátkým Transmission Time Interval (např. 2ms TTI) pro nízkou latenci
- Používá jedinečné signaturní sekvence pro identifikaci UE a procesu HARQ
- Fyzicky kódově multiplexován s E-RGCH na stejném kanalizačním kódu
- Umožňuje rychlé opakované přenosy řízené Node B pro zlepšenou spolehlivost v sestupném směru
- Integrální součást signalizace fyzické vrstvy HSUPA (E-DCH)

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [E-RGCH – E-DCH Relative Grant Channel](/mobilnisite/slovnik/e-rgch/)
- [E-RNTI – E-DCH Radio Network Temporary Identifier](/mobilnisite/slovnik/e-rnti/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [E-HICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-hich/)
