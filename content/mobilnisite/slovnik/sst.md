---
slug: "sst"
url: "/mobilnisite/slovnik/sst/"
type: "slovnik"
title: "SST – Spectral Smoothing Technique"
date: 2026-01-01
abbr: "SST"
fullName: "Spectral Smoothing Technique"
category: "Physical Layer"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sst/"
summary: "Technika zpracování signálu aplikovaná na základnový signál před vysíláním za účelem snížení jeho poměru špičkového a průměrného výkonu (PAPR). Vysoký PAPR nutí výkonové zesilovače pracovat neefektivn"
---

SST je technika zpracování signálu aplikovaná před vysíláním za účelem snížení poměru špičkového a průměrného výkonu (PAPR), čímž se zlepšuje účinnost výkonového zesilovače v systémech založených na OFDM, jako jsou LTE a 5G NR.

## Popis

Technika spektrálního vyhlazování (SST) je klíčový algoritmus zpracování signálu používaný v bezdrátových systémech založených na ortogonálním frekvenčním multiplexu ([OFDM](/mobilnisite/slovnik/ofdm/)) a OFDM s rozprostřením pomocí diskrétní Fourierovy transformace (DFT-s-OFDM), včetně LTE a 5G New Radio (NR). Jejím hlavním účelem je snížení poměru špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)) vysílaného vysokofrekvenčního signálu. OFDM signály jsou inherentně složeny z více ortogonálních subnosných, které mohou konstruktivně interferovat a vytvářet vysoké okamžité výkonové špičky. Tyto špičky nutí výkonový zesilovač ([PA](/mobilnisite/slovnik/pa/)) ve vysílači pracovat s velkou rezervou od svého saturačního bodu, aby se předešlo nelineárnímu zkreslení a spektrálnímu přeslechu, což vede k velmi nízké účinnosti. SST funguje tak, že strategicky upravuje signál v časové oblasti, aby tyto špičky řízeně ořezala.

Z architektonického hlediska se SST aplikuje v řetězci zpracování základnového pásma po vygenerování časového OFDM nebo DFT-s-OFDM signálu a před digitálně-analogovým převodem. Tato technika zahrnuje analýzu obálky signálu a identifikaci vzorků, které překračují předem stanovenou prahovou hodnotu. Namísto prostého tvrdého ořezu, které způsobuje významný mimo-pásmový vyzařovaný výkon a zkreslení v pásmu, SST využívá sofistikovanější přístup založený na okénkování nebo filtrování. Běžnou metodou je vynásobení segmentu signálu s vysokou špičkou speciálně navrženým vyhlazovacím oknem (např. oknem s kosinusovým průběhem) v časové oblasti. Toto lokalizované vyhlazení efektivně snižuje velikost špičky a zároveň se snaží udržet výsledné spektrální zkreslení v rámci přidělené šířky kanálu.

Z provozní perspektivy zahrnuje algoritmus SST kompromis mezi snížením PAPR a věrností signálu. Klíčové parametry zahrnují prahovou hodnotu ořezu a tvar/dobu trvání vyhlazovacího okna. Agresivnější prahová hodnota a vyhlazení vedou k většímu snížení PAPR, ale zvyšují velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)) a mohou zhoršit výkon z hlediska chybovosti ([BER](/mobilnisite/slovnik/ber/)). Vyhlazený signál je poté přiveden do PA. Snížením PAPR umožňuje SST, aby PA pracovala blíže svému saturačnímu bodu (s menší rezervou), což významně zlepšuje její účinnost. To je zvláště důležité pro vysílače uživatelského zařízení (UE), kde je klíčová životnost baterie, a pro vysílače základnových stanic, kde jsou spotřeba energie a provozní náklady hlavními faktory. Tato technika je standardizována, aby byla zajištěna předvídatelná výkonnost a interoperabilita, přičemž konkrétní implementační pokyny jsou uvedeny ve specifikacích 3GPP pro testování shody vysílače.

## K čemu slouží

SST existuje, aby řešila základní nevýhodu vícekanálových modulačních schémat, jako je [OFDM](/mobilnisite/slovnik/ofdm/), kterou je jejich vysoký poměr špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)). Vysoký PAPR byla známá výzva již od počátků nasazování OFDM pro buněčné standardy, jako je LTE. Bez zmírnění vyžaduje použití drahých, vysoce lineárních výkonových zesilovačů s velkou rezervou, což vede k nízké účinnosti, zvýšenému odvodu tepla, vyšším nákladům a kratší výdrži baterie mobilních zařízení. Rané systémy touto neefektivitou trpěly, což omezovalo přenosové rychlosti a formát zařízení.

Motivací pro standardizaci technik jako SST bylo umožnit praktické a ekonomické nasazení vysokorychlostních buněčných sítí založených na OFDM. Řeší problém neefektivity vysílače přímo na úrovni zdrojového signálu. Před těmito technikami byla řešení z velké části v analogové oblasti (jako použití lineárnějších [PA](/mobilnisite/slovnik/pa/)) nebo jiné digitální techniky, jako je rezervace tónů nebo selektivní mapování, které mohly mít vyšší složitost nebo režii. SST poskytuje relativně nízkonákladové, efektivní řešení v digitální části vysílače, které může být integrováno do čipových sad základnového pásma. Její vznik byl hnán potřebou splnit přísné požadavky na spektrální masku vysílače při maximalizaci účinnosti výkonového zesilovače, což je klíčový faktor pro komerční úspěch zařízení a infrastruktury 4G a 5G.

## Klíčové vlastnosti

- Snižuje poměr špičkového a průměrného výkonu (PAPR) OFDM/DFT-s-OFDM signálů.
- Funguje v digitální doméně základnového pásma před výkonovým zesilovačem.
- Používá funkce okénkování/vyhlazování v časové oblasti k řízenému ořezávání špiček signálu.
- Zlepšuje účinnost výkonového zesilovače tím, že umožňuje provoz se sníženou rezervou.
- Zahrnuje konstrukční kompromis mezi snížením PAPR a zavedeným zkreslením signálu (EVM).
- Standardizována pro zajištění konzistentního výkonu vysílače a dodržení spektrálních masek.

## Související pojmy

- [PAPR – Peak-to-Average Power Ratio](/mobilnisite/slovnik/papr/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.851** (Rel-19) — Feasibility Study on Network Sharing Aspect
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 31.105** (Rel-19) — Slice Subscriber Identity Module (SSIM) Application
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 46.020** (Rel-19) — GSM Half Rate Speech Codec Specification

---

📖 **Anglický originál a plná specifikace:** [SST na 3GPP Explorer](https://3gpp-explorer.com/glossary/sst/)
