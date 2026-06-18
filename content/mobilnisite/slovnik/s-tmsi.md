---
slug: "s-tmsi"
url: "/mobilnisite/slovnik/s-tmsi/"
type: "slovnik"
title: "S-TMSI – SAE Temporary Mobile Subscriber Identity"
date: 2025-01-01
abbr: "S-TMSI"
fullName: "SAE Temporary Mobile Subscriber Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/s-tmsi/"
summary: "Dočasný identifikátor přiřazený MME pro UE v EPS. Používá se k ochraně trvalé identity uživatele (IMSI) během signalizačních procedur, jako je paging a žádosti o službu, což zvyšuje soukromí a snižuje"
---

S-TMSI je dočasný identifikátor přiřazený MME pro UE v EPS, který chrání trvalý IMSI uživatele během signalizačních procedur, jako je paging, čímž zvyšuje soukromí a snižuje zátěž rádiového rozhraní.

## Popis

[SAE](/mobilnisite/slovnik/sae/) Temporary Mobile Subscriber Identity (S-TMSI) je klíčový dočasný identifikátor používaný v rámci 3GPP Evolved Packet System (EPS). Vytváří a přiřazuje jej Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) uživatelskému zařízení (UE) po úspěšném připojení k síti nebo během aktualizace oblasti sledování ([TAU](/mobilnisite/slovnik/tau/)). S-TMSI slouží jako stručný alias pro globálně jedinečný International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), s primárním cílem chránit soukromí účastníka a optimalizovat efektivitu rádiové signalizace. Používá se ve scénářích, kdy je třeba identitu UE přenést přes rádiové rozhraní, například během pagingové procedury pro upozornění UE na příchozí data, nebo v počáteční zprávě Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) při žádosti o službu.

Strukturně je S-TMSI 40bitová hodnota složená ze dvou hlavních částí: MME Code ([MMEC](/mobilnisite/slovnik/mmec/)) a MME Temporary Mobile Subscriber Identity ([M-TMSI](/mobilnisite/slovnik/m-tmsi/)). MMEC je 8bitový kód, který jednoznačně identifikuje MME ve skupině MME (MME Group, identifikovaný MME Group ID nebo [GUMMEI](/mobilnisite/slovnik/gummei/)). M-TMSI je 32bitové číslo, které jednoznačně identifikuje UE v rámci tohoto konkrétního MME. V kombinaci s MME Group ID (které je odvozeno od PLMN ID a části MME Group ID z GUMMEI) umožňuje S-TMSI jakékoli síťové entitě jednoznačně identifikovat obsluhující MME pro dané UE. S-TMSI je doručeno UE v rámci NAS zpráv Attach Accept nebo TAU Accept.

Z procedurálního hlediska se S-TMSI hojně používá. V procesu pagingu odešle MME eNodeB pagingovou zprávu obsahující S-TMSI (nebo, pokud není k dispozici, IMSI). eNodeB poté tuto pagingovou zprávu vysílá vzduchem pomocí tohoto S-TMSI. UE, které monitoruje pagingový kanál, rozpozná své přiřazené S-TMSI a zahájí proceduru žádosti o službu. V počáteční NAS zprávě této žádosti o službu (nebo během periodické TAU) UE zahrne své S-TMSI, což síti umožní rychle identifikovat kontext UE v MME bez přenosu plného IMSI. Tento mechanismus nejen chrání IMSI před odposlechem, ale také snižuje velikost zpráv na rádiovém spoji, šetří cenné rádiové zdroje a urychluje navázání spojení.

## K čemu slouží

S-TMSI bylo zavedeno s EPS ve 3GPP Release 8, aby řešilo dvě klíčové nedostatky předchozích systémů: soukromí identity účastníka a efektivitu signalizace. V před-LTE systémech, jako jsou GSM a UMTS, sloužil podobnému účelu Temporary Mobile Subscriber Identity (TMSI), ale S-TMSI bylo přepracováno pro plošší, plně IP architekturu EPS. Jeho primárním účelem je zakrýt trvalý IMSI, což je klíčový problém soukromí, protože častý přenos IMSI by umožňoval snadné sledování a profilování účastníků. Používáním často se měnícího dočasného identifikátoru se poloha a aktivita uživatele stávají pro neoprávněné pozorovatele obtížněji korelovatelnými.

Dále S-TMSI řeší problém signalizační režie. IMSI je dlouhý, 15místný identifikátor. Jeho častý přenos pro paging a navazování spojení spotřebovává významnou šířku rádiového pásma. Kompaktní, fixně dlouhé 40bitové S-TMSI drasticky snižuje velikost signalizačních zpráv. Jeho struktura také slouží architektonickému účelu: zahrnutím MMEC poskytuje efektivní mechanismus směrování v rámci jádra sítě. Když eNodeB nebo jiné MME přijme S-TMSI, může odvodit obsluhující MME (nebo alespoň fond MME) bez rozsáhlých vyhledávání, čímž zefektivňuje procedury, jako jsou předávání mezi MME. Motivace pro jeho vytvoření byla nedílnou součástí designových cílů EPS – zlepšená bezpečnost, snížená latence a podpora obrovského počtu zařízení, což z něj činí základní prvek pro všechny následující generace mobilních sítí včetně 5G, kde se používá podobný koncept (5G-S-TMSI).

## Klíčové vlastnosti

- 40bitový dočasný identifikátor skládající se z 8bitového MMEC a 32bitového M-TMSI
- Přiřazený MME pro UE během procedur připojení nebo aktualizace oblasti sledování
- Používaný k pagingu UE a jeho identifikaci v počátečních NAS zprávách, čímž chrání IMSI
- Umožňuje efektivní směrování v jádru sítě prostřednictvím MMEC
- Snižuje signalizační režii na rádiovém rozhraní ve srovnání s použitím plného IMSI
- Základní pro soukromí UE a efektivitu sítě v EPS a 5GS

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [GUMMEI – Globally Unique MME Identifier](/mobilnisite/slovnik/gummei/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)

---

📖 **Anglický originál a plná specifikace:** [S-TMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-tmsi/)
