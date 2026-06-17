---
slug: "ietf"
url: "/mobilnisite/slovnik/ietf/"
type: "slovnik"
title: "IETF – Internet Engineering Task Force Standard"
date: 2025-01-01
abbr: "IETF"
fullName: "Internet Engineering Task Force Standard"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ietf/"
summary: "Odkazuje na standardy vyvinuté IETF, otevřenou mezinárodní komunitou, která navrhuje a prosazuje dobrovolné standardy pro Internet. V rámci 3GPP jsou standardy IETF (jako SIP, Diameter, IPsec) přijímá"
---

IETF je otevřená mezinárodní komunita, která navrhuje dobrovolné standardy pro Internet. Tyto standardy 3GPP přijímá a profiluje pro použití v architekturách mobilních sítí za účelem umožnění propojování sítí.

## Popis

Internet Engineering Task Force (IETF) je rozsáhlá, otevřená mezinárodní komunita návrhářů sítí, operátorů, dodavatelů a výzkumníků zabývající se vývojem architektury Internetu a jeho bezproblémovým provozem. Vytváří kvalitní, relevantní technické dokumenty, které ovlivňují způsob, jakým lidé navrhují, používají a spravují Internet. Mezi tyto dokumenty patří Request for Comments (RFC), což jsou formální publikace standardů, specifikací, protokolů, postupů a osvědčených postupů pro Internet. IETF působí pod záštitou Internet Society (ISOC) a její práce je organizována do různých oblastí, z nichž každá má pracovní skupiny zaměřené na konkrétní technická témata.

V kontextu 3GPP nejsou standardy IETF vytvářeny 3GPP, ale jsou zásadním způsobem přijímány, odkazovány a profilovány pro integraci do architektur mobilních sítí. Toto přijetí je zásadní pro umožnění bezproblémové interoperability mobilních sítí s globálním Internetem a pro implementaci pokročilých služeb založených na IP. Mezi klíčové protokoly IETF specifikované ve standardech 3GPP patří Session Initiation Protocol (SIP) pro řízení multimediálních relací v IP Multimedia Subsystem (IMS), protokol Diameter pro autentizaci, autorizaci a účtování ([AAA](/mobilnisite/slovnik/aaa/)) a [IPsec](/mobilnisite/slovnik/ipsec/) pro zabezpečení komunikací na IP vrstvě. Specifikace 3GPP definují, jak jsou tyto obecné protokoly IETF konkrétně používány, rozšiřovány nebo omezovány v rámci mobilního prostředí, což zajišťuje konzistenci a interoperabilitu mezi zařízeními různých dodavatelů.

Role standardů IETF v rámci 3GPP se dramaticky rozšířila s přechodem na plně IP jádra sítí. Počínaje 3GPP Release 5 a zavedením IMS se závislost na protokolech IETF stala základním kamenem pro poskytování hlasových služeb přes IP (VoIP), videa a dalších multimediálních služeb. Architektura 3GPP v podstatě používá protokoly IETF jako stavební kameny pro svou servisní vrstvu. Například uzly [P-CSCF](/mobilnisite/slovnik/p-cscf/), [I-CSCF](/mobilnisite/slovnik/i-cscf/) a S-CSCF v IMS jsou SIP servery, které komunikují pomocí metod a hlaviček SIP definovaných IETF, často s rozšířeními specifickými pro 3GPP. Podobně 5G Core (5GC) používá [HTTP](/mobilnisite/slovnik/http/)/2 jako protokol pro rozhraní založené na službách, což je další standard vyvinutý v rámci IETF. Tento symbiotický vztah umožňuje sítím 3GPP využívat robustní, široce ověřené internetové standardy, zatímco své standardizační úsilí soustřeďuje na rádiový přístup a mobilní adaptace.

## K čemu slouží

Účelem odkazování na standardy IETF v rámci 3GPP je vyhnout se znovuvynalézání již dobře zavedených a globálně nasazených protokolů pro Internet. Tím, že 3GPP staví na práci IETF, zajišťuje, že její mobilní sítě jsou ze své podstaty kompatibilní s Internetem, který je primárním cílem většiny datového provozu. Tento přístup řeší kritický problém vzájemného propojování sítí a interoperability služeb mezi uzavřeným, okruhově přepínaným světem tradičních telekomunikací a otevřeným, paketově přepínaným Internetem. Historicky sítě před 3GPP a rané sítě 2G používaly proprietární signalizační protokoly nebo protokoly orientované na [ITU-T](/mobilnisite/slovnik/itu-t/). Přechod na plně IP architekturu si vyžádal přechod na signalizační a transportní protokoly založené na IP.

Motivací pro tuto integraci byl explozivní růst internetových služeb a vize konvergovaných sítí. Použití standardů IETF umožnilo 3GPP rychle vyvinout sofistikované schopnosti služeb založených na IP (jako je IMS) prostřednictvím využití protokolů, které již prošly rozsáhlým odborným posouzením a nasazením v reálném provozu. Tím byly odstraněny limity předchozích přístupů specifických pro telekomunikace, které byly často složité, neefektivní pro data a izolované od inovací na Internetu. Přijetí standardů IETF zajišťuje budoucí odolnost architektur 3GPP, protože jim umožňuje začleňovat nové internetové technologie, jak se objevují, jako je například přechod od Diameter ke službám založeným na [HTTP](/mobilnisite/slovnik/http/)/2 v 5G Core.

## Klíčové vlastnosti

- Přijetí základních internetových protokolů, jako jsou SIP, Diameter a IPsec
- Profilování a rozšíření standardů IETF pro mobilní specifické požadavky
- Umožňuje bezproblémové vzájemné propojení sítí 3GPP s globálním Internetem
- Základ pro IP Multimedia Subsystem (IMS) a plně IP jádra sítí
- Využití bezpečnostních protokolů IETF (např. TLS, IPsec) pro zabezpečenou komunikaci
- Použití směrovacích protokolů IETF a standardů pro správu mobility IP

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.141** (Rel-19) — Presence Service Requirements
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- … a dalších 52 specifikací

---

📖 **Anglický originál a plná specifikace:** [IETF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ietf/)
