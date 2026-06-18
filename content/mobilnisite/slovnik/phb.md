---
slug: "phb"
url: "/mobilnisite/slovnik/phb/"
type: "slovnik"
title: "PHB – Per Hop Behaviour"
date: 2025-01-01
abbr: "PHB"
fullName: "Per Hop Behaviour"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/phb/"
summary: "Komponenta modelu DiffServ definující způsob přeposílání (např. plánování, priorita zahazování) aplikovaný na paket v jediném síťovém uzlu. Je to stavební prvek pro kvalitu služeb (QoS) od konce ke ko"
---

PHB je komponenta modelu DiffServ, která definuje způsob přeposílání aplikovaný na paket v jediném síťovém uzlu, a slouží jako stavební prvek pro kvalitu služeb (QoS) od konce ke konci.

## Popis

Per Hop Behaviour (PHB) je klíčový koncept v architektuře Differentiated Services (DiffServ), standardizovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý 3GPP pro správu IP přenosů. Definuje chování při přeposílání paketů, které musí síťový uzel („hop“) aplikovat na konkrétní třídu provozu. PHB není služba, ale soubor pravidel implementovaných v mechanismech front a plánovače routeru či uzlu. Je vyvolán na základě hodnoty DiffServ Code Point ([DSCP](/mobilnisite/slovnik/dscp/)) v poli Type of Service (ToS) nebo Traffic Class hlavičky IP. Když paket dorazí, uzel zkontroluje jeho DSCP, namapuje ho na konkrétní PHB a následně aplikuje odpovídající zacházení prostřednictvím svých funkcí pro kondicionování provozu.

Implementace PHB zahrnuje několik klíčových komponent uvnitř síťového uzlu: klasifikátory, měřiče, značkovače, zahazovače a fronty. Klasifikátor třídí pakety podle DSCP. PHB pak diktuje akce, jako je plánovací priorita pro přenos z výstupního portu, fronta, do které je paket zařazen, a priorita zahazování používaná při zahlcení. Například PHB Expedited Forwarding ([EF](/mobilnisite/slovnik/ef/)) poskytuje službu s nízkou ztrátou, nízkou latencí a garantovanou šířkou pásma tím, že zajišťuje obsluhu paketů z fronty s vysokou prioritou a minimálním zpožděním ve frontě. Skupina PHB Assured Forwarding ([AF](/mobilnisite/slovnik/af/)) poskytuje několik tříd, každou se třemi úrovněmi priority zahazování, což umožňuje podrobnější zacházení při zahlcení.

V architektuře 3GPP jsou PHB klíčové pro implementaci charakteristik QoS přenosu EPS Bearer nebo 5G QoS Flow přes IP transportní síť (např. rozhraní [S1-U](/mobilnisite/slovnik/s1-u/), N3 nebo N9). Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) označí DSCP downlink IP paketů na základě pravidel QoS přidružených k přenosu/toku. Každý router v transportní síti jádra a přístupové trasy je nakonfigurován tak, aby tyto hodnoty DSCP rozpoznal a aplikoval odpovídající PHB. Tím vzniká souvislé zacházení hop po hopu, které společně realizuje cíle výkonu od konce ke konci, jako je garantovaný přenosový výkon, rozpočet zpoždění paketů a míra ztráty paketů. Model PHB je bezstavový a škálovatelný, protože každý uzel činí nezávislá rozhodnutí pouze na základě hlavičky paketu, čímž se vyhýbá potřebě signalizace na úrovni jednotlivých toků napříč jádrovou sítí.

## K čemu slouží

PHB existuje pro umožnění škálovatelné kvality služeb (QoS) ve velkých IP sítích, jako je Internet a transport 3GPP jádra. Před DiffServ používal model Integrated Services (IntServ) signalizaci na úrovni jednotlivých toků ([RSVP](/mobilnisite/slovnik/rsvp/)), což nebylo škálovatelné pro sítě poskytovatelů služeb s miliony současných toků. Model DiffServ založený na PHB byl vyvinut, aby toto překonal agregací provozu do omezeného počtu behaviorálních agregátů (tříd) a aplikací jednoduchého, rychlého zpracování na každém routeru.

3GPP tento model přijal pro správu různorodých požadavků na QoS různých aplikací (hlas, video, prohlížení webu, IoT) přes sdílenou IP infrastrukturu. Řeší problém poskytování předvídatelného doručování paketů pro služby v reálném čase, jako je VoLTE nebo kritický IoT, vedle datového provozu typu best-effort. Standardizací mapování mezi parametry QoS 3GPP (QCI/5QI) a DSCP/PHB zajišťuje konzistentní zacházení od brány jádrové sítě přes transportní síť až k okraji rádiové přístupové sítě.

Vytvoření PHB bylo motivováno potřebou jednoduchého, nasaditelného mechanismu pro diferenciaci služeb. Umožňuje síťovým operátorům definovat smlouvy o úrovni služeb (SLA) a optimalizovat své sítě pro jejich plnění bez nutnosti udržovat stav pro každou jednotlivou uživatelskou relaci. To je zásadní pro all-IP evoluci 3GPP, která umožňuje efektivní podporu konvergovaných služeb s různou citlivostí na zpoždění, rozkmity a ztráty přes nákladově efektivní, paketově přepínanou páteřní síť.

## Klíčové vlastnosti

- Definuje způsob přeposílání (plánování, zařazování do front, zahazování) v jediném síťovém uzlu.
- Aktivován hodnotou DiffServ Code Point (DSCP) v hlavičce IP paketu.
- Klíčová komponenta škálovatelné architektury IETF DiffServ.
- Zahrnuje standardizovaná chování jako Expedited Forwarding (EF) a Assured Forwarding (AF).
- Umožňuje agregaci toků provozu do malého počtu tříd pro škálovatelnou správu QoS.
- Implementován ve frontách a plánovačích routerů bez stavu na úrovni jednotlivých toků.

## Související pojmy

- [DSCP – Differentiated Services Code Point](/mobilnisite/slovnik/dscp/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study

---

📖 **Anglický originál a plná specifikace:** [PHB na 3GPP Explorer](https://3gpp-explorer.com/glossary/phb/)
