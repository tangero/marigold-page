---
slug: "sblp"
url: "/mobilnisite/slovnik/sblp/"
type: "slovnik"
title: "SBLP – Service Based Local Policy"
date: 2025-01-01
abbr: "SBLP"
fullName: "Service Based Local Policy"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sblp/"
summary: "SBLP je rámec pro řízení politik ke správě interakcí založených na službách v rámci 5G jádra sítě. Umožňuje dynamické vynucování politik na síťových funkcích, čímž zajišťuje, že QoS, účtování a řízení"
---

SBLP je rámec pro řízení politik určený ke správě interakcí založených na službách a umožňující dynamické vynucování politik týkajících se QoS, účtování a řízení přístupu v rámci 5G jádra sítě.

## Popis

Service Based Local Policy (SBLP) je základní mechanismus pro řízení politik v architektuře 3GPP 5G systému, navržený k řízení chování síťových funkcí ([NF](/mobilnisite/slovnik/nf/)) v prostředí rozhraní založeného na službách ([SBI](/mobilnisite/slovnik/sbi/)). Na rozdíl od tradičních rámců, které spoléhaly na centralizované, monolitické politické servery, SBLP distribuuje schopnosti vynucování politik přímo jednotlivým NF, jako je Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). Toho je dosaženo vložením logiky pro rozhodování o politikách do těchto funkcí, což jim umožňuje interpretovat a aplikovat politiky lokálně na základě standardizovaných pravidel politik poskytnutých funkcí Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)). PCF zůstává centrální autoritou pro politiky, zodpovědnou za vytváření, ukládání a distribuci pravidel politik spotřebitelským NF prostřednictvím služebního rozhraní Npcf. Tato pravidla jsou typicky vyjádřena ve strukturovaném formátu, jako je [JSON](/mobilnisite/slovnik/json/), a mohou určovat parametry pro Quality of Service (QoS), účtování, řízení přístupu a směrování provozu.

Činnost SBLP začíná, když síťová funkce potřebuje rozhodnutí o politice, například během zřizování Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)) session. Spotřebitelská NF (např. SMF) odešle požadavek na politiku PCF, který jej vyhodnotí vůči datům účastníka, stavu sítě a politikám definovaným operátorem. PCF poté vrátí sadu pravidel politik přizpůsobenou danému kontextu. Spotřebitelská NF tato pravidla uloží lokálně a vynucuje je v reálném čase po dobu trvání session nebo dokud není spuštěna aktualizace politiky. Akce vynucení mohou zahrnovat nastavení deskriptorů QoS Flow (QFD), aplikaci pravidel účtování, povolení nebo zakázání určitých služeb nebo přesměrování provozu. Klíčovým architektonickým principem je, že PCF přímo neřídí NF; místo toho poskytuje deklarativní politiky, které NF autonomně interpretuje a provádí, čímž se snižuje latence a signalizační režie pro častá, lokalizovaná rozhodnutí.

Role SBLP je nedílnou součástí cloud-nativního, na mikroslužbách založeného designu 5G jádra. Podporuje síťové slicing tím, že umožňuje vynucování politik specifických pro slice na úrovni NF, čímž zajišťuje izolaci a záruky výkonu. Také umožňuje dynamickou adaptaci politik v reakci na síťové události, jako je zahlcení nebo změna polohy uživatele, prostřednictvím schopnosti PCF zasílat aktualizované politiky. Rámec se spoléhá na standardizovaná služební rozhraní (např. Npcf) a společné datové modely definované v OpenAPI specifikacích, což zajišťuje interoperabilitu mezi NF od různých dodavatelů. Díky decentralizaci vynucování politik SBLP zvyšuje škálovatelnost, snižuje závislost na jediném bodě selhání a usnadňuje rychlejší inovace služeb, protože nové politiky lze nasadit bez přepracování celé síťové architektury.

## K čemu slouží

SBLP byl vytvořen, aby řešil omezení dřívějších architektur pro řízení politik, jako je rámec Policy and Charging Control (PCC) používaný v 4G EPC, který byl více centralizovaný a rigidní. V 4G většinu rozhodnutí o politikách činila funkce Policy and Charging Rules Function (PCRF) a sdělovala je prostřednictvím rozhraní Gx funkci Policy and Charging Enforcement Function (PCEF) v PGW. Tento model vytvářel úzká místa a zvyšoval latenci, protože každé rozhodnutí o politice vyžadovalo signalizaci k PCRF. Také se potýkal s podporou dynamických, na službách založených interakcí vyžadovaných pro cloud-nativní jádro 5G, síťový slicing a edge computing.

Hlavní motivací pro SBLP bylo umožnit flexibilnější, škálovatelnější a efektivnější rámec pro politiky v souladu s architektonickými principy 5G. 5G zavádí architekturu založenou na službách (SBA), kde NF interagují prostřednictvím API založených na HTTP/2. SBLP toho využívá tím, že z řízení politik dělá nativní službu, což umožňuje jakékoli NF spotřebovávat rozhodnutí o politikách. Tato decentralizace řeší problém škálovatelnosti tím, že umožňuje lokální vynucování, což je klíčové pro aplikace s nízkou latencí a masivní nasazení IoT. Také zjednodušuje integraci nových služeb a síťových slicingů, protože politiky mohou být přizpůsobeny a vynucovány na úrovni jednotlivých NF nebo slicingů bez neustálé centrální intervence.

Historicky se SBLP vyvinul z rámce PCC, přičemž zachoval oddělení rozhodování o politikách (PCF) a vynucování, ale distribuoval logiku vynucování. Byl představen v 3GPP Release 15 jako součást specifikace 5G systému pro podporu pokročilých případů užití, jako je síťový slicing, řetězení služeb a multi-access edge computing (MEC). Tím, že řeší problémy centralizace a latence, SBLP umožňuje operátorům automatizovat síťové operace, implementovat komplexní smlouvy o úrovni služeb (SLA) a rychle nasazovat nové výnosové služby softwarově definovaným způsobem.

## Klíčové vlastnosti

- Decentralizované vynucování politik na síťových funkcích
- Deklarativní pravidla politik poskytovaná funkcí Policy Control Function (PCF)
- Podpora dynamických aktualizací politik prostřednictvím služebních rozhraní
- Integrace se síťovým slicingem 5G pro politiky specifické pro slice
- Umožňuje rozhodování o politikách s nízkou latencí pro aplikace v reálném čase
- Používá standardizované OpenAPI datové modely pro interoperabilitu

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.803** (Rel-7) — PCC Architecture Harmonization Study
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.247** (Rel-19) — IMS Messaging Service Protocol Details
- **TS 24.819** (Rel-7) — IMS Services via Fixed Broadband Access
- **TR 24.930** (Rel-19) — IMS Session Setup Signalling Flows

---

📖 **Anglický originál a plná specifikace:** [SBLP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sblp/)
