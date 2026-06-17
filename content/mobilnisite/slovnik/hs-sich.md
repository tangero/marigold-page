---
slug: "hs-sich"
url: "/mobilnisite/slovnik/hs-sich/"
type: "slovnik"
title: "HS-SICH – Shared Information Channel for HS-DSCH"
date: 2025-01-01
abbr: "HS-SICH"
fullName: "Shared Information Channel for HS-DSCH"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hs-sich/"
summary: "Uplinkový fyzický řídicí kanál v UMTS používaný ve spojení s HSDPA. Přenáší zásadní zpětnou vazbu od UE k Node B, včetně indikátoru kvality kanálu (CQI) a potvrzení HARQ (ACK/NACK), které jsou klíčové"
---

HS-SICH je uplinkový fyzický řídicí kanál v UMTS, který přenáší zpětnou vazbu od UE, jako je CQI a HARQ ACK/NACK, k Node B pro provoz HSDPA.

## Popis

Shared Information Channel for [HS-DSCH](/mobilnisite/slovnik/hs-dsch/) (HS-SICH) je uplinkový protějšek ke kanálu [HS-SCCH](/mobilnisite/slovnik/hs-scch/) v systému UMTS High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)), zavedeném ve 3GPP Release 5. Jde o fyzický kanál přenášený z uživatelského zařízení (UE) k Node B. Primární úlohou HS-SICH je přenášet časově kritické informace zpětné vazby, které umožňují efektivní fungování plánovače a entity Hybrid [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)) v Node B. Tato zpětná vazba je základní součástí uzavřených řídicích smyček, které poskytují HSDPA vysoký výkon a efektivitu.

HS-SICH přenáší dvě klíčové informace: indikátor kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) a potvrzení HARQ ([ACK](/mobilnisite/slovnik/ack/) nebo [NACK](/mobilnisite/slovnik/nack/)). CQI je měření hlášené UE, které indikuje podmínky downlinkového kanálu, které zařízení zažívá. Tato hodnota je vypočítána UE na základě přijímaného poměru signálu k šumu společného pilotního kanálu (CPICH). CQI v podstatě informuje plánovač Node B o tom, jakou modulační schéma a kódovou rychlost může UE spolehlivě podporovat v příštím přenosu, čímž tvoří základ pro adaptivní modulaci a kódování (AMC). HARQ ACK/NACK indikuje, zda byl datový paket přijatý na HS-PDSCH úspěšně dekódován (ACK) nebo ne (NACK), a v případě potřeby spouští retransmisi.

Z architektonického hlediska je HS-SICH vysílán UE po předem definované době po přijetí sub-rámce HS-PDSCH. Toto časování je striktně definováno vzhledem k downlinkovému přenosu HS-SCCH/HS-PDSCH, aby byla zajištěna zpětná vazba s nízkou latencí. Kanál používá rozprostírací faktor 16. Na rozdíl od vyhrazeného kanálu je HS-SICH sdílený prostředek, ale jeho přenos je spuštěn jako odpověď na downlinkové přidělení signalizované na HS-SCCH. Node B musí HS-SICH správně přijmout a interpretovat, aby se rozhodl o parametrech pro další downlinkový přenos (na základě CQI) a spravoval stav procesu HARQ (na základě ACK/NACK).

Jeho fungování je nedílnou součástí smyčky HSDPA. Poté, co UE dekóduje HS-SCCH a přidružená data HS-PDSCH, pokusí se dekódovat transportní blok. Na základě kontroly CRC vygeneruje ACK nebo NACK. Současně změří kvalitu downlinkového kanálu, aby vygenerovala hodnotu CQI. Tyto dvě informace jsou naformátovány, zakódovány a přeneseny na HS-SICH zpět k Node B. Plánovač Node B použije CQI od všech aktivních UE, aby se rozhodl, kterou UE naplánovat příště a s jakou datovou rychlostí. Jeho proces HARQ použije ACK/NACK k vyprázdnění bufferu (při ACK) nebo k přípravě retransmise s redundantní verzí (při NACK). Tato těsná, rychlá zpětnovazební smyčka, umožněná HS-SICH, je tím, co umožňuje HSDPA dosáhnout vysoké spektrální efektivity a robustního výkonu spoje.

## K čemu slouží

HS-SICH byl vytvořen, aby vyřešil klíčové chybějící spojení v architektuře HSDPA: rychlou, spolehlivou uplinkovou zpětnou vazbu. Přesunutí plánování a HARQ k Node B (základní princip HSDPA) vyžadovalo, aby Node B mělo bezprostřední znalost dvou věcí: úspěch nebo neúspěch svého downlinkového přenosu a aktuální kvalitu downlinkového kanálu na straně UE. Stávající signalizační kanály z Release 99 byly příliš pomalé a nebyly navrženy pro zpětnovazební cykly kratší než 2 ms.

Bez vyhrazeného kanálu zpětné vazby s nízkou latencí, jako je HS-SICH, by pokročilé funkce HSDPA nebyly možné. Adaptivní modulace a kódování (AMC) spoléhá na časté a přesné hlášení CQI pro výběr optimální modulace a kódové rychlosti pro aktuální rádiové podmínky. Rychlý proces Hybrid ARQ vyžaduje, aby ACK/NACK byly přijaty s minimálním zpožděním, aby byla udržena krátká doba cyklu procesu HARQ, což umožňuje rychlé retransmise a efektivní využití protokolu stop-and-wait.

HS-SICH vyřešil problém, jak získat tyto kritické informace od UE k Node B v rámci přísného časování 2ms TTI. Poskytl standardizovaný, efektivní fyzický kanál s definovanou strukturou, kódováním a časováním. To umožnilo Node B činit autonomní, informovaná rozhodnutí o plánování každé 2 ms a reagovat na změny kanálu a chyby paketů téměř v reálném čase. Vytvoření HS-SICH spolu s HS-SCCH dokončilo řídicí rovinu s nízkou latencí nezbytnou pro paketově optimalizované rozhraní vzduchu, které HSDPA představovalo.

## Klíčové vlastnosti

- Přenáší uplinkovou zpětnou vazbu pro HSDPA: CQI a HARQ ACK/NACK
- Umožňuje adaptivní modulaci a kódování (AMC) prostřednictvím hlášení CQI
- Umožňuje rychlý Hybrid ARQ s měkkým kombinováním prostřednictvím zpětné vazby ACK/NACK
- Časování přenosu je těsně svázáno s příjmem downlinkového HS-PDSCH
- Používá rozprostírací faktor 16
- Nezbytný pro uzavřenou smyčku plánování Node B a adaptaci spoje

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [HS-SCCH – High Speed Physical Downlink Shared Control Channel](/mobilnisite/slovnik/hs-scch/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [HS-PDSCH – High Speed Physical Downlink Shared Channel](/mobilnisite/slovnik/hs-pdsch/)
- [AMC – Adaptive Modulation and Coding](/mobilnisite/slovnik/amc/)

## Definující specifikace

- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.874** (Rel-11) — HSPA Feedback & Signalling Efficiency for LCR TDD

---

📖 **Anglický originál a plná specifikace:** [HS-SICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/hs-sich/)
