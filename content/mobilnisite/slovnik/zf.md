---
slug: "zf"
url: "/mobilnisite/slovnik/zf/"
type: "slovnik"
title: "ZF – Zero Forcing"
date: 2025-01-01
abbr: "ZF"
fullName: "Zero Forcing"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/zf/"
summary: "Lineární technika zpracování signálu používaná ve víceanténních (MIMO) systémech k eliminaci interference mezi uživateli nebo datovými proudy. Funguje aplikací prekódovací nebo kombinační matice, kter"
---

ZF je lineární technika zpracování signálu v MIMO systémech, která eliminuje interferenci aplikací prekódovací nebo kombinační matice, jež ji na přijímači potlačí, čímž zjednodušuje detekci, ale může zesílit šum.

## Popis

Zero Forcing (ZF) je základní lineární algoritmus používaný ve vícevstupových a vícevýstupových ([MIMO](/mobilnisite/slovnik/mimo/)) bezdrátových komunikačních systémech, což je klíčová technologie v 4G LTE a 5G NR. Jedná se o strategii zpracování signálu používanou na straně vysílače (prekódování) nebo přijímače (kombinace) ke zmírnění interference mezi více datovými proudy vysílanými současně ve stejném časově-frekvenčním zdroji. Základní matematický princip spočívá ve výpočtu pseudoinverze kanálové matice. Tato kanálová matice, označovaná jako H, popisuje komplexní zesílení mezi každou dvojicí vysílací a přijímací antény. Aplikací ZF filtru, což je v podstatě H⁺ (Moore-Penroseova pseudoinverze), se efektivní kombinovaný kanál stane jednotkovou maticí. Tato operace vynutí, aby interference od ostatních proudů na výstupu filtru byla nulová.

Ve scénáři downlink Multi-User MIMO ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)) používá základnová stanice (gNB v 5G, [eNB](/mobilnisite/slovnik/enb/) v LTE) ZF prekódování. Vypočítá prekódovací matici na základě informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) hlášené více uživatelskými zařízeními (UE). Tato matice předem zkreslí vysílané signály tak, že když procházejí skutečným bezdrátovým kanálem, každé UE přijímá pouze svůj zamýšlený signál, zatímco signály pro ostatní UE se na jeho přijímači jeví jako nuly. Naopak v uplink MU-MIMO nebo pro prostorové multiplexování jednoho uživatele může přijímač použít ZF kombinaci. Zde je přijímaný signálový vektor z více antén vynásoben ZF filtrem, aby oddělil prostorově multiplexované proudy a zrušil vzájemné přeslechy mezi nimi.

Klíčovými součástmi jsou odhadovač kanálu, který poskytuje matici H, a jednotka pro zpracování lineární algebry, která počítá pseudoinverzi. Zatímco ZF v ideálním scénáři s vysokým [SNR](/mobilnisite/slovnik/snr/) a dobře podmíněnou kanálovou maticí dokonale ruší interferenci, má významnou nevýhodu: zesílení šumu. Potlačením interference může filtr zesílit šum, zejména když je kanálová matice špatně podmíněná (např. u vysoce korelovaných antén). To činí výkon ZF vysoce závislým na podmínkách kanálu a plánování uživatelů. Jeho role v síti je jako základní, výpočetně jednodušší alternativa k pokročilejším nelineárním technikám, jako je Dirty Paper Coding ([DPC](/mobilnisite/slovnik/dpc/)) nebo iterační přijímače, nabízející dobrý kompromis mezi výkonem a implementační složitostí pro systémy omezené interferencí.

## K čemu slouží

Zero Forcing byl vyvinut k řešení kritického problému interference mezi proudy v prostorově multiplexních [MIMO](/mobilnisite/slovnik/mimo/) systémech. Rané koncepty MIMO slibovaly multiplikativní zisky kapacity vysíláním nezávislých datových proudů z více antén. Bez zpracování by však tyto proudy na přijímači destruktivně interferovaly. Jednoduché přijímače je nedokázaly oddělit, což by negovalo výhody. ZF poskytl matematicky zpracovatelné lineární řešení tohoto problému rušení interference, což umožnilo praktickou realizaci zisků prostorového multiplexování definovaných ve standardech jako LTE a NR.

Jeho vznik byl motivován potřebou implementovatelného zpracování signálu v základnových stanicích a zařízeních. Neoptimální metody, jako je výběr antény, nabízely omezený zisk, zatímco optimální, ale složitá detekce s maximální věrohodností byla výpočetně neúnosná pro mnoho proudů. ZF našel rovnováhu, nabízeje podstatné potlačení interference se zvládnutelnou složitostí (kubickou vzhledem k počtu antén). Vyřešil problém umožnění prostorového sdílení více uživateli, což je nezbytné pro zvýšení kapacity buňky a spektrální účinnosti. Jeho omezení v prostředích citlivých na šum však vedlo k paralelnímu vývoji a přijetí robustnějších technik, jako je zpracování s minimální střední kvadratickou chybou ([MMSE](/mobilnisite/slovnik/mmse/)), které vyvažuje rušení interference s potlačením šumu.

## Klíčové vlastnosti

- Lineární rušení interference pomocí pseudoinverze kanálové matice
- Lze implementovat jako prekódování (na straně vysílače) nebo kombinaci (na straně přijímače)
- Za ideálních podmínek zcela eliminuje interferenci mezi více proudy
- Podléhá zesílení šumu, zejména u špatně podmíněných kanálů
- Výpočetní složitost je O(N³) pro N antén
- Tvoří základ pro pokročilejší hybridní a nelineární prekódovací schémata

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TR 38.877** (Rel-18) — Technical Report
- **TR 38.922** (Rel-19) — Study on IMT Parameters for NR in Higher Bands

---

📖 **Anglický originál a plná specifikace:** [ZF na 3GPP Explorer](https://3gpp-explorer.com/glossary/zf/)
