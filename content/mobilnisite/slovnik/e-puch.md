---
slug: "e-puch"
url: "/mobilnisite/slovnik/e-puch/"
type: "slovnik"
title: "E-PUCH – Enhanced Uplink Physical Channel"
date: 2025-01-01
abbr: "E-PUCH"
fullName: "Enhanced Uplink Physical Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-puch/"
summary: "Vyhrazený fyzický kanál pro uplink v režimech TDD s 3,84 Mcps a 7,68 Mcps standardu UMTS (TD-SCDMA). Přenáší uživatelská data a řídicí informace pro funkci Vylepšeného uplinku (HSUPA), což výrazně zvy"
---

E-PUCH je vylepšený fyzický kanál pro uplink v TD-SCDMA (UMTS TDD), který přenáší uživatelská data a řídicí informace za účelem umožnění funkce HSUPA pro zvýšení přenosových rychlostí v uplinku a snížení latence.

## Popis

Vylepšený fyzický kanál pro uplink (E-PUCH) je základní kanál definovaný ve standardu 3GPP TD-SCDMA (Time Division-Synchronous Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)) pro jeho režimy TDD s 3,84 Mcps a 7,68 Mcps. Je to primární fyzický kanál používaný k implementaci Vylepšeného uplinku, známého také jako High Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)) pro TDD. E-PUCH přenáší vyhrazený transportní kanál pro uplink ([E-DCH](/mobilnisite/slovnik/e-dch/)), který přenáší pakety uživatelských dat. Jeho provoz je charakterizován dynamickým plánováním a rychlou zpětnou vazbou na fyzické vrstvě. Struktura kanálu je založena na časových slotech a kanalizačních kódech. Klíčovou vlastností je podpora vícekódového přenosu, kdy jednomu uživatelskému zařízení (UE) mohou být v rámci stejného časového slotu přiděleny vícekanalizační kódy pro dosažení vyšších přenosových rychlostí. Plánovač Node B sítě dynamicky přiděluje tyto prostředky (časové sloty, kódy a maximální povolený výkon) uživatelským zařízením na základě poptávky po přenosech v uplinku a zatížení systému, přičemž povolení jsou signalizována prostřednictvím downlink kanálů [E-AGCH](/mobilnisite/slovnik/e-agch/) (Absolute Grant Channel) a [E-RGCH](/mobilnisite/slovnik/e-rgch/) (Relative Grant Channel). Uživatelské zařízení vysílá svá data na E-PUCH spolu s řídicími informacemi přenášenými v pásmu, jako je Happy Bit (udávající, zda UE požaduje více prostředků) a Retransmission Sequence Number (RSN). Procesy hybridního [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)) běží paralelně, což umožňuje rychlé retransmise řízené přímo Node B, což ve srovnání s retransmisemi řízenými RNC ve starších verzích bez vylepšeného uplinku drasticky snižuje latenci v uplinku. E-PUCH funguje ve spojení s kanálem [E-UCCH](/mobilnisite/slovnik/e-ucch/) (Uplink Control Channel) pro signalizaci a s kanálem E-RUCCH (Random Access Uplink Control Channel) pro počáteční žádosti o prostředky.

## K čemu slouží

E-PUCH byl vytvořen, aby řešil úzké hrdlo v uplinku v raných sítích 3G UMTS TDD, kde byly přenosové rychlosti v uplinku nízké a latence vysoká kvůli centralizovanému plánování a řízení retransmisí v radiovém síťovém řadiči (RNC). Toto omezení bránilo symetrickým vysokorychlostním datovým aplikacím, jako je videokonferencing, nahrávání velkých souborů a interaktivní služby v reálném čase. Funkce Vylepšeného uplinku, pro kterou je E-PUCH fyzickou vrstvou, zavedla plánování a HARQ řízené Node B (základnovou stanicí). To přesunulo kritická rozhodnutí o rychlém plánování a retransmisích blíže k rozhraní vzduchu, což umožnilo rychlejší adaptaci na podmínky kanálu a potřeby provozu. Motivací bylo poskytnout TDD UMTS srovnatelný výkon v uplinku se standardem FDD HSUPA, což výrazně zvýšilo špičkové přenosové rychlosti (teoreticky nad 2 Mbps), zvýšilo kapacitu uplinku a snížilo dobu odezvy, čímž se zlepšil uživatelský zážitek u aplikací citlivých na zpoždění s vysokou zátěží v uplinku.

## Klíčové vlastnosti

- Podporuje dynamické plánování prostředků pro uplink řízené Node B
- Umožňuje vícekódový přenos v rámci časového slotu pro vysoké přenosové rychlosti
- Integruje se s rychlými procesy hybridního ARQ (HARQ) na fyzické vrstvě
- Přenáší jak uživatelská data, tak řídicí informace v pásmu (např. Happy Bit)
- Funguje v obou variantách TDD s čipovou rychlostí 3,84 Mcps a 7,68 Mcps
- Používá přidělování prostředků v časových slotech a kódové doméně

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)

## Definující specifikace

- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.874** (Rel-11) — HSPA Feedback & Signalling Efficiency for LCR TDD

---

📖 **Anglický originál a plná specifikace:** [E-PUCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-puch/)
