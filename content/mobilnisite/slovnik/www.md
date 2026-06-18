---
slug: "www"
url: "/mobilnisite/slovnik/www/"
type: "slovnik"
title: "WWW – World Wide Web"
date: 2025-01-01
abbr: "WWW"
fullName: "World Wide Web"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/www/"
summary: "World Wide Web (WWW) je globální informační systém přístupný prostřednictvím internetu, který umožňuje získávání a zobrazování hypertextových dokumentů. Ve standardech 3GPP představuje primární servis"
---

WWW (World Wide Web) je globální informační systém přístupný prostřednictvím internetu, který ve standardech 3GPP představuje primární servisní model, který určuje požadavky na IP konektivitu, QoS (kvalitu služby) a účtování v mobilních sítích.

## Popis

V rámci architektonického rámce 3GPP není World Wide Web síťovou komponentou, ale dominantní službou aplikační vrstvy, která zásadně utváří návrh a schopnosti mobilního paketového jádra. Je modelována jako klíčová služba v IP Multimedia Subsystem (IMS) a paketově spínané ([PS](/mobilnisite/slovnik/ps/)) doméně, která vyžaduje, aby síť poskytovala spolehlivou IP konektivitu, správu relací a řízení politik. Specifikace 3GPP definují servisní požadavky pro přístup k WWW, včetně nezbytných parametrů QoS (kvality služby) pro interaktivní a background třídy provozu, bezpečnostních mechanismů pro integritu dat a modelů účtování za využití dat.

Fungování služeb WWW závisí na základních schopnostech Evolved Packet Core (EPC) nebo 5G Core (5GC). Klíčové síťové funkce, jako je Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), poskytují kotvící bod pro IP konektivitu k veřejnému internetu, kde se nacházejí webové servery. Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) vynucují politiky, které mohou upřednostňovat nebo tvarovat webový provoz. Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5GC spravuje [PDU](/mobilnisite/slovnik/pdu/) (Protocol Data Unit) relace, které přenášejí [HTTP](/mobilnisite/slovnik/http/)/HTTPS provoz.

Z protokolového hlediska používá WWW provoz primárně HTTP a jeho zabezpečenou variantu HTTPS, které fungují nad TCP/IP. Úlohou mobilní sítě je efektivně přenášet tyto IP pakety mezi uživatelským zařízením (UE) a internetem. To zahrnuje plánování rádiových zdrojů v RAN, tunelování přes jádro sítě pomocí protokolů jako GTP-U a aplikaci šablon toků provozu pro filtrování. Výkon služeb WWW je kritickým metrikem pro uživatelský zážitek, na který přímo působí latence sítě, propustnost a spolehlivost, jak je specifikováno v servisních požadavcích 3GPP.

## K čemu slouží

Zařazení WWW do standardů 3GPP od Release 99 bylo hnací silou explozivního růstu služeb založených na internetu a potřeby integrovat mobilní telekomunikace s globálním internetem. Před 3G byly mobilní sítě primárně okruhově spínané, optimalizované pro hlas a nízkorychlostní data, což bylo nevhodné pro trhanou, asymetrickou povahu webového prohlížení. Standardizace servisních požadavků pro WWW zajistila, že sítě 3GPP mohly nativně podporovat IP-based aplikace, čímž se mobilní zařízení stala skutečnými internetovými koncovými body.

Toto formální uznání motivovalo vývoj klíčových architektonických prvků paketově spínané domény, jako je GPRS jádro sítě a později EPS. Vytvořilo konkrétní technické požadavky na trvalou konektivitu (always-on), dynamické přidělování IP adres a efektivní zpracování četných současných, krátce žijících TCP spojení typických pro webové stránky. Definováním WWW jako služby zajistilo 3GPP, že síťové plánování, QoS rámce a systémy účtování byly navrženy tak, aby vyhovovaly jejím charakteristikám provozu, které dodnes tvoří dominantní část mobilních dat.

## Klíčové vlastnosti

- Definuje servisní požadavky pro přístup k hypertextovým dokumentům přes IP
- Určuje potřebu podpory interaktivní a background třídy QoS
- Ovlivňuje návrh řízení politik pro diferenciaci datových služeb
- Vyžaduje podporu standardních internetových protokolů (HTTP, HTTPS, TCP/IP)
- Tvoří základ pro předpoklady modelů provozu při dimenzování sítě
- Integruje se s IMS pro obohacené webové komunikační služby

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [HTTP – Hypertext Transfer Protocol](/mobilnisite/slovnik/http/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 22.960** (Rel-4) — UMTS Mobile Multimedia Technical Challenges
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)

---

📖 **Anglický originál a plná specifikace:** [WWW na 3GPP Explorer](https://3gpp-explorer.com/glossary/www/)
