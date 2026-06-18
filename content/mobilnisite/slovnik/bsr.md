---
slug: "bsr"
url: "/mobilnisite/slovnik/bsr/"
type: "slovnik"
title: "BSR – Buffer Status Report"
date: 2025-01-01
abbr: "BSR"
fullName: "Buffer Status Report"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bsr/"
summary: "Řídicí prvek vrstvy MAC vysílaný UE k obsluhujícímu gNB/eNB pro hlášení množství dat uložených v bufferu pro uplink přenos. Jedná se o klíčový mechanismus pro plánování uplinku, který umožňuje síti ef"
---

BSR je řídicí prvek vrstvy MAC vysílaný UE k obsluhující základnové stanici, který hlásí množství dat uložených v bufferu pro uplink, což umožňuje efektivní alokaci síťových zdrojů pro plánování.

## Popis

Buffer Status Report (BSR) je řídicí prvek (control element) datové jednotky protokolu Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) definovaný ve specifikacích 3GPP pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). Jeho hlavní funkcí je poskytnout síti (konkrétně gNB v 5G NR nebo [eNB](/mobilnisite/slovnik/enb/) v 4G LTE) informaci o množství dat pro uplink čekajících na přenos v bufferech UE, členěnou podle skupin logických kanálů (Logical Channel Groups, [LCG](/mobilnisite/slovnik/lcg/)). Tato informace je zásadní pro síťový plánovač uplinku, aby mohl činit inteligentní rozhodnutí o alokaci zdrojů (Resource Blocks, [RB](/mobilnisite/slovnik/rb/)). Mechanismus BSR funguje uvnitř podsložky MAC protokolového zásobníku UE. Když data dorazí do vrstvy Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) UE pro logický kanál, jsou uložena v odpovídajících bufferech. Vrstva MAC tyto buffery monitoruje a spouští generování BSR za specifických podmínek definovaných standardizovanými spouštěcími událostmi.

Z architektonického hlediska je BSR přenášen jako MAC Control Element ([CE](/mobilnisite/slovnik/ce/)), který je multiplexován s MAC Service Data Units ([SDU](/mobilnisite/slovnik/sdu/)) z vyšších vrstev za účelem vytvoření MAC PDU pro přenos na Uplink Shared Channel (UL-SCH). Pro optimalizaci signalizační režie a rychlosti reakce jsou definovány různé typy BSR: Pravidelný BSR (Regular BSR), Periodický BSR (Periodic BSR) a Výplňový BSR (Padding BSR). Pravidelný BSR je spuštěn, když se pro logický kanál stanou dostupná uplink data, která mají vyšší prioritu než ta, která jsou aktuálně dostupná na jiných kanálech, nebo když nejsou dostupná žádná data pro žádný logický kanál a poté data dorazí (to spustí BSR pro 'prázdný buffer'). Periodický BSR je spuštěn vypršením časovače (periodicBSR-Timer), což zajišťuje, že síť dostává aktualizace i během trvalého datového toku. Výplňový BSR je spuštěn, když má UE přiděleny uplink zdroje, ale množství výplňových bitů potřebných k zaplnění transportního bloku by bylo dostatečné k přenosu BSR MAC CE, což umožňuje efektivní využití přidělených zdrojů.

Obsah BSR MAC CE zahrnuje pole Buffer Size pro každou nakonfigurovanou skupinu logických kanálů (LCG). V LTE a NR může být nakonfigurováno až 8 LCG (0-7), ačkoli typicky se používají 4. Buffer Size udává celkové množství dat dostupných napříč všemi logickými kanály patřícími do dané LCG, včetně dat dostupných pro přenos ve vrstvách RLC a PDCP. Hlášená hodnota je index mapovaný na rozsah bajtů (např. 0 bajtů, 1-10 bajtů, 11-20 bajtů atd.), jak je definováno v přehledové tabulce ve specifikacích (TS 36.321, 38.321). Tato kvantizace snižuje signalizační režii. Po přijetí BSR používá plánovač gNB/eNB tuto informaci spolu s dalšími faktory, jako je kvalita kanálu UE (CQI), požadavky QoS přenosů a celkové zatížení buňky, k rozhodnutí o velikosti, načasování a frekvenci uplink povolení (přes Uplink Grant ve formátu DCI 0_1 v NR nebo DCI 0 v LTE) zasílaných UE na Physical Downlink Control Channel (PDCCH).

