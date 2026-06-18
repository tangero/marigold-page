---
slug: "tom"
url: "/mobilnisite/slovnik/tom/"
type: "slovnik"
title: "TOM – Telecom Operations Map"
date: 2025-01-01
abbr: "TOM"
fullName: "Telecom Operations Map"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tom/"
summary: "Telecom Operations Map (TOM) je rámec od TM Forum, přijatý 3GPP, který modeluje obchodní procesy pro poskytovatele telekomunikačních služeb. Definuje procesní toky pro plnění objednávek (Fulfillment),"
---

TOM (Telecom Operations Map) je mapování telekomunikačních operací, což je rámec TM Forum přijatý 3GPP, který modeluje obchodní procesy telekomunikačního sektoru pro plnění objednávek (Fulfillment), zajištění služeb (Assurance) a účtování (Billing), a poskytuje návrh pro OSS a BSS.

## Popis

Telecom Operations Map (TOM), vyvinutý TeleManagement Forum ([TM](/mobilnisite/slovnik/tm/) Forum) a referencovaný ve specifikacích 3GPP, je komplexní, vysokourovňový rámec popisující klíčové obchodní procesy vyžadované pro poskytovatele telekomunikačních služeb. Není to protokol vynalezený 3GPP, ale průmyslový model, s nímž se 3GPP sladuje pro definici aspektů řízení a operací. TOM hierarchicky organizuje procesy se zaměřením na klíčové vertikální hodnotové řetězce poskytovatele služeb: procesy péče o zákazníka (Customer Care Processes) a procesy vývoje a provozu služeb (Service Development & Operations Processes). Jeho hlavním cílem je poskytnout standardní referenční model pro vedení vývoje operačních podpůrných systémů ([OSS](/mobilnisite/slovnik/oss/)) a obchodních podpůrných systémů ([BSS](/mobilnisite/slovnik/bss/)), což umožňuje automatizaci, interoperabilitu a efektivitu.

V jádru je TOM postaven na modelu FAB: plnění objednávek (Fulfillment), zajištění služeb (Assurance) a účtování (Billing). Procesy plnění objednávek zahrnují vše od přijetí objednávky po aktivaci a konfiguraci služby. Procesy zajištění služeb jsou zodpovědné za udržení kvality služeb, včetně monitorování výkonu, řešení problémů a obnovy po poruše. Procesy účtování spravují stanovení cen, fakturaci a inkaso příjmů. Tyto tři jsou považovány za základní provozní procesy orientované na zákazníka. Pod nimi TOM definuje podpůrné a přípravné procesy (Support & Readiness processes), které zahrnují funkce jako správa inventáře sítě, poskytování síťových prostředků a řízení pracovní síly. Tyto podpůrné procesy zajišťují, že infrastruktura je připravena k provedení procesů FAB. Model také definuje procesy řízení vztahů s dodavateli/partnery (Supplier/Partner Relationship Management processes).

V kontextu 3GPP specifikace, které odkazují na TOM (jako např. ty ze série 32 o telekomunikačním řízení), jej používají jako základ pro definování podrobnějších, technologicky specifických požadavků na řízení. Například 3GPP TS 32.101 nastiňuje principy telekomunikačního řízení a sladuje je s rámcem TOM. Zajišťuje, že systémy řízení pro sítě 3GPP (např. pro správu síťových řezů 5G) jsou navrženy s procesně orientovaným pohledem, který se integruje s celkovou architekturou OSS/BSS poskytovatele služeb. TOM poskytuje kontext obchodních procesů, do kterého se musí vejít podrobná rozhraní pro správu sítě 3GPP (jako referenční bod Itf-N) a informační modely. Pomáhá zajistit, že automatizované procesy pro zřizování toku QoS 5G nebo zajištění životního cyklu síťového řezu lze namapovat na širší podnikové pracovní postupy od objednávky k platbě a od závady k vyřešení.

## K čemu slouží

Telecom Operations Map byl vytvořen [TM](/mobilnisite/slovnik/tm/) Forum, aby řešil historický chaos a vysoké náklady spojené s operacemi poskytovatelů telekomunikačních služeb. Před takovými rámci si každý poskytovatel vyvíjel proprietární, izolované systémy [OSS](/mobilnisite/slovnik/oss/)/[BSS](/mobilnisite/slovnik/bss/), které bylo obtížné integrovat, automatizovat a přizpůsobovat novým službám. To vedlo k dlouhé době uvedení nových služeb na trh, vysokým provozním nákladům ([OPEX](/mobilnisite/slovnik/opex/)) a špatné zákaznické zkušenosti. TOM poskytl neutrální, průmyslem dohodnutý návrh, který umožnil dodavatelům a poskytovatelům diskutovat o požadavcích a vyvíjet systémy pomocí společného jazyka a procesního modelu.

Přijetí a odkazování na TOM ze strany 3GPP v jeho specifikacích pro řízení slouží kritickému účelu: překlenutí mezery mezi podrobnými, síťově-technologicky specifickými řídicími protokoly definovanými 3GPP a širším obchodním a provozním kontextem poskytovatele služeb. Sladěním s TOM 3GPP zajišťuje, že řídicí schopnosti, které standardizuje pro sítě 4G/5G, mohou být bezproblémově integrovány do většího provozního prostředí poskytovatele služeb. Řeší problém, že řízení technologie je izolovaný ostrov. Například TOM motivuje definici standardizovaných řídicích služeb pro síťové řezy (např. zřizování řezů, zajištění výkonu), které přímo mapují na procesy plnění objednávek (Fulfillment) a zajištění služeb (Assurance) v TOM, což umožňuje komplexní automatizaci nabídek řezu jako služby.

## Klíčové vlastnosti

- Definuje základní rámec provozních procesů FAB (plnění objednávek, zajištění služeb, účtování)
- Poskytuje hierarchický model oddělující vrstvy řízení zákazníka, služeb a sítě/prostředků
- Slouží jako referenční model pro integraci systémů OSS/BSS a dosažení provozní automatizace
- Přijat 3GPP, aby poskytl obchodní kontext pro technologicky specifické standardy řízení
- Podporuje interoperabilitu mezi řídicími systémy různých dodavatelů a procesy poskytovatelů služeb
- Tvoří konceptuální základ pro podrobnější rámce, jako je Business Process Framework (eTOM) od TM Forum

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.140** (Rel-19) — Subscription Management (SuM) requirements
- **TS 32.150** (Rel-19) — IRP Concept and Definitions
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol
- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [TOM na 3GPP Explorer](https://3gpp-explorer.com/glossary/tom/)
