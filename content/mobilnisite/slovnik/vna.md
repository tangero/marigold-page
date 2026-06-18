---
slug: "vna"
url: "/mobilnisite/slovnik/vna/"
type: "slovnik"
title: "VNA – Vector Network Analyzer"
date: 2025-01-01
abbr: "VNA"
fullName: "Vector Network Analyzer"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/vna/"
summary: "Vektorový síťový analyzátor (VNA) je vysoce přesný elektronický měřicí přístroj používaný k měření frekvenční odezvy sítí, především RF komponent, jako jsou antény, filtry a kabely. V 3GPP je odkazová"
---

VNA je vysoce přesný elektronický měřicí přístroj používaný v 3GPP k měření frekvenční odezvy RF komponent, jako jsou antény a filtry, a zajišťuje, že rádiové zařízení splňuje standardy.

## Popis

Vektorový síťový analyzátor (VNA) je sofistikovaný měřicí systém používaný k analýze elektrického výkonu vysokofrekvenčních ([RF](/mobilnisite/slovnik/rf/)) a mikrovlnných zařízení a sítí. Na rozdíl od jednodušších měřičů výkonu nebo skalárních analyzátorů měří VNA jak velikost, tak fázi signálu, což poskytuje úplnou 'vektorovou' charakterizaci. Jeho hlavní funkcí je určit, jak síť (zařízení se vstupními a výstupními porty) reaguje na podnět v rozsahu frekvencí. Tato odezva je typicky vyjádřena jako S-parametry (rozptylové parametry), například S11 (vstupní odraz) a S21 (přímý přenos). VNA vstřikuje známý testovací signál (ze syntetizovaného zdroje) do testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)) a přesně měří odražené a přenášené signály pomocí naladěných přijímačů.

Architektura VNA se skládá ze zdroje signálu, testovací sady s směrovými vazebníky nebo můstky pro oddělení dopadajících, odražených a přenášených vln a vysoce citlivých přijímačů pro detekci. Moderní systémy VNA jsou často založeny na konceptu reflektometru. Provádějí měření porovnáním fáze a amplitudy signálu vracejícího se z DUT s původním podnětem. Kalibrace je kritický proces využívající známé standardy (otevřený, zkrat, zátěž) k eliminaci chyb z vlastního testovacího uspořádání a zajištění přesnosti. Měření VNA jsou zásadní pro kvantifikaci klíčových parametrů RF komponent: impedance, odrazové ztráty, vložné ztráty, zesílení, skupinové zpoždění a šířky pásma.

V kontextu specifikací 3GPP je na VNA odkazováno jako na doporučený nebo požadovaný přístroj pro testování shody a ověřování výkonu rádiového zařízení. Specifikace jako TS 37.544 (testování shody základnových stanic) a TS 38.551 (testování shody NG-RAN) definují testovací případy, kde se VNA používá k měření impedance anténních konektorů, izolace mezi anténními porty nebo přenosových charakteristik filtrů. Například pro ověření, že anténní port základnové stanice splňuje požadované odrazové ztráty (např. < -10 dB), je VNA připojen k portu pro měření S11 v provozním frekvenčním pásmu. Jeho vysoká přesnost a schopnost měřit komplexní impedanci z něj činí nepostradatelný nástroj pro validaci, že hardwarové komponenty splňují přísné požadavky na RF výkon nutné pro spolehlivý provoz sítí 5G/4G.

## K čemu slouží

VNA existuje jako přístroj, který poskytuje komplexní a přesnou charakterizaci [RF](/mobilnisite/slovnik/rf/) a mikrovlnných sítí, což je nezbytné pro návrh, výrobu a testování telekomunikačního hardwaru. Problém, který řeší, je potřeba pochopit nejen to, zda signál prochází komponentou, ale přesně to, jak je modifikován – jeho změna amplitudy, fázový posun a kolik se odráží. Tyto podrobné informace jsou kritické pro zajištění, že komponenty jako filtry, zesilovače, antény a kabely fungují v systému podle návrhu, což ovlivňuje celkový výkon sítě, integritu signálu a energetickou účinnost.

Před vektorovou analýzou se inženýři spoléhali na skalární měření (pouze výkon) nebo nepřímé metody, které byly nedostatečné pro moderní komplexní RF systémy, kde jsou fázové vztahy (kritické pro beamforming, [MIMO](/mobilnisite/slovnik/mimo/)) a impedance (kritické pro minimalizaci ztrát) prvořadé. VNA tyto limity řeší poskytováním přímých, kalibrovaných měření komplexních S-parametrů. V 3GPP vytvoření stále složitějších rádiových systémů (od 4G po 5G a dále) se širšími šířkami pásma, massive MIMO a integrovanými aktivními anténami vyžadovalo přísnější testovací metodologie. Odkazy na VNA v testovacích specifikacích (zavedené v Rel-14 spolu s pokročilejšími RF požadavky) motivují jeho použití k zajištění, že základnové stanice a další zařízení RAN splňují definované metriky RF výkonu, což garantuje interoperabilitu a kvalitu sítě.

Historický kontext je, že technologie VNA se vyvinula z dřívějších síťových analyzátorů a stala se základem v laboratořích RF inženýrství. Jeho zařazení do specifikací 3GPP formalizuje jeho roli ve standardizovaném procesu zajištění kvality pro průmysl, což zajišťuje, že všichni výrobci testují kritické RF parametry konzistentní, vysoce přesnou metodologií.

## Klíčové vlastnosti

- Měří jak velikost, tak fázi RF signálů (vektorové měření)
- Charakterizuje zařízení pomocí S-parametrů (S11, S21, S12, S22)
- Vyžaduje přesnou kalibraci pomocí známých standardů pro přesné výsledky
- Pracuje v širokých frekvenčních rozsazích, od MHz po GHz, relevantních pro buněčná pásma
- Používá se k měření impedance, odrazových ztrát, vložných ztrát, zesílení a skupinového zpoždění
- Nezbytný pro testování shody RF charakteristik základnových stanic dle 3GPP

## Definující specifikace

- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [VNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/vna/)
