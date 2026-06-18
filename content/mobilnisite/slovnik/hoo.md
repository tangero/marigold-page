---
slug: "hoo"
url: "/mobilnisite/slovnik/hoo/"
type: "slovnik"
title: "HOO – HandOver parameter Optimization"
date: 2025-01-01
abbr: "HOO"
fullName: "HandOver parameter Optimization"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/hoo/"
summary: "Funkce správy sítě, která automatizuje optimalizaci parametrů řízení předávání spojení. Analyzuje výkonnostní měření a klíčové ukazatele výkonu (KPI) pro úpravu prahových hodnot a hodnot hystereze s c"
---

HOO je funkce správy sítě, která automatizuje optimalizaci parametrů řízení předávání spojení (handover) analýzou KPI za účelem zvýšení robustnosti mobility a efektivity sítě.

## Popis

Optimalizace parametrů předání spojení (HOO) je funkce samo-organizující se sítě ([SON](/mobilnisite/slovnik/son/)) standardizovaná v rámci 3GPP, primárně popsaná v TS 28.628 (pro správu) a TS 32.522 (pro měření). Jedná se o automatizovaný optimalizační proces s uzavřenou smyčkou navržený pro konfiguraci a průběžné ladění mnoha parametrů, které řídí rozhodnutí o předání spojení ([HO](/mobilnisite/slovnik/ho/)) v rádiové přístupové síti (RAN). Předání spojení je klíčový mobilitní postup, při kterém je spojení uživatelského zařízení (UE) převedeno z jedné buňky (zdrojové) do jiné (cílové). Jeho výkon je velmi citlivý na parametry, jako je hysterezní rozmezí pro předání (hysteresis), doba do spuštění ([TTT](/mobilnisite/slovnik/ttt/)), individuální posuny buněk (CIO) a různé prahové hodnoty událostí (např. pro události [A3](/mobilnisite/slovnik/a3/), A5 v LTE/NR). Špatně nastavené parametry mohou vést k selháním rádiového spoje ([RLF](/mobilnisite/slovnik/rlf/)), ping-pong předáním nebo selháním předání, což zhoršuje uživatelský zážitek a efektivitu sítě.

HOO funguje na základě sběru široké škály výkonnostních měření a klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)) ze sítě. Patří mezi ně čítače pokusů o předání, úspěšných a neúspěšných předání (předčasná, pozdní, předání do nevhodné buňky), hlášení o selhání rádiového spoje, případy ping-pong předání a měření síly ([RSRP](/mobilnisite/slovnik/rsrp/)) a kvality ([RSRQ](/mobilnisite/slovnik/rsrq/)) přijímaného referenčního signálu. Algoritmus HOO, typicky umístěný v systému správy, administrace a údržby (OAM) nebo na vyhrazeném SON serveru, tato data zpracovává, aby identifikoval podoptimální vzorce výkonu. Například vysoká míra pozdních předání může naznačovat, že je prahová hodnota pro předání nastavena příliš nízko, což způsobuje, že UE zůstává příliš dlouho připojeno k slábnoucí zdrojové buňce. Algoritmus následně vypočítá nové, optimalizované hodnoty pro relevantní parametry předání a tyto konfigurační aktualizace zašle do příslušných základnových stanic (eNB/gNB).

Proces je iterativní a kontinuální, což síti umožňuje přizpůsobit se dlouhodobým změnám prostředí, jako jsou nové budovy, sezónní změny listoví nebo posuny ve vzorcích uživatelského provozu. HOO je klíčovou součástí optimalizace robustnosti mobility (MRO), což je širší případ užití SON. Automatizací této tradičně manuální a experty řízené úlohy HOO snižuje provozní náklady (OPEX), minimalizuje lidské chyby a zajišťuje důslednou optimalizaci parametrů předání v celé síti, což vede ke stabilnější a výkonnější mobilní službě. Je použitelná napříč 3GPP technologiemi, včetně LTE a NR, s konkrétními definicemi měření a parametry přizpůsobenými každému RAT.

## K čemu slouží

HOO byla vytvořena k řešení významného provozního problému ruční správy stovek parametrů předání spojení napříč tisíci buňkami v moderní mobilní síti. Před SON a HOO spoléhali síťoví inženýři na terénní měření (drive testy), heuristická pravidla a ruční analýzu KPI pro ladění těchto parametrů – proces, který byl časově náročný, nákladný, náchylný k chybám a neschopný dynamicky reagovat na změny v síti. To často vedlo k tomu, že podoptimální výkon předání zůstal po delší dobu neopravený, což způsobovalo předvídatelné ztráty hovorů a špatný uživatelský zážitek.

Hnací motivací byla rostoucí komplexita a hustota sítí, zejména se zavedením LTE a heterogenních sítí (HetNets) s malými buňkami. V takovém prostředí se počet sousedních buněčných vztahů a frekvence rozhodnutí o předání dramaticky zvyšují, čímž se ruční optimalizace stává zcela nepraktickou. HOO řeší základní problém robustnosti mobility: nalezení optimálního kompromisu mezi provedením předání příliš brzy (riziko zbytečných předání a ping-pong efektu) a příliš pozdě (riziko selhání spojení). Implementací automatizované, daty řízené uzavřené smyčky HOO zajišťuje, že síť neustále hledá tento optimální bod, čímž zlepšuje celkovou kvalitu služby. Byla základním předpokladem pro efektivní provoz sítí ve velkém měřítku, snižovala OPEX a využívala bohatství provozních dat dostupných v digitálních sítích k autonomnímu zlepšování výkonu.

## Klíčové vlastnosti

- Automatizovaná optimalizace parametrů řízení předání spojení v uzavřené smyčce
- Analýza KPI souvisejících s předáním a hlášení o selhání (např. RLF hlášení)
- Optimalizace parametrů jako hystereze, doba do spuštění (TTT) a posuny buněk
- Podpora scénářů mobility pro více RAT a heterogenní sítě (HetNet)
- Integrace v rámci širší SON funkce optimalizace robustnosti mobility (MRO)
- Kontinuální adaptace na dlouhodobé změny v rádiovém prostředí

## Definující specifikace

- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service

---

📖 **Anglický originál a plná specifikace:** [HOO na 3GPP Explorer](https://3gpp-explorer.com/glossary/hoo/)
