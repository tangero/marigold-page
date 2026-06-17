---
slug: "hrtf"
url: "/mobilnisite/slovnik/hrtf/"
type: "slovnik"
title: "HRTF – Head-Related Transfer Function"
date: 2025-01-01
abbr: "HRTF"
fullName: "Head-Related Transfer Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hrtf/"
summary: "HRTF je matematická funkce, která popisuje, jak je zvuk z bodu v prostoru filtrován tvarem hlavy, uší a trupu posluchače před dopadem na bubínek. V 3GPP je standardizována pro vytváření ponořujících p"
---

HRTF je standardizovaná matematická funkce, která popisuje, jak je zvuk filtrován anatomii posluchače, aby umožnila ponořující prostorový zvuk, jako je 3D audio, v multimediálních službách 3GPP.

## Popis

Head-Related Transfer Function (HRTF) je soubor akustických filtrů, které charakterizují směrem závislé spektrální modifikace, jež jsou zvukové vlně vnuceny anatomickými rysy jedince – především boltci (vnější uši), hlavou a trupem. Pro danou polohu zdroje zvuku (definovanou úhly azimutu a elevace) se HRTF skládá ze dvou složek: pro levé ucho (HRTF_L) a pro pravé ucho (HRTF_R). Tyto funkce modelují efekty difrakce, odrazu a rezonance zvuku, které vytvářejí interaurální časové rozdíly ([ITD](/mobilnisite/slovnik/itd/)), interaurální úrovňové rozdíly ([ILD](/mobilnisite/slovnik/ild/)) a spektrální signály, které lidský mozek používá k lokalizaci zvuku v trojrozměrném prostoru.

V rámci standardů 3GPP se HRTF využívá v audiokodecích a vykreslovacích enginech k syntéze binaurálního zvuku. Proces spočívá v tom, že se monofonní nebo vícekanálový audio signál konvoluje s příslušným párem HRTF filtrů odpovídajícím požadované virtuální pozici zdroje zvuku. Tím se vygeneruje binaurální signál, který při přehrávání přes standardní sluchátka vytváří iluzi, že zvuky přicházejí ze specifických míst kolem posluchače, což umožňuje ponořující 3D audio zážitky. Specifikace 3GPP, zejména v sérii TS 26.xxx (Kodek pro audio a video), definují profily, formáty a postupy pro přenos a aplikaci HRTF dat v multimediálních službách.

Technická implementace zahrnuje ukládání HRTF datových sad, které mohou být generické (založené na průměrném člověku nebo umělé hlavě) nebo personalizované. Tyto sady používají mediální přehrávače nebo audio procesorové jednotky v zařízeních. V síťových kontextech, například u Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) nebo ponořující telekonference, lze HRTF zpracování použít k vytváření prostorových audio míchání, což umožní posluchači rozlišit více vzdálených mluvčích, jako by byli na různých pozicích ve virtuální místnosti. To výrazně zvyšuje realističnost a srozumitelnost komunikačních a zábavních služeb.

## K čemu slouží

Technologie HRTF byla integrována do standardů 3GPP, aby řešila omezení tradičního stereo nebo mono audia v poskytování realistických, ponořujících zvukových scén pro mobilní multimédia a komunikaci. Ploché, neprostorové audio nedokáže přenést přirozené akustické prostředí, což je klíčové pro aplikace jako virtuální realita (VR), rozšířená realita ([AR](/mobilnisite/slovnik/ar/)), pokročilé hraní her a ponořující teleprezence. Hlavní problém, který HRTF řeší, je umožnění věrohodné 3D audio lokalizace přes standardní dvoukanálová sluchátka, což je zásadní pro vytvoření pocitu přítomnosti.

Motivace pro standardizaci vyplynula z rostoucího trhu s obohacenými mediálními službami a potřebou interoperability. Definováním společných formátů a zpracovatelských metod pro HRTF data v rámci multimediálních kodeků (jako je [EVS](/mobilnisite/slovnik/evs/)) a souborových formátů (jako je 3GPP [DASH](/mobilnisite/slovnik/dash/)) zajišťuje 3GPP, že prostorový audio obsah vytvořený jedním poskytovatelem služeb může být přesně vykreslen na jakémkoli kompatibilním zařízení. To odemyká nové uživatelské zážitky pro mobilní sítě, které přesahují pouhé hlasové hovory a stereo hudbu směrem k plně ponořujícímu zvuku, jenž obohacuje vyprávění příběhů, komunikaci a zábavu.

## Klíčové vlastnosti

- Matematický model akustického filtrování lidskou anatomií pro lokalizaci zvuku
- Umožňuje binaurální vykreslování 3D audia přes standardní sluchátka
- Definováno v 3GPP pro interoperabilitu v ponořujících multimediálních službách
- Může být generické nebo personalizované pro přesnější prostorové vnímání
- Integruje se s kodeky jako EVS pro prostorové komunikační služby
- Poskytuje signály jako interaurální časový rozdíl (ITD) a spektrální tvarování

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.251** (Rel-19) — IVAS Codec Fixed-Point C Code Specification
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.254** (Rel-19) — IVAS Rendering Functions Specification
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report
- **TR 26.950** (Rel-19) — Surround Sound in 3GPP Services Study
- **TR 26.997** (Rel-19) — IVAS Codec Specification

---

📖 **Anglický originál a plná specifikace:** [HRTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/hrtf/)
