---
slug: "sip"
url: "/mobilnisite/slovnik/sip/"
type: "slovnik"
title: "SIP – Session Initiation Protocol"
date: 2026-01-01
abbr: "SIP"
fullName: "Session Initiation Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sip/"
summary: "SIP je signalizační protokol aplikační vrstvy definovaný IETF, který se používá k vytváření, modifikaci a ukončování multimediálních relací, jako jsou hlasová a videohovorová spojení přes IP sítě. V 3"
---

SIP je signalizační protokol aplikační vrstvy definovaný IETF, který se používá k vytváření, modifikaci a ukončování multimediálních relací a je základním protokolem pro služby IMS v sítích 3GPP.

## Popis

Session Initiation Protocol (SIP) je textový řídicí protokol aplikační vrstvy standardizovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 3261 a další). Jeho primární funkcí je navazování, správa a ukončování interaktivních komunikačních relací mezi účastníky. Tyto relace mohou zahrnovat hlas, video, instant messaging, online hry a virtuální realitu – v podstatě jakoukoli výměnu dat v reálném čase. SIP funguje na modelu klient-server, ale ve správě relací je inherentně peer-to-peer. Je nezávislý na podkladové transportní vrstvě a typicky běží přes [UDP](/mobilnisite/slovnik/udp/), TCP nebo [TLS](/mobilnisite/slovnik/tls/).

SIP funguje prostřednictvím výměny požadavků a odpovědí mezi uživatelskými agenty ([UA](/mobilnisite/slovnik/ua/)), kteří mohou být klienti ([UAC](/mobilnisite/slovnik/uac/)) iniciující požadavky, nebo servery ([UAS](/mobilnisite/slovnik/uas/)) na ně odpovídající. Typická SIP transakce pro zřízení hlasového hovoru zahrnuje několik klíčových zpráv: volající UA odešle požadavek INVITE na adresu volaného (SIP [URI](/mobilnisite/slovnik/uri/)). Tento požadavek je směrován přes SIP proxy servery, které pomáhají lokalizovat volaného a vynucují směrovací politiky. UA volaného odpoví provizorními odpověďmi (např. 180 Ringing) a konečnou úspěšnou odpovědí (200 OK), která obsahuje parametry popisu relace typicky formátované pomocí Session Description Protocol (SDP). Volající potvrdí zprávou ACK a mediální relace (používající RTP/RTCP) je zřízena přímo mezi koncovými body. Pro ukončení relace je odeslán požadavek BYE.

V rámci architektury 3GPP je SIP klíčovým signalizačním protokolem IP Multimedia Subsystem (IMS). IMS poskytuje standardizovaný rámec pro poskytování multimediálních služeb přes IP. Mezi klíčové síťové prvky 3GPP, které fungují jako SIP servery, patří Proxy-Call Session Control Function (P-CSCF), což je první kontaktní bod pro UE; Serving-CSCF (S-CSCF), který provádí řízení relací a komunikuje s aplikačními servery; a Interrogating-CSCF (I-CSCF), který zprostředkovává rozhraní s jinými sítěmi. SIP v IMS se používá pro registraci, autentizaci (často s využitím IMS Authentication and Key Agreement (AKA)) a řízení relací pro služby jako Voice over LTE (VoLTE), Voice over NR (VoNR), Rich Communication Services (RCS) a videotelefonie. Protokol je rozšířen o specifické hlavičky a parametry 3GPP pro podporu požadavků mobilních sítí, jako je nouzové volání, informace o přístupové síti a integrace řízení politik.

## K čemu slouží

SIP byl vytvořen k řešení problému navazování a správy multimediálních relací v rozvíjejícím se internetovém prostředí. Před SIP byly běžné proprietární signalizační protokoly, které bránily interoperabilitě mezi zařízeními různých výrobců a poskytovatelů služeb. Růst IP sítí vytvořil potřebu standardizovaného, flexibilního a rozšiřitelného signalizačního protokolu, který by mohl podporovat rostoucí škálu aplikací v reálném čase přesahujících jednoduchý hlas. SIP byl navržen jako jednoduchý, modulární a textový (jako HTTP), což usnadňuje jeho implementaci, ladění a rozšiřování ve srovnání s binárními protokoly jako H.323.

3GPP přijalo SIP jako signalizační protokol pro IMS, aby umožnilo konvergenci mobilní telefonie s internetovými multimediálními službami. Tím bylo řešeno kritické strategické zadání: vyvinout služby přepojování okruhů pro hlas k efektivnější, funkčně bohatší, plně IP architektuře. SIP umožnil mobilním operátorům nabízet standardizované, interoperabilní hlasové a videohovorové služby přes jejich LTE a 5G datové sítě (VoLTE/VoNR), což zajišťuje kontinuitu a kvalitu služeb. Poskytl také základ pro nové služby generující příjmy, jako je RCS (obchodované jako Chat), a bezproblémovou integraci s aplikacemi typu over-the-top (OTT). Využitím standardu IETF zajistilo 3GPP, že služby založené na IMS mohou interoperovat s pevnými VoIP sítěmi a širším internetem, což usnadňuje konvergenci pevných a mobilních sítí a podporuje bohatý ekosystém vývojářů aplikací a poskytovatelů služeb.

## Klíčové vlastnosti

- Textový signalizační protokol aplikační vrstvy pro zahajování, modifikaci a ukončování relací
- Používá model transakcí požadavek/odpověď podobný HTTP
- Nezávislý na transportu, funguje přes UDP, TCP nebo TLS
- Používá SIP URI (např. sip:user@domain.com) pro adresování
- Spolupracuje se SDP při vyjednávání parametrů mediální relace
- Základní protokol v architektuře 3GPP IMS pro služby jako VoLTE a RCS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [URI – Universal Resource Identifier](/mobilnisite/slovnik/uri/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TR 22.940** (Rel-19) — IMS Messaging Requirements Analysis
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TR 22.953** (Rel-19) — Multimedia Priority Service Feasibility Study
- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- … a dalších 124 specifikací

---

📖 **Anglický originál a plná specifikace:** [SIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sip/)
