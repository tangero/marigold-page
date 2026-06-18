---
slug: "zoa"
url: "/mobilnisite/slovnik/zoa/"
type: "slovnik"
title: "ZOA – Zenith angle Of Arrival"
date: 2025-01-01
abbr: "ZOA"
fullName: "Zenith angle Of Arrival"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/zoa/"
summary: "Parametr pro modelování kanálu reprezentující vertikální úhel, pod kterým rádiová vlna dorazí k přijímací anténní soustavě, měřený od zenitu (svisle nad hlavou). Je klíčový pro 3D modelování kanálu, e"
---

ZOA je vertikální úhel, měřený od svislice nad hlavou, pod kterým rádiová vlna dorazí k přijímací anténní soustavě. Používá se pro 3D modelování kanálu a elevaci beamformingu v mobilních sítích.

## Popis

Zenith Angle of Arrival (ZOA) je klíčový úhlový parametr v pokročilých trojrozměrných (3D) modelech rádiového kanálu definovaných 3GPP pro 5G New Radio (NR) a novější systémy. Určuje vertikální úhel příchodu multipath komponenty (paprsku nebo klastru) k přijímací anténní soustavě. Geometricky se měří ve stupních mezi přímkou od přijímače k přicházející vlně a zenitovou osou, která směřuje svisle vzhůru z lokálního souřadnicového systému přijímače. ZOA 0° značí vlnu přicházející přímo ze svislice nad hlavou, zatímco 90° značí příchod z horizontální roviny. Tento parametr, v kombinaci s Azimuth Angle of Arrival ([AOA](/mobilnisite/slovnik/aoa/)), poskytuje úplný sférický popis směru příchodu.

V rámci architektury 3GPP kanálového modelu (např. TR 38.901) je ZOA stochastický parametr generovaný pro každý šířicí klastr a subcestu. Model definuje statistická rozdělení pro ZOA, jako je Laplacovo nebo obalové Gaussovo rozdělení, s průměrným zenitovým úhlem (např. navázaným na elevaci dominantní cesty klastru) a specifickým úhlovým rozptylem. Tato rozdělení jsou odvozena z rozsáhlých měřících kampaní kanálů v různých prostředích (Urban Macro, Indoor Office atd.). Model tyto úhly generuje, aby realisticky simuloval, jak se rádiové vlny šíří, odrážejí a difraktují na budovách a terénu, a nakonec dopadají na přijímač z různých vertikálních směrů.

Jeho fungování v návrhu a evaluaci systémů je zásadní pro [MIMO](/mobilnisite/slovnik/mimo/) a beamforming. Moderní základnové stanice využívají rozsáhlé dvourozměrné anténní soustavy s prvky rozmístěnými horizontálně i vertikálně. Parametr ZOA přímo ovlivňuje návrh vertikálního anténního vyzařovacího diagramu a výpočet vektoru odezvy soustavy pro každou přicházející cestu. To umožňuje simulaci a implementaci 3D beamformingu, kde lze svazky nasměrovat nejen horizontálně (azimut), ale také v elevaci. Role ZOA je proto kritická pro hodnocení výkonu technologií jako Full Dimension MIMO (FD-MIMO) a Massive MIMO, které se spoléhají na přesnou prostorovou informaci o kanálu k nasměrování energie k uživatelům, správě mezibuněčného rušení ve vertikální doméně a podpoře víceuživatelského multiplexování v trojrozměrném prostoru.

## K čemu slouží

Parametr ZOA byl zaveden, aby řešil omezení tradičních dvourozměrných (2D) kanálových modelů, které uvažovaly pouze azimutální úhly. S vývojem celulárních sítí směrem k 4G LTE-Advanced a 5G začaly základnové stanice nasazovat anténní soustavy s vertikálními prvky, aby využily elevaci. Stávající 2D modely byly pro návrh a evaluaci těchto 3D beamformingových technik nedostatečné, protože nedokázaly charakterizovat vertikální rozptyl a směr přicházejících signálů, což je klíčové pro výkon v městských kaňonech a s výškovými budovami.

Jeho vytvoření v 3GPP Release 14 bylo motivováno snahou průmyslu o FD-MIMO a potřebou přesné predikce výkonu pro 3D nasazení sítí. Standardizované kanálové modely zahrnující ZOA (a jeho protějšek, Zenith Angle of Departure - [ZOD](/mobilnisite/slovnik/zod/)) řeší problém nerealistické simulace, která nadhodnocuje výkon systému. Umožňují výrobcům zařízení a operátorům přesně navrhovat algoritmy náklonu antén, hodnotit pokrytí buňky ve vertikální rovině a optimalizovat víceuživatelské plánování pro uživatele umístěné v různých výškách (např. úroveň terénu vs. vysoká patra). To umožňuje praktickou realizaci zisků v kapacitě a pokrytí slibovaných 3D-MIMO, což bylo klíčové vylepšení pro 5G NR k podpoře různorodých scénářů nasazení a distribuce uživatelů.

## Klíčové vlastnosti

- Definuje vertikální úhel příchodu rádiové vlny vzhledem k zenitu
- Klíčový vstup pro 3D prostorové kanálové modely (např. 3GPP TR 38.901)
- Statisticky modelován specifickými rozděleními a úhlovými rozptyly podle prostředí
- Zásadní pro výpočet vertikální odezvy soustavy u 2D anténních polí
- Umožňuje realistickou simulaci a evaluaci elevace beamformingu a FD-MIMO
- Funguje v součinnosti s Azimuth Angle of Arrival (AOA) pro úplný sférický směr

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

📖 **Anglický originál a plná specifikace:** [ZOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/zoa/)
