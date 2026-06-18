---
slug: "zsd"
url: "/mobilnisite/slovnik/zsd/"
type: "slovnik"
title: "ZSD – Zenith angle Spread of Departure"
date: 2025-01-01
abbr: "ZSD"
fullName: "Zenith angle Spread of Departure"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/zsd/"
summary: "ZSD je parametr kanálového modelu, který kvantifikuje úhlové rozprostření odcházejících rádiových vln ve vertikální (zenitové) rovině od vysílače. Je klíčový pro modelování výkonu 3D MIMO a beamformin"
---

ZSD je parametr kanálového modelu, který kvantifikuje úhlové rozprostření odcházejících rádiových vln ve vertikální rovině od vysílače.

## Popis

Zenith angle Spread of Departure (ZSD) je statistický parametr definovaný v rámci 3GPP kanálových modelů, konkrétně v 3D prostorovém kanálovém modelu ([SCM](/mobilnisite/slovnik/scm/)) a jeho evoluci ke clusterovaným modelům se zpožděním ([CDL](/mobilnisite/slovnik/cdl/)). Kvantifikuje úhlovou disperzi, neboli rozprostření, vícecestných komponent opouštějících anténní pole vysílače ve vertikální (zenitové) rovině. Tento parametr není jedinou naměřenou hodnotou, ale distribuční charakteristikou používanou pro generování realistických impulsních odezev kanálu pro systémové simulace. V praxi je ZSD klíčovým vstupem pro generování kanálových koeficientů, které definují, jak se signál šíří, a zahrnuje efekty rozptylu a odrazu v prostředí, které způsobují, že signály opouštějí vysílač pod různými elevacemi.

Parametr funguje v rámci geometrických stochastických kanálových modelů. Tyto modely definují shluky (clustery) rozptylovačů, každý s přidruženými úhly odchodu (AoD) a příchodu (AoA) jak v azimutální, tak v zenitové (elevační) doméně. ZSD je úhlová směrodatná odchylka zenitových úhlů odchodu pro vícecestné komponenty uvnitř shluku nebo napříč kanálem. Větší hodnota ZSD značí větší rozprostření ve vertikálních úhlech odchodu, což je typické v prostředích s významnými výškovými variacemi, jako jsou městské kaňony nebo vnitřní budovy s více podlažími. Naopak, menší ZSD je charakteristické pro otevřenější, rovný terén. Model generuje tyto úhly podle specifikovaného rozdělení (jako je Laplacovo) s tím, že ZSD definuje rozprostření, což následně ovlivňuje směrovací vektory a nakonec kanálovou matici H.

Klíčové komponenty při využití ZSD zahrnují konfiguraci kanálového modelu (např. CDL-A, CDL-B, CDL-C), model anténního pole (specifikující vyzařovací charakteristiky prvků a jejich pozice ve 3D) a linkový nebo systémový simulátor, který počítá kanálové koeficienty. Role ZSD je klíčová pro vyhodnocení výkonu Multi-User [MIMO](/mobilnisite/slovnik/mimo/) ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)) a beamformingových algoritmů, zejména pro Full Dimension MIMO (FD-MIMO) a massive MIMO systémy, které využívají anténní pole s vertikálními prvky. Přímo ovlivňuje metriky jako beamformingový zisk, schopnost prostorového multiplexování a interferenci mezi uživateli v elevační doméně. Přesným modelováním ZSD mohou inženýři vyhodnotit, jak dobře dokáže vertikální beamforming základnové stanice oddělit uživatele v různých výškách nebo podlažích, což je zásadní pro optimalizaci kapacity a pokrytí v moderních 3D sítích.

## K čemu slouží

ZSD byl zaveden, aby řešil omezení dřívějších 2D kanálových modelů, které uvažovaly pouze azimutální (horizontální) úhlové rozprostření. Jak se mobilní sítě vyvíjely směrem k LTE-Advanced a 5G NR, začalo být běžné používání aktivních anténních systémů ([AAS](/mobilnisite/slovnik/aas/)) s dvourozměrnými anténními poli. Tyto systémy umožnily beamforming a [MIMO](/mobilnisite/slovnik/mimo/) operace nejen v horizontální rovině, ale také ve vertikální (elevační) rovině, což je technologie známá jako 3D nebo elevační beamforming. Stávající kanálové modely byly pro vyhodnocení těchto pokročilých technik nedostatečné, protože jim chyběly parametry pro charakterizaci vertikálních úhlových vlastností prostředi šíření.

Vytvoření ZSD, spolu s jeho protějškem Zenith angle Spread of Arrival ([ZSA](/mobilnisite/slovnik/zsa/)), bylo motivováno potřebou realistického vyhodnocení výkonu FD-MIMO a massive MIMO v rámci standardizace a vývoje produktů. Bez přesných parametrů vertikálního úhlového rozprostření by byly systémové simulace příliš optimistické nebo pesimistické, což by vedlo k chybným závěrům o beamformingových ziscích, výhodách dělení buněk a řízení víceuživatelské interference v elevační doméně. Začleněním ZSD do 3GPP kanálových modelů počínaje Release 14 poskytl standardizační orgán jednotnou a ověřenou metodologii pro průmysl, aby mohl benchmarkovat a porovnávat výkon pokročilých anténních systémů za realistických 3D podmínek šíření, což je klíčové pro plánování sítí v hustých městských a vnitřních scénářích.

## Klíčové vlastnosti

- Kvantifikuje vertikální úhlovou disperzi odcházejících vícecestných komponent
- Definován jako statistický parametr (např. úhlová směrodatná odchylka) ve stochastických kanálových modelech
- Klíčový vstup pro generování 3D kanálových koeficientů v CDL a SCM modelech
- Závislý na prostředí, s hodnotami specifikovanými pro scénáře jako UMi, UMa, RMa a InH
- Nezbytný pro realistickou simulaci elevačního beamformingu a vertikální sektorizace
- Přímo ovlivňuje modelování mezivrstvové a meziuživatelské interference v 3D MIMO systémech

## Související pojmy

- [ZSA – Zenith angle Spread of Arrival](/mobilnisite/slovnik/zsa/)
- [ASA – Azimuth Spread of Arrival](/mobilnisite/slovnik/asa/)
- [ASD – Azimuth Spread of Departure](/mobilnisite/slovnik/asd/)

## Definující specifikace

- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [ZSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/zsd/)
