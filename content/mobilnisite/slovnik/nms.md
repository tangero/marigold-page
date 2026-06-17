---
slug: "nms"
url: "/mobilnisite/slovnik/nms/"
type: "slovnik"
title: "NMS – Network Management Subsystem"
date: 2025-01-01
abbr: "NMS"
fullName: "Network Management Subsystem"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nms/"
summary: "Zastřešující rámec a soubor funkcí zodpovědný za správu, monitorování a řízení telekomunikační sítě. Zahrnuje správu poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS). NMS je klíčový pro zaj"
---

NMS je zastřešující rámec zodpovědný za správu, monitorování a řízení telekomunikační sítě, zahrnující správu poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS).

## Popis

Network Management Subsystem (NMS) je komplexní architektonická a funkční entita definovaná 3GPP pro provoz, správu, údržbu a poskytování služeb (OAM&P) veřejné pozemní mobilní sítě (PLMN). Není to jediný fyzický uzel, ale distribuovaný systém skládající se z více logických funkcí a rozhraní. Architektura NMS je typicky strukturována hierarchicky, zahrnuje systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)), které spravují konkrétní síťové prvky ([NE](/mobilnisite/slovnik/ne/)), jako jsou základnové stanice, a vyšší úrovně systémů pro správu sítě, které poskytují konsolidovaný pohled na celou síť. Rozhraní NMS komunikuje s telekomunikační sítí prostřednictvím standardizovaných rozhraní (např. Itf-N) za účelem sběru dat a vydávání příkazů.

V jádru NMS implementuje model FCAPS: Správa poruch pro detekci, izolaci a nápravu anomálií v síti; Správa konfigurace pro instalaci, sledování a aktualizaci softwarových a hardwarových nastavení síťových prvků; Správa účtování pro sledování využití síťových zdrojů pro fakturaci nebo přirážky; Správa výkonu pro shromažďování a analýzu statistických dat za účelem zajištění optimálního provozu sítě; a Správa zabezpečení pro řízení přístupu k síťovým zdrojům a datům. Tyto funkce jsou realizovány kombinací protokolů typu manažer-agent, databází a uživatelských aplikací, které operátorům poskytují grafické mapy sítě, řídicí panely a konzoly pro alarmy.

Jeho role je nedílnou součástí celého životního cyklu síťových služeb. NMS umožňuje centralizované monitorování a řízení, což je nezbytné pro rozsáhlá nasazení sítí s více dodavateli. Automatizuje rutinní úlohy, usnadňuje rychlé poskytování služeb a poskytuje nástroje pro analýzu hlavní příčiny při výpadcích. Zpracováním dat o výkonu z celé sítě podporuje NMS plánování kapacity a zajišťování kvality. V moderních sítích tvoří základ pokročilých operačních konceptů, jako je Zero-Touch Network and Service Management (ZSM), a poskytuje nezbytná rozhraní pro integraci s širšími systémy podpory podnikání ([BSS](/mobilnisite/slovnik/bss/)).

## K čemu slouží

NMS existuje proto, aby vnesl řád, automatizaci a škálovatelnost do komplexního úkolu správy telekomunikačních sítí. Rané sítě byly spravovány pomocí proprietárních nástrojů pro jednotlivé prvky, což činilo integrovanou správu v prostředích s více dodavateli obtížnou a pracnou. Rámec NMS, standardizovaný 3GPP, byl vytvořen k řešení tohoto problému interoperability a poskytuje společnou sadu principů správy, informačních modelů a rozhraní, které umožňují operátorům spravovat heterogenní síťové zařízení z jedné nebo federované správní platformy.

Řeší základní provozní výzvy spojené s udržováním dostupnosti, kvality a zabezpečení služeb, jak sítě rostou ve velikosti a složitosti. Bez sofistikovaného NMS by byly úlohy, jako jsou softwarové aktualizace, korelace poruch a analýza trendů výkonu, manuální, náchylné k chybám a pomalé, což by přímo ovlivňovalo spolehlivost služeb a dobu uvedení nových funkcí na trh. NMS je motor, který umožňuje efektivní síťové operace, snižuje provozní výdaje ([OPEX](/mobilnisite/slovnik/opex/)) a minimalizuje prostoje služeb.

Historicky bylo jeho formalizování v 3GPP Release 4 součástí širšího přechodu od monolitických síťových architektur k modulárnějším systémům založeným na standardech. Poskytlo nezbytný protějšek správy pro vyvíjející se síťovou architekturu a zajistilo, že jak se síť sama stávala schopnější (se zavedením paketově orientovaných jader v [GPRS](/mobilnisite/slovnik/gprs/) a UMTS), nástroje pro její správu držely krok, podporujíce přechod od hlasově orientovaného k datově orientovanému poskytování služeb.

## Klíčové vlastnosti

- Implementuje model správy FCAPS (Fault, Configuration, Accounting, Performance, Security)
- Standardizovaná rozhraní (např. Itf-N) pro interoperabilitu mezi různými dodavateli
- Hierarchická struktura správy (vrstva správy sítě, vrstva správy prvků)
- Podpora automatizovaného poskytování služeb a správy konfigurace
- Centralizované možnosti sledování alarmů a správy poruch
- Sběr, ukládání a analýza dat o výkonu pro reportování a plánování

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.878** (Rel-18) — Technical Report on 5G Timing Resiliency
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.819** (Rel-8) — Element Management Layer OS Functions
- **TS 32.826** (Rel-10) — Study on Energy Savings Management in LTE/SAE Networks
- **TS 32.851** (Rel-12) — Network Sharing OAM Requirements
- **TS 32.854** (Rel-11) — FMC Federated Network Information Model
- **TS 32.861** (Rel-13) — IRP Subset Selection for Network Management
- **TS 32.880** (Rel-15) — Simplified Itf-N IRP Solution Sets Study

---

📖 **Anglický originál a plná specifikace:** [NMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nms/)
