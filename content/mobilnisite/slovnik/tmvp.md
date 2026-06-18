---
slug: "tmvp"
url: "/mobilnisite/slovnik/tmvp/"
type: "slovnik"
title: "TMVP – Temporal Motion Vector Prediction"
date: 2025-01-01
abbr: "TMVP"
fullName: "Temporal Motion Vector Prediction"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tmvp/"
summary: "Technika video kódování používaná v pokročilých kodecích jako HEVC (H.265) a VVC (H.266), která predikuje pohybové vektory pro blok využitím pohybových informací z dříve zakódovaného referenčního sním"
---

TMVP je technika video kódování, která predikuje pohybové vektory bloku pomocí pohybových informací z dříve zakódovaného referenčního snímku za účelem zvýšení účinnosti komprese.

## Popis

Temporal Motion Vector Prediction (TMVP) je klíčový predikční nástroj v moderních standardech komprese videa standardizovaných 3GPP, zejména v rámci kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) a pro video služby. Funguje na principu časové redundance – myšlenky, že se objekty pohybují předvídatelným způsobem napříč po sobě jdoucími snímky video sekvence. Namísto zakódování pohybového vektoru (který popisuje posun bloku pixelů z jednoho snímku do druhého) od nuly pro každý blok v každém snímku umožňuje TMVP kodéru predikovat tento vektor na základě pohybových informací již zakódovaných pro prostorově odpovídající blok v dříve dekódovaném referenčním snímku, typicky v kolineárním snímku z jiného časového okamžiku.

Technický proces funguje následovně: Pro aktuálně kódovaný blok („aktuální blok“) kodér a dekodér identifikují „kolineární blok“ v předem definovaném referenčním snímku, což je často snímek z jiné vrstvy v hierarchické predikční struktuře (např. snímek z předchozí [GOP](/mobilnisite/slovnik/gop/)). Načtou se pohybové vektory asociované s tímto kolineárním blokem. Tyto uložené vektory jsou následně škálovány na základě časové vzdálenosti mezi aktuálním snímkem a jeho referenčním snímkem versus vzdálenosti mezi kolineárním snímkem a jeho referenčním snímkem. Tento škálovaný pohybový vektor se stává kandidátem v seznamu potenciálních prediktorů pohybového vektoru (MVP). Kodér vybere nejlepšího prediktora z tohoto seznamu a potřebuje zakódovat pouze malý rozdíl (rozdíl pohybového vektoru, MVD), pokud predikce není dokonalá, čímž ušetří značné množství bitů.

V architektuře kodeku je TMVP klíčovou součástí modulu mezisnímkové predikce. Funguje spolu s prostorovou predikcí pohybového vektoru (která používá vektory ze sousedních bloků ve stejném snímku) a vytváří robustní sadu kandidátů prediktorů. Integrace TMVP je obzvláště účinná u video sekvencí s konzistentním lineárním pohybem, jako jsou panoramatické záběry nebo rolující text, kde se pohyb objektu v čase mění jen málo. Díky využití této časové korelace TMVP významně snižuje přenosovou rychlost potřebnou k reprezentaci pohybových informací, což je hlavní složka celkového bitového toku. Tímto uvolněný bitový rozpočet pak může být přerozdělen ke zlepšení kódování reziduí (detailů textury) nebo ke snížení celkové velikosti souboru, což přímo přispívá k vyšší účinnosti komprese, která je zásadní pro mobilní streamování videa a video telefonii přes buňkové sítě s omezenou přenosovou kapacitou.

## K čemu slouží

TMVP byl vyvinut k řešení základní výzvy komprese videa: snížení přenosové rychlosti při zachování percepční kvality. Rané video kodeky jako H.263 a MPEG-4 Part 2 se silně spoléhaly na jednodušší formy pohybové kompenzace. S rostoucími nároky na rozlišení a snímkovou frekvenci se bitová cena přenosu pohybových vektorů stala významnou režií. Vytvoření TMVP bylo motivováno pozorováním, že pohyb je často v čase perzistentní; objekt pohybující se v jednom směru ve snímku N se s vysokou pravděpodobností bude podobným směrem pohybovat i ve snímku N+1.

Tato technika řeší problém neefektivního kódování pohybových vektorů přímým využitím časové redundance, což je dimenze, kterou dřívější metody pouze prostorové predikce plně nevyužívaly. Před jejím přijetím musely kodéry kódovat pohybové vektory explicitněji nebo se spoléhat pouze na prostorové sousedy, což mohlo selhávat u objektů nově vstupujících do snímku nebo u scén se složitým pohybem. TMVP poskytuje účinný mechanismus dlouhodobé predikce, který je obzvláště cenný v konfiguracích kódování s nízkým zpožděním a náhodným přístupem používaných v reálném čase (jako jsou videohovory) a adaptivním streamování. Jeho zařazení do standardů jako [HEVC](/mobilnisite/slovnik/hevc/) (z něhož jsou odvozeny video kodekové profily 3GPP) bylo klíčovým faktorem pro dosažení přibližně 50% snížení přenosové rychlosti ve srovnání s jeho předchůdcem H.264/[AVC](/mobilnisite/slovnik/avc/) při stejné kvalitě videa, což umožnilo služby videa ve vysokém a ultra vysokém rozlišení na mobilních sítích.

## Klíčové vlastnosti

- Predikuje pohybové vektory pomocí dat z časově kolineárního bloku
- Používá škálování pohybového vektoru na základě vzdáleností v pořadí snímků (POC)
- Generuje kandidáty pro seznam prediktorů pohybového vektoru (MVP)
- Velmi účinné pro sekvence s perzistentním lineárním pohybem
- Snižuje počet bitů potřebných pro kódování rozdílu pohybového vektoru (MVD)
- Integrováno do mezisnímkové predikce moderních kodeků (HEVC, VVC)

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [POC – Push To Talk Over Cellular](/mobilnisite/slovnik/poc/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [TMVP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmvp/)
