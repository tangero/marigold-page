---
slug: "nul"
url: "/mobilnisite/slovnik/nul/"
type: "slovnik"
title: "NUL – Uplink EARFCN / Uplink LARFCN"
date: 2025-01-01
abbr: "NUL"
fullName: "Uplink EARFCN / Uplink LARFCN"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nul/"
summary: "NUL označuje číslo absolutního rádiového kmitočtového kanálu pro uplink v LTE nebo číslo lokálního rádiového kmitočtového kanálu pro uplink v NR. Je to skalární číslo, které jednoznačně identifikuje k"
---

NUL je číslo absolutního rádiového kmitočtového kanálu pro uplink v LTE nebo číslo lokálního rádiového kmitočtového kanálu pro uplink v NR; jedná se o skalární hodnotu, která jednoznačně identifikuje kmitočet nosné pro přenos ze zařízení UE k základnové stanici.

## Popis

NUL, označující číslo absolutního rádiového kmitočtového kanálu pro uplink ([EARFCN](/mobilnisite/slovnik/earfcn/)) v LTE nebo číslo lokálního rádiového kmitočtového kanálu pro uplink ([LARFCN](/mobilnisite/slovnik/larfcn/)) v 5G NR, je základním parametrem v mobilních rádiových systémech. Je to bezrozměrné celé číslo, které poskytuje standardizovanou metodu pro odkazování na konkrétní kmitočty rádiové nosné pro uplink bez nutnosti uvádět skutečnou hodnotu kmitočtu v hertzech. Tato abstrakce zjednodušuje signalizaci protokolů, konfiguraci a testovací specifikace. Každá hodnota NUL se mapuje na konkrétní středový kmitočet uplinku pomocí definovaného vzorce, který zahrnuje kmitočtovou mřížku kanálů a referenční kmitočet.

Pokud jde o princip fungování, NUL se hojně používá v signalizaci řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a ve specifikacích schopností UE. Například, když síť nakonfiguruje UE pro provoz v určitém kmitočtovém pásmu, učiní tak signalizací příslušné hodnoty NUL (nebo rozsahu hodnot) pro uplink. Radiový přijímač a vysílač UE se poté naladí na odpovídající fyzický kmitočet odvozený z tohoto NUL. Mapovací vzorce se mezi LTE a NR liší a jsou specifické pro pásmo. V LTE je vzorec F_[UL](/mobilnisite/slovnik/ul/) = F_UL_low + 0,1*(NUL - N_Offs_UL). V NR je vzorec obecnější: F_UL = F_REF + (NUL * k), kde k je velikost kroku kmitočtové mřížky kanálů (např. 5 kHz, 15 kHz, 60 kHz).

Klíčovými součástmi, které jsou zapojeny, jsou radiový transceiver UE, který musí NUL interpretovat, a základnová stanice (eNodeB/gNodeB), která jej přiřazuje. NUL je součástí informací o konfiguraci nosné vysílaných v zprávách systémového informačního bloku ([SIB](/mobilnisite/slovnik/sib/)) a zasílaných v dedikovaných RRC zprávách, jako je RRCConnectionReconfiguration. Je také kritickým parametrem ve specifikacích [RF](/mobilnisite/slovnik/rf/) konformních testů (např. 36.521-1 pro LTE), kde testovací zařízení používá NUL k definování testovacího kmitočtu pro uplink měření, jako je výkon, kvalita modulace a nežádoucí emise.

Jeho role v síti je klíčová pro správu kmitočtů a provoz UE. Umožňuje síti nasměrovat UE na konkrétní uplink kanály v rámci licencovaného spektra. To je zásadní pro vyvažování zátěže, správu interference a provoz agregace nosných, kde může být UE přiřazeno více NUL pro simultánní uplink přenos na různých komponentních nosných. NUL spolu se svým protějškem pro downlink ([NDL](/mobilnisite/slovnik/ndl/)) tvoří kompletní systém číslování kanálů pro spárované spektrum.

## K čemu slouží

NUL existuje proto, aby poskytoval jednoduchý, škálovatelný a technologicky agnostický způsob odkazování na kmitočty rádiové nosné pro uplink v rámci standardů 3GPP. Před zavedením čísel kanálů, jako je [EARFCN](/mobilnisite/slovnik/earfcn/), systémy odkazovaly na kmitočty přímo v MHz nebo kHz, což bylo v signalizačních protokolech těžkopádné a náchylné k chybám. Vytvoření systému čísel kanálů abstrahuje od složitých desetinných hodnot kmitočtů a poskytuje čistý celočíselný index, který je snadněji kódovatelný, přenositelný a zpracovatelný v digitálních zprávách.

Historická motivace vychází z GSM, které zavedlo ARFCN (Absolute Radio Frequency Channel Number). Tento koncept byl úspěšně přenesen do UMTS jako UARFCN a následně do LTE jako EARFCN. Pro NR byl rozvinut do LARFCN, aby pojal mnohem širší kmitočtový rozsah (od pásem pod 1 GHz až po mmWave) a flexibilní numerologie. NUL konkrétně řeší potřebu jedinečného identifikátoru pro *uplink* nosnou, což je obzvláště důležité v systémech s frekvenčním duplexem (FDD), kde se kmitočty pro uplink a downlink liší.

Řeší několik klíčových problémů: Za prvé umožňuje efektivní RRC signalizaci, protože přenos malého celého čísla je mnohem efektivnější z hlediska šířky pásma než přenos kmitočtu v plovoucí řádové čárce. Za druhé zajišťuje globální interoperabilitu; zařízení UE od jakéhokoli výrobce, nakonfigurované s hodnotou NUL 'X' pro dané pásmo, se naladí na přesně stejný kmitočet kdekoli na světě. Za třetí zjednodušuje testování a certifikaci; testovací případy jsou psány vůči hodnotám NUL, což zajišťuje, že jsou UE testována na správných kmitočtech vzhledem ke kmitočtové mřížce kanálů definované ve standardu. Tento systém byl klíčový pro škálovatelné nasazení LTE a NR napříč stovkami kmitočtových pásem po celém světě.

## Klíčové vlastnosti

- Celočíselný identifikátor kmitočtu nosné pro uplink
- Používá se v LTE (jako EARFCN) a v NR (jako LARFCN)
- Mapuje se na fyzický kmitočet pomocí standardizovaných vzorců
- Kritický pro RRC signalizaci a konfiguraci UE
- Základní pro RF konformní testování (např. 36.141, 38.321)
- Umožňuje agregaci nosných a konfiguraci části šířky pásma

## Související pojmy

- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)
- [LARFCN – LCR TDD Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/larfcn/)
- [NDL – Downlink LARFCN](/mobilnisite/slovnik/ndl/)

## Definující specifikace

- **TS 25.116** (Rel-19) — LCR TDD Repeater RF Characteristics
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TR 38.892** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NUL na 3GPP Explorer](https://3gpp-explorer.com/glossary/nul/)
