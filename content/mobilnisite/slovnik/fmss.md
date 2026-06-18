---
slug: "fmss"
url: "/mobilnisite/slovnik/fmss/"
type: "slovnik"
title: "FMSS – Flexible Mobile Service Steering"
date: 2026-01-01
abbr: "FMSS"
fullName: "Flexible Mobile Service Steering"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fmss/"
summary: "Síťová schopnost, která dynamicky směruje uživatelský provoz na nejvhodnější přístupovou síť (např. 3GPP, ne-3GPP jako Wi-Fi) na základě politik, podmínek a požadavků služby. Optimalizuje uživatelský"
---

FMSS je síťová schopnost, která dynamicky směruje uživatelský provoz na nejvhodnější přístupovou síť na základě politik, podmínek a požadavků služby za účelem optimalizace uživatelského zážitku a využití zdrojů.

## Popis

Flexible Mobile Service Steering (FMSS) je rámec 3GPP zavedený pro inteligentní správu a směrování uživatelského datového provozu napříč více dostupnými přístupovými sítěmi, včetně 3GPP (např. LTE, 5G NR) a ne-3GPP (např. Wi-Fi, pevný broadband). Funguje na úrovni jádra sítě a zahrnuje především funkce řízení politik a mechanismy pro zjišťování a výběr přístupové sítě. Cílem je zajistit doručování služeb přes nejvhodnější přístupovou cestu podle aktuálních podmínek, politik a potřeb aplikace.

Architektonicky FMSS využívá několik komponent systému 3GPP. Mezi klíčové patří Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), která poskytuje pravidla politik; Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) v dřívějších vydáních nebo UE Policy Container v pozdějších systémech 5G, který doručuje směrovací politiky do UE; a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), která vynucuje rozhodnutí o směrování provozu. Rámec zohledňuje faktory jako zatížení přístupové sítě, kvalita signálu, údaje o předplatném, typ služby (např. nízká latence, vysoká propustnost) a uživatelské preference při rozhodování o směrování.

Jak to funguje, zahrnuje kontinuální cyklus monitorování, rozhodování a provedení. Síťové prvky a UE monitorují podmínky, jako je síla rádiového signálu, úroveň zahlcení a dostupná šířka pásma na každém přístupu. Na základě předem nakonfigurovaných politik z PCF (např. „směrovat video provoz na Wi-Fi, pokud je dostupná a není zahlcená“) se síť nebo UE rozhodne zahájit výběr přístupu nebo směrování provozu. To může vést k akcím, jako je přepnutí veškerého provozu [PDU](/mobilnisite/slovnik/pdu/) session na jiný přístup, vykládání konkrétních služebních datových toků nebo použití více přístupů současně prostřednictvím [ATSSS](/mobilnisite/slovnik/atsss/) (Access Traffic Steering, Switching and Splitting). Směrování může být řízeno sítí, asistováno UE nebo plně založeno na UE v závislosti na implementaci.

Její role v síti spočívá ve zlepšení kvality služby, optimalizaci využití zdrojů a umožnění plynulé kontinuity služeb. Dynamickým směrováním provozu pomáhá FMSS předcházet zahlcení v celulárních sítích, využívá levnější nebo vyšší kapacitní Wi-Fi spoje, pokud je to vhodné, a zajišťuje, že kritické služby udržují požadovaný výkon. Je to základní kámen pro konvergovaný přístup v 5G, podporující scénáře jako konvergence pevných a mobilních sítí a multi-access edge computing. FMSS mění tuhý, statický výběr přístupu na adaptivní, politikami řízený proces.

## K čemu slouží

FMSS bylo vytvořeno, aby řešilo rostoucí složitost heterogenních síťových prostředí, kde mají uživatelé současný přístup k více rádiovým technologiím (např. 5G, LTE, Wi-Fi). Tradiční výběr přístupu, často založený pouze na síle signálu nebo manuální volbě uživatele, byl neefektivní a mohl vést ke špatnému uživatelskému zážitku nebo suboptimálnímu vyrovnávání zatížení sítě. FMSS poskytuje systematický, na politikách založený přístup k automatizaci a optimalizaci tohoto výběru.

Primární problémy, které řeší, zahrnují správu zahlcení sítě, zlepšení kvality zážitku ([QoE](/mobilnisite/slovnik/qoe/)) a efektivní využití zdrojů. Například bez FMSS by UE mohlo zůstat na zahlcené celulární síti, i když je k dispozici vysokokvalitní Wi-Fi, což zhoršuje službu pro všechny uživatele. FMSS umožňuje operátorům definovat politiky, které směrují provoz na méně zatížené přístupy, čímž zlepšují celkový výkon sítě. Také umožňuje směrování citlivé na službu, kde jsou služby citlivé na latenci, jako je autonomní řízení, udržovány na 5G s nízkou latencí, zatímco hromadné stahování je vykládáno na Wi-Fi.

Historicky poskytovala raná řešení jako [ANDSF](/mobilnisite/slovnik/andsf/) ve vydání 8 statické politiky, ale postrádala dynamickou přizpůsobivost. FMSS, vyvíjející se prostřednictvím vydání jako 13 a 15, zavedlo větší flexibilitu integrací aktuálních síťových podmínek a bohatších ovládacích prvků politik. Řeší omezení předchozího jedno-přístupového nebo manuálního směrování tím, že umožňuje plynulé, inteligentní řízení více přístupů, což je nezbytné pro splnění různorodých požadavků služeb 5G a dosažení skutečné konvergence pevných a mobilních sítí.

## Klíčové vlastnosti

- Dynamické směrování provozu napříč 3GPP a ne-3GPP přístupovými sítěmi
- Rozhodování řízené politikami na základě síťových podmínek a požadavků služby
- Podpora Access Traffic Steering, Switching and Splitting (ATSSS)
- Integrace s PCF pro centralizované řízení politik
- Umožňuje režimy směrování řízené sítí, asistované UE nebo založené na UE
- Optimalizuje uživatelský zážitek a využití síťových zdrojů

## Související pojmy

- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.808** (Rel-14) — Study on Flexible Mobile Service Steering (FMSS)
- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TS 23.718** (Rel-13) — Flexible Mobile Service Steering Architecture
- **TS 23.746** (Rel-14) — Feasibility Study on Enhanced TV Services over 3GPP

---

📖 **Anglický originál a plná specifikace:** [FMSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fmss/)
