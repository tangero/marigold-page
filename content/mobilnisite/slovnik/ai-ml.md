---
slug: "ai-ml"
url: "/mobilnisite/slovnik/ai-ml/"
type: "slovnik"
title: "AI/ML – Artificial Intelligence and Machine Learning"
date: 2026-01-01
abbr: "AI/ML"
fullName: "Artificial Intelligence and Machine Learning"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ai-ml/"
summary: "AI/ML v 3GPP označuje standardizovanou integraci technik umělé inteligence a strojového učení do mobilních sítí. Umožňuje daty řízenou optimalizaci, automatizaci a inteligentní rozhodování napříč domé"
---

AI/ML je standardizovaná integrace umělé inteligence a strojového učení do mobilních sítí za účelem umožnění daty řízené optimalizace, automatizace a inteligentního rozhodování napříč síťovými doménami.

## Popis

Framework [AI](/mobilnisite/slovnik/ai/)/[ML](/mobilnisite/slovnik/ml/) v 3GPP stanovuje standardizované mechanismy pro začlenění umělé inteligence a strojového učení do provozu mobilních sítí. Architektura využívá distribuovaný přístup s funkcemi AI/ML nasazenými na různých síťových lokalitách: funkce téměř v reálném čase u RAN Intelligent Controller (RIC) pro optimalizaci rádiového rozhraní, funkce mimo reálný čas u Service Management and Orchestration (SMO) pro optimalizaci v celosíťovém měřítku a funkce v core síti pro inteligenci služeb. Framework definuje standardizovaná rozhraní pro sběr dat, trénink modelů, provádění inferencí a distribuci výsledků mezi síťovými elementy.

Klíčové komponenty zahrnují systém pro správu pipeline AI/ML, který zvládá kompletní životní cyklus ML modelů od tréninku přes nasazení až po monitorování. NWDAF (Network Data Analytics Function) v 5G core síti slouží jako centralizovaný analytický engine, který může hostovat ML modely pro síťovou a servisní analytiku. Architektura RIC podporuje xApps a rApps implementující ML algoritmy pro optimalizaci RAN, se standardizovanými rozhraními (A1, E2) pro výměnu dat a řízení. Framework také specifikuje mechanismy sběru dat včetně standardizovaných datových sad, frekvencí sběru a datových formátů, aby byla zajištěna interoperabilita mezi řešeními AI/ML od různých dodavatelů.

Technická implementace zahrnuje několik standardizovaných procedur: sběr a přípravu dat pomocí definovaných datových modelů, trénink modelů centrálně nebo distribuovaně, nasazení modelů na inference body a průběžné monitorování a přetrénování modelů. Framework podporuje různé ML paradigmy včetně učení s učitelem, zpětnovazebního učení a federovaného učení. Pro optimalizaci RAN mohou ML modely predikovat vzorce provozu, optimalizovat beamforming, řídit handovery a dynamicky alokovat prostředky. V core síti ML umožňuje prediktivní správu QoS, detekci anomálií a optimalizaci uživatelského prožitku ze služeb. Systém managementu zahrnuje mechanismy pro správu verzí modelů, monitorování výkonu a záložní procedury pro zajištění stability sítě při podvýkonu ML modelů.

Bezpečnostní aspekty jsou nedílnou součástí návrhu s mechanismy pro ověřování integrity modelů, ochranu soukromí dat a bezpečnou distribuci modelů. Framework řeší výpočetní nároky definováním schopností pro integraci edge computingu a distribuované inference. Monitorování výkonu zahrnuje jak tradiční [KPI](/mobilnisite/slovnik/kpi/), tak metriky specifické pro ML, jako je přesnost modelu, latence inference a konvergence tréninku. Standardizace zajišťuje, že schopnosti AI/ML mohou být konzistentně implementovány napříč multisupplierskými sítěmi, a zároveň umožňuje inovace prostřednictvím otevřených rozhraní pro vlastní ML aplikace.

## K čemu slouží

Integrace [AI](/mobilnisite/slovnik/ai/)/[ML](/mobilnisite/slovnik/ml/) řeší rostoucí komplexitu sítí 5G a budoucích sítí 6G, kterou tradiční optimalizace založená na pravidlech nemůže efektivně zvládat. Jelikož sítě podporují rozmanité služby s náročnými požadavky (ultranízká latence, ultra vysoká spolehlivost, massive IoT), ruční konfigurace a statická optimalizace se stávají nepraktickými. Exploze síťových dat z připojených zařízení, aplikací a síťových elementů vytváří příležitosti pro daty řízenou optimalizaci, které předchozí generace sítí nemohly plně využít.

Historicky se síťová optimalizace spoléhala na expertní znalosti, předdefinovaná pravidla a periodické ruční úpravy. Tento přístup se nemohl rychle přizpůsobit měnícím se podmínkám ani odhalit složité vzorce v síťovém chování. Omezení se stala zvláště zjevná se zavedením síťového řezání (network slicing) v 5G, kde každý řez vyžaduje různé optimalizační cíle, které mohou být v konfliktu. Tradiční metody také zápasily s rozsahem konfigurací massive [MIMO](/mobilnisite/slovnik/mimo/), kde správa beamů zahrnuje tisíce parametrů, které na sebe komplexně působí.

Standardizovaný framework AI/ML umožňuje sítím stát se samooptimalizujícími se, čímž snižuje provozní náklady a zároveň zlepšuje výkon. Řeší konkrétní výzvy jako optimalizace energetické účinnosti (snižování spotřeby energie základnových stanic na základě predikcí provozu), robustnost mobility (predikce a prevence selhání handoverů) a vyvažování zatížení (optimální distribuce provozu mezi buňkami). Tím, že jsou schopnosti AI/ML součástí standardu, 3GPP zajišťuje interoperabilitu mezi řešeními různých dodavatelů a vytváří základnu pro síťovou inteligenci, která bude nezbytná pro vizi skutečně autonomních sítí v 6G.

## Klíčové vlastnosti

- Standardizovaná správa životního cyklu AI/ML (trénink, nasazení, monitorování)
- Distribuovaná inferenční architektura napříč doménami RAN, core sítě a managementu
- Integrace s NWDAF pro síťovou a servisní analytiku
- Optimalizace založená na RIC prostřednictvím xApps/rApps s ML schopnostmi
- Podpora federovaného učení s ochranou soukromí dat
- Monitorování výkonu modelů a záložní mechanismy

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.288** (Rel-20) — 5GS Architecture Enhancements for Data Analytics
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.530** (Rel-19) — AF AI/ML Services Stage 3 Protocol
- **TS 32.254** (Rel-19) — Charging for Northbound APIs
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters

---

📖 **Anglický originál a plná specifikace:** [AI/ML na 3GPP Explorer](https://3gpp-explorer.com/glossary/ai-ml/)
