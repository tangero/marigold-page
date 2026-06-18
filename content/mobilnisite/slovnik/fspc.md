---
slug: "fspc"
url: "/mobilnisite/slovnik/fspc/"
type: "slovnik"
title: "FSPC – Feature Set Per Component-carrier"
date: 2025-01-01
abbr: "FSPC"
fullName: "Feature Set Per Component-carrier"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/fspc/"
summary: "FSPC je mechanismus hlášení schopností v 5G NR, kdy uživatelské zařízení (UE) deklaruje své podporované funkce samostatně pro každou komponentní nosnou (CC) v scénářích agregace nosných (CA). Umožňuje"
---

FSPC je mechanismus hlášení schopností v 5G NR, kdy uživatelské zařízení deklaruje své podporované funkce samostatně pro každou komponentní nosnou při agregaci nosných.

## Popis

Feature Set Per Component-carrier (FSPC) je technický koncept ve specifikacích 5G New Radio (NR), který definuje, jak uživatelské zařízení (UE) hlásí své podporované rádiové funkce nezávisle pro každou komponentní nosnou ([CC](/mobilnisite/slovnik/cc/)) při konfigurované agregaci nosných ([CA](/mobilnisite/slovnik/ca/)). Při agregaci nosných se kombinuje více CC ke zvýšení šířky pásma a datových rychlostí, ale každá CC může pracovat v různých kmitočtových pásmech nebo částech šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)) s odlišnými charakteristikami. FSPC umožňuje UE specifikovat, které funkce podporuje na každé CC samostatně, namísto poskytnutí jediného agregovaného hlášení schopností pro všechny CC. Tato granularita na úrovni nosné je komunikována z UE do gNodeB (gNB) během procedur výměny schopností, typicky prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/).

Z architektonického hlediska se FSPC integruje do frameworku schopností UE definovaného v 3GPP. UE udržuje seznam sad funkcí, který zahrnuje parametry jako podporované modulační schémy (např. 256QAM, 1024QAM), [MIMO](/mobilnisite/slovnik/mimo/) vrstvy (např. 2x2, 4x4), konfigurace šířky pásma a další schopnosti fyzické vrstvy. Když je CA povolena, UE organizuje tyto informace do samostatných záznamů pro každou CC, indexovaných podle indexu obslužné buňky nebo kmitočtového pásma. gNB tyto informace zpracovává, aby vytvořil komplexní pohled na schopnosti UE napříč agregovaným spektrem. Mezi klíčové součásti zapojené do procesu patří vrstva řízení rádiových prostředků (RRC) UE, která formátuje a vysílá hlášení schopností, a plánovač gNB, který používá data FSPC k informovaným rozhodnutím o přidělování prostředků, výběru modulačního a kódovacího schématu ([MCS](/mobilnisite/slovnik/mcs/)) a konfiguraci MIMO na každou CC.

V provozu FSPC funguje následovně: během počátečního přístupu nebo rekonfigurace gNB požádá o schopnosti UE. UE odpoví podrobnou zprávou, která obsahuje sady funkcí na úrovni CC, pokud je CA podporována. Například UE může hlásit podporu 4x4 MIMO na CC1 (ve středním pásmu), ale pouze 2x2 MIMO na CC2 (v vysokém pásmu) kvůli hardwarovým omezením nebo úvahám o výkonu. gNB pak tyto informace použije k přizpůsobení svých strategií plánování a adaptace spojení. Při přidělování downlinkových nebo uplinkových prostředků může gNB přizpůsobit přenášené datové toky nejsilnějším schopnostem UE na každé CC, čímž optimalizuje propustnost a spolehlivost. Tato optimalizace na úrovni nosné je obzvláště důležitá v heterogenních sítích, kde mohou mít CC různé podmínky šíření nebo úrovně interference.

