---
slug: "epre"
url: "/mobilnisite/slovnik/epre/"
type: "slovnik"
title: "EPRE – Energy Per Resource Element"
date: 2025-01-01
abbr: "EPRE"
fullName: "Energy Per Resource Element"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/epre/"
summary: "EPRE je průměrná energie vysílaná na jeden zdrojový element (Resource Element, RE) v OFDM mřížce LTE a NR. Jde o základní parametr fyzické vrstvy pro řízení výkonu, výpočet rozpočtu rádiového spoje a"
---

EPRE je průměrná energie vysílaná na jeden zdrojový element (Resource Element) v OFDM mřížce LTE a NR, která slouží jako základní parametr fyzické vrstvy pro řízení výkonu a výpočet rozpočtu rádiového spoje.

## Popis

Energy Per Resource Element (EPRE, energie na zdrojový element) je klíčový parametr fyzické vrstvy ve specifikacích 3GPP pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). Kvantifikuje průměrný vysílací výkon přidělený jednomu zdrojovému elementu (Resource Element) v časově-frekvenční mřížce ortogonálního multiplexu s frekvenčním dělením ([OFDM](/mobilnisite/slovnik/ofdm/)). Zdrojový element je nejmenší jednotka fyzického zdroje, představující jeden podkmitočet po dobu trvání jednoho OFDM symbolu. EPRE není přímo měřený okamžitý výkon, ale konfigurovaná a standardizovaná referenční úroveň. Typicky je definován vzhledem k celkovému vysílacímu výkonu buňky nebo k výkonu referenčního signálu, jako je buňkově specifický referenční signál ([CRS](/mobilnisite/slovnik/crs/)) v LTE nebo blok synchronizačního signálu/fyzického vysílacího kanálu (SS/PBCH) v NR.

Tento parametr je zásadní pro přidělování výkonu v downlinku a pro činnost přijímače UE. Síť konfiguruje výkonové poměry, jako je poměr EPRE pro [PDSCH](/mobilnisite/slovnik/pdsch/) k EPRE pro CRS (ρ_A a ρ_B v LTE) nebo přidělení výkonu pro různé kanály a signály vzhledem k SSB. UE tyto signalizované nebo předdefinované poměry používá k odhadu efektivní síly signálu pro datový kanál (PDSCH) a řídicí kanály ([PDCCH](/mobilnisite/slovnik/pdcch/)), což je nezbytné pro přesný odhad kanálu, demodulaci a dekódování. Tento koncept zajišťuje předvídatelné rozdělení výkonu v šířce pásma a v čase a řeší kompromis mezi pokrytím pro uživatele na okraji buňky (kteří potřebují vyšší výkon) a kapacitou/interferencí pro uživatele ve středu buňky.

Nastavení EPRE je nedílnou součástí správy rádiových zdrojů (RRM) a adaptace rádiového spoje. Ovlivňuje klíčové ukazatele výkonu, jako je propustnost a míra chybových bloků ([BLER](/mobilnisite/slovnik/bler/)). Například vyšší EPRE pro PDSCH vzhledem k referenčnímu signálu zlepšuje poměr signálu k interferenci a šumu (SINR) pro příjem dat, což může umožnit použití modulačně-kódového schématu ([MCS](/mobilnisite/slovnik/mcs/)) vyššího řádu. Síťové algoritmy tyto poměry dynamicky upravují na základě zpětné vazby od UE ([CQI](/mobilnisite/slovnik/cqi/)), rozhodnutí o plánování a podmínek interference. Specifikace jako 36.213 (LTE) a 38.213 (NR) podrobně popisují postupy a vzorce pro řízení výkonu, které určují, jak jsou parametry související s EPRE stanoveny a aplikovány.

## K čemu slouží

EPRE bylo zavedeno, aby poskytlo standardizovanou a detailní metodu pro definici a řízení distribuce vysílacího výkonu v rozhraní založeném na OFDM u LTE (od Release 8). Předchozí mobilní systémy často používaly agregovanější metriky výkonu. Přechod na OFDMA vyžadoval detailní výkonový model, protože zdroje jsou přidělovány v malých časově-frekvenčních blocích více uživatelům současně. Bez jasné definice, jako je EPRE, by bylo nejednoznačné, kolik výkonu je věnováno konkrétním datovým symbolům uživatele oproti celobuněčným referenčním signálům, což by vedlo k nekonzistentnímu výkonu přijímače a neefektivní koordinaci interference.

Jeho primárním účelem je umožnit přesnou analýzu rozpočtu rádiového spoje, předvídatelnou činnost přijímače UE a efektivní plánování sítě. Definováním výkonu na základní zdrojový element mohou inženýři přesně vypočítat sílu přijímaného signálu pro jakýkoli kanál, což zajišťuje, že UE mohou správně nastavit své automatické řízení zesílení a prahy demodulace. Řeší problém nejednoznačnosti výkonu v prostředí sdíleného kanálu, což je klíčové pro pokročilé funkce jako koordinované vícebodové vysílání/příjem (CoMP) a vylepšená koordinace interference mezi buňkami (eICIC), kde je nezbytná přesná znalost úrovní vysílacího výkonu sousedních buněk. EPRE poskytuje základní stavební kámen pro všechny vzorce řízení výkonu v downlinku specifikované v 3GPP.

## Klíčové vlastnosti

- Definuje vysílací výkon na nejmenší časově-frekvenční jednotku OFDM (zdrojový element – Resource Element).
- Slouží jako reference pro výkonové poměry mezi datovými kanály (PDSCH) a referenčními signály (např. CRS, SSB).
- Umožňuje přijímači UE přesně odhadnout kanál a provést demodulaci.
- Základní prvek pro výpočet rozpočtu rádiového spoje v downlinku a plánování pokrytí.
- Používá se v algoritmech dynamického řízení výkonu pro správu interference a adaptaci rádiového spoje.
- Specifikováno odlišně pro různé fyzické kanály a signály v downlinku (PDSCH, PDCCH, CSI-RS).

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [CRS – Cell-specific Reference Signals](/mobilnisite/slovnik/crs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR
- **TR 38.884** (Rel-18) — Technical Report
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [EPRE na 3GPP Explorer](https://3gpp-explorer.com/glossary/epre/)
