---
slug: "adaes"
url: "/mobilnisite/slovnik/adaes/"
type: "slovnik"
title: "ADAES – Application Data Analytics Enablement Services"
date: 2026-01-01
abbr: "ADAES"
fullName: "Application Data Analytics Enablement Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/adaes/"
summary: "ADAES je rámec 3GPP umožňující vystavení analytických dat ze sítě aplikacím. Umožňuje aplikacím (Application Functions, AF) žádat a přijímat analytická data ze sítě, což napomáhá inteligentnějšímu cho"
---

ADAES je rámec 3GPP, který umožňuje vystavení analytických dat ze sítě aplikacím, což umožňuje aplikacím (Application Functions) žádat a přijímat analytická data za účelem inteligentnějšího chování aplikací a optimalizace.

## Popis

Application Data Analytics Enablement Services (ADAES) je standardizovaný rámec v architektuře 5G Core, který poskytuje mechanismus pro autorizované aplikace (Application Functions, [AF](/mobilnisite/slovnik/af/)) k vyžádání a příjmu analytických dat odvozených ze síťových dat. Slouží jako mezivrstva služeb, která vystavuje analytické schopnosti sítě externím aplikacím bezpečným a řízeným způsobem. Hlavními architektonickými komponentami jsou ADAES Provider (poskytovatel), což je logická funkce typicky umístěná společně nebo jako součást Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)) či jiných producentů analytiky, a ADAES Consumer (konzument), což je aplikace (AF) žádající o analytiku. Služba je vystavena prostřednictvím standardizovaných rozhraní založených na službách, primárně Nadaes (ADAES Services), jak je definováno v 3GPP TS 29.549.

Rámec ADAES funguje tak, že definuje sadu operací služeb, které umožňují aplikaci (AF, konzument) přihlásit se k odběru, vyžádat si nebo být informována o konkrétních analytických informacích. Žádosti o analytiku jsou vysoce přizpůsobitelné; aplikace (AF) může specifikovat typ analytiky (např. analytiku úrovně zatížení, analytiku mobility UE, analytiku udržitelnosti QoS), cíl analytiky (např. konkrétní skupinu UE, geografickou oblast, síťový řez) a požadované charakteristiky reportování (např. periodické, spouštěné událostí, okamžité). ADAES Provider tyto žádosti zpracovává, případně agreguje a analyzuje surová data z různých síťových funkcí, jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), než vrátí zpracované analytické výsledky aplikaci (AF).

Klíčovou rolí ADAES je oddělení produkce analytiky od její spotřeby. Standardizuje datové modely a procedury pro výměnu analytiky, čímž zajišťuje interoperabilitu mezi různými implementacemi síťové analytiky od různých dodavatelů a různorodými aplikacemi třetích stran. Poskytovaná analytika může zahrnovat metriky výkonnosti sítě, vzorce chování uživatelského zařízení (UE) až po predikce budoucích síťových podmínek. To umožňuje aplikacím (AF) činit inteligentní, daty řízená rozhodnutí, jako je úprava datového toku aplikace na základě predikované kongesce sítě nebo spouštění specifických akcí pro skupiny UE vykazující určité vzorce mobility.

Z procedurálního hlediska interakce typicky zahrnuje odběr a notifikaci. Aplikace (AF) se přihlásí k odběru analytické události odesláním požadavku Nadaes_AnalyticsSubscription_Create ADAES Providerovi. Odběr zahrnuje kritéria filtrování analytiky a zpětné volání [URI](/mobilnisite/slovnik/uri/) pro notifikace. ADAES Provider poté monitoruje síť pro specifikované podmínky. Když dojde k analytické události nebo je čas na periodický report, poskytovatel vygeneruje analytický report a odešle jej prostřednictvím zprávy Nadaes_AnalyticsSubscription_Notify na zpětné volání URI aplikace (AF). Tento asynchronní, událostmi řízený model je efektivní a škálovatelný. ADAES také podporuje přímé interakce typu request-response pro analytické dotazy na vyžádání bez odběru.

## K čemu slouží

ADAES byl vytvořen, aby řešil rostoucí potřebu aplikací být si vědomy stavu sítě a být kontextově inteligentní. Před jeho standardizací měly aplikace omezené, proprietární nebo žádné prostředky pro přístup k bohaté analytice odvozené z jádra mobilní sítě. Tento nedostatek standardizovaného vystavení bránil vývoji pokročilých služeb, které by se mohly dynamicky přizpůsobovat síťovým podmínkám, mobilitě uživatelů a kvalitě služeb v reálném čase. Motivace vychází z vize 5G umožnit vertikální průmysly a inovativní případy užití – jako je enhanced Mobile Broadband (eMBB), Ultra-Reliable Low-Latency Communications ([URLLC](/mobilnisite/slovnik/urllc/)) a massive Machine-Type Communications (mMTC) – které vyžadují hlubokou integraci mezi aplikacemi a síťovými schopnostmi.

Rámec řeší problém izolované síťové inteligence. Bez ADAES zůstávaly cenné poznatky generované uvnitř sítě (např. funkcí [NWDAF](/mobilnisite/slovnik/nwdaf/)) uzavřeny v doméně operátora. ADAES poskytuje bezpečnou, řízenou politikami a standardizovanou bránu pro vystavení těchto poznatků. To umožňuje vývojářům aplikací třetích stran a podnikovým aplikacím (AF) vytvářet služby, které proaktivně reagují na síťové události, optimalizují využití zdrojů a personalizují uživatelský zážitek. Například služba streamování videa může preventivně snížit kvalitu videa po obdržení analytické předpovědi o zahlcení buňky, nebo IoT platforma může přesměrovat provoz na základě predikcí mobility UE.

Historicky omezená programovatelnost aplikací a nedostatek otevřených rozhraní v předchozích generacích (4G/LTE) omezovaly takovou dynamickou synergii mezi sítí a aplikacemi. Zavedení ADAES v 3GPP Release-18 je přímou reakcí na tato omezení a formalizuje 'zpřístupnění' datové analytiky jako základní síťové služby. Souladí se širším principem architektury 3GPP pro vystavení sítě, doplňuje další služby vystavení, jako je Network Exposure Function (NEF), ale se specifickým, vyhrazeným zaměřením na analytická data. Tato specializace zajišťuje efektivní, škálovatelné a přizpůsobené interakce pro spotřebu analytiky, což se liší od obecného vystavení parametrů nebo řízení politik.

## Klíčové vlastnosti

- Standardizované vystavení analytiky odvozené ze sítě aplikacím (Application Functions, AF)
- Podpora pro odběrový (událostmi řízený) a request-response (dotazovací) model doručování analytiky
- Flexibilní filtrování analytiky pro cílové UE, geografické oblasti, síťové řezy a specifické typy analytiky
- Integrace se základními síťovými funkcemi, jako je NWDAF pro produkci analytiky a policy control pro autorizaci
- Využití rozhraní založených na službách (Nadaes) pro interoperabilní komunikaci mezi ADAES Provider a Consumer
- Podpora analytiky včetně úrovně zatížení, mobility UE, udržitelnosti QoS a poznatků o abnormálním chování

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.558** (Rel-19) — Edge Enabler APIs Stage 3
- **TS 24.559** (Rel-19) — Application Data Analytics Enablement Services
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications

---

📖 **Anglický originál a plná specifikace:** [ADAES na 3GPP Explorer](https://3gpp-explorer.com/glossary/adaes/)
