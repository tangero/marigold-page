---
slug: "smp"
url: "/mobilnisite/slovnik/smp/"
type: "slovnik"
title: "SMP – System Management Processes"
date: 2025-01-01
abbr: "SMP"
fullName: "System Management Processes"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/smp/"
summary: "System Management Processes (SMP) jsou standardizované postupy a funkce pro správu síťových prvků 3GPP. Poskytují rámec pro správu poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS), čímž zaj"
---

SMP je soubor standardizovaných postupů a funkcí pro správu síťových prvků 3GPP, který poskytuje rámec pro správu poruch, konfigurace, účtování, výkonu a zabezpečení za účelem zajištění konzistentního provozu.

## Popis

System Management Processes (SMP) představují komplexní rámec pro správu definovaný ve specifikacích 3GPP, který řídí provoz, administraci a údržbu ([OAM](/mobilnisite/slovnik/oam/)) síťových prvků. Architektura je založena na modelu FCAPS, který vymezuje pět klíčových funkčních oblastí: správu poruch, správu konfigurace, správu účtování, správu výkonu a správu zabezpečení. Tyto procesy jsou implementovány kombinací řídicích funkcí umístěných na síťových prvcích (spravované objekty) a řídicích systémů (řídicí systémy), které komunikují prostřednictvím standardizovaných rozhraní. Rámec zajišťuje, že síťové prvky od různých dodavatelů lze spravovat jednotným způsobem, což usnadňuje interoperabilitu v prostředí více dodavatelů a zjednodušuje provoz sítě.

Jádrem SMP je definice informačních modelů, postupů a protokolů nezbytných pro efektivní správu. Informační modely, často založené na konceptech jako jsou báze řídicích informací ([MIB](/mobilnisite/slovnik/mib/)), formálně popisují spravovatelné atributy, operace a notifikace síťových zdrojů. Postupy specifikují posloupnosti akcí pro úkoly, jako jsou softwarové aktualizace, hlášení alarmů nebo sběr dat o výkonu. Protokoly jako [SNMP](/mobilnisite/slovnik/snmp/) nebo řešení založená na [CORBA](/mobilnisite/slovnik/corba/) (historicky používané) či modernější RESTful [API](/mobilnisite/slovnik/api/) (jak je vidět v pozdějších specifikacích, například 29.500 pro 5G Core) poskytují komunikační mechanismy pro provádění těchto postupů. Řídicí systém komunikuje s agentem spravovaného prvku za účelem získávání dat (operace GET), úpravy konfigurací (operace [SET](/mobilnisite/slovnik/set/)) a přijímání asynchronních notifikací událostí (trapy nebo notifikace).

Role SMP je nedílnou součástí celého životního cyklu sítě, od počátečního nasazení a uvedení do provozu až po průběžnou optimalizaci a případné vyřazení. Umožňuje operátorům sítě sledovat stav, diagnostikovat poruchy, provizionovat služby, sledovat využití zdrojů pro účtování, sbírat klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) pro optimalizaci a vynucovat bezpečnostní politiky. Standardizací těchto procesů 3GPP zajišťuje snížení složitosti správy, kontrolu provozních nákladů a udržení spolehlivosti služeb. Specifikace jako 32.150 stanovují vysoké požadavky, zatímco jiné, například 29.500 (pro architekturu 5G založenou na službách), definují konkrétní implementaci těchto principů správy na úrovni protokolů.

## K čemu slouží

Hlavním účelem System Management Processes (SMP) je poskytnout dodavatelsky neutrální a na technologii nezávislý rámec pro správu sítí 3GPP. Před zavedením takové standardizace čelili operátoři sítí významným výzvám při integraci a správě zařízení od více dodavatelů, z nichž každý měl proprietární řídicí rozhraní a datové modely. To vedlo k vysokým provozním nákladům ([OPEX](/mobilnisite/slovnik/opex/)), složitým integračním projektům a snížené flexibilitě při nasazování sítí a inovaci služeb. SMP bylo vytvořeno k řešení těchto problémů s interoperabilitou definováním společných principů správy, informačních modelů a rozhraní.

Historicky, jak se mobilní sítě vyvíjely od 2G GSM přes 3G UMTS a dále, složitost síťových prvků a služeb, které podporovaly, dramaticky vzrostla. Potřeba automatizované, efektivní a spolehlivé správy se stala prvořadou pro zajištění kvality služeb, rychlého řešení poruch a škálovatelného provozu. Model FCAPS, převzatý z rámce Telekomunikační řídicí sítě (TMN) ITU-T, poskytl osvědčený strukturní základ. Práce 3GPP na SMP přetavila tyto vysoké koncepty do konkrétních, implementovatelných standardů šitých na míru buněčným síťovým prvkům, jako jsou NodeB, eNodeB, MME, SGW a AMF.

SMP řeší kritickou potřebu správy životního cyklu v moderních softwarově definovaných a virtualizovaných sítích. S nástupem 5G a virtualizace síťových funkcí (NFV) musí řídicí procesy zvládat nejen fyzický hardware, ale také virtualizované síťové funkce (VNF), jejich softwarové image a stavy jejich životního cyklu (instanciace, škálování, ukončení). Rámce SMP se vyvinuly tak, aby podporovaly tyto cloud-nativní paradigmy, a zajistily, že základní úkoly správy poruch, konfigurace, účtování, výkonu a zabezpečení zůstávají konzistentní a účinné i ve vysoce dynamickém, softwarově založeném síťovém prostředí.

## Klíčové vlastnosti

- Standardizovaný rámec správy FCAPS (Fault, Configuration, Accounting, Performance, Security)
- Dodavatelsky neutrální informační modely pro spravované objekty
- Podpora více řídicích protokolů (např. SNMP, CORBA, RESTful API)
- Definované postupy pro hlášení alarmů, sběr měření výkonu a správu softwaru
- Interoperabilita mezi řídicími systémy a síťovými prvky od více dodavatelů
- Podpora jak zastaralých fyzických síťových funkcí, tak moderních virtualizovaných/cloud-nativních síťových funkcí

## Související pojmy

- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TS 29.500** (Rel-19) — 5GC Service Based Architecture Specification
- **TS 32.150** (Rel-19) — IRP Concept and Definitions
- **TS 36.840** (Rel-12) — LTE 450 MHz Band Technical Requirements for Brazil

---

📖 **Anglický originál a plná specifikace:** [SMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/smp/)
