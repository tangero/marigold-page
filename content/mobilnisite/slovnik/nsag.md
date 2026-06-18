---
slug: "nsag"
url: "/mobilnisite/slovnik/nsag/"
type: "slovnik"
title: "NSAG – Network Slice Access Group"
date: 2026-01-01
abbr: "NSAG"
fullName: "Network Slice Access Group"
category: "Network Slicing"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nsag/"
summary: "Skupinový identifikátor používaný v RAN k asociaci UE s konkrétní sadou síťových řezů. Umožňuje RAN aplikovat společnou politiku a optimalizace (jako je paging, alokace prostředků) pro všechny UE patř"
---

NSAG je skupinový identifikátor používaný v RAN k asociaci UE s konkrétní sadou síťových řezů, umožňující společnou politiku a optimalizace pro všechny UE v této skupině řezů.

## Popis

Network Slice Access Group (NSAG) je koncept na úrovni RAN zavedený ve specifikaci 3GPP Release 17 pro optimalizaci procedur Radio Access Network (RAN) pro síťové řezy. Jde o identifikátor, který sdružuje jednu nebo více hodnot Network Slice Selection Assistance Information ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)). Hlavní myšlenkou je, že z pohledu RAN lze k UE, kterým je povolen přístup ke stejné sadě řezů (tj. ke stejnému NSAG), přistupovat obdobně u určitých RAN procedur, což umožňuje efektivnější správu prostředků a signalizaci. NSAG je v RAN konfigurován systémem řízení ([OAM](/mobilnisite/slovnik/oam/)) a je komunikován k UE a k jádru sítě.

Provozně se NSAG používá v několika klíčových RAN procedurách. Během počátečního přístupu může UE indikovat svůj podporovaný NSAG gNB ve zprávě [RRC](/mobilnisite/slovnik/rrc/), což pomáhá RAN pochopit kontext skupinování řezů již v rané fázi. Důležitější je využití NSAG pro optimalizaci pagingu. Když jádro sítě ([AMF](/mobilnisite/slovnik/amf/)) potřebuje pagovat UE ve stavu RRC_IDLE nebo RRC_INACTIVE, zahrne NSAG UE do pagingové zprávy odeslané do RAN. RAN pak může vysílat pagingovou zprávu pouze v buňkách, které podporují řezy asociované s tímto NSAG, namísto ve všech buňkách. To výrazně snižuje zbytečnou režii pagingu a zlepšuje výdrž baterie u UE, která nepatří do cílové skupiny řezů. Dále může RAN používat NSAG pro politiky alokace rádiových prostředků, priorizaci navazování spojení a nastavení mobility, která jsou společná pro všechny řezy ve skupině.

Identifikátor NSAG je součástí kontextu UE jak v jádře sítě, tak v RAN. AMF určí NSAG pro UE na základě přihlášených a povolených S-NSSAI a zahrne jej do kontextu UE navázaného s gNB (např. přes rozhraní [NGAP](/mobilnisite/slovnik/ngap/)). To umožňuje RAN udržovat mapování mezi UE, jejími povolenými řezy a odpovídajícím NSAG. Použití NSAG efektivně abstrahuje potenciálně velkou a dynamickou sadu S-NSSAI na menší počet stabilních skupin, čímž zjednodušuje implementace v RAN a snižuje signalizační zátěž spojenou se zpracováním jednotlivých identifikátorů řezů v každé RAN proceduře.

## K čemu slouží

NSAG byl zaveden pro řešení výzev škálovatelnosti a efektivity RAN vyvolaných velkým počtem jemně odlišených síťových řezů. V prvních releasech 5G musel RAN zpracovávat jednotlivé [S-NSSAI](/mobilnisite/slovnik/s-nssai/) pro každé UE, což mohlo vést k signalizační režii a složitému zpracování, zejména u procedur jako je paging a mobilita, které jsou nezávislé na konkrétní službě, ale souvisejí se skupinou řezů, do které UE patří. RAN potřeboval způsob, jak agregovat informace specifické pro řezy, aby mohl aplikovat společnou politiku bez zpracovávání každého řezu jednotlivě.

Hlavním problémem, který NSAG řeší, je neefektivní paging. Bez NSAG by RAN při pagingu UE musel pravděpodobně vysílat paging ve všech buňkách, což plýtvá rádiovými prostředky a způsobuje interference, protože neví, které buňky podporují konkrétní řezy dané UE. NSAG umožňuje RAN provádět 'paging s ohledem na řezy' (slice-aware paging), cílící pouze na relevantní buňky. To je pro efektivitu síťových řezů v RAN klíčové. Dále NSAG zjednodušuje implementaci RAN pro správu rádiových prostředků na základě řezů, což umožňuje gNB konfigurovat společné parametry (jako jsou vyhrazené prostředky pro náhodný přístup nebo politiky plánování) na NSAG namísto na S-NSSAI, což je škálovatelnější a lépe spravovatelné.

## Klíčové vlastnosti

- Sdružuje více S-NSSAI do jediného identifikátoru na úrovni RAN pro efektivní zpracování.
- Umožňuje optimalizaci pagingu s ohledem na řezy omezením pagingu na buňky podporující daný NSAG.
- Umožňuje RAN aplikovat společnou politiku správy rádiových prostředků na všechna UE ve stejné skupině.
- Snižuje signalizační režii mezi jádrem a RAN abstrakcí seznamů řezů.
- Konfigurován systémem OAM a komunikován k UE a síťovým funkcím (AMF, gNB).
- Používán v signalizaci RRC (např. schopnosti UE, paging) a v procedurách rozhraní NGAP.

## Související pojmy

- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [NGAP – Next Generation Application Protocol](/mobilnisite/slovnik/ngap/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.531** (Rel-19) — 3GPP TS 29531: Nnssf Service Based Interface
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.470** (Rel-19) — F1 Interface Introduction
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [NSAG na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsag/)
