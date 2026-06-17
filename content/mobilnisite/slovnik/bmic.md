---
slug: "bmic"
url: "/mobilnisite/slovnik/bmic/"
type: "slovnik"
title: "BMIC – Bridge Management Information Container"
date: 2025-01-01
abbr: "BMIC"
fullName: "Bridge Management Information Container"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bmic/"
summary: "BMIC je standardizovaný datový kontejner zavedený ve 3GPP Release 16 pro správu síťových mostů v rámci 5G Core Network. Poskytuje strukturovaný formát pro výměnu konfiguračních, stavových a výkonnostn"
---

BMIC je standardizovaný datový kontejner podle 3GPP Release 16 určený pro výměnu informací pro správu mostů mezi síťovými funkcemi za účelem umožnění automatizované správy síťových mostů.

## Popis

Bridge Management Information Container (BMIC) je klíčová datová struktura definovaná v rámci řídicího rámce 3GPP, konkrétně ve specifikacích pro architekturu založenou na službách (SBA) 5G Core Network. Funguje jako standardizovaný obal nebo balík pro přenos podrobných informací týkajících se správy síťových mostů. Tyto mosty jsou logické nebo fyzické přepínací entity propojující různé síťové segmenty, jako jsou funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v rámci řezu nebo spojení mezi páteřní sítí a lokalitami edge computingu. BMIC je navržen pro přenos přes rozhraní založená na službách, primárně mezi funkcí pro analýzu síťových dat (NWDAF) a konzumentními [NF](/mobilnisite/slovnik/nf/), jako je funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) nebo funkce výběru síťového řezu ([NSSF](/mobilnisite/slovnik/nssf/)).

Architektonicky je BMIC součástí datových modelů a [API](/mobilnisite/slovnik/api/) pro správu definovaných ve specifikacích jako 29.512 (Network Slice Management) a 29.514 (Policy and Charging Control). Nejde o samostatnou síťovou funkci, ale o formát datové části. Když NF (např. řídicí systém) potřebuje nahlásit stav nebo nakonfigurovat most, naplní BMIC příslušnými atributy a odešle jej prostřednictvím služební operace. Kontejner obsahuje pole pro identifikátory mostů, provozní stavy (aktivní, pohotovostní, porucha), výkonnostní metriky (propustnost, latence, ztráta paketů), konfigurační parametry (politiky QoS, směrovací pravidla) a přidružené identifikátory síťového řezu nebo instance služby. Tento strukturovaný přístup zajišťuje interoperabilitu mezi řídicími systémy různých dodavatelů a analytickými funkcemi.

Hlavní úlohou BMIC je umožnit inteligentní správu v uzavřené smyčce. Například NWDAF může shromažďovat data BMIC z různých zdrojů, aby analyzovala trendy výkonu mostů. Pokud analýza odhalí přetížení nebo hrozící selhání kritického mostu v rámci síťového řezu, může NWDAF použít formát BMIC k doporučení nápravných akcí – jako je přerozdělení zátěže nebo převzetí služeb záložním mostem – řídicímu politickému subjektu. Standardizované schéma kontejneru umožňuje NWDAF porozumět a korelovat informace o mostech z různých částí sítě, což umožňuje holistickou optimalizaci. BMIC funguje jako společný jazyk pro data správy mostů a odděluje analytickou logiku od implementací mostů specifických pro dodavatele.

Během provozu zahrnuje životní cyklus vytvoření, naplnění, přenos a spotřebu. Spravující NF vytvoří instanci BMIC, naplní ji aktuálními řídicími informacemi (např. prostřednictvím služby Nnwdaf_EventsSubscription) a odešle ji konzumentovi. Konzument, často NWDAF, kontejner zpracuje, extrahuje data a použije je ve svých analytických modelech. Na základě výsledku může NWDAF vygenerovat nový BMIC s doporučenými akcemi nebo aktualizovanými politikami a odeslat jej zpět spravující NF nebo bodu pro rozhodování o politikách. Tato výměna umožňuje dynamické přizpůsobení prostředků mostů, což je zásadní pro udržování přísných smluv o úrovni služeb (SLA) pro 5G síťové řezy, zejména pro služby ultra-spolehlivé komunikace s nízkou latencí (URLLC) a komunikace s masivním počtem zařízení (mMTC).

## K čemu slouží

BMIC byl vytvořen, aby řešil rostoucí složitost správy přepínacích cest a mostů v architektuře založené na službách (SBA) 5G Core. Před Release 16 se správa propojovacích funkcí (jako rané mosty [UPF](/mobilnisite/slovnik/upf/) nebo bránové funkce) často opírala o proprietární nebo volně standardizované informační modely. To ztěžovalo automatizovanou analytiku a vynucování politik napříč doménami, protože zařízení každého dodavatele hlásila stav v různých formátech. Absence společné datové struktury bránila vizi plně automatizované, samostatně optimalizující sítě (SON) a komplikovala realizaci dynamického síťového řezání, kde mosty mezi segmenty řezů vyžadují přesnou správu v reálném čase.

Hnacím problémem byla potřeba jednotného datového modelu pro správu mostů na podporu pokročilé síťové automatizace a řezání. V 5G jsou síťové řezy logické end-to-end sítě se specifickými charakteristikami. Mosty mezi funkcemi uživatelské roviny nebo mezi páteří a edge představují kritická místa pro výkon řezu. Bez standardizovaného způsobu hlášení stavu, konfigurace a kapacity mostů nemohly systémy NWDAF a politik tyto prostředky efektivně monitorovat ani optimalizovat. To mohlo vést ke zhoršení výkonu řezů, porušení SLA a neefektivnímu využití zdrojů. BMIC poskytuje tento chybějící prvek a umožňuje správu řízenou analýzou.

Navíc nástup edge computingu a distribuovaných cloudových architektur v 5G zvýšil počet a význam mostů spojujících centrální páteřní sítě s edge lokalitami. Ruční správa těchto distribuovaných mostů je nepraktická. BMIC jako součást rámce pro analýzu dat správy 3GPP umožňuje shromažďování standardizovaných výkonnostních a poruchových dat z těchto distribuovaných mostů. Tato data živí modely strojového učení v NWDAF za účelem predikce selhání, optimalizace směrování provozu a automatického přizpůsobení konfigurace mostů – čímž řeší výzvy škálovatelnosti a agility vyplývající z distribuované povahy 5G.

## Klíčové vlastnosti

- Standardizované datové schéma pro konfiguraci, stav a metriky mostů
- Umožňuje interoperabilitu mezi systémy správy a analytickými funkcemi (NWDAF)
- Podporuje automatizaci v uzavřené smyčce pro optimalizaci mostů a obnovu po selhání
- Přenáší přidružená data pro síťové řezy a instance služeb
- Přenositelný přes rozhraní 3GPP založená na službách (např. Nnwdaf_EventsSubscription)
- Umožňuje daty řízené vynucování politik pro správu prostředků mostů

## Definující specifikace

- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3

---

📖 **Anglický originál a plná specifikace:** [BMIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bmic/)
