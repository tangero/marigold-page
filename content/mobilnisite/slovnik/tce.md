---
slug: "tce"
url: "/mobilnisite/slovnik/tce/"
type: "slovnik"
title: "TCE – Trace Collection Entity"
date: 2025-01-01
abbr: "TCE"
fullName: "Trace Collection Entity"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tce/"
summary: "Síťový prvek odpovědný za shromažďování, ukládání a správu záznamů trasování (trace records) od uživatelských zařízení (UE) a síťových uzlů pro monitorování výkonu, odstraňování problémů a optimalizac"
---

TCE je síťový prvek, který shromažďuje, ukládá a spravuje záznamy trasování (trace records) od uživatelských zařízení a síťových uzlů za účelem monitorování výkonu, odstraňování problémů a optimalizace.

## Popis

Trace Collection Entity (TCE) je klíčovou součástí architektury správy sítí podle 3GPP, speciálně navrženou pro shromažďování a ukládání informací o trasování generovaných uživatelskými zařízeními (UE) a různými síťovými elementy. Funguje jako součást funkce trasování (Trace Function) definované v rámci Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)). TCE přijímá záznamy trasování prostřednictvím rozhraní Itf-N od funkce Management Data Collection (MDC) nebo přímo od síťových elementů, v závislosti na architektuře. Tyto záznamy obsahují detailní, časově označené informace o signalizačních zprávách, datech uživatelské roviny, rádiových podmínkách a dalších událostech, které jsou nezbytné pro síťové operátory k monitorování výkonu, diagnostice problémů a optimalizaci síťových zdrojů.

Architektonicky je TCE typicky server nebo logická funkce, která komunikuje s řídicím prvkem trasování (Trace Control Entity, který aktivuje a deaktivuje trasování) a s trasovanými entitami, jako je [eNB](/mobilnisite/slovnik/enb/) v LTE nebo gNB v 5G, a s UE. Když je trasování aktivováno pro konkrétní UE nebo oblast, trasované entity generují záznamy trasování podle nakonfigurovaných parametrů (např. hloubka trasování, spouštěcí události) a předávají je TCE. TCE následně agreguje tyto záznamy, často z více zdrojů, a ukládá je ve strukturovaném formátu, například do souborů, pro následnou analýzu. V systémech 5G je role TCE rozšířena v rámci Service-Based Architecture ([SBA](/mobilnisite/slovnik/sba/)), kde může komunikovat s síťovými funkcemi (NFs), jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), za účelem sběru dat trasování souvisejících s rozhraními založenými na službách.

TCE podporuje různé typy trasování, včetně signalizačního trasování (signaling trace), trasování správy (management trace) a trasování pro minimalizaci jízdních testů ([MDT](/mobilnisite/slovnik/mdt/) trace). Signalizační trasování zachycuje signalizační zprávy mezi síťovými elementy, trasování správy shromažďuje data o konfiguraci a správě chyb a MDT trasování sbírá rádiová měření od UE, aby se snížila potřeba fyzických jízdních testů. TCE zajišťuje integritu a bezpečnost dat během sběru a ukládání, často s podporou šifrování a mechanismů řízení přístupu. Jeho výstup je využíván systémy správy sítě, analytickými nástroji a nástroji pro odstraňování problémů k získání přehledu o chování sítě, identifikaci anomálií a podpoře monitorování klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)), což v konečném důsledku přispívá ke zlepšení kvality služeb a uživatelského zážitku.

## K čemu slouží

TCE bylo zavedeno, aby řešilo rostoucí složitost mobilních sítí a potřebu efektivních, automatizovaných mechanismů pro sběr detailních provozních dat pro správu a optimalizaci. Před jeho standardizací se síťoví operátoři spoléhali na ad-hoc metody, jako je ruční sběr logů nebo proprietární nástroje, které byly často nekonzistentní, obtížně škálovatelné a nedostatečné pro řešení problémů v reálném čase. TCE poskytuje standardizovaný, centralizovaný přístup ke sběru trasování, který operátorům umožňuje shromažďovat komplexní data z distribuovaných síťových elementů a UE bez narušení služby.

Historicky, jak se sítě vyvíjely od 3G přes LTE k 5G, objem dat a rozmanitost služeb exponenciálně rostly, což činilo manuální monitorování nepraktickým. TCE tento problém řeší automatizací procesu sběru, umožňujíc spouštěné trasování na základě konkrétních událostí (např. přerušení hovoru, selhání předání) nebo periodického vzorkování. To je obzvláště důležité pro optimalizaci rádiových přístupových sítí, kde se podmínky dynamicky mění, a pro zajištění dodržování smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) v prostředí s více dodavateli. Jeho vytvoření bylo motivováno potřebou snížit provozní náklady (OPEX) prostřednictvím minimalizace jízdních testů a rychlejšího řešení závad.

V kontextu 5G a síťového dělení (network slicing) se role TCE stává ještě kritičtější. S síťovými řezy přizpůsobenými pro různé služby (např. enhanced mobile broadband, ultra-reliable low-latency communications) potřebují operátoři detailní data trasování pro monitorování výkonu řezy a izolaci problémů v rámci specifických řezů. TCE to podporuje umožněním trasování s ohledem na řezy (slice-aware tracing), kde mohou být záznamy trasování korelovány s identifikátory řezů. Tím se řeší omezení dřívějších systémů správy, které zacházely se sítí jako s monolitickou entitou, a poskytuje se tak viditelnost potřebná pro efektivní správu sofistikovaných, virtualizovaných infrastruktur moderních sítí.

## Klíčové vlastnosti

- Centralizovaný sběr a ukládání záznamů trasování (trace records) od UE a síťových uzlů
- Podpora více typů trasování včetně signalizačního, správy a MDT trasování
- Integrace s řídicím prvkem trasování (Trace Control Entity) pro aktivaci/deaktivaci relací trasování
- Standardizovaná rozhraní (např. Itf-N) pro interoperabilitu v sítích s více dodavateli
- Zabezpečené zpracování dat s mechanismy šifrování a řízení přístupu
- Schopnosti trasování s ohledem na řezy (slice-aware tracing) pro správu síťového dělení v 5G

## Související pojmy

- [MDT – Minimization of Drive Tests](/mobilnisite/slovnik/mdt/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TR 26.909** (Rel-19) — QoE Enhancement for Streaming Services
- **TS 32.421** (Rel-19) — Subscriber & Equipment Trace Concepts & Requirements
- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study
- **TS 32.851** (Rel-12) — Network Sharing OAM Requirements
- **TS 36.880** (Rel-13) — MDT Enhancements Study for E-UTRAN
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TR 38.890** (Rel-17) — NR QoE Management and Optimization

---

📖 **Anglický originál a plná specifikace:** [TCE na 3GPP Explorer](https://3gpp-explorer.com/glossary/tce/)
