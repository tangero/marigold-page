---
slug: "tdf-c"
url: "/mobilnisite/slovnik/tdf-c/"
type: "slovnik"
title: "TDF-C – Traffic Detection Function Control plane function"
date: 2025-01-01
abbr: "TDF-C"
fullName: "Traffic Detection Function Control plane function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tdf-c/"
summary: "Řídicí komponenta TDF, zodpovědná za správu pravidel a zásad pro detekci aplikací. Rozhraním k PCRF/PCF odděluje řídicí logiku od zpracování paketů v uživatelské rovině, což umožňuje škálovatelnost a"
---

TDF-C je řídicí (control plane) komponenta funkce pro detekci provozu (Traffic Detection Function), která spravuje pravidla a zásady pro detekci aplikací prostřednictvím rozhraní k PCRF/PCF.

## Popis

Funkce řídicí roviny pro detekci provozu (Traffic Detection Function Control plane function, TDF-C) je logická entita zavedená jako součást rozdělení monolitického [TDF](/mobilnisite/slovnik/tdf/). Představuje řídicí komponentu, zodpovědnou za všechny signalizační aspekty a správu zásad souvisejících s detekcí provozu. TDF-C komunikuje s funkcí pro pravidla řízení a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)) v 4G nebo s funkcí pro řízení zásad ([PCF](/mobilnisite/slovnik/pcf/)) v 5G přes referenční bod Sd (nebo jeho 5G ekvivalent). Jejím hlavním úkolem je přijímat, spravovat a ukládat pravidla pro detekci a řízení aplikací ([ADC](/mobilnisite/slovnik/adc/)) od řadiče zásad. Tato pravidla definují, které aplikace detekovat, metodu detekce (např. založenou na signatuře, na chování) a požadované akce po detekci, jako je hlášení PCRF/PCF nebo pokyn uživatelské rovině k blokování či přesměrování provozu.

Architektonicky je TDF-C oddělena od uživatelské roviny funkce pro detekci provozu ([TDF-U](/mobilnisite/slovnik/tdf-u/)), která zajišťuje vlastní hlubokou kontrolu paketů a jejich přeposílání. Toto oddělení následuje princip separace řídicí a uživatelské roviny (CUPS), což je klíčový trend moderního návrhu sítí pro vyšší škálovatelnost, nezávislé škálování zdrojů a flexibilitu nasazení (např. umístění funkcí uživatelské roviny blíže k okraji sítě). TDF-C obsahuje logiku pro správu relací, poskytování pravidel a hlášení událostí. Interpretuje ADC pravidla od PCRF/PCF a překládá je do specifických konfiguračních instrukcí pro jednu nebo více instancí TDF-U. Komunikace mezi TDF-C a TDF-U je standardizována, typicky s použitím protokolu jako je [PFCP](/mobilnisite/slovnik/pfcp/) (Packet Forwarding Control Protocol), jak je definováno pro jiné scénáře CUPS.

Během provozu, když je uživatelská relace zřízena, PCRF/PCF určí potřebu detekce aplikací a poskytne ADC pravidla TDF-C. TDF-C poté nastaví odpovídající detekční relaci na příslušné TDF-U instalací pravidel pro detekci paketů ([PDR](/mobilnisite/slovnik/pdr/)) a pravidel pro akce přeposílání ([FAR](/mobilnisite/slovnik/far/)). Když TDF-U detekuje specifikovaný aplikační provoz, může odeslat hlášení událostí zpět TDF-C, která je agreguje a přepošle PCRF/PCF. To umožňuje rámci zásad činit dynamická rozhodnutí na základě aktuálního využití aplikací. TDF-C také zajišťuje funkce související s účtováním, jako je spouštění generování záznamů o účtování TDF (TDF-CDR) účtovacím systémem na základě událostí detekce aplikací.

## K čemu slouží

TDF-C byla zavedena ve 3GPP Release 14 primárně pro podporu celoprůmyslového posunu k virtualizaci síťových funkcí (NFV), softwarově definovaným sítím (SDN) a separaci řídicí a uživatelské roviny (CUPS). Tradiční, monolitický TDF kombinoval funkce řídicí a uživatelské roviny v jednom fyzickém zařízení, což omezovalo flexibilitu nasazení, činilo škálování neefektivním (protože se obě roviny musely škálovat společně) a brzdilo inovace v datové rovině. Operátoři potřebovali možnost nasazovat vysoce výkonné, škálovatelné funkce uživatelské roviny (pro DPI) nezávisle na řídicí logice.

Oddělením TDF na TDF-C a TDF-U 3GPP tyto limity odstranila. Umožňuje operátorům nasazovat instance TDF-U distribuovaným způsobem, například na okraji sítě pro kontrolu s nízkou latencí, zatímco TDF-C je centralizována pro snadnější správu a koordinaci zásad. Toto oddělení umožňuje efektivnější využití zdrojů, protože řídicí rovina (TDF-C) může být škálována na základě počtu relací a složitosti zásad, zatímco uživatelská rovina (TDF-U) může být škálována na základě potřeb propustnosti a zpracování paketů. Také usnadňuje použití komerčních standardních hardwarových komponent pro uživatelskou rovinu a cloudové nasazení pro řídicí rovinu.

Vytvoření TDF-C bylo motivováno potřebou větší agility při nasazování nových služeb detekce aplikací a integrace s moderními orchestracemi a systémy správy. Poskytuje standardizovaný způsob řízení více, potenciálně od různých dodavatelů, uzlů TDF-U, což zajišťuje interoperabilitu a zjednodušuje síťové operace. Tato architektonická evoluce byla nezbytným krokem k tomu, aby se prosazování zásad s ohledem na aplikace stalo kompatibilní s principy 5G jádra sítě a širším trendem k rozděleným, službami založeným architekturám.

## Klíčové vlastnosti

- Spravuje ADC pravidla přijatá od PCRF/PCF přes rozhraní Sd
- Řídí jednu nebo více instancí TDF-U pomocí protokolů jako je PFCP
- Zajišťuje správu relací pro detekci aplikací
- Agreguje a hlásí události detekce aplikací řadiči zásad
- Umožňuje nezávislé škálování funkcí řídicí a uživatelské roviny
- Podporuje účtovací spouštěče pro využití založené na aplikacích

## Související pojmy

- [TDF-U – Traffic Detection Function User plane function](/mobilnisite/slovnik/tdf-u/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)

## Definující specifikace

- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.844** (Rel-14) — Control and User Plane Separation for EPC Nodes

---

📖 **Anglický originál a plná specifikace:** [TDF-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdf-c/)
