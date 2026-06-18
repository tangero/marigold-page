---
slug: "rtwp"
url: "/mobilnisite/slovnik/rtwp/"
type: "slovnik"
title: "RTWP – Received Total Wideband Power"
date: 2025-01-01
abbr: "RTWP"
fullName: "Received Total Wideband Power"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rtwp/"
summary: "RTWP je klíčové měření v sítích UMTS/WCDMA představující celkový přijímaný výkon v celé šířce kanálu základnové stanice. Zahrnuje jak požadované signály, tak interferenci a slouží jako klíčový ukazate"
---

RTWP je celkový přijímaný výkon v celé šířce kanálu základnové stanice UMTS, zahrnující jak požadované signály, tak interferenci, a slouží jako klíčový ukazatel pro řízení zatížení v uplinku a optimalizaci sítě.

## Popis

Received Total Wideband Power (RTWP, celkový přijímaný širokopásmový výkon) je základní měření prováděné přijímači NodeB (základnové stanice) v sítích 3GPP UMTS (Universal Mobile Telecommunications System), které využívají technologii [WCDMA](/mobilnisite/slovnik/wcdma/) (Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)). Kvantifikuje celkový výkon přijímaný přes celou šířku uplink kanálu 5 MHz na anténním konektoru NodeB, zahrnující všechny příspěvky: požadované uživatelské signály, intracelulární a intercelulární interferenci, tepelný šum a jakékoli externí zdroje šumu. Toto měření se typicky vyjadřuje v dBm a je nepřetržitě sledováno fyzickou vrstvou NodeB a hlášeno Radio Network Controlleru ([RNC](/mobilnisite/slovnik/rnc/)) pro zpracování na vyšších vrstvách.

Technické provádění měření RTWP zahrnuje obvody přijímače NodeB, které vzorkují příchozí vysokofrekvenční signál po zesílení s nízkým šumem a filtrování. Výkon je integrován přes celé pásmo 5 MHz, což poskytuje ekvivalent širokopásmového ukazatele síly přijímaného signálu ([RSSI](/mobilnisite/slovnik/rssi/)). Protože WCDMA je systém omezený interferencí, kde všichni uživatelé sdílejí stejné kmitočtové pásmo a jsou odděleni jedinečnými rozprostíracími kódy, RTWP přímo odráží nárůst šumu v uplinku (noise rise) – zvýšení celkového přijímaného výkonu nad úroveň tepelného šumu způsobené aktivními přenosy. RNC využívá hlášení RTWP, často spolu s dalšími měřeními jako [SIR](/mobilnisite/slovnik/sir/) (Signal-to-Interference Ratio), k provádění algoritmů Radio Resource Management ([RRM](/mobilnisite/slovnik/rrm/)), jako je řízení přístupu (admission control), řízení přetížení (congestion control) a řízení výkonu.

Z architektonického hlediska je RTWP nedílnou součástí rozhraní lub mezi NodeB a RNC, kde je předáváno prostřednictvím měřicích hlášení definovaných ve specifikacích 3GPP. Klíčové komponenty zahrnují měřicí hardware NodeB, software RRM v RNC a systémy [OAM](/mobilnisite/slovnik/oam/) (Operations, Administration, and Maintenance), které shromažďují data RTWP pro monitorování výkonu. Jeho role je zásadní pro udržení stability systému; sledováním RTWP může síť předcházet podmínkám přetížení, které by degradovaly kvalitu hovoru a zvýšily počet spadlých hovorů. Také napomáhá koordinaci interference, zejména v heterogenních nasazeních s makro a small buňkami, a podporuje funkce jako enhanced uplink ([HSUPA](/mobilnisite/slovnik/hsupa/)), kde je přesný odhad zatížení klíčový pro plánování.

## K čemu slouží

RTWP byl zaveden, aby řešil jedinečné výzvy správy interference vlastní sítím UMTS založeným na WCDMA. Na rozdíl od přístupu FDMA/TDMA v GSM umožňuje WCDMA více uživatelům vysílat současně na stejné frekvenci, což činí uplink vysoce náchylným k hromadění interference. Bez přesného měření celkového přijímaného výkonu by síť mohla snadno dojít k přetížení, což by vedlo k efektu 'dýchání buňky' (cell breathing), kdy se pokrytí dynamicky zmenšuje pod zatížením, a k vážné degradaci služeb. RTWP poskytuje potřebnou přehlednost o úrovni interference v uplinku, což umožňuje proaktivní řídicí mechanismy.

Hlavním problémem, který RTWP řeší, je správa kapacity a stability uplinku. Monitorováním RTWP může RNC určit, jak blízko se buňka nachází své maximální kapacitě (pole capacity) – teoretickému maximálnímu zatížení – a činit informovaná rozhodnutí o přijetí nebo zablokování nových hovorů, úpravě vysílacích výkonů uživatelů nebo zahájení procedur snížení zatížení. To je nezbytné pro zajištění Quality of Service (QoS) a maximalizaci spektrální účinnosti. Historicky jeho standardizace v 3GPP Release 8 (a odkaz v dřívějších releasech UMTS) formalizovala měřicí postupy, zajistila konzistenci napříč výrobci a umožnila pokročilé funkce RRM.

Účel RTWP navíc zasahuje do plánování a optimalizace sítě. Operátoři využívají dlouhodobé statistiky RTWP k identifikaci ohnisek interference, optimalizaci sklonu antén a plánování rozšíření kapacity. S vývojem směrem k LTE a 5G, kde je v uplinku používáno OFDMA, koncept měření širokopásmového výkonu přetrvává v podobách jako měření interference v uplinku, ale RTWP zůstává základním kamenem pro provoz sítí UMTS a interoperabilitu s novějšími technologiemi během migračních fází.

## Klíčové vlastnosti

- Měří celkový přijímaný výkon přes celou šířku uplink pásma WCDMA 5 MHz
- Klíčový vstup pro algoritmy Radio Resource Management (RRM) a řízení zatížení v uplinku
- Umožňuje detekci interference a nárůstu šumu v uplinku
- Podporuje rozhodování o řízení přístupu (admission control), řízení přetížení a řízení výkonu
- Používá se pro monitorování výkonu sítě a optimalizaci
- Standardizované hlášení prostřednictvím rozhraní lub mezi NodeB a RNC

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TS 25.865** (Rel-10) — Distributed Antenna Enhancements for TDD
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 32.406** (Rel-19) — Performance Management for CN PS Domain
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview

---

📖 **Anglický originál a plná specifikace:** [RTWP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtwp/)
