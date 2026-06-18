---
slug: "sir"
url: "/mobilnisite/slovnik/sir/"
type: "slovnik"
title: "SIR – Signal-to-Interference Ratio"
date: 2025-01-01
abbr: "SIR"
fullName: "Signal-to-Interference Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sir/"
summary: "Základní metrika fyzické vrstvy představující poměr výkonu požadovaného signálu ke kombinovanému výkonu interference a šumu. Je to klíčová míra kvality rádiového spoje, která přímo ovlivňuje výběr mod"
---

SIR je poměr výkonu požadovaného signálu ke kombinovanému výkonu interference a šumu. Slouží jako klíčová metrika kvality rádiového spoje v mobilních sítích.

## Popis

Poměr signálu k interferenci (Signal-to-Interference Ratio, SIR) je bezrozměrná veličina, typicky vyjadřovaná v decibelech (dB), která kvantifikuje kvalitu přijímaného rádiového signálu v bezdrátovém komunikačním systému. Je definován jako poměr výkonu požadovaného signálu (S) k celkovému výkonu interferujících signálů (I) a implicitně i šumu (N), ačkoli tento pojem často zahrnuje šum do složky interference. Vyšší SIR indikuje čistší a silnější požadovaný signál vzhledem k rušivému pozadí, což umožňuje použití modulačních schémat vyšších řádů a nižší kódové redundance, což vede k vyšší datové propustnosti. Naopak nízký SIR vyžaduje robustní, ale spektrálně neefektivní modulaci a kódování k udržení spolehlivosti spoje.

V systémech 3GPP se SIR měří na přijímači, jako je uživatelské zařízení (UE) nebo základnová stanice (NodeB, eNodeB, gNB). Proces měření zahrnuje filtrování a zpracování přijímaného signálu za účelem izolace příspěvku výkonu od zamýšleného vysílače od celkového výkonu ko-kanálové interference, interference z přilehlých kanálů a intersymbolové interference. Pro širokopásmový přístup s kódovým dělením ([WCDMA](/mobilnisite/slovnik/wcdma/)) v UMTS je odhad SIR zvláště klíčový pro rychlé smyčky řízení výkonu. UE odhaduje SIR na vyhrazeném fyzickém kanálu ([DPCH](/mobilnisite/slovnik/dpch/)) a porovnává jej s cílovou hodnotou SIR nastavenou řadičem rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). Na základě tohoto porovnání UE vysílá příkazy řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)), které instruují NodeB, aby zvýšil nebo snížil svůj vysílací výkon, s cílem udržet přijímaný SIR na cílové úrovni, a tím čelit útlumu a problému blízko-daleko.

V LTE a 5G NR, zatímco řízení výkonu zůstává důležité, je SIR (často diskutován jako poměr signálu k interferenci a šumu, [SINR](/mobilnisite/slovnik/sinr/)) primární metrikou pro adaptaci spoje a plánování. Indikátor kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) hlášený UE je odvozen z měření SINR a informuje základnovou stanici, které modulační a kódové schéma ([MCS](/mobilnisite/slovnik/mcs/)) může být podporováno pro další přenos. SIR je také nedílnou součástí pokročilých přijímacích technik, jako je kombinace s potlačením interference ([IRC](/mobilnisite/slovnik/irc/)). Výkon celé rádiové přístupové sítě, včetně pokrytí, kapacity a uživatelského zážitku, je zásadně řízen distribucí SIR napříč buňkami a uživateli. Aktivity plánování a optimalizace sítě se silně spoléhají na predikce a měření SIR, aby zajistily dostatečné překrytí buněk, řídily inter-buněčnou interferenci a nasazovaly funkce jako je vylepšená koordinace inter-buněčné interference (eICIC) v heterogenních sítích.

## K čemu slouží

SIR existuje jako základní metrika fyzické vrstvy pro objektivní posouzení životaschopnosti a kvality rádiového komunikačního spoje v prostředí omezeném interferencí. Na rozdíl od jednoduchých indikátorů síly přijímaného signálu (RSSI) SIR zohledňuje škodlivý vliv interference, která je primárním faktorem omezujícím kapacitu v celulárních sítích kvůli opakovanému využití frekvencí. Jeho základním účelem je poskytovat kvantifikovatelný vstup pro kritické mechanismy řízení v reálném čase, které přizpůsobují přenosové parametry dynamickým rádiovým podmínkám.

Motivace pro jeho přesné měření a použití pramení z potřeby spektrální účinnosti a spolehlivé komunikace. Rané mobilní systémy trpěly přerušenými hovory a špatnou kvalitou, když se uživatelé pohybovali nebo narůstala interference. Zavedení rychlého uzavřeného smyčkového řízení výkonu v UMTS, řízeného měřeními SIR, bylo revolučním krokem ke zmírnění problému 'blízko-daleko' v systémech CDMA a ke snížení zbytečného vysílacího výkonu, čímž se snížila interference a zvýšila kapacita systému. Bez přesného odhadu SIR by bylo řízení výkonu neúčinné, což by vedlo buď k nadměrné interferenci (pokud je výkon příliš vysoký), nebo k přerušeným spojením (pokud je výkon příliš nízký).

Dále, jak se sítě vyvíjely směrem k modulačním schématům vyšších řádů (např. 256QAM, 1024QAM) a komplexním víceanténním (MIMO) schématům v LTE a 5G NR, se tolerance k interferenci snížila. Přesný odhad SIR/SINR se stal ještě kritičtějším pro adaptaci spoje, aby bylo možné vybrat nejvyšší možnou datovou rychlost, kterou kanál může spolehlivě podporovat. Umožňuje síti využívat dobré podmínky kanálu a chránit přenosy během špatných podmínek, což přímo ovlivňuje propustnost pro uživatele a efektivitu sítě. SIR tedy není pouze měřením, ale základním prvkem umožňujícím adaptivní správu rádiových prostředků.

## Klíčové vlastnosti

- Základní metrika pro hodnocení kvality spoje, vyjádřená jako poměr nebo v dB.
- Primární vstup pro rychlé algoritmy řízení výkonu, zejména v systémech WCDMA/UMTS.
- Základní podklad pro odvození indikátoru kvality kanálu (CQI) pro adaptaci spoje v LTE a NR.
- Používá se v plánovacích algoritmech k alokaci prostředků uživatelům s příznivými rádiovými podmínkami.
- Nedílná součást pokročilého návrhu přijímače a technik potlačení interference (např. IRC).
- Klíčový ukazatel výkonnosti (KPI) pro plánování sítě, optimalizaci a benchmarkování výkonu.

## Související pojmy

- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
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
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [SIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sir/)
