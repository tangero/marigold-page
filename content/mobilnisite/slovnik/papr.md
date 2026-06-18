---
slug: "papr"
url: "/mobilnisite/slovnik/papr/"
type: "slovnik"
title: "PAPR – Peak-to-Average Power Ratio"
date: 2025-01-01
abbr: "PAPR"
fullName: "Peak-to-Average Power Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/papr/"
summary: "Metrika vyjadřující poměr mezi okamžitým špičkovým výkonem a průměrným výkonem vysílaného signálu. Vysoký PAPR vyžaduje použití drahých, neefektivních výkonových zesilovačů s velkou rezervou (back-off"
---

PAPR je poměr okamžitého špičkového výkonu signálu k jeho průměrnému výkonu. Představuje zásadní výzvu v systémech využívajících OFDM, jako jsou LTE a NR, protože vysoký PAPR vyžaduje použití energeticky neefektivních výkonových zesilovačů.

## Popis

Poměr špičkového a průměrného výkonu (Peak-to-Average Power Ratio, PAPR) je základní metrikou v digitálních komunikacích, zejména pro vícekanálové modulační schémata jako ortogonální multiplex s frekvenčním dělením ([OFDM](/mobilnisite/slovnik/ofdm/)) používaný v 3GPP LTE a NR. Matematicky je definován jako PAPR = (P_peak) / (P_avg), kde P_peak je maximální okamžitý výkon vysílaného signálu a P_avg je jeho průměrný výkon v čase. Vysoký PAPR signalizuje, že signál má velké, avšak nepříliš časté špičky vzhledem ke své střední úrovni. Tyto špičky vznikají, když se fáze více ortogonálních podnosných konstruktivně sečtou, čímž vytvoří tvar vlny s vysokou amplitudou. Statistické rozdělení PAPR se často charakterizuje pomocí doplňkové distribuční funkce (CCDF), která vykresluje pravděpodobnost, že PAPR překročí určitou prahovou hodnotu.

Ve vysílacím řetězci představuje signál s vysokým PAPR hlavní výzvu pro výkonový zesilovač ([PA](/mobilnisite/slovnik/pa/)). Aby se předešlo zkreslení signálu (ořezávání) a spektrálnímu přesahu, který by porušoval emisní masky, musí PA pracovat s výraznou výkonovou rezervou (back-off) od svého saturačního bodu. Tato rezerva zajišťuje, že zesilovač zůstává ve své lineární oblasti i během špiček signálu, ale drasticky snižuje jeho energetickou účinnost. Pro uživatelská zařízení (UE) to přímo znamená vyšší spotřebu energie a kratší výdrž baterie. U základnových stanic to zvyšuje provozní náklady a nároky na chlazení. Řízení PAPR tedy není pouze otázkou kvality signálu, ale kritickým ekonomickým a konstrukčním omezením.

Specifikace 3GPP se problematikou analýzy a technik pro snížení PAPR zabývají v řadě technických zpráv a specifikací. Tyto dokumenty hodnotí charakteristiky PAPR různých tvarů vln, včetně DFT-s-OFDM (používaného pro uplink v LTE a NR k dosažení nižšího PAPR než u čistého OFDM) a [CP-OFDM](/mobilnisite/slovnik/cp-ofdm/). Specifikace definují referenční metody měření a poskytují analýzu dopadu na požadavky na výkonové zesilovače. Mezi techniky pro snížení PAPR, které jsou v těchto specifikacích často studovány, patří rezervace tónů (tone reservation), selektivní mapování (selective mapping) a ořezávání s filtrací (clipping and filtering). Volba tvaru vlny a techniky pro snížení PAPR je klíčovým kompromisem v návrhu systému, který vyvažuje spektrální účinnost, implementační složitost a účinnost výkonového zesilovače.

## K čemu slouží

Účelem definice a analýzy PAPR v rámci standardů 3GPP je kvantifikovat a řídit hlavní nevýhodu vysoce spektrálně účinné [OFDM](/mobilnisite/slovnik/ofdm/) modulace zvolené pro LTE a 5G NR. Odolnost OFDM vůči vícecestnému útlumu a jeho vhodnost pro [MIMO](/mobilnisite/slovnik/mimo/) a široká pásma z něj učinily preferovanou technologii, ale jeho inherentně vysoký PAPR byla významná známá nevýhoda. Standardizace jeho analýzy zajišťuje konzistentní hodnocení napříč odvětvím a podporuje vývoj kompatibilního a účinného hardwaru.

Historicky měly jednokanálové modulace používané v dřívějších systémech, jako je GSM, konstantní obálku a tedy velmi nízký PAPR, což umožňovalo použití vysoce účinných nelineárních výkonových zesilovačů. Přechod na OFDM pro širokopásmové služby s vysokou přenosovou rychlostí vytvořil novou sadu výzev pro návrh výkonových zesilovačů. Bez pečlivého řízení PAPR by se náklady, velikost a spotřeba energie zařízení staly neúnosnými, zejména pro mobilní zařízení napájená bateriemi. Specifikace 3GPP poskytují společný rámec potřebný pro výrobce čipových sad, výrobce zařízení a dodavatele síťových prvků k návrhu interoperabilních řešení, která splňují výkonnostní cíle a zároveň zvládají toto kritické omezení na fyzické vrstvě.

## Klíčové vlastnosti

- Kvantifikuje požadavek na dynamický rozsah výkonových zesilovačů v vícekanálových systémech.
- Kritický výkonnostní parametr pro tvary vln OFDM a DFT-s-OFDM definované v LTE a NR.
- Ovlivňuje volbu mezi CP-OFDM (vyšší PAPR) a DFT-s-OFDM (nižší PAPR) pro uplink.
- Analýza dokumentovaná v technických zprávách a specifikacích 3GPP slouží jako vodítko pro implementaci a testování.
- Podněcuje potřebu algoritmů pro snížení PAPR, jako je ořezávání (clipping), rezervace tónů (tone reservation) a předkódování (precoding).
- Přímo ovlivňuje výdrž baterie uživatelského zařízení (UE) a energetickou účinnost základnových stanic.

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [SC-FDMA – Single Carrier – Frequency Division Multiple Access](/mobilnisite/slovnik/sc-fdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 38.812** (Rel-16) — Study on NOMA for NR
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [PAPR na 3GPP Explorer](https://3gpp-explorer.com/glossary/papr/)
