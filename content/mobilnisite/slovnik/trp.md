---
slug: "trp"
url: "/mobilnisite/slovnik/trp/"
type: "slovnik"
title: "TRP – Transmission and Reception Point"
date: 2026-01-01
abbr: "TRP"
fullName: "Transmission and Reception Point"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/trp/"
summary: "Fyzický nebo logický bod v rádiové přístupové síti, který vysílá a přijímá rádiové signály od/ k uživatelskému zařízení (UE). Je to základní prvek v systémech MIMO, beamformingu a distribuovaných anté"
---

TRP (bod vysílání a příjmu) je fyzický nebo logický bod v rádiové přístupové síti, který vysílá a přijímá rádiové signály od a k uživatelskému zařízení (UE) a slouží jako základní prvek pro MIMO, beamforming a flexibilní nasazení sítě.

## Popis

Transmission and Reception Point (TRP) je základní architektonická komponenta v rámci 3GPP rádiové přístupové sítě (RAN), konkrétně definovaná od LTE (Rel-7) dále a klíčová pro 5G NR. Představuje fyzický nebo logický bod, který zajišťuje vysílání a příjem rádiových signálů přes rozhraní vzduchu s uživatelským zařízením (UE). Koncepčně je TRP asociován se sadou geograficky společně umístěných nebo distribuovaných anténních prvků. V tradičních nasazeních makro-buněk často TRP odpovídá jedné lokalitě základnové stanice nebo sektoru. V pokročilých architekturách, jako je Coordinated Multi-Point (CoMP), Distributed [MIMO](/mobilnisite/slovnik/mimo/) a cloud RAN (C-RAN), však může komunikaci jednoho UE spravovat více TRP současně, které mohou být fyzicky oddělené, ale logicky koordinované centrální jednotkou ([CU](/mobilnisite/slovnik/cu/)) nebo distribuovanou jednotkou ([DU](/mobilnisite/slovnik/du/)). Toto oddělení funkce vysílání/příjmu od monolitického buněčného místa je klíčové pro zahušťování sítě a flexibilitu.

Z technické perspektivy je TRP zodpovědný za fyzickou vrstvu zpracování signálů pro specifickou sadu anténních portů. Zpracovává úlohy jako digitální beamforming, precoding, modulaci a mapování zdrojů pro downlink a odpovídající příjem, demodulaci a odhad kanálu pro uplink. V kontextu 5G NR je TRP úzce spojen s konceptem Synchronization Signal Block (SSB) a Channel State Information Reference Signal ([CSI-RS](/mobilnisite/slovnik/csi-rs/)), které jsou vysílány z konkrétních TRP, aby umožnily UE měřit podmínky kanálu, provádět správu beamů a podávat zpětnou vazbu. gNB (5G základnová stanice) se může skládat z jednoho nebo více TRP. Specifikace 3GPP definují procedury pro multi-TRP operaci, kde může být UE konfigurováno s více stavy Transmission Configuration Indicator ([TCI](/mobilnisite/slovnik/tci/)), z nichž každý je spojen s jiným TRP, což umožňuje robustní přenosová schémata jako prostorová diverzita nebo zvýšení datových rychlostí prostřednictvím multi-streamového přenosu.

Role TRP je klíčová pro umožnění hlavních funkcí 5G. Je to koncový bod pro beam-based komunikaci, kde je každý beam efektivně spravován TRP. V sítích s integrovaným přístupem a backhaulem ([IAB](/mobilnisite/slovnik/iab/)) funguje IAB uzel jako TRP pro své podřízené uzly a UE. Pro mobilitu jsou handovery a převýběry buněk řízeny na základě měření referenčních signálů z různých TRP. Síť může dynamicky aktivovat nebo deaktivovat TRP na základě zatížení provozem, což umožňuje úsporu energie. Dále, v network slicingu mohou být různé slice obsluhovány specifickými sadami TRP, aby byly splněny různé požadavky služeb. Správa a řízení TRP je zajišťována protokoly vyšších vrstev v RAN, přičemž rozhraní jako F1 a E1 v disaggreagované architektuře RAN 5G usnadňují komunikaci mezi CU a DU, které TRP řídí.

## K čemu slouží

Koncept TRP byl zaveden, aby abstrahoval fyzickou funkci vysílání a příjmu od tradičního monolitického konceptu buňky. Dřívější buněčné systémy byly z velké části postaveny na myšlence buňky, řízené jedinou základnovou stanicí s pevnou sadou společně umístěných antén. Tento model se stal omezujícím pro pokročilé techniky jako [MIMO](/mobilnisite/slovnik/mimo/), CoMP a zahušťování sítě, kde signály mohly pocházet z více geograficky oddělených anténních polí nebo jimi být přijímány. TRP poskytuje pro tyto techniky jemnější a flexibilnější referenční bod.

Jeho vytvoření bylo motivováno potřebou podporovat vylepšenou spektrální účinnost a síťovou kapacitu. Definováním TRP umožnilo 3GPP specifikace pro schémata, kde může více TRP obsluhovat jedno UE (např. nekoherentní společné vysílání v CoMP), čímž se zlepšuje spolehlivost signálu na okrajích buněk a celková propustnost. Také usnadňuje praktickou implementaci massive MIMO a beamformingu, kde je velké anténní pole složeno z více sub-polní nebo panelů, z nichž každý může být pro účely správy považován za samostatný TRP.

Ve vývoji směrem k 5G a dále je TRP základním kamenem pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a vylepšené mobilní širokopásmové připojení (eMBB). Multi-TRP přenos umožňuje redundanci, čímž snižuje pravděpodobnost selhání spoje. Pro průmyslový IoT a služby s vysokými nároky na spolehlivost zvyšuje spolehlivost simultánní vysílání z více TRP k jednomu UE (opakování PDCCH, opakování PDSCH). TRP tedy není jen aktualizací terminologie, ale klíčovým architektonickým prvkem umožňujícím flexibilní, vysoce výkonné a spolehlivé rádiové sítě.

## Klíčové vlastnosti

- Představuje fyzický nebo logický koncový bod pro vysílání a příjem rádiových signálů
- Základní jednotka pro správu beamů a beamformingové operace v 5G NR
- Umožňuje multi-TRP operaci pro CoMP, diverzitu a zvýšení kapacity
- Asociován se specifickými referenčními signály (SSB, CSI-RS) pro měření a podávání zpráv UE
- Odděluje funkci vysílání od identity buňky, což umožňuje flexibilní nasazení sítě
- Nedílná součást pokročilých RAN architektur jako C-RAN, D-RAN a IAB sítě

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 25.144** (Rel-11) — UE OTA Antenna Performance Requirements
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.144** (Rel-19) — UE OTA Antenna Performance Requirements
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.902** (Rel-19) — OTA TRP/TRS Measurement for LTE Terminals
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- … a dalších 44 specifikací

---

📖 **Anglický originál a plná specifikace:** [TRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/trp/)
