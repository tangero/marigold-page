---
slug: "m-irs"
url: "/mobilnisite/slovnik/m-irs/"
type: "slovnik"
title: "M-IRS – Modified Intermediate Reference System"
date: 2025-01-01
abbr: "M-IRS"
fullName: "Modified Intermediate Reference System"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/m-irs/"
summary: "Standardizovaný zvukový referenční systém definovaný organizací 3GPP pro objektivní testování kvality řeči. Poskytuje konzistentní referenční bod pro hodnocení a porovnávání výkonu řečových kodeků a p"
---

M-IRS je standardizovaný zvukový referenční systém definovaný organizací 3GPP pro objektivní testování kvality řeči kodeků a přenosových systémů.

## Popis

Modified Intermediate Reference System (M-IRS) je klíčová součást rámce standardizace 3GPP pro hodnocení kvality řeči. Nejde o fyzické zařízení, ale o přesně definovaný matematický model, který simuluje frekvenční odezvu konkrétního, historicky významného telefonního sluchátka. Tento model je implementován v softwaru a používá se jako referenční filtr v objektivních měřicích algoritmech, jako je Perceptual Evaluation of Speech Quality ([PESQ](/mobilnisite/slovnik/pesq/)) a jeho nástupce [POLQA](/mobilnisite/slovnik/polqa/). Při hodnocení řečového kodeku nebo síťové trasy je původní čistý řečový signál nejprve přefiltrován modelem M-IRS, aby se simuloval efekt typického přijímacího koncového zařízení. Tento 'modifikovaný' signál pak slouží jako reference, vůči níž je porovnáván degradovaný výstupní signál (po kódování, přenosu a dekódování). Jádrem architektury M-IRS jsou koeficienty digitálního filtru specifikované v 3GPP TS 46.085. Tyto koeficienty definují přenosovou funkci, která přesně replikuje amplitudově-frekvenční odezvu Intermediate Reference System ([IRS](/mobilnisite/slovnik/irs/)) definovaného [ITU-T](/mobilnisite/slovnik/itu-t/), ale s modifikacemi pro lepší reprezentaci určitých regionálních charakteristik telefonů. Systém funguje tak, že tento lineární časově invariantní filtr aplikuje na zvukový signál, potlačuje nebo zesiluje konkrétní frekvenční pásma, aby napodobil nerovnoměrnou odezvu skutečného elektroakustického měniče. Jeho úlohou je zajistit, aby měření kvality nebylo pouze o výkonu digitálního kodeku izolovaně, ale o celkovém zvukovém dojmu, jak by byl vnímán prostřednictvím typického sluchátka, čímž ukotvuje laboratorní testy v praktických, reálných poslechových podmínkách. Tím, že poskytuje tento pevný, neměnný referenční bod, umožňuje M-IRS spravedlivé a konzistentní srovnání různých implementací kodeků, síťových zařízení od různých výrobců a výkonu systému napříč různými releasy 3GPP. Je základním prvkem procesů zajištění kvality, výběru kodeků a optimalizace sítě.

## K čemu slouží

M-IRS byl vytvořen za účelem standardizace a objektivizace procesu hodnocení kvality řeči v digitálních telekomunikačních systémech. Před jeho zavedením byly primární metodou hodnocení kvality kodeků subjektivní poslechové testy, které byly časově náročné, drahé a náchylné k variabilitě. Průmysl potřeboval spolehlivou, opakovatelnou a automatizovanou objektivní metodu. Účelem M-IRS je sloužit jako kontrolovaný, reprodukovatelný 'poslechový terminál' v rámci těchto objektivních měřicích nástrojů. Řeší problém nekonzistentních testovacích podmínek tím, že přesně definuje, jak má být referenční signál před porovnáním akusticky upraven. To zajišťuje, že skóre kvality pro kodek GSM Enhanced Full Rate ([EFR](/mobilnisite/slovnik/efr/)) testovaný v Evropě jsou přímo srovnatelná se skóre pro kodek [EVS](/mobilnisite/slovnik/evs/) testovaný v Asii, protože oba jsou posuzovány vůči stejné simulované charakteristice přijímače. Historicky různé regiony používaly mírně odlišné frekvenční odezvy telefonních sluchátek (např. severoamerické versus evropské charakteristiky). M-IRS, založený na [ITU-T](/mobilnisite/slovnik/itu-t/) [IRS](/mobilnisite/slovnik/irs/), ale s modifikacemi, poskytl jediný globálně přijímaný kompromisní model pro kontext mobilních sítí 3GPP. Jeho vytvoření bylo motivováno potřebou efektivního vývoje kodeků a síťového benchmarkingu během rychlého vývoje od 2G k 3G a dále, kde prokázání lepší nebo srovnatelné kvality hovoru bylo klíčovým konkurenčním a regulatorním požadavkem.

## Klíčové vlastnosti

- Standardizované koeficienty digitálního filtru definované v TS 46.085
- Simuluje frekvenční odezvu typického telefonního sluchátka
- Poskytuje konzistentní referenci pro objektivní měření kvality řeči (např. PESQ, POLQA)
- Umožňuje reprodukovatelné a výrobně neutrální testování řečových kodeků
- Integrální součást ověřování výkonu a compliance testů kodeků v 3GPP
- Základní prvek pro hodnocení kvality hovoru od konce ke konci v mobilních sítích

## Související pojmy

- [PESQ – Perceptual Evaluation of Speech Quality](/mobilnisite/slovnik/pesq/)
- [POLQA – Perceptual Objective Listening Quality Assessment](/mobilnisite/slovnik/polqa/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)

## Definující specifikace

- **TS 46.085** (Rel-19) — GSM Speech Codec Interoperability Test Report

---

📖 **Anglický originál a plná specifikace:** [M-IRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/m-irs/)
