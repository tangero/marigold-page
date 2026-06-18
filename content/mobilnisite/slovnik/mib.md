---
slug: "mib"
url: "/mobilnisite/slovnik/mib/"
type: "slovnik"
title: "MIB – Management Information Base"
date: 2026-01-01
abbr: "MIB"
fullName: "Management Information Base"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mib/"
summary: "Strukturovaná hierarchická databáze používaná pro správu sítí, která uchovává informace o spravovaných objektech, jako jsou zařízení, rozhraní a protokoly. Je nezbytná pro monitorování, řízení a konfi"
---

MIB je strukturovaná databáze používaná pro správu sítí, která uchovává informace o spravovaných objektech a umožňuje standardizované monitorování a řízení síťových prvků pomocí protokolů jako SNMP.

## Popis

Management Information Base (MIB) je základní součást systémů pro správu sítí, definovaná jako virtuální databáze uchovávající správní informace síťových entit. Je strukturována podle Structure of Management Information ([SMI](/mobilnisite/slovnik/smi/)), která používá hierarchický stromový formát s identifikátory objektů ([OID](/mobilnisite/slovnik/oid/)) pro jednoznačné pojmenování každého spravovaného objektu. Tyto objekty reprezentují různé aspekty síťového zařízení, jako jsou konfigurační parametry, statistika výkonu, provozní stavy a stavy poruch. MIB sama data neuchovává, ale definuje schéma – typy dat, k nimž lze přistupovat, jejich syntaxi a přístupová práva (např. pouze pro čtení nebo pro čtení i zápis). Toto schéma je implementováno v agentech pro správu sítí, kteří jsou umístěni na zařízeních jako jsou směrovače, přepínače nebo základnové stanice.

Při provozu systém pro správu sítí ([NMS](/mobilnisite/slovnik/nms/)) komunikuje s MIB prostřednictvím správních protokolů, především Simple Network Management Protocol ([SNMP](/mobilnisite/slovnik/snmp/)). NMS odešle SNMP požadavky (např. GET, [SET](/mobilnisite/slovnik/set/)) agentovi na spravovaném zařízení a specifikuje OID požadovaného objektu. Agent následně přistoupí k odpovídajícím datům z vnitřního stavu zařízení a vrátí je v SNMP odpovědi. Například MIB může definovat objekty pro propustnost rozhraní, počty chyb nebo vytížení [CPU](/mobilnisite/slovnik/cpu/), což umožňuje NMS monitorovat stav sítě. Úlohou MIB je poskytnout standardizované, dodavatelsky neutrální rozhraní, které zajišťuje konzistentní interpretaci správních dat z různých zařízení.

Klíčové součásti MIB zahrnují spravované objekty, což jsou datové proměnné reprezentující síťové zdroje; notifikace (nebo pasti), což jsou asynchronní upozornění odesílané agenty pro hlášení událostí, jako jsou poruchy; a skupiny, které organizují související objekty pro modularitu. MIB jsou definovány v textových souborech pomocí notace ASN.1 a jsou kompilovány do formátu použitelného správním softwarem. V sítích 3GPP jsou MIB klíčové pro správu prvků napříč rádiovou přístupovou sítí (RAN) a jádrem sítě (CN), jako jsou NodeB, eNodeB, gNB a [MME](/mobilnisite/slovnik/mme/). Umožňují správu poruch, monitorování výkonu, konfiguraci a auditování zabezpečení a tvoří základ systémů pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)).

Architektura MIB v 3GPP se vyvíjí napříč releasy, přičemž specifikace detailně popisují MIB moduly pro různé síťové funkce. Například řada 3GPP TS 32.600 definuje MIB pro správu výkonu, zatímco TS 28.622 pokrývá modely síťových zdrojů pro 5G. MIB podporují škálovatelnost prostřednictvím modulárního návrhu, což umožňuje přidávání nových objektů pro vznikající technologie, jako je 5G NR nebo síťové segmenty (network slicing). Integrují se s vyššími správními rámci, jako jsou vrstvy Network Management (NM) a Element Management (EM) v modelu Telecommunications Management Network (TMN). Tím, že abstrahují specifické detaily zařízení do společného schématu, MIB snižují složitost správy a usnadňují automatizaci, což je klíčové pro rozsáhlé dynamické sítě.

