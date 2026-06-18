---
slug: "ttff"
url: "/mobilnisite/slovnik/ttff/"
type: "slovnik"
title: "TTFF – Time To First Fix"
date: 2026-01-01
abbr: "TTFF"
fullName: "Time To First Fix"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ttff/"
summary: "Klíčový ukazatel výkonu (KPI) pro polohovací systémy, měřící dobu potřebnou pro zařízení k zachycení signálů satelitů a výpočtu jeho počáteční polohy (fixu). Kratší TTFF je zásadní pro uživatelský kom"
---

TTFF je doba potřebná pro zařízení k zachycení signálů satelitů a výpočtu jeho počáteční polohy (fixu), což je klíčový ukazatel výkonu polohovacích systémů.

## Popis

Time To First Fix (TTFF, čas do prvního fixu) je základní metrika výkonu přijímačů Globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)), včetně těch v mobilních zařízeních pro polohování založené na 3GPP. Kvantifikuje dobu, která uplyne od zapnutí přijímače nebo zahájení polohovacího požadavku do okamžiku, kdy poskytne platný polohový fix se stanovenou přesností. Tato metrika je klíčová pro hodnocení rychlosti odezvy a použitelnosti služeb založených na poloze ([LBS](/mobilnisite/slovnik/lbs/)). TTFF se měří za různých počátečních podmínek, které významně ovlivňují jeho délku: Studený start (Cold Start), Teplý start (Warm Start) a Horký start (Hot Start).

Studený start představuje nejhorší scénář, kdy přijímač nemá žádné předchozí informace. Musí provést úplné prohledání oblohy pro satelity, stáhnout kompletní almanach a efemeridní data (navigační zprávy) z každého satelitu a poté vypočítat polohu. Tento proces může trvat 30 sekund až několik minut v závislosti na podmínkách signálu a citlivosti přijímače. Přijímač sekvenčně vyhledává signály, dekóduje pomalý 50 bps navigační datový proud z každého satelitu, aby získal orbitální parametry (efemeridy), a potřebuje signály od alespoň čtyř satelitů pro výpočet 3D polohy.

Teplý start předpokládá, že přijímač má platný, ale neaktuální almanach (hrubou databázi oběžných drah všech satelitů) a přibližný čas a polohu. To mu umožňuje předpovědět, které satelity by měly být viditelné, a zúžit tak vyhledávání. Stále však potřebuje stáhnout čerstvá efemeridní data z každého satelitu, což trvá 18-30 sekund na satelit, protože jsou data vysílána v podrámcích. Horký start je nejrychlejší podmínka, kdy přijímač má platná efemeridní data (stará méně než 2-4 hodiny), přesný čas a přibližnou polohu. Může okamžitě zachytit předpokládané satelity a vypočítat fix, často za méně než jednu sekundu, protože potřebuje pouze synchronizovat se satelitními signály a změřit pseudovzdálenosti.

Ve standardech 3GPP je TTFF specifikováno jako výkonnostní požadavek pro uživatelské zařízení (UE) podporující Asistovaný GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). V A-GNSS síť poskytuje pomocná data (jako efemeridy, almanach, přibližný čas a polohu UE) zařízení UE přes buněčnou signalizaci. Tato pomocná data dramaticky snižují TTFF tím, že odstraní nebo zkrátí dobu potřebnou pro UE k dekódování těchto informací přímo ze satelitů. Specifikace 3GPP definují testovací postupy a minimální výkonnostní kritéria pro TTFF v různých asistovaných i neasistovaných scénářích, aby zajistily konzistentní uživatelský komfort pro tísňové služby (např. E-911) a komerční LBS.

## K čemu slouží

TTFF existuje jako klíčová metrika pro kvantifikaci a standardizaci výkonu při startu a rychlosti odezvy polohovacích systémů, což přímo souvisí s uživatelským komfortem. U starších samostatných [GPS](/mobilnisite/slovnik/gps/) zařízení byly dlouhé časy studeného startu významným problémem použitelnosti, který frustroval uživatele čekající minuty na navigační fix. Pro tísňové služby jako Enhanced 911 (E-911) může být dlouhý TTFF život ohrožující, protože poloha volajícího musí být určena co nejrychleji.

Vytvoření a standardizace TTFF v rámci 3GPP bylo motivováno integrací polohovacích schopností do mobilních zařízení a potřebou garantovat výkon pro regulační a komerční služby. Standardy 3GPP, jako jsou ty pro [A-GNSS](/mobilnisite/slovnik/a-gnss/), měly za cíl zmírnit inherentní omezení samostatného příjmu [GNSS](/mobilnisite/slovnik/gnss/) v náročném prostředí (městské kaňony, vnitřní prostory) a urychlit proces polohování. Definováním požadavků na TTFF a testovacích metodologií 3GPP zajišťuje, že zařízení UE od různých výrobců poskytují předvídatelnou a přijatelnou úroveň výkonu.

Dále optimalizace TTFF pohání inovace v návrhu přijímačů, algoritmech zpracování signálu a síťových asistovaných protokolech. Řeší problém „úzkého hrdla navigačních dat“ – pomalé datové rychlosti vysílané ze satelitů. Řešení jako A-GNSS, predikce efemerid a využití dat z jiných senzorů (fúze senzorů) jsou všechny částečně hodnocena podle jejich dopadu na snížení TTFF. TTFF tedy slouží jako klíčový benchmark pro celý ekosystém polohovacích technologií v mobilních komunikacích.

## Klíčové vlastnosti

- Definován pro tři počáteční podmínky: Studený (Cold), Teplý (Warm) a Horký (Hot) start
- Klíčový ukazatel výkonu (KPI) pro výkon GNSS a A-GNSS přijímačů
- Přímo ovlivňuje uživatelský komfort u služeb založených na poloze a tísňových volání
- Specifikován v 3GPP jako požadavek konformního testu pro UE
- Významně redukován pomocnými daty (Assistance Data) poskytovanými sítí v A-GNSS
- Ovlivněno signálním prostředím, citlivostí přijímače a aktuálností pomocných dat

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 23.731** (Rel-16) — 5G LCS Architecture Enhancement Study
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TR 38.845** (Rel-17) — NR Positioning Use Cases Study
- **TS 38.855** (Rel-16) — Study on NR Positioning Support
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS

---

📖 **Anglický originál a plná specifikace:** [TTFF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ttff/)
