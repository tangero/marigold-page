---
slug: "larfcn"
url: "/mobilnisite/slovnik/larfcn/"
type: "slovnik"
title: "LARFCN – LCR TDD Absolute Radio Frequency Channel Number"
date: 2025-01-01
abbr: "LARFCN"
fullName: "LCR TDD Absolute Radio Frequency Channel Number"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/larfcn/"
summary: "Jedinečný číselný identifikátor používaný k určení přesné kmitočtové nosné pro provoz v režimu časového duplexu (TDD) s nízkou čipovou rychlostí (LCR) v UTRA. Poskytuje standardizovanou metodu pro kmi"
---

LARFCN je jedinečný číselný identifikátor používaný k určení přesné kmitočtové nosné pro provoz v režimu časového duplexu (TDD) s nízkou čipovou rychlostí (LCR) v UTRA.

## Popis

Absolutní číslo rádiového kmitočtového kanálu pro [LCR](/mobilnisite/slovnik/lcr/) [TDD](/mobilnisite/slovnik/tdd/) (LARFCN) je klíčový parametr ve specifikacích [UTRA](/mobilnisite/slovnik/utra/) (UMTS Terrestrial Radio Access) pro TDD režim, konkrétně pro variantu s nízkou čipovou rychlostí (LCR) 1,28 Mcps. Slouží jako standardizovaný index, který se mapuje na absolutní hodnotu rádiového kmitočtu. Výpočet skutečné kmitočtové nosné z LARFCN je definován konkrétním vzorcem ve specifikacích 3GPP, který zohledňuje, že v TDD režimu používají uplink i downlink stejný kmitočet. Tento identifikátor je zásadní pro konfiguraci sítě, plánování buněk a hlášení měření od UE.

Z architektonického hlediska LARFCN používá řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) a Node B (základnová stanice) ke konfiguraci pracovního kmitočtu buňky. Je také vysílán v blocích systémových informací ([SIB](/mobilnisite/slovnik/sib/)), aby uživatelské zařízení (UE) mohlo identifikovat a měřit sousední buňky. UE používá LARFCN v hlášeních měření, například pro procedury převýběru buňky nebo předání, aby informovalo síť o kvalitě signálu na konkrétních kmitočtech. To umožňuje RNC činit informovaná rozhodnutí v řízení rádiových zdrojů.

Klíčové komponenty spojené s LARFCN zahrnují měřicí jednotku UE, rádiový vysílač/přijímač Node B a algoritmy řízení rádiových zdrojů v RNC. Jeho role je základní pro kmitočtové dělení v rámci TDD spektra, což umožňuje více operátorům nasazovat sítě bez interference používáním odlišných, číselně označených kanálů. Je to základní kámen pro správu mobility v TDD sítích, který zajišťuje, že UE mohou přesně identifikovat a připojit se ke správné kmitočtové nosné při pohybu.

## K čemu slouží

LARFCN byl vytvořen, aby poskytl jasnou, jednoznačnou a standardizovanou metodu pro identifikaci kmitočtových nosných v [LCR](/mobilnisite/slovnik/lcr/) [TDD](/mobilnisite/slovnik/tdd/) režimu [UTRA](/mobilnisite/slovnik/utra/). Před takovou standardizací mohlo být kmitočtové plánování a komunikace mezi sítěmi náchylné k chybám při používání surových kmitočtových hodnot. LARFCN abstrahuje fyzický kmitočet do spravovatelného celého čísla, což zjednodušuje procedury konfigurace, provozu a údržby sítě.

Historický kontext spočívá ve vývoji UMTS, který zahrnoval jak FDD, tak TDD režimy. TDD režim, zejména jeho LCR varianta (známá také jako TD-SCDMA), vyžadoval vlastní specifický systém číslování kmitočtů odlišný od UARFCN pro FDD. To bylo nutné z důvodu různých kmitočtových pásem a duplexních metod. LARFCN řeší problém efektivního řízení TDD spektra a umožňuje funkce jako automatizované kmitočtové plánování, konzistentní hlášení měření napříč dodavateli a spolehlivé provádění předání.

Řeší omezení ad-hoc odkazování na kmitočty a zajišťuje, že všechny síťové prvky a UE od různých výrobců mají společnou představu o tom, který kmitočet je používán. Tato interoperabilita je klíčová pro úspěšné nasazení a provoz 3G TDD sítí, zejména v regionech, kde byla tato technologie významně nasazena.

## Klíčové vlastnosti

- Jednoznačně identifikuje kmitočtovou nosnou pro buňky LCR TDD (1,28 Mcps).
- Umožňuje standardizované kmitočtové plánování a konfiguraci buněk.
- Používá se v hlášeních měření od UE pro procedury mobility.
- Vysílán v systémových informacích pro identifikaci buňky.
- Poskytuje referenci nezávislou na dodavateli pro správu sítě.
- Zásadní pro řízení interference a alokaci spektra v TDD pásmech.

## Související pojmy

- [UARFCN – UTRA Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/uarfcn/)
- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)
- [UTRA – Universal Terrestrial Radio Access](/mobilnisite/slovnik/utra/)

## Definující specifikace

- **TS 25.116** (Rel-19) — LCR TDD Repeater RF Characteristics
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing

---

📖 **Anglický originál a plná specifikace:** [LARFCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/larfcn/)
