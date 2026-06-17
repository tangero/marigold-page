---
slug: "esd"
url: "/mobilnisite/slovnik/esd/"
type: "slovnik"
title: "ESD – Equivalent Spatial Domain"
date: 2025-01-01
abbr: "ESD"
fullName: "Equivalent Spatial Domain"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/esd/"
summary: "Modelovací a analytický koncept používaný při hodnocení výkonu vícevstupových a výstupových systémů (MIMO) a beamformingu pro rádiové systémy 3GPP (UTRAN, E-UTRAN, NR). Poskytuje zjednodušenou ekvival"
---

ESD je zjednodušený modelovací koncept používaný v hodnocení MIMO a beamformingu 3GPP k reprezentaci složitých anténních polí pro posouzení charakteristik, jako jsou vyzařovací diagramy a zisk.

## Popis

Ekvivalentní prostorová doména (ESD) je konceptuální a matematický rámec používaný ve specifikacích 3GPP k definování a hodnocení výkonu pokročilých anténních systémů ([AAS](/mobilnisite/slovnik/aas/)), včetně [MIMO](/mobilnisite/slovnik/mimo/) a beamformingu, standardizovaným a zpracovatelným způsobem. Nejde o fyzickou síťovou entitu, ale o analytický nástroj používaný primárně ve specifikacích pro testování shody (např. TS 37.113, 38.113) a v dokumentech požadavků na rádiové rozhraní. Model ESD převádí fyzikální charakteristiky anténního pole – jako jsou vyzařovací diagramy jednotlivých prvků, jejich pozice a komplexní váhy – na ekvivalentní reprezentaci, která popisuje chování systému v prostorové doméně (tj. jako funkci azimutálního a elevančního úhlu).

Z architektonického hlediska je tento koncept aplikován na definici požadavků na rádiové rozhraní základnových stanic (NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB) a uživatelského zařízení (UE). Pro testované zařízení ([DUT](/mobilnisite/slovnik/dut/)) s AAS je jeho skutečný anténní systém charakterizován sadou anténních prvků. Přístup ESD umožňuje odvodit ekvivalentní anténní diagram nebo ekvivalentní sadu prostorových paprsků, které reprezentují složený efekt pole a jeho digitálního zpracování signálu. To je klíčové, protože přímé testování všech možných kombinací beamformingových vah pro rozsáhlé pole je nepraktické. ESD poskytuje model redukovaného řádu, který zachycuje podstatné prostorové vlastnosti za účelem definování vyzařovaného výkonu, citlivosti a limitů nežádoucích emisí.

Metodologie funguje tak, že definuje mapování ze skutečných anténních portů pole na ekvivalentní sadu vzorků nebo paprsků v prostorové doméně. Specifikace podrobně popisují vzorce a postupy pro výpočet ekvivalentního izotropně vyzařovaného výkonu ([EIRP](/mobilnisite/slovnik/eirp/)) nebo ekvivalentní izotropní citlivosti ([EIS](/mobilnisite/slovnik/eis/)) v různých prostorových směrech na základě tohoto modelu. Například TS 38.113 pro NR definuje požadavky na emise základnových stanic pomocí konceptu ESD k určení limitů výkonu pro ekvivalentní hlavní lalok a boční laloky paprsku. To zahrnuje koncepty jako „ekvivalentní činitel pole“ a aplikaci beamformingových vah na diagramy prvků za účelem vytvoření složeného ESD diagramu.

Klíčové součásti analýzy ESD zahrnují definici vyzařovacího diagramu anténního prvku, geometrii pole, vektory beamformingových vah a mapování na prostorovou mřížku. Jejím úkolem je umožnit specifikaci metrik výkonu, které jsou nezávislé na konkrétní vnitřní implementaci AAS, a zároveň zajistit, že zařízení splňuje základní požadavky na rádiový výkon, koexistenci a regulatorní požadavky. Tvoří most mezi složitými fyzikálními anténními systémy a potřebou jasných, testovatelných požadavků ve standardech 3GPP.

## K čemu slouží

Koncept ESD byl vyvinut, aby řešil významnou výzvu specifikace a testování výkonu základnových stanic a uživatelských zařízení využívajících pokročilé anténní systémy ([AAS](/mobilnisite/slovnik/aas/)) s možnostmi beamformingu. Tradiční testy rádiové shody byly navrženy pro jednoduché antény nebo antény s diverzitou, kde postačovalo provedené testování na anténním portu. S příchodem [MIMO](/mobilnisite/slovnik/mimo/) a massive MIMO, kde je výkon neodmyslitelně prostorový a závisí na digitálním beamformingu, byla vyžadována nová metodologie.

Historicky, počínaje 3GPP Rel-4 s počátečními studiemi MIMO pro UMTS a dále se vyvíjejíc přes LTE a 5G NR, se složitost anténních systémů dramaticky zvýšila. Účelem definování ekvivalentní prostorové domény bylo vytvořit standardizovaný rámec nezávislý na implementaci pro definování požadavků na vyzařovaný výkon. Řeší problém, jak napsat technickou specifikaci, která se stejně vztahuje na dodavatele používajícího 64prvkové obdélníkové pole a na jiného používajícího 32prvkové kruhové pole, pokud jejich ekvivalentní prostorové chování splňuje stejná kritéria.

Tento přístup byl motivován potřebou spravedlnosti v certifikaci, praktičnosti testování a souladu s regulatorními požadavky na parazitní emise a vyzařovaný výkon. Bez modelu ESD by nebylo možné definovat jednoznačné požadavky pro testování přes vzduch (OTA) pro zařízení s beamformingem. Umožňuje 3GPP specifikovat klíčové aspekty výkonu, jako je celkový vyzařovaný výkon (TRP), efektivní izotropní citlivost (EIS) a prostorové masky emisí, způsobem, který odráží reálné provozní beamformingové chování moderních rádiových systémů. Tím je zajištěn výkon sítě a spektrální účinnost při zachování shody s mezinárodními rádiovými předpisy.

## Klíčové vlastnosti

- Poskytuje ekvivalentní prostorovou reprezentaci složitých anténních polí a beamformingu
- Umožňuje definici požadavků na vyzařovaný výkon (EIRP, EIS) pro AAS
- Tvoří základ pro metodologie testování přes vzduch (OTA) v 3GPP
- Nezávislý na implementaci, zaměřuje se na vnější prostorové chování spíše než na vnitřní architekturu
- Používá se k modelování vyzařovacích diagramů, bočních laloků a prostorové korelace pro testování shody
- Aplikovatelný napříč více rádiovými přístupovými technologiemi (UTRAN, E-UTRAN, NG-RAN)

## Související pojmy

- [AAS – Active Antenna System](/mobilnisite/slovnik/aas/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [EIRP – Effective Isotropic Radiated Power](/mobilnisite/slovnik/eirp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TS 34.124** (Rel-19) — EMC Requirements for 3G UTRA Terminals
- **TS 36.113** (Rel-19) — EMC Requirements for E-UTRA Base Stations
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.124** (Rel-19) — NR UE EMC Requirements
- **TS 38.175** (Rel-19) — EMC for NR IAB Nodes
- **TS 38.809** (Rel-16) — IAB Radio Transmission & Reception Background

---

📖 **Anglický originál a plná specifikace:** [ESD na 3GPP Explorer](https://3gpp-explorer.com/glossary/esd/)
