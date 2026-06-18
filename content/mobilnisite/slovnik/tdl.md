---
slug: "tdl"
url: "/mobilnisite/slovnik/tdl/"
type: "slovnik"
title: "TDL – Tapped Delay Line"
date: 2025-01-01
abbr: "TDL"
fullName: "Tapped Delay Line"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tdl/"
summary: "Matematický model používaný v simulacích bezdrátového kanálu k reprezentaci vícecestného šíření. Modeluje rádiový kanál jako filtr s konečnou impulsní charakteristikou (FIR) s více zpožděnými větvemi,"
---

TDL je matematický model kanálu, který simuluje vícecestné šíření tím, že reprezentuje rádiový kanál jako filtr s více zpožděnými větvemi (taps), z nichž každá má specifické útlum a fázový posuv.

## Popis

Tapped Delay Line (TDL) je základní model kanálu hojně používaný ve specifikacích 3GPP pro charakterizaci časově disperzní povahy rádiového šíření v prostředích s vícecestným šířením. Matematicky reprezentuje impulsní odezvu bezdrátového kanálu jako lineární filtr s konečnou impulsní charakteristikou ([FIR](/mobilnisite/slovnik/fir/)). Model se skládá ze série diskrétních 'větví' (taps), kde každá větev odpovídá samostatné šíř[ec](/mobilnisite/slovnik/ece-c/)í dráze se specifickým časovým zpožděním, středním výkonem (útlumem) a fázovými charakteristikami. Celková sada větví popisuje, jak je vysílaný signál přijímán jako více zpožděných a utlumených kopií, což způsobuje frekvenčně selektivní úniky.

Při činnosti model TDL konvoluje vysílaný signál s impulsní odezvou kanálu. Každá větev je definována parametry včetně zpoždění (τ), výkonu (P) a tvaru Dopplerova spektra (např. Classical Jakes, Round Robin), které modeluje časovou variaci způsobenou mobilitou. Profil výkonu a zpoždění ([PDP](/mobilnisite/slovnik/pdp/)), který uvádí výkon každé větve v závislosti na jejím zpoždění, je klíčovým výstupem. 3GPP standardizovala několik TDL modelů (např. TDL-A, TDL-B, TDL-C, TDL-D, TDL-E) pro různé scénáře nasazení, jako je urban macro, urban micro a indoor. Tyto modely jsou odvozeny z rozsáhlých měřicích kampaní kanálu a poskytují reprodukovatelný referenční základ pro simulace na úrovni spojení a systému.

Architektura TDL modelu v simulacích zahrnuje generování komplexního kanálového filtru v základním pásmu. Pro každou větev je generován komplexní Gaussův náhodný proces se specifikovaným výkonem a Dopplerovým spektrem, který reprezentuje časově proměnlivý únik. Součet příspěvků všech větví, každé vhodně zpožděné, vytváří přijímaný signál. Tento model je klíčový pro vyhodnocování výkonu fyzické vrstvy NR a LTE, včetně metrik jako chybový vektorový modul ([EVM](/mobilnisite/slovnik/evm/)), propustnost a bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)) za realistických podmínek kanálu. Umožňuje inženýrům testovat přijímací algoritmy, jako jsou ekvalizéry a odhadovače kanálu, bez nutnosti nákladných terénních zkoušek.

## K čemu slouží

Model TDL existuje, aby poskytl standardizovanou, přesnou a výpočetně efektivní metodu pro simulaci znehodnocení rádiového kanálu v laboratorním a softwarovém prostředí. Před těmito modely se hodnocení výkonu systému spoléhalo silně na teoretické aproximace nebo nákladné testy v provozu, které nebyly reprodukovatelné a nemohly pokrýt všechny možné scénáře. Model TDL řeší problém potřeby společného benchmarku pro porovnání různých zařízení od výrobců a algoritmů za konzistentních, realistických podmínek.

Jeho vytvoření bylo motivováno potřebou specifikovat požadavky na výkon (např. v 3GPP TS 38.101 a TS 38.141) pro základnové stanice a uživatelská zařízení. Regulátoři a operátoři vyžadují důkazy, že zařízení adekvátně fungují v typických prostředích s vícecestným šířením. Model TDL se svou strukturou větví přímo řeší omezení jednodušších modelů (jako je kanál s aditivním bílým Gaussovským šumem), které ignorují časovou disperzi a frekvenční selektivitu. Zachycuje základní charakteristiky vícecestného šíření, což je kritické pro návrh a testování širokopásmových systémů, jako jsou LTE a 5G NR, které využívají vysoké šířky pásma, kde je frekvenčně selektivní únik výrazný.

Historicky se modelování kanálu vyvinulo od jednoduchých statistických modelů k přesnějším geometrickým stochastickým modelům (GSCM). Model TDL nachází rovnováhu mezi přesností a složitostí simulace. Je to negeometrický stochastický model, který je snazší implementovat než plné sledování paprsků (ray-tracing), ale reprezentativnější než modely s plochým únikem. Jeho standardizace napříč releasy zajišťuje zpětnou kompatibilitu a umožňuje vývoj modelů pro podporu nových kmitočtových pásem (jako mmWave v Rel-15+) a scénářů (jako vysokorychlostní vlak v Rel-14).

## Klíčové vlastnosti

- Modeluje vícecestné šíření jako filtr s konečnou impulsní charakteristikou (FIR) s diskrétními větvemi (taps)
- Každá větev je charakterizována zpožděním, středním výkonem a Dopplerovým spektrem
- Standardizované profily výkonu a zpoždění pro různá prostředí (např. TDL-A pro UMi)
- Podporuje časově proměnlivé podmínky kanálu prostřednictvím generování úniků větví
- Používá se pro testování shody výkonu přijímače základnové stanice a UE
- Aplikovatelný napříč kmitočtovými rozsahy včetně FR1 a FR2 (mmWave)

## Definující specifikace

- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [TDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdl/)
