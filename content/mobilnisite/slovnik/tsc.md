---
slug: "tsc"
url: "/mobilnisite/slovnik/tsc/"
type: "slovnik"
title: "TSC – Time Sensitive Communications"
date: 2026-01-01
abbr: "TSC"
fullName: "Time Sensitive Communications"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tsc/"
summary: "Time Sensitive Communications (TSC) je soubor schopností 3GPP navržený pro podporu aplikací s přísnými požadavky na latenci, spolehlivost a časovou synchronizaci. Je základním kamenem pro průmyslovou"
---

TSC je soubor schopností 3GPP, které podporují aplikace s přísnými požadavky na latenci, spolehlivost a časovou synchronizaci tím, že zajišťují deterministické doručování paketů v rámci ohraničených koncových zpoždění.

## Popis

Time Sensitive Communications (TSC) označuje komplexní rámec v rámci standardů 3GPP, který umožňuje deterministické doručování dat přes sítě 3GPP. Determinismus znamená garantovat, že datové pakety jsou doručeny v rámci striktně ohraničené koncové latence (často ultranízké, např. pod 1 ms až desítky ms) s extrémně vysokou spolehlivostí (např. 99,9999 %) a přesnou časovou synchronizací mezi zařízeními (např. s přesností ±1 µs). Jedná se o zásadní odklon od tradičních mobilních komunikací typu best-effort.

Architektura TSC prostupuje více síťovými doménami. V 5G Core Network (5GC) využívá funkce jako podpora služby Ultra-Reliable Low Latency Communication ([URLLC](/mobilnisite/slovnik/urllc/)), síťovou expozici pro deterministickou komunikaci a model 5G QoS se specifickými QoS toky pro TSC provoz. Mezi klíčové architektonické komponenty patří Time Synchronization Function (TSF) definovaná v TS 23.501, která poskytuje časové informace pro RAN a UE, a podpora pro integraci time-sensitive networking ([TSN](/mobilnisite/slovnik/tsn/)). 5G systém může fungovat jako TSN bridge a účastnit se TSN sítí pro průmyslové [LAN](/mobilnisite/slovnik/lan/).

Na úrovni Radio Access Network (RAN) je TSC umožněno vylepšeními pro URLLC, jako je grant-free uplink transmission, mini-slot scheduling, redundantní přenosy (prostřednictvím duplikace paketů přes více cest) a pokročilé kódování kanálu. RAN používá specifické algoritmy plánování pro zvýšení priority TSC paketů a zajištění, že splní své termíny doručení. Na koncové úrovni systém využívá TSC Assistance Information ([TSCAI](/mobilnisite/slovnik/tscai/)) poskytovanou aplikační funkcí síti, která ji informuje o časech příchodu a termínech pro pakety, což umožňuje proaktivní rezervaci prostředků a plánování.

Jak to funguje, zahrnuje úzkou koordinaci mezi aplikací, core sítí a RAN. Aplikace (např. řídicí jednotka robotu) zaregistruje TSC relaci se specifickými požadavky. Síť zřídí vyhrazené QoS toky se garantovanou přenosovou rychlostí a rozpočtem zpoždění paketů. Aplikace následně poskytne TSCAI, signalizující očekávaný vzor kritických paketů. Plánovač RAN tyto informace použije k alokaci prostředků přesně včas pro příchozí pakety, čímž minimalizuje zpoždění ve frontách. Současně funkce časové synchronizace sítě distribuuje společný časový referenční signál, což umožňuje všem zařízením v systému pracovat koordinovaně, což je zásadní pro synchronizované akce v automatizaci.

## K čemu slouží

TSC bylo vytvořeno proto, aby umožnilo sítím 3GPP, primárně 5G, sloužit jako komunikační páteř pro vertikální odvětví, jako je tovární automatizace, distribuce elektřiny a doprava. Tato odvětví dlouho spoléhala na drátové sběrnice nebo průmyslové ethernetové systémy (např. PROFINET, EtherCAT), které nabízejí deterministickou latenci a těsnou synchronizaci. Omezením těchto drátových systémů je jejich nepružnost a vysoká cena nasazení/překonfigurování.

Základní problém, který TSC řeší, je inherentní nedeterminismus v paketových mobilních sítích, kde proměnlivá zpoždění ve frontách, souběžný přístup ke sdíleným prostředkům a fluktuace rádiového kanálu činí předvídatelné časování nemožným se standardními mechanismy. Předchozí generace mobilních sítí (4G a starší) byly navrženy pro provoz orientovaný na člověka (web, video), který je tolerantní k variacím zpoždění (jitru). To je činilo nevhodnými pro systémy s uzavřenou smyčkou řízení, kde opožděný senzorový údaj nebo příkaz pro aktuátor může způsobit selhání systému nebo bezpečnostní rizika.

Motivace pro standardizaci TSC přišla od silné poptávky průmyslu po bezdrátové flexibilitě v automatizaci. Vizí je "bezdrátová továrna" a "kritický IoT". 3GPP, počínaje Release 15 (5G fáze 1) a významně rozšiřující v Release 16 (5G fáze 2 pro [URLLC](/mobilnisite/slovnik/urllc/) a integraci [TSN](/mobilnisite/slovnik/tsn/)), vyvinulo schopnosti TSC, aby tuto mezeru překlenulo. Umožňuje mobilním sítím nejen připojovat zařízení, ale stát se integrální součástí časově kritických řídicích smyček, což otevírá nové případy užití, jako jsou mobilní robotika, rozšířená realita pro vzdálenou údržbu a ochrana chytrých sítí.

## Klíčové vlastnosti

- Podpora ohraničené ultranízké koncové latence (např. pod 1 ms až 10 ms) a ultra vysoké spolehlivosti (až 99,9999 %)
- Přesná distribuce časové synchronizace v síti (např. prostřednictvím 5G systému jako TSN Grandmaster nebo klienta)
- Integrace se standardy IEEE Time-Sensitive Networking (TSN) pro bezproblémovou konvergenci drátových a bezdrátových sítí
- Rozhraní pro expozici aplikace za účelem poskytnutí Time Sensitive Communication Assistance Information (TSCAI) síti
- Vyhrazené QoS mechanismy a QoS toky pro deterministický provoz se garantovanou alokací prostředků
- Vylepšení RAN včetně grant-free uplink, plánování mini-slotů a redundantních přenosových cest (PDCP duplikace)

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [TSCAI – Time Sensitive Communication Assistance Information](/mobilnisite/slovnik/tscai/)
- [TSN – AF Time Sensitive Networking Application Function](/mobilnisite/slovnik/tsn/)

## Definující specifikace

- **TR 21.904** (Rel-4) — 3GPP UE Baseline Capability Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.519** (Rel-17) — TSN AF to DS-TT/NW-TT Protocol Aspects
- **TS 24.535** (Rel-19) — TS 24535: (g)PTP Message Delivery Protocol
- **TS 24.539** (Rel-19) — NW-TT Protocol Aspects
- **TR 28.839** (Rel-18) — Technical Report
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TR 28.865** (Rel-18) — Technical Report on Deterministic Communication Service Assurance
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [TSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsc/)
