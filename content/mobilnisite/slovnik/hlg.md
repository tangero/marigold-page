---
slug: "hlg"
url: "/mobilnisite/slovnik/hlg/"
type: "slovnik"
title: "HLG – Hybrid Log Gamma"
date: 2025-01-01
abbr: "HLG"
fullName: "Hybrid Log Gamma"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hlg/"
summary: "Standard videa s vysokým dynamickým rozsahem (HDR) podporovaný v 3GPP pro doručování médií přes mobilní sítě. Kombinuje percepční kvantizační křivku (PQ) pro vysokou světelnost s gama křivkou pro komp"
---

HLG je standard videa s vysokým dynamickým rozsahem (HDR) pro mobilní sítě, který kombinuje percepční kvantizační křivku (PQ) a gama křivky pro vylepšený kontrast a barvy při zachování kompatibility se zobrazovači se standardním dynamickým rozsahem (SDR).

## Popis

Hybrid Log Gamma (HLG) je převodní funkce pro video s vysokým dynamickým rozsahem ([HDR](/mobilnisite/slovnik/hdr/)), standardizovaná společnostmi BBC a NHK a přijatá do specifikací 3GPP pro doručování médií. Na rozdíl od HDR standardů založených na percepční kvantizační křivce (PQ) (jako HDR10 nebo Dolby Vision), které jsou absolutní a vyžadují metadata, je HLG relativní systém navržený pro vysílání a živou produkci. Definuje nelineární elektro-optickou převodní funkci ([EOTF](/mobilnisite/slovnik/eotf/)), která mapuje hodnoty videosignálu na světlo zobrazovače. Její 'hybridní' povaha vychází z kombinace: používá gama křivku (podobnou standardnímu dynamickému rozsahu/SDR) pro spodní část signálu a logaritmickou křivku pro vyšší úrovně jasu. To umožňuje, aby byly signály HLG zobrazeny s HDR efektem na kompatibilních displejích, zatímco zůstávají zobrazitelné (bez ořezání) na starších SDR displejích, což je vlastnost známá jako zpětná kompatibilita.

V kontextu 3GPP je HLG specifikována pro použití v multimediálních vysílacích a streamovacích službách. Je podporována v kodecích jako [HEVC](/mobilnisite/slovnik/hevc/) (H.265) a VVC (H.266) pro efektivní kompresi HDR obsahu. Když mediální server doručuje video stream kódovaný v HLG přes mobilní síť (např. přes [MBMS](/mobilnisite/slovnik/mbms/) nebo unicast streamování), klient zařízení interpretuje HLG signál. Na displeji s podporou HDR je plný dynamický rozsah rekonstruován, což poskytuje jasnější světla, hlubší černě a širší barevný gamut. Na SDR displeji je tonální mapování inherentně jednodušší díky gama části křivky, což vede k sledovatelnému, i když ne HDR, obrazu bez potřeby složitého zpracování metadat.

Technické specifikace v 3GPP (např. TS 26.116 pro shodu mediálních kodeků, TS 26.265 pro HEVC, TS 26.511 pro 5G mediální streamování, TS 26.955 pro MBMS) definují, jak je HLG signalizována, zapouzdřena a zpracovávána v rámci mediálního řetězce. To zahrnuje parametry barevného prostoru (typicky [BT](/mobilnisite/slovnik/bt/).2020), bitovou hloubku (často 10 bitů) a konkrétní identifikátor převodní funkce. Pro vysílací služby jako 5G Broadcast založený na LTE nebo FeMBMS poskytuje HLG praktické HDR řešení, protože jeho relativní povaha a absence povinných metadat zjednodušuje živé kódování a přenos, což jej činí vhodným pro události v reálném čase, jako je sport.

## K čemu slouží

HLG byl vyvinut, aby řešil výzvu zavedení videa s vysokým dynamickým rozsahem ([HDR](/mobilnisite/slovnik/hdr/)) do vysílacích a streamovacích ekosystémů bez narušení stávající instalované základny displejů se standardním dynamickým rozsahem (SDR). Předchozí HDR přístupy, primárně založené na PQ, vyžadovaly statická nebo dynamická metadata k popisu charakteristik masteringového displeje pro správné tonální mapování. To přidávalo složitost živé produkci a představovalo problém kompatibility: SDR displej přijímající PQ signál by bez sofistikovaného, zařízení-specifického tonálního mapování zobrazoval silně vybledlý nebo tmavý obraz. HLG to řeší použitím převodní funkce, která je vztažena k displeji, nikoli ke scéně.

Motivací pro její zařazení do 3GPP, počínaje Release 16, byl průmyslový tlak na vylepšené multimediální zážitky v 5G. Vysoká propustnost a nízká latence 5G umožňují kvalitní video služby a HDR je klíčovou součástí tohoto zlepšení kvality. Zpětná kompatibilita HLG ji učinila obzvláště atraktivní pro mobilní vysílací a multicastové služby (např. 5G Broadcast), kde jediný přenášený stream musí obsloužit heterogenní populaci zařízení, od starších smartphonů se SDR obrazovkami po nejnovější modely s HDR schopnostmi. Přijetím HLG umožnilo 3GPP poskytovatelům služeb doručovat nadřazený videozážitek schopným zařízením při zachování služby pro všechny ostatní, čímž urychlilo adopci HDR v mobilních médiích bez nutnosti kompletní obměny všech zařízení.

## Klíčové vlastnosti

- Zpětně kompatibilní HDR převodní funkce zobrazitelná na SDR displejích
- Kombinuje gama křivku (nízká světla) a logaritmickou křivku (vysoká světla)
- Nevyžaduje statická ani dynamická metadata, což zjednodušuje živou produkci
- Standardizována pro použití s kodeky HEVC/H.265 a VVC/H.266 v 3GPP
- Typicky používána s širokým barevným gamutem BT.2020 a 10bitovou hloubkou
- Vhodná pro vysílání a živé streamování přes mobilní sítě

## Související pojmy

- [HDR – High Dynamic Range](/mobilnisite/slovnik/hdr/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.265** (Rel-19) — Video Operation Points & Capabilities
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [HLG na 3GPP Explorer](https://3gpp-explorer.com/glossary/hlg/)
