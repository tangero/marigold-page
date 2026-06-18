---
slug: "dm-rs"
url: "/mobilnisite/slovnik/dm-rs/"
type: "slovnik"
title: "DM-RS – Demodulation Reference Signal"
date: 2025-01-01
abbr: "DM-RS"
fullName: "Demodulation Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dm-rs/"
summary: "Referenční signály zabudované v časově-frekvenčních zdrojích fyzického datového kanálu za účelem umožnění koherentní demodulace. Poskytují přijímači známý signál pro odhad podmínek rádiového kanálu, c"
---

DM-RS je referenční signál zabudovaný do zdrojů fyzického datového kanálu, který umožňuje koherentní demodulaci tím, že poskytuje známý signál pro odhad kanálu, což je nezbytné pro přesné dekódování přenášených dat.

## Popis

Demodulační referenční signály (DM-RS) jsou pilotní signály definované ve specifikacích fyzické vrstvy 3GPP pro LTE a NR. Jsou specificky navrženy tak, aby napomáhaly demodulaci přidružených fyzických datových kanálů, jako je Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)), Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)) a Physical Sidelink Shared Channel ([PSSCH](/mobilnisite/slovnik/pssch/)). Na rozdíl od buněčně specifických referenčních signálů ([CRS](/mobilnisite/slovnik/crs/) v LTE) jsou DM-RS uživatelsky specifické a jsou vysílány pouze v rámci bloků zdrojů přidělených pro přenos dat konkrétního uživatele. To znamená, že procházejí stejným předkódováním, beamformingem a podmínkami kanálu jako samotné datové symboly, čímž poskytují vysoce přesný odhad kanálu pro zamýšlený přijímač.

Z architektonického hlediska jsou DM-RS multiplexovány s datovými symboly v časově-frekvenční mřížce. Jejich konkrétní vzor – hustota, umístění a sekvence – je konfigurovatelný a signalizován prostřednictvím signalizace vyšší vrstvy ([RRC](/mobilnisite/slovnik/rrc/)) nebo dynamické signalizace ([DCI](/mobilnisite/slovnik/dci/)). V NR je návrh vysoce flexibilní a podporuje front-loaded DM-RS (umístěné na začátku slotu pro časný odhad kanálu), dodatečné DM-RS symboly pro scénáře s vysokou mobilitou a konfigurovatelnou hustotu (např. jedno-symbolové nebo dvou-symbolové). Generování sekvence pro DM-RS je založeno na pseudonáhodných sekvencích, které jsou promíchány s parametry, jako je identita buňky fyzické vrstvy, číslo slotu a uživatelsky specifická identita pro promíchání, aby se minimalizovala interference mezi referenčními signály různých uživatelů.

Princip fungování DM-RS je klíčový pro moderní systémy založené na [OFDM](/mobilnisite/slovnik/ofdm/). Po přijetí přenosu UE nebo gNB extrahuje DM-RS symboly ze známých pozic ve svých přidělených zdrojích. Poté porovná přijaté DM-RS s lokálně generovanou známou referenční sekvencí. Rozdíl mezi vyslanou a přijatou sekvencí charakterizuje dopad rádiového kanálu – včetně efektů jako útlum, Dopplerův posun a fázová rotace. Tento odhad kanálu je pak použit pro ekvalizaci přijatých datových symbolů, což efektivně odstraní zkreslení kanálu a umožní koherentní demodulaci. Pro Multi-User [MIMO](/mobilnisite/slovnik/mimo/) (MU-MIMO) jsou ortogonální DM-RS porty přiřazeny různým uživatelům sdílejícím stejné časově-frekvenční zdroje, což přijímači umožňuje oddělit a demodulovat vlastní datový tok i přes interferenci. Role DM-RS je proto nepostradatelná pro dosažení vysoké spektrální účinnosti, podporu pokročilých víceanténních technik a zajištění spolehlivého příjmu dat v náročných rádiových prostředích.

## K čemu slouží

DM-RS byly zavedeny, aby odstranily omezení společných referenčních signálů (jako CRS v LTE) v podpoře pokročilých víceanténních technologií a uživatelsky specifického beamforming. V raných verzích LTE byly CRS vysílány v celém šířkovém pásmu buňky a subrámci a poskytovaly odhad kanálu pro celou buňku. Tento přístup se však stal neefektivním pro MU-MIMO a beamforming, kde je efektivní kanál specifický pro předkódovací váhy uživatele. Vysílání CRS pro všechny anténní porty také vytvářelo významnou režii a interferenci.

Hlavní problém, který DM-RS řeší, je umožnění přesného, uživatelsky specifického odhadu kanálu pro předkódované přenosy. Protože DM-RS procházejí stejným předkódováním jako data, může přijímač odhadnout složený kanál (fyzický kanál kombinovaný s předkodérem), což je přesně to, co je potřeba pro demodulaci dat. Tato uživatelsky specifická povaha snižuje režii pilotních signálů, když je přidělena pouze podmnožina zdrojů, a je nezbytná pro podporu velkého počtu anténních prvků v Massive MIMO. Také zvyšuje bezpečnost a správu interference, protože sekvence DM-RS je uživatelsky specifická a pro nezamýšlené přijímače je obtížnější ji využít.

Navíc evoluce směrem k NR vyžadovala ještě větší flexibilitu pro podporu různých případů užití, od rozšířeného mobilního širokopásmového připojení (eMBB) až po ultra-spolehlivou komunikaci s nízkou latencí (URLLC). Konfigurovatelné vzory DM-RS v NR umožňují systému dynamicky vyvažovat kompromis mezi režií a přesností odhadu kanálu. Pro sloty s krátkou dobou trvání a nízkou latencí umožňují front-loaded DM-RS rychlé dekódování. Pro scénáře s vysokorychlostními vlaky poskytují dodatečné DM-RS symboly časté sledování kanálu. DM-RS jsou tedy základní technologií fyzické vrstvy, která umožňuje vysoký výkon, flexibilitu a účinnost rádiových přístupových sítí 4G a 5G.

## Klíčové vlastnosti

- Uživatelsky specifické a předkódované spolu s přidruženými daty, což umožňuje přesnou demodulaci beamformingových přenosů
- Konfigurovatelné vzory a hustota (např. front-loaded, dodatečné symboly) pro podporu různých případů užití a mobility
- Ortogonální multiplexování pro více vrstev a uživatelů, nezbytné pro provoz SU-MIMO a MU-MIMO
- Generování založené na sekvencích s uživatelsky specifickým promícháním pro minimalizaci mezibuněčné a meziuživatelské interference
- Signalizováno dynamicky (prostřednictvím DCI) nebo semi-staticky (prostřednictvím RRC) pro flexibilní plánování sítě
- Podporuje odhad kanálu jak pro demodulaci dat, tak pro sledování fáze v pokročilých OFDM systémech

## Související pojmy

- [PT-RS – Phase Tracking Reference Signal](/mobilnisite/slovnik/pt-rs/)
- [SRS – Space Radiocommunication Stations](/mobilnisite/slovnik/srs/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.766** (Rel-15) — LTE BS Interference Cancellation Receiver Study
- **TS 36.871** (Rel-11) — Downlink MIMO Enhancement for LTE-Advanced
- **TS 36.884** (Rel-13) — MMSE-IRC Receiver Performance for LTE BS
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [DM-RS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dm-rs/)
