---
slug: "ht"
url: "/mobilnisite/slovnik/ht/"
type: "slovnik"
title: "HT – Hilly Terrain"
date: 2025-01-01
abbr: "HT"
fullName: "Hilly Terrain"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ht/"
summary: "Standardizovaný model terénu používaný v 3GPP pro simulace šíření rádiového signálu a plánování sítí. Definuje specifické charakteristiky prostředí, jako je zvlnění terénu a překážky, k modelování cho"
---

HT je standardizovaný model terénu používaný v 3GPP simulacích šíření rádiového signálu k definování charakteristik prostředí, jako je zvlnění terénu, což zajišťuje realistické predikce výkonu mobilních sítí v kopcovitých oblastech.

## Popis

Hilly Terrain (HT) je definovaný model prostředí v rámci specifikací 3GPP, primárně používaný pro plánování rádiových sítí, simulace a testování výkonu. Není to síťový protokol ani architektura, ale klíčový vstupní parametr pro modely šíření a simulace kanálů. Model charakterizuje specifický typ krajiny s mírnou až významnou variací nadmořské výšky, odlišný od jiných standardizovaných prostředí jako Urban, Suburban, Rural nebo Indoor. Tyto modely jsou zásadní pro predikci chování rádiových vln, včetně útlumu na dráze, stínování a mnohacestných jevů, které přímo ovlivňují výpočty pokrytí, kapacity a kvality služeb.

Model HT je aplikován v rámci standardizovaných modelů šíření a kanálových podmínek definovaných v 3GPP Technických zprávách (TR) a Specifikacích (TS). Například ovlivňuje parametry v modelu Okumura-Hata, modelu COST-231 nebo pokročilejších 3D prostorových kanálových modelech (SCM) používaných pro [MIMO](/mobilnisite/slovnik/mimo/) simulace. Klíčové parametry spojené s HT zahrnují výšku zvlnění terénu (např. Δh, rozdíl mezi 10 % a 90 % výšek terénu na určité vzdálenosti), průměrný sklon a hustotu a výšku vegetace nebo překážek (jako jsou stromy). Tyto parametry se používají k výpočtu středního útlumu na dráze a statistického rozdělení stínování (lognormální fading), které signály zažívají.

V praktickém použití nástroje pro plánování sítí zpracovávají tyto modely terénu spolu s digitálními výškovými mapami k simulaci výkonu sítě. Pro systémové simulace, zejména pro funkce jako pokročilé anténní systémy ([AAS](/mobilnisite/slovnik/aas/)) nebo komunikace vozidlo-se-vším (V2X), scénář HT poskytuje opakovatelnou, standardizovanou testovací podmínku pro vyhodnocení nových algoritmů nebo hardwaru v realistických, náročných podmínkách šíření. Jeho role spočívá v zajištění toho, aby hodnocení výkonu napříč různými dodavateli a výzkumnými skupinami byla srovnatelná a zakládala se na společném chápání ne-městského, topograficky členitého prostředí.

## K čemu slouží

Model Hilly Terrain byl vytvořen, aby poskytl standardizované, reprodukovatelné referenční prostředí pro vývoj, testování a validaci výkonu 3GPP technologií rádiového přístupu. Před takovou standardizací mohly simulace a tvrzení o výkonu vycházet z příliš zjednodušených nebo nekonzistentních předpokladů o prostředí, což ztěžovalo srovnání výsledků mezi různými dodavateli zařízení nebo výzkumnými studiemi. Model HT tento problém řeší definováním specifické, dohodnuté sady charakteristik terénu.

Jeho vytvoření bylo motivováno potřebou realistického plánování sítí a robustního návrhu systémů. Mobilní sítě musí spolehlivě fungovat v různorodých geografických podmínkách. Kopcovité prostředí představuje jedinečné výzvy, jako je významné stínování, rychlé změny síly signálu a potenciál pro díry v pokrytí, které jsou v rovinatých terénech méně výrazné. Začleněním HT do testovacích specifikací 3GPP zajišťuje, že technologie od GSM/[EDGE](/mobilnisite/slovnik/edge/) přes LTE, NR a dále jsou hodnoceny vůči těmto výzvám, což vede k odolnějším síťovým zařízením a nasazovacím směrnicím, které fungují v reálných podmínkách mimo ideální laboratorní prostředí.

## Klíčové vlastnosti

- Standardizovaný model prostředí pro opakovatelné testování
- Definuje specifické parametry zvlnění terénu a překážek
- Používá se jako vstup pro výpočty útlumu při šíření (např. modely útlumu na dráze)
- Poskytuje statistické parametry pro rozdělení stínování
- Umožňuje srovnatelné benchmarkování výkonu napříč dodavateli a verzemi
- Aplikován v simulacích na úrovni spoje i systému pro plánování sítí

## Definující specifikace

- **TR 25.943** (Rel-19) — Channel Models for Deployment Evaluation
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [HT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ht/)
