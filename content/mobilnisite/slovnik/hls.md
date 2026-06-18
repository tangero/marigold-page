---
slug: "hls"
url: "/mobilnisite/slovnik/hls/"
type: "slovnik"
title: "HLS – HTTP Live Streaming"
date: 2025-01-01
abbr: "HLS"
fullName: "HTTP Live Streaming"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hls/"
summary: "HTTP Live Streaming (HLS) je adaptivní streamovací komunikační protokol vyvinutý společností Apple a později standardizovaný pro přenos multimédií přes IP sítě. Funguje tak, že rozdělí datový proud na"
---

HLS je adaptivní streamovací protokol pro přenos multimédií přes IP sítě, který funguje tak, že rozdělí datový proud na sekvenci malých souborů stahovaných přes HTTP.

## Popis

[HTTP](/mobilnisite/slovnik/http/) Live Streaming (HLS) je adaptivní streamovací protokol ([ABR](/mobilnisite/slovnik/abr/)), který doručuje multimédia (audio, video a přidružená metadata) přes standardní HTTP spojení. Ačkoli byl původně vyvinut společností Apple, jeho rozšířené přijetí vedlo k jeho specifikaci v rámci 3GPP pro zajištění interoperability a efektivního doručování v mobilním prostředí. Základním principem HLS je segmentace kontinuálního mediálního proudu na sérii krátkých, samostatných mediálních souborů (typicky .ts soubory pro [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Transport Stream nebo fragmenty .mp4). Tyto segmenty jsou uvedeny v souboru seznamu stop nazývaném Hlavní seznam stop a Mediální seznamy stop (formát M3U8), což jsou jednoduché textové soubory odkazující na [URL](/mobilnisite/slovnik/url/) segmentů. Klientovský přehrávač nejprve stáhne seznam stop a poté sekvenčně stahuje a přehrává mediální segmenty.

Architektura systému pro doručování HLS se skládá ze tří hlavních komponent: serveru, distribuční komponenty a klienta. Na straně serveru zdrojový obsah připravuje mediální enkodér a segmentátor proudu. Enkodér typicky vytváří více verzí stejného obsahu s různými datovými toky a rozlišeními. Segmentátor zabalí každou verzi do série malých souborů a vygeneruje odpovídající seznamy stop. Tyto soubory jsou poté umístěny na standardní webový server nebo Content Delivery Network ([CDN](/mobilnisite/slovnik/cdn/)) pro distribuci. Distribuce probíhá čistě přes HTTP, využívá masivní existující infrastrukturu webu včetně cache proxy a CDN. Není vyžadován žádný specializovaný streamovací serverový protokol.

Na straně klienta provádí HLS přehrávač (např. v mobilní aplikaci nebo webovém prohlížeči) adaptivní logiku. Začne stažením Hlavního seznamu stop, který obsahuje odkazy na různé Mediální seznamy stop, z nichž každý odpovídá verzi s jiným datovým tokem. Přehrávač nejprve vybere vhodný datový tok na základě odhadované šířky pásma a možností zařízení. Poté začne stahovat segmenty ze seznamu stop této verze. Klíčové je, že přehrávač kontinuálně monitoruje rychlost stahování a stav vyrovnávací paměti. Pokud se podmínky zhorší, může plynule přepnout na seznam stop s nižším datovým tokem pro následující segmenty, aby se předešlo opětovnému načítání. Naopak, pokud se šířka pásma zlepší, může přepnout na vyšší kvalitu. K tomuto přepínání dochází na hranicích segmentů, díky čemuž je adaptace plynulá. Práce 3GPP na HLS, zdokumentovaná ve specifikacích jako TS 26.244 (Transparentní paketově spínaná streamovací služba end-to-end), se zaměřuje na profily, kodeky a optimalizace doručování pro mobilní sítě, čímž zajišťuje efektivní využití rádiových zdrojů a dobrou kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)).

## K čemu slouží

HLS byl vytvořen k řešení problému spolehlivého streamování videa vysoké kvality přes nepředvídatelné sítě, zejména veřejný internet a mobilní sítě. Předchozí streamovací technologie, jako [RTSP](/mobilnisite/slovnik/rtsp/)/[RTP](/mobilnisite/slovnik/rtp/), často vyžadovaly specializované servery, čelily problémům s průchodem přes firewally/NAT a neuměly dobře zvládat kolísání šířky pásma. Přechod na doručování založené na HTTP byl motivován univerzální kompatibilitou HTTP: snadno prochází firewally, těží z všudypřítomné infrastruktury webového ukládání do mezipaměti (CDN) a škáluje se jednoduše pomocí standardních webových serverů. To dramaticky snižuje náklady a složitost nasazení rozsáhlých streamovacích služeb.

Jeho přijetí do standardů 3GPP bylo poháněno explozivním růstem mobilního video provozu. Mobilní sítě představují jedinečné výzvy s proměnlivou propustností, latencí a ztrátou paketů v důsledku rádiových podmínek, mobility a zahlcení. Schopnost HLS adaptivně měnit datový tok je pro toto prostředí dokonale vhodná, protože umožňuje klientovi dynamicky přizpůsobit kvalitu videa dostupné síťové kapacitě, čímž předchází zastavením a poskytuje nejlepší možný zážitek. Standardizace 3GPP zajišťuje konzistentní základní implementaci napříč zařízeními a sítěmi a usnadňuje interoperabilitu. Řeší omezení dřívějších proprietárních nebo méně adaptivních streamovacích metod a umožňuje službám, jako je živé TV, video na vyžádání a streamování událostí, bezchybně fungovat na chytrých telefonech a tabletech, které se staly primárními zařízeními pro konzumaci videa.

## Klíčové vlastnosti

- Adaptivní streamování s proměnným datovým tokem (ABR): Dynamicky přepíná mezi více enkodovanými datovými toky na základě aktuálních síťových podmínek.
- Doručování založené na HTTP: Používá standardní HTTP GET požadavky, čímž využívá existující webovou infrastrukturu, CDN a ukládání do mezipaměti.
- Segmentace médií: Rozděluje datové proudy na krátké, stahovatelné soubory (např. 2-10 sekund) pro flexibilní přepínání a vyhledávání.
- Řízeno seznamy stop (M3U8): Používá textové soubory seznamů stop k indexování dostupných mediálních segmentů a alternativních verzí.
- Široká podpora kodeků: Typicky používá H.264/AVC nebo H.265/HEVC pro video a AAC pro audio, s podporou dalších.
- Podpora živého vysílání a obsahu na vyžádání: Jednotná architektura protokolu podporuje jak živé streamování, tak doručování předem nahraného obsahu.

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [CDN – Content Delivery Network / Content Distribution Network](/mobilnisite/slovnik/cdn/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.347** (Rel-19) — MBMS Transport Protocol and API (TRAPI)
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [HLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hls/)
