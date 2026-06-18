---
slug: "arp"
url: "/mobilnisite/slovnik/arp/"
type: "slovnik"
title: "ARP – Allocation and Retention Priority"
date: 2026-01-01
abbr: "ARP"
fullName: "Allocation and Retention Priority"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/arp/"
summary: "ARP je parametr QoS podle 3GPP používaný k stanovení priority při přidělování a udržování síťových prostředků pro přenosové kanály (bearery) během řízení přístupu a při zahlcení sítě. Určuje, které ka"
---

ARP je parametr QoS podle 3GPP, který stanovuje prioritu při přidělování a udržování přenosových kanálů (bearerů) během řízení přístupu (admission control) a při zahlcení sítě, aby bylo zajištěno přednostní zacházení s kritickými službami.

## Popis

Allocation and Retention Priority (ARP) je klíčový parametr kvality služeb (QoS) definovaný v architektuře 3GPP, konkrétně v rámci frameworku Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Funguje jako skalární hodnota, která typicky zahrnuje úroveň priority (1–15, přičemž 1 je nejvyšší), příznak schopnosti přerušení (pre-emption capability) a příznak zranitelnosti vůči přerušení (pre-emption vulnerability). ARP není parametrem na úrovni beareru používaným pro dynamické plánování (jako [QCI](/mobilnisite/slovnik/qci/)), ale spíše parametrem na úrovni předplatného nebo relace uplatňovaným při zřizování a správě životního cyklu beareru. Jeho primární funkce je vyvolána funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a vynucována funkcí Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) v jádru sítě, ve spolupráci s Radio Access Network (RAN) během správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)).

Z architektonického hlediska je ARP nedílnou součástí procedur zřizování a modifikace bearerů. Když dorazí požadavek na nový bearer (např. pro hlasové volání nebo datovou relaci), síť provede řízení přístupu (admission control). Hodnota ARP požadovaného beareru je porovnána s hodnotami ARP existujících bearerů a dostupnou kapacitou prostředků. Bearer s vyšší prioritou ARP (nižší číselná hodnota) má větší šanci na přidělení prostředků. Naopak při zahlcení sítě ARP určuje, které bearery mohou být přerušeny (uvolněny), aby se uvolnily prostředky pro provoz s vyšší prioritou. Příznak schopnosti přerušení udává, zda může bearer přerušit jiné, zatímco příznak zranitelnosti vůči přerušení udává, zda může být bearer sám přerušen.

Fungování ARP zahrnuje vícekrokový rozhodovací proces. Nejprve Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) ukládá hodnoty ARP specifické pro účastníka jako součást profilu předplatitele. Během zahájení relace PCRF tyto informace načte nebo použije dynamická pravidla politiky k přiřazení ARP k relaci [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network) nebo vyhrazenému beareru. Toto ARP je poté sděleno PCEF (např. v [PGW](/mobilnisite/slovnik/pgw/) pro 4G/5G) přes rozhraní Gx. PCEF zahrne ARP do požadavku na zřízení beareru odeslaného do přístupové sítě. V RAN používá eNB/gNB ARP spolu s dalšími parametry, jako jsou QCI a GBR, k provedení konečných rozhodnutí o přístupu a ke správě priority rádiových bearerů během handoverů a událostí zahlcení.

Jeho role se rozprostírá napříč celým životním cyklem sítě, od počátečního připojení (attach) přes mobilitu až po ukončení relace. Zajišťuje, že služby kritické pro misi, jako jsou tísňová volání IMS, signalizace operátora a vysokoprioritní podnikové služby, vždy získají přístup k síti, i když je síť vytížená. To činí z ARP základní kámen spolehlivosti sítě, efektivního využití prostředků a poskytování diferencovaných služeb, který tvoří statickou vrstvu priority, na níž operují dynamické mechanismy QoS.

## K čemu slouží

ARP byl zaveden, aby vyřešil základní problém správy omezených a sdílených síťových prostředků v prostředí s více službami. Před standardizovanými mechanismy QoS, jako je ARP, se sítě potýkaly s inteligentní prioritizací provozu, což vedlo k potenciální degradaci služeb pro všechny uživatele při zahlcení nebo k neschopnosti garantovat prostředky pro nezbytné služby. Vytvoření ARP bylo motivováno potřebou standardizované, politikou řízené metody pro kontrolu toho, které relace získají přístup k síti (přidělení – allocation) a které relace jsou zachovány, když je kapacita napjatá (udržení – retention).

Historicky, jak se mobilní sítě vyvíjely od hlasově orientovaných (2G) k paketovým sítím s více službami (3G a dále), rozmanitost provozu – od best-effort prohlížení webu po citlivé na zpoždění (VoIP) – vyžadovala sofistikovanější strategii řízení přístupu než jednoduché „kdo dřív přijde, ten dřív mele“. ARP řeší omezení takových zjednodušených přístupů tím, že poskytuje předem definované, operátorem konfigurovatelné schéma priorit. To umožňuje síťovým operátorům implementovat obchodní pravidla a smlouvy o úrovni služeb (SLA) přímo do logiky správy prostředků sítě, a zajistit tak ochranu výnosových nebo zákonem vyžadovaných služeb.

Dále ARP řeší specifickou výzvu kontinuity služeb během handoverů a výpadků sítě. Poskytnutím jasného indikátoru priority umožňuje síti činit konzistentní rozhodnutí o tom, které relace zachovat, když se uživatel přesouvá mezi buňkami nebo když je síťový prvek přetížen. Tento účel je klíčový pro udržení uživatelského zážitku a splnění regulatorních požadavků na služby, jako jsou nouzová komunikace, kterým musí být za všech síťových podmínek přiděleny prostředky s absolutní prioritou.

## Klíčové vlastnosti

- Definuje úroveň priority (1–15) pro přidělení a udržení beareru (admission and retention)
- Zahrnuje příznaky schopnosti přerušení (pre-emption capability) a zranitelnosti vůči přerušení (pre-emption vulnerability) pro správu zahlcení
- Používá se staticky během zřizování a modifikace beareru, nikoli pro dynamické plánování paketů
- Integruje se s architekturou PCC přes PCRF a PCEF
- Ukládá se v profilech účastníků na HSS pro prioritizaci založenou na předplatném
- Vynucuje se během správy rádiových prostředků (RRM) v RAN pro řízení přístupu

## Související pojmy

- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.216** (Rel-19) — SRVCC Architecture Enhancements
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.442** (Rel-19) — Node B Implementation Specific O&M Transport via RNC
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- … a dalších 26 specifikací

---

📖 **Anglický originál a plná specifikace:** [ARP na 3GPP Explorer](https://3gpp-explorer.com/glossary/arp/)
