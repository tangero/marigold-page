---
slug: "as"
url: "/mobilnisite/slovnik/as/"
type: "slovnik"
title: "AS – Angle Spread"
date: 2026-01-01
abbr: "AS"
fullName: "Angle Spread"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/as/"
summary: "Angle Spread (AS), známý také jako Azimuth Spread, je statistická míra úhlového rozptylu vícecestných složek dopadajících na anténní pole přijímače. Kvantifikuje prostorové rozptylové prostředí, což j"
---

AS je statistická míra úhlového rozptylu vícecestných složek dopadajících na anténní pole přijímače, která kvantifikuje prostorové rozptylové prostředí pro modelování kanálu a výkon beamformingu.

## Popis

Angle Spread (AS) je klíčový parametr pro charakterizaci bezdrátového kanálu, definovaný ve specifikacích 3GPP pro hodnocení výkonu rádiového přenosu. Konkrétně měří rozptyl úhlů příchodu (nebo odchodu) vícecestných složek kolem středního směru. Výpočet, pokud není stanoveno jinak, následuje kruhovou metodu podrobně popsanou v dodatku A 3GPP, která poskytuje standardizovaný přístup pro zajištění konzistence napříč simulacemi a hodnocením výkonu. Tento parametr není přímým fyzikálním měřením ze živé sítě, ale statistickým deskriptorem používaným v kanálových modelech k emulaci reálných podmínek šíření.

V technickém provozu je AS nedílnou součástí prostorových kanálových modelů ([SCM](/mobilnisite/slovnik/scm/)) a modelů s klastrovaným zpožděním ([CDL](/mobilnisite/slovnik/cdl/)) definovaných 3GPP. Tyto modely generují realistické impulsní odezvy kanálu definováním parametrů, jako je rozptyl zpoždění, úhlový rozptyl a výkony klastrů. Hodnota AS ovlivňuje, jak je signální energie distribuována přes různé úhlové směry na přijímači. Nízká AS označuje vysoce směrový kanál s omezeným rozptylem, typický pro prostředí s přímou viditelností (LoS) nebo venkovské oblasti. Vysoká AS značí prostředí bohaté na rozptyl se signály přicházejícími z mnoha směrů, běžné v městských zástavbách nebo vnitřních prostorech.

Z architektonického hlediska je AS kritickým vstupem pro systémové a linkové simulace, které hodnotí výkon víceanténních technik. Například v systémech Massive [MIMO](/mobilnisite/slovnik/mimo/) a beamformingu dosažitelné zisky beamformingu a potenciál pro prostorové multiplexování výrazně závisí na úhlových vlastnostech kanálu. Nástroje pro plánování sítí a algoritmy správy rádiových zdrojů využívají znalost typických hodnot AS pro různé scénáře nasazení (např. Urban Micro, Rural Macro) k predikci pokrytí, kapacity a vzorců interference. AS je tedy základním prvkem při návrhu, testování a optimalizaci rádiových rozhraní 5G NR a LTE.

Jeho role sahá až k definování korelačních vlastností mezi anténními prvky. V poli korelace mezi signály přijímanými na různých anténách klesá s rostoucím úhlovým rozptylem (AS). Tento vztah je zachycen v korelační matici antén, která je odvozena z výkonového úhlového spektra ([PAS](/mobilnisite/slovnik/pas/)) a parametru AS. Vysoká korelace (nízká AS) může omezit hodnost MIMO kanálu a snížit zisky multiplexování, zatímco nízká korelace (vysoká AS) umožňuje více nezávislých datových proudů. Přesné modelování AS je tedy nezbytné pro hodnocení praktické propustnosti a spolehlivosti MIMO schémat specifikovaných ve standardech 3GPP.

## K čemu slouží

Angle Spread existuje jako standardizovaná metrika pro kvantitativní popis prostorových charakteristik rádiového přenosového kanálu. Před jeho formální definicí v 3GPP se systémoví návrháři spoléhali na kvalitativní popisy nebo proprietární modely, což ztěžovalo srovnávání výsledků výkonu mezi různými dodavateli a výzkumnými skupinami. Vytvoření jednotného parametru AS spolu s dalšími parametry kanálového modelu vyřešilo problém nekonzistentních simulačních předpokladů a umožnilo spravedlivé a reprodukovatelné benchmarkování pokročilých anténních technologií.

Historický kontext jeho zavedení, zejména od 3GPP Release 99 dále, se časově shoduje s vývojem a standardizací [MIMO](/mobilnisite/slovnik/mimo/) a chytrých anténních technik pro 3G/UMTS a později 4G/LTE. Jak sítě začaly využívat prostorovou doménu, stalo se kritickým mít společný popis úhlových vlastností kanálu pro predikci účinnosti beamformingu, potenciálu prostorového multiplexování a potlačení interference. Parametr AS poskytuje tento společný jazyk, což umožňuje komunitě 3GPP definovat základní scénáře nasazení (např. pro hodnocení IMT-Advanced) se specifickými hodnotami AS a zajistit, aby tvrzení o výkonu byla založena na srovnatelných a realistických podmínkách kanálu.

Dále AS řeší omezení příliš zjednodušených kanálových modelů, které uvažovaly pouze útlum na trase a rozptyl zpoždění. Takové modely byly nedostatečné pro návrh algoritmů prostorového zpracování. Začleněním AS mohou kanálové modely 3GPP přesněji odrážet výkon reálných systémů v různorodých prostředích, od otevřených polí po husté městské zástavby. To umožňuje efektivnější nasazení sítí, protože zařízení mohou být navržena a konfigurována na základě známého statistického chování kanálu, což optimalizuje náklady a výkon.

## Klíčové vlastnosti

- Standardizovaná statistická míra úhlového rozptylu
- Klíčový vstup pro prostorové kanálové modely 3GPP (SCM, CDL)
- Určuje prostorovou korelaci mezi anténními prvky
- Kritický pro predikci výkonu MIMO a beamformingu
- Definován pro různé scénáře nasazení 3GPP (např. UMi, RMa)
- Výpočet následuje specifikovanou kruhovou metodu pro konzistenci

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.882** (Rel-19) — Study on Energy Efficiency as a Service Criteria
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- … a dalších 183 specifikací

---

📖 **Anglický originál a plná specifikace:** [AS na 3GPP Explorer](https://3gpp-explorer.com/glossary/as/)
