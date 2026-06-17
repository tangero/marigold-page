---
slug: "fsw"
url: "/mobilnisite/slovnik/fsw/"
type: "slovnik"
title: "FSW – Frame Synchronization Word"
date: 2025-01-01
abbr: "FSW"
fullName: "Frame Synchronization Word"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fsw/"
summary: "Předdefinovaná bitová sekvence vysílaná na začátku rádiového rámce, která umožňuje přijímači detekovat hranici rámce a dosáhnout časové synchronizace. Jedná se o základní mechanismus fyzické vrstvy pr"
---

FSW je předdefinovaná bitová sekvence vysílaná na začátku rádiového rámce, která umožňuje přijímači detekovat hranici rámce a dosáhnout počáteční časové synchronizace.

## Popis

Frame Synchronization Word (FSW) je kritický primitiv fyzické vrstvy definovaný ve specifikacích 3GPP, především pro UMTS a jeho vývoj. Skládá se ze specifického, známého vzoru bitů nebo čipů, který je vložen na předem určenou pozici ve struktuře vysílaného rádiového rámce. Primární technickou funkcí FSW je poskytnout jasný, detekovatelný marker, který umožní synchronizačnímu obvodu přijímače identifikovat přesný začátek rámce. Tento proces, známý jako synchronizace rámce, je prvním krokem v řetězci akvizice signálu přijímače. Bez úspěšné synchronizace rámce nemůže přijímač správně zarovnat svůj časový referenční signál s příchozím datovým tokem, což znemožňuje demodulaci následného přenosu dat.

Během provozu přijímač průběžně koreluje příchozí signál se známým vzorem FSW. Když je detekován vysoký korelační pík, značí to vysokou pravděpodobnost nalezení hranice rámce. Tato detekce umožňuje přijímači upravit svůj interní hodinový signál a čítač rámců, aby se zarovnaly s časováním vysílače. Návrh vzoru FSW je klíčový; musí mít dobré autokorelační vlastnosti (ostrý pík při zarovnání) a nízkou vzájemnou korelaci s jinými sekvencemi, aby se minimalizovaly falešné detekce v šumovém prostředí nebo za přítomnosti rušivých signálů. V systémech založených na WCDMA, jako je UMTS, je to často implementováno pomocí specifických skramblovacích kódů nebo midamble sekvencí ve struktuře fyzického kanálu.

Role FSW přesahuje pouhou detekci hranice. Jakmile je synchronizace rámce dosažena, poskytuje časový základ pro všechny ostatní synchronizační procesy, včetně synchronizace time slotů, synchronizace symbolů a synchronizace frekvence. Umožňuje přijímači správně deskramblovat signál pomocí známého rámci periodického skramblovacího kódu a provést desprezování ortogonálních kanalizačních kódů. Dále je v systémech využívajících duplex s časovým dělením (TDD) přesná synchronizace rámce nezbytná pro rozlišení mezi vysílacími a přijímacími time sloty. FSW je tedy základním prvkem, který zajišťuje, že přijímač může koherentně rekonstruovat vysílaná data, což ovlivňuje celkový výkon systému, dobu hledání buňky a spolehlivost předávání spojení.

## K čemu slouží

Frame Synchronization Word existuje, aby řešil základní problém časové akvizice v systémech digitální rádiové komunikace. Když uživatelské zařízení (UE) zapne nebo vstoupí do oblasti pokrytí nové buňky, nemá žádnou předchozí znalost o přesném časování vysílání základnové stanice. Účelem FSW je poskytnout jednoznačný referenční bod v kontinuálním toku vysílaných symbolů, což umožní UE rychle a spolehlivě určit, kde každý rámec začíná. Tím se řeší počáteční problém 'hledání jehly v kupce sena', tedy nalezení struktury v šumovém, neznámém signálu.

Historicky by bez vyhrazeného, robustního synchronizačního slova přijímače vyžadovaly složité a časově náročné algoritmy pro slepý odhad hranic rámců, což by vedlo k delší počáteční době přístupu, zvýšené spotřebě baterie během hledání buňky a vyšší pravděpodobnosti selhání synchronizace, zejména v podmínkách nízkého poměru signálu k šumu. Standardizované FSW poskytuje deterministickou a efektivní metodu synchronizace. Jeho vytvoření bylo motivováno potřebou rychlých a spolehlivých procedur hledání a výběru buňky, které jsou klíčové pro mobilitu uživatele a dostupnost sítě. Řeší omezení ad-hoc synchronizačních metod tím, že nabízí v celé síti konzistentní signál, který jsou všechna UE navržena hledat, čímž zefektivňuje počáteční přístupovou proceduru definovanou ve standardech 3GPP.

## Klíčové vlastnosti

- Předdefinovaná bitová/čipová sekvence pro deterministickou detekci
- Umožňuje přijímači identifikovat začátek rádiového rámce
- Poskytuje základ pro všechny následné časové a synchronizační procesy
- Navrženo se silnými autokorelačními vlastnostmi pro spolehlivou detekci píku
- Integrální součást struktury fyzického kanálu ve standardech 3GPP UTRA
- Snižuje dobu hledání buňky a počáteční akvizice pro UE

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels

---

📖 **Anglický originál a plná specifikace:** [FSW na 3GPP Explorer](https://3gpp-explorer.com/glossary/fsw/)
