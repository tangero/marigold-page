---
slug: "sii2"
url: "/mobilnisite/slovnik/sii2/"
type: "slovnik"
title: "SII2 – Service Interaction Indicators Two"
date: 2025-01-01
abbr: "SII2"
fullName: "Service Interaction Indicators Two"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sii2/"
summary: "Sada parametrů používaná v sítích GSM/UMTS pro řízení interakcí mezi více doplňkovými službami (např. přesměrování hovoru a čekání hovoru). Definuje pravidla a prioritu, aby předešla konfliktům při so"
---

SII2 je sada parametrů používaná v sítích GSM/UMTS k definování pravidel a priority pro řízení interakcí mezi více doplňkovými službami, čímž předchází konfliktům a zajišťuje předvídatelné chování sítě.

## Popis

Service Interaction Indicators Two (SII2, indikátory interakce služeb dva) je standardizovaný parametr definovaný ve specifikacích 3GPP pro řízení interakce mezi různými doplňkovými službami v sítích GSM a UMTS. Doplňkové služby, jako je bezpodmínečné přesměrování hovoru ([CFU](/mobilnisite/slovnik/cfu/)), čekání hovoru ([CW](/mobilnisite/slovnik/cw/)) nebo konference (MPTY), mohou potenciálně konfliktovat, pokud je pro účastníka aktivních více služeb najednou. SII2 poskytuje sadu indikátorů, které určují prioritu a pravidla interakce mezi těmito službami. Parametr je uložen v síti, typicky v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) jako součást profilu služeb účastníka, a používá jej Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) během zpracování hovoru. Když dojde k události hovoru, MSC vyhodnotí aktivní doplňkové služby pro zúčastněné strany a konzultuje indikátory SII2, aby určilo pořadí provádění služeb a vyřešilo případné konflikty. Například SII2 může určovat, zda má za určitých podmínek přednost přesměrování hovoru před zákazem hovoru. Indikátory jsou definovány jako bitmapy nebo kódované hodnoty v signalizačních zprávách, například v protokolu Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) (např. v operacích InsertSubscriberData nebo ProvideRoamingNumber). Tento mechanismus zajišťuje konzistentní a deterministické chování služeb napříč různými síťovými implementacemi, což je klíčové pro udržení spolehlivosti služeb a spokojenosti účastníků. Technická implementace spočívá v tom, že servisní logika MSC interpretuje hodnoty SII2 spolu s dalšími informacemi o stavu hovoru, aby aplikovala správnou sekvenci akcí služeb.

## K čemu slouží

SII2 byl vyvinut k řešení složitosti řízení více doplňkových služeb, které mohly interagovat nepředvídatelným způsobem. Rané telefonní systémy postrádaly standardizovaná pravidla pro interakci služeb, což vedlo k nekonzistentnímu chování napříč sítěmi a potenciálním konfliktům služeb, které zhoršovaly uživatelský zážitek. Vytvoření SII2 poskytlo jednotný rámec operátorům pro definování a řízení toho, jak spolu interagují služby jako přesměrování hovoru, čekání hovoru nebo zákaz hovoru. Tím byly vyřešeny problémy, jako jsou nekonečné přesměrovací smyčky nebo nejednoznačné scénáře, kdy je současně spuštěno více služeb. Standardizací těchto interakcí ve specifikacích 3GPP byla zajištěna interoperabilita mezi síťovými zařízeními od různých výrobců a umožněno spolehlivé zavádění nových doplňkových služeb. Tato sada parametrů se vyvinula z dřívějších indikátorů interakce (jako SII), aby pokryla širší škálu služeb a složitější scénáře, což odráží rostoucí sofistikovanost mobilních sítí. Její zařazení do základních specifikací, jako jsou TS 23.078 a TS 23.084, podtrhuje její zásadní roli v architektuře služeb.

## Klíčové vlastnosti

- Definuje pravidla priority pro interakce doplňkových služeb
- Uloženo v HLR jako součást dat služeb účastníka
- Používáno MSC pro řešení konfliktů během zpracování hovoru
- Standardizované bitmapy v signalizačních zprávách MAP
- Zajišťuje konzistentní chování služeb napříč sítěmi
- Podporuje složité scénáře, jako je více současně aktivních služeb

## Související pojmy

- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 23.084** (Rel-19) — Multi Party (MPTY) Service Stage 2 Description
- **TS 23.097** (Rel-19) — Multiple Subscriber Profile (MSP) Phase 2

---

📖 **Anglický originál a plná specifikace:** [SII2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/sii2/)
