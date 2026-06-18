---
slug: "oam"
url: "/mobilnisite/slovnik/oam/"
type: "slovnik"
title: "OAM – Operations, Administration, and Maintenance"
date: 2026-01-01
abbr: "OAM"
fullName: "Operations, Administration, and Maintenance"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/oam/"
summary: "OAM zahrnuje procesy, činnosti, nástroje a standardy používané k provozování, správě a údržbě telekomunikační sítě. Je klíčové pro zajištění spolehlivosti sítě, monitorování výkonu, správu poruch a po"
---

OAM (Operace, správa a údržba) je soubor procesů, činností, nástrojů a standardů používaných k provozování, správě a údržbě telekomunikační sítě za účelem zajištění její spolehlivosti, výkonu a poskytování služeb.

## Popis

Operations, Administration, and Maintenance (OAM) je komplexní rámec pro správu telekomunikačních sítí, definovaný v četných specifikacích 3GPP. Nejde o jeden protokol, ale o soubor funkcí, rozhraní a procedur. Architektura je typicky založena na modelu Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)) a jeho evoluci do modelu FCAPS (Fault, Configuration, Accounting, Performance, Security). OAM funkce jsou distribuovány mezi síťové prvky (NEs), systémy správy prvků (EMSs) a systémy správy sítě (NMSs), které komunikují prostřednictvím standardizovaných rozhraní jako Itf-N. Mezi klíčové komponenty patří Network Resource Model ([NRM](/mobilnisite/slovnik/nrm/)), který poskytuje informační rámec pro spravované objekty, a mechanismy pro sběr a reportování dat Performance Management ([PM](/mobilnisite/slovnik/pm/)) a Fault Management ([FM](/mobilnisite/slovnik/fm/)). Jeho úlohou je zajistit efektivní provoz sítě, plnění smluv o úrovni služeb (SLAs) a možnost aktualizace a oprav s minimálním narušením. To zahrnuje kontinuální monitorování klíčových ukazatelů výkonu (KPIs), automatizované generování a korelaci alarmů pro izolaci poruch, správu softwaru a konfigurace pro aktualizace sítě a správu zabezpečení pro řízení přístupu a auditní stopy. V moderních sítích jsou principy OAM rozšířeny na virtualizovaná a cloud-nativní prostředí, která spravují virtualizované síťové funkce (VNFs) a cloudovou infrastrukturu spolu s fyzickými síťovými funkcemi (PNFs).

## K čemu slouží

OAM existuje, aby řešilo základní výzvu správy stále složitějších, heterogenních a rozsáhlých telekomunikačních sítí. Bez standardizovaného OAM by provozovatelé sítí čelili obrovským obtížím při poskytování služeb, diagnostice poruch, zajišťování kvality služeb a provádění rutinní údržby, což by vedlo k vysokým provozním nákladům a špatné zkušenosti zákazníků. Historicky proprietární systémy správy vytvářely závislost na dodavateli a problémy s interoperabilitou. 3GPP standardizovalo OAM, aby umožnilo interoperabilitu mezi více dodavateli, automatizovalo provozní úkoly a poskytlo jednotný pohled na síť. Řeší problémy jako manuální, náchylná k chybám konfigurace; pomalá detekce a řešení poruch; a nedostatek holistické viditelnosti výkonu. Vytvoření komplexních OAM standardů bylo motivováno potřebou provozní efektivity, zajištění služeb a schopnosti zavádět nové technologie (jako 5G a síťové segmenty) řiditelným způsobem. Řeší omezení ad-hoc a nestandardizovaných přístupů ke správě, které byly neudržitelné pro globální, škálovatelné mobilní sítě.

## Klíčové vlastnosti

- Standardizovaná správa poruch (FM) pro dohled nad alarmy, lokalizaci a nápravu poruch
- Komplexní správa výkonu (PM) pro sběr a analýzu klíčových ukazatelů výkonu (KPIs)
- Správa konfigurace pro manipulaci se softwarem, inventář a zřizování síťových prostředků
- Správa účtování pro sledování využití prostředků pro fakturaci a alokaci nákladů
- Funkce správy zabezpečení včetně řízení přístupu, auditních stop zabezpečení a kontroly integrity
- Podpora správy jak tradičních fyzických síťových funkcí, tak moderních virtualizovaných/cloud-nativních síťových funkcí

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.791** (Rel-16) — NWDAF Data Collection & Analytics Framework
- **TS 25.703** (Rel-12) — HNB Emergency Warning Area Study for UTRA
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- … a dalších 38 specifikací

---

📖 **Anglický originál a plná specifikace:** [OAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/oam/)
