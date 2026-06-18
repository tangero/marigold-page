---
slug: "pcc"
url: "/mobilnisite/slovnik/pcc/"
type: "slovnik"
title: "PCC – Performance-oriented Congestion Control"
date: 2026-01-01
abbr: "PCC"
fullName: "Performance-oriented Congestion Control"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pcc/"
summary: "PCC je rámec 3GPP pro dynamické řízení politik a účtování, primárně definovaný v architektuře PCC. Umožňuje operátorům spravovat síťové prostředky, vynucovat kvalitu služeb (QoS) a implementovat účtov"
---

PCC je rámec 3GPP pro dynamické řízení politik a účtování, který umožňuje operátorům spravovat prostředky, vynucovat QoS a implementovat účtovací pravidla na základě předplatného, typů služeb a stavu sítě.

## Popis

Performance-oriented Congestion Control (PCC, řízení přetížení orientované na výkon) je komplexní rámec ve standardech 3GPP, který poskytuje dynamické řízení politik a účtovací funkce pro služby založené na IP. Je klíčovou součástí Evolved Packet Core (EPC) v LTE a 5G systémech, přičemž jeho původ sahá k Release 7. Architektura PCC centralizuje rozhodování o QoS a účtování, což umožňuje síťovým operátorům uplatňovat přesnou kontrolu na uživatele a na datový tok služby. Jádro PCC tvoří klíčové funkční entity: Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)), Application Function ([AF](/mobilnisite/slovnik/af/)) a Subscription Profile Repository ([SPR](/mobilnisite/slovnik/spr/)) nebo Unified Data Repository ([UDR](/mobilnisite/slovnik/udr/)). Tyto prvky spolupracují na autorizaci prostředků, vynucování politik a zajištění odpovídajícího účtování na základě vstupů v reálném čase.

Rámec PCC funguje prostřednictvím řady standardizovaných rozhraní, především rozhraní Gx mezi PCRF a PCEF, rozhraní Rx mezi PCRF a AF a rozhraní Sy mezi PCRF a [OCS](/mobilnisite/slovnik/ocs/) (Online Charging System). Jeho činnost začíná zřízením [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network) relace uživatelským zařízením (UE). PCEF, typicky umístěná v Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v LTE nebo v SMF/UPF v 5G, detekuje relaci a požaduje politiky od PCRF přes Gx. PCRF následně rozhoduje na základě konsolidace informací z více zdrojů: dat o předplatiteli ze SPR/UDR (např. povolené služby, QoS profily), informací o službě od AF (např. požadovaná šířka pásma pro video stream) a stavu sítě z interních politik nebo Traffic Detection Function (TDF). Tato rozhodnutí pak poskytuje jako PCC pravidla PCEF k provedení.

Klíčové součásti PCC zahrnují PCC pravidla, což jsou sady informací umožňující detekci datového toku služby a definující parametry pro jeho zacházení. Každé PCC pravidlo obsahuje identifikátor pravidla, filtry datového toku služby (např. 5-tice IP filtrů), prioritu, parametry QoS (QCI, ARP, přenosové rychlosti), účtovací informace (způsob měření, účtovací klíč) a akce k provedení. PCEF používá tato pravidla k provádění hluboké kontroly paketů (DPI) za účelem identifikace toků, aplikaci QoS značení (nastavení DSCP nebo alokace prostředků přenosového kanálu), omezení rychlosti a generování záznamů o účtovaných datech (CDR) nebo interakci s online účtovacími systémy. To umožňuje detailní kontrolu, jako je upřednostnění VoIP provozu před běžným webovým prohlížením nebo aplikace zero-ratingu pro konkrétní aplikace.

Role PCC přesahuje základní QoS; je nedílnou součástí síťového řezání, edge computingu a automatizace sítě v 5G. V 5G Core přebírá roli PCRF funkce Policy Control Function (PCF), která komunikuje s Session Management Function (SMF) přes rozhraní N7. Principy PCC umožňují dynamické úpravy politik na základě SLA pro síťové řezy, změn lokace nebo událostí přetížení. Například při přetížení sítě může PCC omezit neesenciální provoz nebo nabídnout sponzorované datové služby. Rámec podporuje jak statické politiky (předkonfigurované), tak dynamické politiky (specifické pro relaci), což poskytuje operátorům flexibilitu pro inovace v nabídkách služeb při zachování síťového výkonu a monetizace.

## K čemu slouží

PCC bylo vytvořeno, aby řešilo omezení statických, předkonfigurovaných mechanismů řízení politik a účtování v dřívějších mobilních datových sítích (např. GPRS). Před PCC byly QoS a účtování často založeny na jednoduchém nastavení APN (Access Point Name) nebo profilech předplatitelů bez možnosti adaptace v reálném čase. Tato nepružnost ztěžovala operátorům nabízet diferencované služby, dynamicky spravovat síťové přetížení nebo implementovat sofistikované účtovací modely, jako jsou vrstvené datové tarify, zero-rating nebo sponzorovaná data. Exploze služeb založených na IP (streamování videa, VoIP, IoT) v polovině roku 2000 si vyžádala agilnější systém, který by dokázal reagovat na potřeby aplikací a stav sítě v reálném čase.

Primární problém, který PCC řeší, je efektivní a zpeněžitelné řízení vzácných síťových prostředků v prostředí různorodých typů provozu. Umožňuje operátorům vynucovat politiky sladěné s obchodními cíli – například zajistit prémiovým předplatitelům vysokou kvalitu videa, zatímco omezit vytížené uživatele během přetížení. PCC také usnadňuje inovace služeb tím, že umožňuje poskytovatelům aplikací třetích stran komunikovat se sítí prostřednictvím AF (např. přes rozhraní Rx) a žádat konkrétní QoS pro své služby, což umožňuje partnerství a nové zdroje příjmů. Jednalo se o posun paradigmatu od sítě jako pouhého přenosového kanálu k síti jako službě.

Historicky byl vývoj PCC v Release 7 motivován konvergencí služeb IMS (IP Multimedia Subsystem) a ne-IMS služeb přes paketově přepínané domény. Poskytl jednotný rámec řízení politik pro obě oblasti, nahrazující dřívější nesouvisející mechanismy, jako bylo rozhraní Go pro IMS. Jak se sítě vyvíjely k LTE a 5G, stalo se PCC ještě důležitějším kvůli zvýšeným objemům dat, požadavkům na nízkou latenci a síťovému řezání. Řešilo potřebu automatizace v rozhodování o politikách, snižovalo provozní náročnost a umožňovalo účtování v reálném čase pro služby na vyžádání. PCC tak tvoří základ ekonomiky moderního mobilního broadbandu, což operátorům umožňuje vyvážit výkon, spravedlnost a ziskovost v konkurenčním prostředí.

## Klíčové vlastnosti

- Dynamické rozhodování a vynucování politik na datový tok služby
- Integrace s daty předplatitele, požadavky aplikací a stavem sítě
- Podpora integrace online i offline účtování
- Detailní kontrola QoS včetně parametrů QCI, ARP a šířky pásma
- Schopnosti hluboké kontroly paketů pro detekci datových toků služeb
- Standardizovaná rozhraní (Gx, Rx, Sy) pro interoperabilitu více dodavatelů

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 23.803** (Rel-7) — PCC Architecture Harmonization Study
- … a dalších 54 specifikací

---

📖 **Anglický originál a plná specifikace:** [PCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcc/)
