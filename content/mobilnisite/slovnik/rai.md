---
slug: "rai"
url: "/mobilnisite/slovnik/rai/"
type: "slovnik"
title: "RAI – Routing Area Identity"
date: 2025-01-01
abbr: "RAI"
fullName: "Routing Area Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rai/"
summary: "Identifikátor lokální oblasti používaný v paketových jádrových sítích 2G (GPRS) a 3G (UMTS). Jednoznačně identifikuje směrovací oblast (RA) v rámci PLMN a používá se pro správu mobility, konkrétně pro"
---

RAI je identifikátor lokální oblasti používaný v paketových sítích 2G a 3G, který jednoznačně identifikuje směrovací oblast (Routing Area) v rámci PLMN pro volání (paging) a sledování mobilních zařízení pro paketové datové služby.

## Popis

Routing Area Identity (RAI) je klíčový identifikátor v architektuře paketové domény 2G ([GPRS](/mobilnisite/slovnik/gprs/)) a 3G (UMTS). Jednoznačně identifikuje směrovací oblast ([RA](/mobilnisite/slovnik/ra/)), což je pododdělení lokální oblasti ([LA](/mobilnisite/slovnik/la/)) používané pro služby s přepojováním okruhů. RA je skupina buněk definovaná za účelem sledování a volání (paging) uživatelského zařízení (UE), které používá paketové datové služby. RAI je tvořen z několika složek: Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)), Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)), Location Area Code ([LAC](/mobilnisite/slovnik/lac/)) a Routing Area Code ([RAC](/mobilnisite/slovnik/rac/)). Strukturálně platí: RAI = MCC + MNC + LAC + RAC. Tato hierarchická struktura umožňuje síti přesně lokalizovat UE na úrovni směrovací oblasti pro efektivní správu mobility v paketové doméně.

Jeho funkce je nedílnou součástí procedur GPRS Mobility Management ([GMM](/mobilnisite/slovnik/gmm/)) a UMTS Mobility Management (MM). Když se UE připojuje pro paketové datové služby, provádí proceduru aktualizace směrovací oblasti (RAU) se Serving GPRS Support Node (SGSN) a poskytuje svůj aktuální RAI. SGSN ukládá tento RAI do kontextu mobility UE. Dokud je UE ve stavu připraveno (aktivně komunikuje), síť zná jeho přesnou buňku. Když přejde do klidového stavu, provede RAU pouze tehdy, když zjistí, že vstoupilo do nové směrovací oblasti (načtením RAI vysílaného v systémové informaci buňky). Pokud pro klidové UE dorazí příchozí paket, SGSN zahájí volání (paging) ve všech buňkách patřících k RAI uloženému v jeho kontextu, čímž UE lokalizuje bez potřeby přesnosti na úrovni buňky.

Jeho úlohou je vyvážit signalizační zátěž a efektivitu volání (paging). Bez RA by síť musela volat (page) v celé lokální oblasti (která může být velmi rozsáhlá) kvůli paketovým datům, což by zvýšilo zatížení kanálu pro volání. Definováním menších RA specificky pro paketový provoz je volání cílenější. RAI se používá v zprávách mezi UE a SGSN (např. Attach, RAU požadavky) a uvnitř jádrové sítě mezi SGSN během aktualizací směrovací oblasti mezi SGSN. Je to základní koncept pro mobilitu v paketové doméně, který předcházel konceptu sledovací oblasti (TA) používanému v 4G LTE a 5G.

## K čemu slouží

RAI byl vytvořen se zavedením služby General Packet Radio Service (GPRS) za účelem umožnění efektivní správy mobility pro paketová data. Před GPRS měly sítě GSM pouze lokální oblasti (LA) pro mobilitu hlasu s přepojováním okruhů. Charakter provozu paketových dat (více impulzní, potenciálně delší klidová období) vyžadoval jinou úroveň podrobnosti pro sledování a volání (paging), aby se optimalizovalo signalizování a využití zdrojů.

RAI řeší problém, jak lokalizovat mobilní zařízení schopné přenosu paketových dat bez nadměrné signalizační režie. Definováním směrovacích oblastí jako podmnožin lokálních oblastí může síť sledovat paketová UE přesněji než s rozsáhlejší LA, což vede k efektivnějšímu volání (paging). Toto bylo klíčovou inovací, která oddělila správu mobility pro paketovou a okruhovou doménu, což umožnilo optimalizovat každou z nich pro příslušné charakteristiky provozu. Řešilo to omezení použití jediné, hrubé lokální oblasti pro všechny služby, což by bylo neefektivní pro tehdy vznikající mobilní datové služby.

## Klíčové vlastnosti

- Jednoznačně identifikuje směrovací oblast (Routing Area) v rámci PLMN
- Tvořen z MCC, MNC, LAC a RAC
- Používá se pro správu mobility v paketové doméně GPRS/UMTS (GMM/MM)
- Umožňuje procedury aktualizace směrovací oblasti (RAU)
- Definuje oblast pro volání (paging) klidových UE kvůli paketovým datům
- Vysílán v systémové informaci pro identifikaci UE

## Související pojmy

- [LAI – Location Area Identity](/mobilnisite/slovnik/lai/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [TAI – Tracking Area Identifier](/mobilnisite/slovnik/tai/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.731** (Rel-16) — 5G LCS Architecture Enhancement Study
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [RAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rai/)
