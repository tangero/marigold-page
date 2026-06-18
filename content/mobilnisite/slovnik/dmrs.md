---
slug: "dmrs"
url: "/mobilnisite/slovnik/dmrs/"
type: "slovnik"
title: "DMRS – Dedicated Demodulation Reference Signals"
date: 2025-01-01
abbr: "DMRS"
fullName: "Dedicated Demodulation Reference Signals"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dmrs/"
summary: "Dedicated Demodulation Reference Signals (DMRS) jsou předdefinované signály vestavěné do prostředků fyzického kanálu v 5G NR a LTE-Advanced, které napomáhají odhadu kanálu pro demodulaci dat. Jsou 'vy"
---

DMRS je vyhrazený referenční signál vestavěný do fyzického kanálu pro konkrétní UE, který umožňuje přesný odhad kanálu pro demodulaci dat v systémech 5G NR a LTE-Advanced.

## Popis

Dedicated Demodulation Reference Signals (DMRS) jsou kategorií referenčních signálů používaných v rozhraních 3GPP 5G New Radio (NR) a vyvinutého LTE (LTE-Advanced). Jejich hlavní funkcí je poskytnout známý signálový vzor, který uživatelské zařízení (UE) a gNodeB (gNB) nebo eNodeB ([eNB](/mobilnisite/slovnik/enb/)) mohou použít k odhadu podmínek rádiového kanálu za účelem demodulace přijímaných dat. Na rozdíl od referenčních signálů specifických pro buňku ([CRS](/mobilnisite/slovnik/crs/) v LTE) jsou DMRS specifické pro UE – jsou vysílány pouze v časově-frekvenčních prostředcích přidělených fyzickému downlinkovému sdílenému kanálu ([PDSCH](/mobilnisite/slovnik/pdsch/)) nebo fyzickému uplinkovému sdílenému kanálu ([PUSCH](/mobilnisite/slovnik/pusch/)) daného konkrétního UE. Tato vyhrazená povaha snižuje režii a zvyšuje kapacitu sítě.

DMRS je multiplexován s uživatelskými daty ve stejném bloku fyzických prostředků ([PRB](/mobilnisite/slovnik/prb/)). V downlinku vysílá DMRS gNB a UE jej používá k odhadu kanálu pro demodulaci doprovodných dat PDSCH. V uplinku vysílá DMRS UE a gNB jej používá k demodulaci PUSCH. Signálový vzor je definován sekvencí referenčního signálu, která je generována na základě parametrů, jako je identifikátor fyzické buňky ([PCI](/mobilnisite/slovnik/pci/)), číslo slotu a scrambling identita specifická pro UE. To zajišťuje ortogonalitu mezi DMRS pro různá UE nebo různé vrstvy v [MIMO](/mobilnisite/slovnik/mimo/) přenosu. Struktura DMRS v NR je vysoce flexibilní, s konfigurovatelnou hustotou v časové doméně (front-loaded nebo další symboly) a ve frekvenční doméně, aby vyhovovala různým podmínkám kanálu a scénářům mobility.

Klíčovými součástmi architektury DMRS jsou konfigurace DMRS signalizovaná přes řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a downlinkovou řídicí informaci (DCI), generátor sekvence referenčního signálu a mapování na konkrétní prvky prostředků (RE) v rámci mřížky prostředků. Jeho role je zásadní pro fungování pokročilých funkcí fyzické vrstvy. Poskytnutím přesných, okamžitých odhadů kanálu umožňují DMRS použití modulačních schémat vysokého řádu (např. 256QAM, 1024QAM) a vícevrstvého prostorového multiplexování (MIMO), které jsou nezbytné pro dosažení vysokých datových rychlostí a cílů spektrální účinnosti 5G. Konstrukce také podporuje beamforming, protože DMRS je vysílán stejným předkódovaným paprskem jako data, což přijímači umožňuje odhadnout efektivní kanál po předkódování.

## K čemu slouží

DMRS byly zavedeny, aby překonaly omezení architektury společného referenčního signálu (CRS) používané v raných vydáních LTE. CRS byly vysílány nepřetržitě přes celou šířku pásma buňky a pro všechny anténní porty, což vytvářelo významnou režii omezující spektrální účinnost, zejména s rostoucím počtem anténních portů pro MIMO. CRS také nebyly beamformované, což je činilo neefektivními pro beam-centric design 5G NR. Hlavní motivací pro DMRS bylo vytvořit schéma referenčního signálu, které se efektivně škáluje s pokročilými anténními systémy (Massive MIMO) a beamformingem.

Vytvoření vyhrazených, pro UE specifických referenčních signálů řeší problém režie a umožňuje efektivnější podporu multi-user MIMO (MU-MIMO) a operací s více paprsky. Protože jsou DMRS vysílány pouze tehdy a tam, kde jsou naplánována uživatelská data, a jsou předkódovány spolu s daty, je režie přímo úměrná počtu aktivních UE a vrstev, nikoli celkovému počtu anténních portů buňky. To je klíčovým prvkem pro Massive MIMO, kde může mít základnová stanice desítky nebo stovky anténních prvků. Konfigurovatelná povaha DMRS v NR navíc umožňuje síti vyvažovat mezi režií referenčního signálu a přesností odhadu kanálu na základě rychlosti UE a podmínek kanálu, čímž dynamicky optimalizuje výkon.

V podstatě existují DMRS proto, aby poskytly přesný a efektivní mechanismus pro odhad kanálu v moderních, hustých a vysoce dynamických rádiových sítích. Jsou základní technologií fyzické vrstvy, která řeší klíčovou výzvu spolehlivé demodulace vysokorychlostních dat ve složitých prostředích šíření, čímž přímo podporuje klíčové výkonnostní ukazatele 5G, jako je rozšířené mobilní širokopásmové připojení (eMBB) a ultra-spolehlivá nízkolatenční komunikace (URLLC).

## Klíčové vlastnosti

- Specifické pro UE, vysílané pouze v přidělených uživatelských blocích prostředků
- Předkódováno s daty, což umožňuje podporu beamformingu a Massive MIMO
- Konfigurovatelná časová a frekvenční hustota pro optimalizaci sledování kanálu
- Podporuje vícevrstvý přenos pro MIMO (až 12 vrstev v NR)
- Používá scrambling sekvence pro ortogonalitu mezi UE a vrstvami
- Front-loaded konstrukce umožňuje časný odhad kanálu a nízkolatenční zpracování

## Související pojmy

- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.787** (Rel-19) — UE Radio Transmission for Sidelink CA in ITS Band
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.812** (Rel-16) — Study on NOMA for NR
- **TS 38.817** — 3GPP TR 38.817
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [DMRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dmrs/)
