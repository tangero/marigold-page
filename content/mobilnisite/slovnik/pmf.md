---
slug: "pmf"
url: "/mobilnisite/slovnik/pmf/"
type: "slovnik"
title: "PMF – Performance Measurement Function"
date: 2026-01-01
abbr: "PMF"
fullName: "Performance Measurement Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pmf/"
summary: "Síťová funkce, která shromažďuje, zpracovává a reportuje data o výkonnostních měřeních z různých síťových prvků. Je klíčová pro monitorování sítě, optimalizaci a zajištění kvality služeb tím, že posky"
---

PMF je síťová funkce, která shromažďuje, zpracovává a reportuje data o výkonnostních měřeních ze síťových prvků za účelem monitorování, optimalizace a zajištění kvality služeb.

## Popis

Funkce pro výkonnostní měření (PMF) je základní komponentou v rámci architektury správy 3GPP, konkrétně definovanou v kontextu 5G Core Network a jeho rozhraní založených na službách. Funguje jako producent dat o výkonnostních měřeních, shromažďující surové metriky ze síťových funkcí ([NF](/mobilnisite/slovnik/nf/)), jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). PMF tato data, která mohou zahrnovat čítače úspěšných procedur, míry selhání, měření latence a využití zdrojů, zpracovává a transformuje do strukturovaných reportů o výkonnosti. Tyto reporty jsou následně zpřístupněny konzumentům, především Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)) nebo externím systémům Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), prostřednictvím standardizovaných rozhraní založených na službách, jako je Npmf.

Architektonicky je PMF definována tak, aby podporovala jak okamžité, tak agregované reportování. Pro okamžité reportování může poskytovat data o výkonnosti téměř v reálném čase na vyžádání. Pro agregované reportování shromažďuje data po definovaných měřicích obdobích a generuje konsolidované reporty. Funkce spravuje měřicí úlohy, což jsou konfigurace specifikující, co měřit, ze které NF a v jakém formátu reportovat. Zajišťuje konzistenci dat a soulad s typy měření a formáty specifikovanými 3GPP, což umožňuje standardizovanou analýzu napříč více-dodavatelskými sítěmi.

Její role je nedílnou součástí automatizace s uzavřenou smyčkou a síťové inteligence. Tím, že poskytuje centralizovaný, standardizovaný mechanismus pro sběr dat o výkonnosti, PMF zásobuje analytické nástroje, které pohánějí optimalizaci sítě, prediktivní údržbu a dynamické přidělování zdrojů. Abstrahuje složitost sběru surových dat z jednotlivých NF a nabízí jednotnou službu pro správu výkonnosti. To podporuje klíčové cíle 5G, jako je síťové krájení (network slicing), kde je monitorování výkonnosti na úrovni jednotlivých řezů zásadní pro zajištění Smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)).

## K čemu slouží

PMF byla zavedena, aby řešila výzvy správy výkonnosti v architektuře 5G založené na službách ([SBA](/mobilnisite/slovnik/sba/)). Předchozí generace se spoléhaly na rigidnější přístupy orientované na správce prvků, kde byl sběr dat o výkonnosti často specifický pro dodavatele a těsně svázaný se síťovými prvky. To ztěžovalo centralizovanou, mezidoménovou analýzu a automatizaci. 5G SBA se svými oddělenými, cloud-nativními funkcemi vyžadovala nový paradigma pro pozorovatelnost.

Primární motivací bylo vytvořit standardizovanou, škálovatelnou a flexibilní funkci věnovanou vystavování dat o výkonnosti. To umožňuje síťovým analytickým a OAM systémům konzumovat data o výkonnosti konzistentním způsobem bez ohledu na dodavatele podkladové NF. Řeší problém datových sil a heterogenních metod sběru, které byly překážkou pro implementaci pokročilé, AI-řízené síťové automatizace a zajištění pro komplexní případy užití 5G, jako je síťové krájení a ultra-spolehlivá komunikace s nízkou latencí (URLLC).

Definováním PMF poskytlo 3GPP základní prvek pro službu Management Data Analytics Service (MDAS) a ekosystém NWDAF. Umožňuje síti samostatně monitorovat a optimalizovat na základě skutečných dat o výkonnosti, což znamená posun od reaktivní k proaktivní a prediktivní správě sítě. To je klíčové pro splnění různorodých a přísných požadavků na výkonnost služeb 5G.

## Klíčové vlastnosti

- Standardizovaný sběr výkonnostních měření ze síťových funkcí 5G Core prostřednictvím rozhraní založených na službách
- Podpora jak okamžitého (na vyžádání), tak agregovaného (periodického) reportování výkonnosti
- Správa měřicích úloh, včetně jejich vytváření, modifikace a ukončování
- Vystavení zpracovaných dat o výkonnosti konzumentům, jako jsou NWDAF a OAM systémy
- Soulad s typy měření a datovými formáty definovanými 3GPP pro konzistenci
- Umožňuje zajištění výkonnosti pro síťové řezy prostřednictvím schopností měření specifických pro jednotlivé řezy

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [PMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmf/)
