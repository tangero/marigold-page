---
slug: "ir"
url: "/mobilnisite/slovnik/ir/"
type: "slovnik"
title: "IR – Incremental Redundancy"
date: 2025-01-01
abbr: "IR"
fullName: "Incremental Redundancy"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ir/"
summary: "Incremental Redundancy (IR) je technika Hybrid Automatic Repeat reQuest (HARQ) používaná v bezdrátové komunikaci ke zvýšení spolehlivosti přenosu a spektrální účinnosti. Při opakovaných přenosech vysí"
---

IR je technika HARQ, která zvyšuje spolehlivost a spektrální účinnost vysíláním dodatečných paritních bitů při opakovaných přenosech, které přijímač kombinuje pro dekódování dat.

## Popis

Incremental Redundancy je základní součástí procesu Hybrid [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)) v systémech 3GPP, jako jsou LTE a NR. Funguje tak, že nejprve přenese datový blok s určitou úrovní kanálového kódování (např. s mateřskou kódovou rychlostí). Pokud přijímač tento počáteční přenos nedekóduje a odešle záporné potvrzení ([NACK](/mobilnisite/slovnik/nack/)), vysílač nevyšle znovu stejná data. Místo toho odešle jinou, doplňkovou sadu kódovaných bitů, známých jako redundantní verze (RVs). Tyto RVs obsahují dodatečné paritní bity vygenerované ze stejného původního datového bloku, ale s odlišným punkturováním. Přijímač ukládá měkké bity (log-likelihood poměry) z neúspěšného přenosu do vyrovnávací paměti. Po přijetí opakovaného přenosu kombinuje tyto nové měkké bity s uloženými, čímž efektivně vytváří celkově nižší kódovou rychlost a robustnější složené kódové slovo. Tento proces Chase Combining nebo Incremental Redundancy pokračuje, dokud nejsou data úspěšně dekódována nebo není dosaženo maximálního počtu opakovaných přenosů.

Architektura podporující IR je integrována v rámci funkcí kanálového kódování a správy HARQ fyzické vrstvy. Mezi klíčové komponenty patří entita HARQ na straně vysílače i přijímače, která spravuje více paralelních HARQ procesů pro kontinuální tok dat; generátor redundantních verzí ([RV](/mobilnisite/slovnik/rv/)), který vybírá konkrétní vzorek systematických a paritních bitů k přenosu; a vyrovnávací paměť pro měkké bity na straně přijímače pro ukládání a kombinaci log-likelihood poměrů. eNodeB/gNB plánuje přenosy a opakované přenosy, zatímco UE provádí dekódování a kombinaci. Konkrétní kódovací schéma, jako jsou Turbo kódy v LTE nebo [LDPC](/mobilnisite/slovnik/ldpc/)/Polar kódy v NR, definuje mateřský kód a pravidla pro generování různých RVs.

Role IR je klíčová pro adaptaci spoje a robustní doručování dat přes nespolehlivé rádiové kanály. Postupným vysíláním většího množství paritních informací umožňuje systému přizpůsobit efektivní kódovou rychlost aktuálním podmínkám kanálu. Za dobrých podmínek může stačit počáteční přenos, což maximalizuje propustnost. Za špatných podmínek akumulovaná redundance z více přenosů poskytuje silnou korekci chyb. Díky tomu je IR vysoce účinná, neboť se vyhýbá plýtvání šířkou pásma na úplné opakované přenosy již přijatých informací. Je klíčovým prvkem pro dosažení vysokých přenosových rychlostí a nízké latence s vysokou spolehlivostí, zejména pro řídicí kanály a datové kanály v náročných rádiových prostředích.

## K čemu slouží

Incremental Redundancy byla vytvořena, aby řešila základní výzvu efektivního a spolehlivého přenosu dat přes náchylné k chybám bezdrátové kanály. Tradiční schémata [ARQ](/mobilnisite/slovnik/arq/), která zahazují neúspěšné pakety a vyžadují identické opakované přenosy, jsou neefektivní z hlediska využití spektra a zpoždění. Účelem IR je vylepšit proces Hybrid ARQ tím, že každý opakovaný přenos učiní hodnotnějším než pouhé opakování. Řeší problém plýtvání šířkou pásma vysíláním nových, doplňujících informací s každým opakovaným přenosem, čímž zvyšuje pravděpodobnost úspěšného dekódování s každým pokusem.

Historicky, před sofistikovaným [HARQ](/mobilnisite/slovnik/harq/) s IR, systémy spoléhaly na jednodušší opakované kódování nebo ARQ s Chase combining (který opakuje stejné bity). Tyto metody byly méně spektrálně účinné. IR, zavedená jako klíčová součást HARQ v 3GPP Rel-8 pro LTE, představovala významný vývoj. Byla motivována potřebou vyšších přenosových rychlostí a lepšího výkonu na okrajích buněk v nově vznikajících systémech založených na [OFDMA](/mobilnisite/slovnik/ofdma/). Tím, že umožňuje přijímači kombinovat různé části stejného kódovaného paketu, IR efektivně vytváří silnější kód pro opravu chyb s nižší rychlostí za běhu, přizpůsobuje se podmínkám kanálu bez nutnosti explicitní signalizace ke změně počátečního schématu modulace a kódování (MCS).

Tato technika je zásadní pro splnění požadavků na kvalitu služeb (QoS) pro různé služby. Zlepšuje propustnost a snižuje latenci pro paketové datové služby minimalizací potřebného počtu opakovaných přenosů a zvýšením účinnosti každého z nich. V pozdějších verzích, jako je NR (Rel-15), zůstává IR základním kamenem, nyní aplikovaným na nová schémata kanálového kódování jako LDPC pro data, což zajišťuje pokračující zisky ve spektrální účinnosti a spolehlivosti pro různorodé případy užití 5G, od rozšířeného mobilního širokopásmového připojení až po ultra-spolehlivou komunikaci s nízkou latencí.

## Klíčové vlastnosti

- Při opakovaných přenosech vysílá doplňkové redundantní verze (RVs), nikoli identická data
- Umožňuje měkké kombinování log-likelihood poměrů (LLRs) na straně přijímače
- Dynamicky přizpůsobuje efektivní kódovou rychlost na základě podmínek kanálu
- Integrována s paralelními HARQ procesy pro kontinuální zpracování dat v řetězci
- Funguje s různými kanálovými kódy (Turbo v LTE, LDPC/Polar v NR)
- Snižuje celkový počet přenosů potřebných pro úspěšné dekódování

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [LDPC – Low-Density Parity-Check](/mobilnisite/slovnik/ldpc/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [IR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ir/)
