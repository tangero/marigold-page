---
slug: "l2s"
url: "/mobilnisite/slovnik/l2s/"
type: "slovnik"
title: "L2S – Link to System mapping"
date: 2025-01-01
abbr: "L2S"
fullName: "Link to System mapping"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/l2s/"
summary: "Simulační metodologie používaná k vyhodnocení výkonu rádiového spoje v mobilních sítích. Převádí podmínky kanálu fyzické vrstvy na metriky výkonu na systémové úrovni, což umožňuje realistické síťové s"
---

L2S je simulační metodologie, která převádí podmínky kanálu fyzické vrstvy na metriky výkonu na systémové úrovni za účelem vyhodnocení výkonu rádiového spoje v mobilních sítích.

## Popis

Link to System (L2S) mapování je klíčová metodologie definovaná v 3GPP pro systémové simulace mobilních sítí. Slouží jako most mezi podrobnými, výpočetně náročnými simulacemi na úrovni spoje (které modelují přenos a příjem na fyzické vrstvě jednotlivých rádiových rámců v konkrétním kanálu) a simulacemi na vyšší, systémové úrovni (které modelují topologii sítě, mobilitu uživatelů, charakteristiky provozu a správu zdrojů). Hlavní problém, který L2S řeší, je obrovský rozdíl v časových měřítcích a komplexitě simulací; simulace na úrovni spoje pracují v časech symbolů nebo bitů, zatímco systémové simulace pracují v časech hovorů nebo paketů.

Metodologie funguje tak, že abstrahuje chování fyzické vrstvy do sady vyhledávacích tabulek nebo matematických modelů. Tyto modely, často nazývané 'interface tables' nebo techniky 'effective SINR mapping' ([ESM](/mobilnisite/slovnik/esm/)), jsou generovány offline z rozsáhlých simulací na úrovni spoje. Mapují sadu okamžitých ukazatelů kvality kanálu (jako SINR na subnosnou v systémech [OFDM](/mobilnisite/slovnik/ofdm/)) pozorovaných přijímačem na jedinou efektivní metriku kvality. Tato efektivní metrika je pak použita k určení pravděpodobnosti správného dekódování transportního bloku na základě zvoleného schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)). Tato abstrakce umožňuje systémovým simulátorům předpovídat míru chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)) a propustnost bez nutnosti spouštět simulace spoje v reálném čase.

Klíčovými součástmi rámce L2S jsou definice modelu kanálu, simulátor na úrovni spoje používaný k vytváření výkonnostních tabulek a konkrétní mapovací algoritmus (např. Exponential ESM, Mutual Information ESM). Jeho role je zásadní v procesu standardizace, protože umožňuje různým společnostem a výzkumníkům porovnávat výkon navrhovaných rádiových technologií (jako jsou nové tabulky MCS, algoritmy plánování nebo konfigurace antén) za konzistentních a srovnatelných předpokladů. Je rozsáhle používán pro hodnocení pokrytí, kapacity a výkonu mobility u technologií od GSM po 5G NR.

## K čemu slouží

L2S mapování existuje proto, aby učinilo hodnocení výkonu komplexních mobilních rádiových systémů proveditelným a standardizovaným. Před jeho formalizací bylo porovnávání různých síťových návrhů nebo technologií obtížné kvůli nekonzistentním simulačním předpokladům a metodologiím. Každý výrobce nebo výzkumná skupina mohla používat proprietární, nesrovnatelné modely spoje, což znemožňovalo objektivní posouzení přínosů nových funkcí.

Vytvoření L2S, formalizovaného v 3GPP TR 45.914 pro GSM/[EDGE](/mobilnisite/slovnik/edge/) a později aplikovaného na UMTS, LTE a NR, bylo motivováno potřebou společného, dohodnutého hodnotícího rámce. Řeší problém výpočetní neřešitelnosti; přímé propojení plnohodnotného simulátoru spoje se systémovým simulátorem pokrývajícím stovky buněk a tisíce uživatelů je nepřijatelně pomalé. Poskytnutím zjednodušené, ale přesné abstrakce umožňuje L2S rozsáhlé, statisticky významné studie výkonu sítě v přiměřeném výpočetním čase.

Historicky řešilo omezení příliš zjednodušených systémových modelů, které používaly pevné [BLER](/mobilnisite/slovnik/bler/) křivky nebo ignorovaly rychlé úniky, což vedlo k nepřesným predikcím kapacity. L2S zavedlo standardizovaný způsob, jak zohlednit vliv realistických, časově proměnných podmínek rádiového kanálu na klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) na systémové úrovni, a zajistilo tak, že tvrzení o výkonu během standardizace 3GPP jsou založena na konzistentní a transparentní metodologii.

## Klíčové vlastnosti

- Abstrakce výkonu fyzické vrstvy do předpočítaných vyhledávacích tabulek
- Umožňuje výpočetně efektivní rozsáhlé simulace na systémové úrovni
- Standardizovaná metodologie zajišťující srovnatelné výsledky mezi různými posuzovateli
- Podporuje více algoritmů Effective SINR Mapping (ESM) pro různé technologie
- Aplikovatelné napříč více generacemi 3GPP (GSM, UMTS, LTE, NR)
- Integruje podrobné modely kanálu (např. tapped delay lines, prostorovou korelaci) do analýzy výkonu sítě

## Definující specifikace

- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [L2S na 3GPP Explorer](https://3gpp-explorer.com/glossary/l2s/)
