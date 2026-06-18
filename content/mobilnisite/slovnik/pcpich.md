---
slug: "pcpich"
url: "/mobilnisite/slovnik/pcpich/"
type: "slovnik"
title: "PCPICH – Primary Common Pilot Channel"
date: 2025-01-01
abbr: "PCPICH"
fullName: "Primary Common Pilot Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pcpich/"
summary: "Downlinkový fyzický kanál v UMTS (WCDMA) používaný pro odhad kanálu a identifikaci buňky. Vysílá známou nemodulovanou pilotní sekvenci, což umožňuje uživatelskému zařízení (UE) měřit kvalitu signálu,"
---

PCPICH (Primary Common Pilot Channel) je primární společný pilotní kanál, downlinkový fyzický kanál v UMTS, který vysílá známou pilotní sekvenci pro identifikaci buňky, odhad kanálu a umožnění měření kvality signálu uživatelským zařízením.

## Popis

Primární společný pilotní kanál (PCPICH) je klíčový downlinkový fyzický kanál definovaný pro rádiové rozhraní UMTS Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)). Je to nepřetržitý, nemodulovaný kanál, který vysílá známou bitovou sekvenci (všechny nuly) rozprostřenou specifickým kanalizačním kódem a zakódovanou primárním scramblovacím kódem ([PSC](/mobilnisite/slovnik/psc/)) buňky. Jeho primární funkcí je sloužit jako fázový a amplitudový referenční bod pro všechny ostatní downlinkové fyzické kanály ve stejné buňce. Protože je signál PCPICH předem znám, může jej uživatelské zařízení (UE) použít k odhadu impulsní odezvy rádiového kanálu, což je proces nezbytný pro koherentní demodulaci jiných kanálů, jako je Dedicated Physical Channel ([DPCH](/mobilnisite/slovnik/dpch/)) nebo Secondary Common Pilot Channel ([S-CPICH](/mobilnisite/slovnik/s-cpich/)).

PCPICH je vysílán s relativně vysokým, konstantním výkonem, aby bylo zajištěno spolehlivé přijetí v celé buňce. Používá pevný kanalizační kód (s rozprostíracím faktorem 256, číslo kódu 0). Kanál je vždy vysílán pomocí primárního scramblovacího kódu buňky, který buňku v její oblasti jednoznačně identifikuje. To činí z PCPICH primární referenci pro proceduru hledání buňky. Během počátečního přístupu nebo předání spojení UE skenuje scramblovací kód [P-CPICH](/mobilnisite/slovnik/p-cpich/), aby identifikovalo cílovou buňku a synchronizovalo se s ní. Kvalita PCPICH, měřená jako Received Signal Code Power ([RSCP](/mobilnisite/slovnik/rscp/)) nebo poměr přijaté energie na čip k celkové spektrální hustotě výkonu ([Ec](/mobilnisite/slovnik/ece-c/)/Io), je klíčovou metrikou pro rozhodování radio resource management (RRM), jako je výběr buňky, její převýběr a předání spojení.

Z architektonického hlediska je PCPICH generován v Node B (základnové stanici) a je povinným kanálem pro každou buňku. Nepřenáší informace vyšších vrstev ani uživatelská data. Jeho návrh je optimalizován pro robustnost a předvídatelnost. Konstantní vysílání umožňuje nepřetržité monitorování kvality kanálu. V plánování sítě je výkon přidělený PCPICH klíčovým parametrem, který vyvažuje pokrytí (vyžadující vyšší výkon) a kapacitu (protože výkon PCPICH spotřebovává část celkového rozpočtu vysílacího výkonu Node B). Charakteristiky kanálu jsou standardizovány, aby byla zajištěna interoperabilita mezi UE a síťovým zařízením od různých výrobců.

## K čemu slouží

PCPICH byl vytvořen k řešení základních výzev v systémech založených na WCDMA, konkrétně potřeby spolehlivého referenčního signálu specifického pro buňku. V systémech CDMA sdílejí všechny kanály stejné frekvenční pásmo a jsou odděleny jedinečnými kódy. Aby přijímač mohl koherentně demodulovat požadovaný kanál, musí přesně odhadnout účinky rádiového kanálu (jako je útlum, rozptyl zpoždění a fázová rotace). PCPICH poskytuje tuto společnou referenci. Bez takového vyhrazeného pilotního signálu by každý kanál musel obsahovat vlastní referenci, což by vedlo k významné režii a snížené datové efektivitě.

Historicky dřívější buněčné systémy, jako je GSM, používaly Frequency Division Multiple Access (FDMA) a Time Division Multiple Access (TDMA), kde bylo synchronizace a odhadu kanálu dosahováno různými mechanismy, jako jsou frekvenční pulzy a tréninkové sekvence. Přechod na CDMA v 3G si vyžádal nový přístup. PCPICH řeší problém poskytování stabilní fázové reference v prostředí s rozprostřeným spektrem, kde jsou signály záměrně překrývány. Umožňuje klíčové síťové funkce: je majákem pro identifikaci buňky, základem pro měření síly signálu řídící procedury mobility a referencí pro beamforming v pozdějších verzích (pomocí vyhrazeného beam P-CPICH). Jeho zavedení bylo nezbytné pro praktickou implementaci a výkon sítí UMTS.

## Klíčové vlastnosti

- Vysílá známou, konstantní pilotní sekvenci (všechny nuly) pro spolehlivý odhad kanálu.
- Používá primární scramblovací kód buňky, což z něj činí primární identifikátor buňky.
- Používá pevný kanalizační kód (SF=256, kód 0) pro předvídatelné vysílání.
- Poskytuje fázovou referenci pro koherentní demodulaci ostatních downlinkových kanálů.
- Slouží jako klíčový zdroj měření pro metriky hlášené UE, jako jsou RSCP a Ec/Io.
- Je nepřetržitě vysílán s konstantním výkonem pro podporu průběžného hledání buňky a monitorování.

## Související pojmy

- [S-CPICH – Secondary Common Pilot Channel](/mobilnisite/slovnik/s-cpich/)
- [RSCP – Reference Signal Carrier Phase](/mobilnisite/slovnik/rscp/)

## Definující specifikace

- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications

---

📖 **Anglický originál a plná specifikace:** [PCPICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcpich/)
