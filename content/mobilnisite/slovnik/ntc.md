---
slug: "ntc"
url: "/mobilnisite/slovnik/ntc/"
type: "slovnik"
title: "NTC – Non-contiguous Test Configuration"
date: 2025-01-01
abbr: "NTC"
fullName: "Non-contiguous Test Configuration"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ntc/"
summary: "Standardizovaná testovací konfigurace pro hodnocení rádiového výkonu při práci s nesouvislým spektrem. Definuje konkrétní scénáře agregace nosných, ve kterých jsou komponentní nosné odděleny mezerami,"
---

NTC je standardizovaná testovací konfigurace pro hodnocení rádiového výkonu při práci s nesouvislým spektrem. Definuje scénáře agregace nosných s mezerami mezi komponentními nosnými za účelem zajištění konzistentního testování.

## Popis

Testovací konfigurace pro nesouvislé spektrum (NTC) je klíčový rámec definovaný ve specifikacích 3GPP pro testování shody a výkonu uživatelského zařízení (UE) a síťové infrastruktury. Konkrétně řeší složitosti zaváděné agregací nosných ([CA](/mobilnisite/slovnik/ca/)), když agregované komponentní nosné ([CC](/mobilnisite/slovnik/cc/)) nejsou ve frekvenční doméně sousední, což znamená, že mezi nimi existují spektrální mezery. Tento nesouvislý provoz je běžný v reálných nasazeních kvůli fragmentovaným přidělením spektra, která mají operátoři k dispozici. NTC poskytuje standardizovanou sadu parametrů a scénářů, které musí výrobci testovacích zařízení a certifikační orgány používat k ověření, že zařízení nebo základnová stanice dokáže správně zvládnout výzvy v oblasti rádiových frekvencí ([RF](/mobilnisite/slovnik/rf/)), jako je správa samostatných lokálních oscilátorů, výkonových zesilovačů a filtrů pro odlišné frekvenční bloky, a udržování synchronizace a agregace dat napříč nimi.

Z architektonického hlediska je scénář NTC definován specifikací přesných kmitočtových pásem pro primární buňku (PCell) a jednu nebo více sekundárních buněk (SCell) spolu s velikostí mezery mezi nimi. Klíčovými součástmi testu jsou RF požadavky pro každou CC, jako je výstupní výkon, limity nežádoucích emisí a citlivost přijímače, které musí být splněny současně. Konfigurace také určuje šířku pásma každé CC (např. 10 MHz, 20 MHz) a konkrétní kombinaci pásem CA, která je testována (např. Pásmo 1 + Pásmo 3). Testovací postupy, podrobně popsané ve specifikacích jako 38.521 (shoda UE) a 38.113 (základnová stanice), měří metriky výkonu, jako je propustnost, velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)) a poměr úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)), za těchto nesouvislých podmínek.

Její role v síťovém ekosystému je zásadní pro zajištění interoperability a výkonu. Díky povinnému společnému testovacímu základu NTC zaručuje, že UE od různých výrobců budou spolehlivě fungovat na jakékoli síti využívající nesouvislou CA, což je klíčová technika pro dosažení vysokých přenosových rychlostí. Ověřuje schopnost UE provádět plánování, hybridní automatické opakování požadavku ([HARQ](/mobilnisite/slovnik/harq/)) a podávání zpráv o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) napříč nespojitými frekvenčními zdroji. Bez takových standardizovaných testovacích konfigurací by mohl být výkon při nesouvislém provozu nekonzistentní, což by vedlo k potenciálnímu zhoršení služeb, přerušeným spojením nebo neschopnosti plně využít dostupné spektrální zdroje operátora, a tím by se v konečném důsledku omezil uživatelský zážitek a účinnost sítě.

## K čemu slouží

NTC bylo vytvořeno za účelem vyřešení kritického problému zajištění spolehlivého a vysoce výkonného provozu ve scénářích agregace nosných, kdy je dostupné spektrum operátora fragmentované. Historicky časná nasazení LTE často využívala souvislé bloky spektra, což zjednodušovalo [RF](/mobilnisite/slovnik/rf/) návrh a testování. Jak se však spektrum stalo vzácným zdrojem, operátoři často získávali nespojité frekvenční bloky v různých pásmech (např. prostřednictvím aukcí nebo přerozdělení). Zatímco technologie CA teoreticky umožňovala agregaci těchto bloků, praktická RF implementace – správa samostatných výkonových zesilovačů, zvládání intermodulačního zkreslení a splnění přísných emisních masek pro nesousední kanály – přinesla nové složitosti, které stávající testy pro souvislou CA nepokrývaly.

Primární motivací bylo vytvořit jednotnou a důslednou testovací metodologii, která odráží výzvy reálného nasazení. Před standardizací NTC mohli výrobci testovat nesouvislou CA pomocí proprietárních nebo nekonzistentních metod, což ztěžovalo porovnání výkonu zařízení nebo zaručení celosíťové interoperability. Tento nedostatek standardizace riskoval suboptimální uživatelský zážitek, jako jsou nižší než očekávané přenosové rychlosti nebo zvýšený počet spadlých hovorů, když UE agregovalo nesouvislé nosné. Zavedením NTC ve verzi 10 spolu s vylepšenými funkcemi CA poskytla 3GPP jasný etalon, což průmyslu umožnilo s důvěrou nasazovat pokročilé funkce CA, maximalizovat spektrální účinnost a naplnit slibované přenosové rychlosti v řádu gigabitů za sekundu u 4G a 5G, bez ohledu na fragmentaci spektra.

## Klíčové vlastnosti

- Standardizuje testování agregace nosných s frekvenčními mezerami mezi komponentními nosnými
- Definuje konkrétní kombinace pásem, šířky pásma a velikosti mezer pro reprodukovatelné testy
- Pokrývá požadavky na RF výkon vysílače i přijímače při nesouvislém provozu
- Zajišťuje konzistentní hodnocení schopností UE, jako je simultánní vysílání a příjem na nespojitých frekvencích
- Ověřuje výkon plánování, HARQ a podávání zpráv CSI napříč nesouvislými zdroji
- Podporuje testování shody a interoperability pro základnové stanice a uživatelská zařízení

## Definující specifikace

- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.175** (Rel-19) — EMC for NR IAB Nodes
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [NTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ntc/)
