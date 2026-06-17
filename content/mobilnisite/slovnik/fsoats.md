---
slug: "fsoats"
url: "/mobilnisite/slovnik/fsoats/"
type: "slovnik"
title: "FSOATS – Free Space Over-the-Air Test System"
date: 2025-01-01
abbr: "FSOATS"
fullName: "Free Space Over-the-Air Test System"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fsoats/"
summary: "FSOATS je testovací metodika pro hodnocení vysokofrekvenčního (RF) výkonu zařízení 5G NR ve volném prostoru, která eliminuje vliv kabelů a konektorů. Zajišťuje přesné měření vyzařovaného výkonu, citli"
---

FSOATS je testovací metodika pro hodnocení vysokofrekvenčního (RF) výkonu zařízení 5G NR ve volném prostoru, která zajišťuje přesné měření vyzařovaného výkonu, citlivosti přijímače a charakteristik antény.

## Popis

Free Space Over-the-Air Test System (FSOATS) je standardizované testovací prostředí definované 3GPP pro provádění bezdrátových ([OTA](/mobilnisite/slovnik/ota/)) měření na uživatelských zařízeních (UE) a základnových stanicích (gNB) 5G New Radio (NR). Na rozdíl od vedeného (conducted) testování, které využívá fyzických kabelových spojení, umisťuje FSOATS testované zařízení ([DUT](/mobilnisite/slovnik/dut/)) do bezodrazové komory nebo podobného řízeného prostředí volného prostoru. Toto uspořádání umožňuje vyhodnocení kompletního vysokofrekvenčního předního konce, včetně antén, způsobem, který replikuje reálné podmínky elektromagnetického šíření bez zkreslení zavedených kabeláží. Systém měří klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je celkový vyzařovaný výkon (TRP), celková izotropní citlivost (TIS) a charakteristiky formování svazku, které jsou zásadní pro posouzení skutečných vysílacích a přijímacích schopností zařízení.

Z architektonického hlediska se FSOATS skládá z několika klíčových komponent: bezodrazové komory, která minimalizuje odrazy a vnější rušení; polohovacího systému (např. otočného stolu) pro otáčení DUT za účelem prostorových měření; referenční měřicí antény připojené k vektorovému analyzátoru signálu nebo generátoru signálu; a kalibračního vybavení pro zajištění přesnosti měření. Testovací sestava je pečlivě kalibrována pomocí referenčních antén se známými vyzařovacími charakteristikami pro stanovení výchozího bodu. Měření se provádějí napříč specifikovanými kmitočtovými pásmy a prostorovými úhly, zachycující trojrozměrný vyzařovací diagram DUT. Tato komplexní prostorová analýza je obzvláště klíčová pro 5G zařízení využívající pokročilé anténní systémy ([AAS](/mobilnisite/slovnik/aas/)) a formování svazku, kde je výkon vysoce směrový.

Při provozu zahrnuje testování FSOATS vysílání známých testovacích signálů z DUT a měření vyzařovaného výkonu na různých místech v komoře, nebo naopak vysílání signálů na DUT pro měření jeho přijímací citlivosti. Naměřená data se zpracují pro výpočet metrik jako TRP (integrál vyzařovaného výkonu přes kouli) a TIS (průměrná citlivost ve všech směrech). Tyto metriky poskytují komplexní pohled na RF výkon zařízení, čímž zajišťují, že splňuje jak technické specifikace 3GPP, tak regulatorní požadavky (např. od orgánů jako [FCC](/mobilnisite/slovnik/fcc/) nebo [ETSI](/mobilnisite/slovnik/etsi/)). Ověřováním účinnosti antény a přesnosti směrování svazku pomáhá FSOATS zaručit, že 5G zařízení budou spolehlivě fungovat v různých scénářích nasazení, od hustých městských prostředí až po rozsáhlé pokrytí.

