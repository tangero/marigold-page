---
slug: "dc-af"
url: "/mobilnisite/slovnik/dc-af/"
type: "slovnik"
title: "DC-AF – Data Collection Application Function"
date: 2025-01-01
abbr: "DC-AF"
fullName: "Data Collection Application Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dc-af/"
summary: "Data Collection AF je síťová funkce zavedená v 5G za účelem standardizace a automatizace sběru dat o výkonu od síťových funkcí a uživatelských zařízení. Poskytuje centralizovaný, politikami řízený rám"
---

DC-AF je síťová funkce 5G, která standardizuje a automatizuje sběr dat o výkonu od síťových funkcí a uživatelských zařízení pro monitorování, optimalizaci a zajištění služeb.

## Popis

Data Collection Application Function (DC-AF) je klíčovou součástí architektury 5G založené na službách ([SBA](/mobilnisite/slovnik/sba/)), konkrétně součástí rámce Management Data Analytics ([MDA](/mobilnisite/slovnik/mda/)) definovaného 3GPP. Funguje jako centralizovaný bod pro řízení politik a orchestrátor úloh sběru dat napříč 5G Core Network (5GC) a v některých nasazeních i Radio Access Network (RAN). DC-AF komunikuje s ostatními síťovými funkcemi, jako je Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)), Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a různými producenty dat (např. [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/)), pomocí standardizovaných rozhraní založených na službách (např. Ndcaf_DataCollectionProvisioning, Ndcaf_DataReporting). Jejím hlavním úkolem je převádět vysokou úroveň analytických nebo monitorovacích požadavků – často přijímaných z Operations Support System ([OSS](/mobilnisite/slovnik/oss/)), Business Support System (BSS) operátora nebo z aplikační funkce (AF) spotřebitele – na konkrétní úlohy sběru dat.

Architektonicky DC-AF funguje tak, že přijímá požadavky na sběr dat, které specifikují, jaká data se mají sbírat (např. konkrétní KPI, události), od koho (cílové síťové funkce nebo UE), za jakých podmínek (spouštěče jako prahové hodnoty nebo periodické intervaly) a kam mají být sebraná data doručena (např. do NWDAF pro analýzu nebo do externí AF). Následně tyto zásady sběru zajišťuje pro příslušné producenty dat prostřednictvím svých jižních rozhraní. Tito producenti jsou vybaveni klienty pro sběr dat, kteří tyto zásady provádějí, shromažďují specifikovaná data a hlásí je zpět určenému příjemci dat (Data Collection Consumer), kterým může být samotná DC-AF, NWDAF nebo jiná autorizovaná entita. DC-AF spravuje životní cyklus těchto úloh sběru, včetně aktivace, změny, pozastavení a ukončení.

Klíčové součásti fungování DC-AF zahrnují službu Data Collection Provisioning Service, která se zabývá vytvářením a správou úloh sběru, a službu Data Reporting Service, která může přijímat a předávat sebraná data. Využívá Common API Framework (CAPIF) od 3GPP pro zabezpečenou expozici a objevování služeb. DC-AF je definována tak, aby podporovala širokou škálu datových typů, včetně měření výkonu (např. latence, propustnost, míra chyb), událostí mobility, událostí správy relací a analytických dat uživatelských zařízení (UE). Může sbírat data na základě jednotlivého UE, jednotlivého síťového řezu nebo agregovaně napříč skupinou UE nebo síťových funkcí.

V širším síťovém ekosystému hraje DC-AF klíčovou roli při umožňování daty řízené automatizace a inteligence. Poskytnutím standardizovaného, automatizovaného mechanismu pro sběr dat na vyžádání odstraňuje potřebu ruční, ad-hoc konfigurace sond nebo systémů protokolování na jednotlivých síťových funkcích. Tím se snižuje provozní zátěž a zajišťuje konzistence dat sebraných pro analytické účely. DC-AF je základním prvkem pro uzavřenou smyčku automatizace, optimalizaci sítě řízenou AI/ML a proaktivní zajištění služeb v samostatných sítích 5G (SA).

## K čemu slouží

DC-AF byla vytvořena, aby řešila rostoucí složitost a náročnost na data v sítích 5G. Předchozí generace (4G/LTE) se při sběru dat o výkonu sítě a uživatelském zážitku silně spoléhaly na proprietární, dodavatelsky specifická řešení a manuální procesy. Operátoři často nasazovali samostatné systémy sond nebo spoléhali na nekonzistentní protokolování od síťových prvků, což vedlo k fragmentovaným datovým úložištím, vysokým nákladům na integraci a pomalému získávání poznatků. Tento přístup byl nedostatečný pro dynamické případy užití 5G – jako je síťové krájení (network slicing), ultra spolehlivá komunikace s nízkou latencí (URLLC) a masivní IoT – které vyžadují data v reálném čase, podrobná a korelovaná z více síťových domén pro efektivní zajištění služeb a optimalizaci.

Hlavní motivací pro standardizaci DC-AF ve 3GPP Release 17 bylo poskytnout jednotný, otevřený a automatizovaný rámec pro sběr dat v architektuře 5G založené na službách. Řeší problém, jak efektivně shromažďovat správná data ze správných zdrojů ve správný čas pro napájení pokročilých analytických nástrojů, jako je NWDAF. Definováním standardního API a modelu politik umožňuje DC-AF interoperabilitu mezi zařízeními od různých dodavatelů a umožňuje aplikacím třetích stran (prostřednictvím NEF) požadovat sběr dat kontrolovaným způsobem. To podporuje inovace v síťové analýze a umožňuje nové obchodní modely, kde mohou operátoři vystavovat síťové poznatky vertikálním odvětvím.

DC-AF dále řeší problémy škálovatelnosti a efektivity. V síti 5G s miliony zařízení a četnými síťovými řezy je manuální konfigurace sběru dat na řez nebo službu nepraktická. Politikami řízená automatizace DC-AF umožňuje operátorům definovat šablony sběru a dynamicky je aplikovat na základě síťových podmínek nebo požadavků služby. Tím se snižují provozní výdaje (OPEX) a umožňuje síti samostatně se optimalizovat na základě sebraných dat, což směřuje k bezdotykové správě sítě a služeb (ZSM).

## Klíčové vlastnosti

- Standardizovaná rozhraní založená na službách (Ndcaf_DataCollectionProvisioning, Ndcaf_DataReporting) pro interoperabilní řízení sběru dat
- Řízení úloh sběru dat pomocí politik s podporou aktivace, změny, pozastavení a ukončení
- Podpora různých cílů sběru dat včetně síťových funkcí (NF), uživatelských zařízení (UE) a síťových řezů
- Flexibilní spouštěče sběru včetně periodických intervalů, podmínek založených na událostech a překročení prahových hodnot
- Integrace s Network Data Analytics Function (NWDAF) a Network Exposure Function (NEF) pro analýzu a expozici třetím stranám
- Využití Common API Framework (CAPIF) pro zabezpečenou registraci služeb, jejich objevování a autorizaci

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 24.559** (Rel-19) — Application Data Analytics Enablement Services
- **TS 26.532** (Rel-19) — 5G Data Collection and Reporting API Specification

---

📖 **Anglický originál a plná specifikace:** [DC-AF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dc-af/)
