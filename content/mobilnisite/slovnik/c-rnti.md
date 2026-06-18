---
slug: "c-rnti"
url: "/mobilnisite/slovnik/c-rnti/"
type: "slovnik"
title: "C-RNTI – Cell Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "C-RNTI"
fullName: "Cell Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/c-rnti/"
summary: "Dočasný, jedinečný identifikátor přidělený gNB/eNB uživatelskému zařízení (UE) na dobu jeho spojení v konkrétní buňce. Je klíčový pro plánování, přidělování prostředků a adresování UE přes rozhraní vz"
---

C-RNTI je dočasný, jedinečný identifikátor přidělený gNB/eNB uživatelskému zařízení (UE) pro jeho spojení v konkrétní buňce, klíčový pro plánování, přidělování prostředků a adresování UE přes rozhraní vzdušného rozhraní.

## Popis

Cell Radio Network Temporary Identifier (C-RNTI, dočasný identifikátor buňkové rádiové sítě) je základní identifikátor používaný v 3GPP rádiových přístupových sítích (RAN), včetně UMTS, LTE a NR. Jedná se o 16bitovou hodnotu v LTE a NR, kterou obslužná základnová stanice ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR) jedinečně přidělí uživatelskému zařízení (UE) po úspěšném náhodném přístupu a navázání spojení v dané konkrétní buňce. Primární úlohou C-RNTI je sloužit jako dočasná adresa UE na fyzické a [MAC](/mobilnisite/slovnik/mac/) vrstvě, což síti umožňuje efektivně spravovat a směrovat rádiové prostředky pro tohoto konkrétního uživatele.

Z architektonického hlediska je C-RNTI klíčovou součástí řídicí roviny RAN. Používá se ke skramblování kontrolního součtu [CRC](/mobilnisite/slovnik/crc/) (Cyclic Redundancy Check) zpráv [DCI](/mobilnisite/slovnik/dci/) (Downlink Control Information) na kanálu [PDCCH](/mobilnisite/slovnik/pdcch/) (Physical Downlink Control Channel). Když UE monitoruje PDCCH, pokouší se dekódovat zprávy DCI pomocí svého přiděleného C-RNTI jako součásti procesu de-skramblování. Úspěšné dekódování indikuje, že řídicí zpráva (např. povolení pro uplink nebo přiřazení pro downlink) je určena právě pro toto konkrétní UE. Tento mechanismus poskytuje bezpečné a efektivní adresování bez nutnosti neustálého přenosu delších, trvalých identit UE přes zranitelné rozhraní vzdušného rozhraní.

C-RNTI je ústřední pro dynamické plánování. Pro každý přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/)) plánovač v základnové stanici používá C-RNTI k adresování povolení a přiřazení konkrétním UE. Používá se pro přenosy na sdílených kanálech pro uplink ([UL-SCH](/mobilnisite/slovnik/ul-sch/)) i downlink ([DL-SCH](/mobilnisite/slovnik/dl-sch/)). Identifikátor je dočasný a specifický pro buňku; pokud UE provede předání spojení (handover) do nové buňky, cílová buňka mu přidělí nové C-RNTI. Tím je zajištěna jedinečnost identifikátoru v oblasti pokrytí buňky a zjednodušena správa prostředků. C-RNTI je uvolněno při uvolnění RRC spojení UE nebo během procedur předání spojení.

Kromě základního plánování hraje C-RNTI roli i v dalších procedurách. Používá se pro náhodný přístup s kolizemi (contention-based), kde může být UE zpočátku přiděleno dočasné C-RNTI, které může být později potvrzeno jako jeho trvalé C-RNTI pro dané spojení. V připojeném režimu se používá pro příkazy řízení výkonu (TPC-PUCCH-RNTI, TPC-PUSCH-RNTI jsou odvozené koncepty) a další řídicí elementy MAC. Jeho dočasná povaha je klíčovým bezpečnostním a soukromím prvkem, který brání dlouhodobému sledování UE na základě jejího identifikátoru v rádiové signalizaci.

## K čemu slouží

C-RNTI bylo vytvořeno k vyřešení základního problému efektivního a bezpečného adresování konkrétního uživatelského zařízení v rámci rádiové buňky za účelem přidělování prostředků a řídicí signalizace. Před koncepty jako C-RNTI mohly sítě spoléhat na delší, trvalé identifikátory pro plánování, což by bylo neefektivní pro časté, malé řídicí zprávy a představovalo by významné riziko pro soukromí kvůli snadnému sledování zařízení přes vzdušné rozhraní.

Jeho zavedení, zejména při návrhu LTE, bylo motivováno potřebou vysoce dynamického, paketově plánovaného vzdušného rozhraní. Na rozdíl od systémů s přepojováním okruhů přidělují LTE a NR prostředky v řádu milisekund. Přenos plné identity UE (jako IMSI nebo S-TMSI) s každým plánovacím povolením by vytvořil obrovskou režii. C-RNTI poskytuje krátký, lokálně významný ukazatel, který minimalizuje režii na řídicím kanále a zároveň umožňuje vysokorychlostní plánování s nízkou latencí vyžadované pro širokopásmové datové služby.

C-RNTI také řeší bezpečnostní a soukromí aspekty. Tím, že je dočasný a specifický pro buňku, zmírňuje riziko pasivního odposlechu, který by mohl sledovat polohu uživatele a vzorce spojení v široké oblasti. UE je v každé buňce přiděleno nové C-RNTI, čímž se přerušuje spojitost jeho identity v rádiové signalizaci napříč různými lokalitami. Tento návrh je základní součástí ochrany soukromí účastníků v 3GPP. Dále zjednodušuje implementaci RAN tím, že omezuje správu identifikátorů na jedinou buňku nebo gNB, čímž se vyhýbá potřebě globální koordinace těchto dočasných adres.

## Klíčové vlastnosti

- 16bitový dočasný identifikátor, jedinečný v rámci buňky
- Používá se ke skramblování CRC zpráv DCI na PDCCH pro adresování specifické pro UE
- Základní pro dynamické plánování prostředků sdílených kanálů UL a DL
- Přidělen během náhodného přístupu a navazování spojení
- Specifický pro buňku a mění se při předání spojení (handover)
- Zvyšuje soukromí na vzdušném rozhraní tím, že brání dlouhodobému sledování UE

## Související pojmy

- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [C-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-rnti/)
