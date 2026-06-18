---
slug: "aod"
url: "/mobilnisite/slovnik/aod/"
type: "slovnik"
title: "AOD – Azimuth Angle of Departure"
date: 2025-01-01
abbr: "AOD"
fullName: "Azimuth Angle of Departure"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aod/"
summary: "AOD (azimutální úhel odchodu) je horizontální úhel odchodu rádiového signálu vysílaného z anténního pole základnové stanice k uživatelskému zařízení. Je klíčovým parametrem v systémech 3D formování sv"
---

AOD (azimutální úhel odchodu) je horizontální úhel odchodu rádiového signálu vysílaného z anténního pole základnové stanice k uživatelskému zařízení, používaný pro přesné formování svazku v mobilních sítích.

## Popis

Azimuth Angle of Departure (AOD) je základní prostorový parametr v 3GPP kanálovém modelu, konkrétně definovaný v rámci 3D prostorového kanálového modelu ([SCM](/mobilnisite/slovnik/scm/)) a jeho vývoje do modelů s klastrovaným zpožděním ([CDL](/mobilnisite/slovnik/cdl/)) pro New Radio (NR). Představuje horizontální úhel, měřený v azimutální rovině, pod kterým rádiový signál opouští vysílací anténní pole základnové stanice (gNB) směrem ke konkrétnímu uživatelskému zařízení (UE) nebo ke klastru rozptylovačů. Azimutální rovina je definována vzhledem k referenčnímu směru, typicky k čelnímu směru anténního pole, s úhly měřenými ve stupních. Ve standardizovaných kanálových modelech (např. TR 38.901) je AOD statistický parametr spojený s každou šířovou cestou nebo klastrem v rámci realizace vícecestného kanálu. Je to kritický vstup pro generování kanálových koeficientů, které definují prostorové charakteristiky rádiového spoje.

Technická specifikace AOD je úzce integrována s geometrií anténního pole a celkovým rámcem modelování kanálu. Pro rovinné rovnoměrné pole ([UPA](/mobilnisite/slovnik/upa/)) běžně používané v nasazeních Massive [MIMO](/mobilnisite/slovnik/mimo/) definuje AOD spolu se zenitovým úhlem odchodu ([ZOD](/mobilnisite/slovnik/zod/)) směrový vektor odcházejícího signálu v trojrozměrném prostoru. Tento vektor se používá k výpočtu fázových posunů, které signál zažívá na různých anténních prvcích v poli. Tyto fázové posuny jsou zásadní pro konstrukci vektoru odezvy anténního pole (nebo směrovacího vektoru) pro vysílač. Kombinace AOD a ZOD umožňuje systému modelovat a využívat plnou 3D prostorovou doménu, což umožňuje techniky jako elevace formování svazku a full-dimension MIMO (FD-MIMO).

V systémovém provozu a návrhu algoritmů je znalost nebo odhad AOD nezbytná pro správu svazků a formování svazku. gNB může použít informace o AOD, často odvozené z průzkumu uplink kanálu (např. pomocí Sounding Reference Signals - [SRS](/mobilnisite/slovnik/srs/)) za předpokladu reciprocity kanálu, nebo z explicitní zpětné vazby UE, k nasměrování svých vysílacích svazků. Výpočtem předkódovacích vah na základě odhadnutých AOD pro různá UE může gNB přesně směrovat energii signálu k zamýšleným uživatelům (zisk formování svazku) a vytvářet prostorové nuly vůči spolunaplánovaným uživatelům, aby zmírnil víceuživatelskou interferenci. To je operační princip prostorového dělení více přístupů ([SDMA](/mobilnisite/slovnik/sdma/)). Přesnost odhadu AOD přímo ovlivňuje výkon těchto algoritmů formování svazku, což ovlivňuje klíčové metriky jako poměr signálu k interferenci a šumu ([SINR](/mobilnisite/slovnik/sinr/)) a celkovou propustnost buňky.

