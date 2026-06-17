---
slug: "dcn"
url: "/mobilnisite/slovnik/dcn/"
type: "slovnik"
title: "DCN – Data Communications Network"
date: 2025-01-01
abbr: "DCN"
fullName: "Data Communications Network"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dcn/"
summary: "DCN je vyhrazená, zabezpečená síť založená na protokolu IP používaná pro přenos provozu správy, řízení a signalizace mezi síťovými prvky a systémy řízení. Je klíčová pro provoz, správu a údržbu sítě ("
---

DCN je vyhrazená, zabezpečená síť založená na protokolu IP pro přenos provozu správy, řízení a signalizace mezi síťovými prvky a systémy řízení za účelem podpory provozu, správy a údržby sítě.

## Popis

Datová komunikační síť (Data Communications Network – DCN) je základní architektonickou součástí sítí 3GPP, která poskytuje podpůrnou přenosovou infrastrukturu pro veškerý provoz správy, provozu a údržby (OAM). Jedná se o logicky a často i fyzicky oddělenou IP síť navrženou pro přenos komunikace řídicí roviny, včetně konfiguračních příkazů, měření výkonu, alarmů poruch a aktualizací softwaru, mezi síťovými prvky (NEs), jako jsou základnové stanice a uzly jádra sítě, a systémy podpory provozu ([OSS](/mobilnisite/slovnik/oss/)), které je spravují. Toto oddělení od uživatelské roviny (která přenáší data účastníků) a řídicí roviny (která zpracovává signalizaci, jako je navázání hovoru) je základním principem, jenž zajišťuje, že provoz správy není ovlivněn zahlcením uživatelského provozu a že síť zůstává spravovatelná i při vysokém zatížení nebo částečných poruchách.

Architektonicky je DCN strukturována hierarchicky, často v souladu s operačními doménami sítě. Typicky se skládá z páteřní části DCN spojující hlavní síťová místa (jako centra provozu sítě nebo regionální uzly) a přístupových segmentů DCN, které připojují jednotlivé síťové prvky k této páteři. Klíčovými komponentami v rámci DCN jsou vyhrazené směrovače, přepínače a firewally, které implementují potřebné směrování, bezpečnostní politiky a kvalitu služeb (QoS). Síťové prvky se k DCN připojují prostřednictvím specifických rozhraní pro správu, jako je rozhraní Itf-N mezi správcem sítě ([NM](/mobilnisite/slovnik/nm/)) a správci prvků (EMs), nebo rozhraní směrem k vyšší vrstvě (northbound) od EMs k systémům OSS. Protokoly jako SNMP (Simple Network Management Protocol), NETCONF/YANG a [CORBA](/mobilnisite/slovnik/corba/) (ve starších vydáních) jsou přenášeny přes IP v rámci DCN, aby umožňovaly funkce správy.

Provoz DCN se řídí přísnými požadavky na spolehlivost, bezpečnost a výkon. Pro odolnost a redundanci využívá protokoly IP směrování (např. OSPF, BGP). Bezpečnost je prvořadá a je implementována prostřednictvím technik jako VPN (např. [IPsec](/mobilnisite/slovnik/ipsec/)), seznamy řízení přístupu (ACLs) a fyzická izolace, aby se zabránilo neoprávněnému přístupu k řídicí rovině. Mechanismy QoS upřednostňují kritický OAM provoz, jako jsou alarmy správy poruch, před méně časově citlivým provozem, jako je sběr logů. Role DCN se rozprostírá přes celý životní cyklus sítě a umožňuje dálkové zřizování, monitorování výkonu v reálném čase, centralizovanou správu poruch a automatizované zajištění služeb, což je nezbytné pro efektivní a nákladově efektivní provoz sítě.

## K čemu slouží

DCN byla vytvořena, aby řešila kritickou potřebu robustní, vyhrazené a standardizované přenosové infrastruktury pro správu v telekomunikačních sítích. Před jejím formalizováním v 3GPP byl provoz správy často přenášen přes sdílené sítě nebo prostřednictvím přímých point-to-point spojů, což představovalo významná rizika. Sdílený přenos mohl vést k zpoždění nebo ztrátě provozu správy během špiček uživatelského provozu, což omezovalo schopnost operátora včas monitorovat a napravovat problémy sítě. Přímé spoje nebyly škálovatelné pro velké, distribuované sítě jako 3G a novější.

Hlavním problémem, který DCN řeší, je zajištění garantovaného a bezpečného doručování OAM provozu, jenž je životodárnou mízou provozu sítě. Poskytnutím izolované sítě zaručuje, že se operátoři mohou vždy dostat k síťovým prvkům za účelem konfigurace, monitorování výkonu a řešení problémů, nezávisle na zatížení služeb směrovaných k uživateli. Tato izolace je klíčová pro udržení dostupnosti služeb a pro provádění postupů obnovy při anomáliích sítě nebo útocích. Její vznik byl motivován rostoucí složitostí, rozsahem a požadavky na automatizaci sítí 3GPP, kde se ruční správa na místě stala nepraktickou.

Historicky se tento koncept vyvinul z dřívějších telekomunikačních sítí pro správu, ale byl standardizován v 3GPP Release 5 spolu se zavedením IP multimediální podsystému (IMS) a silnějším tlakem na plně IP sítě. Tato standardizace byla nezbytná pro zajištění interoperability mezi síťovými prvky a systémy správy od různých výrobců, což operátorům umožnilo budovat jednotné, efektivní rámce OAM. DCN přímo řeší omezení ad-hoc spojení pro správu tím, že poskytuje škálovatelný, bezpečný a spolehlivý základ pro všechny následující pokroky v oblasti správy sítě a automatizace, včetně správy samoorganizujících se sítí (SON) a správy síťových řezů.

## Klíčové vlastnosti

- Logická a fyzická izolace od uživatelského a řídicího provozu
- Přenos založený na protokolu IP podporující standardní protokoly pro správu (SNMP, NETCONF)
- Hierarchická architektura s páteřními a přístupovými segmenty
- Vestavěné bezpečnostní mechanismy včetně VPN a řízení přístupu
- Kvalita služeb (QoS) pro upřednostnění kritických OAM zpráv
- Škálovatelný návrh pro podporu velkého počtu distribuovaných síťových prvků

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TR 23.785** (Rel-14) — Architecture enhancements for LTE V2X services
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.371** (Rel-19) — Security Management Concept & Requirements
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [DCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcn/)
