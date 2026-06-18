---
slug: "mmtel"
url: "/mobilnisite/slovnik/mmtel/"
type: "slovnik"
title: "MMTEL – Multimedia Telephony Service for IMS"
date: 2026-01-01
abbr: "MMTEL"
fullName: "Multimedia Telephony Service for IMS"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmtel/"
summary: "MMTEL je standardizovaná telefonní služba přes IMS, která umožňuje hlasovou, video a textovou komunikaci v reálném čase. Poskytuje bohatou IP alternativu k tradiční okruhově přepínané telefonii a podp"
---

MMTEL je standardizovaná služba multimediální telefonie 3GPP přes IMS, která umožňuje hlasovou, video a komunikaci v reálném čase pomocí textu jako IP alternativu k tradiční okruhově přepínané telefonii.

## Popis

Multimedia Telephony Service for IMS (MMTEL) je služba definovaná 3GPP, která poskytuje telefonní a multimediální komunikační schopnosti přes sítě IP Multimedia Subsystem (IMS). Standardizuje sadu komunikačních služeb včetně hlasu, videa a textu v reálném čase, což umožňuje operátorům nabízet bohaté, interoperabilní služby napříč různými sítěmi a zařízeními. MMTEL funguje v rámci architektury IMS a využívá základní prvky IMS, jako je Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)), Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a Application Servers ([AS](/mobilnisite/slovnik/as/)), ke správě relací a servisní logiky. Služba používá pro signalizaci [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) k navázání, změně a ukončení multimediálních relací a [RTP](/mobilnisite/slovnik/rtp/)/[RTCP](/mobilnisite/slovnik/rtcp/) (Real-time Transport Protocol/Control Protocol) pro přenos médií. Mezi klíčové komponenty patří MMTEL Application Servers, které hostují servisní logiku pro funkce jako přesměrování hovorů, blokování a doplňkové služby, a Service Centralization and Continuity Application Server ([SCC](/mobilnisite/slovnik/scc/) AS) pro zajištění mobility a kontinuity služeb mezi okruhově přepínanou a paketově přepínanou doménou. MMTEL definuje komplexní sadu doplňkových služeb, jako je Communication Diversion (např. přesměrování hovoru), Communication Barring (např. blokování hovoru), Originating Identification Presentation/Restriction, Terminating Identification Presentation/Restriction a služby jako Call Hold, Call Waiting a Multi-Party Conferencing. Podporuje také text v reálném čase ([RTT](/mobilnisite/slovnik/rtt/)) pro zpřístupnění a tísňové služby. Služba zajišťuje kvalitu služeb (QoS) prostřednictvím mechanismů řízení politik v IMS a interaguje s Policy and Charging Rules Function (PCRF) pro přidělování síťových zdrojů. MMTEL je nedílnou součástí Voice over LTE (VoLTE) a Voice over NR (VoNR) a poskytuje servisní vrstvu, která umožňuje hlasové a video hovory ve vysokém rozlišení přes sítě 4G a 5G. Usnadňuje interoperabilitu mezi sítěmi různých operátorů prostřednictvím standardizovaných procedur a profilů, čímž zajišťuje konzistentní uživatelský zážitek. MMTEL navíc podporuje tísňové hovory (např. přes IMS) a integraci s dalšími službami založenými na IMS, jako je Rich Communication Services (RCS).

## K čemu slouží

MMTEL byl vytvořen k řešení přechodu od tradiční okruhově přepínané telefonie k plně IP sítím, což umožňuje operátorům nabízet pokročilé multimediální komunikační služby přes IMS. Před MMTEL byly telefonní služby z velké části založeny na okruhově přepínané technologii, která omezovala funkce na základní hlas a byla neefektivní pro integraci dat. S příchodem LTE a později 5G, které jsou pouze paketově přepínané, vznikla kritická potřeba standardizované telefonní služby založené na IP, aby byla zajištěna kontinuita a bohatost hlasových služeb. MMTEL tento problém řeší poskytnutím komplexního rámce pro multimediální telefonii, včetně hlasu, videa a textu, přes IMS, a zajišťuje tak interoperabilitu napříč sítěmi a zařízeními. Historicky existovala proprietární VoIP řešení, ale postrádala standardizaci, což vedlo k fragmentaci a špatné uživatelské zkušenosti. MMTEL standardizoval servisní vrstvu, což umožnilo operátorům nasazovat konzistentní služby globálně. Řeší také potřebu doplňkových služeb (např. přesměrování hovorů, konferenční hovory) v IP kontextu, které byly v okruhově přepínaných sítích dobře zavedené, ale pro IMS bylo nutné je znovu definovat. MMTEL navíc podporuje regulatorní požadavky, jako jsou tísňové hovory a zákonné odposlechy, což jej činí vhodným pro komerční nasazení. Jeho vytvoření bylo motivováno přechodem odvětví na plně IP sítě, poháněným efektivitou a flexibilitou paketově přepínané technologie, a snahou umožnit bohaté komunikační zážitky přesahující tradiční hlas.

## Klíčové vlastnosti

- Standardizovaná hlasová, video a textová komunikace v reálném čase přes IMS
- Komplexní doplňkové služby včetně přesměrování hovorů, blokování, hold, čekání a konferenčních hovorů
- Interoperabilita mezi různými operátory a zařízeními prostřednictvím specifikací 3GPP
- Podpora kontinuity služeb mezi okruhově přepínanou a paketově přepínanou doménou (např. SRVCC)
- Integrace s řízením politik v IMS pro správu kvality služeb (QoS)
- Podpora tísňových hovorů a funkce zpřístupnění jako text v reálném čase (RTT)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [RCS – Return Channel via Satellite](/mobilnisite/slovnik/rcs/)

## Definující specifikace

- **TS 22.153** (Rel-20) — Multimedia Priority Service (MPS) requirements
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.806** (Rel-13) — Application Specific Congestion Control for Data
- **TR 22.854** (Rel-17) — Feasibility Study on Multimedia Priority Service - Phase 2
- **TR 22.953** (Rel-19) — Multimedia Priority Service Feasibility Study
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.239** (Rel-19) — Flexible Alerting Protocol for IMS
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.827** (Rel-16) — Policy and Charging for Volume Based Charging
- **TS 29.866** (Rel-19) — IMS Disaster Prevention & Restoration Enhancement
- **TR 29.935** (Rel-19) — HSS Reference Data Model for Ud Interface
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [MMTEL na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmtel/)
