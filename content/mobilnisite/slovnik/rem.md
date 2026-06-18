---
slug: "rem"
url: "/mobilnisite/slovnik/rem/"
type: "slovnik"
title: "REM – Radio Environment Measurement"
date: 2025-01-01
abbr: "REM"
fullName: "Radio Environment Measurement"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rem/"
summary: "Radio Environment Measurement (REM) označuje sběr a analýzu rádiových frekvenčních dat, jako je síla signálu, úroveň rušení a kvalita kanálu, v rámci mobilní sítě. Používá se pro plánování sítě, optim"
---

REM (Radio Environment Measurement) je sběr a analýza rádiových frekvenčních dat, jako je síla signálu a rušení, v rámci mobilní sítě pro plánování, optimalizaci a funkce samoorganizace sítě za účelem zlepšení pokrytí a výkonu.

## Popis

Radio Environment Measurement (REM) je komplexní proces v sítích 3GPP zahrnující získávání, ukládání a zpracování měření rádiových frekvencí ([RF](/mobilnisite/slovnik/rf/)) z různých zdrojů, včetně uživatelských zařízení (UE), základnových stanic (eNodeB v LTE, gNB v NR) a dedikovaných měřicích jednotek. Tato měření zahrnují klíčové parametry, jako je Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/)), Reference Signal Received Quality ([RSRQ](/mobilnisite/slovnik/rsrq/)), Signal-to-Interference-plus-Noise Ratio ([SINR](/mobilnisite/slovnik/sinr/)) a úrovně rušení v různých frekvenčních pásmech. Shromážděná data vytvářejí mapu rádiového prostředí, která poskytuje prostorový a časový pohled na stav sítě, což je klíčové pro správu a optimalizaci sítě.

Proces REM typicky zahrnuje několik kroků: sběr měření, kdy UE a základnové stanice hlásí RF data periodicky nebo na vyžádání; agregaci dat, kdy se měření z více zdrojů kombinují do koherentní datové sady; a analýzu, kdy algoritmy zpracovávají data k identifikaci problémů, jako jsou díry v pokrytí, ohniska rušení nebo kapacitní omezení. V LTE a NR je REM integrována s funkcemi samoorganizující se sítě ([SON](/mobilnisite/slovnik/son/)), jako je Coverage and Capacity Optimization ([CCO](/mobilnisite/slovnik/cco/)) a Mobility Robustness Optimization ([MRO](/mobilnisite/slovnik/mro/)), což umožňuje automatizované úpravy náklonu antén, nastavení výkonu a parametrů předávání hovoru. Tím se snižuje potřeba manuálního zásahu a zlepšuje se výkon sítě.

Data REM jsou uložena v centralizovaných nebo distribuovaných databázích, často v rámci Operation and Support System ([OSS](/mobilnisite/slovnik/oss/)) nebo Network Management System (NMS). Pokročilé systémy REM mohou využívat techniky strojového učení k predikci chování sítě a doporučování optimalizačních akcí. Díky využití REM mohou operátoři efektivněji provádět úkoly, jako je frekvenční plánování, správa seznamu sousedních buněk a koordinace rušení. V sítích 5G REM také podporuje dynamické sdílení spektra a síťové segmenty (network slicing) tím, že poskytuje přehled o využití rádiových zdrojů v reálném čase, což zajišťuje efektivní provoz v komplexních prostředích.

## K čemu slouží

Radio Environment Measurement (REM) bylo zavedeno, aby řešilo rostoucí složitost mobilních sítí, zejména s nasazením LTE ve verzi 8 (Release 8), které vyžadovalo sofistikovanější nástroje pro plánování a optimalizaci sítě. Před zavedením REM se operátoři sítí spoléhali převážně na manuální testy z vozidel a statické plánovací nástroje, které byly časově náročné, nákladné a nedokázaly zachytit dynamické rádiové podmínky v reálném čase. REM automatizuje sběr RF dat ze síťových prvků a poskytuje kontinuální a přesný pohled na rádiové prostředí pro podporu rozhodování založeného na datech.

REM řeší problém neefektivní správy sítě tím, že umožňuje proaktivní optimalizaci a samoozdravné schopnosti prostřednictvím SON. Umožňuje operátorům detekovat a řešit problémy, jako je špatné pokrytí, rušení a přetížení, rychleji než tradiční metody, čímž zlepšuje uživatelský zážitek a snižuje provozní náklady. To je obzvláště důležité v hustých městských nasazeních a heterogenních sítích, kde se rádiové podmínky rychle mění vlivem faktorů, jako je uspořádání budov a pohyb uživatelů.

Vývoj REM v sítích 5G dále řeší výzvy spojené s massive MIMO, beamformingem a síťovými segmenty (network slicing), kde je přesná znalost rádiového prostředí klíčová pro přidělování zdrojů a zajištění kvality služeb. Integrací REM s pokročilou analytikou mohou operátoři optimalizovat výkon sítě v reálném čase, čímž podporují vysoké přenosové rychlosti, nízkou latenci a požadavky na spolehlivost moderních aplikací.

## Klíčové vlastnosti

- Sběr RF měření (např. RSRP, RSRQ, SINR) z UE a základnových stanic
- Vytváření map rádiového prostředí pro prostorovou a časovou analýzu
- Integrace s funkcemi SON pro automatizovanou optimalizaci sítě
- Podpora optimalizace pokrytí a kapacity, správy rušení a robustnosti mobility
- Umožňuje plánování sítě a přidělování zdrojů založené na datech
- Umožňuje sledování v reálném čase a prediktivní analýzu pro proaktivní správu

## Související pojmy

- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [RSRQ – Reference Signal Receiving Quality](/mobilnisite/slovnik/rsrq/)
- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)

## Definující specifikace

- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report

---

📖 **Anglický originál a plná specifikace:** [REM na 3GPP Explorer](https://3gpp-explorer.com/glossary/rem/)
