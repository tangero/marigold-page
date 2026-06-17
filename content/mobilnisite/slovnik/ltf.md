---
slug: "ltf"
url: "/mobilnisite/slovnik/ltf/"
type: "slovnik"
title: "LTF – Location Triggering Function"
date: 2025-01-01
abbr: "LTF"
fullName: "Location Triggering Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ltf/"
summary: "Location Triggering Function (LTF) je síťová funkce, která iniciuje procedury založené na poloze pro legální odposlech a služby tísňového volání. Je definována v rámci architektury zabezpečení 5G za ú"
---

LTF je síťová funkce v architektuře zabezpečení 5G, která na základě specifických událostí iniciuje standardizované procedury založené na poloze pro legální odposlech a služby tísňového volání.

## Popis

Location Triggering Function (LTF) je klíčová komponenta v architektuře zabezpečení 3GPP, specificky definovaná pro systémy 5G. Funguje jako logická funkce, která může být integrována v rámci síťových entit, jako je funkce pro legální odposlech ([LIF](/mobilnisite/slovnik/lif/)) nebo Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)). Jejím primárním úkolem je generovat a spravovat spouštěče (triggery) pro žádosti o polohu na základě předem nastavených kritérií nebo dynamických událostí. Tyto spouštěče jsou nezbytné pro služby, které vyžadují, aby síť určila geografickou polohu uživatelského zařízení (UE) za specifických okolností, například při aktivaci povolení k legálnímu odposlechu nebo při zahájení tísňového volání.

Z architektonického hlediska LTF komunikuje s ostatními síťovými funkcemi za účelem vyžádání a přijetí informací o poloze. V kontextu legálního odposlechu interaguje s funkcí pro správu legálního odposlechu (LIAF), aby získala autorizaci a konfiguraci pro spouštěče polohy související s odposlechem. Pro služby tísňového volání může komunikovat s GMLC a funkcí pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) za účelem spuštění procedur určení polohy pro tísňová volání. LTF definuje podmínky, za kterých má být žádost o polohu iniciována, jako je například zřízení hovoru, události mobility nebo periodické intervaly, čímž zajišťuje, že získání polohy je provedeno pouze tehdy, když je to právně nebo provozně odůvodněné.

Funkce pracuje tak, že monitoruje specifické spouštěcí události definované ve specifikacích 3GPP. Když dojde ke konfigurované události, LTF sestaví zprávu žádosti o polohu a odešle ji příslušnému systému pro určení polohy, jako je GMLC. Tento systém pak koordinuje s přístupovou rádiovou sítí (RAN) a UE získání odhadu polohy pomocí metod jako je [OTDOA](/mobilnisite/slovnik/otdoa/) nebo asistovaný [GNSS](/mobilnisite/slovnik/gnss/). Získaná data o poloze jsou poté doručena žadateli, například orgánu činnému v trestním řízení nebo přijímacímu středisku tísňového volání. Provoz LTF je řízen přísnými bezpečnostními a ochrannými protokoly, aby se zabránilo neoprávněnému přístupu a zajistil soulad s regulatorními požadavky.

Mezi klíčové komponenty LTF patří definice spouštěcích událostí, mechanismy vynucování politik pro rozhodnutí o aktivaci žádosti o polohu a rozhraní pro komunikaci s funkcemi správy a získávání polohy. Její role je klíčová pro oddělení logiky spouštění od samotného procesu určení polohy, což umožňuje modulární a škálovatelnou architekturu zabezpečení. Standardizací této funkce 3GPP zajišťuje, že služby založené na poloze pro bezpečnostní a tísňové účely jsou implementovány konzistentně napříč různými síťovými nasazeními a dodavateli, což usnadňuje interoperabilitu a soulad s předpisy.

## K čemu slouží

Location Triggering Function byla zavedena, aby řešila rostoucí potřebu standardizovaných, bezpečných a efektivních mechanismů pro spouštění žádostí o polohu v mobilních sítích, zejména pro legální odposlech a služby tísňového volání. Před její standardizací byly implementace pro spouštění procedur založených na poloze často závislé na konkrétním dodavateli nebo vázané na specifické síťové architektury, což vedlo k problémům s interoperabilitou a nekonzistentními bezpečnostními kontrolami. Vzhledem k tomu, že sítě 5G přinesly nové architektury založené na službách a vylepšené funkce ochrany soukromí, byla vyžadována dedikovaná funkce pro správu komplexních politik a událostí spojených se spouštěním polohy bezpečným způsobem.

Vytvoření LTF bylo motivováno regulatorními požadavky po celém světě, které ukládají poskytovatelům telekomunikačních služeb povinnost pomáhat orgánům činným v trestním řízení s možnostmi legálního odposlechu, což stále častěji zahrnuje i informace o poloze. Kromě toho kritická povaha služeb tísňového volání, kde přesná a včasná data o poloze mohou zachraňovat životy, si vyžádala robustní a spolehlivý spouštěcí mechanismus uvnitř jádra sítě. LTF poskytuje jasný architektonický bod pro implementaci těchto právně vyžadovaných funkcí, čímž zajišťuje, že žádosti o polohu jsou spouštěny pouze za autorizovaných podmínek a že proces dodržuje přísné standardy ochrany dat.

Definováním LTF ve specifikacích 3GPP Release 16 a novějších chtěl standardizační orgán zajistit budoucí připravenost spouštění polohy pro vyvíjející se síťové technologie a případy užití. Řeší omezení předchozích ad-hoc přístupů tím, že poskytuje jednotný rámec, který se integruje s rozhraními založenými na službách a bezpečnostními architekturami jádra sítě 5G. To umožňuje síťovým operátorům efektivněji nasazovat kompliantní systémy a dává orgánům činným v trestním řízení a službám tísňového volání možnost spoléhat se na konzistentní a kvalitní informace o poloze, když jsou nejvíce potřeba.

## Klíčové vlastnosti

- Standardizované spouštěcí události pro žádosti o polohu
- Integrace s architekturou legálního odposlechu
- Podpora spouštění určení polohy pro služby tísňového volání
- Řízení aktivačních kritérií na základě politik
- Rozhraní k GMLC a funkcím správy
- Mechanismy vynucování zabezpečení a ochrany soukromí

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [LTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ltf/)
