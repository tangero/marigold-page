---
slug: "rlc"
url: "/mobilnisite/slovnik/rlc/"
type: "slovnik"
title: "RLC – Radio Link Control"
date: 2025-01-01
abbr: "RLC"
fullName: "Radio Link Control"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rlc/"
summary: "Radio Link Control (RLC) je protokol vrstvy 2 v rádiové přístupové síti, který zajišťuje spolehlivý přenos dat přes rozhraní vzdušného rozhraní. Funguje mezi vrstvami MAC a PDCP a poskytuje segmentaci"
---

RLC je protokol vrstvy 2, který zajišťuje spolehlivý přenos dat přes rozhraní vzdušného rozhraní tím, že poskytuje segmentaci, opravu chyb a doručování ve správném pořadí mezi vrstvami MAC a PDCP.

## Popis

Podvrstva Radio Link Control (RLC) je klíčovou součástí zásobníku protokolů vrstvy 2 v rádiových přístupových sítích 3GPP, včetně UMTS, LTE a NR. Umístěná mezi spodní vrstvou Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a horní vrstvou Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) je RLC zodpovědná za spolehlivý přenos dat přes rádiový spoj. Funguje ve třech režimech: Transparentní režim ([TM](/mobilnisite/slovnik/tm/)), Nepotvrzovaný režim ([UM](/mobilnisite/slovnik/um/)) a Potvrzovaný režim ([AM](/mobilnisite/slovnik/am/)), z nichž každý je přizpůsoben různým požadavkům služeb. V TM předává RLC data bez přidání hlaviček, používá se pro služby citlivé na zpoždění, jako je hlas. V UM poskytuje segmentaci a opětovné složení s číslováním sekvencí, ale bez retransmisí, což je vhodné pro streamování nebo vysílání. V AM přidává opravu chyb prostřednictvím automatického opakovaného dotazu ([ARQ](/mobilnisite/slovnik/arq/)), čímž zajišťuje spolehlivé doručení pro datové služby. RLC funguje tak, že přijímá servisní datové jednotky (SDUs) od PDCP, segmentuje je nebo spojuje do protokolových datových jednotek (PDUs) pro přenos přes MAC. Spravuje vyrovnávací paměti, zpracovává retransmise v AM a zajišťuje doručení ve správné sekvenci vyšším vrstvám. Mezi klíčové komponenty patří entita RLC, která udržuje stavové proměnné a časovače, a nosič RLC, který odpovídá logickému kanálu. RLC interaguje s MAC pro plánování a [HARQ](/mobilnisite/slovnik/harq/) a přizpůsobuje se rádiovým podmínkám pro optimalizaci propustnosti a latence. Jeho role je zásadní pro zmírnění chyb z fyzické vrstvy, podporu diferenciace QoS a umožnění efektivního využití rádiových zdrojů napříč vyvíjejícími se technologiemi 3GPP.

## K čemu slouží

Protokol RLC byl vytvořen, aby řešil inherentní nespolehlivost a proměnlivost bezdrátových rádiových spojů, které jsou náchylné k chybám, zpožděním a ztrátám paketů kvůli útlumu, rušení a mobilitě. V raných celulárních systémech byly jednoduché mechanismy přenosu dat nedostatečné pro podporu různorodých služeb, jako je hlas, video a přístup k internetu s různými požadavky na spolehlivost a latenci. RLC to řeší tím, že poskytuje flexibilní rámec založený na režimech, který zajišťuje integritu a pořadí dat a přizpůsobuje se požadavkům služeb. Historicky, před standardizací 3GPP, vedly proprietární řešení k problémům s interoperabilitou. RLC, zavedený v [R99](/mobilnisite/slovnik/r99/), stanovil jednotný přístup pro UMTS a vyvíjel se napříč releasy, aby zvládal zvýšené datové rychlosti a nové případy užití v LTE a NR. Řeší omezení protokolů nižších vrstev, jako je PHY a MAC, kterým chybí mechanismy spolehlivosti end-to-end, tím, že nabízí schopnosti ARQ a segmentace. Motivací bylo umožnit efektivní a spolehlivou komunikaci přes rozhraní vzdušného rozhraní, podpořit růst od přepojování okruhů pro hlas k paketově přepínanému multimédiu a později k ultra-spolehlivé komunikaci s nízkou latencí v 5G. RLC zůstává nezbytný pro udržení kvality spoje a umožnění pokročilých funkcí, jako je agregace nosných a duální konektivita.

## Klíčové vlastnosti

- Tři provozní režimy: Transparentní, Nepotvrzovaný a Potvrzovaný
- Segmentace a opětovné složení datových jednotek pro efektivní přenos
- Oprava chyb prostřednictvím ARQ v Potvrzovaném režimu
- Doručování ve správném pořadí a detekce duplicit
- Správa vyrovnávacích pamětí pro řízení toku a retransmise
- Podpora různých požadavků QoS napříč službami

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- … a dalších 43 specifikací

---

📖 **Anglický originál a plná specifikace:** [RLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlc/)
