---
slug: "v-pcc"
url: "/mobilnisite/slovnik/v-pcc/"
type: "slovnik"
title: "V-PCC – Video-based Point Cloud Compression"
date: 2025-01-01
abbr: "V-PCC"
fullName: "Video-based Point Cloud Compression"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/v-pcc/"
summary: "Standardizovaný kodek 3GPP pro efektivní kompresi dynamických 3D dat bodového mračna využitím technologie video kódování. Převádí 3D prostorová a atributová data na 2D videosledy, což umožňuje vysoko"
---

V-PCC je standardizovaný kodek 3GPP, který komprimuje dynamická 3D data bodového mračna jejich převodem na 2D videosledy za účelem efektivního streamování imerzivního objemového obsahu.

## Popis

Video-based Point Cloud Compression (V-PCC) je kompresní standard vyvinutý 3GPP, specifikovaný v sérii 26.9xx (např. TS 26.928), pro dynamická data bodového mračna. Bodové mračno je soubor datových bodů v 3D souřadnicovém systému, reprezentující povrchovou geometrii objektu nebo scény, často doplněný o atributy jako barva a odrazivost. V-PCC řeší problém obrovské velikosti dat takových objemových reprezentací pomocí 'video-based' přístupu. Hlavní myšlenkou je promítnutí 3D dat bodového mračna na 2D roviny, čímž se generují geometrické a texturní videosledy, které lze komprimovat pomocí stávajících, vysoce účinných videokodeků jako [HEVC](/mobilnisite/slovnik/hevc/) (H.265) nebo [VVC](/mobilnisite/slovnik/vvc/) (H.266).

Proces kódování V-PCC zahrnuje několik klíčových kroků. Nejprve je bodové mračno segmentováno na pláty – spojité oblasti povrchu. Tyto pláty jsou následně zabaleny do 2D geometrických a atributových (např. barevných) obrazů. Balící algoritmus se snaží minimalizovat nevyužitý prostor a respektovat hranice plátů. Geometrický obraz kóduje informace o hloubce každého bodu vzhledem k promítací rovině. Tyto vygenerované 2D obrazové sekvence (geometrické video a atributové video) jsou vloženy do standardního video kodéru. Pomocné informace, jako jsou metadata plátů, promítací parametry a mapy obsazenosti (udávající, které pixely v zabaleném obraze odpovídají skutečným bodům), jsou také generovány a komprimovány samostatně, často pomocí aritmetického kódování.

Na straně dekodéru je proces obrácen. Videobitové toky jsou dekódovány pro rekonstrukci 2D geometrických a atributových obrazů. Pomocí dekódovaných pomocných informací dekodér rozbalí pláty a zpětně promítne pixely z 2D obrazů do 3D prostoru, čímž rekonstruuje geometrii a barvy původního bodového mračna. V-PCC podporuje jak ztrátové, tak bezztrátové kompresní režimy a dokáže zpracovávat dynamicky se měnící bodová mračna (sekvence snímků) pro objemové video. Jeho integrace do standardů 3GPP umožňuje streamování těchto složitých dat přes mobilní sítě, protože komprimovaný bitový tok může být zabalen a doručen pomocí stávajících rámců pro doručování multimédií jako [DASH](/mobilnisite/slovnik/dash/) nebo [MMS](/mobilnisite/slovnik/mms/), což z něj činí základní technologii pro novou generaci služeb imerzivních médií.

## K čemu slouží

V-PCC byl standardizován, aby umožnil praktické šíření a komunikaci v reálném čase vysoce věrných 3D objemových obsahů přes sítě s omezenou šířkou pásma, zejména mobilní sítě. Před jeho vývojem vyžadovala data bodového mračna, zejména pro dynamické scény, pro přenos nepřiměřeně vysoké bitové toky, což činilo aplikace jako 6 Degrees of Freedom (6DoF) imerzivní video, holografická teleprezence a sdílení [AR](/mobilnisite/slovnik/ar/)/[VR](/mobilnisite/slovnik/vr/) nerealizovatelnými pro masovou spotřebu. Stávající metody komprese 3D sítí nebo obecné metody komprese bodových mračen nebyly optimalizovány pro dynamický obsah nebo nebyly dostatečně účinné pro bezdrátový přenos.

Vytvoření V-PCC, s prací začínající ve verzi 16, bylo přímo motivováno posunem průmyslu směrem k imerzivním médiím jako klíčovému případu užití 5G. 3GPP uznalo, že pro naplnění slibu 5G v podobě rozšířeného mobilního širokopásmového připojení (eMBB) a masivních mediálních služeb je nezbytný standardizovaný, účinný kodek pro objemové video. Chytrým znovuvyužitím obrovské kompresní účinnosti desetiletí výzkumu video kódování (prostřednictvím [HEVC](/mobilnisite/slovnik/hevc/)/[VVC](/mobilnisite/slovnik/vvc/)) poskytuje V-PCC pragmatické a vysoce efektivní řešení. Řeší problém interoperability, což umožňuje tvůrcům obsahu, síťovým operátorům a výrobcům zařízení spoléhat se na jedinou, dobře specifikovanou kompresní technologii pro bodová mračna, čímž urychluje ekosystém pro imerzivní zážitky na mobilních zařízeních.

## Klíčové vlastnosti

- Využívá stávající videokodeky (HEVC, VVC) pro kompresi 3D geometrie a textury
- Podporuje sekvence dynamických bodových mračen (objemové video)
- Na plátech založená projekce a balení 3D dat do 2D obrazů
- Zahrnuje kompresi pomocných informací pro metadata a mapy obsazenosti
- Podporuje škálovatelné a progresivní kompresní režimy
- Umožňuje integraci s protokoly pro doručování médií 3GPP (např. DASH)

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [V-PCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-pcc/)