Role FSOATS v 5G ekosystému je zásadní pro certifikaci zařízení a interoperabilitu. Překlenuje propast mezi simulovaným výkonem a reálným provozem, což výrobcům umožňuje optimalizovat návrhy antén a RF komponent. Jelikož 5G sítě využívají vyšší kmitočtová pásma (včetně mmWave), kde je šíření signálu náchylnější na překážky a útlum na trase, přesné OTA testování se stává ještě kritičtějším. FSOATS zajišťuje, že zařízení mohou udržet robustní konektivitu a poskytovat slibované přenosové rychlosti a nízkou latenci, čímž podporuje celkovou kvalitu služeb (QoS) a uživatelský zážitek v 5G sítích.

## K čemu slouží

FSOATS byl zaveden, aby řešil omezení tradičních metod vedeného (conducted) testování, které se staly nedostatečnými pro hodnocení moderních 5G zařízení s integrovanými, složitými anténními systémy. U dřívějších generací mobilních sítí se RF testování často spoléhalo na přímá kabelová připojení k anténnímu portu zařízení, čímž se obcházely samotné antény. Tento přístup byl dostačující, když byly antény jednodušší a výkon byl méně směrový. S příchodem 5G však zařízení začleňují vícevstupové/vícevýstupní ([MIMO](/mobilnisite/slovnik/mimo/)) pole a technologie formování svazku, kde je anténa nedílnou, neodstranitelnou součástí RF řetězce. Vedené testování nedokáže zachytit vliv účinnosti antény, vyzařovacích diagramů nebo zisků z formování svazku, což vede k výraznému nesouladu mezi laboratorními měřeními a reálným výkonem.

Motivace pro FSOATS vychází z potřeby zajistit, aby 5G zařízení splňovala přísné výkonnostní standardy v reálných podmínkách použití. Regulační orgány vyžadují dodržování specifických limitů vyzařovaného výkonu, aby zabránily rušení a zajistily bezpečnost, zatímco operátoři požadují spolehlivou konektivitu. Historický kontext ukazuje, že s rostoucími kmitočty (např. se zavedením mmWave v 5G) se vliv návrhu antény na celkový výkon systému stal výraznějším. Předchozí přístupy postrádaly standardizovanou metodologii pro [OTA](/mobilnisite/slovnik/ota/) testování, což vedlo k nekonzistentním výsledkům mezi různými testovacími laboratořemi a dodavateli vybavení. FSOATS poskytuje jednotný, opakovatelný rámec, který umožňuje spravedlivé srovnání a certifikaci zařízení.

Řešením těchto problémů FSOATS usnadňuje komercializaci pokročilých 5G zařízení. Umožňuje výrobcům ověřit, že jejich produkty budou v terénu fungovat podle očekávání, čímž podporuje klíčové případy užití 5G, jako je rozšířené mobilní širokopásmové připojení (eMBB), masivní IoT a ultra-spolehlivá komunikace s nízkou latencí (URLLC). Bez takového testovacího systému by existovalo vyšší riziko podprůměrného výkonu zařízení, což by vedlo ke špatným uživatelským zkušenostem a potenciálním problémům se sítí. FSOATS je tedy nezbytný pro důvěru ekosystému ve schopnosti zařízení a pro urychlení nasazení inovativních 5G technologií.

## Klíčové vlastnosti

- Standardizovaná metodologie bezdrátového (OTA) měření ve volném prostoru pro 5G NR
- Hodnocení celkového vyzařovaného výkonu (TRP) a celkové izotropní citlivosti (TIS)
- Podpora testování formování svazku a pokročilých anténních systémů (AAS)
- Řízené prostředí bezodrazové komory pro minimalizaci odrazů
- Možnost prostorového měření napříč 3D úhly
- Kalibrace pomocí referenčních antén pro zajištění přesnosti

## Definující specifikace

- **TS 38.113** (Rel-19) — NR Base Station EMC Specification

---

📖 **Anglický originál a plná specifikace:** [FSOATS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fsoats/)
