---
slug: "spdf"
url: "/mobilnisite/slovnik/spdf/"
type: "slovnik"
title: "SPDF – Service-based Policy Decision Function"
date: 2025-01-01
abbr: "SPDF"
fullName: "Service-based Policy Decision Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/spdf/"
summary: "Funkce jádra sítě 5G, která poskytuje rozhraní založené na službách pro přijímání rozhodnutí o politikách souvisejících se síťovým řezáním. Působí jako centrální autorita pro politiky v rámci instance"
---

SPDF je funkce jádra sítě 5G, která poskytuje rozhraní založené na službách (service-based interface) pro přijímání centrálních rozhodnutí o politikách a pro překlad požadavků služeb na síťové politiky v rámci instance síťového řezu.

## Popis

Service-based Policy Decision Function (SPDF) je specializovaná síťová funkce definovaná v architektuře jádra sítě 5G, konkrétně v kontextu správy síťového řezání. Je součástí frameworku Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)) a správy síťových řezů. SPDF vystavuje rozhraní založené na službách (jak je specifikováno v 3GPP TS 24.524) a funguje jako centrální bod pro rozhodování o politikách pro konkrétní instanci síťového řezu ([NSI](/mobilnisite/slovnik/nsi/)). Jejím hlavním úkolem je interpretovat vysokourovňové požadavky služeb a smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) pro řez a převádět je na konkrétní, vynutitelné síťové politiky, které řídí chování a zdroje řezu.

Z architektonického hlediska SPDF interaguje s dalšími funkcemi správy, jako je Communication Service Management Function (CSMF), Network Slice Management Function ([NSMF](/mobilnisite/slovnik/nsmf/)) a Network Slice Subnet Management Function (NSSMF). Pracovní postup typicky začíná, když spotřebitel řezu (např. podnik) požaduje přes CSMF řez s určitými charakteristikami. NSMF, odpovědná za správu životního cyklu celého řezu, konzultuje SPDF. SPDF přebírá požadavky služeb (např. garantovaná šířka pásma, latence, geografická oblast) a činí rozhodnutí o politikách, jak je realizovat. To zahrnuje určení politik pro přidělování zdrojů, QoS politiky, bezpečnostní politiky a směrovací politiky specifické pro daný řez.

SPDF politiky přímo nevynucuje, ale poskytuje rozhodnutí o politikách funkcím pro vynucování politik v datové rovině, jako je [PCF](/mobilnisite/slovnik/pcf/) (Policy Control Function) pro politiky na úrovni relací nebo NSSMF pro politiky na úrovni zdrojů v RAN a přenosové síti. Funguje na základě předem nakonfigurované sady pravidel politik a potenciálně v reálném čase na základě vstupů ze síťové analytiky. Díky centralizaci rozhodnutí o politikách na úrovni řezu SPDF zajišťuje konzistentní aplikaci politik napříč všemi podsítěmi (RAN, Transport, Jádro), které řez tvoří. Je klíčovým prvkem pro automatizovanou, záměrem řízenou správu síťových řezů, která umožňuje dynamické přizpůsobení chování řezu v reakci na měnící se požadavky služeb nebo stav sítě.

## K čemu slouží

SPDF byla zavedena, aby vyřešila kritický problém koordinace a překladu politik, který je vlastní síťovému řezání v 5G. Před její definicí se správa politik v mobilních sítích zaměřovala primárně na relace účastníků (přes [PCRF](/mobilnisite/slovnik/pcrf/)/[PCF](/mobilnisite/slovnik/pcf/)) nebo na jednotlivé síťové domény. Síťové řezání však zavádí novou abstrakci: logicky izolovanou end-to-end síť šitou na míru konkrétní službě. Problém spočíval v tom, že neexistovala standardizovaná funkce, která by komplexně řídila politiky pro celou instanci řezu a překlenula propast mezi obchodními záměry služeb a technickými konfiguracemi sítě.

Její vytvoření bylo motivováno potřebou automatizované správy řezů v uzavřené smyčce. Ruční konfigurace konzistentních politik napříč RAN, transportem a jádrem pro každý řez by byla náchylná k chybám a nebyla by škálovatelná pro předpokládané tisíce současných řezů. SPDF poskytuje vyhrazenou funkci založenou na službách, kterou mohou systémy správy dotazovat, aby získaly autoritativní rozhodnutí o politikách pro daný řez. Tím se řeší omezení spočívající v rozptýlení rozhodnutí o politikách mezi doménově specifické manažery, což by mohlo vést ke konfliktům nebo nesouladu s celkovou [SLA](/mobilnisite/slovnik/sla/) řezu. Tvoří základní kámen přístupu 3GPP k řízení řezů na základě záměru (intent-based management), což operátorům umožňuje nabízet Slice-as-a-Service se zaručenými výkonnostními charakteristikami.

## Klíčové vlastnosti

- Poskytuje rozhraní založené na službách (SBI) pro žádosti o rozhodnutí politik řezu.
- Překládá vysokourovňové požadavky služeb a SLA na technické síťové politiky.
- Působí jako centrální autorita pro politiky pro instanci síťového řezu (NSI).
- Generuje politiky pro přidělování zdrojů, QoS, zabezpečení a směrování na řez.
- Interaguje s NSMF, NSSMF a PCF pro šíření a vynucování politik.
- Umožňuje automatizovanou, záměrem řízenou správu životního cyklu síťového řezu.

## Související pojmy

- [NSMF – Network Slice Management Function](/mobilnisite/slovnik/nsmf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [NSI – Network Slice Instance Identifier](/mobilnisite/slovnik/nsi/)

## Definující specifikace

- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture

---

📖 **Anglický originál a plná specifikace:** [SPDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/spdf/)
