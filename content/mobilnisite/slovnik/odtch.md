---
slug: "odtch"
url: "/mobilnisite/slovnik/odtch/"
type: "slovnik"
title: "ODTCH – ODMA Dedicated Traffic Channel"
date: 2025-01-01
abbr: "ODTCH"
fullName: "ODMA Dedicated Traffic Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/odtch/"
summary: "Vyhrazený (dedikovaný) kanál pro přenos dat používaný v konceptu ODMA (Opportunity Driven Multiple Access), což byl raný návrh 3GPP pro ad-hoc, více-skokové přenosy v sítích UMTS. Byl navržen pro rozš"
---

ODTCH je vyhrazený (dedikovaný) kanál pro přenos uživatelských dat používaný v konceptu ODMA, což byl raný návrh 3GPP pro ad-hoc, více-skokové přenosy v sítích UMTS za účelem rozšíření pokrytí a kapacity.

## Popis

[ODMA](/mobilnisite/slovnik/odma/) Dedicated Traffic Channel (ODTCH) byl logický kanál definovaný ve specifikacích 3GPP pro UMTS jako součást rámce ODMA (Opportunity Driven [Multiple Access](/mobilnisite/slovnik/multiple-access/)). ODMA byl inovativní koncept představený ve vydání Release 99, který představoval systém ad-hoc, více-skokových přenosů založený na [TDD](/mobilnisite/slovnik/tdd/) (Time Division Duplex) a integrovaný do pozemní rádiové přístupové sítě UMTS ([UTRAN](/mobilnisite/slovnik/utran/)). ODTCH fungoval jako vyhrazený kanál pro přenos uživatelských dat (řeč nebo data) mezi uživatelskými zařízeními (UE) fungujícími jako přenosové stanice nebo mezi UE a pevnou síťovou infrastrukturou prostřednictvím těchto stanic. Operoval v rámci ODMA podsítě, což je dynamická topologie typu mesh, kde si UE mohla vzájemně objevovat a příležitostně navazovat přenosová spojení za účelem rozšíření dosahu sítě a zlepšení využití prostředků.

Z architektonického hlediska ODMA zavedlo nové síťové prvky a protokolové vrstvy pro podporu přenosové funkčnosti. ODTCH byl mapován na fyzické kanály definované pro ODMA TDD rozhraní. Kanál podporoval jak spojově orientované, tak nespojové služby, přizpůsobující se nepředvídatelné povaze ad-hoc spojení. Mezi klíčové součásti patřily vrstvy ODMA Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)), které zajišťovaly segmentaci, zpětné sestavování a plánování přenosů po více-skokové cestě. Provoz ODTCH byl řízen procedurami pro objevování přenosových stanic, navazování spojení a údržbu tras, vše koordinované distribuovaným směrovacím protokolem ve vrstvě ODMA.

Role ODTCH byla klíčová pro dosažení cílů ODMA, jimiž bylo rozšíření pokrytí a zvýšení kapacity bez nutnosti hustého nasazení infrastruktury. Umožňoval provozu procházet více bezdrátovými skoky mezi UE, čímž je efektivně využíval jako opakovače. Toto bylo zvláště zamýšleno pro scénáře jako venkovské oblasti nebo obnovu po živelních pohromách. ODTCH a širší koncept ODMA však čelily významným technickým výzvám, včetně složitého řízení výkonu napříč skoky, režie směrování, obtíží se synchronizací v TDD a potenciálních dopadů na výdrž baterií UE. Následně, přestože byly podrobně specifikovány, nebylo ODMA nikdy komerčně nasazeno v sítích UMTS, přičemž jeho koncepty později ovlivnily výzkum v oblasti komunikace zařízení mezi sebou ([D2D](/mobilnisite/slovnik/d2d/)) a přenosových technologií v LTE a 5G.

## K čemu slouží

ODTCH byl vytvořen pro podporu konceptu [ODMA](/mobilnisite/slovnik/odma/), jehož cílem bylo řešit základní výzvy raného nasazení sítí 3G UMTS: omezené rádiové pokrytí, zejména ve venkovských nebo topograficky náročných oblastech, a vysoké náklady na nasazení a údržbu husté sítě základnových stanic (Node B). Motivací bylo využít existující populace uživatelských terminálů k vytvoření samoorganizující se více-skokové přenosové sítě, čímž by se rozšířila služební stopa a zlepšila spektrální účinnost prostorovým opakovaným využitím.

Historicky, před ODMA, byly buněčné sítě striktně hierarchické, přičemž veškerá komunikace proudila přímo mezi UE a základnovou stanicí. Tento model vyžadoval kontinuální investice do infrastruktury pro pokrytí a byl neefektivní při zpracování sporadického rozložení uživatelů. ODMA, představené v základním vydání Release 99, navrhlo posun paradigmatu směrem k ad-hoc, uživateli podporované architektuře. ODTCH byl vyhrazeným přenašečem umožňujícím tento uživatelsky přenášený provoz, čímž řešil omezení jednoskokových buněčných spojení.

Navzdory své inovativní myšlence praktické problémy, které zavedlo – jako je řízení interference v více-skokovém TDD systému, zajištění kvality služeb (QoS) od konce ke konci a komerční složitost motivace uživatelů k přenosu provozu pro ostatní – nakonec zabránily jeho adopci. Práce na ODMA a ODTCH však poskytla cenné základy pro pozdější standardizované funkce 3GPP, jako je LTE Direct (ProSe) pro veřejnou bezpečnost a 5G NR sidelink, které zahrnují řízené formy komunikace mezi zařízeními.

## Klíčové vlastnosti

- Vyhrazený (dedikovaný) kanál pro uživatelská data v ODMA více-skokových přenosech
- Operuje v TDD režimu v rámci spektra UMTS
- Podporuje jak spojově orientované, tak nespojové služby
- Mapován na fyzické kanály ODMA TDD rozhraní
- Využívá ODMA-specifické protokoly RLC a MAC pro více-skokový provoz
- Umožňuje dynamické, příležitostně řízené navazování tras mezi UE

## Související pojmy

- [ODMA – Opportunity Driven Multiple Access](/mobilnisite/slovnik/odma/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN

---

📖 **Anglický originál a plná specifikace:** [ODTCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/odtch/)
