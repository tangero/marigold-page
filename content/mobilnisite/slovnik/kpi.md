---
slug: "kpi"
url: "/mobilnisite/slovnik/kpi/"
type: "slovnik"
title: "KPI – Key Performance Indicators"
date: 2026-01-01
abbr: "KPI"
fullName: "Key Performance Indicators"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/kpi/"
summary: "Kvantifikovatelné metriky používané k vyhodnocování výkonu, stavu a kvality mobilní sítě a jejích služeb. KPI jsou nezbytné pro plánování sítě, optimalizaci, správu poruch a zajišťování Quality of Ser"
---

KPI je sada kvantifikovatelných metrik používaných k vyhodnocování výkonu, stavu a kvality mobilní sítě a jejích služeb pro plánování, optimalizaci a zajišťování kvality služeb.

## Popis

Klíčové ukazatele výkonu (KPI) v 3GPP jsou standardizované, měřitelné hodnoty, které ukazují, jak efektivně síť, síťový řez nebo služba dosahuje klíčových provozních a obchodních cílů. Jsou odvozeny z měření shromažďovaných různými síťovými elementy ([NE](/mobilnisite/slovnik/ne/)), manažerskými systémy a sondami. Architektura pro správu KPI zahrnuje hierarchický řetězec sběru a zpracování dat: data výkonnostního měření (PM) jsou generována síťovými elementy (např. gNB, [AMF](/mobilnisite/slovnik/amf/), [UPF](/mobilnisite/slovnik/upf/)) jako hrubé čítače, události a měřidla. Tato data jsou následně shromažďována síťovými manažerskými ([NM](/mobilnisite/slovnik/nm/)) nebo elementárními manažerskými ([EM](/mobilnisite/slovnik/em/)) systémy přes standardizovaná rozhraní (např. Itf-N). Manažerské systémy následně aplikují definované vzorce – často specifikované v dokumentech 3GPP – aby agregovaly a spočítaly KPI z hrubých PM dat.

Fungování KPI je kontinuálním cyklem měření, sběru, výpočtu a analýzy. Například základní KPI rádiového přístupového segmentu (RAN) jako úspěšnost nastavení LTE Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) je vypočítáváno EM systémem. Ten sbírá ze základnové stanice eNodeB za definované měřicí období (např. 15 minut) hrubý čítač „AttConnEstabAtt“ (počet pokusů o navázání spojení RRC) a „AttConnEstabSucc“ (počet úspěšných pokusů). KPI je pak spočteno jako (Úspěšné pokusy / Celkový počet pokusů) * 100%. Tato vypočtená hodnota KPI je následně uložena, vizualizována a porovnávána s cílovými prahy pro posouzení výkonu. KPI pokrývají všechny síťové domény: Dostupnost (např. úspěšnost navázání hovoru), Uchování spojení (např. míra zrušených hovorů), Integritu (např. propustnost, latence), Dostupnost (např. doba provozuschopnosti uzlu) a Mobilitu (např. úspěšnost předání spojení).

Klíčové komponenty v ekosystému KPI zahrnují Úlohy výkonnostního měření konfigurované v síťových elementech, funkce Management Data Analytics ([MDA](/mobilnisite/slovnik/mda/)), které mohou KPI zpracovávat pro automatizaci, a standardizované definice a vzorce poskytované v Technických specifikacích (TS) a Technických zprávách (TR) 3GPP. Jejich role je mnohostranná: pro inženýry jsou diagnostickými nástroji pro analýzu hlavní příčiny; pro plánovače jsou vodítkem pro rozšiřování kapacity; pro operátory zajišťují soulad se Smlouvou o úrovni služeb (SLA), zejména u síťového řezání, kde jsou KPI specifické pro řez zásadní. Popis a metody výpočtu stovek KPI jsou detailně popsány v četných specifikacích 3GPP, včetně požadavků na služby (řada 22), management (řady 28, 32) a aspektů výkonu (řada 38.8xx pro NR).

## K čemu slouží

KPI existují, aby poskytly objektivní, kvantitativní základ pro hodnocení výkonu sítě a kvality služeb. Základní problém, který řeší, je potřeba přesunu od subjektivního, nepodloženého hodnocení stavu sítě k rozhodování založenému na datech. V počátcích mobilních sítí operátoři postrádali standardizované metriky, což ztěžovalo benchmarkování a interoperabilitu. KPI poskytují společný jazyk pro definování, co znamená „dobrý výkon“ v aspektech jako kvalita hlasového hovoru, rychlost dat a spolehlivost sítě.

Vytváření a kontinuální vývoj KPI v 3GPP je motivováno několika faktory: zaváděním nových technologií (např. 5G NR, síťové řezání), novými službami (např. Ultra-Reliable Low Latency Communication – URLLC) a potřebou automatizovaného řízení sítě. Každé nové vydání zavádí schopnosti, které vyžadují nová KPI pro jejich efektivní měření. Například 5G zavedlo KPI pro správu svazků, výkon síťového řezu a energetickou účinnost. Řeší omezení předchozích přístupů poskytováním stále granularnějších, na služby zaměřených a v reálném čase dostupných metrik. To operátorům umožňuje nejen monitorovat technický výkon sítě, ale také jej korelovat s kvalitou zážitku (QoE) koncového uživatele, což umožňuje proaktivní optimalizaci a efektivní využití zdrojů.

## Klíčové vlastnosti

- Standardizované definice a výpočetní vzorce napříč výrobci
- Pokrývají všechny síťové domény: RAN, Core, Transport a End-to-End
- Podpora tradičních síťových metrik i nových 5G/na služby zaměřených metrik
- Umožňují benchmarkování výkonu, monitorování SLA a analýzu hlavní příčiny
- Základ pro uzavřenou smyčku automatizace a Self-Organizing Networks (SON)
- Kritické pro zajištění a správu výkonu Síťového řezu

## Související pojmy

- [MDA – Mobile Data Analytics](/mobilnisite/slovnik/mda/)

## Definující specifikace

- **TR 21.866** (Rel-15) — Study on Energy Efficiency in 3GPP Standards
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.915** (Rel-15) — Release 15 Description: Summary of Rel-15 Work Items
- **TR 21.916** (Rel-16) — Rel-16 Description Summary
- **TR 21.917** (Rel-17) — Rel-17 Work Items Summary
- **TR 21.918** (Rel-18) — Release 18 Feature Summaries
- **TS 22.179** (Rel-20) — MCPTT Service Requirements
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.830** (Rel-16) — Business Role Models for Network Slicing
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 26.179** (Rel-19) — Codecs and Media Handling for MCPTT
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- … a dalších 21 specifikací

---

📖 **Anglický originál a plná specifikace:** [KPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/kpi/)
