---
slug: "foa"
url: "/mobilnisite/slovnik/foa/"
type: "slovnik"
title: "FOA – First Order Ambisonics"
date: 2025-01-01
abbr: "FOA"
fullName: "First Order Ambisonics"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/foa/"
summary: "Prostorový audio formát standardizovaný organizací 3GPP pro imerzivní mediální služby, jako je VR a 360° video. Reprezentuje zvukové pole pomocí čtyř audio kanálů (W, X, Y, Z), což umožňuje plnosféric"
---

FOA je prostorový audio formát standardizovaný organizací 3GPP, který využívá čtyři kanály (W, X, Y, Z) k reprezentaci plnosférického zvukového pole pro imerzivní média, jako je VR a 360° video.

## Popis

First Order Ambisonics (FOA) je metoda pro snímání, zpracování a reprodukci trojrozměrného prostorového zvuku. V rámci 3GPP byl standardizován jako základní audio formát pro imerzivní mediální služby, podrobně popsaný napříč specifikacemi jako TS 26.118 ([VR](/mobilnisite/slovnik/vr/) profily) a TS 26.260 (specifika audio kodeků). FOA reprezentuje zvukové pole v bodě prostoru pomocí souboru sférických harmonických složek prvního řádu. Prakticky to vede ke čtyřkanálovému audio signálu: jednomu všesměrovému (W) kanálu a třemi osmičkovým směrovým kanálům (X, Y, Z) orientovaným podle kartézských os.

Technicky kanál W zachycuje celkový tlak (mono audio), zatímco kanály X, Y a Z zachycují gradienty tlaku podél příslušných os, čímž kódují směrovost zvukových zdrojů. Při přehrávání jsou tyto čtyři kanály dekódovány na základě orientace hlavy posluchače (poskytované údaji o sledování hlavy) a vykresleny pro sluchátka nebo soustavu reproduktorů, čímž vzniká iluze zvuků přicházejících z konkrétních směrů v 3D prostoru. Klíčovou vlastností Ambisonics je její rotační invariance; matematická rotace zvukového pole je přímočará, což je zásadní pro VR, kde se hlava uživatele neustále pohybuje.

V architektuře 3GPP pro imerzivní média jsou FOA audio proudy typicky zabaleny v rámci segmentů dynamického adaptivního streamování přes [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)) a synchronizovány s 360° videem. Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) obsahuje metadata popisující audio jako FOA. Mediální přehrávač klienta, často součást aplikace rozšířené reality ([XR](/mobilnisite/slovnik/xr/)), přijímá údaje o orientaci hlavy ze senzorů, dekóduje FOA signály ve formátu B a provádí binaurační vykreslování pro výstup do sluchátek, čímž vytváří přesvědčivou 3D audio scénu odpovídající vizuálnímu pohledu. Tato integrace je klíčová pro zachování audiovizuální koherence a zvýšení pocitu přítomnosti ve virtuálních prostředích.

## K čemu slouží

FOA byla standardizována v 3GPP, aby řešila kritickou potřebu imerzivního prostorového zvuku pro nové mediální služby, jako je virtuální realita ([VR](/mobilnisite/slovnik/vr/)), rozšířená realita ([AR](/mobilnisite/slovnik/ar/)) a 360° video. Tradiční stereo nebo surround formáty (např. 5.1) jsou uzamčeny na perspektivu tvůrce obsahu a nepřizpůsobují se pohybu hlavy uživatele, což narušuje imerzi v interaktivních VR zážitcích. Hlavním problémem byl nedostatek standardizovaného, efektivního a adaptabilního formátu pro 3D audio v telekomunikacích.

Motivace pro jeho zařazení, počínaje Release 14, byla hnací silou snahy průmyslu směrem k imerzivním médiím. Práce 3GPP na VR profilech a mediálních kodecích identifikovala prostorový zvuk jako základní komponentu. FOA byla zvolena, protože poskytuje dobrou rovnováhu mezi kvalitou zvuku, výpočetní složitostí a efektivitou přenosového toku ve srovnání s Ambisonics vyššího řádu ([HOA](/mobilnisite/slovnik/hoa/)) nebo objektovým audiem. Řeší omezení kanálového audia tím, že poskytuje plnosférickou reprezentaci, která je nezávislá na konfiguraci reproduktorů přehrávacího systému a může být dynamicky rotována.

Historicky existovaly proprietární nebo výzkumné formáty, ale pro interoperabilitu mezi nástroji pro tvorbu obsahu, streamovacími službami a přehrávacími zařízeními byl potřeba univerzální standard. Standardizace FOA organizací 3GPP umožnila masové nasazení VR služeb s působivým audiem a zajišťuje, že zvukové zdroje zůstávají pevné ve virtuálním světě, když se uživatel rozhlíží, což je zásadní pro realismus a uživatelský komfort v aplikacích XR.

## Klíčové vlastnosti

- Kóduje plné 3D zvukové pole pomocí čtyř audio kanálů (W, X, Y, Z ve formátu B)
- Poskytuje rotační invarianci, umožňující rotaci zvukového pole v reálném čase na základě sledování hlavy
- Umožňuje efektivní binaurační vykreslování pro přehrávání do sluchátek, čímž vytváří personalizované 3D audio
- Standardizován pro interoperabilitu v imerzivním mediálním streamování 3GPP (např. DASH-IF IOP)
- Podporuje škálovatelné přenosové toky a může být komprimován pomocí kodeků jako EVS nebo MPEG-H 3D Audio
- Tvoří základ pro složitější prostorové audio formáty, jako je Ambisonics vyššího řádu (HOA)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TR 26.997** (Rel-19) — IVAS Codec Specification

---

📖 **Anglický originál a plná specifikace:** [FOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/foa/)
