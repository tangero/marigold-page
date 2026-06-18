---
slug: "lwrc"
url: "/mobilnisite/slovnik/lwrc/"
type: "slovnik"
title: "LWRC – Long Window Rate Control"
date: 2025-01-01
abbr: "LWRC"
fullName: "Long Window Rate Control"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lwrc/"
summary: "LWRC je mechanismus řízení přenosové rychlosti pro služby multimediálního vysílání, jako je MBMS a eMBMS, který spravuje rychlosti přenosu dat v dlouhých časových úsecích. Zajišťuje efektivní využití"
---

LWRC je mechanismus řízení přenosové rychlosti pro služby multimediálního vysílání, který spravuje rychlosti přenosu dat v dlouhých časových úsecích, aby zajistil efektivní využití rádiových prostředků a stabilní kvalitu přizpůsobením se síťovým podmínkám.

## Popis

Long Window Rate Control (LWRC) je síťová funkce a algoritmus definovaný v architektuře služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) dle 3GPP, specifikovaný v TS 26.937. Jde o klíčovou komponentu pro správu doručování vysílaného a skupinového obsahu, jako je živé [TV](/mobilnisite/slovnik/tv/) nebo distribuce souborů, přes mobilní sítě. Z architektonického hlediska se LWRC typicky nachází v Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) nebo v příbuzném síťovém uzlu odpovědném za správu MBMS relací. Jeho primární rolí je určovat a řídit datovou rychlost, jakou je multimediální obsah přenášen přes vysílací přenosovou cestu (broadcast bearer).

LWRC funguje na základě analýzy požadavků a omezení v rámci 'dlouhého okna' (long window) – což je výrazně delší časový úsek ve srovnání s krátkodobým řízením rychlosti na úrovni jednotlivých paketů. Bere v úvahu různé vstupy, včetně požadavků na kvalitu služby (QoS) pro službu MBMS (např. garantovaný bitový tok), dostupných rádiových prostředků v buňkách vysílajících tuto službu, geografického rozložení zainteresovaných uživatelů a zpětné vazby o stavu kanálu. Na základě těchto agregovaných informací algoritmus LWRC vypočítá vhodnou přenosovou rychlost, kterou lze udržovat v celé vysílací oblasti, a zároveň splňuje cíle kvality služby a optimalizuje spektrální účinnost.

Klíčové komponenty, které s LWRC interagují, zahrnují MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)), eNodeB/gNodeB (pro LTE/NR) a UE. Rozhodnutí LWRC ovlivňuje, jak je obsah plánován na fyzické vrstvě. Jeho role spočívá v nalezení rovnováhy: nastavení rychlosti dostatečně vysoké pro doručení kvalitního videa nebo dat, ale dostatečně nízké, aby se zabránilo nadměrné spotřebě prostředků, která by mohla narušit unicastové služby nebo plýtvat kapacitou při nízkém počtu uživatelů. Díky práci v dlouhém časovém oknu poskytuje stabilitu, brání rychlým výkyvům rychlosti, které by mohly degradovat uživatelský zážitek, a umožňuje efektivní statistické multiplexování více toků služeb MBMS.

## K čemu slouží

LWRC byl zaveden, aby vyřešil základní výzvu efektivního řízení prostředků pro služby vysílání (broadcast) a skupinového vysílání (multicast) v mobilních sítích. Tradiční unicastový přenos je pro oblíbený obsah doručovaný současně mnoha uživatelům ve stejné oblasti inherentně neefektivní, protože duplikuje datové toky. [MBMS](/mobilnisite/slovnik/mbms/)/eMBMS byl vyvinut, aby tento problém řešil pomocí přenosu typu point-to-multipoint. Nicméně prosté vysílání obsahu pevnou vysokou rychlostí je plýtváním cenným rádiovým spektrem, zvláště když se hustota uživatelů mění.

Omezením dřívějších přístupů bez sofistikovaného řízení rychlosti byla buď statická, neefektivní alokace prostředků, nebo reaktivní, krátkodobá přizpůsobení, která mohla způsobovat nestabilitu kvality. Motivací pro LWRC byla potřeba proaktivního, na síť orientovaného řídicího mechanismu. Existuje za účelem optimalizace kompromisu mezi kvalitou služby a využitím prostředků v dlouhých časových úsecích a na rozsáhlých geografických oblastech. Tím, že bere v úvahu dlouhodobé trendy v poptávce uživatelů a síťovém zatížení, umožňuje LWRC operátorům nabízet vysílací služby (jako živé sportovní přenosy nebo zprávy) nákladově efektivním způsobem. Zajišťuje, že vysílací kanály použijí právě tolik prostředků, kolik je potřeba k uspokojení většiny uživatelů, aniž by připravovaly o kapacitu ostatní buněčné služby, čímž se MBMS stává životaschopnou komerční službou.

## Klíčové vlastnosti

- Řízení rychlosti založené na analýze v dlouhých časových oknech (minuty až hodiny)
- Zohledňuje QoS profily, dostupné prostředky buněk a rozložení uživatelů
- Optimalizuje spektrální účinnost pro vysílací/přenos typu point-to-multipoint
- Poskytuje stabilní přenosové rychlosti, aby se zabránilo kolísání kvality
- Umožňuje statistické multiplexování více toků služeb MBMS
- Síťový algoritmus, typicky umístěný v BM-SC

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [LWRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/lwrc/)
