---
slug: "cgp"
url: "/mobilnisite/slovnik/cgp/"
type: "slovnik"
title: "CGP – Charge Generation Point"
date: 2025-01-01
abbr: "CGP"
fullName: "Charge Generation Point"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cgp/"
summary: "Charge Generation Point (CGP) je síťová funkce odpovědná za vytváření účtovacích záznamů za využití sítě a služeb. Shromažďuje účtovací informace z různých síťových prvků a formátuje je pro fakturační"
---

CGP je síťová funkce odpovědná za vytváření účtovacích záznamů sběrem a formátováním účtovacích informací ze síťových prvků pro fakturační systémy.

## Popis

Charge Generation Point (CGP) je klíčová komponenta v účtovací architektuře 3GPP, která slouží jako centrální entita pro generování standardizovaných záznamů účtovacích dat. Funguje v rámci architektury Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)) a je odpovědná za přijímání, zpracování a formátování účtovacích informací z více síťových prvků před jejich předáním do fakturační domény. CGP funguje jako prostředník mezi síťovými funkcemi, které generují účtovací události, a fakturačními systémy, které je zpracovávají pro inkaso výnosů.

Architektonicky CGP komunikuje s různými Charging Trigger Functions ([CTF](/mobilnisite/slovnik/ctf/)) umístěnými v síťových prvcích jako [MME](/mobilnisite/slovnik/mme/), SGW, PGW a aplikační servery. Tyto CTF detekují zpoplatnitelné události a posílají Charging Data Requests ([CDR](/mobilnisite/slovnik/cdr/)) do CGP přes standardizovaná rozhraní. CGP tyto požadavky přijímá, validuje účtovací informace, koreluje související události z různých síťových prvků a vytváří konsolidované Charging Data Records (CDR) ve vhodném formátu. Tyto naformátované záznamy jsou následně přeneseny do fakturačního systému pro další zpracování a generování faktur.

Klíčové komponenty uvnitř CGP zahrnují modul sběru účtovacích dat, který přijímá účtovací události ze síťových prvků; korelační engine, který asociuje související účtovací události z různých zdrojů; formátovací modul, který vytváří standardizované CDR; a přenosovou funkci, která doručuje dokončené záznamy do fakturačních systémů. CGP také obsahuje validační mechanismy pro zajištění integrity a konzistence účtovacích dat před předáním do fakturačních domén. Podporuje různé účtovací modely včetně časového, objemového, událostního a relací založeného účtování.

Role CGP přesahuje pouhý sběr dat a zahrnuje důležité funkce jako agregaci účtovacích dat, kdy kombinuje více účtovacích událostí do komplexních záznamů; mediaci dat, kdy transformuje účtovací informace do formátů kompatibilních s fakturačními systémy; a správu účtovacích relací, kdy udržuje stavové informace pro probíhající účtovací relace. Centralizací těchto funkcí CGP snižuje složitost v jednotlivých síťových prvcích a poskytuje standardizované rozhraní pro fakturační systémy, což umožňuje operátorům zavádět nové služby bez nutnosti změn jejich fakturační infrastruktury.

## K čemu slouží

Charge Generation Point (CGP) byl vytvořen, aby řešil rostoucí složitost účtování v mobilních sítích s vývojem služeb přesahujících jednoduché hlasové hovory. Před jeho zavedením byly účtovací funkce distribuovány napříč síťovými prvky, což vedlo k nekonzistentním formátům účtovacích dat, obtížím v korelaci účtovacích událostí z různých síťových domén a výzvám v integraci nových služeb s existujícími fakturačními systémy. Tento distribuovaný přístup ztěžoval operátorům přesně účtovat za komplexní služby zahrnující více síťových prvků a servisních komponent.

CGP tyto problémy řeší tím, že poskytuje centralizovanou funkci generování účtování, která standardizuje způsob sběru, zpracování a formátování účtovacích informací. Umožňuje operátorům implementovat konzistentní účtovací politiky napříč různými síťovými doménami a typy služeb, zjednodušuje integraci nových síťových prvků a služeb s fakturačními systémy a zlepšuje přesnost a spolehlivost účtovacích dat. Oddělením generování účtování od síťových funkcí umožňuje CGP síťovým prvkům soustředit se na jejich primární funkce, zatímco zajišťuje, že jsou požadavky na účtování konzistentně naplňovány.

Historicky zavedení CGP ve verzi Release 8 časově souviselo s přechodem na sítě LTE/EPC a rozšířením datových služeb, které vyžadovaly sofistikovanější účtovací schopnosti než předchozí generace. Architektura CGP byla navržena tak, aby podporovala rozmanité účtovací požadavky služeb založených na IP, včetně diferenciace kvality služby, roamingových scénářů a komplexních balíčků služeb. Řešila omezení dřívějších účtovacích přístupů tím, že poskytla škálovatelný a flexibilní rámec, který se mohl vyvíjet spolu s síťovou technologií a inovacemi služeb.

## Klíčové vlastnosti

- Centralizovaný sběr účtovacích dat z více síťových prvků
- Standardizované generování a formátování Charging Data Record (CDR)
- Korelace účtovacích událostí napříč různými síťovými doménami
- Podpora více účtovacích modelů (časový, objemový, událostní, relací založený)
- Mediace rozhraní mezi síťovými funkcemi a fakturačními systémy
- Validace účtovacích dat a kontrola integrity

## Definující specifikace

- **TS 29.458** (Rel-8) — SIP Transfer of Tariff Info for Charging
- **TS 29.658** (Rel-19) — SIP Transfer of Tariff Information

---

📖 **Anglický originál a plná specifikace:** [CGP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cgp/)
