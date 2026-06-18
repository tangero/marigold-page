---
slug: "tt"
url: "/mobilnisite/slovnik/tt/"
type: "slovnik"
title: "TT – Technical Trigger"
date: 2026-01-01
abbr: "TT"
fullName: "Technical Trigger"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tt/"
summary: "Standardizovaná událost nebo podmínka používaná v síťovém managementu 3GPP k automatickému zahájení specifických akcí, jako jsou měření výkonu, obnova po poruše nebo změny konfigurace. Umožňuje automa"
---

TT (Technická spoušť) je standardizovaná událost nebo podmínka používaná v síťovém managementu 3GPP k automatickému zahájení specifických akcí, což umožňuje automatizovaný a proaktivní provoz a údržbu sítě.

## Popis

Technická spoušť (TT) ve standardech 3GPP je formálně definovaný mechanismus v rámci frameworku Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), který způsobí provedení předdefinované akce při splnění specifické technické podmínky. Funguje jako pravidlo typu 'jestliže-pak' v systémech síťového managementu. Podmínka neboli spouštěcí bod je založena na monitorování síťových parametrů, metrik výkonu, indikací poruch nebo jiných technických událostí. Když monitorovaná hodnota překročí práh, vstoupí do specifického stavu nebo odpovídá vzoru, spoušť se aktivuje a přidružená akce se provede. Tyto akce mohou zahrnovat zaznamenání dat a generování notifikací až po spouštění složitých skriptů pro nápravu, rekonfiguraci síťových elementů nebo zahájení nových měření výkonu.

Architektonicky jsou Technické spouště implementovány v systémech Network Management ([NM](/mobilnisite/slovnik/nm/)) a Element Management ([EM](/mobilnisite/slovnik/em/)), jak je definováno v technických specifikacích (TS) 3GPP pro management, například v řadě TS 32. Jsou klíčovou součástí management modelu Fault, Configuration, Accounting, Performance, and Security (FCAPS). TT se typicky skládá z několika klíčových komponent: definice spouštěcí podmínky (např. 'vytížení [CPU](/mobilnisite/slovnik/cpu/) > 90 % po dobu 5 minut'), detekčního mechanismu (monitorovací funkce, která podmínku vyhodnocuje), seznamu akcí (soubor operací k provedení po aktivaci) a administrativních ovládacích prvků (stav povoleno/zakázáno, priorita). Tyto spouště mohou být konfigurovány staticky operátory sítě nebo dynamicky prostřednictvím management rozhraní jako je Itf-N.

Provoz Technické spouště zahrnuje kontinuální nebo periodické monitorování spravovaných objektů v síti. Tyto objekty mohou být fyzické síťové funkce (např. gNB), virtualizované síťové funkce ([VNF](/mobilnisite/slovnik/vnf/)), logická rozhraní nebo kolekce měření výkonu. Například TT může být nastavena pro monitorování míry 'Radio Link Failure' ([RLF](/mobilnisite/slovnik/rlf/)) na buňce. Pokud míra překročí kritický práh, spoušť může automaticky zahájit detailní trasování na postižených UE, generovat alarm pro Network Operations Center (NOC) a dokonce spustit samoléčící proceduru, která upraví parametry anténního náklonu. V automatizovaných sítích jsou TT nedílnou součástí uzavřené smyčky automatizace, kde vstupují do orchestračních systémů, které mohou provádět složité pracovní postupy bez lidského zásahu.

Technické spouště hrají klíčovou roli v moderních paradigmatech síťového managementu, jako jsou Self-Organizing Networks ([SON](/mobilnisite/slovnik/son/)) a zero-touch network and service management (ZSM). Poskytují 'senzorickou' schopnost, která informuje autonomní rozhodování. Například v Energy Saving Management ([ESM](/mobilnisite/slovnik/esm/)) může TT založená na nízkém síťovém vytížení spustit vypnutí určitých komponent nosné nebo buněk. Ve výkonnostním managementu může TT detekující degradaci Key Performance Indicators (KPI), jako je propustnost nebo latence, automaticky spustit kampaň pro analýzu hlavní příčiny. Formalizací těchto spouští ve specifikacích 3GPP je zajištěna interoperabilita mezi více-dodavatelskými management systémy a síťovými elementy, což umožňuje konzistentní a spolehlivé automatizované operace v celém síťovém ekosystému.

## K čemu slouží

Koncept Technické spouště byl vyvinut pro řešení rostoucí složitosti a rozsahu mobilních sítí, což činilo čistě manuální provoz a údržbu nepraktickou, náchylnou k chybám a pomalou. Raný síťový management byl silně závislý na lidských operátorech reagujících na alarmy nebo periodické reporty. Tento reaktivní přístup často vedl k prodloužené degradaci služeb, protože problémy byly řešeny až poté, co byli ovlivněni uživatelé. Mezi omezení patřily zpožděné časy odezvy, nekonzistentní řešení problémů a neschopnost spravovat obrovské množství konfigurovatelných parametrů v moderních sítích jako 4G a 5G.

Primární motivací pro standardizaci Technických spouští bylo umožnit proaktivní a automatizovaný síťový management. Řeší problém, jak převést provozní politiky ('chceme udržovat latenci pod 20 ms') na automatizované síťové akce bez neustálého lidského dohledu. Definováním spouští na základě technických podmínek mohou sítě samy monitorovat a iniciovat nápravné nebo optimalizační akce téměř v reálném čase. To je zásadní pro splnění přísných Service Level Agreements (SLA) služeb 5G, jako je ultra-reliable low-latency communications (URLLC), kde milisekundy hrají roli a lidská reakční doba je nedostatečná.

Historicky potřeba TT rostla se zavedením SON v 3GPP Release 8 pro LTE. Funkce SON jako Mobility Robustness Optimization (MRO) a Mobility Load Balancing (MLB) vyžadovaly automatizované mechanismy pro detekci suboptimálních podmínek (např. vysoká míra selhání handoveru) a spouštění úprav parametrů. TT poskytla standardizovaný stavební blok pro tyto funkce. Její rozsah se v následujících release rozšířil na pokrytí širších oblastí managementu, včetně výkonnostního managementu, managementu poruch a managementu virtualizovaných a řezaných sítí. V kontextu 5G a síťového řezání jsou TT klíčové pro zajištění specifické pro řez, což umožňuje management systému automaticky detekovat porušení SLA v rámci řezu a spouštět škálovací nebo nápravné akce. Technická spoušť se tak vyvinula z podpůrného konceptu pro SON v základní prvek autonomních sítí, který zvyšuje efektivitu, spolehlivost a snižuje provozní náklady.

## Klíčové vlastnosti

- Standardizovaný mechanismus pro podmíněné automatizované akce v OAM
- Podporuje proaktivní a reaktivní operace síťového managementu
- Nedílná součást Self-Organizing Network (SON) a uzavřené smyčky automatizace
- Konfigurovatelná pro různé monitorované parametry (KPI, poruchy, stavy)
- Umožňuje interoperabilitu v více-dodavatelských prostředích managementu
- Umožňuje rychlou reakci na síťové události a zajištění SLA

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.535** (Rel-19) — TS 24535: (g)PTP Message Delivery Protocol
- **TS 31.117** (Rel-19) — USIM Application Toolkit Test for Non-Removable UICC
- **TS 31.127** (Rel-18) — UICC-terminal interaction testing specification
- **TS 32.862** (Rel-14) — Service KQI Standardization Study
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [TT na 3GPP Explorer](https://3gpp-explorer.com/glossary/tt/)
