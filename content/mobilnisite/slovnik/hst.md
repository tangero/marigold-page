---
slug: "hst"
url: "/mobilnisite/slovnik/hst/"
type: "slovnik"
title: "HST – High Speed Train"
date: 2025-01-01
abbr: "HST"
fullName: "High Speed Train"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hst/"
summary: "HST označuje scénáře a technické funkce navržené pro podporu spolehlivé mobilní komunikace pro uživatele ve vysokorychlostních vlacích. Řeší specifické výzvy, jako je výrazný Dopplerův jev, časté přec"
---

HST je soubor scénářů a technických funkcí navržených pro podporu spolehlivé mobilní komunikace pro uživatele ve vysokorychlostních vlacích, které řeší výzvy jako výrazný Dopplerův jev a časté přechody mezi buňkami.

## Popis

Ve standardech 3GPP není Vysokorychlostní vlak (HST) samostatnou technologií, ale scénářem nasazení a souborem souvisejících technických vylepšení pro zajištění kvality služeb pro cestující pohybující se velmi vysokou rychlostí, typicky až 350 km/h nebo dokonce 500 km/h v pozdějších studiích. Hlavní výzvou je extrémní Dopplerův jev, který způsobuje výrazný posun frekvence přijímaného signálu. Například při rychlosti 350 km/h a nosné frekvenci 2 GHz může být Dopplerův posuv přibližně ±650 Hz. Tento posun narušuje ortogonalitu subnosných [OFDM](/mobilnisite/slovnik/ofdm/) v LTE a NR, což vede k interferenci mezi nosnými ([ICI](/mobilnisite/slovnik/ici/)) a zhoršuje kvalitu signálu.

Pro zmírnění těchto efektů specifikoval 3GPP několik adaptací na fyzické a vyšší vrstvě. Na fyzické vrstvě může uživatelské zařízení (UE) určené pro scénáře HST implementovat pokročilé algoritmy odhadu kanálu a techniky kompenzace frekvenčního posunu. Síť může konfigurovat specifické referenční signály a přenosové módy, které jsou odolnější vůči rychlému útlumu a častým změnám kanálu. Dále byla studována koncepce 'pohyblivých buněk' nebo skupinové mobility, kdy je vlak považován za jednu mobilní skupinu. Namísto individuálních přechodů mezi buňkami pro každé UE cestujícího může síť spravovat přechod pro celou skupinu UE současně, což výrazně snižuje signalizační režii a pravděpodobnost selhání přechodu.

Na úrovni správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) jsou parametry přechodu mezi buňkami optimalizovány pro vysokorychlostní scénáře. To zahrnuje zkrácení doby spouštění ([TTT](/mobilnisite/slovnik/ttt/)) pro měření pro přechod a úpravu hysterezních hodnot pro zahájení přechodu dříve a spolehlivěji, jak se vlak blíží k hranicím buňky. Aspekty základní sítě zahrnují optimalizaci procedur aktualizace sledované oblasti ([TAU](/mobilnisite/slovnik/tau/)) a přechodu mezi buňkami pro zvládnutí rychlé změny obsluhujících základnových stanic. V 5G NR se studie v Release 15 a novějších zaměřily na správu a sledování svazků pro vysokorychlostní mobilitu, aby bylo zajištěno, že úzké svazky používané v mmWave pásmech mohou být přesně nasměrovány a udržovány pro uživatele ve vysokorychlostním vlaku.

## K čemu slouží

Standardizace funkcí HST byla motivována globální expanzí vysokorychlostních železničních sítí a rostoucím očekáváním cestujících mít během cesty nepřerušovaný přístup k vysokokvalitnímu mobilnímu širokopásmovému připojení. Tradiční mobilní sítě byly optimalizovány pro rychlosti chodců a běžných vozidel, kde byly Dopplerovy posuvy a míra přechodů mezi buňkami zvládnutelné. Při rychlostech vlaku přesahujících 300 km/h tyto konvenční mechanismy často selhávaly, což vedlo k přerušeným hovorům, datovým relacím a špatné uživatelské zkušenosti.

Počáteční práce v 3GPP, zejména kolem Release 8 pro LTE, začaly studovat dopad vysoké rychlosti na výkon. Formální vytvoření specifických scénářů HST a testovacích požadavků mělo za cíl poskytnout standardizovaný rámec pro výrobce a operátory pro vývoj a nasazení interoperabilních řešení. Tím byl vyřešen problém roztříštěných proprietárních implementací. Definováním společných kanálových modelů (např. 'High Speed Train' kanálový model pro testování), požadavků na výkon a potenciálních technik vylepšení umožnil 3GPP průmyslu systematicky řešit jedinečné výzvy rádiového šíření a mobility, a zajistit tak, že mobilní komunikace může držet krok s moderní dopravní infrastrukturou.

## Klíčové vlastnosti

- Definice specifických kanálových modelů pro vysokorychlostní mobilitu pro zkušební shodu (např. až 500 km/h)
- Vylepšení algoritmů fyzické vrstvy pro odhad a kompenzaci Dopplerova posuvu
- Optimalizované procedury přechodu mezi buňkami s upravenými parametry (např. zkrácená doba spouštění) pro vysokorychlostní změnu buňky
- Studie skupinové mobility a správy mobility řízené sítí pro UE ve vlaku
- Vylepšení správy svazků v 5G NR pro udržení spojení s úzkými svazky při vysoké rychlosti
- Optimalizace signalizace v základní síti pro časté aktualizace sledované oblasti během vysokorychlostní jízdy

## Definující specifikace

- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TR 38.852** (Rel-17) — 1900MHz NR band for European Rail Mobile Radio
- **TR 38.853** (Rel-17) — 900MHz NR Band for European Rail Mobile Radio

---

📖 **Anglický originál a plná specifikace:** [HST na 3GPP Explorer](https://3gpp-explorer.com/glossary/hst/)
