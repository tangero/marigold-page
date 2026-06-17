---
slug: "qci"
url: "/mobilnisite/slovnik/qci/"
type: "slovnik"
title: "QCI – Quality of Service Class Identifier"
date: 2026-01-01
abbr: "QCI"
fullName: "Quality of Service Class Identifier"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/qci/"
summary: "Skalární identifikátor používaný k určení standardizované sady charakteristik QoS pro přenosový kanál (bearer) v sítích 3GPP. Definuje parametry pro zpracování přeposílání paketů, jako je priorita, ro"
---

QCI je skalární identifikátor, který specifikuje standardizovanou sadu charakteristik kvality služeb (Quality of Service), jako je priorita a rozpočet zpoždění, pro přenosový kanál (bearer) v sítích 3GPP, a umožňuje tak diferenciaci provozu.

## Popis

Identifikátor třídy kvality služeb (Quality of Service Class Identifier, QCI) je základní mechanismus v rámci Evolved Packet System (EPS) standardu 3GPP pro správu a vynucování kvality služeb (QoS). Jedná se o standardizovanou celočíselnou hodnotu, v původní definici v rozsahu 1 až 9 a později rozšířenou, která se mapuje na předem nakonfigurovanou sadu charakteristik QoS. Tyto charakteristiky nejsou signalizovány pro každý přenosový kanál zvlášť, ale jsou to parametry specifické pro uzel, které jsou předem zřízeny v síťových prvcích, jako je eNodeB, Serving Gateway (S-GW) a Packet Data Network Gateway (P-GW). Když je přenosový kanál zřízen nebo upraven, je mu přidružena konkrétní hodnota QCI. Tato hodnota QCI slouží jako referenční ukazatel, který instruuje každý síťový uzel, jak zacházet s pakety patřícími do daného kanálu.

Každá hodnota QCI je spojena se specifickým typem prostředků (Guaranteed Bit Rate - GBR nebo Non-GBR), úrovní priority, rozpočtem zpoždění paketu (Packet Delay Budget, PDB) a mírou chybových ztrát paketů (Packet Error Loss Rate, PELR). Priorita je celé číslo, kde nižší hodnota znamená vyšší prioritu pro plánování. PDB definuje horní mez pro dobu, o kterou může být paket zpožděn mezi UE a P-GW (nebo mezi UE a RAN uzlem v 5G). PELR definuje horní mez pro míru ztrát paketů nesouvisejících s přetížením. Pro GBR přenosové kanály QCI také implikuje potřebu řízení přístupu (admission control) na základě garantované přenosové rychlosti. Síť tyto parametry používá k rozhodování o plánování, správě front a konfiguraci linkové vrstvy, aby splnila požadavky služeb.

Z architektonického hlediska je QCI klíčovou součástí modelu přenosového kanálu EPS. Používá se na rozhraní S5/S8 mezi S-GW a P-GW, na rozhraní S1 mezi eNodeB a MME/S-GW a přes rádiové rozhraní Uu. V řídicí rovině přijímá MME autorizovanou hodnotu QCI pro přenosový kanál od P-GW (přes S-GW) a předává ji eNodeB při zřizování kanálu. eNodeB poté tuto hodnotu QCI používá spolu se svými lokálně nakonfigurovanými mapovacími tabulkami k aplikování příslušného plánování rádiových prostředků (např. ve vrstvě MAC). V 5G se model QoS vyvinul s identifikátorem QoS pro 5G (5G QoS Identifier, 5QI), který je přímým konceptuálním nástupcem QCI, ačkoli s rozšířeným rozsahem standardizovaných hodnot a flexibilnějšími parametry pro nové typy služeb.

## K čemu slouží

QCI bylo zavedeno k řešení kritického problému diferenciace provozu a garantovaného výkonu služeb ve zcela IP mobilních sítích. Před vydáním 3GPP Release 8 a EPS byly okruhově přepínaná a paketově přepínaná doména oddělené, přičemž QoS byla často vázána na specifické, rigidní služby přenosových kanálů. Přechod na plochou IP architekturu vyžadoval novou, škálovatelnou a efektivní metodu pro správu různorodého provozu – od hlasu a streamování videa po prohlížení webu a na pozadí probíhající stahování souborů – přes sdílenou infrastrukturu. QCI toto poskytuje standardizací omezené sady dobře definovaných profilů QoS, což umožňuje interoperabilitu mezi různými dodavateli a zjednodušuje konfiguraci sítě a správu politik.

Jeho vytvoření bylo motivováno potřebou podporovat služby založené na IMS, jako je Voice over LTE (VoLTE), které vyžadují nízkou latenci a garantovanou šířku pásma, vedle běžného internetového provozu typu best-effort. Bez mechanismu, jako je QCI, by se se všemi pakety zacházelo stejně, což by vedlo ke špatné uživatelské zkušenosti u aplikací v reálném čase. QCI umožňuje operátorům vytvořit virtuální 'potrubí' (přenosový kanál) se specifickými charakteristikami pro službu nebo aplikaci, a zajistit tak přiměřené přidělování síťových prostředků. Abstrahuje složité parametry QoS pro každý tok do jednoduchého celého čísla, čímž snižuje signalizační režii a umožňuje rychlé a konzistentní vynucování politik v celé síťové cestě od jádra k rádiovému rozhraní.

## Klíčové vlastnosti

- Standardizované skalární celé číslo (původně 1-9, později rozšířeno) mapované na parametry QoS
- Definuje typ prostředků (GBR nebo Non-GBR) pro řízení přístupu k přenosovému kanálu (admission control)
- Specifikuje úroveň priority pro plánování paketů vzhledem k jiným přenosovým kanálům
- Přidružuje rozpočet zpoždění paketu (Packet Delay Budget, PDB) pro řízení latence
- Přidružuje míru chybových ztrát paketů (Packet Error Loss Rate, PELR) pro cíle spolehlivosti
- Předem nakonfigurováno v síťových uzlech, minimalizuje signalizační režii na přenosový kanál

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.348** (Rel-19) — xMB Interface Specification
- … a dalších 16 specifikací

---

📖 **Anglický originál a plná specifikace:** [QCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/qci/)
