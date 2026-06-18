---
slug: "mda"
url: "/mobilnisite/slovnik/mda/"
type: "slovnik"
title: "MDA – Mobile Data Analytics"
date: 2026-01-01
abbr: "MDA"
fullName: "Mobile Data Analytics"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mda/"
summary: "MDA (Mobile Data Analytics) označuje soubor schopností a funkcí v sítích 3GPP pro sběr, analýzu a reportování síťových a uživatelských dat. Umožňuje operátorům získat přehled o výkonu sítě, uživatelsk"
---

MDA je soubor síťových schopností definovaných 3GPP pro sběr, analýzu a reportování síťových a uživatelských dat za účelem získání přehledů pro výkon, plánování a optimalizaci služeb.

## Popis

Mobile Data Analytics (MDA) v 3GPP je rámec definovaný pro sběr, zpracování a analýzu dat generovaných v mobilních sítích. Zahrnuje různé typy analýz, z nichž každý odpovídá specifickým MDA schopnostem, a jehož cílem je přeměna nezpracovaných síťových dat na využitelné poznatky. Architektura MDA zahrnuje sběr dat z různých síťových funkcí, centralizované nebo distribuované analytické enginy a tvorbu reportů, přehledů nebo spouštěčů pro optimalizační akce v síti.

Technicky MDA funguje definováním rozhraní a procedur pro zpřístupnění dat ze síťových funkcí ([NF](/mobilnisite/slovnik/nf/)) analytickým funkcím. Klíčové specifikace jako TS 28.104 a TS 28.562 detailně popisují aspekty řízení a orchestrace, včetně severozápadního rozhraní (NBI) pro reportování analytiky. Zdroje dat mohou zahrnovat přístupovou síť, jádro sítě a uživatelské zařízení (UE), zachycující metriky o rádiových podmínkách, propustnosti, latenci, míře chyb, informace o relacích a vzorcích mobility uživatelů. Tato data jsou agregována a zpracována pomocí statistických modelů, algoritmů strojového učení nebo pravidlových enginů za účelem identifikace trendů, anomálií a problémů s výkonem.

Rámec podporuje několik typů analýz, jako je Performance Analytics (pro síťové [KPI](/mobilnisite/slovnik/kpi/)), User Equipment Analytics (pro chování a zážitek UE), Network Function Analytics (pro stav a zatížení virtualizovaných NF) a Service Experience Analytics. Každý typ je spojen se specifickými datovými sadami a analytickými cíli. Například Performance Analytics může zpracovávat KPI na úrovni buňky pro detekci míst se špatným pokrytím, zatímco User Equipment Analytics může analyzovat propustnost na aplikační vrstvě pro vyhodnocení kvality zážitku ([QoE](/mobilnisite/slovnik/qoe/)). Výstup MDA lze využít pro automatizovanou optimalizaci sítě prostřednictvím operací v uzavřené smyčce, plánování kapacity, predikci poruch a vylepšenou péči o zákazníky.

MDA je úzce integrována s dalšími rámci pro řízení v 3GPP, jako je Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)) v 5G jádru a Management Data Analytics ([MDAF](/mobilnisite/slovnik/mdaf/)) v řídicí orchestraci. Zatímco NWDAF se zaměřuje na analýzu v reálném čase v rámci jedné domény pro automatizaci sítě, širší koncept MDA pokrývá jak analýzu v reálném čase, tak historickou analýzu v celém životním cyklu sítě včetně roviny řízení. Hraje klíčovou roli při umožnění samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)), správě síťových řezů a efektivním využívání zdrojů v stále složitějších a softwarově definovaných 5G sítích.

## K čemu slouží

MDA byla zavedena jako odpověď na rostoucí složitost mobilních sítí a explozivní nárůst dat generovaných uživateli, zařízeními a síťovými funkcemi. Před její standardizací se operátoři spoléhali na proprietární, izolované analytické nástroje pro různé síťové domény (RAN, jádro, přenos), což ztěžovalo získání holistického pohledu na výkon sítě a uživatelský zážitek. Toto roztříštění bránilo efektivnímu odstraňování problémů, plánování kapacity a implementaci automatizované optimalizace. Vzestup 4G LTE a následný příchod 5G s jeho sliby síťových řezů, ultra-spolehlivé nízkolatenční komunikace ([URLLC](/mobilnisite/slovnik/urllc/)) a masivního IoT vytvořily naléhavou potřebu po standardizovaném, škálovatelném analytickém rámci.

Primární problém, který MDA řeší, je přeměna obrovského množství nezpracovaných síťových dat na srozumitelné, využitelné informace. Bez efektivní analýzy jsou operátoři zahlceni daty, ale postrádají poznatky. MDA poskytuje strukturovaný způsob sběru dat ze standardizovaných rozhraní, aplikace analytických modelů a produkci výstupů, které mohou řídit rozhodování. To umožňuje proaktivní správu sítě, prediktivní údržbu a dynamické přidělování zdrojů. Například může identifikovat zhoršující se kvalitu streamovaného videa, než si na ni uživatelé stěžují, nebo předpovědět přetížení provozu v konkrétním sektoru buňky.

Motivací pro standardizaci MDA v rámci 3GPP bylo zajistit interoperabilitu mezi síťovým vybavením a analytickými platformami od různých dodavatelů, snížit náklady na integraci a urychlit inovace. Definováním společných datových modelů, rozhraní a typů schopností umožňuje operátorům kombinovat nejlepší komponenty a podporuje ekosystém pro analytické aplikace třetích stran. Navíc, jak se sítě stávají více softwarově definovanými a virtualizovanými ([NFV](/mobilnisite/slovnik/nfv/)), je MDA nezbytná pro monitorování výkonu virtualizovaných síťových funkcí (VNF) a automatickou správu operací životního cyklu. Je základním kamenem pro dosažení vize autonomních, samoléčících a samoopravných sítí.

## Klíčové vlastnosti

- Standardizovaný rámec pro sběr a analýzu síťových a uživatelských dat
- Podpora více typů analýz (např. výkonu, uživatelského zařízení, síťových funkcí)
- Integrace se systémy pro řízení a orchestraci (MANO) podle 3GPP
- Umožňuje automatizaci v uzavřené smyčce pro optimalizaci sítě a samoorganizující se sítě (SON)
- Poskytuje přehledy pro správu životního cyklu síťových řezů a zajištění SLA
- Umožňuje zpřístupnění dat aplikacím třetích stran prostřednictvím severozápadních rozhraní

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TS 28.104** (Rel-19) — Management Data Analytics (MDA)
- **TS 28.561** (Rel-20) — Management and Orchestration; Network Digital Twin
- **TR 28.809** (Rel-17) — Enhancement of Management Data Analytics (MDA) Study
- **TS 28.866** (Rel-19) — Study on Management Data Analytics (MDA) – Phase 3
- **TS 43.802** (Rel-12) — GERAN Enhancements for Mobile Data Applications

---

📖 **Anglický originál a plná specifikace:** [MDA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mda/)
