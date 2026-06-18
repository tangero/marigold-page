---
slug: "ptrs"
url: "/mobilnisite/slovnik/ptrs/"
type: "slovnik"
title: "PTRS – Phase-Tracking Reference Signal"
date: 2025-01-01
abbr: "PTRS"
fullName: "Phase-Tracking Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ptrs/"
summary: "Referenční signál v sestupné i vzestupné lince zavedený v 5G NR pro odhad a kompenzaci fázového šumu, zejména ve vysokofrekvenčních pásmech (mmWave). Je klíčový pro udržení koherentní demodulace a dos"
---

PTRS je referenční signál v sestupné i vzestupné lince v 5G NR, který odhaduje a kompenzuje fázový šum, zejména ve vysokofrekvenčních pásmech, aby byla zachována koherentní demodulace.

## Popis

Phase-Tracking Reference Signal (PTRS) je specializovaný referenční signál ve fyzické vrstvě 5G New Radio (NR) navržený ke sledování a kompenzaci zkreslení způsobených fázovým šumem. Fázový šum je náhodná fluktuace fáze signálu oscilátoru, která se stává významným limitujícím faktorem výkonu při vyšších kmitočtech nosné, jako jsou pásma milimetrových vln (mmWave), a při širších šířkách kanálu. PTRS funguje tak, že vkládá známé pilotní symboly na konkrétní subnosné a [OFDM](/mobilnisite/slovnik/ofdm/) symboly v rámci časově-frekvenční mřížky zdrojů. Příjemce odhadne fázový drift porovnáním přijatých PTRS symbolů se známou vyslanou sekvencí, což mu umožní aplikovat fázovou korekci na symboly nesoucí data.

Z architektonického hlediska je PTRS konfigurovatelný pro každé UE a pro každou část šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)). Jeho hustota v čase a frekvenci je klíčovým parametrem řízeným signalizací Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)). Časová hustota (periodicita v OFDM symbolech) se volí na základě očekávané koherenční doby fázového šumu, zatímco frekvenční hustota (počet subnosných) vychází z koherenční šířky pásma. Tato konfigurovatelnost umožňuje kompromis mezi režií a přesností sledování, přizpůsobující se různým schopnostem UE, kmitočtům nosné a případům použití. PTRS může být vysílán jak v sestupné lince (z gNB do UE), tak ve vzestupné lince (z UE do gNB) a jeho přítomnost je vázána na modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) a naplánovanou velikost fyzického bloku zdrojů ([PRB](/mobilnisite/slovnik/prb/)).

Během provozu plánovač gNB rozhoduje, zda pro dané UE přidělí PTRS, na základě faktorů jako nakonfigurovaná tabulka MCS (modulace vyššího řádu jako 256QAM nebo 1024QAM jsou na fázový šum citlivější), kmitočet nosné a hlášení schopností UE. Blok odhadu kanálu a ekvalizace přijímače použije PTRS k odvození odhadu fázové chyby, který je pak použit k otočení konstelací přijatých datových symbolů zpět do jejich správné fázové pozice. Tento proces je kritický pro udržení nízké míry chyb, zejména ve scénářích s vysokou propustností využívajících široká pásma na mmWave kmitočtech, kde může fázový šum lokálního oscilátoru výrazně degradovat výkon spoje.

## K čemu slouží

PTRS byl zaveden v 5G NR Release 15, aby řešil zásadní problém fyzické vrstvy, který se stal akutním s přijetím mmWave spektra a velmi širokých šířek kanálu. Tradiční systémy LTE, pracující primárně pod 6 GHz, zaznamenávaly relativně nízký fázový šum a běžné referenční signály ([CRS](/mobilnisite/slovnik/crs/), [DM-RS](/mobilnisite/slovnik/dm-rs/)) byly pro odhad kanálu a ekvalizaci dostačující. Nicméně na kmitočtech nad 24 GHz se fázový šum generovaný praktickými oscilátory významně zvyšuje, což způsobuje rychlé a náhodné fázové rotace, které narušují konstelace modulací vyššího řádu (QAM).

Primární problém, který PTRS řeší, je neschopnost standardních demodulačních referenčních signálů (DM-RS) sledovat rychlé fázové variace. DM-RS se používají pro odhad složené odezvy kanálu (včetně fázových posunů), ale jsou obvykle v čase rozmístěny příliš daleko od sebe, aby mohly sledovat rychlé změny fázového šumu. Bez PTRS by fázový šum vedl k nezmenšitelné chybové základně, což by znemožnilo použití modulačních schémat s vysokou spektrální účinností a omezilo by špičkové přenosové rychlosti v nejslibnějších vysokofrekvenčních pásmech 5G. PTRS poskytuje specializovaný, hustší pilotní signál přímo navržený ke sledování těchto rychlých fázových fluktuací.

Jeho zavedení bylo motivováno potřebou umožnit praktickou mmWave komunikaci pro 5G. Tím, že poskytuje mechanismus pro odhad a kompenzaci fázového šumu v reálném čase, PTRS zajišťuje, že teoretické výhody širokých mmWave pásem mohou být realizovány v reálném hardwaru s neideálními oscilátory. Řeší klíčové omezení předchozích systémů založených na OFDM při jejich škálování do nových kmitočtových režimů a zajišťuje robustní výkon pro rozšířené mobilní širokopásmové připojení (eMBB) a další případy použití 5G.

## Klíčové vlastnosti

- Specializovaný referenční signál pro odhad a kompenzaci fázového šumu
- Konfigurovatelná časová a frekvenční hustota prostřednictvím RRC a DCI
- Aktivace vázána na provoz s vysokým MCS, vysokým kmitočtem a širokou šířkou pásma
- Podpora v sestupných i vzestupných přenosech
- Konfigurace specifická pro UE, umožňující adaptivní režii podle potřeby
- Kritický faktor pro použití modulací vyššího řádu QAM (např. 1024QAM) v mmWave pásmech

## Související pojmy

- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [BWP – Bandwidth Part](/mobilnisite/slovnik/bwp/)
- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PTRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptrs/)
