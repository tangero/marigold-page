---
slug: "mepc"
url: "/mobilnisite/slovnik/mepc/"
type: "slovnik"
title: "MEPC – MCPTT Emergency Private Call"
date: 2025-01-01
abbr: "MEPC"
fullName: "MCPTT Emergency Private Call"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mepc/"
summary: "MCPTT Emergency Private Call (MEPC) je klíčová funkce v rámci služby Mission Critical Push-To-Talk (MCPTT). Umožňuje autorizovanému uživateli zahájit během nouzové situace soukromý hlasový hovor typu"
---

MEPC je klíčová funkce služby MCPTT, která autorizovanému uživateli umožňuje zahájit soukromý nouzový hlasový hovor typu jeden na jednoho s dispečerem, přičemž přeruší komunikaci nižší priority pro okamžitou pomoc.

## Popis

[MCPTT](/mobilnisite/slovnik/mcptt/) Emergency Private Call (MEPC) je specializovaná komunikační služba definovaná v rámci standardu 3GPP pro Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), konkrétně pod službou Mission Critical Push-To-Talk (MCPTT). Jedná se o typ hovoru navržený pro naléhavou a důvěrnou komunikaci mezi jednotlivcem v nouzi (iniciátorem nouzového volání) a konkrétním respondentem, typicky dispečerem nebo velitelem týmu, během kritické události. Na rozdíl od skupinového nouzového hovoru, který je vysílán předdefinované skupině, MEPC vytváří vyhrazený audiokanál typu jeden na jednoho. Hovor je zahájen žádostí o nouzové spojení s vysokou prioritou, která v případě potřeby přednostně využívá síťové zdroje a přerušuje probíhající komunikaci.

Z architektonického hlediska funguje MEPC v aplikační vrstvě MCPTT, která je hostována na uživatelském zařízení (UE) a v síti na MCPTT aplikačních serverech. Klíčovými komponentami jsou MCPTT klient na uživatelském zařízení, MCPTT server (který spravuje řízení hovorů a distribuci médií) a podkladová síť 3GPP jádra (EPC nebo 5GC), která zajišťuje prioritní konektivitu. Když uživatel spustí MEPC, MCPTT klient odešle konkrétní servisní požadavek na MCPTT server. Tento požadavek obsahuje indikátory označující jej jako Emergency Private Call, včetně identity cílového uživatele (zamýšleného příjemce). MCPTT server žádost autentizuje, ověří autorizaci uživatele k provedení takového hovoru a následně jej zpracuje s nejvyšší prioritou.

Pracovní postup zahrnuje několik kroků. Nejprve iniciující klient odešle serveru zprávu žádosti o soukromý nouzový hovor MCPTT (MCPTT EMERGENCY private call request). Server poté odešle oznámení o příchozím hovoru klientovi cílového uživatele. Po přijetí je mezi oběma stranami vytvořena vyhrazená přenosová cesta pro média. Zásadní je, že jsou vyvolány mechanismy Quality of Service (QoS) sítě 3GPP. MCPTT server komunikuje s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/) v EPC) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/) v 5GC), aby zajistil, že datové toky hovoru získají nejvyšší QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/) nebo [5QI](/mobilnisite/slovnik/5qi/)), například ty vyhrazené pro mission critical hlas. To zaručuje minimální zpoždění a ztrátu paketů. Hovor je navíc soukromý, což znamená, že žádní jiní uživatelé se k němu bez autorizace nemohou připojit ani jej monitorovat. Hovor zůstává aktivní, dokud jej jedna ze stran výslovně neukončí, a server událost zaznamená pro účely auditu a analýzy incidentu, což je klíčový požadavek pro komunikaci v oblasti veřejné bezpečnosti.

## K čemu slouží

MEPC byl vytvořen, aby vyřešil kritickou mezeru v tradiční skupinové nouzové komunikaci pro záchranné složky a uživatele s požadavky na mission critical služby. Ve vysoce stresových operačních scénářích, jako je policista potřebující okamžitou podporu nebo hasič hlásící uvězněnou oběť, může být vysílání celé skupině nevhodné. Mohlo by způsobit zbytečnou paniku, zahlcovat sdílený kanál nebo ohrozit operační bezpečnost. Účelem MEPC je poskytnout přímou, okamžitou a důvěrnou linku ke konkrétnímu velitelskému orgánu nebo specialistovi, který může poskytnout přesné instrukce nebo vyslat cílenou pomoc bez upozornění ostatních.

Řeší problém přetížení komunikace a nedostatku diskrétnosti během nouzových situací. Před standardizovanými funkcemi [MCPTT](/mobilnisite/slovnik/mcptt/), jako je MEPC, měly profesionální rádiové systémy často omezené typy hovorů – typicky skupinové hovory a všeobecná volání. Jednotlivec v nouzi musel použít sdílený skupinový kanál, což mohlo blokovat komunikaci pro ostatní a chybělo zde soukromí. MEPC zavádí strukturovaný, prioritní soukromý kanál, který koexistuje se skupinovou komunikací. Zajišťuje, že nejnaléhavější individuální žádosti o pomoc jsou spolehlivě doručeny, a to i při přetížení sítě, prostřednictvím využití standardizovaných mechanismů priority a přednostního přerušení 3GPP.

Vývoj MEPC byl motivován požadavky globální komunity veřejné bezpečnosti na služby s požadavky na mission critical založené na LTE a 5G, jak jsou zachyceny v projektech, jako je práce 3GPP na MCPTT počínaje Release 13. Řeší omezení starších systémů pozemní mobilní rádiové komunikace (Land Mobile Radio – [LMR](/mobilnisite/slovnik/lmr/)) a raných VoIP služeb push-to-talk, kterým chyběly propracované, standardizované varianty nouzových hovorů. Definováním MEPC v rámci standardů 3GPP je zajištěna interoperabilita mezi zařízeními a sítěmi různých výrobců, což je prvořadé pro společné operace různých agentur. Tvoří nezbytnou součást širší služby MCPTT a naplňuje požadavek na flexibilní, spolehlivou a okamžitou hlasovou komunikaci v situacích ohrožujících život.

## Klíčové vlastnosti

- Soukromý hlasový hovor typu jeden na jednoho zahájený s nouzovou prioritou
- Přednostně využívá síťové zdroje a přerušuje komunikaci nižší priority pomocí mechanismů QoS (vysokoprioritní 5QI/QCI)
- Vyžaduje autorizaci; MEPC mohou iniciovat nebo přijímat pouze autorizovaní uživatelé MCPTT
- Cílené sestavení hovoru na konkrétní uživatelskou identitu (např. ID dispečera)
- Integrované protokolování a záznam pro auditní stopy a analýzu po incidentu
- Funguje v rámci nadřazené architektury služby MCPTT, rozhraní s MCPTT serverem a politickými funkcemi jádra 3GPP

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [PCP – Priority Code Point](/mobilnisite/slovnik/pcp/)

## Definující specifikace

- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MEPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mepc/)
