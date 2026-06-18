---
slug: "atp"
url: "/mobilnisite/slovnik/atp/"
type: "slovnik"
title: "ATP – Access Transport Parameter"
date: 2026-01-01
abbr: "ATP"
fullName: "Access Transport Parameter"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/atp/"
summary: "ATP je parametr používaný v sítích 3GPP pro charakterizaci přenosových schopností přístupové sítě, zejména pro IP služby. Poskytuje informace o charakteristikách podkladové přenosové sítě, jako je šíř"
---

ATP je parametr používaný v sítích 3GPP pro charakterizaci přenosových schopností přístupové sítě (např. šířky pásma a latence) za účelem umožnění efektivního poskytování IP služeb a správy QoS.

## Popis

Parametr přístupového přenosu (ATP) je standardizovaný mechanismus ve specifikacích 3GPP, který kvantifikuje a sděluje přenosové charakteristiky přístupové sítě síťovým entitám zodpovědným za poskytování služeb a správu kvality. ATP funguje jako soubor parametrů popisujících klíčové ukazatele výkonu přenosové cesty mezi uživatelským zařízením (UE) a jádrem sítě, včetně metrik jako dostupná šířka pásma, zpoždění paketů, míra ztráty paketů a rozkmity. Tyto informace jsou klíčové pro aplikace a síťové funkce, které potřebují přizpůsobit své chování na základě podkladových přenosových schopností, zejména ve scénářích zahrnujících více přístupových technologií nebo síťové segmenty (network slicing).

ATP funguje tak, že je měřen, vypočítáván nebo konfigurován na různých místech přístupové sítě, typicky na úrovni přístupového uzlu nebo brány, a následně sdělován příslušným síťovým funkcím prostřednictvím standardizovaných rozhraní. V architekturách 3GPP lze informace ATP vyměňovat mezi rádiovou přístupovou sítí (RAN), jádrem sítě a aplikačními funkcemi prostřednictvím referenčních bodů jako SGi, Rx a Gx. Soubor parametrů se řídí strukturovaným formátem definovaným ve specifikacích 3GPP, což umožňuje konzistentní interpretaci napříč různými síťovými implementacemi a zařízeními různých dodavatelů.

Klíčové komponenty zapojené do implementace ATP zahrnují měřicí funkce v přístupových uzlech (eNodeB, gNB nebo přístupové brány), funkce řízení politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)/[PCEF](/mobilnisite/slovnik/pcef/)) a aplikační funkce, které informace ATP spotřebovávají. Přístupová síť průběžně monitoruje přenosové charakteristiky a aktualizuje hodnoty ATP, které jsou následně šířeny k rozhodovacím entitám. Tyto entity používají ATP k informovanému rozhodování o řízení přijímání služeb, přidělování prostředků, směrování provozu a adaptaci kvality, čímž zajišťují optimální poskytování služeb vzhledem k aktuálním přenosovým podmínkám.

ATP hraje klíčovou roli při umožnění správy kvality služeb (QoS) od konce do konce napříč heterogenními sítěmi tím, že poskytuje standardizovaný způsob charakterizace přenosových schopností přístupu. Podporuje pokročilé síťové funkce, jako je síťové segmentování (network slicing), tím, že umožňuje porovnávat specifické přenosové požadavky segmentu se skutečnými přenosovými schopnostmi přístupu. ATP navíc usnadňuje efektivnější využití prostředků tím, že umožňuje aplikacím přizpůsobit jejich datové toky, úrovně komprese nebo vzorce přenosu na základě přenosových podmínek v reálném čase, čímž zlepšuje celkový uživatelský zážitek a efektivitu sítě.

## K čemu slouží

ATP byl vytvořen, aby řešil rostoucí složitost správy kvality služeb napříč různými přístupovými technologiemi v sítích 3GPP. Jak se mobilní sítě vyvíjely od primárně okruhově přepínaných hlasových služeb k paketovým multimediálním službám a jak byly integrovány různé rádiové přístupové technologie (2G, 3G, 4G, 5G, Wi-Fi), objevila se potřeba standardizovaného způsobu charakterizace přenosových schopností různých přístupových sítí. Předchozí přístupy se spoléhaly na technologicky specifické metriky, které nebylo možné snadno porovnávat nebo agregovat napříč různými typy přístupu, což ztěžovalo správu QoS od konce do konce.

Primární problém, který ATP řeší, je nedostatek přehledu o charakteristikách přístupového přenosu pro síťové funkce, které činí rozhodnutí související s QoS. Bez ATP měly funkce řízení politiky, aplikační servery a prvky jádra sítě omezené informace o skutečných přenosových podmínkách, které uživatelé zažívají, což vedlo k neoptimálnímu přidělování prostředků, neefektivní adaptaci služeb a nekonzistentnímu uživatelskému zážitku. ATP poskytuje společný jazyk pro popis přenosových schopností, který funguje napříč všemi přístupovými technologiemi definovanými 3GPP, a umožňuje tak inteligentnější rozhodování o poskytování služeb.

Vytvoření ATP bylo motivováno rostoucím významem IP služeb v sítích 3GPP a potřebou podporovat aplikace citlivé na kvalitu, jako je streamování videa, hraní her v reálném čase a kritické komunikace. Tím, že poskytuje standardizovanou charakterizaci přístupového přenosu, umožňuje ATP síťovým operátorům implementovat sofistikovanější mechanismy QoS, podporovat smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) napříč heterogenními přístupovými sítěmi a optimalizovat využití prostředků při zachování konzistentní kvality služeb bez ohledu na podkladovou přístupovou technologii.

## Klíčové vlastnosti

- Standardizovaná charakterizace přenosu napříč heterogenními přístupovými technologiemi
- Monitorování a hlášení metrik výkonu přístupové sítě v reálném čase
- Integrace s architekturou řízení politiky a účtování 3GPP
- Podpora síťového segmentování (network slicing) s přenosovými požadavky specifickými pro segment
- Umožňuje adaptaci aplikací na základě přenosových podmínek
- Usnadňuje správu QoS od konce do konce napříč přístupovou sítí a jádrem sítě

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)

## Definující specifikace

- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [ATP na 3GPP Explorer](https://3gpp-explorer.com/glossary/atp/)
