---
slug: "fl"
url: "/mobilnisite/slovnik/fl/"
type: "slovnik"
title: "FL – Federated Learning"
date: 2026-01-01
abbr: "FL"
fullName: "Federated Learning"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fl/"
summary: "Federated Learning je distribuované paradigma strojového učení, ve kterém je globální model trénován kolaborativně na více decentralizovaných zařízeních nebo síťových uzlech (jako UE nebo základnové s"
---

FL je distribuovaný paradigmat strojového učení, ve kterém je globální model trénován kolaborativně na více decentralizovaných zařízeních nebo síťových uzlech bez výměny nezpracovaných dat.

## Popis

Federated Learning (FL) je decentralizovaný rámec strojového učení standardizovaný v rámci 3GPP, který umožňuje trénování modelů umělé inteligence ([AI](/mobilnisite/slovnik/ai/)) a strojového učení ([ML](/mobilnisite/slovnik/ml/)) napříč ekosystémem mobilní sítě a zároveň řeší omezení související s ochranou soukromí dat a jejich přenosem. V typické 3GPP architektuře FL koordinuje proces učení centrální server známý jako Federated Learning Server (FL Server). Tento server inicializuje globální ML model (např. pro správu rádiových zdrojů, optimalizaci mobility nebo predikci kvality služby) a distribuuje tento model zapojeným FL klientům. Těmito klienty jsou typicky uživatelská zařízení (UE), ale mohou jimi být také síťové funkce jako základnové stanice (gNB) nebo uzly edge computingu.

Jádrem operačního procesu je vícekolová spolupráce. V každém kole FL Server vybere sadu klientů a zašle jim aktuální globální model. Každý vybraný klient následně provede lokální trénink na svém vlastním privátním datovém souboru, který nikdy neopustí zařízení. Tento lokální trénink vypočítá aktualizaci modelu, typicky ve formě vah modelu nebo gradientů. Pouze tato kompaktní aktualizace modelu, nikoli nezpracovaná data, je odeslána zpět na FL Server. Server poté agreguje všechny přijaté aktualizace (pomocí algoritmů jako je Federated Averaging) a vytvoří vylepšený globální model. Tento cyklus se opakuje a globální model se postupně zdokonaluje na základě kolektivní znalosti z datových distribucí všech zapojených klientů.

Klíčovými komponentami v systému FL dle 3GPP jsou FL klient (entita provádějící lokální trénink), FL server (řídící proces) a systém pro správu FL, který zajišťuje výběr klientů, poskytování zdrojů a správu životního cyklu. Specifikace 3GPP definují potřebné protokoly a rozhraní, jako jsou servisně orientovaná rozhraní pro správu FL a přenos dat. Role FL v síti je transformační, neboť umožňuje vytváření inteligentních síťových a servisních funkcí, které se učí z reálných, distribuovaných dat generovaných na okraji sítě – jako jsou podmínky rádiového kanálu, pohybové vzorce nebo využívání aplikací – aniž by byla ohrožena soukromí uživatelů nebo přetížena přenosová síť masivními datovými přenosy. Mění tak celou síť zařízení v kolektivní, na soukromí ohleduplný tréninkový engine AI.

## K čemu slouží

Federated Learning byl do standardů 3GPP zaveden, aby vyřešil dva hlavní problémy vlastní centralizaci dat pro síťovou [AI](/mobilnisite/slovnik/ai/): ochranu/suverenitu dat a obrovskou režii přenosu dat. Tradiční [ML](/mobilnisite/slovnik/ml/) založené na cloudu vyžaduje agregaci obrovského množství nezpracovaných uživatelských a síťových dat v centrálním datovém centru, což přináší významné obavy o soukromí, regulační překážky (jako GDPR) a bezpečnostní rizika z úniků dat. Navíc přenos všech nezpracovaných dat z miliard UE a síťových uzlů do centrálního cloudu je z hlediska síťové šířky pásma a latence neúměrně nákladný.

Motivace pro jeho vytvoření vychází z tlaku průmyslu směrem k vestavěné inteligenci (Network Data Analytics Function - [NWDAF](/mobilnisite/slovnik/nwdaf/), [AI/ML](/mobilnisite/slovnik/ai-ml/) v 5G-Advanced a 6G) a z potřeby využít exponenciálně rostoucí data na okraji sítě. Předchozí přístupy buď tato distribuovaná data ignorovaly, nebo se pokoušely o složité a často nevyhovující techniky anonymizace a agregace dat. FL představuje zásadní architektonický posun. Tato omezení řeší přesunutím výpočtu k datům, nikoli přesunem dat k výpočtu. To umožňuje sítím 3GPP vytvářet přesné, zobecněné AI modely pro optimalizaci a automatizaci – jako je predikce zatížení buňky, řízení předávání hovorů nebo detekce anomálií – učením přímo ze zkušeností uživatelů a síťových podmínek na zařízeních a základnových stanicích, a to vše při zachování citlivých informací v lokálním uložení. Umožňuje spolupráci s ochranou soukromí v měřítku nezbytném pro budoucí autonomní sítě.

## Klíčové vlastnosti

- Decentralizované trénování modelů na UE a síťových uzlech bez výměny nezpracovaných dat
- Od návrhu zaměřené na ochranu soukromí v souladu s předpisy na ochranu dat (GDPR)
- Snižuje provoz v jádru sítě přenosem pouze kompaktních aktualizací modelu
- Podporuje heterogenní distribuce dat mezi klienty (ne-IID data)
- Zahrnuje mechanismy pro výběr klientů, vyjednávání zdrojů a bezpečnou agregaci
- Umožňuje optimalizaci sítě a služeb v reálném čase s využitím dat generovaných na okraji sítě

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.874** (Rel-18) — Technical Report
- **TS 23.288** (Rel-20) — 5GS Architecture Enhancements for Data Analytics
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.560** (Rel-19) — AIML Enablement (AIMLE) Services Stage 3 Protocol
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TS 28.105** (Rel-19) — AI/ML Management for 5GS
- **TS 28.858** (Rel-19) — AI/ML Management Phase 2 Study
- **TS 29.482** (Rel-19) — SEAL AIMLE Services Stage 3 Protocol
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [FL na 3GPP Explorer](https://3gpp-explorer.com/glossary/fl/)
