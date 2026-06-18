---
slug: "fer"
url: "/mobilnisite/slovnik/fer/"
type: "slovnik"
title: "FER – Frame Erasure Rate / Frame Error Rate"
date: 2025-01-01
abbr: "FER"
fullName: "Frame Erasure Rate / Frame Error Rate"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fer/"
summary: "Frame Erasure Rate (FER) neboli míra chybovosti rámců je měřený poměr chybných nebo zahozených datových rámců k celkovému počtu přenesených rámců. Jedná se o klíčový ukazatel výkonu (KPI) v reálném pr"
---

FER je měřený poměr chybných nebo zahozených datových rámců k celkovému počtu přenesených rámců a slouží jako klíčový ukazatel výkonu (KPI) pro hodnocení kvality a spolehlivosti rádiového spoje napříč technologiemi 3GPP.

## Popis

Frame Erasure Rate (FER), běžně označovaná také jako Frame Error Rate, je základní měřený metrický ukazatel výkonu v systémech 3GPP. Je definována jako poměr počtu datových rámců přijatých s neopravitelnými chybami (a proto typicky zahozených neboli 'vymazaných') k celkovému počtu rámců přenesených za dané časové období. Na rozdíl od prediktivního [FEP](/mobilnisite/slovnik/fep/) je FER empirické, následné měření skutečného výkonu spoje. Vypočítává ji přijímač (uživatelské zařízení UE nebo základnová stanice) poté, kdy selže ověření kontrolního součtu [CRC](/mobilnisite/slovnik/crc/) (cyclic redundancy check) pro přijatý transportní blok nebo rámec.

Měření FER probíhá na různých vrstvách protokolu, nejvýznamněji na fyzické vrstvě pro transportní bloky a na vrstvě [RLC](/mobilnisite/slovnik/rlc/) (Radio Link Control) pro datové pakety. Na fyzické vrstvě se často měří míra chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)), která je pro danou velikost transportního bloku konceptuálně podobná FER. Síť využívá měření FER hlášená UE (např. v indikátorech kvality kanálu [CQI](/mobilnisite/slovnik/cqi/) nebo v hlášeních out-of-sync) a vlastní měření k činění klíčových rozhodnutí o řízení rádiových zdrojů. Patří mezi ně spouštění předávání spojení (handover), úprava schémat modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) prostřednictvím adaptace spoje a změna cílů řízení výkonu.

Specifikace FER jsou rozptýleny v četných dokumentech 3GPP pokrývajících požadavky na služby (řada 22), technické specifikace (řada 25 pro [UTRA](/mobilnisite/slovnik/utra/), řada 38 pro NR) a aspekty výkonu. Tyto specifikace definují cílové hodnoty FER pro různé služby (např. hlas, video, data) za různých podmínek na kanálu. Například pro přepojování okruhů hlasu může být cílem FER pod 1 %, aby byla zachována kvalita na úrovni veřejné telefonní sítě. FER přímo ovlivňuje kvalitu vnímanou uživatelem; vysoká FER vede k zkomolenému zvuku, zamrzání videa nebo pomalému datovému přenosu kvůli retransmisím a řízení zahlcení TCP. Proto je neustálé sledování a minimalizace FER primárním cílem provozu a procesů optimalizace sítě rádiového přístupu.

## K čemu slouží

FER existuje jako univerzální, hmatatelná metrika pro kvantifikaci úspěšnosti přenosu dat přes inherentně nespolehlivé bezdrátové médium. Jejím účelem je poskytnout síťovým operátorům, výrobcům zařízení a normalizačním orgánům společný, měřitelný ukazatel kvality spoje. To umožňuje srovnávání výkonu, odstraňování problémů a zajištění, že jsou dodrženy definované úrovně kvality služeb (QoS). Řeší základní výzvu převodu poruch na fyzické vrstvě (šum, interference, útlum) na metriku dopadu na službu, kterou lze použít pro řízení systému.

Historicky, jak se buněčná technologie vyvíjela z analogové na digitální (GSM), koncept rámcového přenosu si vyžádal metriku chybovosti rámců. Se zavedením služeb s přepojováním paketů v [GPRS](/mobilnisite/slovnik/gprs/), UMTS a dalších generacích význam FER vzrostl, protože datové služby jsou na chyby citlivější než hlas. Vyřešila problém mít objektivní měřítko spolehlivosti na vrstvě 2, které lze přímo vázat na protokoly vyšších vrstev (jako je TCP) a na uživatelský zážitek. Rozsáhlá specifikace cílů pro FER napříč releasy zajišťuje zpětnou kompatibilitu a výkonnostní cíle směrem do budoucna, což pohání neustálé zlepšování konstrukce přijímačů, kódovacích technik a síťových algoritmů za účelem dosažení nižších hodnot FER a tím vyšší spektrální účinnosti.

## Klíčové vlastnosti

- Empiricky měřený poměr chybných rámců k celkovému počtu rámců
- Klíčový KPI pro hodnocení kvality rádiového spoje napříč generacemi 3GPP
- Používá se jako zpětná vazba pro algoritmy řízení výkonu a adaptace spoje
- Definuje cíle QoS pro různé typy služeb (např. hlas, video)
- Měří se na více vrstvách (BLER na fyzické vrstvě, vrstva RLC)
- Přímo ovlivňuje uživatelský zážitek a efektivní datovou propustnost

## Související pojmy

- [FEP – Frame Error Probability](/mobilnisite/slovnik/fep/)
- [BLER – Block Error Rate](/mobilnisite/slovnik/bler/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [FER na 3GPP Explorer](https://3gpp-explorer.com/glossary/fer/)
