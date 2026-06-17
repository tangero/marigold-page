---
slug: "mcl"
url: "/mobilnisite/slovnik/mcl/"
type: "slovnik"
title: "MCL – Minimum Coupling Loss"
date: 2025-01-01
abbr: "MCL"
fullName: "Minimum Coupling Loss"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mcl/"
summary: "Klíčový parametr pro plánování rádiové sítě představující minimální útlum na trase mezi vysílačem a přijímačem, typicky mezi základnovou stanicí a uživatelským zařízením (UE). Zajišťuje kvalitu signál"
---

MCL je minimální útlum na trase mezi vysílačem a přijímačem, například základnovou stanicí a uživatelským zařízením (UE), používaný při plánování sítě pro zajištění kvality signálu a prevenci nadměrného rušení.

## Popis

Minimální útlum vazby (MCL) je základním konceptem v plánování a optimalizaci rádiových sítí, definovaným jako minimální útlum na trase, který nastane mezi vysílačem a přijímačem v bezdrátovém komunikačním systému. V kontextech 3GPP často odkazuje na útlum mezi základnovou stanicí (např. [eNB](/mobilnisite/slovnik/enb/) v LTE nebo gNB v NR) a uživatelským zařízením (UE), s ohledem na faktory jako zisky antén, útlumy v kabelech a podmínky šíření. MCL se používá k modelování scénářů nejhoršího případu rušení, aby byl zajištěn signál nad úrovní šumu a prahy rušení pro spolehlivou komunikaci. Je obzvláště důležitý v hustých nasazeních, jako jsou malé buňky nebo heterogenní sítě, kde mohou být zařízení velmi blízko vysílačům.

Z architektonického hlediska MCL ovlivňuje návrh komponent rádiové přístupové sítě (RAN), včetně nastavení výkonu základnových stanic, konfigurací antén a plánování kmitočtů. Vypočítává se na základě parametrů jako výkon vysílače, citlivost přijímače a výšky antén, často s využitím standardizovaných modelů ve specifikacích 3GPP (např. pro LTE nebo NR). Mezi klíčové zahrnuté komponenty patří rádiová jednotka základnové stanice, antény UE a modely prostředí šíření (např. městské nebo venkovské). MCL pomáhá určovat oblasti pokrytí, výkon na okraji buňky a schémata koordinace rušení, jako je vylepšená mezibuněčná koordinace rušení (eICIC) v LTE.

V provozu se MCL aplikuje v nástrojích pro plánování sítě k simulaci scénářů, kdy je UE v nejkratší možné vzdálenosti od základnové stanice, což může způsobit vysoké rušení sousedním buňkám, pokud není řízeno. Například v LTE-Advanced a 5G NR se úvahy o MCL používají k nastavení parametrů pro řízení výkonu, téměř prázdné podrámce ([ABS](/mobilnisite/slovnik/abs/)) a úpravy formování svazků. Role MCL sahá až k zajištění souladu s regulačními limity expozice a optimalizaci spektrální účinnosti vyvážením síly signálu a rušení. Jedná se o statický nebo polostatický parametr, který spíše řídí strategie nasazení než dynamické řízení v reálném čase.

## K čemu slouží

MCL byl zaveden k řešení výzev v řízení rušení v se vyvíjejících rádiových sítích, zejména když se nasazení s příchodem malých buněk a heterogenních sítí stala hustšími. Před jeho formalizací se plánování sítí často spoléhalo na zjednodušené modely útlumu na trase, které nezohledňovaly scénáře minimální vzdálenosti, což vedlo k problémům s rušením a zhoršenému výkonu v případech těsné blízkosti. MCL poskytuje standardizovanou metriku k zajištění, že i v situacích nejhorší vazby zůstávají komunikační spoje životaschopné, aniž by způsobovaly nadměrné narušení ostatním uživatelům.

Historicky, s přechodem ze sítí 3G na LTE a dále, potřeba vyšší kapacity a pokrytí poháněla využívání nízkovýkonových uzlů, jako jsou femtobuňky a pikobuňky, které mohly být umístěny velmi blízko UE. To vytvořilo novou dynamiku rušení, například uplink rušení od blízkých UE k makro buňkám, což motivovalo definici MCL ve 3GPP Release 8. Řešilo to problémy jako efekty blízko-daleko a zajistilo, že síťové simulace a plánovací nástroje přesně odrážely reálné podmínky.

Vytvoření MCL také podporuje pokročilé funkce jako agregace nosných a massive [MIMO](/mobilnisite/slovnik/mimo/) v 5G, kde je přesná kontrola rušení klíčová pro dosažení vysokých přenosových rychlostí. Poskytnutím základny pro výpočty útlumu umožňuje operátorům navrhovat robustní sítě, které maximalizují kapacitu při zachování kvality služeb, zejména v městských prostředích s komplexními charakteristikami šíření.

## Klíčové vlastnosti

- Definuje minimální útlum na trase mezi základnovou stanicí a UE pro modelování rušení
- Používá se v nástrojích pro plánování a optimalizaci rádiové sítě
- Podporuje hustá nasazení jako malé buňky a heterogenní sítě
- Ovlivňuje mechanismy řízení výkonu a koordinace rušení
- Vychází ze zisků antén, útlumů v kabelech a modelů šíření
- Zajišťuje soulad s regulačními požadavky na expozici a kvalitu signálu

## Definující specifikace

- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 25.866** (Rel-9) — 1.28Mcps TDD Home NodeB Study Report
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TR 36.942** (Rel-19) — E-UTRA System Scenarios Specification
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TS 38.817** — 3GPP TR 38.817
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [MCL na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcl/)
