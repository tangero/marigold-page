---
slug: "ofm"
url: "/mobilnisite/slovnik/ofm/"
type: "slovnik"
title: "OFM – Operational Feature Monitor"
date: 2025-01-01
abbr: "OFM"
fullName: "Operational Feature Monitor"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ofm/"
summary: "Funkce systému správy, která monitoruje provozní stav a výkon síťových funkcí. Shromažďuje data, aby zajistila správnou funkci funkcí a plnění smluv o úrovni služeb, což umožňuje proaktivní údržbu a ř"
---

OFM (Operational Feature Monitor) je funkce systému správy, která monitoruje provozní stav a výkon síťových funkcí, aby zajistila jejich správnou funkci a plnění smluv o úrovni služeb (SLA).

## Popis

Operational Feature Monitor (OFM) je klíčová komponenta v rámci frameworku Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)) sítě 3GPP. Funguje jako specializovaný monitorovací agent nebo systém, který průběžně sleduje stav, výkon a dostupnost konkrétních síťových funkcí nebo služeb nasazených v síťové infrastruktuře. Jeho primární rolí je shromažďovat telemetrická data, generovat metriky výkonu a detekovat anomálie nebo poruchy spojené s těmito funkcemi. Toto shromažďování dat je zásadní pro udržení kvality služeb a zajištění, že síťové schopnosti fungují v rámci svých navržených parametrů.

Z architektonického hlediska OFM typicky komunikuje se síťovými elementy ([NE](/mobilnisite/slovnik/ne/)) a systémy správy elementů ([EMS](/mobilnisite/slovnik/ems/)) prostřednictvím standardizovaných rozhraní pro správu, jako jsou ta definovaná ve specifikacích 3GPP řady 32. Používá kombinaci pasivního monitorování (např. analýza čítačů měření výkonu) a aktivního testování (např. generování testovacích transakcí) k posouzení chování funkce. Monitor je konfigurován specifickými prahovými hodnotami a pravidly, které definují normální provozní meze pro každou funkci. Když jsou tyto prahové hodnoty překročeny nebo je detekována provozní porucha, OFM generuje alarmy a výkazy o výkonu pro síťové operátory.

Klíčové komponenty implementace OFM zahrnují engine pro sběr dat, databázi konfigurace pravidel, logiku korelace událostí a reportovací moduly. Engine pro sběr dat odebírá nebo dotazuje relevantní báze management informací ([MIB](/mobilnisite/slovnik/mib/)) ze síťových elementů. Databáze pravidel uchovává provozní pravidla a prahové hodnoty pro každou monitorovanou funkci. Logika korelace analyzuje příchozí datové toky, aby rozlišila mezi izolovanými incidenty a systémovými problémy. Nakonec reportovací moduly formátují a předávají poznatky systémům správy sítě ([NMS](/mobilnisite/slovnik/nms/)) a systémům provozní podpory ([OSS](/mobilnisite/slovnik/oss/)) pro vizualizaci a další akce.

V širším síťovém ekosystému hraje OFM zásadní roli v automatizované správě poruch a zajištění výkonu. Poskytnutím detailního přehledu o provozu na úrovni funkcí umožňuje operátorům přejít od reaktivního řešení problémů k prediktivní údržbě. Tato schopnost je základní pro zajištění vysoké dostupnosti služeb, optimalizaci využití zdrojů a plnění smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) s koncovými uživateli a podnikovými zákazníky.

## K čemu slouží

Operational Feature Monitor (OFM) byl zaveden, aby řešil rostoucí složitost sítí 3GPP a kritickou potřebu detailního dohledu specifického pro jednotlivé funkce. Jak se sítě vyvíjely od základních hlasových služeb a [SMS](/mobilnisite/slovnik/sms/) k bohatému portfoliu datových služeb, multimédií a inteligentních síťových funkcí, tradiční monitorování na úrovni elementů se stalo nedostatečným. Operátoři potřebovali způsob, jak zajistit, že každá jednotlivá servisní funkce – jako je přesměrování hovorů, hlasová schránka nebo služby založené na poloze – není pouze přítomna, ale také optimálně funguje z pohledu koncového uživatele.

Historicky se správa sítě silně zaměřovala na fyzický stav síťových uzlů (např. dostupnost základnové stanice, poruchy spojů). Avšak fakt, že uzel byl v provozu ('up'), nezaručoval, že konkrétní softwarová funkce na něm běžící fungovala správně. Tato mezera vedla k situacím, kdy docházelo ke zhoršení služeb bez aktivace tradičních alarmů, což mělo za následek špatný zákaznický zážitek a dlouhou průměrnou dobu opravy (MTTR). Koncept OFM byl motivován potřebou tuto mezeru zaplnit a poskytnout vrstvu správy, která rozumí logické servisní architektuře a může ověřovat provozní integritu jednotlivých funkcí.

Implementací OFM operátoři řeší problém neprůhledného zajištění služeb. Umožňuje cílené monitorování založené na servisní logice, což umožňuje rychlejší izolaci poruch na konkrétní funkci namísto celého síťového elementu. Tato schopnost je klíčová pro udržení kvality služeb v prostředí s více dodavateli a pro efektivní správu životního cyklu síťových funkcí, od nasazení a aktivace přes aktualizace až po případné vyřazení.

## Klíčové vlastnosti

- Shromažďování a agregace dat o výkonu specifických pro danou funkci
- Konfigurovatelné sledování prahových hodnot a generování alarmů pro stav funkce
- Integrace se standardizovanými rozhraními pro správu 3GPP (např. Itf-N)
- Podpora pro pasivní sběr měření i aktivní testovací sondování
- Korelace událostí k rozlišení poruch funkce od problémů se základními zdroji
- Generování standardizovaných výkazů správy výkonu (PM) a správy poruch (FM)

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification

---

📖 **Anglický originál a plná specifikace:** [OFM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ofm/)
