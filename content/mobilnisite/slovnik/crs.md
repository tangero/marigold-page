---
slug: "crs"
url: "/mobilnisite/slovnik/crs/"
type: "slovnik"
title: "CRS – Cell-specific Reference Signals"
date: 2026-01-01
abbr: "CRS"
fullName: "Cell-specific Reference Signals"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/crs/"
summary: "CRS jsou pilotní signály v downlinku vysílané základnovými stanicemi LTE (eNodeB), které umožňují odhad kanálu, výběr buňky a měření mobility. Jsou nezbytné pro demodulaci, synchronizaci a správu rádi"
---

CRS jsou pilotní signály v downlinku vysílané základnovými stanicemi LTE, které umožňují odhad kanálu, synchronizaci, měření mobility a demodulaci, a vytvářejí tak základní referenční mřížku pro fyzickou vrstvu.

## Popis

Buněčně specifické referenční signály (CRS) jsou předdefinované sekvence komplexních symbolů vysílané LTE eNodeB v celé šířce systémového pásma a v každém downlinkovém subrámci, s výjimkou některých [MBSFN](/mobilnisite/slovnik/mbsfn/) subrámců. Jsou vkládány do specifických zdrojových prvků v [OFDM](/mobilnisite/slovnik/ofdm/) časově-frekvenční mřížce podle vzorů definovaných v 3GPP TS 36.211. Vzor závisí na fyzickém identifikátoru buňky (0-503), počtu anténních portů použitých pro vysílání (1, 2 nebo 4) a délce cyklické předpony (normální nebo rozšířená). Toto buněčně specifické škramblování zajišťuje, že CRS ze sousedních buněk interferují řízeným, pseudonáhodným způsobem. Signály jsou vysílány s konstantním výkonem a poskytují přijímači známý referenční bod amplitudy a fáze.

V uživatelském zařízení (UE) se CRS primárně používají pro odhad downlinkového kanálu. Porovnáním přijatých CRS symbolů se známou vysílanou sekvencí může UE odhadnout frekvenční odezvu kanálu, včetně efektů jako útlum, rozprostření zpoždění a Dopplerův posuv. Tyto informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) jsou klíčové pro koherentní demodulaci fyzického downlinkového sdíleného kanálu ([PDSCH](/mobilnisite/slovnik/pdsch/)) a řídicích kanálů ([PDCCH](/mobilnisite/slovnik/pdcch/), [PCFICH](/mobilnisite/slovnik/pcfich/), [PHICH](/mobilnisite/slovnik/phich/)). Dále CRS umožňují UE provádět měření pro správu rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)), konkrétně výkon přijímaného referenčního signálu (RSRP) a kvalitu přijímaného referenčního signálu (RSRQ). Tato měření jsou hlášena síti a jsou základní pro výběr buňky, rozhodování o předání hovoru a správu mobility.

Z architektonického hlediska jsou CRS celoplošným, trvale vysílaným signálem. Jejich návrh představuje kompromis mezi režií referenčních signálů a přesností odhadu. Zatímco poskytují robustní a buněčně specifický referenční signál, spotřebovávají zdrojové prvky, které by jinak mohly nést uživatelská data. Vzor je navržen tak, aby poskytoval dostatečné vzorkování v časové i frekvenční oblasti pro přesné sledování kanálu. V provozu s více anténami (MIMO) jsou CRS vysílány na každém anténním portu, což umožňuje UE odhadnout kanál pro každý pár vysílací-přijímací antény, což je zásadní pro prostorové multiplexování a schémata vysílací diverzity. CRS také usnadňují časovou a frekvenční synchronizaci, protože je UE může použít k doladění časování symbolů a korekci posuvu nosné frekvence.

## K čemu slouží

CRS byly zavedeny v LTE Release 8/9 k řešení základního problému umožnění spolehlivé downlinkové komunikace v vícecestném, útlumovém rádiovém kanálu. Předchozí systémy jako UMTS používaly vyhrazené pilotní kanály, ale LTE rozhraní založené na OFDMA vyžadovalo novou architekturu referenčních signálů integrovanou do časově-frekvenční mřížky zdrojů. Primárním účelem je poskytnout známý signál, který může UE použít k odhadu impulsní odezvy rádiového kanálu, což je nezbytné k odstranění zkreslení kanálu na datových symbolech. Bez přesného odhadu kanálu by koherentní demodulace modulačních schémat vyššího řádu (jako 64-QAM) používaných v LTE byla nemožná, což by výrazně omezilo datové rychlosti.

Dalším klíčovým problémem, který CRS řeší, je podpora mobility. Aby se UE mohlo rozhodnout, kdy se předat sousední buňce, musí měřit sílu a kvalitu signálu těchto buněk. CRS poskytují buněčně specifický, trvale dostupný signál, který může UE detekovat a měřit, i když není k této buňce připojeno. To umožňuje síťově řízenou mobilitu založenou na přesných měřeních RSRP/RSRQ. Dále CRS podporují základní procedury fyzické vrstvy, jako je hledání buněk a počáteční synchronizace. Návrh CRS jako buněčně specifického signálu, škramblovaného identifikátorem buňky, také pomáhá zmírnit mezibuněčné rušení v heterogenních nasazeních sítě, protože UE dokáže rozlišit požadovaný signál od rušivých.

Vytvoření CRS bylo motivováno potřebou jednotného, efektivního referenčního signálu, který by mohl podporovat klíčové výkonnostní cíle LTE: vysoké špičkové datové rychlosti, nízkou latenci a zlepšenou spektrální účinnost. Jejich trvale vysílaná povaha zajišťuje, že UE, ať už v klidovém stavu nebo připojená, mohou kontinuálně monitorovat rádiové prostředí. Tento návrh však také přinesl omezení, jako je konstantní režie a mezibuněčné rušení v hustých nasazeních, což později vedlo k vývoji efektivnějších referenčních signálů, jako jsou CSI-RS a DM-RS v LTE-Advanced a 5G NR, které mohou být uživatelsky specifické a formované do svazku.

## Klíčové vlastnosti

- Buněčně specifické škramblování založené na fyzickém identifikátoru buňky (PCI)
- Vysílány na 1, 2 nebo 4 anténních portech pro podporu MIMO
- Poskytují referenci pro odhad kanálu a koherentní demodulaci
- Umožňují měření RSRP a RSRQ pro správu mobility
- Zabírají specifické zdrojové prvky v celé šířce pásma ve všech downlinkových subrámcích
- Podporují časovou/frekvenční synchronizaci a procedury hledání buněk

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)
- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [RSRQ – Reference Signal Receiving Quality](/mobilnisite/slovnik/rsrq/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.183** (Rel-19) — Customized Ringing Signal (CRS) Requirements
- **TS 22.810** (Rel-13) — Enhanced Calling Information Presentation Requirements
- **TS 24.183** (Rel-19) — Customized Ringing Signal (CRS) Protocol
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 32.275** (Rel-19) — MMTel Charging Specification
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study
- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.307** (Rel-19) — Release-Independent Frequency Band Support
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [CRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/crs/)
