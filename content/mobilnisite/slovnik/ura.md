---
slug: "ura"
url: "/mobilnisite/slovnik/ura/"
type: "slovnik"
title: "URA – Uniform Rectangular Array"
date: 2025-01-01
abbr: "URA"
fullName: "Uniform Rectangular Array"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ura/"
summary: "Konkrétní konfigurace anténního pole, kde jsou anténní prvky uspořádány v rovnoměrné obdélníkové mřížce. Umožňuje pokročilé beamforming a MIMO techniky tím, že poskytuje kontrolu nad azimutovou i elev"
---

URA je konkrétní konfigurace anténního pole, kde jsou prvky uspořádány v rovnoměrné obdélníkové mřížce, aby umožnila pokročilé beamforming a MIMO díky poskytnutí kontroly nad azimutovou i elevací rovinou.

## Popis

Uniform Rectangular Array (URA) je základní anténní architektura používaná v moderních bezdrátových komunikačních systémech, zejména definovaná ve standardech 3GPP pro pokročilé anténní systémy ([AAS](/mobilnisite/slovnik/aas/)). Skládá se z více anténních prvků – typicky duálně polarizovaných – uspořádaných ve dvourozměrné mřížce s rovnoměrným rozestupem ve vodorovném i svislém směru. Tato geometrická struktura tvoří planární pole, což je klíčová fyzická realizace pro nasazení massive [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) a beamformingu. URA není jen fyzickým pouzdrem, ale definovanou logickou strukturou, která komunikuje s jednotkami základnového pásma (baseband) a umožňuje prostorové zpracování signálu.

Provozně URA funguje tak, že umožňuje síti aplikovat komplexní váhové vektory (prekódovací matice) na signály přiváděné na každý anténní prvek. Manipulací s fází a amplitudou těchto signálů napříč polem může systém vytvářet vysoce směrové paprsky v trojrozměrném prostoru. Obdélníková mřížka umožňuje nezávislé řízení jak v azimutové (vodorovné), tak v elevaci (svislé) oblasti, což je schopnost známá jako full-dimension MIMO (FD-MIMO) nebo 3D beamforming. To je významný pokrok oproti lineárním polím, která primárně ovládají azimutovou rovinu. Výkon pole je charakterizován parametry jako počet prvků na řádek (M) a na sloupec (N), rozestup mezi prvky (typicky polovina vlnové délky) a konfigurace polarizace.

Ve vrstvách protokolu 3GPP je URA nedílnou součástí specifikací fyzické vrstvy, zejména pro získávání a hlášení informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)). UE měří referenční signály (např. [CSI-RS](/mobilnisite/slovnik/csi-rs/)) vysílané z URA a hlásí zpět preferované indexy paprsků a kvalitu kanálu. gNB používá tuto zpětnou vazbu k výběru optimálních prekódovačů pro downlinkový přenos. Specifikace definují kodebóky – předdefinované sady beamformingových vektorů – přizpůsobené geometrii URA pro efektivní kvantizaci informací o beamformingu. Architektura URA přímo podporuje multi-user MIMO ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)), kde jsou stejné časově-frekvenční zdroje sdíleny mezi více UE pomocí prostorově separovatelných paprsků, čímž se násobí kapacita sítě.

Klíčovými součástmi systému založeného na URA jsou anténní pole ([AAU](/mobilnisite/slovnik/aau/)), které integruje zářiče, filtry a výkonové zesilovače; rádiová jednotka ([RU](/mobilnisite/slovnik/ru/)) pro [RF](/mobilnisite/slovnik/rf/) zpracování; a jednotka základnového pásma (BBU) pro digitální zpracování signálu a výpočet prekódování. Úlohou URA v síti je poskytnout fyzický prostředek pro prostorové multiplexování, zisk beamformingu a potlačení interference. Je to základní technologie pro splnění požadavků na vysokou datovou rychlost, nízkou latenci a masivní konektivitu systémů 5G a budoucích 6G, která umožňuje efektivní využití milimetrového spektra a zlepšuje pokrytí v hustých městských prostředích.

## K čemu slouží

URA byl zaveden, aby řešil základní omezení tradičních anténních systémů, které byly z velké části založeny na jednotlivých anténách nebo jednorozměrných lineárních polích. Předchozí přístupy, jako jsou křížově polarizované antény nebo uniformní lineární pole (ULA), nabízely omezené prostorové rozlišení a mohly primárně směrovat paprsky ve vodorovné rovině. Jak se mobilní sítě vyvíjely směrem k 4G LTE-Advanced a 5G, objevila se naléhavá potřeba agresivněji využívat prostorovou doménu k překonání nedostatku spektra. Průmysl potřeboval anténní systémy schopné podporovat masivní nárůst počtu současných datových toků a poskytovat přesný beamforming pro potírání vyšších útlumů na dráze, zejména v nových pásmech milimetrových vln.

Vytvoření URA bylo motivováno snahou o vyšší spektrální účinnost a kapacitu sítě. Uspořádáním prvků do obdélníkové mřížky pole získává schopnost vytvářet paprsky s nastavitelnou šířkou a směrem ve vodorovném i svislém rozměru. Tato schopnost 3D beamformingu umožňuje elevaci beamformingu specifického pro sektor a techniky jako vertikální sektorizaci, kde lze v rámci jednoho fyzického místa buňky vytvořit více 'vertikálních sektorů'. To je klíčové pro obsluhu uživatelů nacházejících se na různých podlažích výškových budov, což je běžný scénář městských nasazení. URA přímo umožňuje FD-MIMO, technologii standardizovanou v 3GPP Release 13 a novějších, která významně zvyšuje propustnost buňky a uživatelský zážitek.

Historicky koncept vychází z klasické teorie anténních polí, ale jeho standardizace v rámci 3GPP byla poháněna praktickými implementačními výzvami a požadavky na výkon komerčních systémů massive MIMO. URA poskytuje standardizovaný model pro charakterizaci anténního pole, který zajišťuje interoperabilitu mezi výrobci základnových stanic a výrobci čipových sad UE. Řeší problém neefektivního pokrytí v elevaci rovině a umožňuje síťovým operátorům dynamicky zaměřovat rádiovou energii tam, kde se uživatelé nacházejí, čímž snižuje interferenci a zlepšuje energetickou účinnost. URA je tedy klíčovým enablerem pro splnění požadavků ITU IMT-2020 na 5G, podporujících případy použití enhanced mobile broadband (eMBB) a massive machine-type communication (mMTC).

## Klíčové vlastnosti

- Dvourozměrné planární pole s rovnoměrným rozestupem prvků ve vodorovném a svislém směru
- Umožňuje nezávislé řízení beamformingu v azimutové i elevaci rovině (3D beamforming)
- Základ pro implementace massive MIMO a Full-Dimension MIMO (FD-MIMO)
- Podporuje duálně polarizované anténní prvky pro polarizační diverzitu a multiplexování
- Definované struktury kodebóků pro efektivní CSI zpětnou vazbu a prekódování
- Umožňuje multi-user MIMO (MU-MIMO) vytvářením prostorově separovatelných paprsků

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [URA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ura/)
