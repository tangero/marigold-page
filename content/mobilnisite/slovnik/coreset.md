---
slug: "coreset"
url: "/mobilnisite/slovnik/coreset/"
type: "slovnik"
title: "CORESET – Control Resource Set"
date: 2025-01-01
abbr: "CORESET"
fullName: "Control Resource Set"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/coreset/"
summary: "CORESET je vyhrazená oblast časových a frekvenčních zdrojů v 5G NR, kde uživatelské zařízení (UE) monitoruje přenosy fyzického řídicího kanálu pro downlink (PDCCH). Definuje místo, kde má UE hledat ří"
---

CORESET je vyhrazená oblast časových a frekvenčních zdrojů v 5G NR, kde uživatelské zařízení (UE) monitoruje přenosy PDCCH, aby přijímalo řídicí informace pro downlink.

## Popis

Control Resource Set (CORESET) je základní koncept fyzické vrstvy v 5G New Radio (NR), který definuje specifickou, konfigurovatelnou množinu bloků fyzických zdrojů ([PRB](/mobilnisite/slovnik/prb/)) a [OFDM](/mobilnisite/slovnik/ofdm/) symbolů v rámci slotu, kde musí uživatelské zařízení (UE) monitorovat kandidáty fyzického řídicího kanálu pro downlink ([PDCCH](/mobilnisite/slovnik/pdcch/)). Na rozdíl od pevné řídicí oblasti v LTE poskytuje CORESET velkou flexibilitu. Je charakterizován několika klíčovými parametry: umístěním ve frekvenční doméně (množina souvislých nebo nesouvislých PRB), dobou trvání v časové doméně (1 až 3 OFDM symboly), typem mapování (prokládané nebo neprokládané) a přidruženou konfigurací referenčního signálu pro demodulaci PDCCH ([DM-RS](/mobilnisite/slovnik/dm-rs/)). Jednomu UE lze nakonfigurovat více CORESETů, z nichž každý může být potenciálně propojen s jinou množinou prohledávacího prostoru, což umožňuje sofistikované řízení zdrojů řídicího kanálu.

Z architektonického hlediska je CORESET pro UE konfigurován prostřednictvím signalizace řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)), konkrétně v rámci informačního elementu PDCCH-Config. Konfigurace zahrnuje ID CORESETu, zdroje ve frekvenční doméně (zadané bitmapou), dobu trvání ve symbolech a granularitu prekódování. Kritickou součástí je Control-Channel Element ([CCE](/mobilnisite/slovnik/cce/)), což je základní jednotka pro přenos PDCCH. CORESET se skládá z množiny skupin zdrojových elementů ([REG](/mobilnisite/slovnik/reg/)), kde REG odpovídá jednomu zdrojovému bloku v jednom OFDM symbolu. REGy jsou seskupeny do svazků REG a CCE jsou tvořeny z těchto svazků REG. Mapování CCE na fyzické zdroje v rámci CORESETu může být prokládané (poskytující frekvenční diverzitu) nebo neprokládané (umožňující lokalizovaný přenos pro beamforming).

Během provozu UE používá nakonfigurované parametry CORESETu k slepé dekódaci kandidátů PDCCH v přidružených množinách prohledávacího prostoru. gNodeB vysílá [DCI](/mobilnisite/slovnik/dci/) mapováním zakódovaných bitů DCI na jeden nebo více CCE (úrovně agregace 1, 2, 4, 8 nebo 16) v rámci nakonfigurovaných zdrojů CORESETu. Chování monitorování UE – jako je periodicita a načasování – je řízeno propojeným prohledávacím prostorem, zatímco CORESET striktně definuje fyzické 'kde' hledat. Toto oddělení definice zdroje (CORESET) od pravidla monitorování (Search Space) je klíčovou inovací 5G. CORESETy hrají zásadní roli při umožňování funkcí, jako je ultra-spolehlivá komunikace s nízkou latencí (URLLC), tím, že umožňují velmi krátké, předem umístěné řídicí oblasti, a při podpoře beamformovaných řídicích kanálů tím, že jsou asociovány se specifickými stavy indikátoru konfigurace přenosu (TCI) pro referenci kvazi-ko-lokace (QCL).

## K čemu slouží

CORESET byl vytvořen, aby řešil nepružnost návrhu řídicího kanálu v LTE, který používal pevnou, na buňku specifickou řídicí oblast na začátku každého podrámce. Tato rigidní struktura byla nevhodná pro rozmanité požadavky služeb 5G, jako jsou různé latence, šířky pásma a případy užití, jako je massive IoT a komunikace s kritickými požadavky. Primární problém, který CORESET řeší, je umožnění dynamické a efektivní alokace zdrojů řídicího kanálu, která se může přizpůsobit různým scénářům nasazení, podmínkám kanálu a schopnostem UE.

Historicky vedla statická řídicí oblast v LTE k neefektivitě, zejména u širokopásmových nosných nebo scénářů s nízkým provozem, protože režie řídicího kanálu byla vždy přítomna. Motivací pro CORESET bylo oddělit signalizaci řízení od pevné časově-frekvenční struktury, což umožňuje operátorům sítí přesně přizpůsobit řídicí zdroje. To umožňuje vynikající podporu pro provoz se širokou šířkou pásma (např. až 400 MHz), kde je neefektivní monitorovat celé pásmo kvůli řídicímu kanálu; místo toho lze CORESET nakonfigurovat v konkrétní části šířky pásma (BWP). Zároveň zásadně umožňuje nízkou latenci tím, že umožňuje umístit řídicí oblast bezprostředně před plánovaná data (provoz s mini-slotem), což je v ostrém kontrastu s plánováním vázaným na podrámec v LTE.

Dále je CORESET nezbytný pro pokročilé anténní systémy a správu beamformingu v 5G NR. Tím, že je CORESET asociován se specifickými předpoklady QCL (prostřednictvím stavů TCI), může síť vysílat PDCCH pomocí beamformingu, směrovat řídicí signály ke konkrétním UE nebo oblastem. Tím se řeší omezení celobuněčného řídicího kanálu v LTE vysílaného způsobem broadcast, který neefektivně podporoval vysokofrekvenční pásma (jako mmWave), kde je beamforming pro pokrytí nezbytný. CORESET tedy poskytuje rámec fyzické vrstvy pro škálovatelnou, efektivní a přizpůsobitelnou signalizaci řízení, která je základem veškerého plánování dat a systémových operací v 5G NR.

## Klíčové vlastnosti

- Flexibilní alokace časových a frekvenčních zdrojů (konfigurovatelná množina PRB a doba trvání 1-3 symboly)
- Podpora prokládaného i neprokládaného mapování CCE na REG pro diverzitu nebo beamforming
- Asociace s více množinami prohledávacího prostoru pro různé účely monitorování (UE-specifické, společné)
- Konfigurovatelnost pro každou část šířky pásma (BWP), což umožňuje efektivní širokopásmový provoz
- Asociace se stavy indikátoru konfigurace přenosu (TCI) pro beamformovaný přenos PDCCH
- Podpora více CORESETů na jedno UE pro robustní příjem řídicího kanálu a příjem z více beamů

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)

## Definující specifikace

- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO

---

📖 **Anglický originál a plná specifikace:** [CORESET na 3GPP Explorer](https://3gpp-explorer.com/glossary/coreset/)
