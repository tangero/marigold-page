---
slug: "sl-prs-rsrp"
url: "/mobilnisite/slovnik/sl-prs-rsrp/"
type: "slovnik"
title: "SL-PRS-RSRP – Sidelink Positioning Reference Signal based Reference Signal Received Power"
date: 2025-01-01
abbr: "SL-PRS-RSRP"
fullName: "Sidelink Positioning Reference Signal based Reference Signal Received Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-prs-rsrp/"
summary: "Měření úrovně přijímaného výkonu Sidelink Positioning Reference Signals (SL-PRS) od vysílajícího UE. Používá se v postranních pozičních postupech k odhadu útlumu na dráze šíření a kvality signálu, čím"
---

SL-PRS-RSRP je naměřená úroveň přijímaného výkonu Sidelink Positioning Reference Signals (pozičních referenčních signálů pro postranní spojení) od vysílajícího UE, používaná v pozičních metodách postranního spoje k odhadu útlumu na dráze šíření a kvality signálu pro odhad vzdálenosti.

## Popis

SL-PRS-RSRP je měření na fyzické vrstvě definované v 3GPP specifikacích 37.571, 38.305 a 38.355. Kvantifikuje lineární průměrný výkon na zdrojových prvcích, které nesou Sidelink Positioning Reference Signals ([SL-PRS](/mobilnisite/slovnik/sl-prs/)) v rámci uvažované šířky měřicího pásma. Konkrétně měří výkon přijímaný ze SL-PRS konkrétního vysílajícího UE, s vyloučením šumu a rušení z jiných zdrojů. Toto měření provádí přijímající UE jako součást technik určování polohy na postranním spoji, jako je Time Difference of Arrival (TDOA) nebo Angle of Arrival (AoA), kde je přesný odhad výkonu klíčový.

Měřicí postup zahrnuje identifikaci a demodulaci symbolů SL-PRS vysílaných cílovým UE přijímajícím UE. SL-PRS jsou specificky navržené sekvence s dobrými autokorelačními a vzájemnými korelačními vlastnostmi, vysílané na předdefinovaných časově-frekvenčních zdrojích. UE měří výkon na těchto zdrojích referenčního signálu, typicky s aplikací filtrování a průměrování pro zmírnění rychlého úniku a zlepšení přesnosti měření. Výsledek je hlášen v dBm a může být použit vyššími vrstvami pozičních protokolů nebo přímo v pozičních algoritmech.

Z architektonického hlediska je měření SL-PRS-RSRP implementováno na fyzické vrstvě UE, přičemž výsledky jsou hlášeny vrstvě Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) nebo vrstvě pozičního protokolu (např. [LPP](/mobilnisite/slovnik/lpp/) přes [SL](/mobilnisite/slovnik/sl/)). Mezi klíčové komponenty patří konfigurace SL-PRS (definující šířku pásma, periodicitu a sekvenci), měřicí šířka pásma a kritéria pro hlášení. Jeho úlohou je poskytnout základní vstup pro odhad útlumu na dráze šíření, což je nezbytné pro poziční metody založené na vzdálenosti. Přesná měření SL-PRS-RSRP umožňují lepší modelování rádiového kanálu, zvyšují přesnost odhadů vzdálenosti mezi UE a zlepšují celkový výkon určování polohy na postranním spoji v aplikacích, jako je formování kolon vozidel nebo průmyslové senzorové sítě.

## K čemu slouží

SL-PRS-RSRP bylo zavedeno v Release 18, aby poskytlo standardizovanou a přesnou metodu pro měření přijímaného výkonu pozičně specifických referenčních signálů na postranním spoji. Před jeho definicí se určování polohy na postranním spoji často spoléhalo na měření obecných referenčních signálů pro synchronizaci nebo demodulaci na postranním spoji, které nebyly optimalizovány pro přesnost určování polohy a mohly být neoptimální kvůli odlišným charakteristikám signálu a scénářům rušení.

Vytvoření SL-PRS-RSRP bylo motivováno rostoucí poptávkou po vysoce přesném určování polohy v aplikacích [V2X](/mobilnisite/slovnik/v2x/) a [ProSe](/mobilnisite/slovnik/prose/), jako je kooperativní zabránění kolizím nebo rozšířená realita. Předchozí přístupy postrádaly vyhrazená měření výkonu pro poziční signály, což vedlo k nekonzistentnostem a sníženému výkonu určování polohy. Definováním specifického měření [RSRP](/mobilnisite/slovnik/rsrp/) pro [SL-PRS](/mobilnisite/slovnik/sl-prs/) zajišťuje 3GPP, že poziční algoritmy mají spolehlivé a konzistentní metriky výkonu, což umožňuje lepší kompenzaci útlumu na dráze šíření, zlepšenou přesnost multilaterace a vyšší robustnost v různých podmínkách kanálu.

## Klíčové vlastnosti

- Měří přijímaný výkon vyhrazených Sidelink Positioning Reference Signals (SL-PRS)
- Poskytuje lineární průměrný výkon na zdrojových prvcích SL-PRS
- Používá se pro odhad útlumu na dráze šíření v pozičních algoritmech postranního spoje
- Podporuje filtrování a průměrování pro přesnost měření
- Hlášeno v dBm vyšším vrstvám (např. RRC nebo LPP)
- Zlepšuje odhad vzdálenosti pro metody určování polohy jako TDOA a další

## Související pojmy

- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)
- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [SL-PRS-RSRPP – Sidelink Positioning Reference Signal based Reference Signal Received Path Power](/mobilnisite/slovnik/sl-prs-rsrpp/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [SL-PRS-RSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-prs-rsrp/)
