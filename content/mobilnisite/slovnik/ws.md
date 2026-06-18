---
slug: "ws"
url: "/mobilnisite/slovnik/ws/"
type: "slovnik"
title: "WS – Work Station"
date: 2025-01-01
abbr: "WS"
fullName: "Work Station"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ws/"
summary: "Výpočetní systém používaný provozovateli síťí a poskytovateli služeb k hostování aplikací pro provoz, administraci a údržbu (OA&M). Ve specifikacích 3GPP často označuje klientský terminál, ze kterého"
---

WS je výpočetní systém používaný provozovateli síťí k hostování a přístupu k aplikacím pro provoz, administraci a údržbu (OA&M) pro řízení síťových elementů.

## Popis

V architektuře 3GPP je Work Station (WS) definována jako terminál nebo výpočetní platforma operátora používaná pro účely provozu, administrace a údržby ([OA](/mobilnisite/slovnik/oa/)&M). Je klíčovou součástí modelu Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)), který 3GPP přijalo pro řízení síťí. WS poskytuje rozhraní člověk-stroj ([HMI](/mobilnisite/slovnik/hmi/)), prostřednictvím kterého administrátor a operátor síťí monitorují výkon síťí, konfigurují síťové elementy, zřizují služby a řeší poruchy. Hostuje klientskou část řídicích aplikací, které komunikují s agentním softwarem umístěným na řízených síťových elementech ([NE](/mobilnisite/slovnik/ne/)), jako jsou základové stanice (gNB, [eNB](/mobilnisite/slovnik/enb/)), uzly jádra síťí ([AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/)) a uživatelská zařízení (UE).

WS funguje v rámci hierarchického řídicího modelu. Typicky se nachází na úrovni řízení síťí ([NML](/mobilnisite/slovnik/nml/)) nebo řízení podnikání (BML) v hierarchii TMN. Komunikuje s systémy nižších úrovní – jako jsou element manažery (EM) nebo NE přímo – pomocí standardizovaných řídicích protokolů a rozhraní. Klíčové rozhraní zmíněné ve specifikacích 3GPP je Itf-N (Interface-Northbound), které je často založeno na protokolů jako CORBA nebo nověji RESTful API a NETCONF/YANG. WS sama běží řídicí software, který může prezentovat data prostřednictvím grafického uživatelského rozhraní (GUI), zpracovávat alarmy, generovat reporty a provádět automatizované skripty nebo workflow pro rutinní úkony.

Z technického pohledu není WS monolitická specifikace, ale funkční role. Její implementace může být od dedikovaného hardware konzole až po software aplikaci běžící na standardním PC nebo virtuálním stroji. Specifikace 3GPP, jako ty v řadě 29.199 (Open Service Access - OSA), definují jak externí aplikace (které mohou být hostované na WS) komunikují s síťovými schopnostmi. Role WS je klíčová pro praktický provoz síťí. Převádí vysoké podnikové a provozní politiky na specifické konfigurační příkazy vysílané přes řídicí plán a agreguje surové výkonové a poruchové data z tisíců síťových elementů do praktických informací pro operátora.

## K čemu slouží

Koncept Work Station ve standardizaci 3GPP řeší základní potřebu centralizovaného a standardizovaného bodu kontroly a sledování pro komplexní, multi-vendor mobilní síťí. V počátcích telekomunikací byly řídicí systémy často proprietární a těsně spojené s hardware vendora, vedoucí k provozním izolacím a vysokým integračním nákladům. Přijetí modelu TMN a definice role WS mělo za cíl oddělit řídicí funkci od síťové funkce, podporovat interoperabilitu a zjednodušený provoz.

Specifikace WS jako logické komponenty umožňuje 3GPP vývoj řídicích aplikací, které mohou pracovat přes síťové elementy různých vendorů, pokud podporují standardní rozhraní. Toto řeší problém vendor lock-in na řídicí úrovni a umožňuje operátorům vybrat nejlepší řídicí software. Také facilituje automatizaci síťového provozu, protože standardizované datové modely a protokoly umožňují WS aplikacím programově kontrolovat síť.

Evoluce od předchozích release odráží změnu řídicích technologií. Zpočátku interakce WS mohly být založeny na TL1 nebo CMIP/GDMO. Zahrnutí WS do specifikací jako 29.199 (od Release 5) pro OSA ukazuje její roli v umožnění zřizování služeb a řízení třetích stran. Časem fyzický koncept 'workstation' se vyvinul do více abstraktního 'řídicího systému' nebo 'orchestrátoru', ale jeho základní účel zůstává: poskytnout operátoru nástroje k efektivnímu řízení životního cyklu síťových služeb, od nasazení a konfigurace až po asurance a optimalizaci, tím zajistit síťovou reliabilitu, security a výkon.

## Klíčové vlastnosti

- Terminál operátora pro OA&M (provoz, administraci a údržbu)
- Poskytuje rozhraní člověk-stroj pro řízení síťí
- Hostuje klientské aplikace pro monitoring, konfiguraci a řízení poruch
- Komunikuje se síťovými elementy prostřednictvím standardizovaných řídicích rozhraní (např. Itf-N)
- Funguje v rámci hierarchické architektury TMN (Telecommunications Management Network)
- Lze použít pro zřizování služeb a přístup aplikací třetích stran (např. prostřednictvím OSA)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services

---

📖 **Anglický originál a plná specifikace:** [WS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ws/)
