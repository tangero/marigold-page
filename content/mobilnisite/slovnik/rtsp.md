---
slug: "rtsp"
url: "/mobilnisite/slovnik/rtsp/"
type: "slovnik"
title: "RTSP – Real-time Streaming Protocol"
date: 2025-01-01
abbr: "RTSP"
fullName: "Real-time Streaming Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rtsp/"
summary: "Řídicí protokol aplikační vrstvy určený pro navazování a správu mediálních relací mezi koncovými body, jako jsou streamovací servery a klienti. Umožňuje kontrolu nad doručováním multimedií v reálném č"
---

RTSP je řídicí protokol aplikační vrstvy pro navazování a správu mediálních relací mezi koncovými body, umožňující kontrolu nad doručováním streamování v reálném čase (jako přehrávání a pozastavení) pro služby v mobilních sítích.

## Popis

Real-time Streaming Protocol (RTSP) je textový protokol fungující na aplikační vrstvě, syntakticky podobný [HTTP](/mobilnisite/slovnik/http/), definovaný [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 2326, s adaptacemi ve specifikacích 3GPP. Umožňuje klientům řídit streamovací mediální servery, poskytuje příkazy pro nastavení, spuštění, pozastavení a ukončení mediálních relací. RTSP zpravidla nenosí vlastní mediální data; místo toho spolupracuje s transportními protokoly jako [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol) pro doručování dat a [RTCP](/mobilnisite/slovnik/rtcp/) (RTP Control Protocol) pro zpětnou vazbu o kvalitě. V architekturách 3GPP je RTSP integrován do multimediálních podsystémů, jako je IP Multimedia Subsystem (IMS), pro podporu streamovacích služeb přes paketově přepínané sítě.

Fungování RTSP zahrnuje model klient-server, kde klient posílá RTSP požadavky (např. DESCRIBE, SETUP, PLAY, PAUSE, TEARDOWN) na server pro vyjednání parametrů relace. Například mobilní zařízení streamující video zahájí RTSP relaci požadavkem na popis média, poté naváže toky RTP/[RTCP](/mobilnisite/slovnik/rtpcp/) pro přenos dat. Klíčové komponenty zahrnují RTSP klienta (např. aplikace v UE), RTSP server (např. poskytovatel streamovací služby) a identifikátory relací, které spravují stav. RTSP zprávy jsou přenášeny přes TCP nebo [UDP](/mobilnisite/slovnik/udp/), přičemž specifikace 3GPP často definují optimalizace pro bezdrátová prostředí pro zvládnutí variací latence a šířky pásma.

Role RTSP v síti je klíčová pro umožnění interaktivních streamovacích služeb, jako je video na požádání nebo živé vysílání, v mobilních ekosystémech. Poskytuje standardizovaný způsob kontroly doručování médií, což zajišťuje kompatibilitu napříč různými zařízeními a sítěmi. V rámci 3GPP je RTSP odkazován ve specifikacích jako 26.234 pro paketově přepínané streamovací služby, podporuje správu QoS a plynulé přehrávání. Jeho integrace pomáhá operátorům nasazovat bohaté mediální aplikace při zachování síťové efektivity a uživatelského zážitku.

## K čemu slouží

RTSP byl vytvořen k řešení potřeby standardizovaného protokolu pro řízení multimediálních toků v reálném čase přes IP sítě, čímž řešil problémy interoperability a správy relací v raném internetovém streamování. Před RTSP dominovala proprietární řešení, což vedlo k fragmentaci a omezené dostupnosti služeb. Protokol, zavedený v 3GPP od Rel-5, umožnil mobilním sítím podporovat streamovací aplikace tím, že poskytl společný rámec pro řízení přehrávání, což odpovídalo růstu mobilních datových služeb a spotřeby multimediálního obsahu.

Historicky vycházela motivace pro RTSP v 3GPP z rozšíření schopností 3G, které nabízely vyšší přenosové rychlosti vhodné pro streamování videa. Řešil omezení jednoduchých modelů „stáhnout a přehrát“ tím, že umožňoval interaktivní kontrolu nad síťovými toky, podobně jako videorekordér. To bylo nezbytné pro služby jako mobilní [TV](/mobilnisite/slovnik/tv/) nebo videohovory, kde uživatelé očekávají funkce pozastavení a převíjení. Konstrukce RTSP odděluje řízení od doručování dat, což optimalizuje využití síťových zdrojů a umožňuje škálovatelnost napříč různými klientskými zařízeními.

V pozdějších vydáních se účel RTSP vyvinul k podpoře pokročilých funkcí, jako je adaptivní streamování s proměnným datovým tokem a integrace s IMS pro obohacené komunikační služby. Zůstává relevantní i v kontextech 5G pro ultra-spolehlivou komunikaci s nízkou latencí, zajišťuje, že streamovací protokoly mohou splňovat přísné požadavky na QoS. Zachováním zpětné kompatibility při přizpůsobení novým síťovým podmínkám zůstává RTSP základním prvkem pro služby médií v reálném čase ve standardech 3GPP.

## Klíčové vlastnosti

- Příkazy pro řízení relace (např. PLAY, PAUSE, TEARDOWN)
- Integrace s RTP/RTCP pro doručování médií
- Textový protokol podobný HTTP pro snadnou implementaci
- Podpora transportu přes TCP i UDP
- Správa stavových relací s jedinečnými identifikátory
- Kompatibilita se streamovacími službami 3GPP a IMS

## Související pojmy

- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TR 25.993** (Rel-19) — UTRA RAB Examples and Radio Interface Mapping
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.827** (Rel-12) — IMS-based Streaming & Download Delivery Enhancements
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)

---

📖 **Anglický originál a plná specifikace:** [RTSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtsp/)
