---
slug: "tbg"
url: "/mobilnisite/slovnik/tbg/"
type: "slovnik"
title: "TBG – Transport Block Group"
date: 2025-01-01
abbr: "TBG"
fullName: "Transport Block Group"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tbg/"
summary: "V 5G NR je TBG skupina jednoho nebo více transportních bloků (TB), které jsou společně naplánovány a sdílejí stejný hybridní ARQ (HARQ) proces. Umožňuje přenos více TB v rámci jediného přidělení zdroj"
---

TBG je skupina jednoho nebo více transportních bloků, které jsou společně naplánovány a sdílejí stejný HARQ proces v 5G NR, což umožňuje přenos více TB v rámci jediného přidělení zdrojů pro vysoké datové rychlosti.

## Popis

Transport Block Group (TBG) je koncept zavedený v 5G New Radio (NR), který je zvláště relevantní pro scénáře ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a rozšířeného mobilního širokopásmového přístupu (eMBB) vyžadující vysokou propustnost. Transportní blok ([TB](/mobilnisite/slovnik/tb/)) je základní jednotka dat předávaná z vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) do fyzické vrstvy ([PHY](/mobilnisite/slovnik/phy/)) pro přenos přes rozhraní. V dřívějších systémech, jako je LTE, byl obvykle přenášen jeden TB na naplánované kodové slovo a vrstvu. NR to vylepšuje tím, že umožňuje síti naplánovat skupinu TB – TBG – v rámci jediného rozhodnutí o plánování (prostřednictvím downlink control information, [DCI](/mobilnisite/slovnik/dci/)).

Provozně, když je TBG nakonfigurována, plánovač gNodeB přidělí zdroje pro více TB současně. Tyto TB v rámci stejné TBG jsou asociovány s jediným identifikátorem procesu hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)). To znamená, že potvrzení/negativní potvrzení ([ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)) je poskytováno pro skupinu jako celek nebo svázaným způsobem v závislosti na konfiguraci, nikoli pro každý jednotlivý TB. TB ve skupině jsou přenášeny přes stejnou sadu časových a frekvenčních zdrojů (např. v rámci stejného slotu nebo mini-slotu), ale mohou být mapovány na různé prostorové vrstvy nebo používat různé modulační a kódovací schémata pro optimalizaci adaptace spojení.

Specifikace parametrů TBG, včetně maximálního počtu TB ve skupině a přidružených mechanismů HARQ zpětné vazby, je definována v procedurách fyzické vrstvy (specifikováno v 38.213). Použití TBG umožňuje efektivnější režii řídicí signalizace, protože jediné DCI může naplánovat více datových jednotek. Poskytuje také jemnější granularitu pro adaptaci spojení a alokaci zdrojů, což systému umožňuje lépe přizpůsobit přenosové parametry podmínkám kanálu a datovým požadavkům pro každý TB ve skupině, což je klíčové pro splnění přísných cílů NR v oblasti latence a spolehlivosti.

## K čemu slouží

Koncept TBG byl vyvinut pro 5G NR, aby řešil omezení plánování jednotlivých TB při plnění různorodých a náročných klíčových výkonnostních ukazatelů (KPI) nových případů užití. Pro eMBB vyžaduje stále rostoucí poptávka po špičkových datových rychlostech efektivnější způsoby zabalení dat do plánovacího intervalu. Přenos více TB v rámci jednoho přidělení snižuje relativní režii řídicí signalizace a umožňuje lepší využití velkých souvislých šířek pásma dostupných v NR.

Pro URLLC a průmyslový IoT je nízká latence prvořadá. Mechanismus TBG podporuje přenos v rámci velmi krátkých dob trvání (mini-slotů). Plánováním více malých TB jako skupiny může systém dosáhnout vysoké spolehlivosti prostřednictvím diverzity (např. různým kódováním pro každý TB), aniž by docházelo k penalizaci latence při sekvenčních přenosech jednotlivých TB a jejich přidružených smyčkách HARQ zpětné vazby. Poskytuje plánovači flexibilní nástroj pro dynamické vyvažování mezi latencí, spolehlivostí a propustností. Toto byla nezbytná evoluce oproti přístupu LTE pro podporu širšího portfolia služeb 5G definovaného v IMT-2020.

## Klíčové vlastnosti

- Umožňuje plánování více transportních bloků jedním přidělením
- TBG sdílí společný identifikátor HARQ procesu
- Snižuje režii řídicí signalizace (efektivita DCI)
- Podporuje flexibilní adaptaci spojení pro každý TB ve skupině
- Umožňuje přenos s nízkou latencí pomocí mini-slotů
- Zvyšuje spolehlivost prostřednictvím diverzity více TB v rámci jediného přenosového času

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures

---

📖 **Anglický originál a plná specifikace:** [TBG na 3GPP Explorer](https://3gpp-explorer.com/glossary/tbg/)
