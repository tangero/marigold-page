---
slug: "da"
url: "/mobilnisite/slovnik/da/"
type: "slovnik"
title: "DA – Distribution Automation"
date: 2026-01-01
abbr: "DA"
fullName: "Distribution Automation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/da/"
summary: "Distribuční automatizace (DA) je služba 3GPP umožňující automatizované monitorování, řízení a ochranu distribučních sítí elektrické energie pomocí buňkové komunikace. Podporuje kritické aplikace chytr"
---

DA je služba 3GPP, která využívá buňkovou komunikaci k automatizaci monitorování, řízení a ochrany distribučních sítí elektrické energie pro chytřejší a spolehlivější síť.

## Popis

Distribuční automatizace (DA) je standardizovaná služba v rámci 3GPP navržená pro podporu komunikačních požadavků na automatizaci distribučních sítí elektrické energie. Využívá buňkové sítě, zejména LTE a 5G, k zajištění spolehlivého, nízkolatenčního a zabezpečeného spojení mezi dispečinkem utility a zařízeními v terénu rozmístěnými po síti. Architektura je postavena na 3GPP frameworku pro komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)), kde jsou zařízení DA implementována jako uživatelská zařízení (UE) se specifickými požadavky na službu. Tato zařízení se připojují k síti prostřednictvím standardního rádiového přístupu (eNodeB/gNB) a funkcí jádra sítě, ale jejich provoz je identifikován a směrován na základě parametrů specifických pro službu, aby bylo zajištěno odpovídající zacházení z hlediska kvality služby (QoS) a zabezpečení.

Služba funguje definováním vyhrazené komunikační služby pro DA v rámci systému 3GPP. To zahrnuje specifikaci požadavků na službu, síťových schopností a adaptací protokolů pro splnění přísných potřeb provozu sítě. Mezi klíčové síťové komponenty patří funkce pro vystavení schopností služby ([SCEF](/mobilnisite/slovnik/scef/)) nebo funkce pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) v 5G, které vystavují síťové schopnosti, jako je spouštění zařízení, monitorování a skupinové zasílání zpráv, aplikačnímu serveru DA ([AS](/mobilnisite/slovnik/as/)) provozovanému utilitou. DA AS komunikuje s zařízeními v terénu – jako jsou dálkové koncové jednotky (RTU), inteligentní elektronická zařízení ([IED](/mobilnisite/slovnik/ied/)) a senzory – prostřednictvím sítě 3GPP. Komunikace může být mezi zařízením a AS (pro řízení a sběr dat) nebo mezi zařízeními navzájem (pro lokalizované ochranné schémata sítě), přičemž síť zajišťuje potřebné směrování, zabezpečení a stanovení priority.

Úlohou DA v síti je umožnit kritické aplikace chytrých sítí. Specifikuje výkonnostní cíle pro latenci, spolehlivost, dostupnost a velikost zpráv pro podporu funkcí, jako je monitorování stavu sítě v reálném čase, dálkové ovládání spínačů, automatická lokalizace a izolace poruch a regulace napětí/ jalového výkonu. Specifikace 3GPP definují, jak buňková síť přiděluje prostředky, vytváří přenosové cesty se zaručenými přenosovými rychlostmi nebo prioritní QoS a uplatňuje bezpečnostní mechanismy, jako je šifrování a ochrana integrity, přizpůsobené pro komunikaci na úrovni utility. To mění veřejnou buňkovou infrastrukturu na životaschopnou, škálovatelnou a nákladově efektivní alternativu k privátním komunikačním sítím utility pro distribuční automatizaci.

## K čemu slouží

Distribuční automatizace byla vytvořena, aby řešila vyvíjející se komunikační potřeby moderních elektrických sítí, které jsou stále více decentralizované, dynamické a závislé na datech v reálném čase. Tradiční distribuční sítě elektrické energie fungovaly s omezenou automatizací, využívaly manuální procesy nebo zastaralé komunikační systémy (jako jsou pronajaté linky, [PLC](/mobilnisite/slovnik/plc/) nebo privátní rádiové sítě), které byly často nákladné, nepružné a neškálovatelné. Integrace obnovitelných zdrojů energie, elektrických vozidel a požadavky na vyšší spolehlivost (např. zkrácení doby výpadků) si vynutily komunikační řešení, které by podporovalo rozsáhlé nasazení inteligentních zařízení v terénu s požadavky na nízkou latenci, vysokou spolehlivost a silné zabezpečení.

Motivací pro standardizaci DA v rámci 3GPP bylo využít všudypřítomnost, úspory z rozsahu a kontinuální vývoj buňkové technologie. Definováním DA jako specifické služby umožňuje 3GPP utilitám používat komerční buňkové sítě pro provozně kritické činnosti v síti bez nutnosti proprietárních řešení. To řeší problémy s interoperabilitou, dlouhodobou použitelností a nákladově efektivním pokrytím široké oblasti. Odstraňuje omezení předchozích přístupů tím, že poskytuje standardizovanou, IP-based a zabezpečenou platformu, která podporuje jak stávající protokoly pro automatizaci sítí (jako DNP3, [IEC](/mobilnisite/slovnik/iec/) 61850), tak nové aplikace, a usnadňuje tak přechod k chytřejším, odolnějším a účinnějším distribučním sítím.

## Klíčové vlastnosti

- Standardizovaná nízkolatenční komunikace pro časově kritické řídicí příkazy (např. ovládání spínačů)
- Vysoké cíle spolehlivosti a dostupnosti vhodné pro ochranu a automatizaci sítě
- Podpora skupinové komunikace pro efektivní multicast/broadcast směrem k zařízením v terénu
- Rozšířené bezpečnostní mechanismy včetně vzájemného ověřování a šifrování pro provoz utility
- Schopnosti vystavení sítě (prostřednictvím SCEF/NEF) pro konfiguraci a monitorování parametrů specifických pro službu
- Diferenciace QoS pro zvýšení priority provozu DA oproti jiným buňkovým službám

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.438** (Rel-20) — SEAL Digital Asset Service for Metaverse
- **TS 24.550** (Rel-19) — Metaverse Enablement Services Protocol
- **TS 28.318** (Rel-19) — Management and Orchestration for Energy Utilities
- **TR 28.829** (Rel-18) — Technical Report on Network and Service Operations for Energy Utilities
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications
- **TS 29.809** (Rel-12) — Diameter Overload Control Study
- **TS 29.892** (Rel-16) — Study on User Plane Protocol in 5GC
- **TS 33.721** (Rel-19) — Security Study for 5G Mobile Metaverse
- **TS 43.068** (Rel-19) — Voice Group Call Service (VGCS) Stage 2
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [DA na 3GPP Explorer](https://3gpp-explorer.com/glossary/da/)
