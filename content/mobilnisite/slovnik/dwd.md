---
slug: "dwd"
url: "/mobilnisite/slovnik/dwd/"
type: "slovnik"
title: "DWD – Distribution Window Description"
date: 2025-01-01
abbr: "DWD"
fullName: "Distribution Window Description"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dwd/"
summary: "Datová struktura používaná ve specifikacích 3GPP k definování načasování a vzoru pro distribuci dat nebo řídicích informací v bezdrátové síti. Je klíčová pro plánování a alokaci prostředků, zajišťuje"
---

DWD je datová struktura používaná ve specifikacích 3GPP k definování načasování a vzoru pro distribuci dat nebo řídicích informací v bezdrátové síti.

## Popis

Distribution Window Description (DWD) je soubor parametrů definovaný v technických specifikacích 3GPP, konkrétně v kontextu mechanismů distribuce dat. Slouží jako formální popis, který vymezuje časové charakteristiky – jako jsou okna, periody nebo vzory – pro doručování datových paketů nebo informací řídicí roviny. Tento popis je typicky využíván síťovými plánovacími funkcemi ke koordinaci toho, kdy a jak jsou informace přenášeny k uživatelskému zařízení (UE) nebo mezi síťovými uzly.

Architektonicky je DWD vložen do protokolů vyšších vrstev nebo konfiguračních zpráv. Nejde o fyzický kanál, ale o logický popis, který řídí chování procesů distribuce dat. Klíčové komponenty DWD zahrnují parametry definující počáteční čas, dobu trvání, periodu opakování a případně granularitu nebo fázování distribučních oken. Tyto parametry umožňují síti plánovat alokaci prostředků předem, sladit přenosy s dostupnými rádiovými prostředky a schopnostmi UE.

Při provozu síťová entita (např. základnová stanice nebo centrální jednotka) generuje nebo konfiguruje DWD na základě požadavků služby, vytížení sítě a politik kvality služby (QoS). Tento popis je pak předán příslušným přijímajícím entitám, ať už uvnitř sítě, nebo k UE, aby synchronizovaly své přijímací nebo zpracovatelské aktivity. Například může definovat, kdy má UE naslouchat konkrétním aktualizacím systémových informací, nebo kdy má distribuovaná jednotka očekávat dávky dat od centrální jednotky v disaggregační architektuře RAN.

Její role v síti spočívá ve zvýšení předvídatelnosti a efektivity. Explicitním popisem distribučních oken síť snižuje nejednoznačnost a signalizační režii pro dynamické plánování. Umožňuje determinističtější datové toky, což je zvláště důležité pro služby s přísnými požadavky na latenci nebo spolehlivost, jako jsou ty v průmyslovém IoT nebo scénářích ultra-spolehlivé nízkolatenční komunikace ([URLLC](/mobilnisite/slovnik/urllc/)). DWD funguje jako smlouva mezi distributorem a příjemcem, zajišťující, že obě strany mají společný pohled na přenosový plán.

## K čemu slouží

Distribution Window Description byl zaveden k řešení potřeby strukturovanějších a efektivnějších plánovacích mechanismů v moderních celulárních sítích, zejména když se služby staly rozmanitějšími a náročnějšími. Předchozí přístupy často spoléhaly na dynamičtější plánování na úrovni paketů nebo na periodické, ale pevné časovače, což mohlo vést k neefektivitám, zvýšené signalizaci nebo nepředvídatelné latenci za měnících se síťových podmínek.

Její vytvoření bylo motivováno vývojem směrem k síťovým architekturám vyžadujícím přesnou koordinaci, jako je Cloud RAN (C-RAN) a disagregované základnové stanice (např. rozdělení gNB-CU a gNB-DU v 5G). V těchto architekturách musí být distribuce dat mezi centrálními a distribuovanými jednotkami přísně řízena, aby splnila omezení latence přístupové části (fronthaul) a požadavky na synchronizaci. DWD poskytuje standardizovaný způsob popisu těchto distribučních vzorů, umožňující interoperabilitu mezi zařízeními od různých výrobců.

Dále, jak se systémy 3GPP rozšířily o podporu nových kategorií služeb, jako je komunikace s masivním počtem strojových zařízení (mMTC) a vylepšené mobilní širokopásmové připojení (eMBB), stala se potřeba efektivního využití prostředků prvořadou. DWD umožňuje předplánování oken pro prostředky, snižuje potřebu nepřetržité signalizace pro přidělení (grant) a umožňuje lepší výdrž baterie pro IoT zařízení díky předvídatelným cyklům spánku. Řeší problém koordinace sporadických, ale časově citlivých doručení dat škálovatelným způsobem.

## Klíčové vlastnosti

- Definuje časové parametry pro okna distribuce dat
- Umožňuje předvídatelnou a naplánovanou alokaci prostředků
- Snižuje signalizační režii dynamického plánování
- Podporuje koordinaci v disagregovaných architekturách RAN
- Usnadňuje efektivní úsporu energie UE prostřednictvím známých plánů příjmu
- Standardizovaný formát zajišťující interoperabilitu mezi více výrobci

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [DWD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dwd/)
