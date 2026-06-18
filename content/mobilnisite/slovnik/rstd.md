---
slug: "rstd"
url: "/mobilnisite/slovnik/rstd/"
type: "slovnik"
title: "RSTD – Reference Signal Time Difference"
date: 2025-01-01
abbr: "RSTD"
fullName: "Reference Signal Time Difference"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rstd/"
summary: "RSTD je základní měření pro metodu lokalizace OTDOA (Observed Time Difference of Arrival) v LTE a NR. Představuje relativní časový rozdíl mezi referenčními signály přijatými z buňky sousední a z buňky"
---

RSTD je změřený relativní časový rozdíl mezi referenčními signály přijatými z buňky sousední a z buňky obsluhující, používaný v OTDOA lokalizaci k výpočtu polohy UE pomocí multilaterace.

## Popis

Reference Signal Time Difference (RSTD) je klíčové měření definované pro lokalizaci uživatelského zařízení (UE) v sítích 3GPP LTE a 5G NR. Je to základní měření pro metodu lokalizace [OTDOA](/mobilnisite/slovnik/otdoa/) (Observed Time Difference of Arrival). RSTD je definován jako relativní časový rozdíl mezi okamžikem, kdy UE přijme pozicovací referenční signál ([PRS](/mobilnisite/slovnik/prs/)) ze sousední buňky, a okamžikem, kdy přijme PRS ze své referenční (typicky obsluhující) buňky. Konkrétně RSTD = T_subframe_Rx_neighbor - T_subframe_Rx_reference, kde T_subframe_Rx je čas příchodu začátku subframu obsahujícího PRS. UE toto měření provádí na speciálních pozicovacích referenčních signálech (PRS) s nízkou interferencí, které jsou periodicky vysílány základnovými stanicemi (eNBs v LTE, gNBs v NR). Lokalizační server sítě ([E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE, [LMF](/mobilnisite/slovnik/lmf/) v NR) asistuje UE poskytnutím OTDOA asistenčních dat přes protokol [LPP](/mobilnisite/slovnik/lpp/). Tato data zahrnují konfiguraci PRS (nosná frekvence, šířka pásma, periodicita, muting pattern) a zeměpisné souřadnice kandidátních vysílačů (eNBs/gNBs). UE tyto informace použije k změření RSTD pro více sousedních buněk vzhledem ke své referenční buňce. Tyto změřené hodnoty RSTD jsou pak nahlášeny zpět lokalizačnímu serveru. Server, který zná přesné časové vztahy vysílání mezi buňkami (poskytnuté jinou síťovou entitou, např. základnovou stanicí), použije sadu měření RSTD k provedení výpočtů multilaterace. Každé měření RSTD definuje jednu hyperbolickou linii polohy (LOP). Průsečík více LOP, odvozených z měření RSTD k alespoň třem geograficky rozptýleným buňkám, určí polohu UE. Přesnost měření RSTD, která může být řádu nanosekund, se přímo promítá do přesnosti lokalizace, často s cílem dosáhnout přesnosti pod 10 metrů v ideálních podmínkách.

## K čemu slouží

RSTD a metoda [OTDOA](/mobilnisite/slovnik/otdoa/) byly vyvinuty k poskytnutí síťové, UE-asistované lokalizační metody, která se nespoléhá výhradně na globální družicové polohové systémy ([GNSS](/mobilnisite/slovnik/gnss/)) jako je [GPS](/mobilnisite/slovnik/gps/). Signály GNSS jsou často slabé nebo nedostupné v interiérech a městských kaňonech. Zatímco Cell-ID poskytuje velmi hrubou lokalizaci a Enhanced Cell-ID (E-CID) používá pro střední přesnost časový předstih a úhlová měření, OTDOA prostřednictvím RSTD bylo navrženo pro vyšší přesnost. Zavedení RSTD řešilo potřebu standardizované, škálovatelné metody využívající vlastní infrastrukturu mobilní sítě pro přesné určování polohy. Řeší problém měření nepatrných rozdílů v době letu signálu od více synchronizovaných vysílačů k přijímači. Použití vyhrazených PRS signálů, zavedených spolu s RSTD, bylo motivováno potřebou čistého, kvalitního signálu pro časová měření. Normální buňkové referenční signály (CRS) podléhají interferencím a nejsou optimalizovány pro měření času příchodu. PRS jsou navrženy se specifickými sekvencemi, zvýšenou hustotou a muting patterny ke snížení interference, což umožňuje přesná měření RSTD nezbytná pro přesnou multilateraci. Toto podporuje regulatorní požadavky jako E911, stejně jako komerční služby založené na poloze.

## Klíčové vlastnosti

- Základní měření pro metodu lokalizace OTDOA (Observed Time Difference of Arrival)
- Definován jako relativní časový rozdíl příchodu PRS ze sousední buňky a referenční buňky
- Vyžaduje měření specializovaných pozicovacích referenčních signálů (PRS)
- UE-asistované měření: UE provádí měření RSTD a hlásí jej síťovému lokalizačnímu serveru
- Používáno sítí v algoritmech multilaterace k výpočtu zeměpisných souřadnic UE
- Standardizováno pro LTE (E-UTRA) i NR, s vylepšeními v každé verzi standardu

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [RSTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/rstd/)