## K čemu slouží

MIB byla vytvořena, aby řešila výzvy správy heterogenních telekomunikačních sítí s více dodavateli. Před standardizací každý výrobce zařízení používal proprietární správní rozhraní, což operátorům ztěžovalo integraci a monitorování různorodých síťových prvků. To vedlo k vysokým provozním nákladům, nekonzistentním datovým formátům a omezené interoperabilitě. MIB jako součást frameworku SNMP vyvinutého koncem 80. let 20. století poskytla univerzální jazyk pro správu sítí, což umožnilo centralizované řízení a monitorování. V 3GPP její přijetí zajistilo, že mobilní sítě mohou být efektivně spravovány, jak rostly ve složitosti od 2G po 5G.

Primární problém, který MIB řeší, je absence společného datového modelu pro správu sítí. Definováním strukturované hierarchie spravovaných objektů umožňuje systémům pro správu sítí dotazovat se a konfigurovat zařízení od různých dodavatelů pomocí stejného protokolu (SNMP). Tato standardizace snižuje úsilí při integraci, zlepšuje detekci poruch a podporuje automatizované operace. Pro 3GPP jsou MIB nezbytné pro splnění regulatorních požadavků, zajištění kvality služeb a umožnění funkcí, jako jsou samoorganizující se sítě (SON). Také usnadňují vývoj směrem k softwarově definovaným sítím (SDN) a virtualizaci síťových funkcí (NFV) tím, že poskytují konzistentní správní rozhraní.

Historicky koncept MIB vznikl v Internet Engineering Task Force (IETF) a byl začleněn do standardů 3GPP, aby sladil s širšími IT postupy. Jeho motivací byla potřeba sledování v reálném čase v dynamických mobilních prostředích, kde se parametry, jako jsou rádiové podmínky nebo zatížení od uživatelů, rychle mění. MIB umožňují operátorům sledovat klíčové ukazatele výkonu (KPI), konfigurovat síťové segmenty (slices) a spravovat bezpečnostní politiky. Jak se sítě vyvíjely, MIB se rozšířily, aby pokryly nové technologie, jako jsou LTE a NR, a řešily tak omezení dřívějších přístupů ke správě, které byly méně flexibilní nebo škálovatelné.

## Klíčové vlastnosti

- Hierarchická struktura využívající identifikátory objektů (OID) pro jednoznačné pojmenování spravovaných objektů
- Standardizovaná definice dat pomocí syntaxe ASN.1, zajišťující interoperabilitu mezi dodavateli
- Podpora SNMP operací (GET, SET, NOTIFY) pro monitorování a řízení síťových prvků
- Modulární návrh umožňující rozšiřitelnost pro nové síťové funkce a technologie
- Integrace s 3GPP správními frameworky, jako je Performance Management (PM) a Fault Management (FM)
- Schopnost definovat notifikace (past) pro asynchronní hlášení událostí

## Související pojmy

- [SNMP – Simple Network Management Protocol](/mobilnisite/slovnik/snmp/)
- [OID – Organisation Identifier](/mobilnisite/slovnik/oid/)
- [SMI – Structure of Management Information](/mobilnisite/slovnik/smi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.122** (Rel-19) — Advanced Alarm Management IRP Information Service
- **TS 32.123** (Rel-9) — Advanced Alarm Management IRP CORBA Solution Set
- **TS 32.125** (Rel-9) — AAM IRP XML File Format Definition
- **TS 32.126** (Rel-19) — AAM IRP Solution Set Definitions
- **TS 32.301** (Rel-19) — Notification IRP Requirements
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [MIB na 3GPP Explorer](https://3gpp-explorer.com/glossary/mib/)
