---
slug: "tmgi"
url: "/mobilnisite/slovnik/tmgi/"
type: "slovnik"
title: "TMGI – Temporary Multicast Group Identifier"
date: 2026-01-01
abbr: "TMGI"
fullName: "Temporary Multicast Group Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tmgi/"
summary: "Temporary Multicast Group Identifier (TMGI) je jedinečný identifikátor používaný v sítích 3GPP k identifikaci konkrétní relace služby Multimedia Broadcast Multicast Service (MBMS). Umožňuje uživatelsk"
---

TMGI je jedinečný identifikátor používaný v sítích 3GPP k identifikaci konkrétní MBMS relace, který umožňuje uživatelskému zařízení objevit, připojit se k ní a přijímat multicastový nebo broadcastový obsah.

## Popis

Temporary Multicast Group Identifier (TMGI) je klíčový identifikátor v architektuře služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) dle 3GPP. Jednoznačně identifikuje konkrétní MBMS relaci v rámci jedné [PLMN](/mobilnisite/slovnik/plmn/) (Public Land Mobile Network) nebo napříč více PLMN. TMGI není trvalá adresa, ale je dočasně přidělen na dobu trvání konkrétní relace služby MBMS. Jeho struktura, definovaná v 3GPP TS 23.003, typicky zahrnuje Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)), Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)) a službě specifické skupinové ID, což umožňuje globální nebo síťově specifickou jedinečnost.

Hlavní funkcí TMGI je sloužit jako ukazatel pro celý řetězec poskytování služby MBMS. Procedury oznámení služby, které informují uživatelské zařízení (UE) o dostupném MBMS obsahu, obsahují TMGI. Když si UE přeje službu přijímat, použije TMGI k zahájení procedury připojení směrem k síti, čímž indikuje svůj zájem o konkrétní multicastovou skupinu. V jádru sítě přiděluje TMGI entita [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Center) a používá ho k identifikaci přenosového kanálu a relace směrem k přístupové síti. V rádiové přístupové síti (RAN) se TMGI používá k identifikaci společných rádiových prostředků (jako je MBMS Point-to-Multipoint Control Channel) přidělených pro danou relaci, což umožňuje více UE efektivně přijímat stejný datový proud.

Z pohledu protokolů se TMGI přenáší na více vrstvách. Objevuje se v signalizačních zprávách [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) pro správu relací, v zprávách [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control) pro správu multicastových skupin v RAN a je nedílnou součástí schématu IP multicastových adres používaného pro datovou rovinu. Síť používá TMGI k namapování služby MBMS na konkrétní kombinaci IP multicastové adresy a portu pro distribuci dat. Toto end-to-end propojení zajišťuje, že od původce služby (BM-SC) až k přijímajícímu UE mohou všechny síťové elementy správně identifikovat a zpracovávat datový tok spojený s konkrétní broadcastovou nebo multicastovou relací.

## K čemu slouží

TMGI bylo vytvořeno k řešení základního problému identifikace a správy multicastových relací v mobilním prostředí. Na rozdíl od unicastu, kde je spojení jedinečné pro jedno UE, zahrnuje multicast doručování stejného obsahu potenciálně milionům zařízení. Byl potřeba jedinečný, relaci specifický identifikátor, který by umožnil UE signalizovat svůj zájem (připojit se/opustit), síti efektivně přidělovat sdílené prostředky a rozlišovat mezi více souběžnými službami [MBMS](/mobilnisite/slovnik/mbms/).

Řeší omezení pouhého použití IP multicastových adres pro tento účel v mobilním kontextu. Samotná adresa IP multicastové skupiny neobsahuje potřebný kontext síťového směrování (např. domovskou síť) a není ideální pro signalizaci v mobilně specifických řídicích rovinách. TMGI poskytuje strukturovaný, pro mobilní sítě vhodný identifikátor, který zahrnuje identitu PLMN, což umožňuje síťově založené objevování služeb, řízení přístupu a podporu roamingu. Jeho vytvoření bylo motivováno zavedením MBMS v Release 6, které si kladlo za cíl umožnit efektivní hromadné doručování obsahu (jako je mobilní TV) přes sítě 3GPP, což vyžadovalo robustní mechanismus správy a identifikace relací přizpůsobený pro mobilní architektury.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro relaci služby MBMS
- Struktura zahrnuje MCC, MNC a skupinové ID služby
- Používá se v oznámení služby pro objevení UE
- Klíčový parametr pro procedury připojení/opuštění UE k multicastové skupině
- Identifikuje relaci pro přidělení prostředků v RAN a jádru sítě
- Mapuje se na IP multicastovou adresu pro distribuci v datové rovině

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TS 23.246** (Rel-19) — MBMS Bearer Service Stage 2 Description
- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TS 23.768** (Rel-12) — Group Communication System Enablers for LTE
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- … a dalších 40 specifikací

---

📖 **Anglický originál a plná specifikace:** [TMGI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmgi/)
