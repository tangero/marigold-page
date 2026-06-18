---
slug: "nal"
url: "/mobilnisite/slovnik/nal/"
type: "slovnik"
title: "NAL – Network Abstraction Layer"
date: 2025-01-01
abbr: "NAL"
fullName: "Network Abstraction Layer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nal/"
summary: "Vrstva v mediálních kodecích, jako je H.264/AVC a H.265/HEVC, která formátuje zakódovaná video data do standardizovaných jednotek nazývaných NAL jednotky. Poskytuje strukturu paketu vhodnou pro síť, o"
---

NAL je vrstva ve video kodecích, která formátuje zakódovaná data do standardizovaných jednotek vhodných pro přenos po síti, odděluje video kódování od specifik přenosu, aby umožnila efektivní streamování a odolnost proti chybám.

## Popis

Network Abstraction Layer (NAL, síťová abstraktní vrstva) je konceptuální vrstva definovaná ve standardech pro kódování videa, jako je H.264/Advanced Video Coding ([AVC](/mobilnisite/slovnik/avc/)) a H.265/High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)), které jsou široce přijímány organizací 3GPP pro multimediální telefonii (IMS), službu Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a streamovací služby. Jejím hlavním úkolem je mapovat výstup Video Coding Layer ([VCL](/mobilnisite/slovnik/vcl/)), který obsahuje komprimovaná video data (slice z makrobloků nebo coding tree units), do jednotného formátu nazývaného NAL jednotky. NAL jednotka je struktura podobná paketu, skládající se z hlavičky a datové části. Hlavička obsahuje klíčové informace, jako je typ NAL jednotky, který identifikuje, zda datová část obsahuje zakódovaný slice snímku, sadu parametrů sekvence ([SPS](/mobilnisite/slovnik/sps/)), sadu parametrů snímku ([PPS](/mobilnisite/slovnik/pps/)) nebo doplňkové informace pro vylepšení ([SEI](/mobilnisite/slovnik/sei/)). Tato abstrakce odděluje vysoce komplexní proces kódování/dekódování videa od specifik podkladové přenosové sítě nebo úložného média.

Jak to funguje: Poté, co VCL zakóduje slice snímku, vyprodukuje surové bitové řetězce. NAL tyto řetězce formátuje do NAL jednotek přidáním prefixu startovního kódu (nebo informace o délce) a hlavičky NAL jednotky. Pro přenos přes paketové sítě jako IP se NAL jednotky často používají přímo jako datová část paketů protokolu Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)), jak je definováno ve specifikacích 3GPP a IETF. Toto je známé jako režim paketizace. Struktura NAL jednotky usnadňuje síťovým prvkům (např. bránám, firewallům) nebo příjemci identifikovat typ dat bez nutnosti úplného dekódování videa, což umožňuje síťově orientované zpracování, jako je upřednostňování sad parametrů (SPS/PPS), které jsou klíčové pro dekódování, nebo aplikaci technik pro maskování chyb při detekci ztráty.

NAL hraje zásadní roli v odolnosti proti chybám a přizpůsobivosti. Oddělením sad parametrů (které obsahují klíčovou konfiguraci pro dekódování) od dat slice umožňuje NAL přenos těchto životně důležitých parametrů spolehlivě a mimo hlavní datový proud, čímž je chrání před ztrátou. Dále jsou definovány specifické typy NAL jednotek pro označení konce sekvence, datového proudu nebo pro přenos výplňových dat. V systémech 3GPP specifikace jako 26.114 (IMS) a 26.346 (MBMS) definují přesné profily a úrovně pro H.264/AVC a H.265/HEVC, které inherentně spoléhají na strukturu NAL. Návrh NAL umožňuje funkce jako časová škálovatelnost a snadná transkódace, protože různé NAL jednotky mohou reprezentovat různé vrstvy nebo kvality video proudu. Jeho standardizovaný formát je důvodem, proč stejný zakódovaný video soubor může být uložen, streamován přes HTTP, přenášen pomocí RTP/UDP ve videohovoru nebo vysílán přes MBMS, přičemž je vyžadována pouze minimální adaptace na přenosové vrstvě.

## K čemu slouží

NAL byl vytvořen k řešení problému přenosu komprimovaných video bitových proudů přes různorodá a potenciálně nepřátelská síťová prostředí. Rané video kodeky často produkovaly souvislý, monolitický bitový proud, který byl vysoce náchylný k chybám; jediná chyba v bitu mohla způsobit ztrátu synchronizace a selhání dekodéru. Motivací pro NAL, zavedený s H.264/AVC, bylo vytvořit flexibilní, paketově orientované rozhraní mezi video enkodérem a sítí. Tato abstrakce řeší omezení těsného propojení mezi kódováním a přenosem.

Historický kontext představuje konvergence video aplikací na IP sítě a bezdrátové systémy na počátku 21. století. 3GPP potřebovalo efektivní způsob doručování videa přes rádiové spoje náchylné k chybám a přes různé brány. NAL to poskytuje strukturou bitového proudu do diskrétních jednotek (NAL jednotek) s jasnými hranicemi a soběstačnými hlavičkami. To umožňuje: 1) Snadnou paketizaci pro přenos přes RTP/IP, 2) Robustní detekci a obnovu chyb (protože ztráty jsou omezeny na konkrétní NAL jednotky), 3) Prioritizaci důležitých dat (sad parametrů) a 4) Kompatibilitu s různými přenosovými protokoly (RTP, MPEG-2 TS, formáty souborů). Pro služby 3GPP jako Packet-switched Streaming Service (PSS) a Multimedia Telephony Service for IMS (MTSI) je NAL nezbytnou formátovací vrstvou, která činí video kodeky nezávislými na síti, což umožňuje interoperabilitu, efektivní využití šířky pásma a odolnost proti ztrátě paketů, což je klíčové pro kvalitu uživatelského zážitku při poskytování mobilního videa.

## Klíčové vlastnosti

- Formátuje zakódovaná video data do paketům podobných NAL jednotek
- Definuje typy NAL jednotek pro video slice, sady parametrů a řídicí informace
- Odděluje Video Coding Layer (VCL) od specifik přenosu
- Umožňuje přímou paketizaci do RTP pro streamování v reálném čase
- Usnadňuje odolnost proti chybám díky nezávislé struktuře jednotek
- Podporuje škálovatelnost a prioritizaci video dat

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TS 26.822** (Rel-19) — 5G RTP Configurations Study Phase 2
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services
- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [NAL na 3GPP Explorer](https://3gpp-explorer.com/glossary/nal/)
