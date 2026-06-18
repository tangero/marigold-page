---
slug: "es"
url: "/mobilnisite/slovnik/es/"
type: "slovnik"
title: "ES – Enterprise Systems"
date: 2026-01-01
abbr: "ES"
fullName: "Enterprise Systems"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/es/"
summary: "Označuje soubor síťových funkcí, architektur a služebních prvků navržených k poskytování přizpůsobených, zabezpečených a izolovaných komunikačních služeb pro podnikové zákazníky ve veřejných mobilních"
---

ES (Enterprise Systems) je soubor síťových funkcí, architektur a služebních prvků navržených k poskytování přizpůsobených, zabezpečených a izolovaných komunikačních služeb pro podnikové zákazníky ve veřejných mobilních sítích.

## Popis

V rámci 3GPP představují Enterprise Systems (ES) standardizované architektury, schopnosti a rozhraní, které umožňují mobilním síťovým operátorům ([MNO](/mobilnisite/slovnik/mno/)) nabízet přizpůsobené služby podnikovým zákazníkům. Nejde o jeden síťový prvek, ale o koncepční rámec, který integruje různé systémy 3GPP – včetně základní sítě (Core Network), řízení a orchestrace (Management and Orchestration) a vystavení služebních schopností (Service Capability Exposure) – za účelem vytvoření virtualizovaných, oddělených nebo vyhrazených síťových prostředků pro podnik. Architektura je postavena na klíčových pilířích: síťové segmentaci (network slicing), která poskytuje logické, koncově izolované sítě; neveřejných sítích (Non-Public Networks, [NPN](/mobilnisite/slovnik/npn/)), které lze nasadit jako samostatné privátní sítě nebo integrovat s veřejnými sítěmi; a rozšířených funkcích pro vystavení (exposure functions), které podnikům umožňují programově řídit aspekty své služby.

Fungování ES zahrnuje několik technických komponent. Základem je architektura založená na službách (Service-Based Architecture, [SBA](/mobilnisite/slovnik/sba/)) 5G základní sítě (5G Core), kde funkce pro vystavení síťových schopností (Network Exposure Function, [NEF](/mobilnisite/slovnik/nef/)) zpřístupňuje síťové schopnosti a události autorizovaným podnikovým aplikacím prostřednictvím [API](/mobilnisite/slovnik/api/). Funkce pro výběr síťového segmentu (Network Slice Selection Function, [NSSF](/mobilnisite/slovnik/nssf/)) pomáhá vybrat vhodnou instanci síťového segmentu pro podnikové koncové zařízení (UE). Pro NPN lze síť nasadit pomocí modelů samostatné NPN (Stand-alone NPN, [SNPN](/mobilnisite/slovnik/snpn/)) nebo NPN integrované s veřejnou sítí (Public Network Integrated NPN, [PNI-NPN](/mobilnisite/slovnik/pni-npn/)). Řízení a orchestrace, zajišťované systémy jako funkce pro správu síťových segmentů (Network Slice Management Function, NSMF) a funkce pro správu komunikačních služeb (Communication Service Management Function, CSMF), umožňují automatizovanou správu životního cyklu (vytvoření, změna, ukončení) těchto podnikových služeb a zajišťují plnění konkrétních smluv o úrovni služeb (SLA).

Bezpečnost a izolace jsou prvořadé. Implementace ES využívají robustní autentizační mechanismy (např. 5G AKA, metody založené na EAP), často s přihlašovacími údaji spravovanými samotným podnikem. Funkce uživatelské roviny (User Plane Function, UPF) může být nasazena na hraně podniku (výběr UPF pro místní ukončení provozu), aby citlivý datový provoz zůstal v areálu podniku, což snižuje latenci a zvyšuje soukromí. Úlohou ES je transformovat veřejnou mobilní síť z obecného spojovacího kanálu na programovatelnou platformu, která může hostovat širokou škálu aplikací specifických pro podniky, jako je ultra-spolehlivá komunikace s nízkou latencí (URLLC) pro tovární automatizaci, rozsáhlé sítě IoT senzorů nebo rozšířené mobilní širokopásmové připojení se zaručenou šířkou pásma.

