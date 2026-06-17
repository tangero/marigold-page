---
slug: "kqi"
url: "/mobilnisite/slovnik/kqi/"
type: "slovnik"
title: "KQI – Key Quality Indicators"
date: 2026-01-01
abbr: "KQI"
fullName: "Key Quality Indicators"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/kqi/"
summary: "Klíčové ukazatele kvality (KQI) jsou standardizované metriky používané k měření a řízení komplexní kvality služby (QoS) a kvality uživatelského zážitku (QoE) telekomunikačních služeb. Poskytují operát"
---

KQI je standardizovaná metrika používaná k měření a řízení komplexní kvality služby (QoS) a kvality uživatelského zážitku (QoE) telekomunikačních služeb z pohledu uživatele.

## Popis

Klíčové ukazatele kvality (KQI) jsou základní součástí řídicího rámce 3GPP, konkrétně v oblasti zajištění služeb a zdrojů. Jsou definovány jako kvantifikovatelné míry, které odrážejí kvalitu konkrétní služby tak, jak ji vnímá koncový uživatel. Na rozdíl od výkonnostních čítačů nižších vrstev ([KPI](/mobilnisite/slovnik/kpi/) – Klíčové ukazatele výkonnosti), které sledují stav síťových prvků (např. dostupnost buňky, propustnost), jsou KQI odvozené metriky, které překládají technický výkon sítě do kvality na úrovni služby. Typicky se vypočítávají agregací a korelací více KPI a dalších zdrojů dat, často za použití definovaných vzorců nebo modelů specifikovaných ve standardech 3GPP.

Architektura pro správu KQI zahrnuje několik funkčních entit. Model síťových zdrojů (NRM) poskytuje definice spravovaných objektů. K zpracování nezpracovaných měřicích dat (PM – Performance Measurement) a KPI za účelem výpočtu KQI lze využít funkci analytiky řídicích dat ([MDAF](/mobilnisite/slovnik/mdaf/)) nebo jiné analytické nástroje. Tyto KQI jsou pak zpřístupněny systémům pro správu sítě ([NMS](/mobilnisite/slovnik/nms/)/[OSS](/mobilnisite/slovnik/oss/)) a systémům pro správu služeb za účelem vizualizace, reportování a spouštění nápravných akcí. Definice KQI zahrnuje jeho název, přesný vzorec pro výpočet, metodu měření, periodu sběru a přidružené prahové hodnoty, které definují přijatelný, degradovaný a kritický stav služby.

KQI jsou definovány pro každý typ služby. Například pro službu Voice over LTE (VoLTE) zahrnují klíčové KQI úspěšnost sestavení hovoru, míru zrušení hovoru a střední hodnotu známky kvality ([MOS](/mobilnisite/slovnik/mos/)) pro kvalitu řeči. Pro službu streamovaného videa by KQI zahrnovaly úspěšnost přehrání videa, počáteční čas bufferingu a poměr opakovaného bufferingu. Sledováním těchto metrik zaměřených na služby mohou operátoři proaktivně identifikovat degradaci kvality, provádět analýzu hlavní příčiny podrobným zkoumáním přispívajících KPI a zajistit plnění smluv o úrovni služeb (SLA). Standardizovaná povaha KQI v rámci 3GPP umožňuje konzistentní benchmarkování a porovnávání napříč různými nasazeními sítí a operátory.

## K čemu slouží

Účelem klíčových ukazatelů kvality je překlenout propast mezi čistě síťově orientovaným sledováním výkonu a skutečnou kvalitou, kterou zažívá zákazník. Tradiční správa sítě se silně zaměřovala na [KPI](/mobilnisite/slovnik/kpi/), jako je dostupnost uzlů a vytížení spojů, které, ač důležité, přímo nekorelovaly s tím, zda může uživatel úspěšně uskutečnit hovor ve vysoké kvalitě nebo streamovat video bez přerušení. Tato nesouvislost ztěžovala zajištění služeb a správu spokojenosti zákazníků.

KQI byly zavedeny, aby poskytly službově orientovaný pohled na výkon sítě. Řeší problém převodu technických metrik na obchodně relevantní míry kvality. To umožňuje operátorům přejít od reaktivního odstraňování problémů zaměřeného na síť k proaktivnímu zajištění služeb zaměřenému na služby. Definováním toho, co znamená „dobrá kvalita“ pro každou službu kvantifikovatelným způsobem, mohou operátoři stanovit jasné cíle, sledovat jejich plnění a upřednostňovat investice do sítě a optimalizace tam, kde mají největší dopad na vnímání uživatele.

Historicky, před rozšířenou standardizací KQI, vyvíjeli operátoři proprietární metriky kvality služeb, což vedlo k fragmentaci a ztěžovalo srovnání napříč dodavateli nebo operátory. Standardizace definic KQI, výpočetních metodologií a řídicích rozhraní (např. v řadě TS 32.450) organizací 3GPP vytvořila společný jazyk pro kvalitu služeb. To bylo motivováno zejména vývojem směrem k plně IP sítím a multimediálním službám (IMS), kde se vztah mezi síťovými podmínkami a vnímanou kvalitou stal složitějším a kritičtějším pro komerční úspěch.

## Klíčové vlastnosti

- Měření zaměřené na službu: Metriky jsou definovány na základě uživatelsky vnímatelných atributů služby (např. čas sestavení hovoru, míra zaseknutí videa).
- Odvozeno z KPI: Vypočítávají se zpracováním a korelací více podkladových síťových a elementových klíčových ukazatelů výkonnosti (KPI).
- Standardizované definice: 3GPP poskytuje společné vzorce, metody sběru a prahové hodnoty pro konzistentní implementaci.
- Hierarchická struktura: KQI lze agregovat z KQI služeb nižší úrovně do složených KQI služeb nebo zákazníků vyšší úrovně.
- Řízení založené na prahových hodnotách: Podporuje konfigurovatelné prahové hodnoty pro spouštění alarmů, reportů a automatizovaných nápravných akcí.
- Integrace s řídicími systémy: Definovaná rozhraní pro reportování KQI do systémů pro správu sítě (NM) a systémů pro správu prvků (EM) za účelem zajištění služeb.

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TR 26.909** (Rel-19) — QoE Enhancement for Streaming Services
- **TS 28.802** (Rel-15) — Management Study for 5G Network Architecture
- **TR 28.863** (Rel-18) — Technical Report on Key Quality Indicators
- **TS 32.410** (Rel-19) — 3GPP TS 32.410: Key Performance Indicators (KPI)
- **TS 32.450** (Rel-19) — E-UTRAN Key Performance Indicators (KPI) Definitions
- **TS 32.451** (Rel-19) — KPI Requirements for E-UTRAN

---

📖 **Anglický originál a plná specifikace:** [KQI na 3GPP Explorer](https://3gpp-explorer.com/glossary/kqi/)
