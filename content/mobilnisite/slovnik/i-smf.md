---
slug: "i-smf"
url: "/mobilnisite/slovnik/i-smf/"
type: "slovnik"
title: "I-SMF – Intermediate Session Management Function"
date: 2026-01-01
abbr: "I-SMF"
fullName: "Intermediate Session Management Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/i-smf/"
summary: "I-SMF je funkce správy relace (Session Management Function) zavedená v 5G Core, která umožňuje lokální breakout a efektivní směrování dat pro UE, zejména v mobilních scénářích zahrnujících přístup pře"
---

I-SMF je mezilehlá funkce správy relace (Session Management Function) v 5G Core, která umožňuje lokální breakout a efektivní směrování dat tím, že spravuje cestu uživatelské roviny lokálně, odděleně od kotvící SMF (anchor SMF).

## Popis

Intermediate Session Management Function (I-SMF) je funkce jádra sítě v rámci 5G systému (5GS) definovaná od 3GPP Release 16. Jedná se o specializovanou instanci [SMF](/mobilnisite/slovnik/smf/) navrženou pro spolupráci s kotvící SMF (A-SMF). Hlavní architektonickou rolí I-SMF je poskytovat lokalizovanou správu relace, když se uživatelské zařízení (UE) připojuje přes přístupovou síť odlišnou od té, kterou obsluhuje jeho A-SMF, nebo když se UE přesune do lokality datové sítě vyžadující samostatnou cestu uživatelské roviny. V takových scénářích je I-SMF vložena do cesty řídicí roviny mezi funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a A-SMF.

Provozně je I-SMF zodpovědná za správu relace [PDU](/mobilnisite/slovnik/pdu/) (Protocol Data Unit) pro UE ve své lokální doméně. To zahrnuje interakci s lokální funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) – často mezilehlou UPF ([I-UPF](/mobilnisite/slovnik/i-upf/)) – pro správu uživatelské roviny, uplatňování lokálních politik a provádění signalizace související s relací s AMF. Klíčové je, že I-SMF přeposílá určité zprávy správy relace k A-SMF a od ní, přičemž A-SMF si ponechává celkovou odpovědnost za relaci PDU, včetně interakce s Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro předplatitelská data a s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) pro rozhodování o politikách. I-SMF v podstatě funguje jako proxy, což umožňuje A-SMF zůstat kotvícím bodem relace a zároveň delegovat lokální úlohy správy.

Mezi klíčové komponenty funkcionality I-SMF patří její rozhraní N11 k AMF, rozhraní N16 k A-SMF (pomocí služby Nsmf_PDUSession) a její rozhraní N4 k lokálně nasazené UPF. Provádí výběr lokální UPF, vytváří, upravuje a ruší N4 relace a uplatňuje pravidla QoS poskytnutá PCF přes A-SMF. Role I-SMF je zásadní pro umožnění efektivního směrování ve scénářích, jako je přístup k lokálním datovým sítím ([LADN](/mobilnisite/slovnik/ladn/)), propojení s non-3GPP sítěmi (např. Wireline Access) a při událostech mobility, kdy vložení bodu lokálního breakoutu snižuje latenci a přenosovou zátěž backhaulové sítě. Odděluje topologii lokálního přístupu od kotvícího bodu v jádru sítě, což poskytuje značnou flexibilitu v návrhu 5G sítí.

## K čemu slouží

I-SMF byla zavedena v Release 16, aby řešila specifické architektonické výzvy vyplývající ze služební architektury 5G Core a potřeby efektivní podpory edge computingu, přístupu přes non-3GPP sítě a komplexní mobility. Před jejím zavedením byla SMF monolitickou entitou spravující celou relaci PDU z jediného logického bodu. Tento model se stal neefektivním, když UE přistupovalo ke službám přes non-3GPP síť (jako WLAN) nebo se přesunulo do lokalizované servisní oblasti (jako tovární kampus). Provoz by musel být přenášen zpět ke kotvící UPF řízené A-SMF, což zbytečně zvyšovalo latenci a zatížení přenosové sítě jádra.

I-SMF to řeší tím, že umožňuje rozdělenou architekturu SMF. Umožňuje operátorům nasadit lokálně, blízko bodu připojení UE, odlehčenou instanci SMF. Tato lokální I-SMF může spravovat lokální cestu uživatelské roviny (přes I-UPF) pro breakout s nízkou latencí, zatímco A-SMF v centrálním cloudu udržuje kotvení relace a celkový kontext politik. Toto oddělení je obzvláště kritické pro podporu Ultra-Reliable Low-Latency Communications (URLLC) a efektivního Mobile Edge Computing (MEC), kde musí být funkce uživatelské roviny nasazeny na okraji sítě. Koncept I-SMF přímo řeší omezení jediné, centralizované SMF tím, že poskytuje topologickou flexibilitu a umožňuje efektivní směrování dat přizpůsobené aktuální poloze a typu přístupu UE.

## Klíčové vlastnosti

- Umožňuje lokální správu relace oddělenou od kotvící SMF (Anchor SMF)
- Funguje jako proxy pro signalizaci N1/N2 mezi AMF a A-SMF pro lokální zpracování relace PDU
- Vybírá a řídí lokální mezilehlou UPF (I-UPF) přes rozhraní N4
- Podporuje lokální uplatňování politik pro QoS a účtování
- Usnadňuje efektivní cesty uživatelské roviny pro edge computing a lokální breakout
- Nezbytná pro mobilní scénáře zahrnující propojení s non-3GPP přístupem

## Související pojmy

- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [I-UPF – Intermediate User Plane Function](/mobilnisite/slovnik/i-upf/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.726** (Rel-16) — SMF/UPF Topology Enhancements in 5G
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.542** (Rel-19) — SMF NIDD Service Based Interface Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 29.591** (Rel-19) — 5G NEF Southbound Services Stage 3
- **TR 29.820** (Rel-17) — Study on PFCP Best Practice
- **TS 29.892** (Rel-16) — Study on User Plane Protocol in 5GC
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [I-SMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/i-smf/)
