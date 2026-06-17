---
slug: "hma"
url: "/mobilnisite/slovnik/hma/"
type: "slovnik"
title: "HMA – Highly Managed Alarms"
date: 2025-01-01
abbr: "HMA"
fullName: "Highly Managed Alarms"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/hma/"
summary: "Highly Managed Alarms (HMA, vysoce řízené alarmy) je rámec správy podle 3GPP pro standardizaci životního cyklu kritických alarmů poruch v síti. Definuje strukturované informační modely alarmů, správu"
---

HMA je rámec správy podle 3GPP, který standardizuje životní cyklus kritických alarmů poruch v síti pomocí strukturovaných informačních modelů a správy stavů za účelem zvýšení spolehlivosti a snížení pracovní zátěže operátorů.

## Popis

Highly Managed Alarms (HMA, vysoce řízené alarmy) je standardizovaný rámec v rámci specifikací správy poruch (Fault Management) 3GPP, podrobně popsaný v několika technických specifikacích (TS) včetně 32.111, 32.859 a 26.999. Definuje komplexní model pro generování, hlášení, správu stavů, korelaci a odstraňování alarmů v prvcích telekomunikačních sítí. Alarm je indikace poruchy nebo abnormálního stavu, který vyžaduje pozornost operátora. Rámec HMA jde nad rámec pouhého oznamování událostí a zachází s alarmy jako s řízenými objekty s plným životním cyklem.

Z architektonického hlediska je HMA implementováno v rámci síťových prvků ([NE](/mobilnisite/slovnik/ne/)) a systémů pro správu prvků ([EMS](/mobilnisite/slovnik/ems/)). Definuje klíčové komponenty, jako je informační model alarmu (Alarm Information Model), který standardizuje atributy alarmu, jako je ID alarmu, vnímaná závažnost (kritický, závažný, méně závažný, varování), pravděpodobná příčina a konkrétní problém. Ústředním konceptem je model stavu alarmu, který zahrnuje stavy jako 'vyvolán', 'odstraněn' a 'potvrzen'. Rámec vyžaduje podporu korelace alarmů, kdy lze více souvisejících alarmů z různých NE spojit s jedinou hlavní příčinou, a podporu odložení alarmů (alarm shelving), což umožňuje operátorům dočasně potlačit alarmy pro plánované činnosti údržby.

Jak to funguje, zahrnuje strukturovaný tok. Když síťový prvek (NE) detekuje poruchový stav, vytvoří instanci objektu alarmu podle modelu HMA a odešle oznámení do řídicího systému (EMS nebo Network Management System - [NMS](/mobilnisite/slovnik/nms/)). Řídicí systém tento alarm prezentuje a operátoři mohou provádět akce životního cyklu, jako je potvrzení nebo odstranění. Rámec zajišťuje konzistentnost v tom, jak jsou tyto akce komunikovány zpět k NE. Jeho úlohou je poskytovat jednotné, interoperabilní rozhraní pro správu poruch, což je kritická podmnožina OAM. To umožňuje operátorům efektivně sledovat stav sítě, diagnostikovat problémy a udržovat dostupnost služeb napříč heterogenním síťovým vybavením od různých dodavatelů.

## K čemu slouží

Rámec Highly Managed Alarms (HMA, vysoce řízené alarmy) byl vytvořen, aby řešil provozní neefektivnost a složitost plynoucí z proprietárních, na dodavatele specifických implementací alarmů v prostředích sítí s více dodavateli. Před standardizací každý dodavatel zařízení implementoval jedinečné formáty alarmů, úrovně závažnosti, pravidla životního cyklu a metody korelace. To nutilo síťové operátory učit se a spravovat více odlišných systémů, což zvyšovalo střední dobu do opravy (MTTR) poruch a riziko lidské chyby, což nakonec ovlivňovalo spolehlivost sítě a kvalitu služeb.

Historický kontext spočívá v úsilí 3GPP o standardizaci rozhraní pro správu, zejména pro sítě nové generace ([NGN](/mobilnisite/slovnik/ngn/)) a později pro LTE/5G. HMA, zavedené ve verzi 12 (Release 12), bylo součástí širšího úsilí o definici společného informačního modelu pro všechny oblasti správy (Fault, Configuration, Accounting, Performance, Security - FCAPS). Řeší problém únavy z alarmů a informačního přetížení tím, že poskytuje strukturovaná, korelovaná a spravovatelná data alarmů. Umožňuje automatizaci procesů správy poruch a vývoj pokročilých, na dodavateli nezávislých aplikací [NMS](/mobilnisite/slovnik/nms/).

Jeho vytvoření bylo motivováno potřebou snížit provozní výdaje ([OPEX](/mobilnisite/slovnik/opex/)) a zlepšit zajištění služeb (service assurance). Tím, že poskytuje standardizovaný 'jazyk' pro alarmy, umožňuje HMA integraci dat správy ze všech síťových vrstev (RAN, Core, Transport) do jednotného přehledového rozhraní. To je zásadní pro dosažení provozní agility vyžadované moderními, softwarově řízenými a řezanými (sliced) sítěmi.

## Klíčové vlastnosti

- Standardizovaný informační model alarmu (Alarm Information Model, AIM) s definovanými atributy a sémantikou
- Formální správa životního cyklu stavu alarmu (vyvolán, odstraněn, potvrzen)
- Podpora korelace alarmů pro identifikaci hlavních příčin
- Schopnost odložení alarmů (alarm shelving) pro plánovaná okna údržby
- Standardizovaná rozhraní pro oznamování a hlášení změn stavu
- Integrace s širším rámcem správy poruch (Fault Management) a OAM podle 3GPP

## Definující specifikace

- **TR 26.999** (Rel-19) — VR Streaming Interoperability Test Material
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 32.859** (Rel-12) — Alarm Management Quality Improvement Study

---

📖 **Anglický originál a plná specifikace:** [HMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/hma/)
