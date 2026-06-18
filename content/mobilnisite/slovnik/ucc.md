---
slug: "ucc"
url: "/mobilnisite/slovnik/ucc/"
type: "slovnik"
title: "UCC – Used Cell Capacity"
date: 2026-01-01
abbr: "UCC"
fullName: "Used Cell Capacity"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ucc/"
summary: "Klíčový ukazatel výkonu (KPI), který měří využitou kapacitu rádiových zdrojů buňky. Je zásadní pro monitorování výkonu sítě, plánování kapacity a vyvažování provozního zatížení, neboť pomáhá operátorů"
---

UCC je klíčový ukazatel výkonu, který měří využitou kapacitu rádiových zdrojů buňky pro monitorování sítě, plánování kapacity a vyvažování provozního zatížení.

## Popis

Used Cell Capacity (UCC) je koncept správy a měření výkonu definovaný ve specifikacích 3GPP pro správu síťových zdrojů a výkonu. Kvantifikuje množství rádiových přenosových zdrojů, které jsou aktivně využívány v rámci buňky v daném okamžiku nebo během měřicího období. UCC není jediná metrika, ale kategorie měření, která může být odvozena z různých čítačů a ukazatelů nižších vrstev souvisejících s využitím zdrojových bloků, využitím kódů, spotřebou výkonu nebo propustností, v závislosti na technologii rádiového přístupu (např. LTE, NR).

Z architektonického hlediska jsou data UCC shromažďována systémem správy sítě, typicky přes rozhraní Itf-N nebo v rámci Operation and Support System ([OSS](/mobilnisite/slovnik/oss/)). Základnová stanice (eNodeB v LTE, gNB v NR) měří využití svých fyzických zdrojů. Například v systému založeném na [OFDMA](/mobilnisite/slovnik/ofdma/), jako je LTE nebo NR, to může zahrnovat měření procenta alokovaných Physical Resource Blocks ([PRB](/mobilnisite/slovnik/prb/)) v časově-frekvenční mřížce. Tato hrubá měření jsou následně zpracována a agregována do dat měření výkonu ([PM](/mobilnisite/slovnik/pm/)) souvisejících s UCC, která jsou hlášena systému správy sítě podle specifikací norem jako je 3GPP TS 32.156 (Performance Management).

Jak UCC funguje, zahrnuje kontinuální monitorování a reportování. Síťový prvek implementuje specifické měřicí vzorce definované v 3GPP TS 28.821 (Management and orchestration; Telecommunication management; Performance measurements for 5G networks and network slicing). Tyto vzorce převádějí hrubé využití zdrojů na standardizované [KPI](/mobilnisite/slovnik/kpi/). Měření UCC může být segmentováno podle typu služby, slice nebo třídy QoS, což poskytuje podrobné přehledy. Systém správy pak tato data používá pro funkce jako plánování kapacity (k identifikaci buněk vyžadujících hardwarové upgrady), řízení provozu (pro odlehčení přetížených buněk) a zajištění plnění smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) pro síťové slice. Jeho role je klíčová v uzavřené smyčce automatizace moderních sítí, kdy zásobuje analytické a politické enginy daty, která pohánějí samooptymalizaci.

## K čemu slouží

UCC bylo zavedeno, aby poskytlo operátorům standardizovaný, technologií nezávislý způsob měření a správy spotřeby vzácných rádiových zdrojů. Před jeho formální definicí se operátoři spoléhali na dodavatelsky specifické nebo ad-hoc metriky, což ztěžovalo správu sítí více dodavatelů a benchmarkování. UCC řeší potřebu společného jazyka pro využití kapacity v sítích s více dodavateli a technologiemi.

Primární problém, který řeší, je efektivní správa síťové kapacity pro udržení kvality služeb a uživatelského zážitku. Přesným měřením využité kapacity mohou operátoři proaktivně identifikovat místa přetížení, plánovat rozšíření sítě a implementovat strategie vyvažování zatížení. Je to základní vstup pro algoritmy řízení provozu a optimalizace sítě.

Jeho vytvoření bylo dále motivováno vývojem směrem ke složitějším sítím s agregací nosných, síťovým slicingem a massive IoT. V těchto kontextech se stává kritickým porozumění tomu, jak je kapacita spotřebovávána různými službami (např. enhanced Mobile Broadband vs. massive IoT) nebo různými klienty (v síťovém slici). UCC, jak je definováno ve specifikacích správy jako TS 28.821, poskytuje rámec pro tato podrobná, na služby zaměřená měření kapacity, což umožňuje efektivní rozdělování zdrojů a zaručuje izolaci mezi slice nebo typy služeb.

## Klíčové vlastnosti

- Standardizovaný KPI pro měření využití rádiových zdrojů
- Podporuje technologií specifické derivace (např. využití PRB v LTE/NR)
- Umožňuje detailní měření podle typu služby nebo síťového slicu
- Zásobuje systémy správy a orchestrace sítě (MANO)
- Kritický pro plánování kapacity a detekci přetížení
- Usnadňuje automatizované řízení provozu a vyvažování zatížení

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)

## Definující specifikace

- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS
- **TS 28.821** (Rel-13) — UML Model Repertoire for FMC Management
- **TS 32.156** (Rel-20) — UML Modeling for Network Management Systems

---

📖 **Anglický originál a plná specifikace:** [UCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ucc/)
