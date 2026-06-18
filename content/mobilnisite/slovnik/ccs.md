---
slug: "ccs"
url: "/mobilnisite/slovnik/ccs/"
type: "slovnik"
title: "CCS – Converged Charging System"
date: 2026-01-01
abbr: "CCS"
fullName: "Converged Charging System"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ccs/"
summary: "Converged Charging System (CCS) je 3GPP standardizovaný systém online účtování, který sjednocuje účtování pro všechny síťové služby. Umožňuje řízení účtování v reálném čase, vynucování politik a správ"
---

CCS je 3GPP standardizovaný systém online účtování, který sjednocuje účtování v reálném čase, řízení politik a správu zůstatků pro všechny síťové služby, jako je hlas, data, zasílání zpráv a IMS.

## Popis

Converged Charging System (CCS) je základní síťová funkce definovaná 3GPP pro online účtování. Představuje zásadní architektonický vývoj od zastaralých, služebně specifických účtovacích systémů k jednotné platformě pro účtování v reálném čase. CCS integruje funkce Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) a Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) pro online účtování a poskytuje jednotný bod interakce pro síťové elementy vyžadující řízení kreditu v reálném čase. Funguje na základě referenčních bodů Diameter Ro a Gy a komunikuje s funkcemi Policy and Charging Rules Functions ([PCRF](/mobilnisite/slovnik/pcrf/)/PCRF), aplikačními servery a síťovými bránami.

Architektonicky je CCS postaven na konceptu Charging Function ([CHF](/mobilnisite/slovnik/chf/)), která je jeho centrální logickou entitou. CHF komunikuje se síťovými funkcemi prostřednictvím standardizovaných rozhraní založených na službách (např. Nchf) v sítích 5G Core. Zpracovává účtovací události v reálném čase, aplikuje tarifní logiku, odečítá prostředky z uživatelských účtů a povoluje nebo zamítá jednotky služeb na základě dostupného kreditu. Mezi klíčové vnitřní komponenty patří Account Balance Management Function ([ABMF](/mobilnisite/slovnik/abmf/)) pro správu zůstatků účastníků a Rating Function ([RF](/mobilnisite/slovnik/rf/)) pro stanovení peněžní ceny událostí využití služeb.

Její role v síti je klíčová pro monetizaci a řízení služeb. CCS autorizuje využití síťových zdrojů v reálném čase před nebo během poskytování služby, což umožňuje předplacené, na požádání a sponzorované datové služby. Generuje standardizované Charging Data Records ([CDR](/mobilnisite/slovnik/cdr/)) pro fakturaci a vyúčtování. Oddělením účtovací logiky od konkrétních síťových služeb umožňuje CCS operátorům rychle zavádět a tarifovat nové služby – jako jsou řezy 5G sítě, datové tarify pro IoT nebo služby edge computingu – bez nutnosti nasazovat pro každou z nich samostatnou účtovací infrastrukturu.

## K čemu slouží

CCS byl vytvořen, aby řešil omezení fragmentovaných, zastaralých účtovacích systémů, kde každý typ služby (hlas s přepojováním okruhů, paketová data, [SMS](/mobilnisite/slovnik/sms/), IMS) měl vlastní vyhrazenou účtovací platformu. Tento izolovaný přístup vedl k provozní složitosti, vysokým nákladům a neschopnosti nabízet jednotné, mezislužební účtovací plány (např. sdílené datové balíčky pro hlas a data). Rozmach nových služeb založených na IP a přechod k plně IP sítím (IMS) vyžadoval agilnější a konsolidovanou účtovací architekturu.

Primární problém, který řeší, je konvergence účtování v reálném čase napříč všemi přístupovými technologiemi (2G/3G/4G/5G, pevné sítě) a všemi typy služeb na jednu standardizovanou platformu. Tato konvergence umožňuje operátorům zavádět inovativní, personalizované cenové modely a rychleji uvádět služby na trh. Poskytuje také budoucí odolný základ pro účtování v samostatných sítích 5G, kde řezy sítě a architektura založená na službách vyžadují flexibilní, softwarově definovanou účtovací funkci, která může dynamicky komunikovat s ostatními síťovými funkcemi prostřednictvím API.

Historicky její zavedení ve 3GPP Release 11 představovalo významný krok k plné realizaci architektury Policy and Charging Control (PCC), neboť poskytla jednotnou entitu pro online účtování. Řešila potřebu jediného zdroje pravdy pro správu kreditu a zůstatků účastníka, čímž zlepšila zajištění příjmů a snížila riziko kreditního podvodu napříč různými doménami služeb.

## Klíčové vlastnosti

- Jednotné online účtování pro hlasové, datové, zprávové a IMS služby
- Řízení kreditu a autorizace v reálném čase prostřednictvím rozhraní Diameter Gy/Ro
- Centralizovaná funkce správy zůstatků účtu (Account Balance Management Function – ABMF)
- Podpora rozhraní založených na službách (Nchf) v sítích 5G Core
- Generování standardizovaných záznamů o účtování dat (Charging Data Records – CDR) pro fakturaci
- Flexibilní ratingový engine pro vícerozměrné tarifní plány

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)

## Definující specifikace

- **TS 23.844** (Rel-12) — IMS P2P Content Distribution Services Study
- **TS 25.709** (Rel-15) — Simplified HS-SCCH for UMTS Study
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 28.203** (Rel-18) — Charging management
- **TR 28.840** (Rel-18) — Technical Report
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TS 29.594** (Rel-19) — 5G Spending Limit Control Service Stage 3
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 32.279** (Rel-19) — 5G MBS Session Converged Charging
- **TS 32.290** (Rel-19) — 5G Charging for Service Based Interface
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters

---

📖 **Anglický originál a plná specifikace:** [CCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccs/)
