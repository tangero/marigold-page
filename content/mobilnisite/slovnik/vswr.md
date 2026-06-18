---
slug: "vswr"
url: "/mobilnisite/slovnik/vswr/"
type: "slovnik"
title: "VSWR – Voltage Standing Wave Ratio"
date: 2025-01-01
abbr: "VSWR"
fullName: "Voltage Standing Wave Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/vswr/"
summary: "Míra přizpůsobení impedance v rádiových frekvenčních (RF) systémech, která udává účinnost přenosu výkonu z vysílače do antény. Nízký VSWR značí dobré přizpůsobení a minimální odražený výkon, což je kl"
---

VSWR je míra impedance v RF systémech, která udává účinnost přenosu výkonu z vysílače do antény, přičemž nízká hodnota značí dobré přizpůsobení a minimální odražený výkon.

## Popis

Poměr stojatého vlnění napětí (Voltage Standing Wave Ratio, VSWR) je základní parametr v [RF](/mobilnisite/slovnik/rf/) technice, který kvantifikuje přizpůsobení impedance mezi vedením (např. koaxiálním kabelem) a jeho zátěží (typicky anténou). Je definován jako poměr maximálního napětí k minimálnímu napětí podél obrazce stojatého vlnění vzniklého na vedení v důsledku nepřizpůsobení impedance. Matematicky VSWR = (1 + |Γ|) / (1 - |Γ|), kde Γ (gama) je koeficient odrazu napětí. Dokonalé přizpůsobení, kdy je veškerý dopadající výkon předán do zátěže, vede k VSWR 1:1. V praxi jsou běžnými cílovými hodnotami např. 1,5:1 nebo 2:1, přičemž vyšší poměry značí větší nepřizpůsobení a větší odražený výkon.

V kontextu 3GPP je VSWR klíčový pro návrh, testování a provoz anténních systémů základnových stanic (NodeB, eNodeB, gNB) a uživatelského zařízení (UE). Měří se na různých rozhraních, zejména na anténním konektoru. Proces zahrnuje použití vektorového analyzátoru sítí ([VNA](/mobilnisite/slovnik/vna/)) k vyslání procházejícího RF signálu a měření odraženého signálu pro výpočet koeficientu odrazu a následně VSWR v provozním frekvenčním pásmu. Mezi klíčové komponenty ovlivňující VSWR patří návrh antény, přívodní vedení, konektory a případné přizpůsobovací obvody. Špatný VSWR může vést ke stojatým vlnám, které způsobují napěťové horké body, potenciálně poškozující výkonové zesilovače vysílače, a snižují efektivní vyzářený výkon, což ovlivňuje pokrytí a kvalitu signálu.

Specifikace 3GPP (např. v TS 37.544, 38.877) definují požadavky na VSWR a testovací postupy pro RF shodu základnových stanic. Ty zajišťují, že zařízení pracuje v síti účinně a spolehlivě. Například specifikace stanovují maximální přípustné limity VSWR na anténním portu základnové stanice, aby za definovaných podmínek zůstal odražený výkon v bezpečných a provozních mezích. Monitorování VSWR je také součástí údržby sítě; náhlý nárůst může značit poškození antény, poruchy kabelu nebo problémy způsobené prostředím, jako je námraza. VSWR tedy není pouze metrikou návrhu, ale i průběžným ukazatelem výkonu a stavu RF fyzické vrstvy, který přímo ovlivňuje kapacitu sítě, pokrytí a životnost zařízení.

## K čemu slouží

VSWR existuje jako klíčový měřicí koncept pro řešení problému neúčinného přenosu výkonu a potenciálního poškození zařízení v [RF](/mobilnisite/slovnik/rf/) systémech. Když se impedance vedení neshoduje s impedancí antény, část vysílaného výkonu se odráží zpět ke zdroji. Tento odražený výkon vytváří stojaté vlny, které mohou vést ke zvýšeným ztrátám, sníženému efektivnímu vyzářenému výkonu a nadměrnému zahřívání komponent vysílače, jako jsou výkonové zesilovače. V raných rádiových systémech mohlo nepřizpůsobení způsobit katastrofální selhání. VSWR poskytuje jednoduchou, standardizovanou metriku pro kvantifikaci tohoto nepřizpůsobení a zajištění, že systémy jsou navrženy a udržovány pro optimální výkon.

V rámci standardizace 3GPP zajišťuje definice požadavků na VSWR interoperabilitu a spolehlivost napříč zařízeními od různých dodavatelů. Řeší potřebu konzistentního RF výkonu základnových stanic a uživatelských zařízení, což je zásadní pro dosažení stanoveného pokrytí, přenosových rychlostí a účinnosti sítě. Zařazení VSWR do specifikací shodných testů (od Release 13 pro konkrétní technologie jako LTE-Advanced a NR) bylo motivováno rostoucí složitostí RF systémů se širšími šířkami pásma a víceanténními technologiemi ([MIMO](/mobilnisite/slovnik/mimo/)), kde se přizpůsobení impedance stává náročnějším. Správná správa VSWR pomáhá maximalizovat přínosy těchto pokročilých funkcí a zajišťuje, že fyzická vrstva sítě funguje podle předpokladů.

## Klíčové vlastnosti

- Kvantifikuje přizpůsobení impedance mezi vedením a anténní zátěží
- Definován jako poměr VSWR = V_max / V_min na stojaté vlně
- Přímo souvisí s odraženým výkonem a koeficientem odrazu
- Kritický parametr v RF testování shody pro základnové stanice a UE
- Používá se k monitorování stavu a výkonu anténních systémů
- Ovlivňuje účinnost vysílače, vyzářený výkon a ochranu zařízení

## Definující specifikace

- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [VSWR na 3GPP Explorer](https://3gpp-explorer.com/glossary/vswr/)
