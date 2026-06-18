---
slug: "tai"
url: "/mobilnisite/slovnik/tai/"
type: "slovnik"
title: "TAI – Tracking Area Identifier"
date: 2026-01-01
abbr: "TAI"
fullName: "Tracking Area Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tai/"
summary: "Jedinečný identifikátor sledovací oblasti (TA) v sítích 3GPP, používaný pro správu polohy UE a paging. Umožňuje efektivní mobilitu seskupováním buněk, čímž snižuje signalizační zátěž při mobilitě v id"
---

TAI je jedinečný identifikátor sledovací oblasti (Tracking Area), která sdružuje buňky v síti 3GPP za účelem správy polohy UE, umožnění efektivní mobility a snížení signalizační zátěže pro procedury pagingu a registrace.

## Popis

Identifikátor sledovací oblasti (TAI) je strukturovaný kód, který jednoznačně identifikuje sledovací oblast (Tracking Area) ve veřejné pozemní mobilní síti ([PLMN](/mobilnisite/slovnik/plmn/)). Sledovací oblast je logické seskupení jedné nebo více buněk, definované operátorem sítě za účelem sledování a pagingu uživatelského zařízení (UE) v idle nebo inactive stavech. TAI se skládá z mobilního kódu země ([MCC](/mobilnisite/slovnik/mcc/)), mobilního kódu sítě ([MNC](/mobilnisite/slovnik/mnc/)) a kódu sledovací oblasti ([TAC](/mobilnisite/slovnik/tac/)). MCC a MNC identifikují PLMN, zatímco TAC, typicky o délce 16 bitů, je přiřazen operátorem k rozlišení sledovacích oblastí v rámci dané PLMN. Tato hierarchická struktura zajišťuje globální jedinečnost a efektivní směrování zpráv pro správu polohy.

Z architektonického hlediska je TAI klíčovým parametrem používaným jak přístupovou rádiovou sítí (RAN), tak jádrem sítě (CN), konkrétně funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Když se UE pohybuje, provádí aktualizaci sledovací oblasti ([TAU](/mobilnisite/slovnik/tau/)), aby informovala síť o vstupu do nové [TA](/mobilnisite/slovnik/ta/), což je identifikováno změnou TAI. Síť pro každé UE udržuje seznam TAI, známý jako seznam identit sledovacích oblastí (TAI List), který umožňuje UE pohybovat se v rámci více TA bez častých aktualizací, čímž optimalizuje signalizaci. AMF používá TAI k určení příslušné obsluhované oblasti a ke správě pagingu; když dorazí downlinková zpráva pro UE v idle stavu, síť provede paging UE napříč všemi buňkami patřícími k TAI v jejím registrovaném seznamu.

Při provozu je TAI vysílán každou buňkou v blocích systémových informací (SIBs), což umožňuje UE detekovat její aktuální TA. Během počáteční registrace nebo procedur připojení UE hlásí TAI buňky, na které je napojena. AMF ověří tento TAI vůči svým nakonfigurovaným oblastem a může přiřadit nový TAI List. Pro mobilitu, pokud UE v idle módu detekuje TAI, který není v jejím přiřazeném seznamu, spustí proceduru TAU. TAI také hraje roli v síťovém slicingu a vynucování politik, protože určité slice nebo služby mohou být omezeny na konkrétní sledovací oblasti. Jeho návrh vyvažuje potřebu přesné znalosti polohy s požadavkem na minimalizaci signalizace, což je klíčové hledisko pro škálovatelnost sítě a životnost baterie UE.

## K čemu slouží

TAI byl zaveden, aby řešil výzvy efektivity správy polohy a pagingu v celulárních sítích, zejména když se sítě vyvíjely pro podporu paketově přepínaných služeb a zvýšené mobility. Před konceptem sledovacích oblastí byla správa polohy často založena na buňkách, což vedlo k nadměrné signalizační zátěži při pohybu UE, zejména v idle módu. To bylo neefektivní jak pro síťové zdroje, tak pro spotřebu baterie UE. Vytvoření sledovacích oblastí, identifikovaných pomocí TAI, umožnilo sítím seskupit buňky do větších logických oblastí, což síti umožnilo sledovat UE s hrubší granularitou během idle období, a tím snížit frekvenci signalizace aktualizace polohy.

Historicky, v 2G/GSM, plnily podobný účel lokalizační oblasti, ale s příchodem 3G/UMTS a zejména 4G/LTE (kde byl TAI formálně standardizován ve verzi 8), se stala zřejmou potřeba více optimalizované, IP-centrické architektury. TAI poskytuje standardizovanou, škálovatelnou metodu pro správu mobility, která je nezávislá na podkladové rádiové technologii, a podporuje bezproblémový vývoj z LTE na 5G. Řeší problém efektivního vyhledání UE pro příchozí hovory nebo datové relace bez nutnosti neustálého podrobného hlášení polohy. Optimalizací kompromisu mezi přesností polohy a signalizační zátěží umožňuje TAI sítím podporovat obrovské množství zařízení, což je nutnost pro internet věcí (IoT) a rozšířené mobilní širokopásmové připojení.

Dále TAI usnadňuje síťové operace, jako je vyrovnávání zatížení, směrování pro nouzové služby a dodržování regulatorních požadavků na hlášení polohy. Je základním prvkem pro funkce jako registrační oblasti (Registration Areas) v 5G, které tento koncept rozšiřují o zahrnutí více typů oblastí (např. sledovací oblasti, registrační oblasti). Návrh TAI zajišťuje zpětnou kompatibilitu a budoucí flexibilitu, což operátorům umožňuje rekonfigurovat uspořádání jejich [TA](/mobilnisite/slovnik/ta/) při změně topologie sítě a vzorců provozu bez dopadu na základní protokoly.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor složený z MCC, MNC a TAC
- Umožňuje efektivní sledování polohy UE a paging v idle/inactive módech
- Podporuje procedury aktualizace sledovací oblasti (TAU) pro správu mobility
- Vysílán v systémových informacích pro detekci UE
- Používá se k vytváření seznamů identit sledovacích oblastí (TAI Lists) pro registraci UE
- Nedílná součást signalizace pro připojení k síti, registraci a předávání spojení

## Související pojmy

- [TAC – Time Alignment Command](/mobilnisite/slovnik/tac/)
- [TAU – Tracking Area Update](/mobilnisite/slovnik/tau/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 23.304** (Rel-20) — 5G Proximity Services (ProSe) Stage 2
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.712** (Rel-13) — Enhancements to Warning Status Reporting Mechanisms
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 28.840** (Rel-18) — Technical Report
- **TS 28.875** (Rel-19) — Study on IAB Node Management
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- … a dalších 24 specifikací

---

📖 **Anglický originál a plná specifikace:** [TAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tai/)
