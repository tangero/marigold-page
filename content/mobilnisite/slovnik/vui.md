---
slug: "vui"
url: "/mobilnisite/slovnik/vui/"
type: "slovnik"
title: "VUI – Video Usability Information"
date: 2025-01-01
abbr: "VUI"
fullName: "Video Usability Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vui/"
summary: "VUI (Video Usability Information) je sada parametrů metadat vestavěná do videosignálu (např. H.264/AVC nebo H.265/HEVC), která popisuje charakteristiky videosignálu. Poskytuje dekodérům a displejům ne"
---

VUI je sada metadat vestavěná do videosignálu, která popisuje charakteristiky signálu, jako je barevný prostor, aby zajistila přesnou reprodukci barev na různých zařízeních.

## Popis

Video Usability Information (VUI) je standardizovaná syntaxe a sémantika definovaná ve standardech pro videokódování, zejména H.264/Advanced Video Coding ([AVC](/mobilnisite/slovnik/avc/)) a H.265/High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)), a je klíčová pro multimediální služby v 3GPP. Nejde o samotná data videokomprese, ale o pomocné informace přenášené v sadě parametrů sekvence (Sequence [Parameter](/mobilnisite/slovnik/parameter/) Set, [SPS](/mobilnisite/slovnik/sps/)) videosignálu. Parametry VUI popisují vlastnosti zdrojového videosignálu, které nelze odvodit pouze z dekódovaných hodnot pixelů, což umožňuje přijímacímu zařízení interpretovat a vykreslit videoobsah tak, jak zamýšlel tvůrce obsahu.

Z architektonického hlediska je VUI generováno na straně kodéru – serverem obsahu, mediálním kodérem nebo během převodu videa – a je zapouzdřeno v elementárním videoproudu. Když zařízení 3GPP, například smartphone, přijme videoproud (např. přes službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) nebo Packet-Switched Streaming Service ([PSS](/mobilnisite/slovnik/pss/))), jeho videodekodér extrahuje parametry VUI během parsování SPS. Tyto parametry jsou následně předány do zobrazovacího řetězce zařízení. Klíčové komponenty popsané VUI zahrnují barevné primární barvy videosignálu (chromaticitní souřadnice červené, zelené a modlé primární barvy), přenosové charakteristiky (elektro-optická přenosová funkce, jako je gama křivka nebo Perceptual Quantizer pro [HDR](/mobilnisite/slovnik/hdr/)) a maticové koeficienty (konverzní matice z nelineárního [RGB](/mobilnisite/slovnik/rgb/) na složky jasu a barvonosné složky, jako je YCbCr).

Funguje to prostřednictvím přesné signalizace. Například pole 'colour_primaries' udává, zda video používá standardní barevný gamut BT.709 (HDTV) nebo BT.2020 (Ultra HD). Pole 'transfer_characteristics' signalizuje, zda je video standardního dynamického rozsahu (SDR) používající gama křivku, nebo vysokého dynamického rozsahu (HDR) používající SMPTE ST 2084 (PQ) nebo HLG. 'matrix_coeffs' říká dekodéru, jak převést dekódované vzorky YCbCr zpět na RGB pro zobrazení. Bez těchto informací by dekodér mohl předpokládat výchozí hodnoty (často BT.709), což by vedlo k nesprávnému sytí barev, nesprávné jasu nebo vybledlým obrazům při přehrávání obsahu vytvořeného s různými parametry, jako je obsah HDR nebo s širokým barevným gamutem.

Její role v sítích 3GPP spočívá v zajištění kvality uživatelského zážitku (QoE) pro videoslužby. S vývojem mobilních sítí směrem k doručování vyššího rozlišení (4K, 8K) a obsahu HDR se správné řízení barev stalo kritickým. VUI poskytuje nezbytná metadata pro věrnost barev od konce ke konci. Umožňuje různorodým zařízením s různými možnostmi displeje (SDR, HDR10, HLG) automaticky se nakonfigurovat pro správné zobrazení videa nebo provést vhodné mapování tónů, pokud displej nemůže plně podporovat signalizované charakteristiky. To je nezbytné pro vysílací služby jako eMBMS a pro adaptivní streamování (DASH), kde může být k dispozici více reprezentací obsahu (s různým VUI).

## K čemu slouží

VUI bylo vytvořeno, aby vyřešilo problém nekonzistentního a nepřesného přehrávání videa na množství různých zařízení a displejů na trhu. Rané standardy digitálního videa často předpokládaly určité kolorimetrické konvence (jako BT.601 pro SD, BT.709 pro HD). S rozvojem tvorby videoobsahu – počítačovou grafikou, různými kamerovými systémy a vznikajícími standardy HDR – však tyto implicitní předpoklady přestaly stačit. Bez explicitní signalizace musel dekodér odhadovat záměr, což vedlo k viditelným chybám, jako je nesprávný barevný nádech (např. červené tváře) nebo neshoda jasu.

Motivace pro standardizaci VUI v kodecích jako H.264/AVC bylo poskytnout robustní mechanismus v pásmu pro přenos těchto kritických metadat pro zobrazení. Řeší omezení signalizace mimo pásmo (jako formáty kontejnerů), která může být ztracena během převodu kódování nebo přenosu. Jejím vestavěním přímo do zakódovaného videosignálu zůstává VUI neporušené ve většině zpracovatelských řetězců. Jeho přijetí do specifikací 3GPP (např. pro PSS a MBMS) bylo poháněno potřebou standardizovat doručování videa přes mobilní sítě, aby bylo zajištěno, že pokročilé funkce videa jako HDR a široký barevný gamut mohou být nasazeny spolehlivě.

Historicky její význam rostl s přechodem na HD a následně UHD. Pro 3GPP konkrétně, jelikož se Rel-13 a pozdější verze zaměřovaly na vylepšené mobilní širokopásmové připojení (eMBB) a bohaté mediální služby, začlenění podpory pro správné parsování a zpracování VUI se stalo nezbytným pro konkurenceschopnou videonabídku. Řeší problém 'vidíte to, co bylo zamýšleno' v fragmentovaném ekosystému zařízení, což umožňuje poskytovatelům obsahu a síťovým operátorům doručovat vysoce kvalitní a konzistentní zobrazovací zážitek, což je klíčový diferenciátor pro mobilní videoslužby.

## Klíčové vlastnosti

- Vestavěné v sadě parametrů sekvence (Sequence Parameter Set, SPS) videosignálu
- Signalizuje barevné primární barvy definující barevný gamut (např. BT.709, BT.2020)
- Signalizuje přenosové charakteristiky definující EOTF (např. gama, PQ, HLG)
- Signalizuje maticové koeficienty pro konverzi YUV na RGB
- Umožňuje automatickou a přesnou konfiguraci displeje na přehrávacích zařízeních
- Nezbytné pro správné vykreslení obsahu s vysokým dynamickým rozsahem (HDR) a širokým barevným gamutem (WCG)

## Související pojmy

- [HDR – High Dynamic Range](/mobilnisite/slovnik/hdr/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [VUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/vui/)
