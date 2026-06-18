---
slug: "tdp"
url: "/mobilnisite/slovnik/tdp/"
type: "slovnik"
title: "TDP – Trigger Detection Point"
date: 2025-01-01
abbr: "TDP"
fullName: "Trigger Detection Point"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tdp/"
summary: "Trigger Detection Point (TDP) je klíčový koncept v architektuře Inteligentní sítě (IN) a CAMEL. Označuje specifický bod v modelu volání/stavu, kde může být spuštěna záchytná funkce k zachycení zpracov"
---

TDP je specifický bod v modelu volání nebo stavu, kde může být spuštěna záchytná funkce (trigger) k zachycení zpracování a vyvolání instance servisní logiky pro síťové služby v reálném čase.

## Popis

Trigger Detection Point (TDP) je klíčový architektonický prvek standardů Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a Customised Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)). Představuje přesnou, standardizovanou pozici v rámci konečného automatu, který modeluje volání nebo relaci (např. Basic Call State Model, [BCSM](/mobilnisite/slovnik/bcsm/)). V TDP může být funkce Service Switching Function ([SSF](/mobilnisite/slovnik/ssf/)) sítě nakonfigurována tak, aby pozastavila běžné zpracování hovoru/relace a komunikovala s externí Service Control Function ([SCF](/mobilnisite/slovnik/scf/)), která hostuje servisní logiku. Tato interakce umožňuje SCF ovlivnit další průběh hovoru nebo relace.

Technicky je TDP definován svým typem a bodem ve zpracování, kde nastává. Typy zahrnují TDP-R (Request), kde dojde k detekci a žádost je odeslána SCF před dalším zpracováním, a TDP-N (Notification), kde SSF pouze notifikuje SCF o události, ale nečeká nutně na instrukce. Klíčové TDP v modelu volání zahrnují Collected_Info (po načtení číslic), Analyzed_Information (po analýze čísla) a Route_Select_Failure (při selhání směrování). Když volání dosáhne aktivovaného TDP, SSF zabalí relevantní data o volání do standardizované zprávy (jako InitialDP v [CAP](/mobilnisite/slovnik/cap/)) a odešle je určené SCF. SCF následně vykoná svou servisní logiku a vrátí instrukce (např. Continue, Connect, Release) SSF pro pokračování ve zpracování.

V síťové architektuře jsou TDP pojítkem mezi přepínací vrstvou a vrstvou servisní inteligence. SSF, často integrovaná v [MSC](/mobilnisite/slovnik/msc/) nebo [GMSC](/mobilnisite/slovnik/gmsc/), obsahuje model stavu volání a monitoruje aktivované TDP. Aktivace může být statická (předem zřízena v profilu účastníka, např. v CAMEL Subscription Information, CSI) nebo dynamická (nastavena SCF během předchozí interakce). Tento mechanismus umožňuje čisté oddělení servisní kontroly od základního přepínání, což umožňuje vytváření a nasazování služeb nezávisle na dodavateli ústředny a bez nutnosti modifikace každé ústředny v síti.

## K čemu slouží

TDP byl vytvořen k řešení zásadního problému s nepružností tradičních telefonních sítí. V sítích před érou IN vyžadovaly nové služby zdlouhavé, nákladné a proprietární softwarové aktualizace každé telefonní ústředny. To dusilo inovace a nasazení funkcí, jako jsou bezplatná čísla (800) nebo komplexní směrování hovorů, bylo velmi náročné. Architektura Inteligentní sítě, s TDP jako základním kamenem, zavedla revoluční oddělení servisní logiky od přepínací funkce.

Jeho účelem je poskytnout standardizovaný 'háček' nebo bod zachycení uvnitř procesu zpracování hovoru. To umožňuje externímu, centralizovanému bodu servisní kontroly ovlivňovat hovory v reálném čase. Historickým kontextem je vývoj od funkcí na úrovni ústředny k síťovým službám v 90. letech 20. století. TDP umožnily vzestup rozsáhlého trhu se službami s přidanou hodnotou, nejvýznamněji předplacené mobilní služby, která by byla ekonomicky neproveditelná bez kontroly kreditu v reálném čase zprostředkované přes TDP jako Collected_Info. Řešily omezení monolitického softwaru ústředen definováním stabilního, abstraktního rozhraní (TDP), kde mohly probíhat servisní interakce, což učinilo síť připravenou na budoucí požadavky nových služeb.

## Klíčové vlastnosti

- Standardizovaný bod v modelu stavu hovoru/relace pro servisní interakci
- Definuje typy, jako je TDP-R (Request) a TDP-N (Notification)
- Umožňuje aktivaci staticky (z dat účastníka) nebo dynamicky (z SCF)
- Spouští pozastavení zpracování hovoru a vyvolání servisní logiky
- Umožňuje výměnu dat o hovoru a řídicích instrukcí mezi SSF a SCF
- Klíčový prvek pro CAMEL, IMS Service Control a další služby založené na IN

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [SSF – Service Switching Function](/mobilnisite/slovnik/ssf/)
- [SCF – Service Control Function (IN context), Service Capability Feature (VHE/OSA context)](/mobilnisite/slovnik/scf/)
- [BCSM – Basic Call State Model](/mobilnisite/slovnik/bcsm/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider

---

📖 **Anglický originál a plná specifikace:** [TDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdp/)
