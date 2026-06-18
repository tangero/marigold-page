---
slug: "pac"
url: "/mobilnisite/slovnik/pac/"
type: "slovnik"
title: "PAC – Phase Alignment Command"
date: 2025-01-01
abbr: "PAC"
fullName: "Phase Alignment Command"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pac/"
summary: "Příkaz pro zarovnání fáze (Phase Alignment Command) je řídicí signál používaný v synchronizačních sítích, zejména pro úpravu fáze hodinového signálu. Je součástí synchronizačních protokolů, které zaji"
---

PAC je řídicí signál používaný v synchronizačních sítích k úpravě fáze hodinového signálu, který zajišťuje přesné časové zarovnání mezi síťovými uzly.

## Popis

Příkaz pro zarovnání fáze (PAC) je mechanismus používaný v protokolech pro synchronizaci a distribuci hodin, jako jsou ty definované pro Synchronní Ethernet (SyncE) nebo v kontextu protokolu Precision Time Protocol ([PTP](/mobilnisite/slovnik/ptp/)). Jeho primární funkcí je poskytovat korekční zpětnou vazbu hodinovému servomechanismu (např. smyčce fázového závěsu – PLL) v podřízených (slave) hodinách a instruovat jej, jak upravit svou fázi, aby dosáhl zarovnání s hlavním referenčním hodinovým signálem. Na rozdíl od prostého hodinového signálu PAC nese explicitní informaci o úpravě, což umožňuje sofistikovanější a stabilnější synchronizaci, zejména v paketových sítích, kde je problémem proměnlivost zpoždění.

Z architektonického hlediska je PAC generován algoritmem pro obnovu hodin v podřízeném uzlu. Tento algoritmus porovnává fázi lokálně generovaných hodin s fázovou informací získanou z příchozích časovacích paketů nebo signálu fyzické vrstvy (jako je SyncE). Na základě tohoto porovnání algoritmus vypočítá fázovou chybu. PAC je výstupem tohoto výpočtu – digitální příkaz, který určuje velikost a směr (předsunutí nebo zpoždění) potřebné úpravy fáze. Tento příkaz je následně přiveden na řídicí vstup hodinového servomechanismu (např. digitálně řízeného oscilátoru – DCO). Servomechanismus interpretuje PAC a aplikuje odpovídající korekci na fázi lokálních hodin.

Jeho role v síti je zásadní pro udržování vysoce kvalitní synchronizace, která je základem mnoha služeb. V mobilních sítích je přesné zarovnání fáze nezbytné pro technologie jako LTE-TDD, 5G NR [TDD](/mobilnisite/slovnik/tdd/) a koordinovaný vícebodový přenos, kde musí být časy vysílání pro uplink a downlink těsně synchronizovány napříč více základnovými stanicemi, aby se předešlo interferenci. PAC to umožňuje tím, že povoluje jemně odstupňovanou dynamickou úpravu fáze hodin. Specifikace jako TS 26.346 ([MBMS](/mobilnisite/slovnik/mbms/)), TS 26.849 (eMBMS) a TS 48.061 odkazují na požadavky synchronizace, kde jsou mechanismy pro zarovnání fáze relevantní. PAC spolupracuje se synchronizací frekvence k dosažení plné časové/fázové synchronizace, často s cílovými požadavky ±1,5 µs nebo lepšími pro 5G.

## K čemu slouží

Příkaz pro zarovnání fáze (PAC) existuje proto, aby řešil problém dosažení a udržení přesné fázové (časové) synchronizace v distribuovaných sítích – což je požadavek přesahující pouhé zarovnání frekvence. Zatímco synchronizace frekvence zajišťuje, že hodiny tikají stejnou rychlostí, synchronizace fáze zajišťuje, že ukazují „dvanáctou hodinu“ ve stejném absolutním okamžiku. To je kritické pro rádiové systémy s časovým duplexním dělením ([TDD](/mobilnisite/slovnik/tdd/)) a mnoho paketových finančních a průmyslových aplikací.

Motivace pro specializovaný příkazový mechanismus, jako je PAC, vychází z omezení tradičních analogových PLL a výzev spojených s přenosem času v paketových sítích ([PTP](/mobilnisite/slovnik/ptp/)). V paketových sítích může proměnlivost síťového zpoždění (paketový jitter) narušit jednoduchá fázová měření. Pokročilé algoritmy pro obnovu hodin využívají filtrování a statistické metody k odhadnutí skutečné fázové chyby z rušených měření zpoždění paketů. PAC je rafinovaným výstupem tohoto odhadovacího procesu – čistý, akční příkaz pro hodinový hardware. Řeší potřebu stability a odolnosti proti šumu, což umožňuje lokálním hodinám provádět plynulé, řízené úpravy namísto reakce na každé rušené měření. Jeho vznik a standardizace byly poháněny vývojem od čistě synchronních [TDM](/mobilnisite/slovnik/tdm/) sítí k hybridním a čistě paketovým mobilním backhaul sítím, kde se přesné dodání fáze stalo zároveň obtížnějším i nezbytnějším.

## Klíčové vlastnosti

- Poskytuje digitální příkaz pro přesné fázové seřízení lokálních hodin
- Generován algoritmy pro obnovu hodin na základě výpočtu fázové chyby
- Řídí hodinový servomechanismus (např. PLL, DCO) pro předsunutí nebo zpoždění fáze hodin
- Nezbytný pro dosažení časové/fázové synchronizace navíc k synchronizaci frekvence
- Umožňuje stabilní synchronizaci i za přítomnosti proměnlivosti zpoždění paketů
- Kritický pro provoz TDD rádiových systémů, koordinované plánování v 5G a MBMS

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TS 48.061** (Rel-19) — BTS-TRAU Protocol for HR Speech/Data

---

📖 **Anglický originál a plná specifikace:** [PAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pac/)
