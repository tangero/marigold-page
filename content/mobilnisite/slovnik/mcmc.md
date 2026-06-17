---
slug: "mcmc"
url: "/mobilnisite/slovnik/mcmc/"
type: "slovnik"
title: "MCMC – Mission Critical MBMS subchannel Control Protocol"
date: 2025-01-01
abbr: "MCMC"
fullName: "Mission Critical MBMS subchannel Control Protocol"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mcmc/"
summary: "Protokol definovaný pro služby Mission Critical Push-to-Talk (MCPTT) využívající MBMS. Řídí řízení podkanálů MBMS vyhrazených pro skupinovou komunikaci, což umožňuje efektivní distribuci hlasu a dat o"
---

MCMC (Mission Critical MBMS subchannel Control Protocol) je protokol pro řízení podkanálů MBMS pro skupinovou komunikaci v rámci služeb MCPTT a pro veřejnou bezpečnost, který umožňuje efektivní distribuci hlasu a dat od jednoho k mnoha.

## Popis

Mission Critical [MBMS](/mobilnisite/slovnik/mbms/) subchannel Control Protocol (MCMC) je řídicí protokol specifikovaný v 3GPP TS 24.380. Působí v rámci služeb Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), konkrétně pro Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) přes MBMS (Multimedia Broadcast Multicast Service). Jeho hlavní funkcí je řídit zřizování, modifikaci a uvolňování podkanálů MBMS přidělených pro relace skupinové komunikace MCPTT. Podkanál MBMS je logický kanál v rámci služby přenosu MBMS, používaný pro přenos médií a řídicích informací pro konkrétní skupinu MCPTT. Protokol umožňuje serveru MCPTT požádat [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Centre) o aktivaci nebo deaktivaci těchto vyhrazených podkanálů na základě dynamických potřeb skupinových hovorů.

Z architektonického hlediska se MCMC nachází mezi aplikačním serverem MCPTT a BM-SC v jádru sítě. Definuje konkrétní procedury a zprávy pro řízení podkanálů. Například při zahájení skupinového hovoru MCPTT použije server MCPTT protokol MCMC k odeslání žádosti o aktivaci podkanálu do BM-SC. Tato žádost zahrnuje parametry jako TMGI (Temporary Mobile Group Identity), popis relace a požadavky QoS pro podkanál. BM-SC po přijetí této žádosti koordinuje s LTE nebo 5G NR sítí zřízení potřebných rádiových přenosů MBMS a přidělení prostředků pro vysílání médií všem přihlášeným uživatelům v rámci servisní oblasti.

Protokol zajišťuje efektivní využití prostředků MBMS pro skupinovou komunikaci v rámci služeb kritických pro misi. Namísto vytváření více jednosměrných spojení slouží jeden vysílací proud MBMS všem členům skupiny MCPTT, čímž se šetří rádiové prostředky i prostředky jádra sítě, zejména ve scénářích s mnoha posluchači. MCMC spravuje životní cyklus těchto podkanálů, včetně změn během relace (např. přidání nového mluvčího, změna QoS) a včasného uvolnění po skončení skupinového hovoru. Toto řízení je klíčové pro udržení kontinuity služby, upřednostnění kritického provozu a zajištění optimálního využití kapacity sítě pro operace veřejné bezpečnosti, kde je spolehlivá skupinová komunikace s nízkou latencí prvořadá.

## K čemu slouží

MCMC byl zaveden, aby řešil specifické požadavky služeb Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) na efektivní skupinovou komunikaci od jednoho k mnoha. Tradiční [MCPTT](/mobilnisite/slovnik/mcptt/) přes jednosměrné přenosové cesty může zatěžovat síťové prostředky při obsluze velkých skupin, protože vyžaduje individuální datové toky pro každého uživatele. To je neefektivní pro scénáře veřejné bezpečnosti, kde mnoho záchranářů potřebuje současně přijímat stejný hlasový přenos. Účelem MCMC je využít vysílací/multicastové schopnosti [MBMS](/mobilnisite/slovnik/mbms/) k odlehčení tohoto provozu, ale byl potřebný vyhrazený řídicí mechanismus pro integraci MBMS s aplikační vrstvou MCPTT.

Před MCMC bylo řízení MBMS obecnější a neoptimalizované pro dynamickou, relacemi řízenou povahu skupinových hovorů kritických pro misi. Vytvoření MCMC vyřešilo problém, jak může aplikační server MCPTT přímo a dynamicky řídit podkanály MBMS. Poskytuje potřebné signalizační rozhraní pro vyžádání vysílacích prostředků na požádání, jejich přizpůsobení konkrétním relacím skupin MCPTT a správu jejich parametrů QoS. To umožňuje síťovým operátorům podporovat rozsáhlou komunikaci kritickou pro misi s předvídatelnou latencí a vysokou spolehlivostí při efektivním využití omezeného rádiového spektra, což je klíčový aspekt během velkých incidentů nebo katastrof.

## Klíčové vlastnosti

- Dynamická aktivace a deaktivace podkanálů MBMS pro skupiny MCPTT
- Signalizační rozhraní mezi aplikačním serverem MCPTT a BM-SC (Broadcast Multicast Service Centre)
- Podpora vyjednávání parametrů QoS pro vysílací přenosy kritické pro misi
- Správa životního cyklu podkanálu (zřízení, modifikace, uvolnění)
- Přidružení podkanálů ke konkrétním TMGI (Temporary Mobile Group Identities) a ID skupin MCPTT
- Umožňuje efektivní distribuci médií od jednoho k mnoha pro komunikaci veřejné bezpečnosti

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol

---

📖 **Anglický originál a plná specifikace:** [MCMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcmc/)
