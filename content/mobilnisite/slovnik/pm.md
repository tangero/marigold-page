---
slug: "pm"
url: "/mobilnisite/slovnik/pm/"
type: "slovnik"
title: "PM – Performance Measurement"
date: 2026-01-01
abbr: "PM"
fullName: "Performance Measurement"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pm/"
summary: "Performance Measurement (PM) je základní funkce správy sítě definovaná standardy 3GPP pro sběr, zpracování a reportování výkonnostních dat ze síťových prvků. Umožňuje operátorům monitorovat stav sítě,"
---

PM (Performance Measurement) je základní funkce správy sítě podle 3GPP pro sběr, zpracování a reportování výkonnostních dat ze síťových prvků za účelem monitorování stavu, kvality a vytížení sítě.

## Popis

Performance Measurement (PM) je klíčovou součástí rámce pro správu telekomunikačních sítí (Telecommunications Management Network – [TMN](/mobilnisite/slovnik/tmn/)) a Network Management ([NM](/mobilnisite/slovnik/nm/)) podle 3GPP, specifikovanou primárně v technických specifikacích řady 32 (Management and orchestration) a řady 28 (Management and orchestration for 5G networks). Definuje komplexní systém pro shromažďování nezpracovaných výkonnostních dat, známých jako Performance Measurements, ze spravovaných síťových prvků (NEs), jako jsou NodeB, eNodeB, gNB a funkce core sítě. Tato nezpracovaná měření představují čítače, měřidla a indikace stavu, které odrážejí provozní stav a vytížení síťových zdrojů.

Architektura zahrnuje úlohy měření výkonu (Performance Measurement Jobs – PM-Jobs) konfigurované systémem správy (např. Operation Support System – [OSS](/mobilnisite/slovnik/oss/)) na síťových prvcích nebo správcích prvků. PM-Job specifikuje, jaká měření se mají sbírat, jejich granularitu (např. 15minutovou, 1hodinovou, 24hodinovou) a plán. Síťový prvek, který funguje jako producent měření, sbírá nezpracovaná data v rámci specifikovaného období granularity, čímž vzniká soubor PM dat. Tato data jsou následně formátována do standardizovaných PM souborů (např. na bázi [XML](/mobilnisite/slovnik/xml/)) a přenášena do systému správy prostřednictvím rozhraní založených na souborech, jako je [FTAM](/mobilnisite/slovnik/ftam/), nebo modernějšími mechanismy.

Po přijetí systém správy, který funguje jako konzument měření, tyto PM soubory zpracovává. Zpracování zahrnuje parsování, validaci, agregaci (např. konsolidaci měření na úrovni buňky na úroveň lokality), analýzu překročení prahových hodnot a korelaci s jinými daty správy, jako jsou alarmy správy chyb (Fault Management – [FM](/mobilnisite/slovnik/fm/)). Zpracovaná data jsou uložena v úložišti správy výkonu (Performance Management – PM) pro historickou analýzu a reportování. Klíčové ukazatele výkonu (KPIs), které jsou odvozeny z jednoho nebo více nezpracovaných PM čítačů pomocí definovaných vzorců, jsou kalkulovány, aby poskytly praktické poznatky o výkonu sítě, jako je úspěšnost sestavení hovoru, úspěšnost předání spojení, propustnost a latence.

Role PM je klíčová pro celý životní cyklus sítě. Poskytuje empirická data potřebná pro plánování kapacity, identifikaci míst s přetížením, řešení problémů s degradací služeb, ověřování smluv o úrovni služeb (SLAs) a pro řízení automatizované optimalizace sítě a funkcí samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)). V 5G a dalších generacích slouží PM data také jako vstup pro síťovou analytiku, aplikace využívající [AI/ML](/mobilnisite/slovnik/ai-ml/) a uzavřenou smyčku automatizace pro správu založenou na záměrech.

## K čemu slouží

Performance Measurement byl vytvořen, aby řešil základní provozní potřebu kvantitativních, objektivních dat o chování sítě. Před standardizací dodavatelé implementovali proprietární řešení pro monitorování výkonu, což operátorům se sítěmi s více dodavateli extrémně ztěžovalo získání jednotného a konzistentního pohledu na výkon napříč celou sítí. Tato roztříštěnost bránila efektivním síťovým operacím, odstraňování problémů a správě kvality služeb.

Primární problém, který PM řeší, je poskytnutí rámce pro sběr výkonnostních dat, který je neutrální vůči dodavateli a agnostický vůči technologii. To umožňuje operátorům nasazovat zařízení od různých výrobců při zachování jednotného a soudržného provozního pohledu. Umožňuje srovnávání, konzistentní definici KPI v celé síti a spravedlivé hodnocení výkonu zařízení a služeb. Historický kontext spočívá v širších principech TMN, kde model správy FCAPS (Fault, Configuration, Accounting, Performance, Security) je klíčovým modelem. PM naplňuje pilíř 'Performance' (výkon), poskytuje data nezbytná pro proaktivní a reaktivní správu.

Navíc, jak se sítě vyvíjely od 2G zaměřené na hlas k datově bohatým 5G a IMS, se složitost a typy výkonnostních metrik dramaticky rozšířily. Standardizovaný rámec PM zajistil, že nové metriky pro propustnost paketových dat, kvalitu IMS (IP Multimedia Subsystem) relací a výkon síťového řezání v 5G mohou být bezproblémově integrovány do stávající infrastruktury správy. Poskytuje základní datovou vrstvu pro vyvíjející se provozní paradigmata, jako je správa sítě a služeb s nulovou dotykovostí.

## Klíčové vlastnosti

- Standardizované definice měření (čítače, měřidla) pro konzistentní sběr dat napříč dodavateli
- Konfigurovatelné úlohy měření (PM-Jobs) umožňující flexibilní plány sběru a granularitu
- Mechanismus reportování založený na souborech (PM soubory) pro spolehlivý hromadný přenos výkonnostních dat
- Podpora akumulace historických dat a analýzy trendů pro plánování kapacity
- Základ pro odvozování standardizovaných i uživatelských klíčových ukazatelů výkonu (KPIs)
- Integrace se správou chyb (Fault Management – FM) pro korelovanou analýzu hlavní příčiny

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)

## Definující specifikace

- **TS 28.533** (Rel-19) — Management and orchestration; Architecture framework
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 28.658** (Rel-19) — E-UTRAN NRM IRP Information Service
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.802** (Rel-15) — Management Study for 5G Network Architecture
- **TR 28.834** (Rel-18) — Technical Report
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 28.875** (Rel-19) — Study on IAB Node Management
- **TR 28.925** (Rel-19) — Enhancement of Service Based Management Architecture
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.103** (Rel-19) — 3GPP Management IRP Overview
- **TS 32.300** (Rel-19) — 3GPP Network Resource Naming Convention
- **TS 32.341** (Rel-19) — File Transfer IRP Requirements
- **TS 32.342** (Rel-19) — File Transfer IRP Information Service
- … a dalších 50 specifikací

---

📖 **Anglický originál a plná specifikace:** [PM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pm/)
