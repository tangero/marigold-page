---
slug: "rtc"
url: "/mobilnisite/slovnik/rtc/"
type: "slovnik"
title: "RTC – Real-Time (media) Communication"
date: 2025-01-01
abbr: "RTC"
fullName: "Real-Time (media) Communication"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rtc/"
summary: "RTC označuje soubor služeb a protokolů standardizovaných 3GPP, které umožňují komunikaci s interaktivními médii v reálném čase, jako jsou hlasové a videohovory, přes IP sítě. Je klíčové pro poskytován"
---

RTC je soubor služeb a protokolů standardizovaných 3GPP, které umožňují komunikaci s interaktivními médii v reálném čase, jako jsou hlasové a videohovory, přes IP sítě.

## Popis

Komunikace v reálném čase (RTC) v rámci 3GPP zahrnuje architekturu, protokoly a kodeky navržené pro podporu interaktivních, na zpoždění citlivých mediálních relací přes IP sítě, primárně přes IMS (IP Multimedia Subsystem). Jádrem RTC je vytváření a správa mediálních toků pomocí protokolu [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) pro signalizaci a protokolu [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol) pro vlastní přenos médií. Jádro IMS poskytuje funkce řídicí roviny – včetně registrace, směrování relací a interakce s politikami – zatímco uživatelské zařízení (UE) a mediální brány zajišťují rovinu médií. Mezi klíčové architektonické komponenty patří [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-Call Session Control Function) jako první kontaktní bod pro UE, [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving-CSCF) pro řízení relací a [MRF](/mobilnisite/slovnik/mrf/) (Media Resource Function) pro konferenční hovory a generování tónů. Kvalita služeb (QoS) je nedílnou součástí, přičemž [PCRF](/mobilnisite/slovnik/pcrf/) (Policy and Charging Rules Function) zajišťuje vytvoření vyhrazených přenašečů pro RTC mediální toky, aby byla zaručena nízká latence a ztrátovost paketů, což je proces definovaný na rozhraních Rx a Gx. Mediální vyjednávání používá protokol [SDP](/mobilnisite/slovnik/sdp/) (Session Description Protocol) uvnitř zpráv SIP k dohodě na kodecích (jako [AMR-WB](/mobilnisite/slovnik/amr-wb/) pro hlas nebo H.264 pro video), číslech portů a IP adresách. RTC služby dále zahrnují mechanismy pro tísňová volání (eMPS), zákonné odposlechy a v případě potřeby transkódování. Vývoj směrem k integraci WebRTC v pozdějších vydáních rozšířil RTC na aplikace založené na prohlížečích, což vyžadovalo nové funkční prvky, jako je WIF (WebRTC Interworking Function), pro propojení signalizačních a mediálních protokolů WebRTC s nativními postupy IMS.

## K čemu slouží

RTC bylo standardizováno za účelem přechodu od tradiční přepojování okruhů (jako hlas v GSM) k jednotné, plně IP síťové architektuře, která umožňuje bohatší multimediální služby. Před RTC přes IMS byly hlasové a video služby izolované, přičemž hlas přes přepojování okruhů postrádal integraci s datovými aplikacemi a internetovými protokoly. Motivací bylo využít IP sítě pro provozní efektivitu, inovace služeb a konvergenci sítí. Definováním RTC v rámci architektury IMS vyřešilo 3GPP problém poskytování hlasových a video služeb úrovně operátora se zaručenou kvalitou, zabezpečením a interoperabilitou napříč různými operátory a typy zařízení. Řešilo omezení best-effort internetového VoIP, kterému chyběla standardizovaná QoS, podpora tísňového volání a bezproblémový přenos při pohybu. Vytvoření standardů RTC umožnilo komerční nasazení VoLTE (Voice over LTE) a VoNR (Voice over NR), které jsou zásadní pro vyřazení starších jader s přepojováním okruhů a efektivnější využití spektra v sítích 4G a 5G.

## Klíčové vlastnosti

- Kompletní přenos médií založený na IP pomocí RTP/RTCP
- Řízení hovoru a signalizace prostřednictvím SIP v jádru IMS
- Integrované mechanismy QoS využívající vyhrazené přenašeče EPS
- Podpora širokopásmového (HD) hlasu (např. kodek EVS) a video kodeků
- Interworking se staršími sítěmi s přepojováním okruhů přes MGCF/IM-MGW
- Podpora tísňových služeb (eMPS) a zákonného odposlechu

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.565** (Rel-19) — Split Rendering Media Service Enabler
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.813** (Rel-19) — Avatar Representation and Communication
- **TS 26.822** (Rel-19) — 5G RTP Configurations Study Phase 2
- **TS 26.847** (Rel-19) — AI/ML Evaluation in 5G Media Services
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR
- **TS 45.820** (Rel-13) — CIoT for Internet of Things

---

📖 **Anglický originál a plná specifikace:** [RTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtc/)
