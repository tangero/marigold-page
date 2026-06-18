---
slug: "dml"
url: "/mobilnisite/slovnik/dml/"
type: "slovnik"
title: "DML – Data Mode Landscape"
date: 2025-01-01
abbr: "DML"
fullName: "Data Mode Landscape"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/dml/"
summary: "Rámec a definovaná sada metrik pro hodnocení výkonu a charakteristik různých režimů přenosu dat v rádiové přístupové síti. Poskytuje strukturovanou metodologii pro analýzu kompromisů mezi propustností"
---

DML je rámec a soubor metrik pro hodnocení výkonu a charakteristik různých režimů přenosu dat v rádiové přístupové síti.

## Popis

Data Mode Landscape (DML) je rámec pro hodnocení a analýzu výkonu specifikovaný v pracovních skupinách pro rádiový přístup (RAN) 3GPP, zejména v kontextu NR a LTE-Advanced Pro. Nejde o jediný protokol nebo rozhraní, ale o komplexní metodologii a sadu definovaných „krajin“ (landscapes), které mapují výkonnostní hranice a charakteristiky různých režimů přenosu dat. Režim přenosu dat (data mode) označuje specifickou kombinaci konfigurací fyzické vrstvy a vyšších vrstev, jako jsou schémata modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)), numerologie (rozestup podnosných, délka symbolu), konfigurace části šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)), vrstvy [MIMO](/mobilnisite/slovnik/mimo/) a parametry plánování. Rámec DML systematicky hodnotí, jak si tyto režimy vedou v klíčových ukazatelích výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je propustnost na uživatele, propustnost buňky, latence, míra chybovosti paketů a spektrální účinnost.

Z architektonického hlediska je DML realizován prostřednictvím detailních simulačních metodologií, testovacích předpokladů a modelů kanálů definovaných ve specifikacích 3GPP. Zahrnuje vytvoření vícerozměrného parametrického prostoru zahrnujícího scénáře nasazení (např. urban macro, indoor hotspot), podmínky kanálu (např. modely úniků, rozprostření zpoždění) a modely provozu (např. full buffer, bursty). V tomto prostoru jsou konkrétní režimy dat simulovány nebo analyticky vyhodnocovány. Výstupem je „krajina“ – výkonnostní mapa, která ukazuje například dosažitelnou propustnost jako funkci poměru signálu k šumu a interferenci ([SINR](/mobilnisite/slovnik/sinr/)) pro různé úrovně MCS a šířky kanálů. Tyto krajiny se používají k odvození výkonnostních požadavků, k vedení rozhodnutí při standardizaci a k pomoci při plánování a optimalizaci sítě.

Klíčové součásti DML zahrnují definované simulační scénáře (např. definované v 3GPP TR 38.151 a TR 37.544), přesné modely kanálů (jako [TDL](/mobilnisite/slovnik/tdl/) a [CDL](/mobilnisite/slovnik/cdl/)), modely provozu a konkrétní KPI, které mají být shromážděny. Rámec podrobně popisuje, jak nakonfigurovat systémový simulátor, včetně chování gNB a UE, podmínek šíření a metodiky měření. Role DML v síťovém ekosystému je primárně během fází návrhu, standardizace a benchmarkingu. Poskytuje společný, dohodnutý základ pro porovnání výkonu různých technických návrhů a zajišťuje, že nové funkce (jako nová tabulka MCS nebo plánovací algoritmus) jsou hodnoceny za konzistentních a realistických podmínek. Pro síťové operátory a výrobce zařízení výsledky odvozené z DML informují o předpovědích schopností, návrhu algoritmů správy rádiových zdrojů a očekávaném výkonu při různém zatížení a konfiguracích sítě.

## K čemu slouží

Účelem Data Mode Landscape je poskytnout objektivní, kvantitativní základ pro hodnocení a porovnávání výkonu v rámci standardizace 3GPP. Jak se bezdrátové systémy jako LTE a NR vyvíjely, počet konfigurovatelných parametrů a přenosových režimů explodoval, což vytvořilo obrovský prostor pro návrh. Bez standardizovaného hodnotícího rámce by bylo obtížné spravedlivě porovnávat různá technická řešení nebo stanovovat realistické výkonnostní požadavky na nové funkce. DML byl vytvořen k vyřešení tohoto problému definováním řízené a opakovatelné metodologie.

Historicky mohla být porovnání výkonu v dřívějších vydáních roztříštěná, přičemž různé společnosti používaly proprietární simulační předpoklady, což vedlo k neshodám a prodlouženým standardizačním debatám. Rámec DML, zavedený v pozdějších studiích LTE-Advanced a NR, vytvořil společný „herní prostor“. Řeší omezení ad-hoc hodnocení podrobnou specifikací simulačních podmínek, modelů kanálů a metrik výkonu. To zajišťuje, že když je navržen nový režim přenosu dat – například schéma modulace vyššího řádu pro extrémní podmínky [SINR](/mobilnisite/slovnik/sinr/) – lze jeho přínosy a kompromisy konzistentně posoudit ve srovnání s existujícími režimy.

Dále DML podporuje vývoj realistických výkonnostních požadavků na rádiové základnové stanice a uživatelská zařízení. Porozuměním výkonnostní krajině může 3GPP definovat minimální požadavky, které jsou náročné, ale dosažitelné. Také napomáhá při plánování sítě tím, že poskytuje vhled do očekávaných výkonnostních hranic v různých prostředích. V konečném důsledku je DML nástrojem pro inženýrskou důslednost, který umožňuje bezdrátovému průmyslu činit informovaná rozhodnutí vyvažující složitost, náklady a výkon, když systémy 5G a další generace cílí na stále rozmanitější a náročnější případy užití.

## Klíčové vlastnosti

- Standardizovaná simulační metodologie a předpoklady pro konzistentní hodnocení výkonu
- Vícerozměrná analýza mapující výkonnostní KPI vůči systémovým parametrům a podmínkám kanálu
- Definuje konkrétní scénáře nasazení, modely kanálů (např. TDL, CDL) a modely provozu
- Používá se k odvození minimálních výkonnostních požadavků pro základnové stanice a uživatelská zařízení
- Podporuje porovnání různých režimů přenosu dat (MCS, numerologie, konfigurace MIMO)
- Poskytuje vstup pro návrh algoritmů správy rádiových zdrojů a optimalizaci sítě

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)
- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)

## Definující specifikace

- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology

---

📖 **Anglický originál a plná specifikace:** [DML na 3GPP Explorer](https://3gpp-explorer.com/glossary/dml/)
