---
slug: "hdtv"
url: "/mobilnisite/slovnik/hdtv/"
type: "slovnik"
title: "HDTV – High-definition television"
date: 2025-01-01
abbr: "HDTV"
fullName: "High-definition television"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hdtv/"
summary: "HDTV označuje televizní služby s výrazně vyšším rozlišením než standardní rozlišení (SD), typicky 720p nebo 1080i/p. V rámci 3GPP zahrnuje poskytování videoobsahu ve vysokém rozlišení přes mobilní sít"
---

HDTV je televizní služba s výrazně vyšším rozlišením než standardní rozlišení (SD), poskytovaná přes mobilní sítě za použití účinných kodeků a adaptivního streamování.

## Popis

Televize s vysokým rozlišením (HDTV) v rámci standardů 3GPP definuje systémové požadavky a technické specifikace pro poskytování televizních a videoslužeb s vysokým prostorovým rozlišením (typicky 1280x720 pixelů nebo 1920x1080 pixelů) přes mobilní sítě jako LTE a 5G. Technologie funguje pomocí pokročilých video kompresních kodeků, především H.264/[AVC](/mobilnisite/slovnik/avc/) a později [HEVC](/mobilnisite/slovnik/hevc/), které redukují vysoké nároky na datový tok nekomprimovaného [HD](/mobilnisite/slovnik/hd/) videa do podoby vhodné pro přenos přes bezdrátové spoje s omezenou šířkou pásma. Architektura pro mobilní HDTV zahrnuje přípravu obsahu (kódování a zabalení), doručování pomocí streamovacích protokolů jako [HTTP](/mobilnisite/slovnik/http/) Adaptive Streaming (HAS) definovaný ve specifikacích 3GPP Packet Switched Streaming (PSS) a Dynamic Adaptive Streaming over HTTP ([DASH](/mobilnisite/slovnik/dash/)), a příjem/dekódování na uživatelském zařízení (UE). Klíčové komponenty zahrnují specifikace mediálních kodeků (TS 26.234 pro PSS), mechanismy kvality služeb (QoS) pro zajištění dostatečné propustnosti a nízké latence, a mechanismy pro objevování služeb pro vysílání/vícebodové vysílání (např. eMBMS). Její úlohou v síti je poskytnout standardizovaný, interoperabilní rámec pro poskytovatele služeb, aby mohli nabízet lineární televizní služby a služby videa na vyžádání vysoké kvality mobilním účastníkům. To vyžaduje úzkou koordinaci mezi jádrem sítě, které spravuje poskytování služeb a vytváření přenosových kanálů, a rádiovou přístupovou sítí, která musí efektivně alokovat prostředky pro video toky s vysokým datovým tokem. Specifikace jako TS 26.140 pro multimediální vysílání/vícebodové vysílání ([MBMS](/mobilnisite/slovnik/mbms/)) definují, jak může být obsah HDTV efektivně distribuován více uživatelům současně, optimalizujíc spektrální účinnost.

## K čemu slouží

Standardizace HDTV v 3GPP byla motivována globálním přechodem od standardního rozlišení (SD) k vysílání ve vysokém rozlišení v pevné televizi a potřebou přinést tento vylepšený divácký zážitek na mobilní zařízení. Před jejím zahrnutím bylo mobilní video z velké části omezeno na formáty s nízkým rozlišením jako QCIF nebo QVGA kvůli omezením zařízení a kapacitě sítě. Rozšíření chytrých telefonů s displeji s vysokým rozlišením a expanze sítí 3G/[HSPA](/mobilnisite/slovnik/hspa/) vytvořily poptávku po bohatších mediálních službách. Specifikace 3GPP pro HDTV vyřešily problém spolehlivého doručování náročného [HD](/mobilnisite/slovnik/hd/) obsahu přes proměnlivé bezdrátové podmínky standardizací technik adaptivního streamování s proměnným datovým tokem a účinných kodeků. To umožnilo operátorům spouštět konkurenceschopné služby mobilní televize a video streamování, což pohánělo ARPU z dat a naplňovalo očekávání spotřebitelů nastavená domácími zábavními systémy. Historický kontext zahrnuje vývoj od služby multimediálního vysílání/vícebodového vysílání (MBMS) pro obsah ve standardním rozlišení v 3GPP Release 6 ke vylepšené MBMS (eMBMS) v pozdějších releasech, což bylo klíčové pro ekonomicky škálovatelnou distribuci živého HDTV.

## Klíčové vlastnosti

- Podpora video formátů s vysokým rozlišením (720p, 1080i, 1080p)
- Využití účinných videokodeků jako H.264/AVC a HEVC pro kompresi
- Doručování pomocí adaptivního HTTP streamování (3GP-DASH) pro jednobodový a vysílací/vícebodový přenos (eMBMS)
- Specifikované parametry kvality služeb (QoS) pro garantovaný datový tok a nízký chvění (jitter)
- Mechanismy pro objevování a oznamování služeb pro elektronický průvodce programem (ESG)
- Definice systémové architektury od konce ke konci zahrnující poskytovatele obsahu až po UE

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [AVC – Assured Voice Communication](/mobilnisite/slovnik/avc/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.265** (Rel-19) — Video Operation Points & Capabilities
- **TS 26.851** (Rel-11) — Enhancements to Multimedia (EMM) for PSS, MMS, MBMS
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [HDTV na 3GPP Explorer](https://3gpp-explorer.com/glossary/hdtv/)
