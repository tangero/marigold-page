---
slug: "cmaf"
url: "/mobilnisite/slovnik/cmaf/"
type: "slovnik"
title: "CMAF – Common Media Application Format"
date: 2025-01-01
abbr: "CMAF"
fullName: "Common Media Application Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cmaf/"
summary: "CMAF je standardizovaný mediální formát pro adaptivní datový tok, který umožňuje efektivní doručování audio a video obsahu po sítích. Snižuje náklady na úložiště a doručování tím, že umožňuje použití"
---

CMAF je standardizovaný mediální formát pro adaptivní datový tok (adaptive bitrate streaming), který umožňuje efektivní doručování tím, že umožňuje použití jedné sady mediálních segmentů napříč více protokoly a zařízeními.

## Popis

Common Media Application Format (CMAF) je kontejnerový a doručovací formát pro média standardizovaný organizacemi 3GPP, [MPEG](/mobilnisite/slovnik/mpeg/) a dalšími, navržený ke sjednocení adaptivního datového toku ([ABR](/mobilnisite/slovnik/abr/)). Definuje společnou sadu formátů mediálních segmentů (založených na [ISO](/mobilnisite/slovnik/iso/) Base Media File Format, [ISOBMFF](/mobilnisite/slovnik/isobmff/)), které mohou být jednou zabaleny a doručovány přes více streamovacích protokolů, jako je [HTTP](/mobilnisite/slovnik/http/) Live Streaming ([HLS](/mobilnisite/slovnik/hls/)) a Dynamic Adaptive Streaming over HTTP (MPEG-DASH). Segmenty CMAF jsou strukturovány jako fragmentované soubory [MP4](/mobilnisite/slovnik/mp4/) (fMP4), obsahující mediální data (např. video, audio) a metadata (např. časování, šifrovací informace) způsobem, který podporuje efektivní přenos po částech (chunked transfer) a přehrávání. Formát zahrnuje podporu pokročilých kodeků jako [HEVC](/mobilnisite/slovnik/hevc/)/H.265 a AV1, stejně jako běžného šifrování (CENC) pro správu digitálních práv (DRM).

Z architektonického hlediska CMAF funguje v rámci řetězce doručování médií mezi přípravou obsahu (kódování/balení) a přehráváním na klientovi. Obsah je zakódován do více reprezentací s různým datovým tokem, z nichž každá je segmentována na části kompatibilní s CMAF. Tyto části jsou uloženy na zdrojových serverech nebo v sítích pro doručování obsahu (CDN). Při streamování klient používá manifest (např. MPD pro DASH nebo m3u8 pro HLS) k adaptivnímu vyžádání segmentů na základě síťových podmínek. Klíčovou inovací CMAF je 'CMAF stopa', která definuje soběstačný mediální proud (např. video nebo audio) se specifickými parametry kodeku a šifrování, což umožňuje interoperabilitu. Například jedna CMAF stopa pro video reprezentaci může být poskytnuta jako segment DASH nebo segment HLS bez přebalování, čímž se snižuje režie úložiště a latence.

Role CMAF v sítích 3GPP je nedílnou součástí mediálních služeb, jako je Multimedia Broadcast Multicast Service (MBMS) a 5G Media Streaming. Umožňuje efektivní vysílání (broadcast) a jednosměrné doručování (unicast) živého a na požádání (on-demand) obsahu, podporuje funkce jako streamování s nízkou latencí a síťové zpracování médií. V systémech 5G se CMAF sladil s edge computingem tím, že umožňuje ukládání a zpracování mediálních segmentů na okraji sítě (např. v Multi-access Edge Computing, MEC), čímž zlepšuje kvalitu uživatelského zážitku (QoE). Formát také zahrnuje mechanismy pro časovaná metadata (např. signály pro vkládání reklam) a kódování přenosu po částech (chunked transfer encoding), což umožňuje streamovacím serverům odesílat částečné segmenty, jakmile jsou k dispozici, což je klíčové pro živé události. Celkově CMAF poskytuje základ pro škálovatelné, interoperabilní doručování médií napříč různorodými zařízeními a sítěmi.

## K čemu slouží

CMAF byl vytvořen, aby řešil fragmentaci v ekosystémech adaptivního streamování, kde různé protokoly (např. HLS, DASH) vyžadovaly samostatné mediální segmenty, což vedlo ke zvýšení úložiště, šířky pásma a složitosti. Před CMAF museli poskytovatelé obsahu udržovat více verzí stejného obsahu pro různé streamovací formáty, což bylo neefektivní a nákladné. Tato fragmentace také bránila inovacím, protože nové kodeky nebo funkce potřebovaly implementaci napříč více formáty. CMAF to řeší tím, že poskytuje společný mezilehlý formát, který odděluje přípravu obsahu od doručování, což umožňuje opakované použití jedné sady segmentů napříč protokoly.

Motivace pro CMAF v rámci 3GPP vychází z rostoucí poptávky po mediálních službách vysoké kvality přes mobilní sítě, jako je 4G LTE a 5G. Jelikož video provoz dominuje využití sítě, efektivní doručování se stává klíčové pro výkon sítě a uživatelský zážitek. CMAF snižuje latenci a spotřebu šířky pásma tím, že umožňuje přenos po částech (chunked transfer) a snižuje duplicitní úložiště. Také podporuje pokročilé mediální schopnosti jako streamování 4K/8K, vysoký dynamický rozsah (HDR) a imerzivní audio, které jsou nezbytné pro služby příští generace. Historicky 3GPP integrovalo CMAF do svých specifikací (počínaje Release 15), aby se sladilo s průmyslovými standardy a vylepšilo doručování médií v systémech MBMS a 5G, čímž zajistilo interoperabilitu s globálními streamovacími postupy.

Řešením těchto omezení CMAF umožňuje nákladově efektivní škálování mediálních služeb, zjednodušuje pracovní postupy s obsahem a zlepšuje přizpůsobivost síťovým podmínkám. Je obzvláště důležitý pro 5G, kde aplikace s nízkou latencí (např. živé sporty, virtuální realita) těží z CMAF streamování po částech a integrace na okraji sítě. Formát také zajišťuje budoucí kompatibilitu doručování médií podporou vznikajících kodeků a šifrovacích schémat, což zajišťuje dlouhodobou životaschopnost v rozvíjejícím se telekomunikačním a mediálním prostředí.

## Klíčové vlastnosti

- Jedna sada mediálních segmentů opakovaně použitelná napříč protokoly HLS a MPEG-DASH
- Založeno na fragmentovaném MP4 (fMP4) formátu pro efektivní přenos po částech a přehrávání
- Podporuje pokročilé kodeky včetně HEVC/H.265, AV1 a VVC pro vysoce účinnou kompresi
- Obsahuje Common Encryption (CENC) pro interoperabilní DRM a ochranu obsahu
- Umožňuje streamování s nízkou latencí prostřednictvím kódování přenosu po částech a režimu CMAF Low Latency
- Poskytuje stopy s časovanými metadaty pro dynamické vkládání reklam a signalizaci událostí

## Související pojmy

- [HLS – HTTP Live Streaming](/mobilnisite/slovnik/hls/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.117** (Rel-19) — 5G Media Streaming Speech/Audio Capabilities
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.265** (Rel-19) — Video Operation Points & Capabilities
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [CMAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmaf/)
