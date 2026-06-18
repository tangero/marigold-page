---
slug: "l1-rsrp"
url: "/mobilnisite/slovnik/l1-rsrp/"
type: "slovnik"
title: "L1-RSRP – Layer 1 Reference Signal Received Power"
date: 2025-01-01
abbr: "L1-RSRP"
fullName: "Layer 1 Reference Signal Received Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/l1-rsrp/"
summary: "Měření fyzické vrstvy prováděné UE nebo gNB na specifických referenčních signálech (např. SSB, CSI-RS) pro odhad přijatého výkonu signálu. Je to kritický vstup pro správu rádiových zdrojů, rozhodování"
---

L1-RSRP je měření fyzické vrstvy přijatého výkonu signálu ze specifických referenčních signálů, používané pro rozhodování o mobilitě, správu paprsků a správu rádiových zdrojů v 5G NR.

## Popis

L1-RSRP (Layer 1 Reference Signal Received Power) je základní rádiové měření definované v 3GPP pro 5G New Radio (NR) a dále rozvíjené v pozdějších vydáních. Představuje lineární průměr výkonových příspěvků prvků zdroje, které nesou buňkově specifické referenční signály v rámci určené měřicí šířky pásma. Na rozdíl od měření filtrovaných na vyšších vrstvách je L1-RSRP měření fyzické vrstvy, což znamená, že je prováděno přímo na přijatých symbolech před rozsáhlým zpracováním a filtrací ve vrstvě 2. UE měří L1-RSRP na referenčních signálech, jako je blok synchronizačního signálu (SSB) pro počáteční výběr buňky a mobilitu, nebo referenční signál pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) pro přesnější měření na úrovni paprsků a hlášení stavu kanálu.

Postup měření zahrnuje řetězec zpracování fyzické vrstvy UE. Po synchronizaci a [OFDM](/mobilnisite/slovnik/ofdm/) demodulaci přijímač identifikuje prvky zdroje přidělené specifickým sekvencím referenčních signálů. Následně vypočítá přijatý výkon pro tyto prvky, typicky průměruje výsledky přes více symbolů a subnosičů, aby zmírnil účinky rychlého útlumu a šumu. Výsledek je interně hlásán vyšším vrstvám (např. vrstvě [RRC](/mobilnisite/slovnik/rrc/)) jako surové měření, které může být následně filtrováno (a stát se L3-RSRP) pro použití v událostech jako je spouštění předání hovoru. V kontextu správy paprsků může UE měřit L1-RSRP na více paprscích CSI-RS vysílaných gNB a hlásit nejlepší paprsky, což síti umožňuje vybrat optimální pár paprsků pro vysílání/příjem.

L1-RSRP je specifikováno s přísnými požadavky na přesnost v konformačních testovacích specifikacích (např. 38.133). Jeho hodnota je hlášena v dBm a je klíčová pro několik síťových funkcí. Slouží jako primární metrika pro výběr a převýběr buňky ve stavech idle/inactive. Během připojeného stavu je používáno pro vyhodnocení předání hovoru a monitorování rádiového spoje (pro detekci selhání rádiového spoje). V paprskově orientovaném provozu 5G jsou měření L1-RSRP na zdrojích CSI-RS základem pro procedury detekce a obnovy selhání paprsku, stejně jako pro určení nejlepšího paprsku pro přenos [PDCCH](/mobilnisite/slovnik/pdcch/) a [PDSCH](/mobilnisite/slovnik/pdsch/).

## K čemu slouží

L1-RSRP bylo zavedeno za účelem poskytnutí rychlého, přesného a detailního měření síly signálu speciálně přizpůsobeného pokročilým funkcím 5G NR. Předchozí technologie jako LTE používaly [RSRP](/mobilnisite/slovnik/rsrp/), ale 5G L1-RSRP je navrženo tak, aby řešilo výzvy vyšších frekvencí (včetně mmWave), massive [MIMO](/mobilnisite/slovnik/mimo/) a beamformingu. Problém, který řeší, je potřeba včasného a přesného hodnocení kvality signálu pro správu paprsků, což je kritické pro udržení spolehlivého připojení v prostředích s vysokým útlumem na dráze šíření a dynamickými překážkami.

Motivace pro specifikaci L1-RSRP samostatně vychází z potřeby měření s nízkou latencí pro podporu rychlého přepínání paprsků a mobility v 5G. Beamforming, zejména na milimetrových vlnách, vytváří úzké, směrové paprsky, které se mohou rychle měnit s pohybem uživatele. Síť vyžaduje častá a přesná měření výkonu na těchto jednotlivých paprscích, aby mohla činit rychlá rozhodnutí o správě paprsků. L1-RSRP poskytuje tento surový, nefiltrovaný datový bod přímo z fyzické vrstvy, což umožňuje rychlejší reakční časy ve srovnání s více filtrovanými měřeními vrstvy 3. Je to základní prvek umožňující spolehlivost a vysokou propustnost slibovanou technologií 5G NR.

## Klíčové vlastnosti

- Měření prováděné přímo na referenčních signálech fyzické vrstvy (SSB, CSI-RS)
- Poskytuje lineární průměrný výkon prvků zdroje referenčního signálu
- Kritický vstup pro správu paprsků a procedury obnovy po selhání paprsku
- Používá se pro rozhodování o výběru buňky, převýběru a předání hovoru
- Definováno s přísnými požadavky na přesnost pro konformační testování
- Podporuje měření na synchronizačních i referenčních signálech stavu kanálu

## Související pojmy

- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface

---

📖 **Anglický originál a plná specifikace:** [L1-RSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/l1-rsrp/)
