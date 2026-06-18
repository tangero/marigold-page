---
slug: "roi"
url: "/mobilnisite/slovnik/roi/"
type: "slovnik"
title: "ROI – Region of Interest"
date: 2025-01-01
abbr: "ROI"
fullName: "Region of Interest"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/roi/"
summary: "Koncept v multimediálních službách, kdy je specifická prostorová nebo časová oblast v rámci mediálního obsahu identifikována pro vylepšené zpracování nebo doručování. Umožňuje efektivnější využití šíř"
---

ROI (Region of Interest) je koncept v multimediálních službách, při kterém je specifická prostorová nebo časová oblast v rámci mediálního obsahu identifikována pro vylepšené zpracování nebo prioritní doručování, aby bylo možné efektivně využívat šířku pásma při streamování.

## Popis

Region of Interest (ROI) je funkce v rámci multimediálních standardů 3GPP, zvláště relevantní pro videokódování a streamovací služby jako Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a evolved Multimedia Broadcast Multicast Service (eMBMS). Funguje tak, že umožňuje poskytovateli obsahu nebo kodéru definovat specifické prostorové oblasti v rámci snímku videa nebo časové segmenty na časové ose média, které jsou považovány za důležitější pro uživatelský zážitek. Tyto oblasti jsou následně označeny metadaty, která dávají síti a přijímacím zařízením pokyn k použití rozdílného zacházení.

Architektonicky je podpora ROI integrována do řetězce zpracování a doručování média. Ve fázi kódování mohou kodeky kompatibilní se standardy jako [HEVC](/mobilnisite/slovnik/hevc/) (H.265) nebo [AVC](/mobilnisite/slovnik/avc/) (H.264) generovat datové toky, kde určité řezy (slices) nebo dlaždice (tiles) odpovídají ROI a jsou často kódovány s vyšší věrností (např. vyšším kvantizačním parametrem). Servisní vrstva, popsaná ve specifikacích jako 23.333 ([ProSe](/mobilnisite/slovnik/prose/)) a 26.114 (kodek), definuje signalizaci a přenos metadat ROI. Tato metadata mohou být přenášena mechanismy jako Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) v Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)).

V fázi doručování, zejména pro služby vysílání/multicastu specifikované v 29.333 (MBMS) a 29.334 (MBMS Upstream), může síť tyto informace využít pro optimalizaci prostředků. Zatímco core network a RAN typicky doručují celý mediální stream, metadata ROI umožňují klientským aplikacím nebo specializovanému middleware upřednostnit prostředky pro dekódování a vykreslování pro zvýrazněnou oblast. V pokročilých implementacích by teoreticky mohla informovat o přidělování rádiových prostředků pro schémata s vrstveným kódováním, i když primární aplikace je end-to-end mezi kodérem a přehrávačem.

Jeho rolí je zvýšit vnímanou kvalitu a efektivitu ve scénářích s omezenou šířkou pásma, běžných v mobilních sítích. Zaměřením přenosových bitů na sémanticky důležitý obsah ROI zlepšuje kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) pro aplikace jako sportovní vysílání (zaměření na hráče), videokonference (zaměření na mluvčího) nebo rozšířenou realitu, aniž by úměrně zvýšilo celkovou datovou rychlost.

## K čemu slouží

Technologie ROI byla zavedena, aby řešila základní výzvu doručování videa vysoké kvality přes mobilní sítě s omezenou a proměnlivou šířkou pásma. Předchozí přístupy aplikovaly jednotnou kvalitu kódování na celé snímky videa, což je neefektivní, protože lidské vnímání upřednostňuje určité oblasti (jako tváře nebo pohybující se objekty). To vedlo buď k nadměrné spotřebě šířky pásma pro video v plné kvalitě, nebo k jednotně špatné kvalitě, když byla šířka pásma omezena.

Vytvoření ROI, formalizované v 3GPP Release 13 spolu s vylepšeními pro eMBMS a mission-critical video, bylo motivováno růstem rich media služeb a potřebou chytřejšího, na obsah reagujícího doručování. Řeší problém optimalizace kvality uživatelského zážitku v rámci daných síťových omezení. Umožněním kódování adaptivního na obsah umožňuje poskytovatelům služeb nabízet subjektivně lepší kvalitu videa při stejné datové rychlosti nebo zachovat přijatelnou kvalitu při nižších datových rychlostech, čímž zlepšuje využití kapacity sítě.

Historicky se jeho vývoj shoduje s pokrokem ve vlastnostech videokodeků a snahou průmyslu o efektivnější vysílací služby pro veřejnou bezpečnost, živé události a automobilové scénáře. Řeší omezení předchozího "univerzálního" streamování zavedením určité míry sémantického povědomí do řetězce doručování médií, čímž činí adaptivní streamování s proměnlivou datovou rychlostí inteligentnějším a optimalizovanějším pro lidské vnímání.

## Klíčové vlastnosti

- Umožňuje definovat prostorové oblasti (např. obdélníkové oblasti) nebo časové segmenty v rámci média pro prioritní kódování
- Podporuje signalizaci pomocí metadat ve streamovacích formátech jako DASH (MPD) a oznámení vysílacích služeb
- Usnadňuje efektivitu využití šířky pásma tím, že umožňuje vyšší kvalitu kódování pro ROI oproti pozadí
- Integruje se s pokročilými videokodeky (HEVC, AVC), které podporují diferenciaci kvality na základě oblasti
- Zvyšuje kvalitu uživatelského zážitku (QoE) pro aplikace jako dohledové systémy, sportovní přenosy a videokonference
- Může být použit ve spojení se škálovatelným nebo vrstveným kódováním pro plynulé snižování kvality

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [ROI na 3GPP Explorer](https://3gpp-explorer.com/glossary/roi/)
