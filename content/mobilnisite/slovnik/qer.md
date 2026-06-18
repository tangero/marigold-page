---
slug: "qer"
url: "/mobilnisite/slovnik/qer/"
type: "slovnik"
title: "QER – QoS Enforcement Rule"
date: 2025-01-01
abbr: "QER"
fullName: "QoS Enforcement Rule"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/qer/"
summary: "Pravidlo pro vynucení QoS (QER) je pravidlo politiky definované v systému 5G pro vynucení specifických požadavků QoS na provoz v uživatelské rovině. Je základní součástí architektury řízení politiky a"
---

QER je pravidlo politiky v systému 5G, které vynucuje specifické požadavky QoS na provoz v uživatelské rovině jako součást architektury řízení politiky a účtování (Policy and Charging Control).

## Popis

Pravidlo pro vynucení QoS (QER) je klíčový prvek architektury řízení politiky a účtování ([PCC](/mobilnisite/slovnik/pcc/)) v 5G, specifikovaný v 3GPP TS 29.244 (protokol [PFCP](/mobilnisite/slovnik/pfcp/)) a TS 26.804 (aspekty specifické pro kodek). QER je kontejner instrukcí, který určuje, jak má funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) zacházet s pakety patřícími do konkrétní relace protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) nebo toku QoS. Je vytvářeno, upravováno nebo odstraňováno funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) na základě politik přijatých od funkce řízení politiky ([PCF](/mobilnisite/slovnik/pcf/)) pomocí referenčního bodu N7.

Každé QER obsahuje několik klíčových informačních prvků, které definují jeho chování při vynucování. To zahrnuje identifikátor QER, identifikátor toku QoS ([QFI](/mobilnisite/slovnik/qfi/)), na který se vztahuje, a sadu vynucovacích akcí. Primárními akcemi jsou stav brány (otevřená/zavřená), který řídí, zda jsou pakety propouštěny, a parametry vynucení QoS. Parametry QoS typicky zahrnují garantovanou přenosovou rychlost toku (GFBR), maximální přenosovou rychlost toku ([MFBR](/mobilnisite/slovnik/mfbr/)) a volitelně agregovanou přenosovou rychlost (ABR) pro daný tok. UPF používá tyto parametry k provádění policingu, označování a plánování paketů, aby byla zajištěna smluvní QoS.

Provozně jsou QER instalována v UPF pomocí procedury modifikace relace protokolu pro přenos paketů (PFCP). SMF odešle požadavek na modifikaci relace PFCP obsahující jedno nebo více QER, která mají být aplikována. UPF následně tato pravidla nainstaluje do své rychlé datové roviny, kde jsou porovnávána s příchozími pakety na základě filtrů, jako je QFI. Vynucování zahrnuje měření provozu vůči nakonfigurovaným přenosovým rychlostem, zahazování nebo označování (např. nastavení indikátoru způsobilosti k zahození) paketů překračujících limity a zajištění udržení minimálních garantovaných rychlostí. Tento mechanismus umožňuje vysoce dynamické a službě specifické zacházení s QoS, což je klíčové pro síťové řezy a architekturu založenou na službách v 5G.

## K čemu slouží

Pravidla pro vynucení QoS (QER) byla zavedena ve 3GPP Release 14, původně pro LTE Advanced Pro, a stala se ústředními pro 5G Core (5GC) definovaný v Release 15. Jejich vytvoření bylo motivováno potřebou flexibilnějšího, dynamičtějšího a podrobnějšího vynucení QoS nad rámec statických mechanismů identifikátoru třídy QoS (QCI) a priority přidělení a udržení (ARP) v 4G EPS. Předchozí systémy postrádaly schopnost dynamicky upravovat garance přenosových rychlostí a politiky vynucení pro každý tok během aktivní relace, což omezovalo podporu nových služeb s vysoce proměnlivými požadavky na šířku pásma.

Hlavním problémem, který QER řeší, je umožnění síťových řezů a službě specifických záruk QoS. V 5G může jedna relace PDU obsahovat více toků QoS s různými požadavky (např. jeden pro rozšířené mobilní širokopásmo a další pro ultra-spolehlivou komunikaci s nízkou latencí). QER poskytují nástroj pro PCF a SMF, aby instruovaly UPF, jak nezávisle a v reálném čase policovat a tvarovat každý tok. To je zásadní pro plnění smluv o úrovni služeb (SLA) pro různé případy užití, jako je průmyslový IoT, autonomní vozidla a rozšířená realita.

Dále QER usnadňují oddělení řídicí a uživatelské roviny v 5G. Definováním standardizovaného formátu pravidel komunikovaného přes PFCP umožňují centralizovanému PCF/SMF efektivně řídit distribuované UPF. Tento architektonický posun podporuje cloud-nativní nasazení a škálovatelnost. QER tak představují klíčový vývoj směrem k softwarově definovanému, politikami řízenému řízení QoS, které se dokáže přizpůsobit rychle se měnícím potřebám aplikací a stavům sítě.

## Klíčové vlastnosti

- Definuje vynutitelné parametry QoS pro každý tok QoS, včetně GFBR, MFBR a agregované přenosové rychlosti
- Obsahuje řízení stavu brány pro dynamické povolení nebo blokování přeposílání paketů pro tok
- Dynamicky poskytována PCF přes SMF a instalována v UPF pomocí protokolu PFCP
- Umožňuje policing, označování a plánování na úrovni jednotlivých toků v uživatelské rovině 5G
- Podporuje dynamické změny politik během aktivní relace PDU
- Základní pro realizaci síťových řezů a službě specifických záruk QoS

## Související pojmy

- [QFI – QoS Flow Identifier](/mobilnisite/slovnik/qfi/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [QER na 3GPP Explorer](https://3gpp-explorer.com/glossary/qer/)
