---
slug: "ptl"
url: "/mobilnisite/slovnik/ptl/"
type: "slovnik"
title: "PTL – Profile, Tier, and Level"
date: 2025-01-01
abbr: "PTL"
fullName: "Profile, Tier, and Level"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ptl/"
summary: "Třídílný klasifikační systém pro video kodeky, především High Efficiency Video Coding (HEVC/H.265), definující sady kódovacích nástrojů, maximální datové toky a zpracovatelské schopnosti. Zajišťuje in"
---

PTL je třídílný klasifikační systém video kodeků, primárně pro HEVC, který definuje kódovací nástroje, datové toky a schopnosti dekodéru, aby zajistil interoperabilitu pro různé úrovně složitosti a kvality videa.

## Popis

Profil, úroveň a stupeň (PTL) je sada parametrů definovaná v rámci standardů pro kódování videa, jako je [HEVC](/mobilnisite/slovnik/hevc/) (H.265) a [VVC](/mobilnisite/slovnik/vvc/) (H.266), a odkazovaná ve specifikacích 3GPP pro doručování médií. Jedná se o trojici, která komplexně popisuje schopnosti potřebné k dekódování video datového proudu. Profil definuje podmnožinu algoritmických nástrojů a funkcí celého kódovacího standardu, kterou musí dekodér podporovat (např. Main Profile, Main 10 Profile pro 10bitovou barevnou hloubku). Úroveň (Tier) označuje rozsah maximálních datových toků, přičemž High Tier umožňuje vyšší datové toky než Main Tier. Stupeň (Level) omezuje klíčové zpracovatelské parametry, jako je maximální velikost snímku (v samplech), snímková frekvence a velikost bufferu dekódovaného snímku, které přímo souvisejí s výpočetními a paměťovými požadavky.

Z architektonického hlediska jsou informace PTL přenášeny v samotném video datovém proudu, typicky v sadách parametrů jako Video [Parameter](/mobilnisite/slovnik/parameter/) Set ([VPS](/mobilnisite/slovnik/vps/)), Sequence Parameter Set ([SPS](/mobilnisite/slovnik/sps/)) nebo podobné syntaxe vysoké úrovně. Když 3GPP aplikace, jako je klient služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) nebo přehrávač Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)), přijme video proud, může analyzovat informace PTL a určit, zda její dekodér (nebo hardwarové vybavení zařízení) má potřebné schopnosti korektně dekódovat a zobrazit video. To je klíčové pro adaptivní streamování, kde server může nabízet více video reprezentací (zakódovaných verzí) s různými kombinacemi PTL a klient si musí vybrat tu, která je kompatibilní s jeho zdroji.

Jak to funguje, je založeno na konformačních bodech. Video enkodér při vytváření datového proudu pracuje v rámci omezení konkrétní kombinace PTL. Například může zakódovat 4K video pomocí Main 10 Profile, High Tier, Level 5.1. Tato volba PTL signalizuje každému dekodéru, že pro přehrání tohoto proudu musí podporovat 10bitové zpracování, kódovací nástroje Main 10 Profile a být schopen zvládnout datové toky a zpracovatelské nároky definované High Tier, Level 5.1. Systém 3GPP používá tuto informaci pro výměnu informací o schopnostech a vyjednávání relace, zejména ve službách jako evolved Multimedia Broadcast Multicast Service (eMBMS) nebo 5G Media Streaming. PTL zajišťuje, že video služba může být efektivně doručována na různorodá zařízení s různými velikostmi obrazovky, výkonem procesoru a výdrží baterie tím, že poskytuje standardizovaný způsob signalizace složitosti.

## K čemu slouží

Systém PTL existuje pro zvládnutí obrovské složitosti a variability moderních video kodeků, jako je HEVC, a pro zajištění interoperability v rozsáhlém ekosystému zařízení. Jak se video rozlišení zvýšila ze SD na HD, 4K a výše a jak byly vyvíjeny nové kódovací nástroje pro lepší kompresi, jediná monolitická implementace dekodéru se stala nepraktickou. Rámec Profil, Úroveň a Stupeň to řeší rozdělením specifikace kodeku na zvládnutelné, interoperabilní podmnožiny. Umožňuje výrobcům zařízení implementovat dekodéry, které podporují pouze kombinace PTL relevantní pro jejich cílový trh (např. mobilní telefon může podporovat až Level 4, zatímco televize podporuje Level 6.2), čímž snižuje náklady a spotřebu energie.

Jeho přijetí do 3GPP, zejména zaznamenané v Technické specifikaci 26.948 pro zpracování mediálních aplikací, bylo motivováno potřebou efektivního doručování videa přes mobilní sítě. Mobilní sítě mají omezenou a proměnlivou šířku pásma a uživatelská zařízení mají různorodé schopnosti. Parametry PTL poskytují granularitu potřebnou pro pokročilé techniky adaptivního streamování. Poskytovatel obsahu může vytvořit více verzí stejného obsahu s různými PTL a klient si může vybrat proud s nejvyšší kvalitou, který jeho zařízení dokáže dekódovat a který síť dokáže doručit, čímž je zajištěn plynulý divácký zážitek. Tím se řeší omezení dřívějšího, méně strukturovaného signalizování schopností.

Historicky podobné koncepty (Profil a Stupeň) existovaly ve starších standardech jako H.264/AVC, ale HEVC formalizovalo koncept Úrovně (Tier) pro lepší zvládnutí aplikací s vysokým datovým tokem a vysokým rozlišením, jako je ultra-high-definition video. Práce 3GPP, zejména od Release 13 dále, integrovala tyto koncepty video kodeků do specifikací své servisní vrstvy pro optimalizaci doručování médií pro LTE Broadcast, streamování a později mediální služby založené na 5G. Rámec PTL je zásadní pro umožnění vysokokvalitních video služeb, které jsou hlavním hybatelem mobilního datového provozu, protože zajišťuje, že složité video může být spolehlivě dekódováno na jakémkoli kompatibilním zařízení, což podporuje konzistentní uživatelský zážitek napříč průmyslem.

## Klíčové vlastnosti

- Třídílný identifikátor (Profil, Úroveň, Stupeň) definující konformační body video dekodéru
- Profil specifikuje podporované kódovací nástroje a bitovou hloubku (např. Main, Main 10)
- Úroveň (Tier) definuje limity maximálního datového toku (Main Tier pro normální, High Tier pro aplikace s vysokým datovým tokem)
- Stupeň (Level) omezuje zpracovatelské parametry jako maximální rozlišení, snímkovou frekvenci a velikost bufferu
- Signalizováno v syntaxi video datového proudu (např. v VPS nebo SPS pro HEVC)
- Umožňuje porovnávání schopností zařízení a adaptivní streamování ve službách médií 3GPP

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [PTL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptl/)
