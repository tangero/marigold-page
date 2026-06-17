---
slug: "cvs"
url: "/mobilnisite/slovnik/cvs/"
type: "slovnik"
title: "CVS – Coded Video Sequence"
date: 2025-01-01
abbr: "CVS"
fullName: "Coded Video Sequence"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cvs/"
summary: "Coded Video Sequence (CVS) je základní struktura pro kódování videa definovaná 3GPP pro přenos video obsahu přes mobilní sítě. Představuje souvislou sekvenci zakódovaných video obrazů, které lze dekód"
---

CVS je základní struktura pro kódování videa podle 3GPP, která se skládá ze souvislé, nezávisle dekódovatelné sekence zakódovaných obrazů a tvoří kompletní video prezentaci nebo segment pro spolehlivé doručení v mobilních sítích.

## Popis

V kontextu specifikací 3GPP je Coded Video Sequence (CVS) samostatný, dekódovatelný bitový proud, který tvoří video program. Technicky se jedná o sekvenci jednotek síťové abstraktní vrstvy ([NAL](/mobilnisite/slovnik/nal/)), která začíná přístupovou jednotkou pro okamžité dekódování ([IDR](/mobilnisite/slovnik/idr/)) nebo přístupovou jednotkou přerušeného spojení ([BLA](/mobilnisite/slovnik/bla/)) a končí před další IDR nebo BLA přístupovou jednotkou, nebo na konci bitového proudu. Tato struktura zajišťuje body náhodného přístupu a čisté přepínání mezi různými video proudy nebo segmenty, což je zásadní pro adaptivní streamování s proměnným datovým tokem a přepínání kanálů ve vysílacích službách jako je eMBMS (evolved Multimedia Broadcast Multicast Service).

Architektura CVS je nedílnou součástí video kodeků standardizovaných 3GPP, jako je Advanced Video Coding ([AVC](/mobilnisite/slovnik/avc/)/H.264) a High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)/H.265). Zapouzdřuje sekvenci zakódovaných obrazů, včetně I-snímků (intra-frame), P-snímků (predikovaných) a B-snímků (bipredikovaných), uspořádaných podle struktury skupiny obrazů ([GOP](/mobilnisite/slovnik/gop/)). Sekvence začíná klíčovým snímkem (IDR nebo BLA), který resetuje stav dekodéru a umožňuje nezávislé dekódování bez odkazu na předchozí snímky. To je klíčové pro odolnost proti chybám, protože poškození v jedné CVS se nešíří do následujících sekvencí.

V systému 3GPP hraje CVS klíčovou roli v protokolech pro doručování video služeb. Například v Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a jeho vyvinuté variantě (eMBMS) je video obsah zabalen a přenášen jako série jednotek CVS přes vysílací/multicastový přenos. Služba 3GPP Packet-switched Streaming (PSS) a Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) také využívají CVS pro unicastové streamování videa a konverzační služby. Specifikace (např. TS 26.346 pro MBMS, TS 26.265 pro shodu kodeků) definují, jak je CVS mapována na transportní protokoly jako RTP/RTCP a formáty souborů jako 3GP, čímž zajišťuje kompatibilitu od kódování obsahu po přehrávání na uživatelském zařízení.

Role CVS sahá až k kvalitě služeb (QoS) a efektivitě sítě. Díky poskytování jasných hranic pro video segmenty umožňuje efektivní adaptaci šířky pásma, maskování chyb a plynulé předávání spojení při pohybu uživatele. Síťové prvky, jako je Broadcast Multicast Service Center (BM-SC) v MBMS, mohou manipulovat s jednotkami CVS pro oznámení služeb, synchronizaci a doručování. Dále je CVS základní jednotkou pro správu digitálních práv (DRM) a šifrování obsahu v 3GPP, což umožňuje selektivní ochranu video sekvencí bez dopadu na celý proud.

## K čemu slouží

Coded Video Sequence (CVS) byl zaveden za účelem standardizace přenosu a zpracování video obsahu v ekosystému 3GPP, aby vyhověl rostoucí poptávce po mobilních video službách. Před jeho formální definicí ve vydání 12 spoléhal přenos videa přes mobilní sítě na různé proprietární nebo volně definované metody balení paketů, což vedlo k problémům s interoperabilitou, neefektivním využitím šířky pásma a špatným uživatelským zážitkem při narušení sítě nebo přepínání kanálů. CVS poskytuje jasnou, na kodeku nezávislou strukturu, která zajišťuje, že video proudy lze spolehlivě dekódovat, upravovat a přenášet přes heterogenní sítě a zařízení.

Primárním motivem pro standardizaci CVS byla podpora efektivních vysílacích a multicastových služeb, konkrétně MBMS/eMBMS, kde je jeden video proud doručován více uživatelům současně. Bez standardizované struktury sekvence bylo náročné zvládat náhodný přístup, kontinuitu služeb a adaptivní streamování ve vysílacích scénářích. CVS umožňuje síti vkládat synchronizační značky, oznamovat hranice služeb a aplikovat dopřednou korekci chyb (FEC) na úrovni sekvence, čímž zvyšuje spolehlivost a snižuje latenci pro živé streamování a doručování souborů.

CVS dále řeší omezení dřívějších mechanismů pro doručování videa tím, že poskytuje základ pro pokročilé funkce jako Dynamic Adaptive Streaming over HTTP (DASH) v mobilním prostředí. Zarovnáním video sekvencí s segmenty DASH CVS usnadňuje plynulé přepínání datového toku a operace trikové reprodukce (např. rychlý posun vpřed, zpět). Jeho definice také podporuje vývoj směrem k vyšší efektivitě video kodeků (HEVC) a imerzivním médiím (např. video 360°), čímž zajišťuje zpětnou kompatibilitu a připravenost na budoucnost architektury video služeb 3GPP. CVS v podstatě existuje proto, aby sjednotil zpracování videa, vyřešil problémy fragmentace a umožnil škálovatelné doručování videa vysoké kvality napříč všemi službami 3GPP.

## Klíčové vlastnosti

- Samostatná dekódovatelná jednotka začínající přístupovou jednotkou IDR nebo BLA
- Umožňuje náhodný přístup a čisté přepínání mezi video proudy
- Základní struktura pro adaptivní streamování s proměnným datovým tokem (např. DASH) v mobilních sítích
- Klíčová pro odolnost proti chybám a prevenci šíření chyb mezi sekvencemi
- Podporuje vysílací/multicastové služby (MBMS/eMBMS) pro efektivní doručování obsahu
- Usnadňuje synchronizaci, šifrování a správu digitálních práv (DRM) na úrovni sekvence

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.265** (Rel-19) — Video Operation Points & Capabilities
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols

---

📖 **Anglický originál a plná specifikace:** [CVS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cvs/)
