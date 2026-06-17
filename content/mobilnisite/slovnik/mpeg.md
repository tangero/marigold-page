---
slug: "mpeg"
url: "/mobilnisite/slovnik/mpeg/"
type: "slovnik"
title: "MPEG – Moving Pictures Experts Group"
date: 2025-01-01
abbr: "MPEG"
fullName: "Moving Pictures Experts Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mpeg/"
summary: "Moving Pictures Experts Group (MPEG) je pracovní skupina ISO/IEC, která vyvíjí mezinárodní standardy pro kompresi, kódování a přenos digitálního audia a videa. V rámci 3GPP jsou standardy MPEG, jako j"
---

MPEG je Moving Pictures Experts Group, pracovní skupina ISO/IEC, která vyvíjí mezinárodní standardy pro digitální kompresi a kódování audio/video, které 3GPP odkazuje a profiluje pro multimediální služby v mobilních sítích.

## Popis

V ekosystému 3GPP se termín Moving Pictures Experts Group (MPEG) nevztahuje k samotné skupině, ale k souboru standardů pro multimediální kódování, které tato skupina ([ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) JTC 1/SC 29/WG 11) vyvinula a které jsou pro použití v mobilní telekomunikaci přijaty a profilovány. 3GPP nevyvíjí vlastní kodeky, místo toho začleňuje a specifikuje použití standardů MPEG v četných technických specifikacích (TS). Mezi klíčové odkazované standardy MPEG patří MPEG-4 pro kódování videa a audia (Part 2 Visual, Part 3 Audio a především Part 10 Advanced Video Coding - [AVC](/mobilnisite/slovnik/avc/)/H.264 a později Part 10 High Efficiency Video Coding - [HEVC](/mobilnisite/slovnik/hevc/)/H.265), [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Transport Stream pro vysílání a formát souboru MPEG-4 (ISO Base Media File Format) pro ukládání a streamování.

Integrace funguje tak, že 3GPP definuje specifické profily a úrovně těchto standardů MPEG, které jsou povinné nebo doporučené pro interoperabilitu. Například 3GPP vyžaduje kodek H.264/AVC pro základní videotelefonii a streamovací služby. Specifikace podrobně popisují, jak se tyto kodeky používají v různých službách: ve službě Packet-Switched Streaming Service (PSS - TS 26.234) se používá 3GPP formát souboru (odvozený od formátu [MP4](/mobilnisite/slovnik/mp4/)); ve službě Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/) - TS 26.346) je pro doručování specifikován MPEG-2 TS; a pro IMS Multimedia Telephony (MMTel) jsou definovány specifické formáty RTP přenosových jednotek pro MPEG-4 audio ([AAC](/mobilnisite/slovnik/aac/)) a video. Architektura zahrnuje umístění kodeku v médiové zpracovávací jednotce UE a v médiových branách nebo aplikačních serverech v síti.

Klíčové komponenty odkazované v desítkách specifikací 3GPP zahrnují informace o konfiguraci dekodéru, synchronizační vrstvy a přenosové protokoly. Role standardů MPEG v 3GPP je fundamentální: poskytují efektivní kompresi nezbytnou pro doručování videa a audia přijatelné kvality přes rádiové kanály s omezenou šířkou pásma a proměnnou přenosovou rychlostí. Umožňují široké spektrum služeb od jednoduchých vyzváněcích melodií po videokonference ve vysokém rozlišení a mobilní TV. Specifikace zajišťují, že jakékoli kompatibilní UE dokáže dekódovat médiové toky odeslané kompatibilním serverem, čímž garantuje globální interoperabilitu pro multimediální služby.

## K čemu slouží

Odkazování na standardy MPEG v rámci 3GPP, počínaje nejstaršími releasy (R99), bylo motivováno základní potřebou přidat do digitálních celulárních sítí multimediální schopnosti nad rámec hlasu. Před 3G byly mobilní sítě primárně okruhově spínané hlasové systémy. Nástup paketově spínaných dat v 2.5G a 3G vytvořil příležitost pro video a audio služby, ty však vyžadovaly vysoce efektivní kompresi, aby byly realizovatelné přes omezená a drahá datová připojení. Vývoj zcela nových proprietárních kodeků by byl neefektivní a fragmentoval by trh.

Účelem 3GPP při přijímání standardů MPEG bylo využít existující, robustní a mezinárodně uznávanou kompresní technologii. MPEG-4 zejména nabídl komplexní soubor nástrojů pro audiovizuální kódování, popis scény a formátování souborů, který byl ideální pro heterogenní prostředí doručování v mobilních sítích (streamování, stahování, vysílání). Tím byl vyřešen problém interoperability a urychleno nasazení multimediálních služeb. Profilováním standardů MPEG zajistilo 3GPP, že zařízení a sítě mají společný, optimalizovaný jazyk pro média, což bylo klíčové pro úspěch služeb jako videohovory, mobilní TV (MBMS) a později vysoce kvalitní streamování přes LTE a 5G. Představuje to klíčový příklad strategie 3GPP integrovat nejlepší externí standardy k vybudování kompletního systému.

## Klíčové vlastnosti

- Přijetí MPEG-4 AVC/H.264 a HEVC/H.265 jako povinných videokodeků pro různé služby
- Specifikace 3GPP formátu souboru založeného na ISO Base Media File Format (MP4)
- Použití MPEG-2 Transport Stream pro vysílání/multicastové doručování v MBMS
- Profilování kodeků z rodiny Advanced Audio Coding (AAC) pro vysoce efektivní audio
- Definice formátů RTP přenosových jednotek a parametrů popisu relace pro média MPEG
- Podpora technik adaptivního streamování (např. DASH) postavených na médiových segmentech MPEG

## Související pojmy

- [AVC – Assured Voice Communication](/mobilnisite/slovnik/avc/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [AAC – Advanced Audio Coding](/mobilnisite/slovnik/aac/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.960** (Rel-4) — UMTS Mobile Multimedia Technical Challenges
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.402** (Rel-19) — Enhanced aacPlus Error Concealment & Processing
- **TS 26.405** (Rel-19) — Parametric Stereo Encoder for Enhanced aacPlus
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [MPEG na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpeg/)
