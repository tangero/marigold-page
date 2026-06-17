---
slug: "cef"
url: "/mobilnisite/slovnik/cef/"
type: "slovnik"
title: "CEF – Charging Enablement Function"
date: 2025-01-01
abbr: "CEF"
fullName: "Charging Enablement Function"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/cef/"
summary: "Charging Enablement Function (CEF) je funkce 5G sítě, která standardizuje a centralizuje vystavování účtovacích dat a událostí externím aplikacím. Poskytuje jednotné rozhraní pro účtovací interakce, u"
---

CEF je funkce 5G sítě, která standardizuje a centralizuje vystavování účtovacích dat a událostí externím aplikacím prostřednictvím jednotného rozhraní.

## Popis

Charging Enablement Function (CEF) je síťová funkce založená na službách zavedená v architektuře 5G System (5GS) za účelem poskytnutí standardizovaného, centralizovaného mechanismu pro účtování. Funguje v rámci domény řízení a orchestrace sítě 5G Core (5GC), konkrétně jako součást architektury Charging Function ([CHF](/mobilnisite/slovnik/chf/)). CEF působí jako prostředník, který vystavuje účtovací schopnosti a události externím Application Functions ([AF](/mobilnisite/slovnik/af/)) a dalším síťovým funkcím prostřednictvím dobře definovaných rozhraní založených na službách (SBI), primárně založených na [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/). Jejím hlavním úkolem je oddělit účtovací logiku od logiky služby, což umožňuje flexibilnější a dynamičtější účtovací scénáře.

Architektonicky CEF komunikuje s Charging Function (CHF) za účelem získání účtovacích dat a politik. Poskytuje severní rozhraní (Nchf) externím entitám, jako jsou Application Functions (AF) nebo poskytovatelé služeb třetích stran, umožňuje jim vyžádat si účtovací relace, přijímat oznámení o účtovacích událostech a ovlivňovat účtovací rozhodnutí. CEF podporuje jak online, tak offline modely účtování. Pro online účtování může komunikovat s Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) prostřednictvím CHF za účelem provádění kontroly kreditu v reálném čase. Pro offline účtování může shromažďovat a předávat záznamy o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) do Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)).

Klíčové komponenty CEF zahrnují Charging Enablement Service, který zpracovává vystavování účtovacích schopností, a Event Exposure Service, který spravuje odběry a oznámení pro účtovací události. CEF implementuje službu Nchf_SpendingLimitControl, která umožňuje AF nastavovat výdajové limity pro uživatele nebo služby, a službu Nchf_ConvergedCharging, která poskytuje jednotné rozhraní pro konvergované účtovací scénáře. Podporuje také integraci politik, spolupracuje s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) na vynucování účtovacích politik na základě síťových podmínek, uživatelských předplatných a požadavků služeb.

Provoz CEF zahrnuje několik kroků: zaprvé, externí AF se přihlásí k odběru účtovacích událostí prostřednictvím CEF; zadruhé, CEF přepošle tyto odběry do CHF; zatřetí, když dojde k účtovací události (např. dosažení prahové hodnoty datového využití), CHF o tom CEF informuje; a nakonec CEF přepošle oznámení do AF. To umožňuje interakce s účtováním v reálném čase, jako je spouštění upgradů služeb nebo upozorňování uživatelů na limity využití. CEF také podporuje dávkové zpracování pro offline účtování, kdy agreguje CDR před jejich předáním do OFCS. Její role je klíčová pro umožnění účtování založeného na službách, kde je účtování přizpůsobeno konkrétním službám, síťovým řezům nebo úrovním kvality služby (QoS), což usnadňuje nové strategie zpoplatnění v 5G sítích.

## K čemu slouží

Charging Enablement Function (CEF) byla zavedena ve 3GPP Release 16, aby řešila omezení předchozích účtovacích architektur, které byly často rigidní, specifické pro dodavatele a postrádaly standardizovaná rozhraní pro externí integraci. V dřívějších generacích (např. 4G) byly účtovací systémy primárně navrženy pro hlasové a datové služby s omezenou podporou dynamického, na službách založeného účtování vyžadovaného 5G případy použití, jako jsou síťové řezy, IoT a edge computing. Tradiční účtovací rozhraní nebyla vhodná pro interakce v reálném čase s externími aplikacemi, což brzdilo inovace a přijímání nových obchodních modelů.

CEF tyto problémy řeší tím, že poskytuje standardizované, na službách založené rozhraní, které odděluje účtovací logiku od logiky služby a umožňuje flexibilnější a dynamičtější účtovací scénáře. Umožňuje externím Application Functions (AF) a poskytovatelům služeb třetích stran přímo komunikovat s účtovacím systémem, což usnadňuje účtování v reálném čase, kontrolu výdajových limitů a oznamování událostí. To je obzvláště důležité pro 5G sítě, které podporují rozmanité služby s různými požadavky na QoS, jako je enhanced mobile broadband (eMBB), ultra-reliable low-latency communications (URLLC) a massive machine-type communications (mMTC). CEF umožňuje operátorům efektivněji zpoplatňovat tyto služby nabídkou přizpůsobených účtovacích plánů a schopností účtování v reálném čase.

Historicky se účtovací systémy vyvinuly z přepojovaných okruhových sítí na paketové sítě, ale zůstaly do značné míry izolované od externích aplikací. CEF představuje posun k otevřeným, programovatelným účtovacím architekturám, což je v souladu se širší vizí 5G pro softwarizaci sítě a architekturu založenou na službách (SBA). Standardizací vystavování účtovacích schopností CEF snižuje složitost integrace, podporuje interoperabilitu mezi zařízeními různých dodavatelů a urychluje nasazování nových služeb. Řeší také potřebu konvergovaného účtování, kde jsou online a offline účtování sjednoceny, a bezproblémově podporují jak předplacené, tak postpaid modely. Tento vývoj je poháněn poptávkou po agilnějších, zákaznicky orientovaných účtovacích řešeních v éře digitální transformace a 5G.

## Klíčové vlastnosti

- Standardizované rozhraní založené na službách (Nchf) pro externí účtovací interakce
- Podpora online a offline modelů účtování prostřednictvím integrace s CHF
- Služba vystavování událostí pro oznámení o účtování v reálném čase pro AF
- Schopnost kontroly výdajových limitů pro správu kvót uživatelů nebo služeb
- Integrace politik s PCF pro dynamická účtovací rozhodnutí
- Podpora konvergovaného účtování napříč více službami a síťovými řezy

## Související pojmy

- [CHF – Charging Function](/mobilnisite/slovnik/chf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [AF – Authentication Framework](/mobilnisite/slovnik/af/)

## Definující specifikace

- **TS 28.201** (Rel-19) — 5G Network Slice Performance Analytics Charging
- **TS 28.202** (Rel-19) — 5G Network Slice Management Charging
- **TS 28.310** (Rel-19) — Energy Efficiency Management for 5G Networks
- **TR 28.815** (Rel-17) — Charging Study for Edge Computing
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TS 28.880** (Rel-19) — Study on 5G Energy Efficiency & Saving
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.257** (Rel-19) — Edge Computing Charging Management
- **TS 32.290** (Rel-19) — 5G Charging for Service Based Interface
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TR 32.847** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [CEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cef/)
