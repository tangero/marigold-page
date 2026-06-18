---
slug: "nsm"
url: "/mobilnisite/slovnik/nsm/"
type: "slovnik"
title: "NSM – Network Slice Management"
date: 2025-01-01
abbr: "NSM"
fullName: "Network Slice Management"
category: "Network Slicing"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nsm/"
summary: "Network Slice Management (NSM) je rámec pro správu životního cyklu síťových řezů (network slices), zahrnující vytváření, modifikaci, monitorování a ukončování. Poskytuje nezbytné schopnosti správy k p"
---

NSM je rámec pro správu životního cyklu síťových řezů (network slices), zahrnující jejich vytváření, modifikaci, monitorování a ukončování, aby mohly být provozovány jako nezávislé logické sítě splňující specifické SLA.

## Popis

Network Slice Management (NSM) je komplexní rámec definovaný v rámci architektury 3GPP Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)), konkrétně podrobně popsaný v TS 28.202 a TS 28.843. Zahrnuje soubor funkcí a rozhraní správy potřebných pro správu životního cyklu síťového řezu. Síťový řez je koncový logický síťový segment poskytující specifické síťové schopnosti a charakteristiky a NSM je zodpovědný za jeho instanciaci, konfiguraci, aktivaci, dohled a vyřazení.

Rámec NSM funguje prostřednictvím souboru služeb správy, které interagují s dalšími funkcemi správy, jako je Communication Service Management Function (CSMF) a Network Slice Management Function ([NSMF](/mobilnisite/slovnik/nsmf/)). NSM přijímá požadavky na řez od CSMF, která překládá obchodní potřeby do technických specifikací. Poté tyto požadavky rozkládá na požadavky pro instance podsíťových řezů a koordinuje s Domain Management Functions (jako je Network Slice Subnet Management Function - NSSMF) pro správu prostředků napříč různými síťovými doménami (např. RAN, Core, Transport).

Klíčové architektonické komponenty v rámci NSM zahrnují rozhraní správy (např. rozhraní Nsmf) a definované postupy správy pro správu šablon řezů, správu instancí řezů a zajištění výkonu řezů. Zajišťuje provizionování potřebných virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) a fyzických síťových funkcí ([PNF](/mobilnisite/slovnik/pnf/)), jejich konektivitu a související politiky. NSM je klíčové pro zajištění, aby každý řez fungoval izolovaně podle své definované [SLA](/mobilnisite/slovnik/sla/), pokrývaje aspekty jako monitorování výkonu, správu poruch a vynucování bezpečnostních politik. Působí jako centrální orchestrační vrstva pro řezy, umožňující automatizované a efektivní operace.

## K čemu slouží

NSM bylo zavedeno, aby řešilo provozní složitost nasazování a správy více izolovaných logických sítí (řezů) nad sdílenou fyzickou infrastrukturou. Před zavedením síťových řezů operátoři spravovali jedinou monolitickou síť nabízející univerzální službu. Nástup 5G a různorodých případů užití (eMBB, [URLLC](/mobilnisite/slovnik/urllc/), mMTC) si vyžádal schopnost vytvářet přizpůsobené sítě se specifickými zárukami výkonu, což nebylo s dědictvím systémů správy možné.

Vytvoření NSM bylo motivováno potřebou standardizovaného, automatizovaného rámce správy. Bez něj by byly operace životního cyklu řezů manuální, pomalé a náchylné k chybám, což by popřelo výhody agility síťových řezů. NSM řeší problém koordinace prostředků napříč více technologickými doménami (RAN, Core, Transport), které jsou často spravovány samostatnými systémy. Poskytuje nezbytnou abstrakci a automatizaci pro překlad požadavků služeb na vysoké úrovni do detailních konfigurací prostředků napříč doménami, což umožňuje efektivní využití infrastruktury a rychlé poskytování služeb.

## Klíčové vlastnosti

- Správa životního cyklu koncového síťového řezu (příprava, instance, aktivace, dohled, deaktivace, vyřazení)
- Správa šablon síťových řezů (NEST) definujících charakteristiky a požadavky řezu
- Koordinace s Domain Management Functions (např. NSSMF) pro provizionování prostředků napříč doménami RAN, Core a Transport
- Správa výkonu a jeho zajištění pro monitorování klíčových ukazatelů výkonu (KPI) řezu vůči SLA
- Správa poruch pro detekci, izolaci a obnovu po selháních v rámci instance řezu
- Správa politik pro vynucování řezu-specifických bezpečnostních, účtovacích a QoS politik

## Související pojmy

- [NSMF – Network Slice Management Function](/mobilnisite/slovnik/nsmf/)

## Definující specifikace

- **TS 28.202** (Rel-19) — 5G Network Slice Management Charging
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios

---

📖 **Anglický originál a plná specifikace:** [NSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsm/)
