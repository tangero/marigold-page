---
slug: "sss"
url: "/mobilnisite/slovnik/sss/"
type: "slovnik"
title: "SSS – Secondary Synchronization Signal"
date: 2025-01-01
abbr: "SSS"
fullName: "Secondary Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sss/"
summary: "Fyzický signál na fyzické vrstvě v LTE a NR používaný pro vyhledávání buňky a synchronizaci. Spolupracuje s primárním synchronizačním signálem (PSS) a umožňuje uživatelskému zařízení (UE) identifikova"
---

SSS (Secondary Synchronization Signal) je sekundární synchronizační signál, fyzický signál na fyzické vrstvě v LTE a NR, který spolu s PSS umožňuje uživatelskému zařízení (UE) identifikovat fyzické ID buňky (PCI) a dosáhnout časování symbolů během vyhledávání buňky.

## Popis

Sekundární synchronizační signál (SSS) je kritický downlinkový fyzický signál vysílaný základnovou stanicí (eNodeB v LTE, gNB v NR). Jeho primární funkcí je usnadnění procedury vyhledávání buňky, při které uživatelské zařízení (UE) detekuje buňku a synchronizuje se s ní. SSS je vždy vysílán společně s primárním synchronizačním signálem ([PSS](/mobilnisite/slovnik/pss/)). Zatímco PSS poskytuje hrubé časování symbolů a udává jednu část fyzické identity buňky ([PCI](/mobilnisite/slovnik/pci/)), SSS poskytuje zbývající a větší část PCI. Konkrétně v LTE je 504 možných PCI rozděleno do 168 unikátních skupin identit buněk, z nichž každá obsahuje 3 unikátní identity. SSS přenáší identitu skupiny (0-167), zatímco PSS přenáší identitu uvnitř skupiny (0-2). V NR je koncept podobný, ale přizpůsobený pro flexibilnější numerologii a širší šířky pásma; 1008 možných PCI je odvozeno z kombinací sekvencí přenášených na PSS a SSS.

SSS je konstruován pomocí specifické sekvence, například M-sekvence v LTE nebo Goldovy sekvence v NR, která je mapována na specifické zdrojové prvky ([RE](/mobilnisite/slovnik/re/)) v rámci bloku synchronizačního signálu (SSB). V LTE je SSS vysílán na centrálních 62 subnosičích (kromě nosné [DC](/mobilnisite/slovnik/dc/)) posledního [OFDM](/mobilnisite/slovnik/ofdm/) symbolu v časových slotech 0 a 10 v rámci rádiového rámce pro [FDD](/mobilnisite/slovnik/fdd/) a ve specifických podrámcích pro [TDD](/mobilnisite/slovnik/tdd/). V NR se SSS nachází v rámci bloku [SS](/mobilnisite/slovnik/ss/)/PBCH (SSB) a zabírá 127 subnosičů. Přesná časově-frekvenční pozice vůči PSS umožňuje uživatelskému zařízení po detekci obou signálů určit časování systémového rámce (tj. hranici 10ms rádiového rámce).

Při zapnutí nebo během předávání spojení uživatelské zařízení nejprve provádí slepé vyhledávání PSS, čímž získá 5ms časování a podmnožinu kandidátních PCI. Poté vyhledává SSS v očekávaném časovém okně. Úspěšnou detekcí sekvence SSS uživatelské zařízení dekóduje celé PCI a dosáhne synchronizace rámce. Tento proces je odolný vůči vysokým Dopplerovým posunům a počátečním frekvenčním odchylkám. Návrh SSS, včetně vlastností jeho sekvence a mapování, je optimalizován pro spolehlivou detekci za podmínek nízkého poměru signál-šum (SNR), což je klíčové pro výkon na okraji buňky. Dále SSS pomáhá rozlišit buňky používající stejnou sekvenci PSS, čímž předchází nejednoznačnosti v hustých síťových nasazeních.

## K čemu slouží

SSS byl vytvořen k řešení základního problému počátečního zachycení buňky a synchronizace v celulárních sítích. Než může uživatelské zařízení dekódovat jakékoliv systémové informace nebo navázat spojení, musí nejprve najít buňku, určit její identitu a sladit svůj přijímač v čase a frekvenci s vysíláním buňky. Samotný PSS je nedostatečný, protože poskytuje pouze částečnou identitu buňky a informace o časování. SSS dokončuje proces identifikace buňky a poskytuje kritické časování rámce.

Historicky existovaly synchronizační signály v dřívějších standardech, jako UMTS, ale se zavedením OFDMA v LTE byl vyžadován nový synchronizační schéma. Spárovaný návrh PSS a SSS v LTE a NR poskytuje rychlý, spolehlivý a výpočetně efektivní dvoukrokový detekční proces. Tento návrh řeší omezení přístupů s jedním signálem rozdělením detekční složitosti a zlepšením odolnosti vůči rušení a útlumu. Umožňuje rychlé vyhledávání buňky, což je zásadní pro zkrácení doby navazování spojení a zlepšení výkonu při předávání spojení, což přímo ovlivňuje uživatelský zážitek z hlediska zpoždění při sestavování hovoru a spolehlivosti mobility.

V NR se účel rozšiřuje o podporu širšího rozsahu frekvencí (včetně mmWave) a flexibilní numerologie. SSS je jako součást SSB v vyšších frekvencích beamformován. Jeho návrh zajišťuje spolehlivou detekci v různých scénářích nasazení, od širokoplošného pokrytí pod 6 GHz až po cílené pokrytí založené na beamformingu v pásmech milimetrových vln, což byl klíčový motiv pro jeho vývoj z LTE.

## Klíčové vlastnosti

- Přenáší skupinu identity buňky (LTE) nebo část PCI (NR) pro jednoznačnou identifikaci buňky.
- Umožňuje určení hranice 10ms rádiového rámce pro synchronizaci systémového rámce.
- Používá specifické sekvence (M-sekvence v LTE, Goldovy sekvence v NR) navržené pro spolehlivou detekci při nízkém SNR.
- Vysílán na známé časově-frekvenční pozici vůči PSS v rámci bloku synchronizačního signálu.
- Podporuje procedury vyhledávání buňky pro počáteční přístup, předávání spojení a reportování měření.
- Navržen pro robustní výkon i za přítomnosti velkých frekvenčních odchylek a Dopplerova rozptylu.

## Související pojmy

- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.788** (Rel-15) — V2X Phase 2 Technical Report for LTE
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations
- **TS 36.863** (Rel-12) — CRS Interference Mitigation for Homogeneous Networks
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TS 36.894** (Rel-13) — Study on LTE Measurement Gap Enhancement
- **TR 36.976** (Rel-19) — LTE-based 5G Terrestrial Broadcast Overview
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- … a dalších 16 specifikací

---

📖 **Anglický originál a plná specifikace:** [SSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sss/)
