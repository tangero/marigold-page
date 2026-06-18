---
slug: "scn"
url: "/mobilnisite/slovnik/scn/"
type: "slovnik"
title: "SCN – Sub-Channel Number"
date: 2025-01-01
abbr: "SCN"
fullName: "Sub-Channel Number"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/scn/"
summary: "SCN je identifikátor používaný v GSM a příbuzných systémech k určení podkanálu v rámci rádiového kanálu. Pomáhá řídit přidělování kmitočtu a časových slotů, což umožňuje efektivní využití spektra a po"
---

SCN je identifikátor používaný v GSM a příbuzných systémech k určení podkanálu v rámci rádiového kanálu pro správu přidělování kmitočtu a časových slotů.

## Popis

Sub-Channel Number (SCN) je základní parametr v GSM (Global System for Mobile Communications) a jeho vývojových systémech, standardizovaný od 3GPP Release 5. Je definován ve specifikaci 21.905. SCN slouží jako index k identifikaci konkrétního podkanálu v rámci širší struktury rádiového kanálu. V GSM je rádiový kanál rozdělen na fyzické kanály na základě přístupu [TDMA](/mobilnisite/slovnik/tdma/) (Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)), kde každý kanál sestává z rámců a časových slotů. SCN poskytuje podrobný identifikátor pro tyto podjednotky, což je nezbytné pro správu zdrojů a signalizaci.

Architektonicky SCN funguje v kontextu přidělování a mapování kanálů. V GSM je nosný kmitočet rozdělen na osm časových slotů na TDMA rámec a každý časový slot lze považovat za podkanál. SCN spolu s dalšími parametry, jako je Absolute Radio Frequency Channel Number ([ARFCN](/mobilnisite/slovnik/arfcn/)), jednoznačně identifikuje fyzický kanál používaný pro přenos uživatelských dat nebo řídicí účely. Používá se v zprávách mezi sítí a mobilními stanicemi k přiřazování zdrojů, specifikaci sekvencí pro přeskakování kmitočtů nebo k označení konfigurace kanálů. Například ve scénářích s přeskakováním kmitočtů pomáhá SCN určit, kterou kombinaci časového slotu a kmitočtu má mobilní stanice použít v daném rámci.

Jak to funguje: Když síť přidělí kanál mobilní stanici, zahrne SCN do příkazů pro přiřazení. Stanice použije toto číslo v kombinaci s ARFCN a číslem rámce k naladění svého přijímače/vysílače na správný časový slot. To umožňuje více uživatelům sdílet stejný kmitočet obsazením různých časových slotů. SCN je také klíčový pro mapování logických kanálů, kde se řídicí kanály (jako [BCCH](/mobilnisite/slovnik/bcch/), [CCCH](/mobilnisite/slovnik/ccch/)) a kanály pro přenos dat ([TCH](/mobilnisite/slovnik/tch/)) mapují na konkrétní podkanály. Poskytnutím standardizovaného číslovacího schématu SCN zajišťuje interoperabilitu mezi síťovým zařízením a koncovými zařízeními, což umožňuje efektivní využití spektra a robustní komunikaci v celulárních sítích.

## K čemu slouží

SCN byl zaveden k řešení potřeby přesné identifikace a správy podkanálů v systémech založených na [TDMA](/mobilnisite/slovnik/tdma/), jako je GSM. Před standardizací mohlo být přidělování zdrojů nejednoznačné, což vedlo ke konfliktům a neefektivnímu využití spektra. Zavedení SCN poskytlo jasný, číselný způsob, jak odkazovat na konkrétní časové sloty v rámci rádiového kanálu, což je nezbytné pro funkce jako přeskakování kmitočtů, dynamické přiřazování kanálů a procedury předávání hovoru (handover).

Řeší problém, jak efektivně koordinovat více uživatelů na omezených rádiových zdrojích. Použitím SCN může síť navádět mobilní stanice na přesné časové sloty, čímž minimalizuje interference a maximalizuje kapacitu. To je obzvláště důležité v přelidněných městských prostředích, kde je spektrum omezené. Parametr také podporuje pokročilé funkce, jako jsou poloviční rychlostní kanály, kde dva hovory sdílejí jeden časový slot, tím, že umožňuje jemně odstupňovanou kontrolu nad přidělováním podkanálů.

Historicky, jak se GSM vyvíjelo a zahrnovalo [GPRS](/mobilnisite/slovnik/gprs/) a EDGE, zůstala role SCN klíčová pro zpětnou kompatibilitu a rozdělování zdrojů. Umožnilo to koexistenci okruhově spínané hlasové služby a paketově spínaných dat na stejném nosiči. Standardizace v 3GPP Release 5 formalizovala jeho definici, což zajistilo konzistentní implementaci napříč generacemi. Jednoduchost a účinnost SCN z něj učinily trvalý prvek v mobilních komunikacích, který je základním kamenem pro efektivní provoz sítí 2G a ovlivnil pozdější technologie stavějící na metodách přístupu s časovými sloty.

## Klíčové vlastnosti

- Identifikuje konkrétní podkanály v rámci TDMA rádiového kanálu
- Používá se při přiřazování kanálů a v sekvencích pro přeskakování kmitočtů
- Podporuje mapování logických kanálů na fyzické zdroje
- Umožňuje efektivní využití spektra prostřednictvím správy časových slotů
- Klíčový pro systémy GSM, GPRS a EDGE
- Standardizovaný parametr pro interoperabilitu mezi sítí a zařízeními

## Související pojmy

- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)
- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [SCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/scn/)