Z pohledu standardizace a testování je AOD definovaným výstupem 3GPP kanálového modelu pro simulace na úrovni spoje i systému. Specifikace jako 38.901 (kanálový model) a 38.811 (studie o NR pro podporu non-terestriálních sítí) podrobně popisují statistická rozdělení (např. Laplacovo) a korelační vlastnosti pro AOD v různých šířových scénářích (např. Urban Macro, Indoor Office). Tyto modely zajišťují konzistentní a reprodukovatelné hodnocení výkonu pro zařízení a algoritmy NR v celém odvětví. Dále je AOD součástí definice prostorové konzistence v rámci kanálového modelu, což znamená, že AOD pro UE se mění korelovaným způsobem, když se UE pohybuje, což je klíčové pro přesné simulace procedur mobility a sledování svazku.

## K čemu slouží

Specifikace a využití Azimuth Angle of Departure (AOD) řeší základní výzvu modelování a využití prostorového rozměru rádiového kanálu v MIMO systémech, což se stalo kriticky důležitým s příchodem LTE-Advanced a NR. Rané MIMO systémy se primárně zaměřovaly na relativně malá anténní pole (např. 2x2, 4x4) a často používaly zjednodušené kanálové modely, které explicitně neoddělovaly azimutální a elevanční úhly. Tento přístup byl nedostatečný pro modelování chování rozsáhlých anténních polí (Massive MIMO) a pro umožnění pokročilých technik 3D formování svazku, které slibují masivní zisky v kapacitě a pokrytí sítě.

Explicitní definice AOD v rámci 3GPP rámce 3D kanálového modelu (zavedeného přibližně v Rel-12 pro LTE a upevněného pro NR) byla motivována potřebou přesné predikce výkonu a vývoje algoritmů pro FD-MIMO. Předchozí přístupy používající všesměrové nebo dvourozměrné kanálové modely nemohly zachytit realistické šířové efekty a potenciál formování svazku anténních polí s mnoha prvky uspořádanými v horizontální i vertikální dimenzi. Poskytnutím standardizované, matematicky rigorózní definice AOD (a jeho protějšku, ZOD) umožnila 3GPP výrobcům zařízení a výzkumníkům vyvíjet, testovat a porovnávat algoritmy formování svazku a předkódování pod společnou sadou realistických předpokladů. Tato standardizace byla nezbytná pro zajištění interoperability a nasměrování ekosystému k vysoce výkonným implementacím.

Konečným účelem definice AOD je odemknout výhody prostorového multiplexování a formování svazku. Přesným charakterizováním směru, ze kterého signály opouštějí základnovou stanici, může síťové zařízení vytvářet užší, více zaměřené svazky. To koncentruje vyzařovanou energii směrem k zamýšlenému uživateli, zlepšuje sílu přijímaného signálu (rozšíření pokrytí) a snižuje přelévání interference do sousedních buněk. Současně umožňuje opakované použití stejných časově-frekvenčních zdrojů pro více uživatelů oddělených v prostoru (SDMA), což dramaticky zvyšuje spektrální účinnost. AOD tedy není jen modelovou abstrakcí, ale základním parametrem, který umožňuje praktickou realizaci slibů vysoké datové rychlosti, nízké latence a vysoké hustoty připojení 5G NR a dalších generací.

## Klíčové vlastnosti

- Definuje horizontální úhel odchodu rádiového signálu v 3D prostorovém kanálovém modelu
- Jádrový parametr pro generování vektorů odezvy (směrování) anténního pole na vysílači
- Umožňuje přesný výpočet fázových rozdílů na anténních prvcích pro formování svazku
- Statisticky modelován (např. Laplacovo rozdělení) podle šířového scénáře v 3GPP TR 38.901
- Nezbytný pro modelování prostorové konzistence v kanálových simulacích pro mobilní scénáře
- Používá se spolu se zenitovým úhlem odchodu (ZOD) pro plnou 3D směrovou charakterizaci

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

📖 **Anglický originál a plná specifikace:** [AOD na 3GPP Explorer](https://3gpp-explorer.com/glossary/aod/)
