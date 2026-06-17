---
slug: "bss-a"
url: "/mobilnisite/slovnik/bss-a/"
type: "slovnik"
title: "BSS-A – Base Station System - Anchor"
date: 2025-01-01
abbr: "BSS-A"
fullName: "Base Station System - Anchor"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bss-a/"
summary: "BSS-A je zdrojový systém základnových stanic (Base Station System) během procedury GSM předání spojení (handover). Slouží jako kotvící bod, který udržuje spojení a zároveň koordinuje přenos mobilní st"
---

BSS-A je zdrojový systém základnových stanic (Base Station System), který slouží jako kotvící bod udržující spojení během procedury GSM předání spojení (handover) a koordinuje přenos k cílovému BSS.

## Popis

Systém základnových stanic – kotva (Base Station System - Anchor, BSS-A) je klíčový funkční prvek definovaný ve specifikacích 3GPP pro operace GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Při předání spojení mezi [BSS](/mobilnisite/slovnik/bss/) (inter-BSS handover) – kdy se mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) přesouvá z pokrytí jednoho systému základnových stanic do druhého – představuje BSS-A zdrojový BSS, který proceduru předání spojení iniciuje a řídí. Působí jako kotvící bod, který udržuje stávající spojení s jádrem sítě (konkrétně s Mobile Switching Center, [MSC](/mobilnisite/slovnik/msc/)) a zároveň koordinuje navázání nového rádiového spojení s cílovým BSS (BSS-T).

Role BSS-A je definována v přípravné a realizační fázi předání spojení popsané v 3GPP TS 23.009. Z architektonického hlediska se BSS-A skládá z řadiče základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) a základnových přenosových stanic ([BTS](/mobilnisite/slovnik/bts/)), které mobilní stanici aktuálně obsluhují. Když BSC rozhodne, že je předání spojení nutné (na základě měřicích hlášení od MS), určí sám sebe jako BSS-A. BSS-A následně komunikuje s cílovým BSS (BSS-T) prostřednictvím jádra sítě, typicky pomocí rozhraní [MAP](/mobilnisite/slovnik/map/)/E mezi MSC, pokud jsou BSS pod různými MSC, nebo přímo přes MSC, pokud jsou pod stejným. Odešle zprávu Handover Required k MSC, která ji přepošle jako Handover Request k BSS-T.

Během realizace předání spojení BSS-A dále zpracovává přenosy a signalizaci MS až do okamžiku, kdy MS úspěšně přistoupí na nový kanál v BSS-T. Je odpovědný za přeposlání jakýchkoli přenášených datových paketů k BSS-T, aby se zabránilo jejich ztrátě (funkce známá jako data forwarding). BSS-A také udržuje spojení na rozhraní A s MSC až do dokončení předání spojení, čímž zajišťuje kontinuitu služby. Po úspěšném předání spojení obdrží BSS-A příkaz k uvolnění a uvolní rádiové a terestrické prostředky dříve přidělené MS.

Tato kotvící funkce je klíčová pro předání spojení typu 'přeruš a pak navázat' (break-before-make), která jsou charakteristická pro GSM. Centralizuje řízení, zajišťuje, aby jádro sítě vnímalo stabilní bod připojení, a spravuje složitost přerozdělení prostředků mezi různými rádiovými přístupovými body. Tento koncept vytváří jasnou hierarchii a model odpovědnosti během událostí mobility, který se stal základním vzorem pro pozdější mechanismy předání spojení v 3G UMTS a dalších technologiích.

## K čemu slouží

Koncept BSS-A byl formalizován, aby vyřešil základní problém udržení kontinuity hovoru a datové relace, když se uživatel pohybuje mezi různými rádiovými buňkami řízenými samostatnými systémy základnových stanic. Před standardizovanými procedurami předání spojení byla mobilita omezena na buňky v rámci stejného BSS (intra-BSS handover). Model BSS-A/BSS-T umožnil předání spojení mezi BSS a mezi MSC, což bylo nezbytné pro budování rozsáhlých souvislých celulárních sítí.

Řešil technickou výzvu 'kdo má řídicí roli' během složitého předání spojení řízeného sítí. Určením kotvy (BSS-A) systém zajišťuje jediný odpovědný bod za koordinaci s jádrem sítě, správu starého rádiového spoje a usnadnění navázání nového. Tím se předchází konfliktům, zjednodušuje signalizace a poskytuje jasný stavový automat pro proces předání spojení. Kotvící model také napomáhá funkcím jako je přeposílání dat (data forwarding) pro paketově orientované služby, kde BSS-A může data ukládat do vyrovnávací paměti a přesměrovávat je na novou cestu.

Historicky šlo o klíčový vývoj od jednodušších, lokalizovanějších předání spojení. Umožnil operátorům nasazovat sítě s více, případně různorodými, oblastmi BSS při zachování plynulé služby. Role BSS-A je základním kamenem paradigmatu předání spojení řízeného sítí (Network Controlled Handover, NCHO) v GSM, kde síť rozhoduje o předání spojení na základě měření od MS, což kontrastuje s pozdějšími přístupy řízenými mobilním zařízením v některých technologiích.

## Klíčové vlastnosti

- Slouží jako řídicí a kotvící entita během přípravy a realizace předání spojení mezi BSS
- Udržuje spojení na rozhraní A k MSC po celou dobu procedury předání spojení
- Iniciuje předání spojení odesláním zprávy Handover Required k MSC
- Odpovídá za přeposílání dat (data forwarding) k cílovému BSS za účelem minimalizace ztráty paketů
- Uvolňuje rádiové a terestrické prostředky až po potvrzení dokončení předání spojení
- Poskytuje stabilní referenční bod pro jádro sítě během události mobility účastníka

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs

---

📖 **Anglický originál a plná specifikace:** [BSS-A na 3GPP Explorer](https://3gpp-explorer.com/glossary/bss-a/)
