---
slug: "esm"
url: "/mobilnisite/slovnik/esm/"
type: "slovnik"
title: "ESM – Energy Savings Management"
date: 2025-01-01
abbr: "ESM"
fullName: "Energy Savings Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/esm/"
summary: "Energy Savings Management (ESM) je soubor funkcí a procedur správy sítě definovaných 3GPP pro monitorování, řízení a optimalizaci spotřeby energie prvků mobilní sítě, zejména základnových stanic. Jeho"
---

ESM je soubor funkcí správy sítě definovaných 3GPP pro monitorování, řízení a optimalizaci spotřeby energie v prvcích mobilní sítě s cílem snížit provozní náklady a uhlíkovou stopu při zachování kvality služeb.

## Popis

Energy Savings Management (ESM) je komplexní rámec v rámci specifikací 3GPP, který primárně spadá do domény provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)). Poskytuje standardizované mechanismy pro síťové operátory k implementaci funkcí pro úsporu energie napříč rádiovou přístupovou sítí (RAN) a potenciálně dalšími síťovými doménami. Základní filozofií ESM je dynamicky sladit využití síťových zdrojů s dopravním zatížením, čímž se snižuje spotřeba energie v obdobích nízkého zatížení bez výrazného dopadu na kvalitu služeb (QoS) vnímanou uživateli.

Architektonicky jsou funkce ESM implementovány ve vrstvách správy sítě ([NM](/mobilnisite/slovnik/nm/)) a správy prvků ([EM](/mobilnisite/slovnik/em/)), jak je definováno v architektuře správy 3GPP (TS 28.628, TS 32.522). Mezi klíčové entity patří funkce správy úspor energie (ESMF), která je zodpovědná za centralizované řízení a koordinaci úspor energie. Rámec ESM definuje regulační smyčku zahrnující fáze monitorování, analýzy, rozhodování a provedení. Shromažďuje výkonnostní měření ([PM](/mobilnisite/slovnik/pm/)) a konfigurační data týkající se energie ze síťových prvků, jako jsou gNB, ng-eNB a [eNB](/mobilnisite/slovnik/enb/). Na základě těchto dat a politik operátora může ESMF aktivovat, deaktivovat nebo upravovat různé akce pro úsporu energie ([ES](/mobilnisite/slovnik/es/)) na konkrétních síťových prvcích nebo skupinách prvků.

Tyto akce ES jsou technické mechanismy, které realizují úspory energie. Jsou podrobně popsány v RAN specifikacích (např. TS 36.927, TS 38.927). Mezi běžné akce patří: převedení nosných komponent do klidového stavu, kdy je většina [RF](/mobilnisite/slovnik/rf/) komponent vypnuta; vypnutí celých buněk nebo sektorů (Cell Switch Off); úprava sklonu antény nebo výkonu pro zmenšení pokrytí při nízkém zatížení; a implementace sofistikovaného vypínání na úrovni symbolů nebo časových slotů v časové doméně, kdy jsou části základnové stanice vypnuty během prázdných nebo málo aktivních časových slotů. Kritickým aspektem ESM je řízení kompromisů. Rámec zahrnuje koncepty jako stav úspory energie (ESS), který definuje úroveň aktivity úspor energie (např. 'neaktivní', 'aktivní s udrženou QoS', 'aktivní se sníženou QoS'), a vztahy kompenzačních sousedních buněk, které jsou předkonfigurovány pro zajištění pokrytí sousedními buňkami při vypnutí buňky. Procedury ESM zajišťují koordinaci těchto akcí, aby se předešlo mezerám v pokrytí nebo degradaci služeb.

## K čemu slouží

ESM bylo vytvořeno v reakci na rychle rostoucí spotřebu energie a provozní náklady mobilních sítí, poháněné zvyšujícím se datovým provozem a zahušťováním sítě. Před jeho standardizací byly funkce pro úsporu energie proprietárními řešeními dodavatelů, což komplikovalo správu více-dodavatelských sítí a omezovalo schopnost operátora implementovat ucelené, celosíťové energetické politiky. Nedostatek standardizace také bránil vývoji pokročilých, koordinovaných úsporných mechanismů, které vyžadují interoperabilitu mezi síťovými prvky od různých dodavatelů.

Primárním účelem ESM je poskytnout standardizovaný, na dodavateli nezávislý rámec, který operátorům umožňuje efektivně snižovat spotřebu energie ([PC](/mobilnisite/slovnik/pc/)) a uhlíkovou stopu (CF) jejich sítě, což jsou klíčové ukazatele výkonnosti (KPI) pro moderní udržitelné sítě. Řeší problém neefektivního statického provozu, kdy síťové prvky spotřebovávají energii blízkou špičkovému výkonu bez ohledu na skutečné zatížení provozem. Umožněním dynamické adaptace mění ESM spotřebu energie sítě z fixních nákladů na variabilní, které se škálují s poptávkou. Dále poskytuje nástroje pro správu k řízení nevyhnutelného kompromisu mezi úsporami energie a výkonem sítě (pokrytí, kapacita, QoS), což operátorům umožňuje implementovat úsporné strategie, které jsou v souladu s jejich konkrétními smlouvami o úrovni služeb a obchodními cíli. Jeho zavedení formalizovalo energetickou účinnost jako prvořadý požadavek v síťovém managementu, na stejné úrovni jako tradiční KPI, jako je propustnost a latence.

## Klíčové vlastnosti

- Standardizovaná rozhraní pro správu (Itf-N) pro řízení a monitorování úspor energie
- Definice stavů úspory energie (ESS) pro kvantifikaci úrovně úsporné aktivity
- Podpora širokého spektra akcí ES (vypnutí buňky, klidový stav nosné, vypnutí symbolu/slotu)
- Mechanismy pro řízení kompromisu mezi úsporami energie a QoS/pokrytím
- Koordinace pro zajištění kompenzace sousedními buňkami během akcí ES
- Integrace se správou výkonnosti (PM) a správou poruch (FM) pro řízení v uzavřené smyčce

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.305** (Rel-19) — Selective Disabling of 3GPP UE Capabilities
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service
- **TS 32.551** (Rel-19) — Energy Savings Management Concepts and Requirements
- **TS 32.826** (Rel-10) — Study on Energy Savings Management in LTE/SAE Networks
- **TS 32.834** (Rel-11) — Inter-RAT Energy Saving Management Study
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.509** (Rel-17) — EPC Special UE Conformance Testing Functions
- **TR 36.927** (Rel-19) — Network Energy Saving for E-UTRAN

---

📖 **Anglický originál a plná specifikace:** [ESM na 3GPP Explorer](https://3gpp-explorer.com/glossary/esm/)
