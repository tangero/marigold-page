---
slug: "rds"
url: "/mobilnisite/slovnik/rds/"
type: "slovnik"
title: "RDS – Reliable Data Service"
date: 2025-01-01
abbr: "RDS"
fullName: "Reliable Data Service"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rds/"
summary: "Služba 3GPP, která poskytuje zvýšenou spolehlivost doručování dat, zejména pro kritické aplikace IoT a průmyslové aplikace. Zajišťuje, že datové pakety jsou doručeny s vysokou pravděpodobností i v nár"
---

RDS je služba 3GPP, která poskytuje zvýšenou spolehlivost doručování dat, zejména pro kritické aplikace IoT, prostřednictvím mechanismů jako jsou retransmise, aby zajistila vysokou pravděpodobnost doručení i v náročných rádiových podmínkách.

## Popis

Reliable Data Service (RDS, služba spolehlivého přenosu dat) je schopnost na úrovni služby standardizovaná organizací 3GPP, která splňuje přísné požadavky na spolehlivost přenosu dat, zejména pro kritické a průmyslové komunikace v rámci internetu věcí (IoT). Funguje nad transportní vrstvou a poskytuje záruku, že aplikační data jsou úspěšně doručena ze zdroje do cílového místa určení. Služba je navržena tak, aby fungovala nad různými podkladovými transportními protokoly, včetně mechanismů pro přenos dat založených na IP i pro přenos ne-IP dat ([NIDD](/mobilnisite/slovnik/nidd/)), což ji činí přizpůsobitelnou různým možnostem zařízení IoT a síťovým architekturám.

Architektonicky je RDS implementována v rámci 3GPP Core Network, konkrétně se zapojením Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)) pro Non-IP Data Delivery (NIDD) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) pro přenos založený na IP. Služba zavádí koncept Reliable Data Server (RDS), který funguje jako koncový bod pro spolehlivou službu. Pro NIDD rozhraní SCEF komunikuje se serverem RDS, zatímco pro IP může UPF aplikovat specifické zpracování paketů. Služba využívá mechanismy jako end-to-end potvrzení, retransmise a případně duplikaci paketů přes více cest, aby dosáhla svých cílů spolehlivosti, které lze konfigurovat na základě jednotlivých požadavků služby.

Služba funguje tak, že mezi žadatelem (např. Application Server ([AS](/mobilnisite/slovnik/as/)) nebo User Equipment (UE)) a serverem RDS vytvoří kontext spolehlivé datové relace. Žadatel specifikuje požadovanou úroveň spolehlivosti a další parametry služby. Během přenosu dat mechanismy RDS sledují úspěšnost doručení. Pokud není potvrzení přijato ve stanoveném čase, jsou spuštěny retransmise. Služba také spravuje stav relace, včetně ukládání dat do vyrovnávací paměti, pokud není UE dosažitelné, a poskytuje žadateli hlášení o doručení. Její role je klíčová pro aplikace, kde je ztráta dat nepřijatelná, jako je dálkové ovládání průmyslových strojů, příkazy pro ochranu chytrých sítí nebo životně důležitá zdravotní telemetrie, a zajišťuje, že systém 5G dokáže podporovat závazky služby Ultra-Reliable Low-Latency Communication ([URLLC](/mobilnisite/slovnik/urllc/)).

## K čemu slouží

RDS byla vytvořena, aby zaplnila mezeru v oblasti standardizovaného, síťově asistovaného spolehlivého doručování dat pro kritickou komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) a služby IoT. Před jejím zavedením musely aplikace vyžadující vysokou spolehlivost implementovat složité proprietární end-to-end protokoly nad službou best-effort IP poskytovanou mobilními sítěmi. To bylo neefektivní, zvyšovalo složitost zařízení a spotřebu energie a neumožňovalo využít síťovou inteligenci pro optimalizaci.

Motivace vycházela z tlaku průmyslu směrem k průmyslovému IoT (IIoT) a automatizaci, kde musí být řídicí příkazy a senzorová data doručena s téměř stoprocentní jistotou. Práce 3GPP na Cellular IoT (CIoT) a kritických komunikacích identifikovala spolehlivost jako klíčový požadavek služby, který by síť sama měla nativně podporovat. RDS poskytuje standardizované, na síti nezávislé rozhraní, které aplikacím umožňuje požadovat a získávat garantované doručení dat, čímž zjednodušuje vývoj aplikací a umožňuje konzistentní kvalitu služeb napříč různými síťovými operátory a typy zařízení. Je klíčovým prvkem pro ambice 5G v oblasti vertikálních průmyslů, neboť poskytuje základní službu pro případy užití [URLLC](/mobilnisite/slovnik/urllc/).

## Klíčové vlastnosti

- Konfigurovatelné úrovně end-to-end spolehlivosti pro přenos dat
- Podpora pro transport založený na IP i Non-IP Data Delivery (NIDD)
- Mechanismy pro potvrzení doručení a retransmise
- Správa relací s udržováním stavu pro nedosažitelná zařízení
- Hlášení o doručení a oznámení o stavu pro žadatele služby
- Integrace s funkcemi Core Network, jako jsou SCEF a UPF

## Související pojmy

- [SCEF – Service Capability Exposure Function](/mobilnisite/slovnik/scef/)
- [NIDD – Non-IP Data Delivery](/mobilnisite/slovnik/nidd/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 24.250** (Rel-19) — Reliable Data Service Protocol Specification
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.541** (Rel-19) — NEF Service-Based Interfaces for NIDD & SMS

---

📖 **Anglický originál a plná specifikace:** [RDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rds/)
