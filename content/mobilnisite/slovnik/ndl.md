---
slug: "ndl"
url: "/mobilnisite/slovnik/ndl/"
type: "slovnik"
title: "NDL – Downlink LARFCN"
date: 2025-01-01
abbr: "NDL"
fullName: "Downlink LARFCN"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ndl/"
summary: "Downlink LARFCN (NDL) je specifický typ LTE absolutního čísla rádiového frekvenčního kanálu (LARFCN) přiřazený downlinkovému nosnému kmitočtu. Je to jednoznačné celé číslo, které jednoznačně identifik"
---

NDL je LTE absolutní číslo rádiového frekvenčního kanálu (LARFCN) přiřazené downlinkovému nosnému kmitočtu, což je jednoznačné celé číslo identifikující střední kmitočet downlinkového LTE kanálu.

## Popis

Downlink [LARFCN](/mobilnisite/slovnik/larfcn/) (NDL) je klíčový parametr v řízení rádiových zdrojů LTE a NR. LARFCN znamená LTE absolutní číslo rádiového frekvenčního kanálu (LTE Absolute Radio Frequency Channel Number). Je to skalární hodnota, která se mapuje na konkrétní kmitočet nosné. NDL konkrétně odkazuje na hodnotu LARFCN přiřazenou downlinkovému směru nosného kmitočtu buňky. Mapování mezi celým číslem NDL a skutečným kmitočtem nosné v Hertzech je definováno vzorcem ve specifikacích 3GPP (např. TS 36.101), který se liší v závislosti na používaném frekvenčním pásmu ([E-UTRA](/mobilnisite/slovnik/e-utra/) operační pásmo). To poskytuje kompaktní, na pásmu nezávislý způsob signalizace informací o kmitočtu.

Při provozu síť vysílá NDL své servisní buňky v blocích systémové informace ([SIB](/mobilnisite/slovnik/sib/)), konkrétně v [SIB1](/mobilnisite/slovnik/sib1/) a SIB2. Když je uživatelské zařízení (UE) zapnuto nebo vstoupí do nové oblasti, provádí vyhledávání a výběr buňky. Po synchronizaci s buňkou přečte SIB a extrahuje parametry jako je NDL. UE použije tento NDL spolu s informací o pásmu k určení přesného downlinkového kmitočtu, na který má naladit svůj přijímač pro danou buňku. NDL je navíc klíčový pro měření sousedních buněk. Síť může poskytnout UE konfiguraci měření, která obsahuje seznam kmitočtů k měření. Ty jsou často poskytovány jako hodnoty LARFCN (NDL pro downlink, [NUL](/mobilnisite/slovnik/nul/) pro uplink). UE pak použije tyto hodnoty NDL k identifikaci a změření kvality signálu ([RSRP](/mobilnisite/slovnik/rsrp/), [RSRQ](/mobilnisite/slovnik/rsrq/)) sousedních buněk na těchto kmitočtech.

NDL se také používá v hlášení a signalizaci. Když UE odešle hlášení o měření do sítě, obsahuje fyzickou identitu buňky ([PCI](/mobilnisite/slovnik/pci/)) změřené buňky a kmitočet, na kterém bylo měření provedeno, což je typicky indikováno odpovídajícím LARFCN. To umožňuje síti jednoznačně identifikovat změřenou buňku a rozhodovat o předání spojení. Ve scénářích agregace nosných (CA) síť nakonfiguruje UE s více komponentními nosnými, z nichž každá je identifikována vlastním LARFCN (NDL pro downlinkovou komponentu). UE musí být schopno současně přijímat na kmitočtech odpovídajících těmto hodnotám NDL.

## K čemu slouží

Downlink LARFCN (NDL) byl vytvořen, aby poskytl standardizovanou, efektivní a jednoznačnou metodu pro identifikaci kmitočtů LTE nosných v downlinkovém směru. Před LTE systémy jako GSM používaly absolutní čísla rádiových frekvenčních kanálů (ARFCN) a UMTS používalo UARFCN. Každý systém měl vlastní číslovací schéma. Zavedení LARFCN pro LTE pokračovalo v tomto principu, ale se vzorcem optimalizovaným pro širší rozsah možných šířek pásma a frekvenčních pásem LTE, včetně párového i nepárového spektra.

Tento adresovací systém řeší problém potřeby komunikovat absolutní hodnoty kmitočtu (v MHz nebo Hz) v každé signalizační zprávě, což by bylo neefektivní z hlediska velikosti zprávy. Jediné celé číslo (NDL) je mnohem kompaktnější. Také abstrahuje fyzický kmitočet, což činí konfiguraci sítě a implementaci UE robustnější napříč mnoha globálně definovanými LTE pásmy. Operátor sítě nebo software UE potřebuje zpracovávat pouze hodnotu LARFCN; převod na skutečný kmitočet je řešen standardizovaným vyhledáním nebo výpočtem.

Jeho účel je hluboce spojen s mobilitou a řízením rádiových zdrojů. Vysíláním a signalizací pomocí NDL síť umožňuje UE efektivně objevovat, měřit a připojovat se k buňkám. Je zásadní pro procedury jako převýběr buňky, předání spojení a agregace nosných. Vývoj NDL prostřednictvím releasů 3GPP odráží přidávání nových frekvenčních pásem pro LTE (a později NR). Každé nové pásmo vyžaduje aktualizaci mapovacích tabulek LARFCN ve specifikacích, což zajišťuje, že UE a síťové zařízení mohou správně interpretovat NDL pro jakékoli podporované pásmo, od nízkopásmového spektra 600 MHz až po vysokopásmové mmWave spektrum.

## Klíčové vlastnosti

- Jednoznačné celočíselné označení pro kmitočet downlinkové LTE nosné
- Mapování na fyzický kmitočet definované vzorci 3GPP pro každé pásmo
- Vysíláno v systémové informaci (SIB1, SIB2) pro identifikaci buňky
- Používá se v konfiguraci měření a hlášení pro mobilitu
- Nezbytné pro konfiguraci agregace nosných
- Poskytuje na pásmu nezávislou metodu pro signalizaci kmitočtu

## Související pojmy

- [LARFCN – LCR TDD Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/larfcn/)
- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)
- [PCI – Physical Cell Identity](/mobilnisite/slovnik/pci/)
- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)

## Definující specifikace

- **TS 25.116** (Rel-19) — LCR TDD Repeater RF Characteristics
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TR 38.892** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ndl/)
