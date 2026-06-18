---
slug: "dmos"
url: "/mobilnisite/slovnik/dmos/"
type: "slovnik"
title: "DMOS – Degradation Mean Opinion Score"
date: 2025-01-01
abbr: "DMOS"
fullName: "Degradation Mean Opinion Score"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dmos/"
summary: "Metrika percepční kvality videa, která předpovídá subjektivní kvalitu, kterou by uživatel zaznamenal při degradaci kvality videa, například při zahlcení sítě nebo při přechodu mezi buňkami (handover)."
---

DMOS je metrika percepční kvality videa, která předpovídá subjektivní uživatelský zážitek při degradaci kvality videa. Je odvozena od MOS a pomáhá operátorům monitorovat a optimalizovat kvalitu uživatelského zážitku (QoE) při streamování v mobilních sítích.

## Popis

Degradation Mean Opinion Score (DMOS) je klíčový ukazatel výkonu ([KPI](/mobilnisite/slovnik/kpi/)) používaný ve specifikacích 3GPP ke kvantifikaci percepční degradace kvality video služeb, jak ji vnímají koncoví uživatelé. Na rozdíl od tradičního středního názoru ([MOS](/mobilnisite/slovnik/mos/)), který poskytuje absolutní hodnocení kvality, DMOS konkrétně měří vnímaný rozdíl neboli degradaci mezi referenčním (původním) videozáznamem a zpracovanou nebo přenesenou verzí, která utrpěla zhoršení, jako jsou kompresní artefakty, ztráta paketů, zpoždění (jitter) nebo opětovné načítání (rebuffering).

Výpočet DMOS obvykle zahrnuje metodiky subjektivního testování standardizované orgány jako [ITU-T](/mobilnisite/slovnik/itu-t/), při kterých lidské osoby hodnotí zhoršené video vůči referenci na škále. V síťových operacích objektivní modely (algoritmy) předpovídají DMOS analýzou charakteristik videa a parametrů síťového zhoršení bez lidského zásahu. Tyto modely, jako jsou ty definované v ITU-T P.1203 nebo jiných přístupech VQM (Video Quality Metric), zpracovávají metriky jako datový tok, snímková frekvence, míra ztráty paketů a události zastavení pro výpočet predikované hodnoty DMOS.

V rámci architektury 3GPP je DMOS sledován a hlášen jako součást rámce pro sběr měření kvality uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) definovaného pro multimediální služby. UE nebo síťová sonda může měřit výkonnost doručování médií a pomocí standardizovaného modelu vypočítat DMOS. Tato data jsou pak nahlášena do sítě, často do funkce detekce provozu ([TDF](/mobilnisite/slovnik/tdf/)), funkce pravidel pro politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo přímo do operačního systému operátora prostřednictvím funkce analýzy manažerských dat ([MDA](/mobilnisite/slovnik/mda/)).

Role DMOS je nedílnou součástí optimalizace sítě v uzavřené smyčce. Sledováním hodnot DMOS v reálném čase nebo prostřednictvím agregovaných hlášení mohou síťoví operátoři identifikovat místa se zhoršením služby, korelovat je s rádiovými podmínkami nebo zatížením jádra sítě a spouštět akce politik. Například pokud DMOS pro službu streamování videa klesne pod práh v určité buňce, síť může upřednostnit provoz tohoto uživatele nebo upravit přidělování rádiových zdrojů, aby zlepšila QoE, zajistila spokojenost účastníků a snížila jejich odchod.

## K čemu slouží

DMOS byl zaveden, aby odstranil omezení jednoduchých metrik zaměřených na síť (jako propustnost, latence, ztráta paketů) při zachycení skutečného uživatelského vnímání kvality videa. Jak se mobilní sítě vyvíjely k doručování video služeb s vysokou šířkou pásma (streamování, konference), potřebovali operátoři způsob, jak měřit úspěch nejen v technickém doručení, ale i ve vnímané kvalitě. Tradiční [MOS](/mobilnisite/slovnik/mos/) poskytovalo absolutní skóre, ale neefektivně zdůrazňovalo dopad degradací způsobených sítí.

Vytvoření DMOS bylo motivováno potřebou diferenciální metriky, která by citlivě odrážela změny kvality způsobené síťovými podmínkami. Řeší problém kvantifikace „faktoru obtěžování“ nebo poklesu kvality, který uživatel zažívá při událostech, jako je zastavení videa, změny rozlišení nebo kompresní artefakty. To umožňuje cílenější optimalizaci; operátor může nastavit prahové hodnoty pro přijatelné úrovně degradace a automatizovat síťové reakce. Historicky jeho přijetí ve standardech 3GPP (počínaje Release 8 pro MBMS a později pro obecné monitorování QoE) umožnilo posun od doručování služeb na principu „best-effort“ k doručování služeb se zaručeným QoE, což je zásadní pro prémiové video služby a konkurenční diferenciaci.

## Klíčové vlastnosti

- Měří percepční degradaci kvality videa vůči nezhoršenému referenčnímu signálu.
- Podporuje jak subjektivní (lidmi hodnocené), tak objektivní (algoritmem predikované) metodiky měření.
- Integrováno do rámce pro sběr a hlášení měření QoE v 3GPP pro multimediální služby.
- Umožňuje síťově spouštěné akce politik na základě prahových hodnot degradace QoE v reálném čase nebo historických.
- Používá se pro benchmarkování a optimalizaci výkonu doručování videa napříč různými technologiemi rádiového přístupu (např. LTE, 5G NR).
- Umožňuje korelaci mezi kvalitou na aplikační vrstvě (DMOS) a podkladovými síťovými KPI pro analýzu hlavní příčiny.

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification

---

📖 **Anglický originál a plná specifikace:** [DMOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dmos/)
