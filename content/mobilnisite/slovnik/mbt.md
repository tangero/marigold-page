---
slug: "mbt"
url: "/mobilnisite/slovnik/mbt/"
type: "slovnik"
title: "MBT – Multi-Band Testing"
date: 2025-01-01
abbr: "MBT"
fullName: "Multi-Band Testing"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mbt/"
summary: "Metodika testování shody pro bezdrátová zařízení pracující v mnoha kmitočtových pásmech. Zajišťuje, že zařízení splňují požadavky na výkon ve všech podporovaných pásmech, což je klíčové pro globální i"
---

MBT je metodika testování shody, která zajišťuje, že bezdrátová zařízení splňují požadavky na výkon ve všech podporovaných kmitočtových pásmech pro globální interoperabilitu a spolehlivý provoz sítě.

## Popis

Multi-Band Testing (MBT) je komplexní testovací rámec definovaný 3GPP pro ověření výkonu a shody uživatelských zařízení (UE) a základnových stanic v mnoha kmitočtových pásmech. Zahrnuje řadu testovacích případů a měřicích postupů specifikovaných v technických specifikacích, jako jsou 37.141 (testování shody základnových stanic) a 37.145 (testování shody UE). Metodika vyhodnocuje klíčové parametry vysokofrekvenční ([RF](/mobilnisite/slovnik/rf/)) části včetně výstupního výkonu vysílače, citlivosti přijímače, nežádoucích emisí a intermodulačních charakteristik v každém podporovaném pásmu. Testování se provádí za různých provozních podmínek simulujících reálné scénáře, aby bylo zajištěno, že zařízení si udržují výkon při různých kombinacích pásem a síťových prostředích.

Architektura MBT zahrnuje specializované testovací vybavení, jako jsou generátory signálů, spektrální analyzátory a emulátory kanálů, nakonfigurované tak, aby replikovaly vícepásmové rádiové podmínky. Testovací konfigurace definují specifická nastavení pásem, šířky kanálů a modulační schémata pro posouzení chování zařízení. U základnových stanic testy pokrývají aspekty jako vedený a vyzařovaný výkon, zatímco u UE zahrnují měření celkového vyzařovaného výkonu ([TRP](/mobilnisite/slovnik/trp/)) a celkové izotropní citlivosti (TIS). Postupy zohledňují scénáře agregace nosných, kdy jsou agregovány vícečetné komponentní nosné z různých pásem za účelem zvýšení datového propustnosti, což vyžaduje ověření souběžného vícepásmového provozu.

MBT funguje tak, že provádí strukturovaný testovací plán, který izoluje každé pásmo a kombinaci pásem. Testovací případy jsou navrženy tak, aby zatěžovaly vysokofrekvenční část zařízení včetně výkonových zesilovačů, filtrů a antén, a identifikovaly tak degradaci výkonu nebo nesplnění požadavků. Naměřené hodnoty se porovnávají s limity definovanými 3GPP pro parametry, jako je velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)), poměr úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)) a charakteristiky blokování. Testování také pokrývá regulatorní požadavky a zajišťuje, že zařízení splňují regionální předpisy pro využití spektra a nezpůsobují škodlivé rušení jiným systémům. Ověřením vícepásmového výkonu MBT zajišťuje, že zařízení mohou bezproblémově fungovat v heterogenních sítích s různorodým využitím kmitočtů.

## K čemu slouží

MBT bylo zavedeno pro řešení rostoucí složitosti bezdrátových zařízení podporujících více kmitočtových pásem pro globální roaming a vylepšenou mobilní širokopásmovou službu. Před jeho standardizací bylo testování často specifické pro jednotlivá pásma, což vedlo k mezerám v ověřování interakcí mezi pásmy a výkonu při agregaci nosných. Jelikož se sítě LTE a později 5G nasazují v širokém rozsahu kmitočtů (např. nízká, střední a vysoká pásma), bylo nutné, aby zařízení spolehlivě fungovala ve všech podporovaných pásmech bez kompromisů ve výkonu. MBT poskytuje jednotnou testovací metodiku pro zajištění konzistentní kvality zařízení a interoperability mezi různými síťovými operátory a regiony.

Hlavním problémem, který řeší, je riziko degradace výkonu při přepínání zařízení mezi pásmy nebo při současném používání více pásem. Bez komplexního vícepásmového testování by problémy jako desenzibilizace přijímače, harmonické vysílače a intermodulační zkreslení mohly zůstat neodhaleny, což by vedlo k přerušeným hovorům, sníženým datovým rychlostem nebo rušení jiných služeb. MBT zajišťuje, že zařízení splňují přísná kritéria [RF](/mobilnisite/slovnik/rf/) výkonu ve všech provozních scénářích, což je klíčové pro udržení efektivity sítě a uživatelského zážitku.

MBT navíc podporuje vývoj mobilních technologií tím, že umožňuje začlenění nových kombinací pásem zaváděných v každé verzi 3GPP. Výrobcům umožňuje ověřovat zařízení pro nové funkce, jako je [EN-DC](/mobilnisite/slovnik/en-dc/) (E-UTRA-NR duální konektivita) a agregace NR nosných napříč kmitočtovými rozsahy. Poskytnutím standardizovaného testovacího rámce MBT snižuje dobu uvedení nových zařízení na trh a usnadňuje globální certifikační procesy, čímž zajišťuje, že spotřebitelé dostávají spolehlivé produkty schopné plně využívat síťové možnosti.

## Klíčové vlastnosti

- Komplexní testování RF shody ve všech podporovaných kmitočtových pásmech
- Ověření výkonu vysílače a přijímače při vícepásmovém provozu
- Podpora testovacích scénářů pro agregaci nosných a duální konektivitu
- Měření klíčových parametrů, jako je výstupní výkon, citlivost a nežádoucí emise
- Vyhodnocení mezipásmového rušení a intermodulačních charakteristik
- Soulad s regulatorními požadavky a regionálními předpisy pro využití spektra

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [MBT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbt/)
