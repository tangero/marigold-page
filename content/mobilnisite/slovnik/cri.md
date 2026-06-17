---
slug: "cri"
url: "/mobilnisite/slovnik/cri/"
type: "slovnik"
title: "CRI – CSI-RS Resource Indicator"
date: 2025-01-01
abbr: "CRI"
fullName: "CSI-RS Resource Indicator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cri/"
summary: "Ukazatel zdroje CSI-RS (CRI) je pole hlášené uživatelským zařízením (UE) k označení toho, který zdroj CSI-RS z nakonfigurované sady poskytl nejlepší kvalitu kanálu pro správu paprsků nebo pro získání"
---

CRI je pole hlášené uživatelským zařízením k označení toho, který konkrétní zdroj CSI-RS z nakonfigurované sady poskytl nejlepší kvalitu kanálu pro správu paprsků nebo pro získání informace o stavu kanálu.

## Popis

Ukazatel zdroje [CSI-RS](/mobilnisite/slovnik/csi-rs/) (CRI) je klíčový zpětnovazební mechanismus v rámci fyzické vrstvy 5G New Radio (NR) a pokročilého LTE pro hlášení informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)). Funguje v kontextu správy paprsků a víceanténních ([MIMO](/mobilnisite/slovnik/mimo/)) operací. Síť nakonfiguruje uživatelskému zařízení (UE) sadu zdrojů obsahující více zdrojů referenčního signálu pro informaci o stavu kanálu (CSI-RS). Každý zdroj odpovídá specifické vysílací konfiguraci, například konkrétnímu beamformingovému signálu z anténního pole gNB nebo specifické konfiguraci portu. UE změří kvalitu signálu (např. na základě přijímaného výkonu referenčního signálu (RSRP) nebo poměru signálu k šumu a interferenci (SINR)) každého zdroje CSI-RS v této sadě.

Při spuštění hlášení CSI vybere UE zdroj CSI-RS, který podle konfigurace hlášení poskytuje nejlepší naměřenou kvalitu. Index tohoto vybraného zdroje v rámci nakonfigurované sady je zakódován a hlášen zpět do gNB jako CRI. Tento index je kompaktní reprezentace, typicky vyžadující jen několik bitů, která specifikuje, která předem nakonfigurovaná konfigurace paprsku nebo portu je pro UE aktuálně optimální. CRI je hlášen spolu s dalšími parametry CSI, jako je ukazatel hodnosti (RI), ukazatel předkodovací matice (PMI) a ukazatel kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), jako součást jednotné struktury hlášení CSI definované v technických specifikacích jako 38.214.

Role CRI je zásadní pro procedury správy paprsků, jako je výběr paprsku a jeho zpřesňování. Při počátečním přístupu a mobilitě pomáhá CRI identifikovat nejlepší paprsek bloku synchronizačního signálu (SSB) nebo CSI-RS pro navázání spojení. V připojeném režimu umožňuje dynamické přepínání a sledování paprsků, což síti dovoluje přizpůsobovat vysílací paprsek měnící se pozici UE nebo rádiovým podmínkám. Pro operace s více TRP (Transmission Reception Point) nebo více paprsky může CRI indikovat preferovaný TRP nebo kombinaci paprsků, což usnadňuje pokročilé koordinační schémata.

Z architektonického hlediska je CRI generováno fyzickou vrstvou UE na základě měření vrstvy 1 ([L1](/mobilnisite/slovnik/l1/)). Hlášení je konfigurováno signalizací vyšší vrstvy [RRC](/mobilnisite/slovnik/rrc/), která definuje sadu zdrojů CSI-RS, periodicitu hlášení a spouštěcí události. Hlášení CRI je následně přenášeno prostřednictvím řídicí informace uplinku (UCI) na PUCCH nebo PUSCH. Plánovač gNB využívá zpětnou vazbu CRI k výběru příslušných beamformingových vah pro downlink, čímž směruje energii k UE a zlepšuje spolehlivost spoje a propustnost dat. Tato zpětnovazební smyčka s uzavřenou smyčkou je nezbytná pro využití výhod massive MIMO a vysokofrekvenčních pásem (např. mmWave), kde je beamforming pro pokrytí nezbytný.

## K čemu slouží

CRI bylo zavedeno, aby řešilo základní výzvu správy paprsků v 5G NR, zejména když sítě začaly využívat vyšší frekvenční pásma s massive [MIMO](/mobilnisite/slovnik/mimo/) anténními poli. V LTE v pásmu pod 6 GHz bylo možné dosáhnout širokoplošného pokrytí s relativně širokými paprsky. Avšak ve spektru mmWave (např. FR2) trpí šíření signálu vysokým útlumem dráhy a stíněním, což vyžaduje použití úzkých paprsků s vysokým ziskem k udržení životaschopného spoje. Síť musí identifikovat a sledovat nejlepší směrový paprsek pro každé UE, což je proces vyžadující efektivní zpětnou vazbu od zařízení. CRI tento mechanismus poskytuje tím, že umožňuje UE indikovat svůj preferovaný paprsek ze sady kandidátů nakonfigurované sítí.

Před 5G se zpětná vazba [CSI](/mobilnisite/slovnik/csi/) v LTE primárně zaměřovala na hlášení širokopásmového CQI a PMI pro MIMO předkódování v relativně homogenním pokrytí buňky. Postrádala standardizovanou, efektivní metodu pro explicitní indikaci paprsku. Rané implementace beamformingu často spoléhaly na buňkově specifické referenční signály nebo vyžadovaly proprietární řešení. CRI, standardizované počínaje 3GPP Release 13 pro vylepšení LTE a plně využívané v NR od Release 15, vytvořilo jednotný a flexibilní rámec pro hlášení paprsků. Řeší problém režie; namísto hlášení plných kanálových matic pro mnoho paprsků UE jednoduše odešle krátký ukazatel, čímž šetří prostředky uplinku.

Jeho vytvoření bylo motivováno potřebou dynamické a agilní správy paprsků pro podporu vysoké mobility, robustního připojení a prostorového multiplexování v hustých nasazeních. CRI umožňuje klíčové případy užití 5G, jako je vylepšené mobilní širokopásmové připojení (eMBB) v mmWave a ultra-spolehlivá komunikace s nízkou latencí (URLLC), tím, že zajišťuje, že síť může rychle přepnout na nejsilnější paprsek, a minimalizuje tak přerušení. Tvoří základ pro pokročilejší funkce, jako je hlášení CSI pro více paprsků, obnova při selhání paprsku a operace s více TRP, což z něj činí základní kámen návrhu fyzické vrstvy 5G.

## Klíčové vlastnosti

- Indikuje index nejlepšího zdroje CSI-RS ze sady nakonfigurované sítí
- Umožňuje efektivní výběr a sledování paprsků pro systémy massive MIMO a mmWave
- Hlášen jako součást zpětné vazby CSI vrstvy 1 spolu s RI, PMI a CQI
- Konfigurovatelné signalizací RRC pro flexibilitu měření a hlášení
- Podporuje periodické i aperiodické hlášení spouštěné DCI
- Nezbytné pro procedury správy paprsků, jako je zpřesňování paprsku a obnova při jeho selhání

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [CRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cri/)
