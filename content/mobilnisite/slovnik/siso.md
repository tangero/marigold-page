---
slug: "siso"
url: "/mobilnisite/slovnik/siso/"
type: "slovnik"
title: "SISO – Soft-Input-Soft-Output decoder"
date: 2025-01-01
abbr: "SISO"
fullName: "Soft-Input-Soft-Output decoder"
category: "Physical Layer"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/siso/"
summary: "Typ dekodéru kanálu používaný v iterativních dekódovacích schématech, jako jsou turbo kódy a LDPC kódy. Zpracovává pravděpodobnostní ('měkké') vstupní hodnoty představující spolehlivost přijatých bitů"
---

SISO je typ dekodéru kanálu používaný v iterativních schématech, jako jsou turbo kódy, který zpracovává a zpřesňuje pravděpodobnostní hodnoty za účelem zlepšení přesnosti dekódování prostřednictvím zpětné vazby.

## Popis

Dekodér se vstupem a výstupem měkkých rozhodnutí (Soft-Input-Soft-Output, SISO) je základní součástí přijímacího řetězce pro moderní kódy opravující chyby, jako jsou Turbo kódy a kódy s nízkou hustotou parity (Low-Density Parity-Check, [LDPC](/mobilnisite/slovnik/ldpc/)), které jsou klíčové ve standardech 3GPP od [HSPA](/mobilnisite/slovnik/hspa/)+ dále. Jeho činnost je založena na pravděpodobnostních neboli 'měkkých' informacích, na rozdíl od tradičních dekodérů s tvrdým rozhodováním (hard-decision), které zpracovávají pouze binární 1 a 0. Vstupem SISO dekodéru jsou poměry logaritmické věrohodnosti (Log-Likelihood Ratios, LLR) pro každý přijatý bit. LLR je měkká hodnota, která udává jak pravděpodobnou binární hodnotu (znaménko), tak spolehlivost (velikost) tohoto rozhodnutí na základě přijatého signálu a šumu.

Vnitřní architektura SISO dekodéru je přizpůsobena konkrétní struktuře kódu. Pro dekodér Turbo kódu typicky zahrnuje dvě dílčí SISO dekodéry (často založené na algoritmu BCJR nebo [MAP](/mobilnisite/slovnik/map/)), které pracují s dvěma konvolučními kodéry použitými v Turbo kodéru. Proces dekódování je iterativní. V první iteraci první SISO dekodér zpracovává systematické bity a první sadu paritních bitů, přičemž používá počáteční apriorní LLR (často nastavené na nulu). Vytváří exstrinsické informace, což jsou nové pravděpodobnostní informace získané z omezení daných kódem. Tento exstrinsický výstup je proházen (interleaving) a předán jako apriorní vstup druhému SISO dekodéru, který zpracovává proházené systematické bity a druhou sadu paritních bitů. Druhý dekodér také generuje exstrinsické informace, které jsou zpětně deproházeny (de-interleaving) a vráceny prvnímu dekodéru pro další iteraci. Tato smyčka pokračuje po stanovený počet iterací nebo dokud není splněno kritérium konvergence.

Po poslední iteraci SISO dekodér(y) zkombinují intristické LLR z kanálu a akumulované exstrinsické informace, aby vytvořily finální měkké výstupní LLR pro každý bit. Tyto výstupy pak mohou být použity pro tvrdé rozhodnutí (odebráním znaménka) k obnovení původních bitů. Síla SISO dekodéru spočívá v tomto iterativním předávání měkkých informací, které mu umožňuje opravit chyby daleko za možnostmi jednoprůchodového dekodéru s tvrdým rozhodováním. V 3GPP jsou principy SISO dekódování zásadní pro dosažení vysoké spektrální účinnosti a výkonu blízkého Shannonově limitu, vyžadovaného pro vysokorychlostní datové služby v LTE a 5G NR, kde LDPC kódy pro datové kanály také využívají iterativní dekódování šířením přesvědčení (belief propagation), což je forma SISO dekódování na faktografu.

## K čemu slouží

SISO dekodér byl vyvinut, aby uvolnil výkonnostní potenciál iterativních kódů opravujících chyby, především Turbo kódů, které představovaly průlom v teorii kódování kanálu. Tradiční dekodéry s tvrdým rozhodováním (např. Viterbiho dekodéry) činily nevratná rozhodnutí již brzy v procesu a zahazovaly tak cenné informace o spolehlivosti. To omezovalo výkonnostní zisk dosažitelný složitějšími kódy.

Základní problém, který SISO dekódování řeší, je jak efektivně dekódovat kódy s dlouhými bloky a složitými vzájemnými závislostmi mezi bity, jako jsou Turbo a [LDPC](/mobilnisite/slovnik/ldpc/) kódy. Tyto kódy jsou konstruovány tak, aby měly pravděpodobnostní grafickou strukturu, kde jsou bity propojeny paritními omezeními. Účelem SISO dekodéru je iterativně procházet tímto grafem, šířit a zpřesňovat pravděpodobnostní přesvědčení o hodnotě každého bitu. Zachováním a zpracováním měkkých informací v celém procesu dekódování umožňuje dekodéru opravit chyby, které se v raných iteracích jeví jako neopravitelné, protože pozdější iterace využívají rostoucí konsenzus ze struktury kódu k rozřešení nejednoznačností.

Jeho přijetí v 3GPP, počínaje zařazením Turbo kódů pro vysokorychlostní data v Release 5 ([HSDPA](/mobilnisite/slovnik/hsdpa/)) a upevněním v LTE a NR, bylo motivováno neustálou poptávkou po vyšších datových rychlostech v omezeném přenosovém pásmu. Iterativní dekódování umožněné SISO dovoluje systémům pracovat při mnohem nižších poměrech signálu k šumu (Signal-to-Noise Ratio, [SNR](/mobilnisite/slovnik/snr/)) pro danou chybovost, nebo používat modulace vyššího řádu pro dané SNR. To přímo vede k vyšší uživatelské propustnosti a lepšímu pokrytí na okraji buňky. Bez SISO dekodérů by cíle vysoké spektrální účinnosti pro 4G a 5G byly nedosažitelné, což z nich činí základní technologii pro moderní mobilní broadband.

## Klíčové vlastnosti

- Zpracovává a generuje poměry logaritmické věrohodnosti (LLR), čímž zachovává pravděpodobnostní informace o spolehlivosti.
- Umožňuje iterativní dekódovací algoritmy klíčové pro Turbo kódy a LDPC kódy.
- Jádrová součást algoritmu BCJR/MAP pro Turbo dekódování a šíření přesvědčení (belief propagation) pro LDPC.
- Vyměňuje si exstrinsické informace mezi dílčími dekodéry (u Turbo kódů) nebo kontrolními/proměnnými uzly (u LDPC) za účelem zpřesnění odhadů bitů.
- Umožňuje, aby se dekódování blížilo teoretickému Shannonovu limitu kapacity kanálu.
- Základní pro dosažení vysoké spektrální účinnosti a spolehlivosti spoje v datových kanálech LTE a 5G NR.

## Související pojmy

- [LDPC – Low-Density Parity-Check](/mobilnisite/slovnik/ldpc/)

## Definující specifikace

- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TR 37.976** (Rel-19) — MIMO OTA Test Methodology Study
- **TR 37.977** (Rel-19) — MIMO OTA Test Methodology
- **TR 38.812** (Rel-16) — Study on NOMA for NR
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [SISO na 3GPP Explorer](https://3gpp-explorer.com/glossary/siso/)
