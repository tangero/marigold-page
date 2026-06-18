---
slug: "ff"
url: "/mobilnisite/slovnik/ff/"
type: "slovnik"
title: "FF – Factories of the Future"
date: 2025-01-01
abbr: "FF"
fullName: "Factories of the Future"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ff/"
summary: "Factories of the Future (FF) je studie a pracovní položka 3GPP zaměřená na definici komunikačních požadavků a umožňujících technologií pro pokročilou, propojenou průmyslovou automatizaci. Jejím cílem"
---

FF je pracovní položka 3GPP, která definuje komunikační požadavky a umožňující technologie pro přizpůsobení systémů 5G pro ultra-spolehlivé bezdrátové řízení s nízkou latencí v pokročilé průmyslové automatizaci.

## Popis

Factories of the Future (FF) je široká iniciativa v rámci 3GPP, která zkoumá a standardizuje využití buněčných technologií, primárně 5G New Radio (NR) a následných evolucí, pro umožnění chytré, flexibilní a vysoce automatizované průmyslové výroby. Nejde o jediný protokol nebo rozhraní, ale o soubor případů užití, požadavků a potenciálních vylepšení architektury systému 3GPP. Práce je dokumentována v technických zprávách (TR), jako jsou 22.804 (studie o komunikaci pro automatizaci ve vertikálních doménách), 23.745 (vylepšení architektury založené na službách pro vertikály) a 38.810 (studie o NR pro průmyslový internet věcí).

Architektonické aspekty FF zahrnují integraci sítí 5G do prostředí průmyslové operační technologie ([OT](/mobilnisite/slovnik/ot/)). To zahrnuje podporu integrace s časově citlivými sítěmi ([TSN](/mobilnisite/slovnik/tsn/)) pro zajištění synchronizace s drátovými ethernetovými sítěmi, vylepšené funkce pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) pro řídicí smyčky s kritickým nasazením a přesné lokalizační schopnosti pro sledování aktiv. Klíčovými komponentami jsou systém 5G (5GS) s možností nasazení v lokalitě nebo na hraně sítě (Non-Public Network - [NPN](/mobilnisite/slovnik/npn/)), uživatelské zařízení (UE) v podobě průmyslových zařízení (senzory, akční členy, [AGV](/mobilnisite/slovnik/agv/)) a propojení s průmyslovými automatizačními řídicími systémy a cloudovými platformami.

Princip fungování spočívá v poskytování deterministických komunikačních služeb. Síť 5G musí garantovat přísné výkonnostní limity pro latenci (pod 1 ms až 10 ms), spolehlivost (99,9999 % a více), dostupnost a synchronizaci (na úrovni mikrosekund). Toho je dosaženo prostřednictvím vylepšení, jako je přístup k uplinku bez udělení grantu (grant-free), plánování v mini-slotech, redundantní přenosové cesty a vylepšené rámce QoS. Síť zpřístupňuje své schopnosti vertikálním aplikacím prostřednictvím rozhraní založených na službách (např. [NEF](/mobilnisite/slovnik/nef/), [CAPIF](/mobilnisite/slovnik/capif/)) definovaných v normách jako 23.745, což umožňuje systémům pro správu továren vyžadovat a spravovat síťové řezy se specifickými charakteristikami FF. Konečnou rolí je nahradit nebo rozšířit tradiční drátové sběrnice (např. PROFINET, EtherCAT) bezdrátovou konektivitou, což umožňuje flexibilní rekonfiguraci výrobních linek, mobilní robotiku a rozšířenou realitu pro údržbu.

## K čemu slouží

Pracovní položka FF byla vytvořena, aby řešila specifické a náročné komunikační potřeby moderního průmyslu, známého jako Průmysl 4.0. Tradiční buněčné sítě byly navrženy pro mobilní širokopásmový přenos a komunikaci zaměřenou na člověka a postrádaly deterministický výkon, ultra-vysokou spolehlivost a integrační schopnosti vyžadované pro řízení strojů v reálném čase. Účelem FF je překlenout tuto mezeru vývojem standardů 3GPP tak, aby se staly životaschopnou, ba i nadřazenou alternativou k průmyslovým drátovým sítím pro určité aplikace.

Motivace vychází z potřeby průmyslu zvýšit flexibilitu, efektivitu a snížit náklady. Drátová připojení omezují mobilitu robotů a automatických vozíků ([AGV](/mobilnisite/slovnik/agv/)) a činí rekonfiguraci výrobních linek pomalou a nákladnou. Bezdrátová konektivita slibuje schopnosti typu 'zapoj a vyrábě'. Iniciativa FF od 3GPP to řeší poskytnutím standardizovaného, globálního a škálovatelného bezdrátového řešení. Odstraňuje omezení předchozích bezdrátových technologií (jako je Wi-Fi), které často selhávají v oblasti spolehlivosti, deterministické latence a plynulé mobility v hustých, kovových továrních prostředích. Definováním těchto požadavků a prosazením odpovídajících funkcí do specifikací 5G NR a core sítě umožňuje 3GPP jednotnou komunikační strukturu pro celou továrnu, od senzoru až po cloud.

## Klíčové vlastnosti

- Definice požadavků na ultra-spolehlivou komunikaci s nízkou latencí (URLLC) pro průmyslové řízení
- Podpora integrace s IEEE Time-Sensitive Networking (TSN)
- Vylepšení pro přesnou lokalizaci a synchronizaci průmyslových zařízení
- Architektonická podpora pro Non-Public Networks (NPN) a nasazení v lokalitě
- Rámce pro zpřístupnění služeb (např. 23.745) pro integraci vertikálních aplikací
- Studie nových případů užití, jako jsou mobilní roboti, řízení pohybu a rozšířená realita

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TS 32.153** (Rel-19) — IRP Technology-Specific Templates Specification
- **TS 32.820** (Rel-8) — Charging Architecture Study for Evolved 3GPP
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [FF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ff/)
