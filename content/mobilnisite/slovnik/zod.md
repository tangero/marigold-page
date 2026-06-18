---
slug: "zod"
url: "/mobilnisite/slovnik/zod/"
type: "slovnik"
title: "ZOD – Zenith angle Of Departure"
date: 2025-01-01
abbr: "ZOD"
fullName: "Zenith angle Of Departure"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/zod/"
summary: "ZOD je parametr kanálu představující vertikální úhel odchodu signálu z vysílací anténní soustavy. Je klíčový pro 3D beamforming a Massive MIMO v 5G NR, umožňuje přesné prostorové filtrování a zlepšení"
---

ZOD je parametr kanálu představující vertikální úhel odchodu signálu z vysílací anténní soustavy, klíčový pro 3D beamforming a Massive MIMO v 5G NR.

## Popis

Zenith angle Of Departure (ZOD) je klíčový parametr v 3GPP kanálovém modelu, konkrétně definovaný v rámci prostorového kanálového modelu pro New Radio (NR). Kvantifikuje vertikální úhel, měřený od zenitu (přímo nad hlavou), pod kterým signál opouští vysílací anténní soustavu směrem ke scatterovacímu clusteru nebo uživatelskému zařízení (UE). Tento parametr je nedílnou součástí modelování trojrozměrného (3D) prostředí šíření, což představuje posun oproti tradičním dvourozměrným (pouze azimutálním) modelům používaným v dřívějších celulárních systémech. ZOD je statisticky charakterizován v rámci specifikací kanálového modelu, jako je TR 38.901, které definují pravděpodobnostní rozdělení, úhlové rozptyly a korelační vlastnosti pro různé scénáře nasazení (např. Urban Macro, Indoor Office).

V praktickém provozu systému je odhad ZOD zásadní pro implementaci elevace beamformingu a Full-Dimension [MIMO](/mobilnisite/slovnik/mimo/) (FD-MIMO). Základnová stanice (gNB) vybavená planární nebo válcovou anténní soustavou využívá zpětnou vazbu informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)), která může zahrnovat parametry související se ZOD, k vytváření úzkých svazků v azimutální i elevace rovině. Přesným nasměrováním energie ve vertikálním směru může síť obsloužit uživatele na různých podlažích budovy, snížit rušení do sousedních buněk a zlepšit sílu signálu pro uživatele na okraji buňky. Přesnost informace o ZOD přímo ovlivňuje výkon pokročilých víceanténních technik.

Parametr je odvozen z geometrie cesty šíření. Při modelování kanálu se používá clusterový přístup, kde má každý cluster sadu paprsků s konkrétními úhly. ZOD pro cluster je nominální úhel odchodu a jednotlivé paprsky v rámci clusteru mají odchylky kolem této nominální hodnoty, definované Zenith angular Spread of Departure ([ZSD](/mobilnisite/slovnik/zsd/)). Kombinace ZOD a ZSD definuje vertikální úhlovou disperzi od vysílače. Pro návrh systému a testování se tyto statistické modely používají k generování kanálových koeficientů, které přesně odrážejí reálné šíření, což zajišťuje robustnost beamforming algoritmů a návrhů přijímačů v různých prostředích.

Z perspektivy síťové architektury je zpracování zohledňující ZOD primárně řešeno na fyzické vrstvě gNB a v funkcích správy rádiových zdrojů. Algoritmy pro odhad kanálu, precoding a správu svazků musí brát vertikální dimenzi v úvahu. Použití ZOD umožňuje efektivnější prostorové multiplexování, což umožňuje současnou obsluhu více uživatelů na stejném časově-frekvenčním zdroji jejich separací v elevaci. To je základním kamenem pro dosažení vysoké spektrální účinnosti a masivní konektivity, což jsou cíle systémů 5G a beyond-5G.

## K čemu slouží

Zavedení ZOD v 3GPP Release 14 bylo motivováno přechodem na sítě 5G a přijetím Massive [MIMO](/mobilnisite/slovnik/mimo/) s aktivními anténními systémy ([AAS](/mobilnisite/slovnik/aas/)). Předchozí systémy LTE primárně využívaly beamforming v horizontální (azimutální) rovině s pasivními anténami nebo omezenou vertikální sektorizací. Tento přístup byl nedostatečný pro splnění požadavků na dramatické zvýšení kapacity sítě, pokrytí v hustých městských kaňonech a podporu uživatelů rozložených vertikálně ve výškových budovách. Parametr ZOD formálně začlenil elevaci do standardizovaných kanálových modelů a návrhu systému, čímž řešil omezení 2D modelů.

Definováním ZOD umožnilo 3GPP vývoj a spravedlivé hodnocení výkonu 3D beamforming algoritmů. Vyřešilo problém neefektivního využití spektra ve vertikální doméně a poskytlo společný rámec pro výrobce a operátory k návrhu, testování a nasazení elevace beamformingu. To bylo klíčové pro odemknutí plného potenciálu AAS, kde mají antény mnoho prvků v horizontálním i vertikálním směru. Parametr umožňuje přesné modelování reálných efektů šíření, jako jsou odrazy od země a difrakce budov ve vertikální rovině, což vede k přesnějším systémovým simulacím a předvídatelnému výkonu v reálném světě.

Vytvoření ZOD bylo součástí širšího úsilí o definici plnohodnotného 3D prostorového kanálového modelu. Funguje v součinnosti s dalšími úhlovými parametry, jako je Azimuth angle Of Departure ([AOD](/mobilnisite/slovnik/aod/)), Zenith angle Of Arrival ([ZOA](/mobilnisite/slovnik/zoa/)) a jejich příslušné rozptyly. Tento komplexní model byl nezbytný pro podporu klíčových use case 5G, jako je enhanced Mobile Broadband (eMBB) v hustých městských oblastech a fixed wireless access, kde je optimální nasměrování svazku ve třech dimenzích zásadní pro dosažení vysokých datových rychlostí a konzistentního uživatelského zážitku.

## Klíčové vlastnosti

- Definuje vertikální úhel odchodu signálu vzhledem k zenitu vysílače.
- Základní parametr v 3GPP 3D prostorovém kanálovém modelu (např. TR 38.901).
- Umožňuje elevace beamforming a Full-Dimension MIMO (FD-MIMO) v 5G NR.
- Používá se pro modelování kanálové statistiky v různých scénářích nasazení (UMa, UMi, InH).
- Zlepšuje kapacitu sítě a pokrytí umožněním prostorové separace v elevaci.
- Nezbytný pro přesné systémové simulace a hodnocení výkonu víceanténních technik.

## Související pojmy

- [ZOA – Zenith angle Of Arrival](/mobilnisite/slovnik/zoa/)
- [AOD – Azimuth Angle of Departure](/mobilnisite/slovnik/aod/)
- [AOA – Azimuth Angle of Arrival](/mobilnisite/slovnik/aoa/)

## Definující specifikace

- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [ZOD na 3GPP Explorer](https://3gpp-explorer.com/glossary/zod/)
