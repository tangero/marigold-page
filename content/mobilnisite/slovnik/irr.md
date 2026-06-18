---
slug: "irr"
url: "/mobilnisite/slovnik/irr/"
type: "slovnik"
title: "IRR – Infrared Reflecting"
date: 2025-01-01
abbr: "IRR"
fullName: "Infrared Reflecting"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/irr/"
summary: "Vlastnost materiálu nebo povrchová úprava, která odráží infračervené záření. V modelování kanálů 3GPP jde o parametr ovlivňující tepelné a elektromagnetické prostředí pro šíření rádiových vln, zvláště"
---

IRR je vlastnost materiálu nebo povrchová úprava, která odráží infračervené záření a ovlivňuje tepelné a elektromagnetické prostředí pro šíření rádiových vln v 3GPP kanálových modelech, zejména pro vysokofrekvenční pásma.

## Popis

Infrared Reflecting (IRR) je fyzikální vlastnost definovaná ve specifikacích kanálových modelů 3GPP, konkrétně v řadách 38.900 a 38.901. Popisuje charakteristiku materiálu nebo povrchu odrážet vlnové délky infračerveného záření, které je součástí elektromagnetického spektra sousedícího s rádiovými frekvencemi. Tato vlastnost je integrována do pokročilých kanálových modelů pro simulaci realističtějšího prostředí šíření, zejména pro frekvence v milimetrových vlnách (mmWave) a sub-THz pásmech, kde interakce s materiály jsou složitější. Kanálový model používá IRR jako jeden z několika parametrů prostředí pro výpočet útlumu na dráze, odrazivosti a charakteristik rozptylu. Pomáhá předpovídat chování signálů při interakci s budovami, vozidly nebo jinými objekty, které mají specifické infračerveně odrazivé vlastnosti, jež mohou v určitých scénářích korelovat s jejich odrazivostí na rádiových frekvencích.

V technické architektuře kanálového modelu 3GPP je IRR parametrem v rámci definic scénářů a vlastností stavebních materiálů. Model definuje různé podmínky šíření, jako je urban microcell (UMi), urban macrocell (UMa) a indoor office (InH), z nichž každý má přiřazené vlastnosti materiálů. Pro každý typ materiálu (např. beton, sklo, kov) může model specifikovat hodnotu IRR nebo související sadu parametrů, které ovlivňují odraz a ohyb rádiových vln. Algoritmy kanálového modelu, jako je sledování paprsků (ray-tracing) nebo stochastické přístupy popsané v 38.901, používají tyto vlastnosti materiálů ke generování impulsních odezev kanálu, včetně parametrů jako rozprostření zpoždění, úhlové rozprostření a ztráty způsobené stíněním.

Úloha IRR v síti je primárně ve fázích návrhu, simulace a testování, nikoli v reálném provozu. Výrobci síťových zařízení a mobilní operátoři používají tyto podrobné kanálové modely k vyhodnocení výkonu nových rádiových technologií, zejména pro 5G-Advanced a 6G, kde jsou vysoké frekvence a integrované snímání a komunikace (ISAC) klíčové. Zahrnutím IRR mohou modely přesněji předpovídat pokrytí, kapacitu a výkon beamformingu v různorodých prostředích, což vede k lepšímu plánování sítí a návrhu hardwaru. Je součástí širšího úsilí o vytvoření jednotného a přesného kanálového modelu, který podporuje vývoj od tradiční komunikace k systémům kombinujícím komunikaci a snímání.

## K čemu slouží

Účelem definice Infrared Reflecting (IRR) v rámci standardů 3GPP je zvýšit přesnost a realističnost modelů rádiových kanálů, zejména pro vysokofrekvenční pásma a nové případy užití, jako je integrované snímání. Tradiční kanálové modely často zjednodušovaly vlastnosti materiálů, zaměřovaly se primárně na odraz a rozptyl [RF](/mobilnisite/slovnik/rf/) bez zohlednění širších elektromagnetických interakcí. Protože 5G a další generace využívají milimetrové vlny a sub-THz frekvence, charakteristiky šíření se stávají citlivějšími na detaily prostředí, včetně vlastností materiálů, které ovlivňují jak rádiové, tak infračervené vlny. Zahrnutí IRR umožňuje komplexnější fyzikální reprezentaci, což zlepšuje věrnost simulací pro plánování sítí a vyhodnocování výkonu systému.

Historicky poskytovaly kanálové modely jako 3GPP Spatial Channel Model ([SCM](/mobilnisite/slovnik/scm/)) nebo modely [ITU-R](/mobilnisite/slovnik/itu-r/) základní přístup, ale postrádaly detailní parametrizaci materiálů. Zavedení IRR v Release 14 spolu s 5G kanálovým modelem v 38.901 řešilo potřebu podrobnějšího modelování prostředí pro podporu pokročilých technologií, jako je massive [MIMO](/mobilnisite/slovnik/mimo/), beamforming a později funkce snímání. Tento parametr pomáhá simulovat scénáře, kde by tepelné nebo infračervené vlastnosti objektů mohly korelovat s jejich chováním na RF, což je zásadní pro vývoj algoritmů pro společnou komunikaci a snímání, kde síť dokáže detekovat a charakterizovat objekty na základě odražených signálů.

Motivace vychází z omezení předchozích přístupů, které zacházely se všemi povrchy pomocí generických koeficientů odrazivosti, což mohlo vést k nepřesným předpovědím výkonu v reálných nasazeních. Zahrnutím IRR umožňuje 3GPP výzkumníkům a inženýrům vytvářet spolehlivější simulace, které zohledňují složité interakce mezi rádiovými vlnami a různými materiály, čímž se snižují rizika nasazení a optimalizuje výkon sítě pro budoucí aplikace, včetně vozidlových sítí, chytrých měst a průmyslového IoT, kde je snímání prostředí nedílnou součástí.

## Klíčové vlastnosti

- Parametr v kanálových modelech 3GPP (38.900/38.901) pro charakterizaci materiálů
- Ovlivňuje modelování šíření rádiových vln pro vysokofrekvenční pásma (mmWave/sub-THz)
- Podporuje přesnou simulaci odrazu a rozptylu v různorodých prostředích
- Integruje se s metodologiemi modelování kanálů založenými na sledování paprsků (ray-tracing) a stochastickými přístupy
- Zlepšuje predikci výkonu pro beamforming a systémy massive MIMO
- Usnadňuje vývoj případů užití integrovaného snímání a komunikace (ISAC)

## Definující specifikace

- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [IRR na 3GPP Explorer](https://3gpp-explorer.com/glossary/irr/)
