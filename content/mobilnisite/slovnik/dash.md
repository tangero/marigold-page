---
slug: "dash"
url: "/mobilnisite/slovnik/dash/"
type: "slovnik"
title: "DASH – Dynamic Adaptive Streaming over HTTP"
date: 2025-01-01
abbr: "DASH"
fullName: "Dynamic Adaptive Streaming over HTTP"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dash/"
summary: "DASH je standard adaptivního streamování s proměnným datovým tokem pro doručování médií přes HTTP. Umožňuje klientům dynamicky vybírat nejvhodnější segment videa na základě síťových podmínek a možnost"
---

DASH je standard adaptivního streamování s proměnným datovým tokem, který doručuje média přes HTTP tím, že umožňuje klientům dynamicky vybírat kvalitu videa na základě síťových podmínek pro plynulé přehrávání v mobilních a širokopásmových sítích.

## Popis

Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) (DASH) je mezinárodní standard pro adaptivní streamování s proměnným datovým tokem, který doručuje mediální obsah z běžných HTTP webových serverů. Jeho architektura je řízena klientem, kde klient autonomně vybírá mediální segmenty z různých reprezentací (datové toky, rozlišení, kodeky) uvedených v souboru Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)). MPD je XML dokument, který popisuje strukturu mediální prezentace včetně časování, URL a charakteristik dostupných mediálních segmentů. Klient tento MPD periodicky načítá a poté žádá o jednotlivé mediální segmenty (obvykle několik sekund dlouhé) prostřednictvím standardních HTTP GET požadavků. Hlavní inteligence spočívá v adaptační logice klienta, která sleduje podmínky sítě v reálném čase (jako dostupná šířka pásma) a parametry zařízení (jako vytížení [CPU](/mobilnisite/slovnik/cpu/) a rozlišení obrazovky), aby vybrala další segment z nejvhodnější reprezentace, s cílem maximalizovat kvalitu a minimalizovat opětovné načítání do vyrovnávací paměti.

Protokol funguje tak, že rozdělí mediální obsah na sekvenci malých segmentů souborů založených na HTTP. Každý segment obsahuje krátký interval doby přehrávání a pro každý interval existuje více alternativních segmentů zakódovaných s různými datovými toky a rozlišeními. Klient tyto segmenty stahuje jeden po druhém. Po stažení segmentu klient vyhodnotí podmínky a rozhodne, jaký datový tok zvolit pro další segment. Toto rozhodnutí probíhá plynule během přehrávání, což umožňuje adaptaci na měnící se propustnost sítě, například když se uživatel přesune ze sítě 5G na Wi-Fi. DASH je nezávislý na kodeku, podporuje běžné video a audio kodeky jako [AVC](/mobilnisite/slovnik/avc/)/H.264, [HEVC](/mobilnisite/slovnik/hevc/)/H.265 a [AAC](/mobilnisite/slovnik/aac/) a může doručovat živý i na vyžádání poskytovaný obsah.

Klíčové komponenty zahrnují DASH klienta (mediální přehrávač s adaptační logikou), HTTP server(y) hostující segmenty a MPD a samotný MPD. MPD popisuje časovou strukturu (Periody, Adaptační sady, Reprezentace a Segmenty), dostupnost (šablony URL) a mediální charakteristiky (kodek, rozlišení, datový tok). Role DASH v sítích 3GPP spočívá v umožnění služeb pro doručování médií, zejména pro službu Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a unicast streamování. Je integrován do služby 3GPP Packet-Switched Streaming Service (PSS) a Multimedia Telephony Service ([MTSI](/mobilnisite/slovnik/mtsi/)) a poskytuje standardizovanou metodu pro efektivní, škálovatelné a kvalitní video streamování přes mobilní a pevné sítě. Jeho využití HTTP umožňuje využít stávající webovou infrastrukturu včetně CDN a cache proxy serverů, což zjednodušuje nasazení a snižuje náklady.

## K čemu slouží

DASH byl vytvořen, aby řešil výzvy spojené s doručováním kvalitního videa přes sítě IP s doručováním v rámci možností (best-effort), zejména přes internet a mobilní sítě, kde se šířka pásma výrazně mění. Před adaptivním streamováním se video doručovalo prostřednictvím progresivního stahování nebo protokolů pro streamování v reálném čase jako RTSP, což často vedlo k častému načítání do vyrovnávací paměti nebo nízké kvalitě při zhoršení síťových podmínek. Tyto metody typicky uzamkly klienta na jediný datový tok po celou dobu relace, což vedlo k neoptimálnímu uživatelskému zážitku. DASH to řeší tím, že umožňuje klientovi přizpůsobit datový tok média v reálném čase, čímž zajišťuje nepřetržité přehrávání díky kompromisu mezi okamžitou kvalitou videa a rizikem opětovného načítání do vyrovnávací paměti.

Historický kontext zahrnuje rozšíření proprietárních řešení adaptivního streamování (jako Apple HLS a Microsoft Smooth Streaming), která fragmentovala trh. 3GPP ve spolupráci s MPEG standardizovalo DASH, aby vytvořilo jediné interoperabilní řešení. To bylo motivováno potřebou univerzálního standardu, který by mohl být nasazen napříč různými sítěmi (3G, 4G, 5G, pevné) a zařízeními, což snižuje složitost pro poskytovatele obsahu a umožňuje inovace v adaptačních algoritmech klientů. Standardizace prostřednictvím 3GPP a ISO/IEC (jako MPEG-DASH) zajistila široké přijetí v odvětví.

DASH konkrétně řeší omezení předchozích přístupů tím, že je čistě založen na HTTP, což zjednodušuje průchod firewally a NAT, využívá všudypřítomné HTTP cache pro škálovatelnost a odděluje logiku streamování od transportního protokolu. Poskytuje poskytovatelům obsahu kontrolu nad nabízenými reprezentacemi a klientům inteligenci pro optimální volbu, čímž vytváří robustní systém pro doručování médií v dynamických síťových prostředích, což je zásadní pro spotřebu mobilního videa.

## Klíčové vlastnosti

- Doručování založené na HTTP s využitím standardních webových serverů a cache
- Výběr adaptivního datového toku řízený klientem na základě podmínek v reálném čase
- XML Media Presentation Description (MPD) pro popis struktury média
- Nezávislost na kodeku s podporou různých video a audio formátů
- Podpora služeb živého streamování i streamování na vyžádání
- Segmentované mediální soubory umožňující flexibilní distribuci přes CDN

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [CMAF – Common Media Application Format](/mobilnisite/slovnik/cmaf/)

## Definující specifikace

- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.117** (Rel-19) — 5G Media Streaming Speech/Audio Capabilities
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.307** (Rel-19) — 3GPP HTML5 Profile Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.347** (Rel-19) — MBMS Transport Protocol and API (TRAPI)
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- … a dalších 30 specifikací

---

📖 **Anglický originál a plná specifikace:** [DASH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dash/)
