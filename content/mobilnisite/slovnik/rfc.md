---
slug: "rfc"
url: "/mobilnisite/slovnik/rfc/"
type: "slovnik"
title: "RFC – Request For Comments"
date: 2025-01-01
abbr: "RFC"
fullName: "Request For Comments"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rfc/"
summary: "Řada dokumentů publikovaných Internet Engineering Task Force (IETF), která zahrnuje navrhované standardy, osvědčené postupy a informační memoranda. RFC tvoří základní technickou a organizační dokument"
---

RFC je řada dokumentů IETF obsahujících navrhované standardy a osvědčené postupy, které tvoří základní technickou dokumentaci pro internetové protokoly, jako jsou SIP a HTTP, používané v systémech 3GPP.

## Popis

Request For Comments (RFC) je formální řada dokumentů vytvářených a publikovaných Internet Engineering Task Force ([IETF](/mobilnisite/slovnik/ietf/)). V ekosystému 3GPP jsou RFC zásadně důležité, protože mnoho základních protokolů a architektonických principů používaných v mobilních sítích je odvozeno nebo specifikováno standardy IETF. RFC může představovat několik fází standardizace: Internet Standard, Proposed Standard, Best Current Practice ([BCP](/mobilnisite/slovnik/bcp/)), Informational nebo Experimental. Proces začíná Internet-Draftem, který po posouzení a dosažení konsenzu v příslušné pracovní skupině IETF může být publikován jako RFC. Po publikaci je RFC přiděleno pořadové číslo a zůstává neměnné; revize jsou vydávány jako nová RFC, což může zastarat předchozí verze.

Obsah RFC může zahrnovat detailní specifikace protokolů (např. RFC 3261 pro [SIP](/mobilnisite/slovnik/sip/), RFC 6733 pro Diameter), architektonické přehledy, dokumenty politik a historické poznámky. Specifikace protokolů definují formáty zpráv, stavové automaty, zpracování chyb a bezpečnostní aspekty. Pro 3GPP jsou tyto protokoly často začleněny odkazem. Například IP Multimedia Subsystem (IMS) zásadně závisí na SIP (RFC 3261) pro řízení relací, Diameter (RFC 6733) pro ověřování a autorizaci a [RTP](/mobilnisite/slovnik/rtp/) (RFC 3550) pro přenos médií. Specifikace 3GPP definují, jak jsou tyto obecné internetové protokoly profilovány, rozšiřovány nebo omezeny pro použití v mobilním prostředí, například přidáním specifických hlavičkových polí nebo definováním nových Diameter aplikací.

Z architektonické perspektivy použití RFC IETF umožňuje 3GPP využívat dobře odladěné, otevřené standardy, což podporuje interoperabilitu mezi mobilními sítěmi a širším internetem. Umožňuje to jasné oddělení mezi vrstvami specifickými pro rádiové rozhraní (definovanými 3GPP) a jádrovými služebními vrstvami používajícími IP technologii. Inženýři pracující na prvcích jádrové sítě 3GPP musí mít hluboké znalosti příslušných RFC, aby správně implementovali uzly jako [P-CSCF](/mobilnisite/slovnik/p-cscf/), [HSS](/mobilnisite/slovnik/hss/) nebo [PCRF](/mobilnisite/slovnik/pcrf/). Proces publikace RFC, s důrazem na otevřené posuzování a hrubý konsenzus, přispívá k robustnosti a bezpečnosti protokolů, na kterých závisí moderní telekomunikace.

## K čemu slouží

Proces RFC byl vytvořen k usnadnění otevřeného vývoje a dokumentace protokolů a postupů, které umožňují fungování internetu. Jeho účelem je poskytovat stabilní, referencovatelný záznam technických specifikací a nápadů. Pro 3GPP přijetí RFC [IETF](/mobilnisite/slovnik/ietf/) řeší několik klíčových problémů. Za prvé se tak zabrání opětovnému vynalézání kola; namísto vytváření proprietárních protokolů pro služby založené na IP může 3GPP integrovat zralé, široce implementované standardy. To urychluje vývoj a zajišťuje globální interoperabilitu. Za druhé to sladí mobilní sítě s internetovým paradigmatem, což byl základní designový cíl pro 3G a následující generace, přecházející od okruhově přepínané telefonie k plně IP jádru.

Historicky rané standardy pro buňkové sítě (jako GSM) používaly telekomunikační signalizační protokoly (např. MAP, CAP). Přechod na 3G (UMTS) a zejména na 4G (LTE) zahrnoval vědomé rozhodnutí založit jádrovou síť na IP. To vyžadovalo protokoly pro správu relací, mobilitu a zabezpečení, které byly škálovatelné a široce známé. Práce IETF na SIP, Diameter a IPsec poskytla hotová řešení. Mechanismus RFC, se svým důkladným odborným posuzováním, poskytl potřebnou technickou hloubku a stabilitu pro rozsáhlé komerční nasazení.

Dále řada RFC zahrnuje dokumenty Best Current Practice, které vedou provozní a bezpečnostní postupy, což je klíčové pro provoz spolehlivých sítí. Odkazováním na RFC mohou specifikace 3GPP zůstat zaměřené na rádiový přístup a mobilní adaptace, zatímco detailní mechaniku IP protokolů delegují na IETF. Toto oddělení zájmů je klíčovým faktorem úspěchu a flexibility architektur moderních mobilních sítí.

## Klíčové vlastnosti

- Formální, pořadově číslované dokumenty publikované IETF
- Zahrnuje Internet Standards, Proposed Standards, Best Current Practices a Informational memoranda
- Specifikuje základní internetové protokoly (např. IP, TCP, UDP, SIP, Diameter, HTTP) používané 3GPP
- Dokumenty jsou statické; aktualizace jsou vydávány jako nová RFC
- Vyvíjeny prostřednictvím otevřeného konsenzuálního procesu zahrnujícího pracovní skupiny
- Poskytuje základní technické specifikace pro služby založené na IP v mobilních sítích

## Související pojmy

- [IETF – Internet Engineering Task Force Standard](/mobilnisite/slovnik/ietf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [IP – IP Packet eXchange](/mobilnisite/slovnik/ip/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- … a dalších 35 specifikací

---

📖 **Anglický originál a plná specifikace:** [RFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfc/)