Úloha FSPC v 5G RAN spočívá v maximalizaci účinnosti nasazení agregace nosných. Díky pochopení přesných schopností na každé CC se síť může vyhnout nadměrnému poskytování (např. pokusu o použití funkce, kterou UE na dané CC nepodporuje) nebo nedostatečnému využití (např. nepoužití pokročilé funkce tam, kde je dostupná). To vede ke zlepšené spektrální účinnosti, vyšším datovým rychlostem a lepší celkové uživatelské zkušenosti. FSPC také podporuje flexibilitu 5G NR, které pracuje napříč různými rozsahy spektra (FR1 a FR2) s různou složitostí zařízení. Zajišťuje, aby síťové prostředky byly sladěny se skutečnými schopnostmi UE, což usnadňuje hladký provoz ve složitých scénářích CA zahrnujících jak nosné s frekvenčním duplexem ([FDD](/mobilnisite/slovnik/fdd/)), tak s časovým duplexem ([TDD](/mobilnisite/slovnik/tdd/)).

## K čemu slouží

FSPC bylo vytvořeno, aby řešilo omezení dřívějších mechanismů hlášení schopností, které byly často agregovány napříč všemi komponentními nosnými v scénářích agregace nosných. V LTE a raných návrzích 5G mohla UE hlásit jednotnou sadu funkcí, která předpokládala stejné schopnosti na všech agregovaných nosných. Tento přístup byl nedostatečný, protože moderní zařízení, zejména ta podporující široké kmitočtové rozsahy, mohou mít různý návrh RF předního konce, konfigurace antén nebo výpočetní výkon na pásmo. Například UE může podporovat pokročilé funkce jako vysoký řád MIMO nebo širokou šířku pásma na primární nosné v nízkém pásmu, ale ne na sekundární nosné v mmWave pásmu kvůli hardwarovým omezením. Bez hlášení na úrovni CC by síť mohla nesprávně předpokládat stejné schopnosti, což by vedlo k chybám v plánování, sníženému výkonu nebo dokonce k selhání spojení.

Motivace pro FSPC vychází z rostoucí složitosti a heterogenity 5G sítí. Jak se agregace nosných rozšiřuje o více CC napříč fragmentovanými spektry, efektivní správa prostředků se stává kritickou. Historický kontext ukazuje, že jak se CA vyvíjela z 2CC na 8CC a více, rostla potřeba granulárního povědomí o schopnostech. Předchozí přístupy riskovaly buď konzervativní plánování (nedostatečné využití síťových prostředků), nebo agresivní plánování (způsobující chyby UE). FSPC to řeší tím, že poskytuje detailní, na nosnou specifické informace, což umožňuje gNB optimalizovat přenosy na každé CC. To je obzvláště důležité pro nákladově efektivní návrhy zařízení, kde výrobci mohou implementovat různé schopnosti na různých pásmech, aby vyvážili výkon a cenu.

Řešením těchto problémů FSPC zvyšuje praktičnost pokročilých konfigurací CA v 5G. Umožňuje sítím využít plný potenciál každé CC podle skutečného hardwaru UE, což podporuje vyšší propustnost a spolehlivost. Toto zpřesnění hlášení schopností je klíčové pro dosažení vícegigabitových datových rychlostí slibovaných 5G, zejména ve scénářích jako nestandalone (NSA) a standalone (SA) nasazení s různorodými spektry. V konečném důsledku FSPC přispívá k adaptivnější a účinnější RAN, zajišťuje, že agregace nosných přináší konzistentní zisky výkonu napříč různými typy zařízení a síťovými podmínkami.

## Klíčové vlastnosti

- Hlášení schopností UE na úrovni komponentní nosné pro agregaci nosných
- Granulární definice sady funkcí zahrnující modulaci, MIMO a šířku pásma
- Podpora heterogenních schopností napříč různými kmitočtovými pásmy
- Integrace se signalizací RRC pro dynamickou výměnu schopností
- Umožňuje optimalizované plánování gNB a adaptaci spojení na každou CC
- Usnadňuje efektivní využití spektrálních zdrojů v 5G NR

## Definující specifikace

- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters

---

📖 **Anglický originál a plná specifikace:** [FSPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fspc/)