## K čemu slouží

Koncept Enterprise Systems vznikl v důsledku rostoucí poptávky vertikálních odvětví (výroba, logistika, zdravotnictví atd.) po privátních bezdrátových sítích na úrovni mobilních sítí, které nabízejí více než jen základní konektivitu. Tradiční veřejné mobilní sítě byly navrženy pro spotřebitelské služby s jednotným přístupem (one-size-fits-all) a postrádaly přizpůsobení, garantovaný výkon, zabezpečení a kontrolu, které podniky vyžadují pro kritické operace. Raná řešení, jako VPN přes veřejné sítě nebo vyhrazená fyzická infrastruktura, byla buď nedostatečná z hlediska výkonu/bezpečnosti, nebo neúměrně drahá a nepružná.

3GPP, počínaje výrazně vydáním 15 pro 5G, systematicky zavádělo schopnosti ES, aby uspokojilo tuto tržní potřebu a otevřelo operátorům nové zdroje příjmů. Motivací bylo využít inherentní flexibilitu 5G – zejména softwarizaci sítě (NFV/SDN), síťovou segmentaci (network slicing) a edge computing – k vytvoření víceklientské platformy schopné hostit nesčetné přizpůsobené podnikové služby na sdílené fyzické infrastruktuře. Tím se řeší omezení předchozích přístupů poskytováním vnitřní izolace (prostřednictvím segmentace), integrované bezpečnosti (od rádiového rozhraní výše) a programovatelnosti (prostřednictvím API).

Standardizací ES umožňuje 3GPP globální ekosystém interoperabilních řešení, čímž předchází závislosti na jednom dodavateli a podporuje inovace. Řeší problém poskytování průmyslově kvalitního, deterministického připojení, které je škálovatelné, nákladově efektivní a bezproblémově integrované s existujícími podnikovými systémy IT a operačními technologiemi (OT). To je základním kamenem slibu 5G jít nad rámec rozšířeného mobilního širokopásmového připojení a stát se klíčovým hybatelem digitální transformace průmyslu.

## Klíčové vlastnosti

- Podpora neveřejných sítí (Non-Public Networks, NPN) v modelech samostatných (Stand-alone) a integrovaných s veřejnou sítí (Public Network Integrated)
- Využití síťové segmentace (network slicing) k poskytnutí izolovaných, logických sítí se zaručenými SLA
- Vystavení síťových schopností a událostí podnikům prostřednictvím NEF a API
- Podpora místního ukončení provozu (local break-out) a edge computingu s funkcemi uživatelské roviny na místě podniku
- Rozšířené modely autentizace a zabezpečení podporující správu přihlašovacích údajů podnikem
- Správa životního cyklu a orchestrace podnikových služeb prostřednictvím standardizovaných rozhraní pro správu

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 28.561** (Rel-20) — Management and Orchestration; Network Digital Twin
- **TR 28.915** (Rel-19) — Management and orchestration; Study on Network Digital Twin
- **TS 29.585** (Rel-19) — TSN Interworking Protocol for 5G System
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.551** (Rel-19) — Energy Savings Management Concepts and Requirements
- **TS 32.826** (Rel-10) — Study on Energy Savings Management in LTE/SAE Networks
- **TS 32.834** (Rel-11) — Inter-RAT Energy Saving Management Study
- **TS 32.835** (Rel-12) — HetNet Management Information Selection
- **TS 36.887** (Rel-12) — Energy Saving Enhancement for E-UTRAN Study
- **TR 36.927** (Rel-19) — Network Energy Saving for E-UTRAN

---

📖 **Anglický originál a plná specifikace:** [ES na 3GPP Explorer](https://3gpp-explorer.com/glossary/es/)
