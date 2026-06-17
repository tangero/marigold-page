---
slug: "epa"
url: "/mobilnisite/slovnik/epa/"
type: "slovnik"
title: "EPA – Expectation Propagation Algorithm"
date: 2025-01-01
abbr: "EPA"
fullName: "Expectation Propagation Algorithm"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/epa/"
summary: "Algoritmus šíření očekávání (EPA) je výpočetní metoda používaná ve zpracování signálu a odhadu kanálu v rámci 3GPP rádiových systémů. Jedná se o iterační Bayesovskou inferenční techniku, která aproxim"
---

EPA je iterační Bayesovský inferenční algoritmus používaný v 3GPP rádiových systémech pro úlohy zpracování signálu, jako je MIMO detekce a odhad kanálu, k aproximaci složitých pravděpodobnostních rozdělení a ke zlepšení výkonu přijímače.

## Popis

Algoritmus šíření očekávání (EPA) je sofistikovaná technika zpracování signálu používaná na fyzické vrstvě 3GPP rádiových přístupových sítí, zvláště relevantní pro LTE a 5G NR. Patří do rodiny přibližných Bayesovských inferenčních metod, navržených pro práci se složitými pravděpodobnostními modely, kde je přesný výpočet neřešitelný. V principu EPA funguje iterativním zpřesňováním jednoduššího, řešitelného rozdělení (jako je Gaussovské) k aproximaci složitějšího aposteriorního rozdělení zahrnujícího více proměnných, jako jsou vysílané symboly v [MIMO](/mobilnisite/slovnik/mimo/) systému nebo bity v kódované sekvenci.

Během činnosti EPA pracuje prostřednictvím série iterací předávání zpráv mezi faktorovými uzly a proměnnými uzly uvnitř pravděpodobnostního grafického modelu reprezentujícího komunikační systém. Každá iterace zahrnuje dva klíčové kroky: krok očekávání, kde jsou spočítány momenty (jako střední hodnota a rozptyl) přibližného rozdělení, a krok projekce, kde jsou tyto momenty použity k aktualizaci parametrů jednoduššího aproximačního rozdělení. Tento proces pokračuje až do konvergence, čímž efektivně odděluje vzájemně závislé proměnné a zjednodušuje problém detekce nebo dekódování. Uvnitř řetězce přijímače může být EPA aplikována na úlohy jako je měkký odhad symbolů pro QAM konstelace ve vysokořádovém MIMO, iterační odhad kanálu a dat nebo jako součást pokročilých schémat turbo ekvalizace.

Z architektonického hlediska je EPA implementována v jednotkách základního pásma jak uživatelského zařízení (UE), tak základnových stanic (gNB/[eNB](/mobilnisite/slovnik/enb/)). Jejím úkolem je zvýšit výkon digitálního přijímače, což mu umožňuje přesněji rekonstruovat vysílaná data v přítomnosti šumu, interference a zkreslení kanálu. Poskytnutím lepších odhadů měkkých informací zlepšuje vstup do dekodérů kanálu (jako [LDPC](/mobilnisite/slovnik/ldpc/) nebo Turbo dekodéry), čímž snižuje míru chyb bloků ([BLER](/mobilnisite/slovnik/bler/)) a zvyšuje efektivní datové rychlosti. Tento algoritmus je klíčovým prvkem pro dosažení vysoké spektrální účinnosti a cílů spolehlivosti moderních celulárních standardů, zejména v náročných podmínkách šíření.

## K čemu slouží

Algoritmus šíření očekávání byl zaveden do působnosti 3GPP, aby řešil rostoucí výpočetní složitost a výkonnostní nároky pokročilých rádiových technologií, jako je [MIMO](/mobilnisite/slovnik/mimo/) a vysokořádová modulace. Tradiční detekční algoritmy, jako je maximální věrohodnost, se stávají nepřijatelně složitými s rostoucím počtem antén a bodů konstelace. EPA poskytuje výpočetně efektivní aproximaci, která dosahuje téměř optimálního výkonu, a řeší tak problém přesné detekce signálu v hustých, interferencí bohatých prostředích bez nutnosti nerealistického výpočetního výkonu.

Historicky, jak se 3GPP vyvíjelo od Release 6 dále, systémy jako [HSPA](/mobilnisite/slovnik/hspa/), LTE a později 5G NR posouvaly hranice spektrální účinnosti. To vytvořilo potřebu sofistikovanějších přijímacích algoritmů, které by dokázaly vytěžit maximum z rádiového spoje. EPA, jako všestranný inferenční rámec, byla přijata ke zlepšení klíčových funkcí přijímače. Její vytvoření a standardizace v různých testovacích specifikacích (např. pro výkonnostní požadavky) bylo motivováno cílem definovat realistické, avšak náročné výkonnostní referenční hodnoty přijímače, což zajišťuje, že implementace různých výrobců mohou poskytovat konzistentní vysokou kvalitu služeb, zejména pro uživatele na okraji buňky, kde jsou podmínky signálu nejhorší.

## Klíčové vlastnosti

- Iterační Bayesovská inferenční metoda pro aproximaci složitých rozdělení
- Používá se v MIMO detekci a odhadu kanálu ke zlepšení přesnosti
- Využívá kroky očekávání a projekce v rámci předávání zpráv
- Snižuje výpočetní složitost ve srovnání s optimálními detektory
- Zvyšuje výkon přijímače pro vysokořádovou QAM a prostorové multiplexování
- Poskytuje vylepšené měkké výstupní informace pro dekodéry kódu s přímou opravou chyb

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 37.171** (Rel-19) — UE Positioning Performance Requirements
- **TR 38.812** (Rel-16) — Study on NOMA for NR

---

📖 **Anglický originál a plná specifikace:** [EPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/epa/)
