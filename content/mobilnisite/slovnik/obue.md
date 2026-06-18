---
slug: "obue"
url: "/mobilnisite/slovnik/obue/"
type: "slovnik"
title: "OBUE – Operating Band Unwanted Emissions"
date: 2025-01-01
abbr: "OBUE"
fullName: "Operating Band Unwanted Emissions"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/obue/"
summary: "Operating Band Unwanted Emissions (OBUE, nežádoucí emise v provozním pásmu) jsou rádiové emise generované vysílačem, které spadají do jeho vlastního přiděleného provozního frekvenčního pásma, avšak mi"
---

OBUE je měřítko rádiových emisí vysílače v jeho vlastním provozním pásmu, avšak mimo přidělený kanál, což je klíčové pro integritu signálu a prevenci vnitropásmového rušení.

## Popis

Operating Band Unwanted Emissions (OBUE, nežádoucí emise v provozním pásmu) je klíčový požadavek na shodu vysílače definovaný v 3GPP rádiových specifikacích (např. pro základnové stanice a uživatelská zařízení). Kvantifikuje nežádoucí výkon vysílaný rádiovým vysílačem v jeho určeném provozním pásmu (frekvenční rozsah, pro který má vysílač licenci), avšak mimo okamžitě obsazenou šířku pásma kanálu. Tyto emise se liší od emisí mimo pásmo (Out-of-Band, OOB) a nežádoucích emisí (spurious emissions), které leží zcela mimo provozní pásmo. OBUE se primárně skládá ze spektrálního nárůstu (spectral regrowth) způsobeného nelinearitou výkonového zesilovače a šumu z vysílacího řetězce. Měření je typicky definováno jako maska spektrálních emisí nebo jako poměr úniku do sousedního kanálu (Adjacent Channel Leakage Ratio, [ACLR](/mobilnisite/slovnik/aclr/)) v rámci provozního pásma. Specifikace stanovuje maximální přípustné limity pro tento nežádoucí výkon, vyjádřené v dB vzhledem k výkonu vysílané nosné (dBc) nebo v absolutním výkonu (dBm). Testovací postup zahrnuje konfiguraci vysílače na konkrétním kanálu a měření spektrální hustoty výkonu na definovaných odstupových frekvencích v rámci provozního pásma. Dodržení limitů zajišťuje, že emise zařízení nadměrně nezhoršují výkon jeho vlastního přijímače (vlastní rušení v systémech s frekvenčním duplexem) a, což je kritičtější, nezpůsobují škodlivé rušení jiným kanálům patřícím stejnému nebo jiným operátorům ve stejném frekvenčním pásmu. Jde o základní parametr pro zajištění spektrální účinnosti a koexistence v hustě nasazených celulárních sítích.

## K čemu slouží

Specifikace OBUE existují pro řízení vnitropásmového rušení, což je kritický problém v celulárních systémech se sdíleným spektrem. Bez přísných limitů by výkonný vysílač pracující na jednom kanále mohl 'uniknout' dostatek energie do sousedních kanálů, což by desenzibilizovalo přijímače nebo zcela blokovalo komunikaci na těchto blízkých kanálech. To je zvláště problematické v širokých provozních pásmech (jako je pásmo 3,5 GHz n78 pro 5G NR), kde je mnoho kanálů umístěno těsně vedle sebe. Předchozí přístupy se silně zaměřovaly na emise mimo pásmo (OOB) a nežádoucí emise (spurious) pro ochranu jiných služeb v různých pásmech. Nicméně jak se spektrum stalo cennějším a jeho opakované využití intenzivnějším, kontrola 'znečištění' v rámci samotného licencovaného provozního pásma se stala prvořadou. Požadavky OBUE řeší omezení pouhého specifikování limitů OOB tím, že poskytují jemnější kontrolu 'sukně' emisí blízko vysílané nosné. To umožňuje síťovým operátorům nasazovat nosné s minimálními ochrannými intervaly, čímž maximalizují spektrální účinnost. Zavedení OBUE v 3GPP Rel-15 se časově shodovalo s prvními specifikacemi 5G NR, což odráží potřebu těsnějších [RF](/mobilnisite/slovnik/rf/) parametrů pro podporu širokých šířek pásma, pokročilé modulace (jako 1024-QAM) a scénářů husté agregace nosných, které jsou klíčové pro splnění slibů 5G o vysokých přenosových rychlostech.

## Klíčové vlastnosti

- Definuje limity nežádoucích emisí v rámci vlastního provozního pásma vysílače
- Měří se jako maska spektrálních emisí nebo poměr úniku do sousedního kanálu (ACLR)
- Kritické pro prevenci vnitropásmového rušení mezi sousedními kanály
- Přímo ovlivňuje dosažitelnou spektrální účinnost a kapacitu sítě
- Klíčový test shovy pro vysílače základnových stanic (gNB) i uživatelských zařízení (UE)
- Specifikováno samostatně pro různé rádiové přístupové technologie (NR, LTE) a frekvenční rozsahy

## Související pojmy

- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)

## Definující specifikace

- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.817** — 3GPP TR 38.817
- **TR 38.844** (Rel-18) — Efficient utilization of licensed spectrum
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [OBUE na 3GPP Explorer](https://3gpp-explorer.com/glossary/obue/)
