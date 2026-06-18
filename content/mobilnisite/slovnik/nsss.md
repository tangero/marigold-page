---
slug: "nsss"
url: "/mobilnisite/slovnik/nsss/"
type: "slovnik"
title: "NSSS – Narrowband Secondary Synchronization Signal"
date: 2025-01-01
abbr: "NSSS"
fullName: "Narrowband Secondary Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nsss/"
summary: "Synchronizační signál používaný v Narrowband IoT (NB-IoT) pro vyhledávání buňky a časovou/frekvenční synchronizaci. Pomáhá UE identifikovat skupinu identit fyzické vrstvy buňky a poskytuje časové info"
---

NSSS (úzkopásmový sekundární synchronizační signál) je signál používaný v NB-IoT pro vyhledávání buňky, který umožňuje UE identifikovat skupinu identit fyzické vrstvy buňky a dosáhnout časové a frekvenční synchronizace pro počáteční přístup k síti.

## Popis

Narrowband Secondary Synchronization Signal (NSSS, úzkopásmový sekundární synchronizační signál) je klíčový signál fyzické vrstvy v technologii 3GPP Narrowband Internet of Things (NB-IoT). Je vysílán základnovou stanicí (známou jako [eNB](/mobilnisite/slovnik/enb/) v LTE nebo gNB v NR-NB-IoT), aby pomohl uživatelskému zařízení (UE) v procesu vyhledávání buňky a synchronizace. NSSS je speciálně navržen pro úzkopásmový provoz NB-IoT, který využívá šířku pásma pouze 180 kHz. Funguje ve spojení s Narrowband Primary Synchronization Signal ([NPSS](/mobilnisite/slovnik/npss/)). UE nejprve detekuje NPSS, aby dosáhlo časování symbolů a hrubé frekvenční synchronizace. Následně detekuje NSSS, aby určilo 504 unikátních identit fyzické vrstvy buňky, dosáhlo synchronizace časování rámců (identifikace hranice 80ms rádiového rámce) a zpřesnilo svou frekvenční synchronizaci.

Technicky je NSSS vysílán v subrámu #9 každého sudého rádiového rámce (tj. každých 20 ms) pro režimy provozu in-band a guard-band a v subrámu #9 každého rámce pro samostatný (standalone) režim. Zabírá posledních 11 [OFDM](/mobilnisite/slovnik/ofdm/) symbolů subrámu v rámci šířky pásma 12 subnosičů (180 kHz). Sekvence NSSS je generována na základě Zadoff-Chuovy sekvence, která má dobré autokorelační vlastnosti prospěšné pro přesnou detekci časování. Konkrétní vysílaná sekvence závisí na Physical Cell Identity ([PCI](/mobilnisite/slovnik/pci/)) a čísle systémového rámce ([SFN](/mobilnisite/slovnik/sfn/)), což umožňuje UE odvodit jak identitu buňky, tak 80ms časování rámce. Detekce NSSS poskytuje UE nezbytné informace pro pokračování ve čtení Narrowband Physical Broadcast Channel (NPBCH) a dalších systémových informací.

Architektura NSSS je integrována do mřížky fyzických zdrojů downlinku NB-IoT. Její návrh zohledňuje extrémní cíle rozšíření pokrytí NB-IoT (až 164 dB [MCL](/mobilnisite/slovnik/mcl/)). Proto je opakován dostatečně často (každých 20 ms), aby byl detekovatelný i ve velmi obtížných podmínkách pokrytí, jako jsou sklepy. Struktura signálu také poskytuje odolnost vůči velkým frekvenčním odchylkám, což je běžné u oscilátorů nízkonákladových IoT zařízení. Úspěšná detekce NSSS je předpokladem pro to, aby UE mohlo dekódovat Master Information Block ([MIB](/mobilnisite/slovnik/mib/)) na NPBCH, který obsahuje základní informace, jako je systémová šířka pásma a plánovací informace pro další systémové informační bloky. NSSS je tedy základním prvkem v proceduře počátečního přístupu NB-IoT, který umožňuje zařízením pro hromadnou komunikaci strojového typu (massive [MTC](/mobilnisite/slovnik/mtc/)) efektivně se připojit k síti s minimální spotřebou energie.

## K čemu slouží

NSSS byl vytvořen jako součást standardu NB-IoT, aby splnil potřebu synchronizačního signálu přizpůsobeného jedinečným omezením nasazení pro hromadný IoT. Tradiční synchronizační signály LTE (PSS/SSS) byly navrženy pro širší šířky pásma a jiné případy použití. NB-IoT vyžadovalo signály, které mohou pracovat v rámci velmi úzkého pásma 180 kHz, poskytovat extrémní pokrytí (pro zařízení hluboko v budovách) a umožnit návrh přijímače s nízkou složitostí a nízkým výkonem v UE. NSSS spolu s NPSS řeší problém efektivního a spolehlivého vyhledávání buňky pro zařízení, která mohou mít špatné rádiové podmínky a nízkokvalitní oscilátory.

Řeší specifickou výzvu identifikace jedné z 504 identit buněk v rámci úzkého pásma a zároveň předávání informací o časování rámců. Bez vyhrazeného úzkopásmového synchronizačního signálu by se zařízení NB-IoT musela spoléhat na signály LTE, což by bylo neefektivní nebo nemožné v samostatných nasazeních nebo v oblastech s hlubokým pokrytím, kde není signál LTE detekovatelný. Návrh NSSS umožňuje UE dokončit identifikaci buňky a dosáhnout časové synchronizace pomocí signálů, které jsou vysílány s dostatečnou periodicitou a výkonem, aby splnily cíl maximální ztráty spojení 164 dB.

Historický kontext souvisí s pracovní položkou 3GPP Release 13 pro Cellular IoT, jejímž cílem bylo vyvinout technologii rádiového přístupu optimalizovanou pro hromadnou komunikaci strojového typu. NSSS je klíčovou součástí tohoto nového rozhraní, která umožňuje proceduru počátečního přístupu, která je kritická pro jakýkoli bezdrátový komunikační systém. Jeho zavedení umožnilo nasazení NB-IoT v různých režimech (in-band, guard-band, standalone) s konzistentním a efektivním synchronizačním mechanismem, což byl základní požadavek pro úspěch technologie v připojování miliard nízkopříkonových IoT zařízení široké oblasti.

## Klíčové vlastnosti

- Používá se pro detekci identity buňky (1 z 504 NB-IoT PCI) a synchronizaci časování rámců v NB-IoT
- Vysílán každých 20 ms v subrámu #9, poskytuje časté příležitosti pro detekci
- Založen na Zadoff-Chuových sekvencích pro robustní detekci za nízkého SNR a vysoké frekvenční odchylky
- Zabírá 11 OFDM symbolů v rámci úzkopásmového nosiče 180 kHz
- Spolupracuje s NPSS k dokončení procesu počáteční synchronizace
- Podporuje všechny režimy nasazení NB-IoT: in-band, guard-band a standalone

## Definující specifikace

- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [NSSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsss/)
