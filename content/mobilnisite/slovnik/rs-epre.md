---
slug: "rs-epre"
url: "/mobilnisite/slovnik/rs-epre/"
type: "slovnik"
title: "RS-EPRE – Reference Signal-Energy Per Resource Element"
date: 2025-01-01
abbr: "RS-EPRE"
fullName: "Reference Signal-Energy Per Resource Element"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rs-epre/"
summary: "RS-EPRE je standardizované měření vysílané energie na jeden zdrojový element pro referenční signály v LTE a NR. Je klíčové pro přesný odhad kanálu, adaptaci spojení a řízení výkonu, což zajišťuje spol"
---

RS-EPRE je standardizované měření vysílané energie na jeden zdrojový element pro referenční signály v LTE a NR, klíčové pro odhad kanálu, adaptaci spojení a řízení výkonu.

## Popis

Reference Signal-Energy Per Resource Element (RS-EPRE) je základní parametr fyzické vrstvy definovaný ve specifikacích 3GPP pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). Kvantifikuje vysílanou energii přidělenou jednomu zdrojovému elementu nesoucímu referenční signál, jako je Cell-Specific Reference Signal ([CRS](/mobilnisite/slovnik/crs/)) v LTE nebo Synchronization Signal Block (SSB) a Channel State Information Reference Signal ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) v NR. RS-EPRE je typicky vyjádřeno relativně k celkovému vysílacímu výkonu buňky nebo konkrétního kanálu, často v decibelech (dB). Toto měření je standardizováno, aby byla zajištěna konzistence napříč síťovým vybavením a implementacemi UE, což umožňuje přesné hodnocení výkonu a interoperabilitu.

V provozu je RS-EPRE klíčové pro přijímací zpracování v UE. Při downlinkovém přenosu základnová stanice (eNodeB v LTE, gNB v NR) vysílá referenční signály se známou úrovní výkonu. UE měří přijímaný výkon těchto signálů a díky znalosti očekávaného RS-EPRE (vysílaného v broadcastu nebo konfigurovaného signalizací vyšší vrstvy) může odhadnout útlum na cestě, interferenci a poměr signál-šum ([SNR](/mobilnisite/slovnik/snr/)) kanálu. Tyto informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) jsou pak použity pro několik klíčových funkcí: přesnou demodulaci datových kanálů poskytnutím fázové a amplitudové reference, zpětnovazební hlášení pro adaptaci spojení (např. doporučení modulačních a kódovacích schémat) a výpočty řízení výkonu pro uplinkové přenosy.

Architektura podporující RS-EPRE zahrnuje jak rádiový přístupový síť, tak schopnosti UE. Specifikace jako 3GPP TS 37.544 (pro testování shody), TS 38.151 (pro rádiový přenos a příjem NR základnové stanice), TS 38.551 (pro shodu NR UE) a TS 38.761 (pro duální konektivitu LTE-NR) definují požadavky na přesnost RS-EPRE, tolerance a měřicí postupy. Klíčové komponenty zahrnují jednotky generování a mapování referenčních signálů ve fyzické vrstvě základnové stanice, výkonový zesilovač zajišťující konzistentní výstup a mechanismy měření a hlášení v UE. Role RS-EPRE je zásadní pro správu rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)), mobilní procedury jako předávání hovoru a celkovou optimalizaci sítě, protože přímo ovlivňuje pokrytí, kapacitu a uživatelský zážitek.

## K čemu slouží

RS-EPRE bylo zavedeno, aby řešilo potřebu standardizované, jednoznačné metriky pro výkon referenčních signálů v systémech LTE a NR. Před jeho formální definicí mohl být výkon referenčního signálu různými dodavateli interpretován odlišně nebo měřen nekonzistentně, což vedlo k problémům s interoperabilitou, suboptimálnímu výkonu sítě a výzvám v testování shody. Definováním RS-EPRE zajistilo 3GPP, že všichni zúčastnění – výrobci zařízení, síťoví operátoři a testovací laboratoře – mají společný referenční bod pro úrovně výkonu, což umožňuje přesný odhad kanálu a spolehlivou komunikaci.

Vytvoření RS-EPRE bylo motivováno rostoucí složitostí technologií [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) a pokročilých anténních systémů v LTE Rel-14 a novějších a později v NR. Tyto technologie se silně spoléhají na přesné informace o stavu kanálu pro beamforming, prostorové multiplexování a koordinaci interference. Nepřesná znalost výkonu referenčního signálu by tyto techniky degradovala, což by snížilo spektrální účinnost a datové rychlosti. RS-EPRE poskytuje konzistentní základnu, která umožňuje UE správně odhadnout podmínky kanálu i v dynamickém prostředí s proměnlivou interferencí a scénáři mobility.

RS-EPRE dále podporuje funkce správy sítě, jako je minimalizace jízdních testů ([MDT](/mobilnisite/slovnik/mdt/)) a samo-organizující se sítě (SON). Standardizací způsobu měření a hlášení výkonu referenčních signálů mohou operátoři sbírat spolehlivá data pro optimalizaci pokrytí, plánování kapacity a detekci chyb. Také usnadňuje scénáře duální konektivity a agregace nosných, kde je koordinace výkonu napříč různými nosnými nebo uzly zásadní pro bezproblémový uživatelský zážitek a efektivní využití zdrojů.

## Klíčové vlastnosti

- Standardizované měření výkonu referenčního signálu na zdrojový element
- Umožňuje přesný odhad kanálu a demodulaci
- Podporuje adaptaci spojení a výběr modulačního/kódovacího schématu
- Nezbytné pro řízení výkonu a časový posun pro uplink
- Usnadňuje optimalizaci výkonu MIMO a beamformingu
- Používá se v RRM procedurách, jako je výběr buňky a předávání hovoru

## Související pojmy

- [CRS – Cell-specific Reference Signals](/mobilnisite/slovnik/crs/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [RRM – Radio Resource Management](/mobilnisite/slovnik/rrm/)

## Definující specifikace

- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE

---

📖 **Anglický originál a plná specifikace:** [RS-EPRE na 3GPP Explorer](https://3gpp-explorer.com/glossary/rs-epre/)
