---
slug: "snmp"
url: "/mobilnisite/slovnik/snmp/"
type: "slovnik"
title: "SNMP – Simple Network Management Protocol"
date: 2025-01-01
abbr: "SNMP"
fullName: "Simple Network Management Protocol"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/snmp/"
summary: "SNMP je široce používaný standardní protokol IETF pro monitorování a správu síťových zařízení. V sítích 3GPP se běžně používá pro správu IP síťových prvků, umožňuje správcům dotazovat se na informace"
---

SNMP je standardní protokol IETF používaný v sítích 3GPP pro monitorování a správu IP síťových prvků dotazováním informací o stavu a aplikací konfigurací.

## Popis

Simple Network Management Protocol (SNMP) je aplikační protokol, který je součástí sady internetových protokolů definovaných [IETF](/mobilnisite/slovnik/ietf/). Umožňuje výměnu řídicích informací mezi síťovými zařízeními (agenty) a stanicami pro správu sítě (manažery). Jádrem SNMP je jednoduchý mechanismus požadavek/odpověď. Manažer zasílá agentovi požadavky (GET, GETNEXT, GETBULK) pro získání hodnot konkrétních spravovaných objektů. Může také zaslat požadavek [SET](/mobilnisite/slovnik/set/) pro změnu hodnoty. Agent, který sídlí na spravovaném zařízení (např. router, switch nebo síťový prvek 3GPP s IP konektivitou), odpoví daty nebo chybovým kódem. Agenti mohou navíc asynchronně zasílat manažerům zprávy TRAP nebo INFORM, aby je upozornili na významné události (jako je výpadek spoje).

Struktura spravovaných informací je definována pomocí Management Information Bases ([MIB](/mobilnisite/slovnik/mib/)). MIB je hierarchický strom spravovaných objektů, z nichž každý je identifikován jedinečným Object Identifier ([OID](/mobilnisite/slovnik/oid/)). Tyto objekty představují skalární hodnoty (např. dobu provozu systému, stav rozhraní) nebo tabulková data (např. směrovací tabulku). 3GPP definuje vlastní MIB moduly (např. pro správu funkcí Node B, [eNB](/mobilnisite/slovnik/enb/) nebo [MME](/mobilnisite/slovnik/mme/)), které rozšiřují standardní MIB od IETF. Protokol funguje nad [UDP](/mobilnisite/slovnik/udp/), typicky na portech 161 (pro GET/SET) a 162 (pro trap), upřednostňuje jednoduchost a nízkou režii před zaručeným doručením.

V systému správy 3GPP se SNMP často používá jako jižní rozhraní (southbound interface) mezi systémem správy (jako [SNM](/mobilnisite/slovnik/snm/) nebo EM) a síťovými prvky, zejména pro správu chyb a výkonu. Manažer v pravidelných intervalech dotazuje agenta o výkonnostní čítače (PM) a přijímá trap zprávy pro hlášení alarmů. Jednoduchost protokolu a jeho všudypřítomnost v IP světě z něj učinily přirozenou volbu pro správu IP komponent, které se staly nedílnou součástí sítí 3G a 4G, jak je uvedeno v četných specifikacích 3GPP včetně těch pro architekturu správy (32.101, 32.102) a integrační referenční body (IRP), jako je Bulk CM IRP (32.622).

## K čemu slouží

SNMP byl vytvořen, aby vyřešil problém správy rychle rostoucích a heterogenních zařízení v IP sítích na konci 80. a začátku 90. let 20. století. Před jeho přijetím se správa často prováděla pomocí proprietárních příkazových řádků (CLI) nebo protokolů, což znemožňovalo centralizovanou správu sítě s více dodavateli. Klíčovou motivací bylo poskytnout jednoduchou, rozšiřitelnou a standardizovanou metodu pro monitorování stavu zařízení, konfiguraci nastavení a přijímání oznámení o událostech.

3GPP přijalo a odkazuje na SNMP (jako standard IETF) pro správu IP infrastruktury ve svých sítích. Jak se systémy 3GPP vyvíjely od jader s přepojováním okruhů k plně IP architekturám (GPRS, IMS, EPS), potřeba standardizované správy IP sítí se stala klíčovou. SNMP řeší problém rozhraní s širokou škálou běžně dostupných (COTS) IP routerů, switchů a serverů, které tvoří přenosovou a jádrovou síť. Poskytuje dobře známý mechanismus pro Operations Support System (OSS) ke sběru výkonnostních dat a chyb z těchto prvků. Zatímco 3GPP také definuje vlastní řešení správy (jako CORBA-based IRP pro prvky jádrové sítě), SNMP zůstává nezbytným nástrojem, zejména pro správu na úrovni prvků a podsítí infrastruktury s výraznou IP tradicí.

## Klíčové vlastnosti

- Jednoduchý mechanismus požadavek/odpověď (GET, SET) a trap
- Používá hierarchickou strukturu Management Information Base (MIB) s OID
- Funguje nad UDP pro nízkou režii
- Široce podporován prakticky všemi IP síťovými zařízeními
- Umožňuje centralizované monitorování a konfiguraci distribuovaných zařízení
- Rozšiřitelný definicí nových MIB modulů

## Související pojmy

- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [OID – Organisation Identifier](/mobilnisite/slovnik/oid/)
- [CORBA – Common Object Request Broker Architecture](/mobilnisite/slovnik/corba/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.602** (Rel-19) — Basic Configuration Management IRP Information Service
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM
- **TS 32.662** (Rel-19) — Configuration Management (CM); Kernel CM IRP
- **TS 32.824** (Rel-9) — SOA and IRP Gap Analysis
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [SNMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/snmp/)
