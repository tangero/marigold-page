---
slug: "stm"
url: "/mobilnisite/slovnik/stm/"
type: "slovnik"
title: "STM – Signalling Traffic Monitoring"
date: 2025-01-01
abbr: "STM"
fullName: "Signalling Traffic Monitoring"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/stm/"
summary: "Funkce správy sítě, která zahrnuje sběr, analýzu a reportování toků signalizačních zpráv mezi síťovými prvky. Používá se pro monitorování výkonu, detekci chyb, plánování kapacity a bezpečnostní dohled"
---

STM je funkce správy sítě pro sběr, analýzu a reportování toků signalizačních zpráv mezi síťovými prvky za účelem podpory monitorování výkonu, detekce chyb, plánování kapacity a bezpečnostního dohledu.

## Popis

Signalling Traffic Monitoring (STM) je kritická funkce správy, správy a údržby (Operations, Administration, and Maintenance – [OAM](/mobilnisite/slovnik/oam/)) definovaná konsorciem 3GPP pro sledování a analýzu signalizace řídicí roviny v mobilní síti. Zahrnuje pasivní odposlech signalizačních spojů (např. [SS7](/mobilnisite/slovnik/ss7/), Diameter, [GTP-C](/mobilnisite/slovnik/gtp-c/)) mezi síťovými uzly, jako jsou [MME](/mobilnisite/slovnik/mme/), [HSS](/mobilnisite/slovnik/hss/), [SGW](/mobilnisite/slovnik/sgw/), [PGW](/mobilnisite/slovnik/pgw/) a [MSC](/mobilnisite/slovnik/msc/), za účelem zachycení výměn zpráv. Architektura typicky sestává ze sond nebo mediačních zařízení nasazených na strategických místech sítě, které kopírují signalizační zprávy, ze sběrného systému, který tato data agreguje a koreluje, a z analytické platformy poskytující vizualizaci, vytváření alarmů a reportování.

STM funguje pomocí neinvazivních sond, které zrcadlí signalizační provoz bez ovlivnění výkonu živé sítě. Tyto sondy dekódují protokoly (např. MAP, CAP, Diameter, S1-AP, NAS) a extrahují klíčové informace z každé zprávy, jako je typ zprávy, zdroj, cíl, časová razítka a obsažené parametry (např. IMSI, MSISDN, příčinné kódy). Následně jsou sebraná data časově korelována a zpracována na bázi relací, aby bylo možné rekonstruovat kompletní signalizační sekvence pro jednotlivé účastníky nebo transakce. To umožňuje síťovým inženýrům trasovat průběh hovoru při neúspěšném volání, analyzovat vzorce směrování nebo detekovat anomální signalizační bouře. Mezi klíčové komponenty patří monitorovací sondy, korelační engine a systém řízení, který prezentuje klíčové ukazatele výkonu (Key Performance Indicators – KPIs), jako jsou rychlosti přenosu zpráv, poměry úspěšnosti/neúspěšnosti a doby odezvy.

Jeho role je zásadní pro zajištění spolehlivosti, bezpečnosti a efektivity sítě. Z pohledu výkonu pomáhá STM identifikovat úzká místa, chybné konfigurace a selhávající síťové prvky analýzou signalizačních zpoždění a chybovosti. Pro bezpečnost je STM primárním nástrojem pro detekci a zmírnění útoků založených na signalizaci, jako je podvod, sledování polohy nebo útoky typu odmítnutí služby (Denial-of-Service – DoS) zneužívající signalizační protokoly. Data z STM jsou navíc neocenitelná pro plánování kapacity, neboť poskytují reálné vzorce provozu pro přesné dimenzování síťových zdrojů, a pro regulatorní shodu, jako je zákonné odposlouchávání a ověřování přenositelnosti čísel.

## K čemu slouží

STM byl vyvinut pro řešení rostoucí složitosti a kritičnosti signalizačních sítí v digitálních mobilních systémech (od GSM výše). Jak se sítě vyvíjely od jednoduchých hlasových hovorů ke komplexním službám s přepojováním paketů, objem a rozmanitost signalizačního provozu explodovaly. Tradiční systémy správy sítě zaměřené na data uživatelské roviny a hardwarové závady byly nedostatečné pro diagnostiku problémů pramenících z interakcí protokolů nebo chyb v softwarové logice řídicí roviny.

Jádrem problému, který STM řeší, je poskytnutí přehledu do 'nervového systému' sítě – signalizace, která navazuje, spravuje a ukončuje každý hovor a datovou relaci. Bez STM bylo odstraňování závad při přerušeném hovoru nebo neúspěšném připojení k datům často pomalý, manuální proces kontroly logů na jednotlivých síťových prvcích. STM poskytuje holistický pohled napříč prvky. Jeho vznik byl motivován potřebou proaktivního zajištění provozu sítě, prevence podvodů a plnění přísných smluvních parametrů úrovně služeb (Service Level Agreements – SLAs) na konkurenčních trzích. Zároveň se stal klíčovým pro bezpečnost, protože signalizační protokoly, původně navržené pro důvěryhodná prostředí, se v IP sítích staly vystaveny novým hrozbám.

## Klíčové vlastnosti

- Neinvazivní, pasivní monitorování všech hlavních signalizačních protokolů (SS7, Diameter, GTP-C, SIP)
- Generování záznamů o hovorech (Call Data Record – CDR) a signalizačních tras pro jednotlivé účastníky
- Reálná korelace signalizačních zpráv napříč více rozhraními
- Detekce anomálií a vytváření alarmů pro signalizační bouře a bezpečnostní hrozby
- Výkonnostní KPIs pro signalizační zatížení, míru úspěšnosti a latenci
- Podpora zákonného odposlechu a extrakce dat pro regulatorní shodu

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 28.560** (Rel-19) — 5G Signalling Traffic Monitoring Specification

---

📖 **Anglický originál a plná specifikace:** [STM na 3GPP Explorer](https://3gpp-explorer.com/glossary/stm/)
