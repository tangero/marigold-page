---
slug: "snpn"
url: "/mobilnisite/slovnik/snpn/"
type: "slovnik"
title: "SNPN – Standalone Non-Public Network"
date: 2026-01-01
abbr: "SNPN"
fullName: "Standalone Non-Public Network"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/snpn/"
summary: "Standalone Non-Public Network (SNPN, samostatná neveřejná síť) je 5G síť nasazená pro soukromé použití, provozovaná nezávisle na veřejných operátorech mobilních sítí. Slouží konkrétním podnikům, továr"
---

SNPN je samostatná 5G síť nasazená pro soukromé použití, provozovaná nezávisle na veřejných operátorech za účelem obsluhy konkrétních podniků s vyhrazenou konektivitou, zvýšeným zabezpečením a plnou kontrolou nad infrastrukturou.

## Popis

Standalone Non-Public Network (SNPN, samostatná neveřejná síť) je kompletní, nezávislý 5G systém definovaný 3GPP počínaje Release 16. Jedná se o neveřejnou síť ([NPN](/mobilnisite/slovnik/npn/)), která funguje pomocí 5G New Radio (NR) a síťových funkcí 5G Core (5GC), ale pro služby své core sítě není závislá na Public Land Mobile Network ([PLMN](/mobilnisite/slovnik/plmn/)). SNPN je identifikována jedinečnou kombinací PLMN ID (které je speciálně vyhrazeno pro použití NPN) a Network Identifier ([NID](/mobilnisite/slovnik/nid/)). Tento identifikátor SNPN (skládající se z PLMN ID a NID) umožňuje UE objevit a vybrat správnou privátní síť. Architektura zahrnuje všechny základní 5G síťové funkce: Next Generation Node B (gNB) pro rádiový přístup, Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)), Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a další, všechny nasazené v rámci privátní domény.

Fungování SNPN zahrnuje vyhrazené procedury pro objevování sítě, výběr a řízení přístupu. UE nakonfigurované pro přístup k SNPN skenuje buňky vysílající identifikátor SNPN. Po objevení zahájí UE registraci u SNPN. Kritickým aspektem provozu SNPN je autentizace a správa přihlašovacích údajů. SNPN podporují dva hlavní modely: použití přihlašovacích údajů spravovaných samotným operátorem SNPN, nebo použití přihlašovacích údajů poskytnutých samostatnou Credential Holder. Používají se metody 5G Authentication and Key Agreement (5G-AKA) nebo metody založené na EAP, často za účasti privátního autentizačního serveru. Síť může vynucovat striktní řízení přístupu, umožňující připojení pouze předem autorizovaným UE (např. firemním zařízením, senzorům).

Úlohou SNPN je poskytnout bezpečnou, izolovanou a výkonnou komunikační platformu pro vertikální odvětví. Umožňuje funkce jako network slicing, ultra-reliable low-latency communication (URLLC) a massive machine-type communication (mMTC) přizpůsobené specifickým potřebám továrny, přístavu, nemocnice nebo energetické sítě. Operátor SNPN má plnou kontrolu nad konfigurací sítě, politikami a daty, což zajišťuje, že citlivý provoz zůstává v lokalitě a není směrován přes veřejné sítě. To z SNPN činí základní kámen pro Průmysl 4.0, umožňující pokročilé případy užití jako automatizovaná vozidla, řízení procesů v reálném čase a údržba asistovaná rozšířenou realitou.

## K čemu slouží

SNPN byly vytvořeny, aby splnily přísné požadavky digitální transformace průmyslu a podniků, které veřejné sítě nemohly plně uspokojit. Veřejné sítě jsou navrženy pro široké pokrytí spotřebitelů a služby obecného určení, často postrádají garantovaný výkon, ultra-nízkou latenci, datovou suverenitu a hluboké přizpůsobení potřebné pro kritické průmyslové operace. Předchozí přístupy, jako lokální Wi-Fi nebo privátní sítě založené na LTE, buď nebyly standardizovány pro bezproblémovou mobilitu a integraci služeb (Wi-Fi), nebo postrádaly plnou sadu funkcí a architektonickou jasnost 5G (privátní LTE před Release 16).

Hlavní problémy, které SNPN řeší, jsou: 1) **Izolace a zabezpečení**: Poskytnutí fyzicky nebo logicky izolované sítě, kde citlivá data nikdy neopustí lokalitu, což je klíčové pro ochranu duševního vlastnictví a zabezpečení operační technologie (OT). 2) **Předvídatelný výkon**: Nabídka vyhrazených zdrojů se garantovanými Service Level Agreements (SLA) pro latenci, spolehlivost a šířku pásma, což je nezbytné pro časově citlivou průmyslovou automatizaci. 3) **Provozní autonomie**: Umožnění podniku vlastnit a provozovat síť nezávisle, bez závislosti na prioritách nebo časových plánech veřejného operátora mobilní sítě. Motivací pro standardizaci SNPN v 3GPP bylo vytvoření globálně harmonizovaného, interoperabilního rámce pro privátní 5G, vyhnutí se proprietárním řešením a podpora zdravého ekosystému síťového vybavení a zařízení.

## Klíčové vlastnosti

- Funguje nezávisle na infrastruktuře veřejné PLMN s využitím vyhrazeného 5GC a NR
- Identifikována jedinečnou kombinací PLMN ID a Network Identifier (NID)
- Podporuje flexibilní modely autentizace, včetně integrace s externími Credential Holders
- Umožňuje podniku plnou kontrolu nad síťovými politikami, slicingem a směrováním dat
- Poskytuje vyhrazenou kapacitu a garantovaný výkon pro aplikace kritické pro činnost
- Usnadňuje bezpečné onboarding a řízení přístupu pouze pro autorizovaná UE a zařízení

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.848** (Rel-19) — Study on Interconnect of SNPN
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.041** (Rel-19) — Cell Broadcast Service and Public Warning System
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.166** (Rel-19) — IMS Conferencing Management Object
- … a dalších 57 specifikací

---

📖 **Anglický originál a plná specifikace:** [SNPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/snpn/)
