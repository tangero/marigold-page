---
slug: "tm"
url: "/mobilnisite/slovnik/tm/"
type: "slovnik"
title: "TM – Telecommunication Management"
date: 2025-01-01
abbr: "TM"
fullName: "Telecommunication Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tm/"
summary: "Komplexní rámec definovaný 3GPP pro správu všech aspektů telekomunikační sítě včetně správy poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS). Poskytuje standardizovaná rozhraní, informační"
---

TM je komplexní rámec 3GPP pro správu všech aspektů sítě, který poskytuje standardizovaná rozhraní a postupy pro monitorování, řízení a optimalizaci zdrojů a služeb.

## Popis

Telecommunication Management (TM) je zastřešující rámec 3GPP a soubor specifikací, které definují způsob provozu, správy a údržby mobilních sítí. Zahrnuje celý model FCAPS – správu poruch, konfigurace, účtování, výkonu a zabezpečení – aplikovaný na celou síťovou doménu včetně rádiové přístupové sítě (RAN), jádra sítě (CN) a koncového zařízení (UE). Architektura je typicky založena na modelu manažer-agent, kde systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)) fungují jako manažeři a jednotlivé síťové prvky ([NE](/mobilnisite/slovnik/ne/)), jako základnové stanice a uzly jádra, fungují jako spravovaní agenti. Komunikace mezi manažery a agenty využívá standardizovaná rozhraní, především Itf-N (severní rozhraní) a proprietární nebo standardizovaná jižní rozhraní.

Rámec funguje prostřednictvím souboru dobře definovaných řídicích funkcí. Správa poruch zahrnuje nepřetržité sledování sítě za účelem detekce, izolace a nápravy abnormálního provozu a poruch, včetně generování alarmů a notifikací. Správa konfigurace se zabývá instalací, poskytováním a úpravou síťového zařízení a softwaru, včetně nastavení síťových parametrů a aktualizací softwaru. Správa výkonu zahrnuje sběr a analýzu statistických dat týkajících se provozu sítě a přenosů, jako jsou úspěšnost hovorů, statistiky předávání hovorů a měření propustnosti, které se používají pro plánování kapacity a optimalizaci.

Správa účtování (často spojená s účtováním) shromažďuje data o využití zdrojů pro účely fakturace. Správa zabezpečení zajišťuje integritu, důvěrnost a dostupnost řídicích dat a operací. 3GPP specifikuje podrobné informační modely pro tyto funkce, často využívající objektově orientované paradigma, kde spravované entity (jako buňka nebo instance síťového řezu) jsou reprezentovány jako spravované objekty s definovanými atributy, operacemi a notifikacemi. Tyto modely jsou často realizovány pomocí protokolů jako [SNMP](/mobilnisite/slovnik/snmp/) nebo [CORBA](/mobilnisite/slovnik/corba/)/[CMIP](/mobilnisite/slovnik/cmip/) ve starších vydáních a v moderních implementacích se stále více přechází k NETCONF/YANG a RESTful [API](/mobilnisite/slovnik/api/). Rámec TM je nezbytný pro dosažení automatizovaného, efektivního a mezi dodavateli interoperabilního provozu sítě, což je klíčové pro škálovatelnost a spolehlivost rozsáhlých mobilních sítí.

## K čemu slouží

Telecommunication Management byl vytvořen k řešení kritických provozních výzev vyplývajících ze složitosti a vícedodavatelské povahy moderních mobilních sítí. V počátcích celulárních sítí byly systémy správy z velké části proprietární, což vedlo k závislosti na dodavateli, vysokým provozním nákladům a neefektivitě pro operátory provozující sítě se zařízeními od více dodavatelů. Nebyl standardizovaný způsob, jak monitorovat základnovou stanici Nokie a uzel jádra od Ericssonu z jediné konzole správy. Účelem standardizace TM v rámci 3GPP bylo definovat jednotný rámec, který zajišťuje interoperabilitu, snižuje provozní složitost a náklady.

K jeho vytvoření motivovala potřeba škálovatelných a automatizovaných operací. Jak sítě rostly od 2G přes 3G a dále, počet síťových prvků prudce vzrostl, což učinilo ruční konfiguraci a řešení problémů nepraktickými. Rámec TM poskytuje plán pro automatizované poskytování služeb, hromadnou konfiguraci a centralizované sledování poruch. Řeší problém integrace nových síťových technologií a služeb – jako IMS, LTE a 5G – do stávajících operačních podpůrných systémů ([OSS](/mobilnisite/slovnik/oss/)) definováním konzistentních řídicích rozhraní a informačních modelů. To umožňuje operátorům zavádět nové schopnosti bez nutnosti budovat zcela nové, izolované systémy správy.

Dále TM standardizuje kritický tok dat o výkonu a účtování, který je životně důležitý pro optimalizaci sítě a obchodní operace. Bez standardizovaných měření výkonu je obtížné porovnávat stav různých částí sítě nebo zařízení od různých dodavatelů. Standardizovaný sběr účtovacích dat je stejně zásadní pro generování přesných fakturačních záznamů. TM v podstatě existuje proto, aby přeměnil telekomunikační síť z kolekce hardwarových zařízení na programovatelnou, pozorovatelnou a efektivně spravovanou platformu pro poskytování služeb, což umožňuje kvalitu služeb a provozní efektivitu, kterou požadují účastníci a operátoři.

## Klíčové vlastnosti

- Komplexní rámec pokrývající správu FCAPS (poruch, konfigurace, účtování, výkonu, zabezpečení)
- Standardizovaná architektura manažer-agent a rozhraní (např. Itf-N) pro vícedodavatelskou interoperabilitu
- Definované informační modely (např. NRM – Network Resource Model) reprezentující spravované objekty
- Podporuje automatizované poskytování služeb, monitorování a optimalizaci síťových zdrojů
- Umožňuje centralizovanou správu poruch, výkonu a konfigurace pro celé sítě
- Usnadňuje integraci s externími OSS/BSS (operačními/obchodními podpůrnými systémy)

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 32.301** (Rel-19) — Notification IRP Requirements
- **TS 32.322** (Rel-19) — Test Management IRP Information Service
- **TS 32.325** (Rel-9) — Test Management IRP XML Definitions
- **TS 32.326** (Rel-19) — Test Management IRP Solution Set Definitions
- **TS 32.371** (Rel-19) — Security Management Concept & Requirements
- **TS 32.600** (Rel-19) — 3GPP Configuration Management Specification
- **TS 32.601** (Rel-19) — Basic Configuration Management IRP Requirements
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [TM na 3GPP Explorer](https://3gpp-explorer.com/glossary/tm/)
