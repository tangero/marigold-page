---
slug: "vcl"
url: "/mobilnisite/slovnik/vcl/"
type: "slovnik"
title: "VCL – Video Coding Layer"
date: 2025-01-01
abbr: "VCL"
fullName: "Video Coding Layer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vcl/"
summary: "Video Coding Layer je konceptuální vrstva v architekturách pro doručování médií, zejména pro streamovací služby jako DASH a MBMS. Představuje sadu video reprezentací zakódovaných s různými datovými to"
---

VCL je konceptuální vrstva v architekturách pro doručování médií, která představuje sadu video reprezentací zakódovaných s různými datovými toky a rozlišeními za účelem umožnění adaptivního streamování dle datového toku.

## Popis

Video Coding Layer (VCL) je termín používaný ve specifikacích 3GPP souvisejících s multimediálním vysíláním a streamovacími službami, jako je Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)) a Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Nejde o fyzickou síťovou vrstvu, ale o logické seskupení v rámci popisu mediální prezentace. VCL zahrnuje více zakódovaných verzí (reprezentací) stejného videoobsahu, z nichž každá má odlišné charakteristiky, jako je datový tok, rozlišení, snímková frekvence a profil kodeku. Tyto reprezentace jsou časově synchronizované, což znamená, že obsahují stejné segmenty obsahu, ale v různých úrovních kvality. Tato struktura je základním kamenem adaptivního streamování dle datového toku ([ABR](/mobilnisite/slovnik/abr/)), kde klientovský přehrávač může během přehrávání dynamicky přepínat mezi reprezentacemi na základě aktuálních síťových podmínek a možností zařízení.

V typické streamovací službě založené na DASH soubor Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) popisuje dostupné VCL. Každý VCL obsahuje jednu nebo více adaptačních sad, které seskupují reprezentace považované klientem za zaměnitelné (např. stejný obsah v různých datových tocích). Uvnitř VCL jsou reprezentace organizovány do segmentů o délce několika sekund. Klient sleduje svou dostupnou šířku pásma, stav vyrovnávací paměti a kapacitu procesoru a pomocí algoritmu adaptace datového toku vybírá další video segment z nejvhodnější reprezentace v rámci zvoleného VCL. Tím je zajištěn plynulý přehrávací proces bez zasekávání a optimalizuje se uživatelský zážitek z kvality ([QoE](/mobilnisite/slovnik/qoe/)).

Koncept je hojně využíván ve službě Enhanced Multimedia Broadcast Multicast Service (eMBMS) a evolved Multimedia Broadcast Multicast Service (FeMBMS) od 3GPP pro efektivní vysílání. Ve vysílacích scénářích může být současně vysíláno více VCL a přijímače mohou dekódovat vrstvu nejvhodnější pro jejich podmínky příjmu. Specifikace popisující VCL (např. 3GPP TS 26.346 pro MBMS, TS 26.247 pro DASH) definují formáty, signalizaci a protokoly pro zapouzdření a doručování těchto vrstevnatých videostreamů. Tento vrstevnatý přístup je klíčový pro nasazení skalabilního kódování videa ([SVC](/mobilnisite/slovnik/svc/)) a vysoce účinného kódování videa ([HEVC](/mobilnisite/slovnik/hevc/)), což umožňuje efektivní využití síťových zdrojů pro jednosměrné i vysílací video služby.

## K čemu slouží

Koncept Video Coding Layer byl vyvinut pro řešení výzvy doručování videa vysoké kvality přes sítě s vysoce proměnnou a nepředvídatelnou šířkou pásma, jako jsou mobilní buněčné sítě. Tradiční progresivní stahování nebo streamování s konstantním datovým tokem často vedlo k přerušením bufferingu nebo suboptimální kvalitě videa při změně síťových podmínek. Model VCL, ústřední pro adaptivní streamování, byl vytvořen za účelem oddělení kódování videa od síťového doručování, což klientovi umožňuje přizpůsobovat se v reálném čase.

Jeho přijetí v rámci standardů 3GPP bylo hnací silou exploze mobilního videoprovozu a potřeby efektivních vysílacích mechanismů pro živé události a oblíbený obsah. Standardizací způsobu, jakým jsou strukturovány a popsány vícečetné video reprezentace (např. v MPD), VCL umožňuje interoperabilitu mezi poskytovateli obsahu, síťovými operátory a výrobci zařízení. Řeší problém "univerzálního" doručování videa, což službám umožňuje současně uspokojovat širokou škálu zařízení (od chytrých telefonů po tablety) a síťových prostředí (od přetížených buněk 4G po vysokorychlostní připojení 5G), čímž maximalizuje spokojenost uživatelů a využití sítě.

## Klíčové vlastnosti

- Seskupuje více zakódovaných video reprezentací stejného obsahu
- Umožňuje dynamické adaptivní přepínání datového toku (ABR) během přehrávání
- Definuje časově synchronizované segmenty pro plynulé přepínání reprezentací
- Podporuje signalizaci prostřednictvím standardů jako DASH MPD a MBMS user service description
- Usnadňuje efektivní vysílací doručování prostřednictvím simultánního přenosu více vrstev
- Integruje pokročilé videokodeky jako AVC, HEVC a VVC pro kvalitní účinnost

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MPD – Media Presentation Description](/mobilnisite/slovnik/mpd/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [VCL na 3GPP Explorer](https://3gpp-explorer.com/glossary/vcl/)
