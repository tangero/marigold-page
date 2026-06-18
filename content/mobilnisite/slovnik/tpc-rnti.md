---
slug: "tpc-rnti"
url: "/mobilnisite/slovnik/tpc-rnti/"
type: "slovnik"
title: "TPC-RNTI – Transmit Power Control Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "TPC-RNTI"
fullName: "Transmit Power Control Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tpc-rnti/"
summary: "Specifický RNTI používaný v LTE k adresování a identifikaci UE za účelem přenosu příkazů řízení vysílacího výkonu (Transmit Power Control) prostřednictvím PDCCH. Umožňuje síťové řízení výkonu pro upli"
---

TPC-RNTI je specifický Radio Network Temporary Identifier (dočasný identifikátor rádiové sítě) používaný v LTE k adresování UE pro přenos příkazů řízení vysílacího výkonu (Transmit Power Control) prostřednictvím PDCCH, což umožňuje síťové řízení výkonu v uplinku.

## Popis

Transmit Power Control Radio Network Temporary Identifier (TPC-RNTI) je typ Radio Network Temporary Identifier definovaný ve specifikacích 3GPP LTE, především v TS 36.331 (protokol Radio Resource Control). [RNTI](/mobilnisite/slovnik/rnti/) je jedinečný identifikátor přiřazený UE nebo skupině UE pro adresování řídicích informací na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). TPC-RNTI se konkrétně používá k předávání příkazů řízení vysílacího výkonu (Transmit Power Control) k UE pro úpravu jejich vysílacího výkonu v uplinku na Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)) a/nebo Physical Uplink Control Channel ([PUCCH](/mobilnisite/slovnik/pucch/)). Na rozdíl od UE-specifických RNTI, jako je [C-RNTI](/mobilnisite/slovnik/c-rnti/), lze TPC-RNTI nakonfigurovat tak, aby adresovalo více UE ve skupině, což umožňuje efektivní vysílání (broadcast) nebo skupinové vysílání (multicast) příkazů řízení výkonu.

Provozně je TPC-RNTI konfigurováno eNodeB prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/), typicky během nastavení nebo rekonfigurace spojení. eNodeB používá toto RNTI k zamíchání (scramble) kontrolního součtu [CRC](/mobilnisite/slovnik/crc/) (Cyclic Redundancy Check) formátu Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)), který nese TPC příkazy. UE monitorují PDCCH pro formáty DCI zamíchané s jejich přiřazeným TPC-RNTI. Po detekci dekódují DCI, aby extrahovaly TPC příkaz, což je bitové pole udávající absolutní nebo relativní úpravu výkonu. UE následně tuto úpravu aplikuje na svůj vysílací výkon v uplinku pro příslušný kanál (kanály). Tento mechanismus je součástí uzavřené smyčky řízení výkonu (closed-loop power control) pro PUSCH a PUCCH, která doplňuje odhady otevřené smyčky (open-loop), aby bylo zajištěno, že přijímaný výkon na eNodeB dosáhne cílové úrovně navzdory změnám útlumu na trase a interferencím.

TPC-RNTI hraje klíčovou roli v architektuře řízení výkonu v uplinku LTE, která zahrnuje komponenty jako algoritmus řízení výkonu eNodeB, funkci výpočtu výkonu UE a PDCCH pro doručení příkazu. Jeho použití je zvláště důležité ve scénářích s dynamickým plánováním a sdílenými zdroji kanálů, kde přesné řízení výkonu minimalizuje interferenci do jiných buněk a zlepšuje kapacitu systému. TPC-RNTI se liší od jiných RNTI, jako je SI-RNTI (pro systémové informace) nebo P-RNTI (pro paging), protože je vyhrazeno pro signalizaci řízení výkonu. Jeho konfigurace a správa jsou řešeny vrstvou RRC, což zajišťuje, že UE správně interpretují příkazy řízení výkonu určené pro ně, a tím udržují kvalitu uplinku a efektivitu sítě.

## K čemu slouží

TPC-RNTI bylo zavedeno v LTE (Release 8), aby poskytlo standardizovaný a efektivní mechanismus pro síťově řízenou úpravu výkonu v uplinku. V předchozích systémech, jako UMTS, byly příkazy řízení výkonu vloženy do vyhrazených fyzických kanálů, ale architektura se sdílenými kanály v LTE vyžadovala flexibilnější přístup. TPC-RNTI umožňuje eNodeB odesílat příkazy řízení výkonu k UE prostřednictvím společného PDCCH, které monitorují všechna aktivní UE, což umožňuje dynamické a UE-specifické nebo skupinově-specifické úpravy výkonu bez režie vyhrazené signalizace.

Tento identifikátor řeší problém, jak efektivně spravovat výkon v uplinku v systému založeném na OFDMA, kde více UE sdílí časově-frekvenční zdroje. Použitím TPC-RNTI může síť rychle přizpůsobit vysílací výkon UE měnícím se rádiovým podmínkám, čímž snižuje mezibuněčnou interferenci a zlepšuje celkovou spektrální účinnost. Také pomáhá šetřit výdrž baterie UE tím, že zabraňuje zbytečnému nadměrnému vysílání. Vytvoření vyhrazeného RNTI pro tento účel odráží konstrukční princip LTE oddělovat řídicí a uživatelskou rovinu pomocí efektivních identifikátorů, což umožňuje škálovatelné a robustní řízení výkonu, nezbytné pro vysoký výkon cílů 4G a dalších generací.

## Klíčové vlastnosti

- Jedinečný identifikátor pro adresování TPC příkazů na PDCCH
- Konfigurovatelný prostřednictvím signalizace RRC pro UE nebo skupinu UE
- Používá se k zamíchání (scramble) CRC formátů DCI nesoucích TPC bity
- Podporuje uzavřenou smyčku řízení výkonu (closed-loop power control) pro PUSCH a PUCCH
- Umožňuje síti dynamicky upravovat výkon v uplinku
- Snižuje interferenci v uplinku a optimalizuje spotřebu výkonu UE

## Související pojmy

- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [TPC-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpc-rnti/)
