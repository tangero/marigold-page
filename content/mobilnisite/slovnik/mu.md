---
slug: "mu"
url: "/mobilnisite/slovnik/mu/"
type: "slovnik"
title: "MU – Measurement Uncertainty"
date: 2025-01-01
abbr: "MU"
fullName: "Measurement Uncertainty"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mu/"
summary: "Nejistota měření (Measurement Uncertainty, MU) kvantifikuje statistické rozptýlení chyb měření v systémech 3GPP. Jedná se o klíčový parametr pro posouzení spolehlivosti rádiových měření, jako jsou RSR"
---

MU (nejistota měření) představuje statistické rozptýlení chyb měření parametrů, jako jsou RSRP a RSRQ v systémech 3GPP, a je klíčové pro posouzení spolehlivosti rádiových měření a zajištění výkonu sítě.

## Popis

Nejistota měření (Measurement Uncertainty, MU) je základním konceptem ve specifikacích 3GPP, který definuje statistický interval spolehlivosti pro jakékoli hlášené rádiové měření. Nejde o samotné měření, ale o ukazatel kvality připojený k výsledkům měření, jako je výkon přijímaného referenčního signálu (RSRP), kvalita přijímaného referenčního signálu (RSRQ) nebo šířka přenosového zpoždění. Nejistota se typicky vyjadřuje jako rozsah (např. ±X dB) s určenou úrovní spolehlivosti, což uznává, že všechna fyzikální měření podléhají inherentním chybám z faktorů, jako je tepelný šum, interference a nedokonalosti hardwaru.

Z architektonického hlediska se s MU počítá na více místech v síti. V uživatelském zařízení (UE) odhadují měřicí algoritmy modemu nejistotu na základě podmínek signálu a interní kalibrace. V rádiové přístupové síti (RAN) také základnové stanice (gNB/[eNB](/mobilnisite/slovnik/enb/)) charakterizují vlastní nejistoty měření pro uplinkové signály. Tyto hodnoty se používají interně pro rozhodovací procesy, jako je předávání spojení (handover), výběr buňky a správa paprsků. Dále jsou parametry MU často definovány v testovacích specifikacích (např. pro testování shody), aby stanovily přijatelné tolerance pro přesnost měření během certifikace zařízení.

Jeho role je klíčová pro odolnost sítě a optimalizaci výkonu. Kvantifikací nejistoty může systém činit informovanější rozhodnutí; například algoritmus pro předání spojení může zacházet s měřením s vysokou nejistotou opatrněji než s měřením s nízkou nejistotou. U pokročilých funkcí, jako je agregace nosných nebo duální konektivita, je pochopení nejistoty měření na různých komponentních nosných zásadní pro spolehlivou agregaci zdrojů. Pro síťové operátory a regulátory standardizované definice MU zajišťují konzistentní hodnocení výkonu a správu interference napříč zařízeními různých dodavatelů, čímž vytvářejí základ pro předvídatelné chování sítě.

## K čemu slouží

Účelem definice nejistoty měření (Measurement Uncertainty) ve standardech 3GPP je formálně uznat a spravovat inherentní nepřesnost veškerých měření rádiových frekvencí. Před její explicitní standardizací mohly výkonnostní požadavky a algoritmy předpokládat ideální měření, což vedlo k potenciálním výkonnostním mezerám v reálných nasazeních s nedokonalým hardwarem a náročnými rádiovými podmínkami. Kvantifikací nejistoty standardy vytvářejí společný rámec pro posouzení skutečné spolehlivosti dat používaných pro kritické síťové funkce.

Historicky, jak se buněčné systémy vyvíjely z 2G na 3G a poté na LTE a 5G, se složitost správy rádiových zdrojů dramaticky zvýšila. Techniky jako [MIMO](/mobilnisite/slovnik/mimo/), agregace nosných a komunikace v milimetrových vlnách spoléhají na přesná měření. Bez standardizovaného konceptu nejistoty by nebylo možné stanovit realistické výkonnostní požadavky pro UE a základnové stanice ani zajistit interoperabilitu mezi implementacemi různých dodavatelů. MU řeší omezení předpokladu dokonalých měření zavedením statistické hranice chyby, což umožňuje návrhářům systémů vytvářet algoritmy odolné vůči měřicímu šumu a variabilitě.

Navíc je MU klíčová pro testování shody a typové schvalování. Testovací specifikace odkazují na MU pro definování kritérií vyhovění/nevyhovění pro rádiový výkon UE. To zajišťuje, že zařízení vstupující na trh fungují v přijatelných chybových mezích, čímž garantují základní úroveň výkonu sítě a uživatelského zážitku. Také podporuje pokročilé nástroje pro automatizaci a optimalizaci sítě, které mohou využívat informace o nejistotě k lepšímu modelování stavu sítě a předpovídání výkonu.

## Klíčové vlastnosti

- Kvantifikuje statistické hranice chyb pro rádiová měření (např. výkon, kvalita, časování).
- Aplikuje se na měření jak na straně UE (downlink), tak na straně sítě (uplink).
- Vyjadřuje se jako rozsah (např. ± hodnota) s přidruženou úrovní spolehlivosti.
- Nedílná součást algoritmů správy rádiových zdrojů, jako je předávání spojení (handover) a výběr buňky.
- Definována v testovacích specifikacích pro testování shody a výkonu.
- Podporuje pokročilé funkce, jako je agregace nosných, tím, že kvalifikuje spolehlivost měření na jednotlivých nosných.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.862** (Rel-14) — Critical Communications Feasibility Study
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.771** (Rel-19) — FR2-1 OTA Testing for STxMP UEs
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TR 38.838** (Rel-17) — Study on XR Evaluations for NR
- **TR 38.871** (Rel-18) — Technical Report
- **TR 38.884** (Rel-18) — Technical Report
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [MU na 3GPP Explorer](https://3gpp-explorer.com/glossary/mu/)
