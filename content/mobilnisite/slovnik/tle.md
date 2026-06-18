---
slug: "tle"
url: "/mobilnisite/slovnik/tle/"
type: "slovnik"
title: "TLE – Two Line Elements"
date: 2026-01-01
abbr: "TLE"
fullName: "Two Line Elements"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tle/"
summary: "Standardizovaný datový formát pro popis oběžné dráhy satelitu, například platformy Neterestriální sítě (NTN). Poskytuje kompaktní soubor parametrů (Keplerovy elementy), který umožňuje pozemní stanici"
---

TLE je standardizovaný datový formát popisující oběžnou dráhu satelitu pomocí kompaktních parametrů, který umožňuje pozemním stanicím a UE předpovídat jeho polohu a rychlost pro zachycení NTN buňky, předání spojení (handover) a časové sladění.

## Popis

Two Line Elements (TLE) je datový formát původně vyvinutý organizací NORAD a přijatý 3GPP pro provoz Neterestriálních sítí ([NTN](/mobilnisite/slovnik/ntn/)). Sada TLE se skládá ze dvou řádků textu obsahujících soubor parametrů oběžné dráhy, známých jako Keplerovy elementy, pro konkrétní satelit nebo kosmický objekt v dané epoše (referenční čas). Tyto parametry zahrnují inklinaci satelitu, rektascenzi vzestupného uzlu, excentricitu, argument perigea, střední anomálii a střední pohyb. Formát také obsahuje identifikační a klasifikační údaje. V kontextu 3GPP může síť vysílat TLE informace pro relevantní NTN platformy (např. satelity na nízké oběžné dráze) prostřednictvím bloků systémových informací ([SIB](/mobilnisite/slovnik/sib/)). Uživatelské zařízení (UE) a síťové uzly mohou tyto informace spolu se standardními modely pro výpočet dráhy, jako je SGP4 (Simplified General Perturbations 4), použít k výpočtu aktuální a budoucí efemeridy satelitu (polohy a rychlosti). Tato vypočtená efemerida je zásadní pro několik procedur specifických pro NTN. Například umožňuje UE určit správný časový předstih (timing advance) pro vysílání v uplinku, aby kompenzovala velké a proměnlivé zpoždění šíření. Také pomáhá předpovídat oblasti pokrytí buňky pro její (resp. paprsku) převýběr a předání spojení, protože pohyb satelitu způsobuje, že jeho servisní oblast se rychle pohybuje po zemském povrchu. Data TLE musí být sítí pravidelně aktualizována, protože oběžná dráha satelitu je ovlivňována faktory jako atmosférický odpor a gravitační anomálie. Integrace TLE do specifikací 3GPP poskytuje odlehčenou, standardizovanou metodu pro distribuci efemerid bez nutnosti neustálého přenosu surových polohových dat s vysokou šířkou pásma.

## K čemu slouží

Účelem integrace formátu TLE do standardů 3GPP je umožnit efektivní a předvídatelnou komunikaci s mobilními platformami v Neterestriálních sítích ([NTN](/mobilnisite/slovnik/ntn/)). Tradiční terestriální sítě spoléhají na pevné umístění základnových stanic, ale NTN zavádí pohyblivé síťové uzly (satelity) s vysokými rychlostmi a velkým, časově proměnným zpožděním šíření. Přímý, nepřetržitý přenos přesných souřadnic typu [GPS](/mobilnisite/slovnik/gps/) pro každý satelit by spotřebovával značné zdroje vysílacího kanálu. Formát TLE tento problém řeší tím, že poskytuje kompaktní parametrický popis oběžné dráhy. Z tohoto malého datového souboru (typicky méně než 200 znaků) může jakýkoli přijímač nezávisle generovat přesné předpovědi efemerid pro významné časové okno (často několik dní) pomocí veřejně dostupných algoritmů. Tím se řeší klíčová výzva, jak umožnit UE a síťovým prvkům autonomně vypočítat základní parametry, jako je zpoždění šíření a viditelnost satelitu, které jsou předpokladem pro synchronizaci, náhodný přístup a správu mobility v dynamickém prostředí NTN. Jeho přijetí využívá dlouhodobě zavedený, ověřený a výpočetně efektivní standard z oblasti kosmonautiky, čímž se vyhýbá nutnosti vytvářet nový, složitý protokol pro distribuci efemerid pro 5G a další generace.

## Klíčové vlastnosti

- Kompaktní parametrizace oběžné dráhy pomocí Keplerových elementů
- Umožňuje autonomní předpověď efemerid pomocí modelů jako SGP4
- Vysílání prostřednictvím 3GPP systémových informací pro zachycení NTN buňky
- Podporuje výpočet časově proměnlivého zpoždění šíření pro časový předstih (timing advance)
- Usnadňuje předpověď viditelnosti satelitu a pokrytí buňky pro mobilitu
- Standardizovaný formát umožňuje využití stávajících, ověřených knihoven z oblasti kosmonautiky

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks

---

📖 **Anglický originál a plná specifikace:** [TLE na 3GPP Explorer](https://3gpp-explorer.com/glossary/tle/)
