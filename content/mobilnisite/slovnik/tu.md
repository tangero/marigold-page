---
slug: "tu"
url: "/mobilnisite/slovnik/tu/"
type: "slovnik"
title: "TU – Typical Urban"
date: 2025-01-01
abbr: "TU"
fullName: "Typical Urban"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tu/"
summary: "Standardizovaný kanálový model představující prostředí šíření rádiového signálu typické pro městské oblasti se střední až vysokou hustotou zástavby. Je hojně používán při testování výkonu a simulacích"
---

TU je standardizovaný 3GPP kanálový model představující typické městské rádiové prostředí se střední až vysokou hustotou zástavby, používaný pro testování výkonu za realistických vícecestných podmínek.

## Popis

Kanálový model Typical Urban (TU) je konkrétní případ vícecestného modelu šíření definovaného 3GPP pro účely zkoušení shody, hodnocení výkonu a simulace systému. Charakterizuje chování rádiového signálu v typickém městském makro-buňkovém prostředí. Model definuje sadu diskrétních cest (odboček), z nichž každá má specifikované relativní zpoždění, průměrný výkon a Dopplerovo spektrum. Tyto parametry reprezentují rozptyl, odraz a ohyb rádiových vln způsobený budovami a dalšími strukturami v městské krajině.

Technicky je model TU modelem s odbočkami a zpožděním. Například běžná definice TU pro testování GSM/[EDGE](/mobilnisite/slovnik/edge/) (specifikovaná v 45.005) zahrnuje 12 odboček se specifickými zpožděními a výkony. Model předpokládá rychlost pohybu mobilního zařízení, která ovlivňuje Dopplerovo rozprostření aplikované na každou odbočku, čímž simuluje efekt pohybu. Dopplerovo spektrum je typicky klasické (Jakesovo) nebo zaoblené, představující rovnoměrné rozložení úhlů příchodu. To vytváří časově proměnný kanál, který útlumově kolísá podle Rayleighova nebo Riceova rozdělení v závislosti na přítomnosti dominantní přímé cesty (TU je typicky bez přímé viditelnosti, což vede k Rayleighovu útlumu).

Při návrhu a testování systému je model TU aplikován na základnovou simulaci rádiového spoje. Při testování přijímače použije generátor signálu nebo emulátor sítě parametry TU ke zkreslení vysílaného signálu před jeho přivedením do testovaného přijímače. Tím se testuje schopnost přijímače zvládnout mezisymbolové rušení ([ISI](/mobilnisite/slovnik/isi/)) způsobené vícecestným rozprostřením zpoždění a jeho schopnost sledovat a kompenzovat rychlé útlumové kolísání signálu. Klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)) nebo propustnost, se měří za podmínek kanálu TU, aby se zajistilo, že zařízení nebo síť splňuje minimální požadavky na výkon.

Úlohou modelu TU je poskytnout reprodukovatelnou, standardizovanou a realisticky náročnou testovací podmínku. Umožňuje spravedlivé srovnání zařízení různých výrobců a různých vydání standardu. Je jedním z několika definovaných prostředí, jako je Rural Area ([RA](/mobilnisite/slovnik/ra/)), Hilly Terrain ([HT](/mobilnisite/slovnik/ht/)) a Pedestrian A/B ([PA](/mobilnisite/slovnik/pa/)/[PB](/mobilnisite/slovnik/pb/)). Model TU se svým středním rozprostřením zpoždění (řádově několik mikrosekund) a významným vícecestným šířením je považován za referenční bod pro hodnocení přijímacích algoritmů, jako jsou ekvalizéry a odhadovače kanálu v systémech 2G (GSM), 3G (UMTS) a 4G (LTE). Jeho parametry byly přizpůsobeny pro různé kmitočty nosné a šířky pásma napříč vydáními standardů.

## K čemu slouží

Kanálový model TU byl vytvořen, aby vyřešil problém nekonzistentního a nerealistického testování výkonu mobilních rádiových zařízení. Před standardizovanými modely mohli výrobci testovat za ideálních nebo proprietárních kanálových podmínek, což vedlo k nadsazeným tvrzením o výkonu, která neodpovídala skutečnému nasazení v městském prostředí. Účelem je definovat společný, dohodnutý referenční bod, který reprezentuje náročný, ale typický reálný scénář, a zajistit tak, že zařízení a sítě jsou dostatečně robustní pro skutečné použití.

Historicky mají kanálové modely jako TU kořeny v evropském projektu COST 207, který vyvinul modely pro GSM. 3GPP tyto modely přijalo a formalizovalo pro svou vlastní standardizační práci. Motivací bylo umožnit specifikaci minimálních požadavků na výkon (MPR) v technických specifikacích. Tyto MPR, testované pomocí modelů jako TU, zaručují základní úroveň kvality služby a interoperability v celém ekosystému.

Řeší omezení testování pouze v podmínkách aditivního bílého Gaussovského šumu (AWGN), což je pro širokoplošné mobilní systémy nedostatečné. Městská prostředí představují specifické výzvy: vícecestné rozprostření zpoždění způsobuje mezisymbolové rušení a mobilita způsobuje časově selektivní útlum. Model TU tyto efekty zachycuje. Jeho existence umožňuje návrhářům systémů optimalizovat algoritmy (např. volbu délky ekvalizéru) vůči známému, standardnímu cíli. Dále poskytuje společný jazyk pro výzkumníky a inženýry k porovnávání výsledků simulací. Jak se sítě vyvíjely směrem k LTE a 5G, byly pro hodnocení MIMO zavedeny nové prostorové kanálové modely (např. SCM, CDL), ale modely s odbočkami a zpožděním, jako je TU, zůstávají klíčové pro základní zkoušení shody výkonu přijímače.

## Klíčové vlastnosti

- Definuje vícecestný model s odbočkami a zpožděním se specifickými zpožděními a výkony odboček
- Reprezentuje městské makro-buňkové prostředí bez přímé viditelnosti se středním rozprostřením zpoždění
- Zahrnuje Dopplerovo rozprostření pro simulaci efektu mobility koncového zařízení
- Používá se jako povinná testovací podmínka pro zkoušení shody výkonu přijímače
- Umožňuje reprodukovatelné a srovnatelné hodnocení výkonu systému napříč výrobci
- Parametry jsou specifikovány pro různé systémy (GSM, UMTS, LTE) a kmitočtová pásma

## Definující specifikace

- **TR 25.943** (Rel-19) — Channel Models for Deployment Evaluation
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations
- **TS 45.820** (Rel-13) — CIoT for Internet of Things
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [TU na 3GPP Explorer](https://3gpp-explorer.com/glossary/tu/)