Procedura BSR je úzce provázána s dalšími procedurami MAC, jako je Prioritizace logických kanálů (Logical Channel Prioritization, LCP), která určuje, která data z kterého logického kanálu budou umístěna do MAC PDU po obdržení povolení. Klíčový časovač `retxBSR-Timer` zajišťuje spolehlivost; pokud je BSR spuštěn, ale UE nemá uplink zdroje k jeho odeslání, spustí proceduru Scheduling Request (SR). Pokud SR není úspěšná před vypršením časovače, je BSR znovu spuštěn. Tato uzavřená smyčka zpětné vazby mezi hlášením stavu bufferu UE a síťovým plánováním je zásadní pro dynamický a efektivní provoz uplinku v LTE i 5G NR, což umožňuje podporu různých typů provozu od paketů s nízkou latencí po datové toky s vysokou propustností.

## K čemu slouží

BSR byl zaveden k vyřešení základního problému efektivní alokace uplink zdrojů v systému se sdíleným kanálem, jako je LTE a NR. V dřívějších celulárních systémech (např. 3G WCDMA) byly uplink přenosy plánovány kódově nebo na bázi soutěžení, což mohlo vést k neefektivitám při dynamickém zatížení provozem. Přechod na OFDMA/SC-FDMA v LTE vyžadoval sofistikovanější, povoleními řízený uplink, kde síť musí UE explicitně říci, kdy a na jakých zdrojích má vysílat. Aby to bylo efektivní, potřebuje síťový plánovač přesné a včasné informace o přenosových potřebách každé UE. Bez mechanismu podobného BSR by síť musela zdroje přidělovat naslepo, což by je buď plýtvalo (nadměrné přidělení), nebo způsobilo nadměrné zpoždění ve frontách (nedostatečné přidělení), což by vážně ovlivnilo QoS, latenci a celkovou kapacitu systému.

Vytvoření mechanismu BSR bylo motivováno potřebou podporovat různé požadavky QoS a velikosti paketů vlastní službám založeným na IP. Aplikace generují trhavý, nepředvídatelný provoz. Statická nebo čistě periodická alokace povolení se této variabilitě nedokáže přizpůsobit. BSR poskytuje zásadní zpětnou vazbu pro dynamické plánování, což síti umožňuje přidělovat zdroje 'na požádání'. To je obzvláště kritické pro služby s přísnými limity latence (např. VoIP, hraní her), kde musí být data přenesena okamžitě po příchodu, a pro služby best-effort, kde má být propustnost maximalizována, když jsou data dostupná. BSR je tedy základním kamenem pro umožnění paketově orientované, plně IP architektury plánované pro 4G a 5G, což znamená odklon od přepojování okruhů, které bylo typické pro předchozí generace.

Dále návrh BSR řeší kompromis mezi přesností hlášení a signalizační režii. Seskupením logických kanálů do LCG a použitím kvantizovaných úrovní velikosti bufferu minimalizuje bitovou délku hlášení. Různé typy spouštěčů (Pravidelný, Periodický, Výplňový) optimalizují různé scénáře: okamžitá potřeba, periodické aktualizace a příležitostné hlášení. Tento elegantní návrh zajišťuje, že smyčka plánování uplinku je jak rychle reagující, tak efektivní, což je klíčový faktor pro dosažení vysoké spektrální účinnosti a nízké latence, které jsou cílem systémů LTE a NR.

## Klíčové vlastnosti

- Hlásí obsazenost bufferu pro uplink podle skupiny logických kanálů (LCG) plánovači gNB/eNB
- Přenášen jako MAC Control Element (CE) na UL-SCH
- Definuje více typů spouštěčů: Pravidelný, Periodický a Výplňový BSR pro optimální signalizaci
- Používá kvantizované indexy velikosti bufferu pro minimalizaci režie
- Integruje se s procedurou Scheduling Request (SR) pro získání zdrojů při potřebě
- Zásadní pro dynamické plánování uplinku umožňující alokaci zdrojů s ohledem na QoS

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.842** (Rel-12) — Small Cell Enhancements for LTE Higher Layers
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification

---

📖 **Anglický originál a plná specifikace:** [BSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/bsr/)
