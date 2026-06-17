---
slug: "gscn"
url: "/mobilnisite/slovnik/gscn/"
type: "slovnik"
title: "GSCN – Global Synchronization Channel Number"
date: 2025-01-01
abbr: "GSCN"
fullName: "Global Synchronization Channel Number"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gscn/"
summary: "Global Synchronization Channel Number (GSCN) je základní parametr v 5G NR, který jednoznačně identifikuje polohu synchronizačních signálových bloků (SSB) v rádiovém kmitočtovém spektru. Poskytuje glob"
---

GSCN je parametr 3GPP, který jednoznačně identifikuje polohu synchronizačních signálových bloků v rádiovém kmitočtovém spektru v 5G NR a poskytuje globální číslovací schéma pro střední kmitočty SSB.

## Popis

Global Synchronization Channel Number (GSCN) je klíčový identifikátor ve fyzické vrstvě 5G New Radio (NR), zavedený ve specifikaci 3GPP Release 15. Slouží jako globální index, který odkazuje na absolutní číslo rádiového kmitočtového kanálu ([ARFCN](/mobilnisite/slovnik/arfcn/)) středního kmitočtu pro Synchronization Signal Block (SSB). SSB nese primární synchronizační signál (PSS), sekundární synchronizační signál (SSS) a fyzický vysílací kanál (PBCH), což jsou základní signály, které uživatelské zařízení (UE) používá k objevení, synchronizaci s 5G buňkou a dekódování základních systémových informací. GSCN poskytuje zjednodušenou a efektivní metodu pro síť, aby signalizovala, a pro UE, aby vyhledávala tyto SSB napříč rozsáhlým a komplexním 5G kmitočtovým pásmem.

Z architektonického hlediska je GSCN definován v rámci specifikací rozhraní NR (např. TS 38.104, TS 38.101). Funguje tak, že vytváří mapování mezi celočíselnou hodnotou GSCN a konkrétním středním kmitočtem SSB (v kHz). Toto mapování je definováno odlišně pro kmitočtový rozsah 1 (FR1: pod 6 GHz) a kmitočtový rozsah 2 (FR2: mmWave, 24,25 GHz a výše) kvůli jejich odlišným charakteristikám kmitočtového rastru. Pro FR1 velikost kroku GSCN odpovídá kmitočtovému kroku (např. 1,2 MHz nebo 1,44 MHz v závislosti na pásmu). Pro FR2 je krok větší, což odpovídá širším šířkám pásma a odlišnému synchronizačnímu rastru. UE používá GSCN, poskytnutý v systémové informaci nebo v konfiguracích měření, k přímému naladění svého přijímače na očekávaný kmitočet SSB, aniž by muselo provádět slepé prohledávání širokého rozsahu možných kmitočtů.

Klíčové komponenty zahrnující GSCN zahrnují synchronizační rastr, SSB a signalizaci vyšších vrstev. Synchronizační rastr definuje množinu povolených kmitočtů, na kterých může být SSB umístěn. GSCN v podstatě globálně čísluje tyto body rastru. Během provozu síť vysílá seznam GSCN v System Information Block 1 (SIB1) prostřednictvím PBCH, což indikuje, na kterém kmitočtu může UE najít SSB sousedních buněk pro měření (např. pro převýběr buňky nebo předání spojení). gNodeB (gNB) také používá GSCN v konfiguraci měřicího objektu pro připojená UE prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) signalizace.

Jeho role je klíčová pro objevování sítě a mobilitu. Výrazně snižuje čas a výkon, které UE spotřebuje na počáteční vyhledávání buňky, zejména v mmWave pásmech, kde se používají beamy. Díky znalosti GSCN UE přesně ví, kde má hledat SSB, což umožňuje rychlejší beam sweeping a asociaci. Tato efektivita je zásadní pro podporu vysoké mobility, úspory energie a spolehlivého připojení v různých scénářích nasazení 5G, od pokrytí široké oblasti v nízkých pásmech až po kapacitu hotspotů ve vysokých pásmech.

## K čemu slouží

GSCN byl vytvořen k řešení významných výzev při vyhledávání buněk a měření, které přineslo extrémně široké a flexibilní využití spektra v 5G NR. Předchozí generace, jako LTE, používaly koncept [EARFCN](/mobilnisite/slovnik/earfcn/) ([E-UTRA](/mobilnisite/slovnik/e-utra/) Absolute Radio Frequency Channel Number), který byl vázán na střední kmitočet nosné. Nicméně 5G zavedlo SSB, které nemusí být centrováno na nosné a může být umístěno na jiném rastru (synchronizační rastr). Navíc 5G podporuje obrovský rozsah kmitočtů od pod 1 GHz až do 100 GHz s fragmentovanými alokacemi spektra a šířkami pásma až do 400 MHz. Jednoduché souvislé číslovací schéma jako EARFCN bylo nedostatečné.

Primární problém, který GSCN řeší, je neefektivita slepého vyhledávání. Bez GSCN by muselo UE skenovat každý možný kmitočtový bod na synchronizačním rastru napříč více pásmy, což by byl proces nepřijatelně časově náročný a energeticky intenzivní, zejména v mmWave pásmech, kde je vyhledávání napříč mnoha beamy již samo o sobě složité. GSCN poskytuje stručnou, globálně jednoznačnou „adresu“ pro SSB, což umožňuje síti přesně říci UE, kde má hledat. To umožňuje rychlý počáteční přístup, efektivní měření sousedních buněk a spolehlivou mobilitu.

Motivace vycházela z potřeby škálovatelného a efektivního provozu napříč heterogenní krajinou 5G. Návrh umožňuje jednotnou metodu signalizace poloh SSB bez ohledu na kmitočtové pásmo nebo konfiguraci části pásma. Abstrahuje složité podkladové kmitočtové výpočty do jednoduchého celého čísla, čímž zjednodušuje implementaci UE a konfiguraci sítě. Jednalo se o nezbytný vývoj z přístupu LTE, aby bylo možné zvládnout nové paradigma oddělených rastrů pro synchronizaci a datové kanály v NR, což přímo podporuje funkce jako nosné s širokým pásmem a flexibilní umístění SSB pro beamforming.

## Klíčové vlastnosti

- Jednoznačně identifikuje střední kmitočet synchronizačního signálového bloku (SSB) v NR.
- Poskytuje globální index mapovaný na konkrétní kmitočet v kHz.
- Různé velikosti kroků a mapovací vzorce pro FR1 (pod 6 GHz) a FR2 (mmWave).
- Signalizováno v systémové informaci (SIB1) pro převýběr buňky a v RRC pro měření.
- Umožňuje efektivní procedury vyhledávání buněk a měření na straně UE snížením slepého skenování.
- Podporuje provoz napříč celým 5G spektrem od nízkých pásem až po milimetrové vlny.

## Související pojmy

- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)

## Definující specifikace

- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.862** (Rel-19) — Adding channel bandwidth in existing NR bands
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- **TR 38.815** (Rel-15) — NR Frequency Range 24.25-29.5 GHz Study
- **TR 38.847** (Rel-17) — NR 47.2-48.2 GHz Frequency Range
- **TR 38.849** (Rel-18) — Technical Report
- **TR 38.852** (Rel-17) — 1900MHz NR band for European Rail Mobile Radio
- **TR 38.853** (Rel-17) — 900MHz NR Band for European Rail Mobile Radio
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [GSCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/gscn/)
