---
slug: "eutran"
url: "/mobilnisite/slovnik/eutran/"
type: "slovnik"
title: "EUTRAN – Evolved Universal Terrestrial Radio Access Network"
date: 2025-01-01
abbr: "EUTRAN"
fullName: "Evolved Universal Terrestrial Radio Access Network"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eutran/"
summary: "Rádiová přístupová síť pro 4G LTE, která se skládá z jednoho nebo více eNodeB (základnových stanic) a rozhraní mezi nimi. Poskytuje rádiové rozhraní (EUTRA) pro uživatelská zařízení (UE) a připojuje s"
---

EUTRAN je rádiová přístupová síť pro 4G LTE, která se skládá ze základnových stanic eNodeB a poskytuje rozhraní pro uživatelská zařízení (UE) a připojuje se k Evolved Packet Core.

## Popis

Evolved Universal Terrestrial Radio Access Network (EUTRAN) je souhrnný termín pro síť rádiových přístupových uzlů a jejich vzájemných propojení, které tvoří LTE rádiovou síť. Její jedinou komponentou je evolved NodeB (eNodeB), která poskytuje ukončení protokolů uživatelské roviny ([PDCP](/mobilnisite/slovnik/pdcp/)/[RLC](/mobilnisite/slovnik/rlc/)/[MAC](/mobilnisite/slovnik/mac/)/[PHY](/mobilnisite/slovnik/phy/)) a řídicí roviny ([RRC](/mobilnisite/slovnik/rrc/)) směrem k uživatelskému zařízení (UE). Na rozdíl od 3G [UTRAN](/mobilnisite/slovnik/utran/) má EUTRAN plně distribuovanou, plochou architekturu, kde je každý eNodeB autonomní a připojuje se přímo k Evolved Packet Core (EPC).

Z architektonického hlediska je EUTRAN definována dvěma klíčovými rozhraními: rozhraním Uu (rádiové rozhraní k UE) a rozhraním S1 (k EPC). Rozhraní S1 je rozděleno na [S1-U](/mobilnisite/slovnik/s1-u/) pro provoz v uživatelské rovině (připojení k Serving Gateway - [S-GW](/mobilnisite/slovnik/s-gw/)) a S1-MME pro signalizaci v řídicí rovině (připojení k Mobility Management Entity - MME). Pro přímou komunikaci mezi eNodeB, například pro koordinaci předání spojení (handover) a správu interference, se používá rozhraní X2. Toto rozhraní X2 je definujícím rysem EUTRAN a umožňuje decentralizovanou správu mobility a rádiových zdrojů bez centrálního řídicího prvku.

EUTRAN funguje tak, že každý eNodeB nezávisle spravuje rádiové zdroje pro uživatelská zařízení ve své buňce (buňkách). Provádí funkce jako rádiové přijímací řízení, řízení mobility spojení, dynamické plánování zdrojů pro uplink a downlink a kompresi IP hlaviček. Během předání spojení zdrojový eNodeB použije rozhraní X2 (pokud je dostupné) k přímé koordinaci s cílovým eNodeB, přenese kontext UE a přepošle právě přenášené datové pakety, aby se minimalizovalo přerušení služby. eNodeB také vynucuje zabezpečení aplikací šifrování a ochranu integrity podle konfigurace od EPC. Celý návrh EUTRAN klade důraz na jednoduchost, nízkou latenci a vysokou dostupnost, aby podporoval plynulé mobilní širokopásmové služby.

## K čemu slouží

EUTRAN byl vytvořen, aby přinesl radikální zjednodušení architektury rádiové přístupové sítě ve srovnání se svým předchůdcem, UTRAN. Hierarchická struktura UTRAN, kde NodeB řídil Radio Network Controller (RNC), představovala jediný bod selhání a přidávala latenci pro zpracování dat a předání spojení. Účelem EUTRAN bylo tuto architekturu zploštit a distribuovat inteligenci do základnové stanice (eNodeB), aby se snížila latence, zlepšila škálovatelnost a snížily náklady.

Motivace vycházela z potřeby optimalizovat síť pro paketově přepínaný, IP-based provoz. Tradiční model s RNC byl lépe přizpůsoben pro správu okruhově přepínaných hlasových kanálů. Odstraněním RNC a přímým připojením eNodeB k bránám paketového jádra EUTRAN snižuje počet síťových prvků v datové cestě, čímž snižuje latenci v uživatelské rovině a provozní složitost. To bylo zásadní pro dosažení cílů LTE pro vysokorychlostní data a služby v reálném čase.

EUTRAN vyřešil klíčové problémy síťové složitosti a latence při předání spojení. Distribuované předání spojení založené na X2 je výrazně rychlejší než předání spojení zprostředkované RNC v UTRAN. Plochá architektura navíc umožňuje flexibilnější a nákladově efektivnější nasazení a škálování sítě, protože kapacitu lze přidávat nasazením dalších eNodeB bez nutnosti přestavby centralizovaného RNC. Tento návrh přímo podporuje požadavky na vysokou kapacitu a nízkou latenci, které byly klíčové pro úspěch LTE jako skutečné mobilní širokopásmové technologie.

## Klíčové vlastnosti

- Plochá architektura skládající se pouze z eNodeB bez centrálního RNC
- Přímé připojení rozhraním S1 (S1-U, S1-MME) mezi eNodeB a EPC
- Rozhraní X2 pro přímou komunikaci mezi eNodeB a předání spojení
- Integrovaná správa rádiových zdrojů, řízení mobility a plánování v eNodeB
- Podpora funkcí Self-Organizing Network (SON) pro automatizovaný provoz
- Podpora plynulé mobility s procedurami předání spojení založenými na X2 a S1

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 22.258** (Rel-7) — All-IP Network Service Requirements
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR

---

📖 **Anglický originál a plná specifikace:** [EUTRAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/eutran/)
