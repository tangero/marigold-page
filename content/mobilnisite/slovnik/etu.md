---
slug: "etu"
url: "/mobilnisite/slovnik/etu/"
type: "slovnik"
title: "ETU – Extended Typical Urban model"
date: 2025-01-01
abbr: "ETU"
fullName: "Extended Typical Urban model"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/etu/"
summary: "Rozšířený typický městský model (Extended Typical Urban, ETU) je standardizovaný model šíření kanálu definovaný 3GPP pro simulaci chování rádiového signálu v prostředí městských makrobuněk s vysokým r"
---

ETU je standardizovaný 3GPP model kanálu pro simulaci šíření rádiového signálu s vysokým rozprostřením zpoždění v městských makrobuňkách, používaný k testování výkonu uživatelského zařízení (UE) a základnové stanice za realistických vícecestných podmínek.

## Popis

Rozšířený typický městský model (Extended Typical Urban, ETU) je statistický model kanálu typu tapped-delay-line (TDL), který charakterizuje vícecestné šíření, jemuž jsou rádiové signály vystaveny v hustě zastavěných městských prostředích. Definovaný v 3GPP specifikacích jako TS 36.104 a TS 38.901 je součástí sady modelů kanálů používaných pro testování výkonu základnových stanic ([BS](/mobilnisite/slovnik/bs/)) a uživatelských zařízení (UE). Model matematicky reprezentuje rádiový kanál jako filtr s konečnou impulsní odezvou ([FIR](/mobilnisite/slovnik/fir/)) se sadou diskrétních zpožďovacích členů (tapů). Každý zpožďovací člen je definován relativním zpožděním, komplexní amplitudou (která se v čase mění, aby modelovala útlum) a úrovní výkonu. Model ETU konkrétně vykazuje efektivní (RMS) rozprostření zpoždění 991 nanosekund a maximální přebytečné zpoždění 5000 nanosekund, což představuje kanál s významnou časovou disperzí způsobenou odrazy od budov a dalších velkých struktur.

V praxi je model ETU implementován v emulátorech kanálů nebo simulačním softwaru pro posouzení výkonu přijímače v náročných reálných podmínkách. Pro testování shody je přijímač UE nebo základnové stanice vystaven standardizovanému testovacímu signálu, který byl zkreslen modelem kanálu ETU, často v kombinaci s aditivním bílým Gaussovským šumem ([AWGN](/mobilnisite/slovnik/awgn/)). Poté se měří schopnost zařízení správně demodulovat a dekódovat signál, přičemž metriky jako propustnost, chybovost bloků ([BLER](/mobilnisite/slovnik/bler/)) nebo referenční citlivost určují kritéria úspěchu/neúspěchu. Model používá specifický Dopplerovský spektrální model (typicky klasické nebo Jakesovo spektrum) k simulaci časově proměnlivé povahy kanálu způsobené relativním pohybem vysílače a přijímače.

Parametry zpožďovacích členů modelu ETU jsou odvozeny z rozsáhlých empirických měřicích kampaní v městských oblastech. Zahrnuje devět samostatných zpožďovacích členů se specifickými zpožděními a úrovněmi výkonu. Profil výkonu v závislosti na zpoždění je exponenciální, což znamená, že později přicházející ozvěny mají obecně nižší výkon. Útlum na každém zpožďovacím členu je typicky modelován jako Rayleighovské nebo Riceovo rozdělení, které reprezentuje podmínky bez přímé viditelnosti, respektive s částečnou přímou viditelností. Tato podrobná statistická reprezentace umožňuje modelu přesně reprodukovat klíčové degradace kanálu, jako je frekvenčně selektivní útlum a mezisymbolové interference ([ISI](/mobilnisite/slovnik/isi/)), které mají pokročilé přijímací algoritmy, jako jsou ekvalizéry a [OFDM](/mobilnisite/slovnik/ofdm/)/[OFDMA](/mobilnisite/slovnik/ofdma/), zmírňovat.

