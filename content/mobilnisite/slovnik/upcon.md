---
slug: "upcon"
url: "/mobilnisite/slovnik/upcon/"
type: "slovnik"
title: "UPCON – User Plane Congestion management"
date: 2025-01-01
abbr: "UPCON"
fullName: "User Plane Congestion management"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/upcon/"
summary: "Rámec mechanismů definovaných 3GPP pro detekci, zmírňování a řízení zahlcení konkrétně v uživatelské rovině (user plane) mobilních sítí. Jeho cílem je udržet kvalitu služeb v období vysoké provozní zá"
---

UPCON je 3GPP rámec pro detekci a zmírňování zahlcení v uživatelské rovině mobilní sítě za účelem udržení kvality služeb při vysokém provozu dynamickým řízením prostředků.

## Popis

Řízení zahlcení uživatelské roviny (User Plane Congestion management, UPCON) je komplexní soubor funkcí a procedur standardizovaných 3GPP pro řešení zahlcení vyskytujícího se v datové cestě (uživatelské rovině) buněčných sítí. Na rozdíl od zahlcení řídicí roviny (control plane), které ovlivňuje signalizaci, se UPCON zabývá nedostatkem prostředků pro skutečný datový provoz uživatelů, jako je rádiová šířka pásma, kapacita transportní sítě nebo výpočetní výkon v uzlech uživatelské roviny. Rámec je podrobně popsán ve specifikacích jako 3GPP TS 23.705 (služby založené na blízkosti) a TS 26.938 (služba multimediálního vysílání/vícenásobného vysílání). Zahrnuje detekční mechanismy, politiky zmírňování a řídicí akce, které lze uplatnit na různých místech v síti, včetně rádiové přístupové sítě (RAN) a jádra sítě.

Z architektonického hlediska se UPCON účastní několik síťových funkcí. Mezi klíčové komponenty patří funkce pro politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)), funkce pro zjišťování a výběr přístupové sítě ([ANDSF](/mobilnisite/slovnik/andsf/)) pro směrování provozu, funkce pro povědomí o zahlcení v RAN ([RCAF](/mobilnisite/slovnik/rcaf/)) a funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v 5G. Detekce zahlcení může být založena na sledování klíčových ukazatelů výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)), jako je využití rádiových prostředků, zpoždění paketů, míra ztráty paketů nebo zaplnění vyrovnávací paměti v síťových uzlech. Jakmile je zahlcení identifikováno, jsou spuštěny akce pro jeho zmírnění. Tyto akce jsou různorodé a lze je uplatnit na uživatele, aplikaci nebo agregát provozu.

Princip fungování spočívá v procesu řízení s uzavřenou smyčkou. Síťový prvek, který zahlcení zažívá (např. eNodeB v LTE nebo gNB v NR), může hlásit svůj stav řídicím funkcím, jako je RCAF, nebo přímo jádru sítě. Na základě předdefinovaných politik pak síť může zavést opatření, jako je dynamické upravování parametrů kvality služeb (QoS) (např. snížení třídy QoS ([QCI](/mobilnisite/slovnik/qci/)) pro určité přenosy), implementace řízení tvarování a omezení provozu s ohledem na aplikaci, přesměrování provozu na alternativní přístupové sítě (např. Wi-Fi) nebo dokonce selektivní odmítání nových požadavků na služby pro provoz s nízkou prioritou. V kontextu služeb založených na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) a služby multimediálního vysílání/vícenásobného vysílání ([MBMS](/mobilnisite/slovnik/mbms/)) jsou mechanismy UPCON klíčové pro řízení zahlcení způsobeného mnoha zařízeními současně žádajícími o nebo účastnícími se skupinové komunikace, často prostřednictvím inteligentního plánování vysílání/vícenásobného vysílání a přidělování prostředků.

## K čemu slouží

UPCON byl zaveden, aby vyřešil rostoucí problém zahlcení uživatelské roviny v čím dál hustších a provozně vytíženějších mobilních sítích, zejména s nástupem streamování videa a neustále připojených aplikací. Tradiční síťové plánování a statické přidělování kapacity byly nedostatečné pro zvládnutí nepředvídatelných nárůstů provozu, což vedlo k výraznému zhoršení uživatelského zážitku pro všechny účastníky v špičce. Vytvoření standardizovaného rámce pro řízení bylo motivováno potřebou dynamické, automatizované a politikami řízené reakce na zahlcení.

Řeší omezení dřívějších, primitivnějších přístupů, jako je prosté zahazování paketů nebo plošné omezování šířky pásma, které jsou neefektivní a nespravedlivé. UPCON umožňuje chytřejší řízení zahlcení tím, že bere v úvahu faktory jako úroveň předplatného uživatele, typ aplikace a aktuální síťové politiky. To je obzvláště kritické pro umožnění nových služeb, jako je tlačítkový hovor pro kritické mise (MCPTT) a veřejná bezpečnostní komunikace přes LTE/5G, kde je garantovaný přístup a priorita při zahlcení nezbytným požadavkem. Rámec umožňuje operátorům udržovat kvalitu služeb pro prémiové uživatele a kritické aplikace i při vysokém zatížení, optimalizovat celkové využití vzácných síťových prostředků.

## Klíčové vlastnosti

- Síťová detekce zahlcení uživatelské roviny pomocí KPI (např. využití prostředků, latence)
- Politikami řízené akce pro zmírnění (např. úprava QoS, omezení provozu, přesměrování)
- Podpora řízení zahlcení s ohledem na aplikaci (např. rozlišení videa od synchronizace na pozadí)
- Mechanismy pro směrování provozu s ohledem na zahlcení mezi 3GPP a ne-3GPP přístupem
- Vylepšené řízení pro skupinovou komunikaci a služby vysílání/vícenásobného vysílání (MBMS)
- Standardizovaná rozhraní pro hlášení a řízení zahlcení mezi RAN a jádrem sítě

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [RCAF – RAN Congestion Awareness Function](/mobilnisite/slovnik/rcaf/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 23.705** (Rel-13) — Study on User Plane Congestion Management
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [UPCON na 3GPP Explorer](https://3gpp-explorer.com/glossary/upcon/)
