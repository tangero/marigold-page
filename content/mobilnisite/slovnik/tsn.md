---
slug: "tsn"
url: "/mobilnisite/slovnik/tsn/"
type: "slovnik"
title: "TSN – AF Time Sensitive Networking Application Function"
date: 2026-01-01
abbr: "TSN"
fullName: "AF Time Sensitive Networking Application Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tsn/"
summary: "Aplikační funkce (AF) v rámci 5G Core sítě, která slouží jako rozhraní mezi 5G systémy a externími sítěmi Time-Sensitive Networking (TSN). Překládá požadavky TSN do politik 5G sítě, což umožňuje, aby"
---

TSN je aplikační funkce (Application Function) v 5G Core, která rozhraní s externími systémy Time-Sensitive Networking a překládá jejich požadavky do politik 5G sítě, aby umožnila deterministické připojení s nízkou latencí pro průmyslovou automatizaci.

## Popis

Aplikační funkce TSN (TSN [AF](/mobilnisite/slovnik/af/)) je klíčová komponenta definovaná 3GPP pro integraci 5G systémů do ekosystémů [IEEE](/mobilnisite/slovnik/ieee/) 802.1 Time-Sensitive Networking (TSN), které jsou ústřední pro průmyslový Ethernet a deterministickou komunikaci. Nachází se v 5G Core síti jako specializovaná aplikační funkce a komunikuje s dalšími funkcemi jádra sítě, jako je Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)), prostřednictvím rozhraní založených na službách. Primární role TSN AF je reprezentovat TSN síť (nebo TSN systém) vůči 5G systému a fungovat jako brána pro konfiguraci a požadavky specifické pro TSN.

Z architektonického hlediska TSN AF komunikuje s TSN Network Controllerem (nebo Centralized Network Controller - [CNC](/mobilnisite/slovnik/cnc/)), což je entita v TSN doméně odpovědná za celkové plánování a správu zdrojů. TSN AF přijímá od CNC požadavky TSN, které zahrnují deterministické komunikační parametry, jako je periodicita, maximální latence, spolehlivost (míra chybovosti paketů) a přesnost časové synchronizace pro datové toky, které budou procházet 5G systémem. Z pohledu TSN sítě je 5G systém modelován jako virtuální TSN most (nebo sada mostů). TSN AF je zodpovědná za to, aby byly schopnosti a zdroje 5G systému viditelné pro TSN CNC, a za mapování požadavků TSN toků do parametrů a politik QoS specifických pro 5G.

Jak to funguje, zahrnuje vícekrokový proces. Nejprve během vystavení schopností TSN AF informuje TSN CNC o charakteristikách 5G systému, jako jsou podporované hranice latence, podpora časové synchronizace (prostřednictvím 5G systému jako časového slave nebo master) a dostupná šířka pásma. Když CNC vypočítá globální plán pro TSN provoz, zahrne do něj virtuální 5G most. CNC odešle tento plán, včetně seznamů řízení bran (gate control lists) pro porty 5G mostu, do TSN AF. TSN AF následně přeloží tyto TSN konstrukty do pravidel politik 5G. Komunikuje s PCF za účelem vytvoření nebo úpravy pravidel [PCC](/mobilnisite/slovnik/pcc/) (Policy and Charging Control), která vynucují požadované QoS – například přidělením vyhrazeného 5G QoS toku se zaručenou přenosovou rychlostí a rozpočtem zpoždění paketů pro konkrétní TSN stream. Může také komunikovat s [SMF](/mobilnisite/slovnik/smf/) (Session Management Function) a [UPF](/mobilnisite/slovnik/upf/) (User Plane Function) pro konfiguraci uživatelské roviny pro deterministické přeposílání.

Mezi klíčové komponenty, se kterými interaguje, patří TSN Translator v UE a/nebo v UPF, které zajišťují skutečnou adaptaci rámců Ethernet na 5G pakety a naopak, včetně časového značkování pro synchronizaci. Role TSN AF je čistě v řídicí rovině, spravuje konfiguraci. Umožňuje end-to-end deterministické připojení, kde může být 5G bezdrátový spoj bezproblémově integrován do kabelové TSN sítě, čímž podporuje kritické aplikace Průmyslu 4.0, jako je řízení pohybu, strojové vidění a systémy řízení se zpětnou vazbou, které vyžadují ultra-spolehlivou, nízkolatenční a časově synchronizovanou komunikaci.

## K čemu slouží

TSN AF byla vytvořena, aby propojila dva historicky oddělené světy: deterministické průmyslové sítě (TSN) a buněčné mobilní sítě (5G). Průmyslová automatizace dlouho spoléhala na kabelové sběrnice (fieldbus) a technologie průmyslového Ethernetu (jako PROFINET, EtherCAT), které poskytují pevné záruky latence, jitteru a synchronizace. Ty jsou nezbytné pro koordinaci strojů na výrobní lince. Bezdrátová řešení byla tradičně nevhodná kvůli nedostatku determinismu, spolehlivosti a přesného časování.

Nástup 5G s jeho schopnostmi URLLC (Ultra-Reliable Low-Latency Communication) sliboval tuto bariéru prolomit a umožnit flexibilní bezdrátové připojení pro pohyblivé části, jako jsou AGV (Automated Guided Vehicles) a robotické ramena. Samotné poskytnutí nízkolatenčního kanálu však nestačilo. Pro skutečnou integraci se musela 5G síť jevit jako standardní, řiditelná komponenta v rámci TSN ekosystému, který je řízen centrálním CNC. TSN AF tento problém řeší tím, že funguje jako zástupce 5G systému pro řídicí rovinu TSN.

Řeší klíčové omezení předchozích bezdrátových řešení – jejich neprůhlednost a nedostatek integrace do deterministického plánování. Bez TSN AF by TSN CNC nemohl vidět ani řídit 5G spoj, což by znemožnilo end-to-end deterministické plánování. TSN AF poskytuje nezbytnou překladovou vrstvu, která umožňuje CNC zacházet s 5G rádiovým spojem jako s dalším TSN mostem se známými charakteristikami. To motivovalo její vytvoření v 3GPP Release 16 jako součást podpory 5G systému pro vertikální odvětví, konkrétně automatizaci továren. Umožňuje konvergenci sítí OT (Operational Technology) a IT, což umožňuje, aby se 5G stalo životaschopnou náhradou kabelů v nejnáročnějších aplikacích průmyslového řízení, a tím umožňuje novou úroveň flexibility a rekonfigurovatelnosti v chytré výrobě.

## Klíčové vlastnosti

- Funguje jako proxy řídicí roviny mezi 5G Core a externím TSN Network Controllerem (CNC)
- Vystavuje schopnosti 5G systému (latence, synchronizace, zdroje) TSN doméně
- Překládá požadavky TSN toků (perioda, latence, spolehlivost) do parametrů QoS a pravidel PCC pro 5G
- Konfiguruje 5G systém tak, aby fungoval jako jeden nebo více virtuálních TSN mostů
- Podporuje protokoly časové synchronizace TSN (např. gPTP) přes 5G systém
- Umožňuje end-to-end deterministické plánování napříč kabelovými TSN a bezdrátovými 5G doménami

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.821** (Rel-16) — 5G LAN-type Services Requirements
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.519** (Rel-17) — TSN AF to DS-TT/NW-TT Protocol Aspects
- **TS 24.535** (Rel-19) — TS 24535: (g)PTP Message Delivery Protocol
- **TS 24.539** (Rel-19) — NW-TT Protocol Aspects
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [TSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsn/)
