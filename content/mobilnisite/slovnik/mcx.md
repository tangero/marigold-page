---
slug: "mcx"
url: "/mobilnisite/slovnik/mcx/"
type: "slovnik"
title: "MCX – Mission Critical X"
date: 2026-01-01
abbr: "MCX"
fullName: "Mission Critical X"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mcx/"
summary: "MCX (Mission Critical X) je rámec 3GPP pro standardizované služby kritické komunikace přes sítě 3GPP, kde X může být Push-to-Talk (MC-PTT), Video (MC-Video) nebo Data (MC-Data). Umožňuje spolehlivou,"
---

MCX je rámec 3GPP pro standardizované služby kritické komunikace, jako je Push-to-Talk, Video a Data přes mobilní sítě, umožňující spolehlivou, nízkolatenční a zabezpečenou skupinovou komunikaci pro uživatele z oblasti veřejné bezpečnosti a profesionální uživatele.

## Popis

Rámec MCX, standardizovaný organizací 3GPP, definuje sadu podpůrných prvků a požadavků na služby pro komunikaci kritickou pro plnění úkolů přes sítě LTE a 5G. Zahrnuje tři primární služby: Mission Critical Push-to-Talk (MC-PTT), Mission Critical Video (MC-Video) a Mission Critical Data (MC-Data). Tyto služby jsou navrženy tak, aby splňovaly přísné požadavky složek veřejné bezpečnosti, záchranných služeb a průmyslových uživatelů na okamžitou, spolehlivou a zabezpečenou skupinovou komunikaci. Architektura je postavena na 3GPP 5G System (5GS) nebo Evolved Packet System (EPS) a využívá řídicí a uživatelské roviny jádra sítě k zajištění garantované kvality služeb, prioritního řízení a robustní bezpečnosti.

Z architektonické perspektivy jsou služby MCX implementovány jako funkce aplikační vrstvy, které interagují s podkladovou sítí 3GPP prostřednictvím standardizovaných rozhraní. Mezi klíčové síťové funkce patří Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) pro QoS a vynucování politik, Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro data účastníků a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) pro zřizování relací. Pro MC-PTT systém spravuje řízení přístupu k vysílání (floor control), správu skupinových hovorů a distribuci médií. MC-Video zvládá přenos videa v reálném čase s funkcemi jako priorizace videa a indikace mluvčího. MC-Data podporuje výměnu dat, jako jsou obrázky, soubory a data ze senzorů, v kontextech kritické komunikace.

Fungování MCX závisí na schopnosti sítě 3GPP poskytovat izolované komunikační kanály se specifickými profily QoS, včetně garantované přenosové rychlosti, priority a možností přerušení jiných přenosů (pre-emption). Když uživatel zahájí relaci kritické komunikace, klientská aplikace MCX komunikuje s aplikačním serverem MCX, který následně interaguje s jádrem sítě 5G, aby vyžádal potřebné prostředky. Síť zajistí, že relace je zřízena s vysokou prioritou, případně přerušuje přenosy s nižší prioritou, pokud jsou prostředky omezené. Komplexní zabezpečení (end-to-end) je udržováno prostřednictvím vzájemného ověřování, šifrování a ochrany integrity, jak je definováno v příslušných bezpečnostních specifikacích 3GPP.

MCX hraje klíčovou roli v přechodu komunikace kritické pro plnění úkolů z tradičních systémů pozemní mobilní rádiové komunikace ([LMR](/mobilnisite/slovnik/lmr/)) na moderní širokopásmové mobilní sítě. Umožňuje složkám veřejné bezpečnosti využívat vysokou přenosovou kapacitu, celostátní pokrytí a pokročilé funkce sítí 4G a 5G při zachování spolehlivosti a bezprostřednosti potřebné pro záchranné operace. Rámec také podporuje interoperabilitu mezi různými sítěmi a poskytovateli služeb, což zajišťuje, že záchranáři mohou během rozsáhlých incidentů komunikovat bezproblémově.

## K čemu slouží

MCX bylo vytvořeno, aby řešilo potřebu standardizované, interoperabilní a vysoce výkonné komunikace kritické pro plnění úkolů přes komerční mobilní sítě. Historicky záviseli uživatelé z oblasti veřejné bezpečnosti a profesionální mobilní rádiové komunikace na proprietárních systémech pozemní mobilní rádiové komunikace ([LMR](/mobilnisite/slovnik/lmr/)), které často trpěly omezenou přenosovou kapacitou, izolovanými sítěmi a nedostatkem interoperability mezi různými organizacemi a regiony. Nástup 4G LTE a později 5G představoval příležitost využít širokopásmové schopnosti pro služby kritické komunikace, ale vyžadoval standardizovaný rámec pro zajištění spolehlivosti, bezpečnosti a konzistentní kvality služeb napříč různými nasazeními sítí a dodavateli.

Primární problém, který MCX řeší, je poskytování garantovaných komunikačních služeb s nízkou latencí, vysokou dostupností a funkcemi pro správu skupin přes sítě založené na IP. Tradiční služby mobilních sítí typu "best-effort" byly nedostatečné pro nouzové scénáře, kde musí být komunikace okamžitá a zaručená. MCX definuje specifické mechanismy QoS, prioritní řízení a možnost přerušení jiných přenosů (pre-emption) za účelem replikace a překonání schopností starších systémů LMR. Dále umožňuje integraci multimédií, jako je video a data, spolu s hlasem, čímž rozšiřuje operační schopnosti záchranářů.

Vývoj MCX byl motivován globálními požadavky veřejné bezpečnosti, zejména v návaznosti na iniciativy jako autorita FirstNet ve Spojených státech a snaha Evropské unie o společnou platformu pro komunikaci kritickou pro plnění úkolů. Vytvořením standardu 3GPP je zajištěna interoperabilita mezi dodavateli, snížení nákladů díky úsporám z rozsahu a ochrana investic do budoucna prostřednictvím sladění s vývojem mobilní technologie. MCX umožňuje organizacím využívat stejnou síťovou infrastrukturu pro komerční i kritický provoz, optimalizovat využití spektra a infrastruktury při zachování přísné izolace a zabezpečení pro kritickou komunikaci.

## Klíčové vlastnosti

- Standardizované služby Push-to-Talk (PTT), Video a Data pro použití v kritické komunikaci
- Garantovaná kvalita služeb (QoS) s úrovněmi priority a možnostmi přerušení jiných přenosů (pre-emption)
- Správa skupinové komunikace včetně dynamického vytváření skupin a řízení přístupu k vysílání (talker arbitration)
- Komplexní zabezpečení (end-to-end) s vzájemným ověřováním, šifrováním a ochranou integrity
- Interoperabilita mezi různými síťovými operátory a poskytovateli služeb MCX
- Využívá 3GPP 5G System (5GS) a Evolved Packet System (EPS) pro mobilitu a služby jádra sítě

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.280** (Rel-20) — Mission Critical Services Common Requirements
- **TR 22.890** (Rel-19) — Study on Railway Smart Station Services
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.500** (Rel-19) — 5GC Service Based Architecture Specification
- **TS 29.536** (Rel-19) — NSACF Service Based Interface Protocol
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing
- **TR 38.845** (Rel-17) — NR Positioning Use Cases Study

---

📖 **Anglický originál a plná specifikace:** [MCX na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcx/)