V rámci ekosystému 3GPP je model ETU klíčový pro zajištění, že zařízení splňují minimální požadavky na výkon, a tím garantují konzistentní uživatelský zážitek napříč různými sítěmi a dodavateli. Používá se v testovacích případech pro referenční citlivost, selektivitu sousedního kanálu a blokovací charakteristiky. S vývojem z LTE na NR základní principy modelu TDL zůstávají, ale parametry ETU jsou integrovány do flexibilnějšího rámce v TR 38.901, který podporuje širší rozsah kmitočtových pásem a scénářů. Porozumění modelu ETU je nezbytné pro radiofrekvenční (RF) a protokolové testovací inženýry, protože tvoří základ realistického ověřování výkonu na fyzické vrstvě.

## K čemu slouží

Rozšířený typický městský model (Extended Typical Urban, ETU) kanálu byl vytvořen, aby poskytl standardizovanou, realistickou a opakovatelnou testovací podmínku pro hodnocení výkonu širokopásmových celulárních systémů, počínaje LTE, v náročných městských podmínkách šíření. Před jeho standardizací se při testování výkonu často používaly jednodušší modely (jako [AWGN](/mobilnisite/slovnik/awgn/) nebo plochý útlum) nebo proprietární modely kanálů, což ztěžovalo srovnání výsledků mezi zařízeními různých dodavatelů nebo zaručení minimální úrovně výkonu v reálném světě. Model ETU tento problém řeší definováním konkrétního, závažného vícecestného scénáře, vůči kterému musí být všechna zařízení testována, čímž zajišťuje, že zvládnou časovou disperzi a útlum typické pro hustě zastavěné městské makrobuňky.

Motivace pro vývoj modelu ETU pramenila z přechodu na systémy založené na OFDMA, jako je LTE, které jsou obzvláště citlivé na rozprostření zpoždění a frekvenčně selektivní útlum. Konstruktéři systémů potřebovali model kanálu, který přesně odrážel rozprostření zpoždění pozorovaná v reálných měřeních ve městech – mnohem větší než v dřívějším modelu Typické město (Typical Urban, TU) používaném pro GSM. Předpona 'Rozšířený' (Extended) označuje toto zvýšené rozprostření zpoždění. Vytvořením náročné, ale standardizované testovací podmínky chtěl 3GPP podnítit vývoj robustních návrhů přijímačů s efektivními algoritmy pro ekvalizaci a odhad kanálu, a tím v konečném důsledku zajistit, aby koncoví uživatelé zažívali spolehlivé služby s vysokou přenosovou rychlostí i ve složitých rádiových prostředích.

Model ETU dále plní kritický regulační a komerční účel. Tvoří část základu pro standardy testování shody, které certifikační orgány používají ke schvalování zařízení pro vstup na trh. To poskytuje síťovým operátorům jistotu, že nasazená zařízení budou na jejich sítích adekvátně fungovat. Z pohledu návrhu systému se model také používá v simulacích na úrovni spojení a na systémové úrovni k odhadu pokrytí buňky, kapacity a přínosů pokročilých funkcí přijímače, čímž usměrňuje plánování sítě a vývoj funkcí. Jeho pokračující používání v éře 5G NR dokládá jeho trvalou hodnotu jakožto benchmarku pro výkon v městských makrobuňkách.

## Klíčové vlastnosti

- Standardizovaný 3GPP model kanálu typu Tapped-Delay-Line (TDL)
- Reprezentuje prostředí městské makrobuňky s vysokým rozprostřením zpoždění (RMS rozprostření zpoždění 991 ns)
- Definován s 9 diskrétními zpožďovacími členy (taps) se specifickými zpožděními a úrovněmi výkonu
- Zahrnuje časově proměnlivý útlum modelovaný pomocí Dopplerovského spektra (např. klasického)
- Používá se pro RF testování výkonu/shody uživatelských zařízení (UE) a základnových stanic
- Použitelný pro hodnocení a simulaci systémů LTE a NR

## Související pojmy

- [EPA – Expectation Propagation Algorithm](/mobilnisite/slovnik/epa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [ETU na 3GPP Explorer](https://3gpp-explorer.com/glossary/etu/)
