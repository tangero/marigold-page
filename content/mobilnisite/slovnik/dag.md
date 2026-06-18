---
slug: "dag"
url: "/mobilnisite/slovnik/dag/"
type: "slovnik"
title: "DAG – Directed Acyclic Graph"
date: 2025-01-01
abbr: "DAG"
fullName: "Directed Acyclic Graph"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dag/"
summary: "Directed Acyclic Graph (DAG, orientovaný acyklický graf) je topologická struktura sítě využívaná v 5G NR, zejména pro Integrated Access and Backhaul (IAB). Organizuje IAB uzly do hierarchické, necykli"
---

DAG je topologická struktura sítě využívaná v 5G NR pro Integrated Access and Backhaul (IAB), která organizuje uzly hierarchickým a necyklickým způsobem, aby umožnila efektivní více-skokové bezdrátové přenosové propojení (backhaul).

## Popis

Ve specifikacích 3GPP, konkrétně v TS 38.300, je Directed Acyclic Graph (DAG) fundamentálním architektonickým konceptem pro framework 5G Integrated Access and Backhaul ([IAB](/mobilnisite/slovnik/iab/)). Definuje logickou topologii a směrovací vztahy mezi IAB uzly a IAB donorem, který se připojuje k jádru sítě. DAG je grafová struktura skládající se z vrcholů (uzlů) a orientovaných hran (propojení), se zásadní vlastností absence cyklů – to znamená, že neexistuje cesta, která by začínala a končila ve stejném uzlu při dodržení směru hran. Tato acyklická vlastnost je klíčová pro prevenci směrovacích smyček a zajištění deterministického, efektivního přeposílání paketů v rámci více-skokového bezdrátového přenosového propojení (backhaul).

Architektura DAG v IAB organizuje uzly hierarchickým způsobem. IAB donor funguje jako kořen (root) DAGu. IAB uzly jsou vůči sobě rodičovské nebo potomkovské uzly a vytvářejí stromovou strukturu, kde každý uzel (kromě donoru) má jeden nebo více rodičovských uzlů pro upstreamovou konektivitu směrem k donoru a jádru sítě. Každý IAB uzel také funguje jako potenciální rodič pro downstreamové potomkovské uzly nebo uživatelská zařízení (UE). Struktura DAG je vytvářena a udržována směrovacími protokoly a funkcemi správy topologie v rámci IAB systému, které se přizpůsobují změnám, jako je přidání uzlu, jeho výpadek nebo proměnlivá kvalita propojení.

Mezi klíčové operační komponenty v rámci DAG patří vrstva Backhaul Adaptation Protocol ([BAP](/mobilnisite/slovnik/bap/)) a směrovací identifikátory. Vrstva BAP, zavedená na IAB uzlech a donoru, je odpovědná za směrování paketů po přenosové síti na základě BAP Routing ID. Tento identifikátor je mapován na topologii DAG, což umožňuje nasměrování paketů správnou cestou prostřednictvím rodičovských-potomkovských vztahů. DAG umožňuje efektivní využití prostředků díky prostorové reutilizaci a více-skokové komunikaci. Podporuje vlastnosti jako redundantní cesty (kde uzel může mít více rodičů pro vyšší spolehlivost) a vyrovnávání zátěže, přičemž primární struktura DAG se vyhýbá cyklům, aby zjednodušila směrovací rozhodnutí a správu.

Role DAGu v 5G RAN spočívá v umožnění škálovatelného a nákladově efektivního zhušťování sítě. Díky možnosti více-skokového bezdrátového přenosového propojení (backhaul) snižuje závislost na pokládce optických kabelů ke každé základnové stanici. DAG poskytuje řízenou topologii, která podporuje správu QoS, výběr cesty a odolnost sítě. Je nedílnou součástí fungování IAB, umožňuje dynamickou rekonfiguraci a efektivní využití rádiových prostředků napříč přístupovými a přenosovými (backhaul) spoji v rámci jednotného 5G NR rozhraní.

## K čemu slouží

Koncept Directed Acyclic Graph (DAG) byl zaveden v 3GPP Release 16 k řešení výzvy ekonomického nasazování hustých 5G sítí, zejména v oblastech, kde je pokládka optického přenosového propojení (backhaul) neúměrně drahá nebo logisticky obtížná. Před [IAB](/mobilnisite/slovnik/iab/) a topologiemi založenými na DAG se mobilní sítě spoléhaly převážně na přenosové propojení (backhaul) se stromovou topologií (star-topology), kde každá základnová stanice vyžadovala přímé, vysokokapacitní drátové (optické nebo mikrovlnné) připojení k jádru sítě. Tento přístup omezoval rychlé nasazování a škálovatelnost. DAG umožňuje více-skokovou bezdrátovou síť se samo-přenosovým propojením (self-backhauling), kde uzly mohou vzájemně přeposílat provoz, což dramaticky snižuje potřebu pokrytí optickými kabely.

Historicky existovalo síťování typu mesh a více-skokové směrování v ad-hoc a bezdrátových senzorových sítích, ale nebyly integrovány do standardizovaných architektur mobilních sítí s přísnými požadavky na latenci, spolehlivost a QoS. Práce na IAB v 3GPP si kladly za cíl přinést tuto flexibilitu do 5G NR. DAG byl zvolen jako základní topologický model, protože jeho acyklická vlastnost inherentně předchází směrovacím smyčkám, které jsou škodlivé pro stabilitu a výkon sítě. Zjednodušuje směrovací protokoly, snižuje režii řízení a zajišťuje předvídatelné doručování paketů – což je nezbytné pro plnění 5G služebních smluv ([SLA](/mobilnisite/slovnik/sla/)).

DAG řeší problém efektivní správy topologie v dynamickém bezdrátovém prostředí. Umožňuje síti automaticky organizovat IAB uzly do hierarchické struktury, optimalizovat cesty na základě metrik propojení a zotavovat se z výpadků změnou přiřazení rodičovského uzlu (re-parenting). To operátorům umožňuje nasazovat sítě způsobem „zapoj a používej“ (plug-and-play) a podporuje případy užití, jako jsou dočasné akce, zlepšení pokrytí ve městech a pevný bezdrátový přístup ([FWA](/mobilnisite/slovnik/fwa/)). DAG je tedy klíčovým prostředkem pro nákladově efektivní a škálovatelné nasazení 5G sítí, jak jej zamýšlejí operátoři po celém světě.

## Klíčové vlastnosti

- Acyklická topologie, která zabraňuje směrovacím smyčkám a zajišťuje stabilní přeposílání paketů
- Hierarchická organizace s IAB donorem jako kořenem a rodičovskými-potomkovskými vztahy mezi uzly
- Podpora více-skokového bezdrátového přenosového propojení (backhaul) využívajícího rozhraní 5G NR
- Dynamická adaptace topologie a správa cest prostřednictvím BAP a směrovacích protokolů
- Umožňuje prostorovou reutilizaci spektra na různých skocích v grafu
- Podporuje redundanci sítě a vyrovnávání zátěže prostřednictvím více rodičovských uzlů

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [DAG na 3GPP Explorer](https://3gpp-explorer.com/glossary/dag/)
