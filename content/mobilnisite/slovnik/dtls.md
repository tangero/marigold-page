---
slug: "dtls"
url: "/mobilnisite/slovnik/dtls/"
type: "slovnik"
title: "DTLS – Datagram Transport Layer Security"
date: 2026-01-01
abbr: "DTLS"
fullName: "Datagram Transport Layer Security"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dtls/"
summary: "Bezpečnostní protokol zajišťující soukromí komunikace pro datagramové protokoly. V 3GPP se používá k zabezpečení nespolehlivé přenosové vrstvy citlivé na zpoždění, jako je UDP, což je klíčové pro služ"
---

DTLS je bezpečnostní protokol, který zajišťuje soukromí komunikace pro datagramové protokoly jako UDP a zabezpečuje služby citlivé na zpoždění, například VoLTE a IoT data, v sítích 3GPP.

## Popis

Datagram Transport Layer Security (DTLS) je komunikační protokol navržený pro zabezpečení aplikací založených na datagramech. Je odvozen od protokolu Transport Layer Security ([TLS](/mobilnisite/slovnik/tls/)), ale je přizpůsoben pro datagramový přenosový model, primárně User Datagram Protocol ([UDP](/mobilnisite/slovnik/udp/)), který negarantuje doručení ani pořadí paketů. DTLS poskytuje stejné bezpečnostní záruky jako TLS – důvěrnost, integritu a autentizaci – a zároveň zohledňuje inherentní nespolehlivost podkladového přenosu. Protokol toho dosahuje přidáním sériových čísel a časovače pro opakovaný přenos handshake zpráv, což zajišťuje dokončení kryptografického handshake i v případě ztráty nebo přeuspořádání paketů, aniž by zaváděl jakoukoli spolehlivost pro samotná aplikační data.

V rámci architektury 3GPP je DTLS specifikován jako klíčový protokol pro zabezpečení různých rozhraní a služeb. Je základní součástí pro zabezpečení mediální cesty založené na WebRTC v IP Multimedia Subsystem (IMS), jak je definováno v TS 23.228 a souvisejících specifikacích. DTLS funguje na aplikační vrstvě, typicky nad UDP/IP. Handshake protokolu zahrnuje výměnu certifikátů nebo předem sdílených klíčů pro vzájemnou autentizaci klienta a serveru a pro vytvoření sdílených tajných klíčů. Tyto klíče se pak používají se symetrickou kryptografií (např. [AES](/mobilnisite/slovnik/aes/)) k šifrování aplikačních dat a s kódy pro ověření zpráv (např. HMAC-SHA256) k zajištění integrity.

Role DTLS v síti 3GPP je mnohostranná. Pro hlasové a video služby založené na IMS (např. VoLTE, ViLTE) používá [DTLS-SRTP](/mobilnisite/slovnik/dtls-srtp/) protokol DTLS k provedení výměny klíčů pro mediální toky Secure Real-time Transport Protocol ([SRTP](/mobilnisite/slovnik/srtp/)). Ve scénářích Machine Type Communication ([MTC](/mobilnisite/slovnik/mtc/)) a IoT, jak je nastíněno ve specifikacích jako TS 23.682 a TS 33.187, může DTLS zabezpečit zprávy CoAP (Constrained Application Protocol) mezi zařízeními a síťovými servery, čímž poskytuje odlehčené bezpečnostní řešení vhodné pro zařízení s omezenými zdroji. Dále se DTLS používá v řídicí rovině, například na rozhraní S14 pro správu zařízení nebo v architektuře pro služby založené na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)). Jeho schopnost fungovat nad UDP jej činí ideálním pro aplikace v reálném čase s nízkou latencí, kde by navázání spojení a řízení zahlcení u TCP zavedlo nepřijatelné zpoždění.

## K čemu slouží

DTLS byl vytvořen, aby rozšířil ověřený bezpečnostní model [TLS](/mobilnisite/slovnik/tls/) na datagramové protokoly, primárně UDP. TLS vyžaduje spolehlivý proud bajtů v pořadí, který poskytuje TCP, ale mnoho moderních aplikací – zejména komunikace v reálném čase, hry a IoT – používá UDP kvůli nižší latenci a absenci blokování hlavy fronty. Hlavní problém, který DTLS řeší, je poskytnutí silné autentizace, šifrování a integrity dat pro tyto aplikace založené na UDP bez nutnosti modifikovat podkladový nespolehlivý přenos.

Historicky aplikace používající UDP buď rezignovaly na zabezpečení, implementovaly vlastní (a často zranitelné) bezpečnostní mechanismy, nebo byly nuceny používat TCP, což ohrožovalo výkon. Vývoj DTLS, standardizovaný IETF v RFC 4347 a aktualizovaný v RFC 6347, zaplnil tuto kritickou mezeru. 3GPP přijalo DTLS počínaje Release 12, aby splnilo bezpečnostní požadavky nových servisních architektur. Motivací byl vzestup WebRTC, který vyžaduje DTLS pro šifrování médií, a potřeba odlehčeného zabezpečení v komunikacích IoT/M2M, kde je režie TCP nepřijatelná. DTLS umožňuje sítím 3GPP nabízet zabezpečené služby s nízkou latencí end-to-end, což je v souladu s průmyslovým posunem k plně IP sítím a šifrovaným médiím.

## Klíčové vlastnosti

- Handshake přes nespolehlivý přenos za použití časovačů pro opakovaný přenos a sériových čísel
- Poskytuje důvěrnost prostřednictvím šifrování (např. AES-GCM, AES-CCM)
- Zajišťuje integritu zpráv a autentizaci pomocí HMAC nebo AEAD šifer
- Podporuje vzájemnou autentizaci pomocí certifikátů, předem sdílených klíčů nebo surových veřejných klíčů
- Odolnost vůči replay útokům díky použití sériových čísel a okénkování
- Definované profily pro použití se SRTP (DTLS-SRTP) a CoAP (DTLS-CoAP)

## Související pojmy

- [TLS – Transport Layer Security](/mobilnisite/slovnik/tls/)
- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)
- [UDP – User Datagram Protocol](/mobilnisite/slovnik/udp/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 24.103** (Rel-19) — Telepresence Protocol for IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.803** (Rel-12) — Telepresence using IMS - Study
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 29.176** (Rel-19) — Nmf Service Based Interface for Media Function
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [DTLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtls/)
