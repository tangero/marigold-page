---
slug: "guti"
url: "/mobilnisite/slovnik/guti/"
type: "slovnik"
title: "GUTI – Globally Unique Temporary UE Identity"
date: 2026-01-01
abbr: "GUTI"
fullName: "Globally Unique Temporary UE Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/guti/"
summary: "Globálně unikátní dočasná identita UE (GUTI) je dočasný identifikátor, který síť přiřadí uživatelskému zařízení (UE), aby ochránil trvalé identifikační údaje předplatitele (SUPI/IMSI). Používá se pro"
---

GUTI je dočasný identifikátor přiřazený síti pro UE, který chrání trvalé identifikační údaje předplatitele; používá se pro signalizaci v EPS a 5GS za účelem zvýšení soukromí a efektivity.

## Popis

Globálně unikátní dočasná identita UE (GUTI) je základním mechanismem pro ochranu soukromí a efektivitu v systému Evolved Packet System (EPS) a 5G System (5GS) konsorcia 3GPP. Její primární úlohou je nahradit použití trvalého, předplatitele citlivého Superscript Permanent Identifier ([SUPI](/mobilnisite/slovnik/supi/)) – což je v 4G [IMSI](/mobilnisite/slovnik/imsi/) – ve většině rádiových signalizačních zpráv. GUTI je přiřazena Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v jádrové síti v rámci EPS nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v rámci 5GS během počáteční registrace nebo procedur připojení. Po přiřazení UE používá GUTI k identifikaci sebe sama v následných signalizačních interakcích, například během služebních požadavků, aktualizací oblasti sledování nebo při předávání spojení.

Struktura GUTI je hierarchická a obsahuje informace, které síti umožňují efektivně směrovat signalizaci a lokalizovat uzel spravující mobilní kontext UE. V EPS se GUTI skládá z Globally Unique MME Identifier ([GUMMEI](/mobilnisite/slovnik/gummei/)) a MME-Temporary Mobile Subscriber Identity ([M-TMSI](/mobilnisite/slovnik/m-tmsi/)). GUMMEI jednoznačně identifikuje MME, které GUTI přidělilo, a M-TMSI je jedinečný identifikátor pro UE v rámci této MME. V 5GS ekvivalentní struktura zahrnuje Globally Unique AMF Identifier ([GUAMI](/mobilnisite/slovnik/guami/)) a [5G-TMSI](/mobilnisite/slovnik/5g-tmsi/). Tato struktura znamená, že když síťová entita obdrží zprávu s GUTI, může okamžitě určit, která MME/AMF je odpovědná za kontext UE.

Provozní životní cyklus GUTI zahrnuje přiřazení, znovupřiřazení a použití. Je přiřazena během počáteční registrace. Síť může znovu přiřadit nové GUTI během určitých procedur, jako jsou předávání spojení mezi MME/AMF nebo pro periodickou obnovu kvůli soukromí. UE ukládá své přiřazené GUTI do nevolatilní paměti, aby jej mohlo používat i po vypnutí a zapnutí napájení. Klíčovou procedurou využívající GUTI je identifikace. Pokud síťový uzel (například nová MME při předávání mezi MME) obdrží GUTI, které nerozpozná, použije vložené GUMMEI/GUAMI k dotazování staré MME/AMF o kontext UE a její trvalou identitu (IMSI/SUPI). Tento mechanismus umožňuje bezproblémovou mobilitu a přenos kontextu, přičemž stále chrání trvalou identitu na rádiovém spojení.

## K čemu slouží

GUTI byla zavedena primárně k řešení kritických problémů soukromí uživatelů spojených s trvalým IMSI. V dřívějších systémech 2G/3G bylo IMSI často odesíláno v nezašifrované podobě přes rádiové rozhraní, což je činilo zranitelným vůči odposlechu a sledování pasivními odposlouchávacími zařízeními. Útočník mohl shromažďovat IMSI za účelem profilace polohy, pohybů a zvyklostí uživatelů – což je závažné narušení soukromí. GUTI to řeší tím, že funguje jako pseudonym; citlivé IMSI/SUPI se přenáší pouze během výjimečných, zabezpečených počátečních procedur a je jinak nahrazeno dočasným GUTI.

Kromě ochrany soukromí slouží GUTI důležitým účelům síťové efektivity a provozu. Hierarchická struktura GUTI (GUMMEI/GUAMI + TMSI) poskytuje vestavěné směrovací informace. To umožňuje ostatním síťovým uzlům, jako jsou eNodeB/gNB nebo jiné MME/AMF, rychle určit 'kotvící' uzel jádrové sítě, který spravuje relaci UE, aniž by potřebovaly složité vyhledávání nebo broadcastové dotazy. Toto urychluje signalizační procedury, jako jsou předávání spojení a volání.

Konstrukce GUTI také podporuje škálovatelnost a vývoj síťové architektury. Oddělením dočasné identity od trvalé mohou operátoři nezávisle znovu přiřazovat GUTI (např. poté, co se UE přesune do oblasti nové MME/AMF). Tato flexibilita je klíčová pro vyrovnávání zatížení, optimalizaci sítě a distribuovanou povahu 5G jádrových sítí. GUTI je v podstatě základním kamenem pro zajištění bezpečného, efektivního a škálovatelného řízení mobility v moderních systémech 3GPP.

## Klíčové vlastnosti

- Dočasný identifikátor, který chrání trvalý SUPI/IMSI uživatele před vystavením na rádiovém přenosu.
- Hierarchická struktura obsahující globálně unikátní identifikátor síťového uzlu (GUMMEI/GUAMI) a lokální identifikátor UE (TMSI).
- Přiřazený MME (4G) nebo AMF (5G) během registrace a může být znovu přiřazen z důvodu mobility nebo ochrany soukromí.
- Používán jako primární identifikátor UE ve většině signalizačních procedur NAS a AS po počátečním připojení.
- Umožňuje efektivní směrování signalizačních zpráv a vyhledání kontextu mezi síťovými uzly.
- Uložen v nevolatilní paměti UE, aby si zachoval identitu i po vypnutí a zapnutí napájení.

## Související pojmy

- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [TMSI – Temporary Mobile Subscriber Identifier](/mobilnisite/slovnik/tmsi/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 31.117** (Rel-19) — USIM Application Toolkit Test for Non-Removable UICC
- **TS 31.127** (Rel-18) — UICC-terminal interaction testing specification
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [GUTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/guti/)
