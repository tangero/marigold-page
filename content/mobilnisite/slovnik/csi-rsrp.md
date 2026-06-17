---
slug: "csi-rsrp"
url: "/mobilnisite/slovnik/csi-rsrp/"
type: "slovnik"
title: "CSI-RSRP – Channel State Information Reference Signal Received Power"
date: 2025-01-01
abbr: "CSI-RSRP"
fullName: "Channel State Information Reference Signal Received Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/csi-rsrp/"
summary: "CSI-RSRP je měření fyzické vrstvy přijatého výkonu z referenčních signálů pro informace o stavu kanálu (CSI-RS) v 5G NR. Kvantifikuje sílu signálu specifických beamformovaných referenčních signálů pou"
---

CSI-RSRP je měření fyzické vrstvy přijatého výkonu z referenčních signálů pro informace o stavu kanálu (Channel State Information Reference Signals) v 5G NR, které kvantifikuje sílu beamformovaného signálu pro odhad kanálu, správu paprsků a mobilitu.

## Popis

CSI-RSRP je měření vrstvy 1 definované ve specifikacích 3GPP 38.214 a 38.215 pro New Radio (NR). Představuje lineární průměr přes příspěvky výkonu prvků prostředků, které nesou referenční signály [CSI](/mobilnisite/slovnik/csi/) v uvažované měřené frekvenční šířce pásma. Na rozdíl od SS-RSRP, které měří bloky synchronizačních signálů, CSI-RSRP specificky měří referenční signály nakonfigurované pro získávání informací o stavu kanálu, což umožňuje přesnější měření specifická pro jednotlivé paprsky.

Postup měření zahrnuje UE, které měří přijatý výkon nakonfigurovaných prostředků [CSI-RS](/mobilnisite/slovnik/csi-rs/), jež mohou být vysílány z gNB v různých prostorových směrech (paprscích). UE provádí měření výkonu na určených prvcích prostředků CSI-RS, aplikuje specifikované filtrování a průměrování. Šířka pásma měření může být konfigurována na prostředek CSI-RS, což umožňuje flexibilní granularitu měření. Měření CSI-RSRP jsou hlášena síti prostřednictvím mechanismů hlášení vrstvy 1 nebo vrstvy 3 a podporují periodické i událostmi spouštěné hlášení.

Z architektonického hlediska CSI-RSRP funguje v rámci měřicího rámce fyzické vrstvy, kde fyzická vrstva UE zpracovává přijaté symboly CSI-RS, extrahuje sekvence referenčních signálů a vypočítává přijatý výkon. Měření zohledňuje konfigurace specifické pro anténní porty a podporuje měření z více vysílacích anténních portů. Mezi klíčové komponenty patří konfigurace prostředku CSI-RS (definující časově-frekvenční vzory), konfigurace časování měření a konfigurace hlášení, které určují, kdy a jak jsou měření hlášena vyšším vrstvám.

V provozu sítě plní CSI-RSRP několik kritických funkcí. Pro správu paprsků umožňuje gNB určit nejlepší páry vysílacích/přijímacích paprsků porovnáním měření CSI-RSRP z různých prostředků CSI-RS vysílaných na různých paprscích. Pro mobilitu poskytuje měření kvality signálu specifická pro paprsky, která doplňují měření na úrovni buňky a umožňují přesnější rozhodování o předání spojení v beamformovaných sítích. Pro adaptaci spoje pomáhá odhadnout kvalitu kanálu pro specifické konfigurace přenosu, podporuje výběr vrstev [MIMO](/mobilnisite/slovnik/mimo/) a adaptaci schémat modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)).

## K čemu slouží

CSI-RSRP bylo zavedeno v 5G NR Release 15, aby řešilo omezení stávajících měření referenčních signálů v beamformovaných systémech. Předchozí systémy LTE primárně používaly měření RSRP založená na [CRS](/mobilnisite/slovnik/crs/) (Cell-specific Reference Signal), která byla vysílána v celé oblasti pokrytí buňky. V nasazeních 5G s masivním [MIMO](/mobilnisite/slovnik/mimo/) a beamformingem však vysílané referenční signály nemohou poskytnout přesné informace o kvalitě kanálu specifické pro paprsek, potřebné pro optimální správu paprsků a mobilitu.

Technologie řeší problém přesného měření síly signálu pro specifické beamformované přenosy. Ve scénářích beamformingu mají různé paprsky různé vzory pokrytí a kvality signálu, což vyžaduje měření specifická pro paprsek pro efektivní výběr paprsku a předání spojení. CSI-RSRP umožňuje přesné měření kvality kanálu, kterou zažívají referenční signály specifické pro UE nebo pro paprsek, což je nezbytné pro procedury správy paprsků včetně průchodu paprsky, měření paprsků a hlášení paprsků.

Historický kontext ukazuje, že dřívější systémy postrádaly schopnosti měření specifická pro paprsek. Měření RSRP v LTE byla celobuněčná a nepodporovala granularitu na úrovni paprsku. Zavedení CSI-RSRP v 5G NR bylo motivováno potřebou podporovat pokročilé funkce správy paprsků, operace masivního MIMO a nasazení milimetrových vln, kde je beamforming klíčový pro pokrytí a kapacitu. Řeší omezení SS-RSRP, které, ač užitečné pro počáteční přístup, neposkytuje přesnost specifickou pro paprsek potřebnou pro průběžnou správu paprsků a mobilitu v hustých beamformovaných sítích.

## Klíčové vlastnosti

- Měření výkonu specifické pro paprsek pro prostředky CSI-RS
- Konfigurovatelná šířka pásma měření na prostředek CSI-RS
- Podpora měření z více anténních portů
- Mechanismy hlášení vrstvy 1 a vrstvy 3
- Flexibilní časové okamžiky měření
- Integrace s procedurami správy paprsků

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.215** (Rel-19) — NR Physical Layer Measurements

---

📖 **Anglický originál a plná specifikace:** [CSI-RSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/csi-rsrp/)
