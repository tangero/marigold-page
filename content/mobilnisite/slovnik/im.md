---
slug: "im"
url: "/mobilnisite/slovnik/im/"
type: "slovnik"
title: "IM – IP Multimedia Core Network Subsystem"
date: 2026-01-01
abbr: "IM"
fullName: "IP Multimedia Core Network Subsystem"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/im/"
summary: "IP Multimedia Core Network Subsystem (IMS) je standardizovaný architektonický rámec pro poskytování IP multimediálních služeb přes mobilní a pevné sítě. Umožňuje hlasové, video, zasílání zpráv a další"
---

IM je standardizovaný architektonický rámec pro poskytování IP multimediálních služeb, jako je hlas a video, přes mobilní a pevné sítě s využitím signalizace založené na SIP.

## Popis

IP Multimedia Core Network Subsystem (IMS) je komplexní, standardizovaná architektura definovaná konsorciem 3GPP pro usnadnění poskytování IP multimediálních služeb. Funguje jako nadstavba nad paketovou doménou, nezávisle na podkladové přístupové technologii, ať už jde o LTE, 5G NR, Wi-Fi nebo pevný širokopásmový přístup. IMS používá protokol Session Initiation Protocol (SIP) jako svůj primární signalizační protokol pro navazování, úpravu a ukončování multimediálních relací. Tento přístup založený na SIP umožňuje flexibilní tvorbu služeb a integraci s internetovými protokoly.

Z architektonického hlediska se IMS skládá z několika klíčových funkčních prvků. Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) funguje jako SIP proxy, zajišťující registraci, směrování relací a vynucování politik. Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) je centrální databáze ukládající uživatelské profily a autentizační data. Mediální funkce spravuje Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) pro zpracování mediálních toků, jako je konferenční hovor nebo transkódování. Application Server ([AS](/mobilnisite/slovnik/as/)) hostuje a provádí nadstavbové služby, jako jsou telefonní aplikační servery pro VoLTE nebo servery pro zasílání zpráv pro RCS. Tyto komponenty vzájemně komunikují prostřednictvím standardizovaných rozhraní, jako je rozhraní Cx mezi CSCF a HSS, což zajišťuje interoperabilitu mezi implementacemi různých dodavatelů.

IMS funguje tak, že zpracovává signalizační zprávy SIP pro správu uživatelské autentizace, autorizace služeb a směrování relací. Když uživatel zahájí multimediální hovor, je požadavek směrován přes [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-CSCF) k S-CSCF (Serving-CSCF), který komunikuje s HSS pro autentizaci a načítá servisní profily z AS. Vyjednávání o médiích je řešeno pomocí SIP a protokolu Session Description Protocol (SDP), přičemž mediální cesty jsou navázány přímo mezi koncovými body nebo přes mediální brány pro propojení se staršími sítěmi. IMS podporuje kvalitu služeb (QoS) prostřednictvím řízení politik přes Policy and Charging Rules Function (PCRF), což zajišťuje odpovídající přidělování prostředků. Jeho role je klíčová v moderních sítích, neboť umožňuje bezproblémové multimediální služby napříč různými přístupovými technologiemi a podporuje konvergenci mezi tradičními telekomunikačními a internetovými aplikacemi.

## K čemu slouží

IMS byl vytvořen, aby řešil omezení sítí s přepojováním okruhů při podpoře pokročilých multimediálních služeb a aby umožnil konvergenci mezi telekomunikačními a internetovými protokoly. Před IMS mobilní sítě primárně nabízely hlas a SMS přes domény s přepojováním okruhů, což bylo neefektivní pro datově náročná multimédia a postrádalo flexibilitu pro inovace služeb. Vzestup IP aplikací zdůraznil potřebu standardizovaného rámce, který by mohl poskytovat integrovaný hlas, video a zasílání zpráv přes paketové sítě.

Vývoj IMS začal ve verzi 3GPP Release 5, navazující na dřívější koncepty IP multimédií z Release 99. Jeho účelem je poskytnout škálovatelnou, bezpečnou a na přístupu nezávislou platformu pro multimediální služby, řešící problémy jako fragmentace služeb, interoperabilita a zajištění kvality. IMS umožňuje operátorům nabízet pokročilé služby jako VoLTE, VoWiFi a RCS, a zároveň podporovat regulatorní požadavky, jako je tísňové volání nebo zákonný odposlech. Oddělením služeb od přístupových sítí IMS usnadňuje vývoj sítí směrem k plně IP infrastrukturám a podporuje konvergenci napříč mobilními, pevnými a internetovými doménami, čímž pohání inovace v komunikačních službách.

## Klíčové vlastnosti

- Standardizovaná architektura pro poskytování IP multimediálních služeb s využitím signalizace SIP
- Nezávislý design na přístupové technologii podporující LTE, 5G, Wi-Fi a pevný širokopásmový přístup
- Centralizovaná uživatelská autentizace a správa profilů prostřednictvím HSS
- Flexibilní tvorba a nasazení služeb prostřednictvím aplikačních serverů (Application Servers)
- Integrované řízení politik pro QoS a účtování prostřednictvím PCRF
- Umožňuje konvergenci telekomunikačních a internetových služeb (např. VoLTE, RCS)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 22.127** (Rel-9) — Open Service Access (OSA) Requirements
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.801** (Rel-12) — Study on Non-MTC Mobile Data Application Impacts
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.204** (Rel-19) — SMS over generic IP access; Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.815** (Rel-5) — IMS Charging Implications
- … a dalších 71 specifikací

---

📖 **Anglický originál a plná specifikace:** [IM na 3GPP Explorer](https://3gpp-explorer.com/glossary/im/)
