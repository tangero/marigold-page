---
slug: "trms"
url: "/mobilnisite/slovnik/trms/"
type: "slovnik"
title: "TRMS – Total Radiated Multi-antenna Sensitivity"
date: 2025-01-01
abbr: "TRMS"
fullName: "Total Radiated Multi-antenna Sensitivity"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/trms/"
summary: "Výkonnostní metrika pro hodnocení celkové přijímací citlivosti víceanténního UE, která zohledňuje kombinovaný účinek všech anténních větví a přijímacího řetězce. Je klíčová pro posouzení reálného výko"
---

TRMS je výkonnostní metrika pro hodnocení celkové přijímací citlivosti víceanténního UE, která zohledňuje kombinovaný účinek všech jeho anténních větví a přijímacího řetězce.

## Popis

Total Radiated Multi-antenna Sensitivity (TRMS) je komplexní výkonnostní metrika definovaná ve specifikacích 3GPP pro hodnocení přijímací citlivosti uživatelského zařízení (UE) vybaveného více anténami. Na rozdíl od tradičních měření citlivosti s jednou anténou, která testují jeden anténní port izolovaně, TRMS posuzuje schopnost UE přijímat signály v realistickém, bezdrátovém ([OTA](/mobilnisite/slovnik/ota/)) uspořádání, kde jsou aktivní všechny anténní větve a celý přijímací zpracovatelský řetězec (včetně kombinačních algoritmů). Metrika je definována jako minimální průměrný výkon přijímaný na anténních konektorech UE (nebo ekvivalentně minimální výkon dopadající z dalekého pole) potřebný k dosažení stanoveného propustnostního výkonu (např. 95 % maximální propustnosti) pro daný referenční měřicí kanál. Obvykle se měří v dBm.

Měření TRMS se provádí v bezodrazové komoře pomocí uspořádání napodobujícího reálné osvětlení sférickou vlnoplochou. Testovací systém vysílá standardizovaný referenční signál (např. specifickou konfiguraci [PDSCH](/mobilnisite/slovnik/pdsch/)) z jedné nebo více antén emulátoru základnové stanice. UE, umístěné na pozicionačním systému, se otáčí v několika prostorových úhlech (azimut a elevace), aby se zachytil jeho výkon v celé sféře. V každém úhlu se upravuje vstupní výkon, aby se našla prahová hodnota, při které je cílové propustnosti právě dosaženo. Hodnota TRMS se pak odvozuje ze statistické agregace (často lineárního průměru) těchto úrovní výkonu citlivosti ve všech měřených úhlech. Tento proces inherentně zachycuje účinky vyzařovacích charakteristik antén, vzájemného vazeb mezi anténami, šumových čísel přijímače a výkonu algoritmů pro diverzitní kombinaci nebo příjem [MIMO](/mobilnisite/slovnik/mimo/) v UE.

Z architektonického hlediska TRMS hodnotí integrovaný výkon anténního subsystému UE, vysokofrekvenčního předřadníku a základnového pásma digitálního přijímače. U víceanténních UE využívajících techniky jako příjem s diverzitou (např. výběrová kombinace, kombinace s maximálním poměrem) nebo prostorové multiplexování MIMO metrika TRMS kvantifikuje skutečné zlepšení citlivosti získané těmito technikami v radiačním prostředí. Nižší (zápornější) hodnota TRMS znamená lepší přijímací citlivost, což znamená, že UE může udržovat spojení při nižších úrovních signálu, což přímo rozšiřuje pokrytí buňky a zlepšuje spolehlivost na jejím okraji. TRMS je proto klíčovým parametrem pro síťové operátory a výrobce zařízení, kteří zajišťují konzistentní uživatelský zážitek, zejména v náročných rádiových podmínkách.

## K čemu slouží

TRMS bylo zavedeno, aby vyřešilo nedostatečnost tradičních testů citlivosti vedeným signálem pro hodnocení moderních víceanténních UE. Testy vedeným signálem, které vstupují přímo do jednoho anténního portu prostřednictvím kabelu, nezohledňují reálné efekty, jako je účinnost antény, vyzařovací charakteristiky a interakce mezi více anténami. Jak se UE vyvíjela a začala obsahovat 2x2, 4x4 [MIMO](/mobilnisite/slovnik/mimo/) a příjem s diverzitou pro zvýšení přenosových rychlostí a spolehlivosti, bylo stále zřejmější, že výkon integrovaného anténně-přijímacího systému nelze předpovědět pouze z testů na úrovni komponent. Špatný návrh antény mohl negovat výhody vynikajícího přijímače základnového pásma.

Jeho vytvoření bylo motivováno potřebou standardizované, holistické metriky, která odráží skutečný zážitek koncového uživatele v podmínkách slabého signálu. Síťoví operátoři zejména potřebovali způsob, jak porovnávat různé modely UE podle jejich schopnosti udržovat službu na okraji pokrytí, což ovlivňuje plánování sítě a spokojenost zákazníků. TRMS toto poskytuje měřením citlivosti bezdrátovým ([OTA](/mobilnisite/slovnik/ota/)) způsobem, kdy je UE považováno za kompletní vyzařující a přijímající entitu. Řeší problém variability výkonu způsobené umístěním antény, průmyslovým designem a manipulací uživatele (např. efekty úchytu ruky).

Historicky bylo OTA testování pro TRMS formalizováno ve verzi 3GPP Release 13, navazující na dřívější práci pro [TRP](/mobilnisite/slovnik/trp/) (Total Radiated Power). Představuje posun k ověřování výkonu na systémové úrovni. Definováním rigorózní testovací metodologie TRMS zajišťuje, že UE, která deklarují víceanténní schopnosti, skutečně poskytují slibovaná zlepšení pokrytí a spolehlivosti v praxi, což je nezbytné pro úspěšné nasazení pokročilých sítí LTE a 5G, kde je MIMO základní technologií.

## Klíčové vlastnosti

- Metrika výkonu bezdrátovým (OTA) přenosem pro přijímací citlivost víceanténního UE.
- Měří minimální dopadající výkon potřebný k dosažení cílové propustnosti.
- Integruje efekty vyzařovacích charakteristik antén, účinnosti, vzájemné vazby a přijímacích algoritmů.
- Zahrnuje sférické měření ve všech azimutálních a elevančních úhlech.
- Klíčový ukazatel reálného pokrytí a výkonu na okraji buňky.
- Standardizovaná testovací metodologie definovaná ve specifikacích 3GPP pro reprodukovatelnost.

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 37.144** (Rel-19) — UE OTA Antenna Performance Requirements
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE

---

📖 **Anglický originál a plná specifikace:** [TRMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/trms/)
