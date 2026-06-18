---
slug: "ovsf"
url: "/mobilnisite/slovnik/ovsf/"
type: "slovnik"
title: "OVSF – Orthogonal Variable Spreading Factor"
date: 2025-01-01
abbr: "OVSF"
fullName: "Orthogonal Variable Spreading Factor"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ovsf/"
summary: "Technika generování kódů používaná ve WCDMA (UMTS) k vytváření ortogonálních kanalizačních kódů. Tyto kódy oddělují různé uživatelské a řídicí kanály vysílané na stejné frekvenci a ve stejném časovém"
---

OVSF je technika generování kódů používaná ve WCDMA k vytváření ortogonálních kanalizačních kódů, které oddělují různé kanály na stejné frekvenci, což umožňuje proměnlivé datové rychlosti při minimalizaci interference.

## Popis

Kódy Orthogonal Variable Spreading Factor (OVSF) jsou základní součástí rozhraní Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)) používaného v UMTS. Poskytují kanalizační funkci v downlinku i uplinku. Strom OVSF kódů je generován rekurzivně: je definován kořenový kód (např. C_{ch,1,0} = [1]) a každý rodičovský kód vytváří dva dceřiné kódy. Jeden dceřiný kód je konkatenací rodičovského kódu se sebou samým ([P, P]) a druhý je konkatenací rodičovského kódu s jeho inverzí ([P, -P]). Tato struktura vytváří sadu kódů, kde jsou libovolné dva kódy ortogonální, pokud ani jeden není předchůdcem druhého ve stromu. Rozprostírací faktor ([SF](/mobilnisite/slovnik/sf/)) definuje délku kódu a je nepřímo úměrný symbolové rychlosti; nižší SF (kratší kód) poskytuje vyšší datovou rychlost a vyšší SF (delší kód) poskytuje nižší datovou rychlost. Fyzickému kanálu je přiřazen konkrétní OVSF kód ze stromu. To umožňuje systému multiplexovat kanály s různými datovými rychlostmi současně na stejném kmitočtu nosné. Ortogonalita, pokud je zachována (zejména v downlinku se synchronním přenosem), výrazně snižuje vícenásobný přístupový šum ([MAI](/mobilnisite/slovnik/mai/)) mezi kanály. Správa kódů, včetně jejich přiřazování a blokování za účelem zachování ortogonality, je klíčovou funkcí Radio Network Controlleru ([RNC](/mobilnisite/slovnik/rnc/)).

## K čemu slouží

Kódy OVSF byly vyvinuty speciálně pro [WCDMA](/mobilnisite/slovnik/wcdma/)/UMTS, aby vyřešily výzvu podpory více uživatelů a služeb s vysoce variabilními datovými rychlostmi v jediném frekvenčním pásmu. Předchozí systémy [CDMA](/mobilnisite/slovnik/cdma/), jako IS-95, používaly Walshovy kódy s pevným rozprostíracím faktorem, což omezovalo flexibilitu. Hlavním problémem, který OVSF řeší, je, jak zachovat ortogonalitu mezi kanály a zároveň umožnit, aby rozprostírací faktor (a tedy i datová rychlost) byl proměnlivý pro každé spojení. To bylo zásadní pro cíl UMTS podporovat jak hlasové, tak vysokorychlostní datové služby. Stromová struktura tuto flexibilitu elegantně poskytuje: volání s vysokou rychlostí používá kód s nízkým [SF](/mobilnisite/slovnik/sf/) (zabírá velkou větev stromu), zatímco více volání s nízkou rychlostí může používat kódy s vyšším SF z disjunktních větví téhož stromu. Řešilo to omezení pevného rozprostíracího faktoru a umožnilo efektivní a dynamické přidělování zdrojů, které je klíčové pro služby 3G. Motivací bylo maximalizovat spektrální účinnost a kapacitu v prostředí smíšených služeb.

## Klíčové vlastnosti

- Generuje ortogonální kanalizační kódy pomocí rekurzivní stromové struktury
- Podporuje proměnlivé rozprostírací faktory (SF), což umožňuje proměnlivé uživatelské datové rychlosti
- Zachovává ortogonalitu mezi kódy s různými SF při správném přidělení
- Základní pro oddělení kanálů v downlinku a uplinku ve WCDMA
- Umožňuje dynamické přiřazování a správu kódů ze strany RNC
- Funkce blokování kódu: přiřazení kódu zablokuje všechny jeho potomky a předky za účelem zachování ortogonality

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.823** (Rel-8) — Synchronised E-DCH Study for UTRA FDD
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements

---

📖 **Anglický originál a plná specifikace:** [OVSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ovsf/)
