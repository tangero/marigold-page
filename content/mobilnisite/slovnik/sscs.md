---
slug: "sscs"
url: "/mobilnisite/slovnik/sscs/"
type: "slovnik"
title: "SSCS – Service Specific Convergence Sublayer"
date: 2025-01-01
abbr: "SSCS"
fullName: "Service Specific Convergence Sublayer"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sscs/"
summary: "Podsložka v rámci adaptační vrstvy ATM (AAL), která přizpůsobuje protokoly vyšších vrstev podkladové službě ATM. V 3GPP často obsahuje SSCOP, aby zajistila spolehlivý přenos signalizace přes rozhraní"
---

SSCS (Service Specific Convergence Sublayer) je služebně specifická konvergenční podsložka v rámci adaptační vrstvy ATM, která přizpůsobuje protokoly vyšších vrstev podkladové službě ATM; v sítích 3GPP často využívá protokol SSCOP pro spolehlivý přenos signalizace.

## Popis

Služebně specifická konvergenční podsložka (SSCS) je součástí adaptační vrstvy [ATM](/mobilnisite/slovnik/atm/) ([AAL](/mobilnisite/slovnik/aal/)), jak je definováno v řadě [ITU-T](/mobilnisite/slovnik/itu-t/) I.363 a převzato 3GPP pro přenos v UMTS. AAL se dělí na dvě podsložky: konvergenční podsložku ([CS](/mobilnisite/slovnik/cs/)) a podsložku segmentace a zpětného složení ([SAR](/mobilnisite/slovnik/sar/)). Konvergenční podsložka se dále člení na společnou část konvergenční podsložky ([CPCS](/mobilnisite/slovnik/cpcs/)) a služebně specifickou konvergenční podsložku (SSCS). SSCS je, jak název napovídá, služebně specifická – poskytuje funkce přizpůsobené požadavkům konkrétní služby nebo protokolu vyšší vrstvy, jako je signalizace nebo přenos dat.

V kontextu 3GPP se SSCS primárně používá v přenosové síťové vrstvě pro signalizaci řídicí roviny přes rozhraní Iu a Iur, je-li využíván ATM. Pro přenos signalizace SSCS typicky obsahuje služebně specifický spojovaný protokol ([SSCOP](/mobilnisite/slovnik/sscop/)) a případně služebně specifickou koordinační funkci ([SSCF](/mobilnisite/slovnik/sscf/)). SSCF mapuje služby SSCOP na požadavky služby vyšší vrstvy, jako je Signal Connection Control Part (SCCP). SSCS pracuje nad společnou částí konvergenční podsložky AAL5 (CPCS), která zajišťuje funkce jako doplňování nebo detekci chyb pomocí CRC koncovky. SSCS přidává specifické schopnosti, jako je správa spojení, obnova po chybě a zaručený přenos dat, které CPCS neposkytuje.

Úlohou SSCS je přizpůsobit potřeby signalizačního protokolu vyšší vrstvy obecným službám nabízeným AAL5 a podkladovou vrstvou ATM. Zajišťuje, aby signalizační zprávy dostaly odpovídající kvalitu služby, spolehlivost a správné pořadí. Zapouzdřením SSCOP poskytuje SSCS spolehlivý, v pořadí zachovávající a tok řídící datový kanál pro kritickou komunikaci řídicí roviny mezi síťovými prvky, jako je RNC a MSC nebo SGSN. Tento vrstvený přístup umožňuje flexibilitu; pro různé služby lze definovat různé implementace SSCS, ačkoli v 3GPP UMTS je nejvýznamnější SSCS založená na SSCOP pro signalizaci.

## K čemu slouží

SSCS existuje za účelem překlenutí mezery mezi obecnými přenosovými službami poskytovanými ATM a specifickými požadavky aplikací vyšších vrstev, zejména signalizačních protokolů. AAL5 v ATM nabízí základní spojovanou službu, ale je primárně navržena pro segmentaci a zpětné složení dat s minimální kontrolou chyb. Signalizační protokoly však pro správnou funkci vyžadují spolehlivé, bezchybné a v pořadí zachované doručování. SSCS poskytuje toto služebně specifické přizpůsobení, aniž by vyžadovala, aby každý protokol vyšší vrstvy implementoval svou vlastní složitou adaptační logiku.

Ve 3GPP Release 99 byl ATM povinným přenosem pro rozhraní Iu a Iur. SSCS, obsahující SSCOP, byla nezbytná pro splnění přísných požadavků na spolehlivost signalizace řídicí roviny v rodící se síti UMTS. Řešila problém, jak přenášet signalizaci přes síť ATM, která byla optimalizována pro hromadná data, ale ne pro malé, kritické zprávy řídicích protokolů. Standardizací SSCS s SSCOP zajistilo 3GPP interoperabilitu mezi zařízeními RAN a CN od různých výrobců a poskytlo konzistentní a spolehlivý základ pro přenos signalizace, který podporoval správu mobility, zřizování hovorů a další vitální síťové funkce.

## Klíčové vlastnosti

- Je součástí adaptační vrstvy ATM a nachází se nad společnou částí konvergenční podsložky AAL5 (CPCS)
- Poskytuje služebně specifické přizpůsobení pro protokoly vyšších vrstev, zejména pro signalizaci
- Často obsahuje SSCOP, aby nabídla spolehlivý, spojovaný přenos dat
- Může zahrnovat služebně specifickou koordinační funkci (SSCF) pro mapování na služby vyšší vrstvy
- Umožňuje obnovu po chybě, zachování pořadí a řízení toku přizpůsobené potřebám signalizace
- Spolupracuje s podsložkou AAL5 SAR pro segmentaci a zpětné složení přes buňky ATM

## Související pojmy

- [AAL – ATM Adaptation Layer](/mobilnisite/slovnik/aal/)
- [SSCOP – Service Specific Connection Oriented Protocol](/mobilnisite/slovnik/sscop/)
- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)
- [CPCS – Common Part Convergence Sublayer](/mobilnisite/slovnik/cpcs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [SSCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sscs/)
