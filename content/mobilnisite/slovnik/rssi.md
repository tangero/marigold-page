---
slug: "rssi"
url: "/mobilnisite/slovnik/rssi/"
type: "slovnik"
title: "RSSI – Received Signal Strength Indication"
date: 2025-01-01
abbr: "RSSI"
fullName: "Received Signal Strength Indication"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rssi/"
summary: "RSSI je základní měření celkového přijímaného výkonu rádiového signálu v šířce přiděleného kanálu, včetně požadovaného signálu, interference a šumu. Je klíčové pro hodnocení kvality spoje, výběr buňky"
---

RSSI je měření celkového přijímaného výkonu rádiového signálu v šířce přiděleného kanálu, včetně požadovaného signálu, interference a šumu, používané pro hodnocení kvality spoje a rozhodování sítě.

## Popis

Received Signal Strength Indication (RSSI) je základní měření šířkopásmového výkonu prováděné uživatelským zařízením (UE) nebo základnovou stanicí (např. NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB). Kvantifikuje celkový přijímaný výkon ve specifikované šířce pásma přijímače. Toto měření zahrnuje všechny přispívající zdroje: požadovaný signál obslužné buňky, ko-kanálovou interferenci z jiných buněk, interferenci z přilehlých kanálů a tepelný šum. Měření se typicky provádí na mezifrekvenčním ([IF](/mobilnisite/slovnik/if/)) nebo základním pásmu (baseband) signálu přijímače po analogově-digitální konverzi, ale před jakýmkoliv rozprostřením spektra (despreading) nebo dekódováním kanálu. Ve specifikacích 3GPP je RSSI definováno pro různé rádiové přístupové technologie ([RAT](/mobilnisite/slovnik/rat/)) včetně UMTS ([UTRA](/mobilnisite/slovnik/utra/)), LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR. Konkrétní šířka měřeného pásma, referenční bod a metody průměrování jsou podrobně popsány ve specifikacích fyzické vrstvy pro každou RAT (např. TS 25.215 pro UTRA, TS 36.214 pro E-UTRA, TS 38.215 pro NR). RSSI je klíčovým vstupem pro výpočet dalších odvozených metrik. Nejvýznamněji je měření Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/)), což je úzkopásmové měření výkonu specifických referenčních symbolů, často posuzováno v kontextu celkového RSSI pro výpočet poměru signálu k interferenci a šumu ([SINR](/mobilnisite/slovnik/sinr/)) nebo Reference Signal Received Quality ([RSRQ](/mobilnisite/slovnik/rsrq/)). RSRQ je definováno jako (N * RSRP) / RSSI, kde N je počet bloků zdrojů (resource blocks), což spojuje kvalitu referenčního signálu s celkovým přijímaným výkonem. Síť používá RSSI a jeho odvozené metriky pro kritické funkce správy rádiových zdrojů (RRM). Při počátečním výběru a převýběru buňky měří UE RSSI/RSRP sousedních buněk k identifikaci nejlepšího kandidáta. Pro správu mobility trendy RSSI spouštějí měřicí reporty, které síti umožňují rozhodovat o předání hovoru (handover). Dále je RSSI použito v algoritmech řízení výkonu v uplinku, které pomáhají UE upravit svůj vysílací výkon pro kompenzaci útlumu na dráze a interference, čímž zajišťují spolehlivou uplink komunikaci a zároveň minimalizují interferenci pro ostatní uživatele.

## K čemu slouží

RSSI existuje jako základní, na technologii nezávislá metrika pro hodnocení nezpracovaných rádiofrekvenčních (RF) podmínek na přijímači. Jeho primárním účelem je poskytnout hrubou, bezprostřední indikaci celkové síly signálu v provozním kanálu, což je nezbytné pro základní rádiovou funkčnost. Předtím, než byly pro LTE a NR standardizovány sofistikovanější měření specifická pro signál, jako je RSRP, sloužilo RSSI (a jeho protějšek v UMTS, Received Signal Code Power - RSCP) jako primární metrika pro hodnocení kvality buňky. Řeší základní problém určení, zda je přijímač v životaschopné oblasti pokrytí. Bez měření RSSI zařízení nemůže vědět, zda je dostatek RF energie k vůbec pokusu o synchronizaci nebo dekódování vysílacích kanálů. Historicky bylo RSSI základem celulárních systémů již od raného GSM a poskytovalo nezbytný vstup pro algoritmy řídící výběr buňky, předání hovoru (handover) a adaptaci spoje. Zatímco moderní systémy se pro přesnost více spoléhají na čistší metriky jako RSRP, RSSI zůstává nepostradatelné pro výpočet hladiny interference a šumu (prostřednictvím metrik jako RSRQ) a pro operace ve scénářích, kde specifické referenční signály nemusí být spolehlivě detekovatelné, což nabízí robustní záložní měření RF prostředí.

## Klíčové vlastnosti

- Šířkopásmové měření celkového přijímaného výkonu v šířce přiděleného kanálu.
- Zahrnuje požadovaný signál, ko-kanálovou interferenci, interferenci z přilehlých kanálů a tepelný šum.
- Základní vstup pro výpočet odvozených metrik kvality, jako je RSRQ a SINR.
- Používá se pro algoritmy výběru buňky, převýběru buňky a rozhodování o předání hovoru (handover).
- Podporuje řízení výkonu v uplinku tím, že poskytuje míru útlumu na downlink dráze a interference.
- Standardizováno napříč všemi 3GPP RAT (UTRA, E-UTRA, NR) s konkrétními definicemi pro každou technologii.

## Související pojmy

- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [RSRQ – Reference Signal Receiving Quality](/mobilnisite/slovnik/rsrq/)
- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)
- [RSCP – Reference Signal Carrier Phase](/mobilnisite/slovnik/rscp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [RSSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rssi/)
