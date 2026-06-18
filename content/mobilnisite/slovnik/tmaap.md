---
slug: "tmaap"
url: "/mobilnisite/slovnik/tmaap/"
type: "slovnik"
title: "TMAAP – Tower Mounted Amplifier Application Part"
date: 2025-01-01
abbr: "TMAAP"
fullName: "Tower Mounted Amplifier Application Part"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tmaap/"
summary: "TMAAP je protokol používaný pro správu a řízení věžových zesilovačů (Tower Mounted Amplifiers, TMA) v základnových stanicích. Umožňuje jejich dálkovou konfiguraci, monitorování a správu poruch. Tyto R"
---

TMAAP je 3GPP protokol používaný pro dálkovou konfiguraci, monitorování a správu poruch věžových zesilovačů (Tower Mounted Amplifiers) v základnových stanicích za účelem zlepšení citlivosti uplinku a pokrytí buňky.

## Popis

Tower Mounted Amplifier Application Part (TMAAP) je standardizovaný aplikační protokol definovaný ve specifikacích 3GPP pro provoz, správu a údržbu (Operation, Administration, and Maintenance, [OAM](/mobilnisite/slovnik/oam/)) věžových zesilovačů. [TMA](/mobilnisite/slovnik/tma/) je zesilovač s nízkým šumem instalovaný na vrcholu vysílací věže, v blízkosti přijímacích antén, který zesiluje slabé uplink signály od uživatelského zařízení (UE) předtím, než dojde k výrazné kabelové ztrátě. TMAAP poskytuje komunikační rámec mezi systémem správy sítě, typicky Správcem prvku (Element Manager, [EM](/mobilnisite/slovnik/em/)) nebo Správcem sítě (Network Manager, [NM](/mobilnisite/slovnik/nm/)), a samotnou jednotkou TMA. Tento protokol funguje přes rozhraní pro správu, často využívající IP transport, k přenosu řídicích informací a příkazů.

Z architektonického hlediska TMAAP definuje soubor procedur a souvisejících zpráv pro správu poruch, správu konfigurace a správu výkonu. Pro správu poruch podporuje hlášení alarmů, což umožňuje TMA oznámit systému správy kritické poruchy, jako je výpadek napájení, degradace zesílení zesilovače nebo překročení teploty. Procedury správy konfigurace umožňují dálkové nastavení parametrů TMA, včetně nastavení zesílení, konfigurace filtrů a provozních režimů (např. bypass režim pro údržbu). Správa výkonu zahrnuje sběr klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako jsou úrovně vstupního/výstupního výkonu, šumové číslo a teplota, které jsou nezbytné pro proaktivní údržbu a zajištění optimálního výkonu zesilovače.

Role tohoto protokolu je nedílnou součástí provozu moderních rádiových přístupových sítí (Radio Access Network, RAN), neboť umožňuje automatizovanou a efektivní správu těchto pasivních nebo aktivních [RF](/mobilnisite/slovnik/rf/) komponent. Poskytnutím standardizovaného rozhraní TMAAP zajišťuje interoperabilitu mezi různými výrobci, což umožňuje operátorům sítí nasazovat TMA od různých výrobců pod jednotným systémem správy. Jeho implementace snižuje potřebu fyzických návštěv lokality za účelem rekonfigurace TMA nebo odstraňování závad, čímž se snižují provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) a zvyšuje dostupnost sítě. Návrh protokolu zohledňuje omezené prostředí TMA, často podporuje efektivní kódování zpráv a robustní zpracování chyb, aby byla zajištěna spolehlivá správa i přes potenciálně omezené backhaulové připojení.

## K čemu slouží

TMAAP byl vytvořen, aby řešil provozní výzvy spojené s nasazením a správou věžových zesilovačů, které se staly stále běžnějšími pro potírání omezení uplinku v mobilních sítích. Před standardizací byla správa [TMA](/mobilnisite/slovnik/tma/) často proprietární, což nutilo operátory používat pro TMA od různých dodavatelů samostatné, nekompatibilní systémy správy. Tento roztříštěný přístup zvyšoval provozní složitost, náklady a riziko chyb při integraci a rozšiřování sítě.

Hlavním problémem, který TMAAP řeší, je absence jednotné možnosti dálkové správy těchto kritických RF komponent. Fyzický přístup k TMA, které jsou umístěny na vrcholu vysílacích věží, je obtížný, časově náročný a nebezpečný. Bez protokolu pro dálkovou správu vyžadovala jakákoli změna konfigurace, monitorování výkonu nebo diagnostika poruchy výstup technika na věž, což vedlo k vysokým OPEX a prodlouženým výpadkům sítě. TMAAP poskytuje potřebnou abstrakci a komunikační standardy pro bezproblémovou integraci správy TMA do širšího ekosystému OAM sítě.

Jeho zavedení v 3GPP Release 8 bylo motivováno snahou průmyslu o automatizovanější a efektivnější provoz RAN, zejména s tím, jak sítě rostly a stávaly se složitějšími. Standardizací této aplikační části umožnil 3GPP operátorům spolehlivě a nákladově efektivně zlepšit výkon uplinku jejich sítě, což je zvláště klíčové pro zajištění vyvážených rozpočtů spojů a konzistentního uživatelského zážitku na okrajích buňky. Představuje klíčový krok v širším trendu standardizace správy síťových zařízení.

## Klíčové vlastnosti

- Dálková konfigurace provozních parametrů TMA (zesílení, bypass režim)
- Standardizovaná správa poruch s hlášením a oznamováním alarmů
- Monitorování výkonu prostřednictvím sběru klíčových RF ukazatelů
- Podpora softwarového stažení a dálkové aktualizace jednotky
- Definovaný informační model pro zařízení a schopnosti TMA
- Interoperabilita mezi TMA od různých výrobců a systémy správy

## Související pojmy

- [TMA – Tower Mounted Amplifier](/mobilnisite/slovnik/tma/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 37.460** (Rel-19) — Iuant Interface Introduction
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TS 37.466** (Rel-19) — Iuant Interface Introduction & RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [TMAAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmaap/)
