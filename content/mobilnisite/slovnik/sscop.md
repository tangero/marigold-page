---
slug: "sscop"
url: "/mobilnisite/slovnik/sscop/"
type: "slovnik"
title: "SSCOP – Service Specific Connection Oriented Protocol"
date: 2025-01-01
abbr: "SSCOP"
fullName: "Service Specific Connection Oriented Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sscop/"
summary: "Transportní protokol v rámci ATM transportní vrstvy rozhraní Iu, zajišťující spolehlivý přenos dat ve správném pořadí pro signalizaci řídicí roviny. Zajišťuje bezchybné doručování a řízení toku mezi R"
---

SSCOP je Service Specific Connection Oriented Protocol, transportní protokol na bázi ATM, který zajišťuje spolehlivý přenos dat ve správném pořadí a řízení toku pro signalizaci řídicí roviny v rámci rozhraní Iu.

## Popis

Service Specific Connection Oriented Protocol (SSCOP) je protokol linkové vrstvy definovaný doporučením [ITU-T](/mobilnisite/slovnik/itu-t/) Q.2110 a přijatý 3GPP pro použití v [ATM](/mobilnisite/slovnik/atm/) transportních sítích, primárně v rámci rozhraní Iu spojujícího Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a Core Network (CN). SSCOP funguje jako část Service Specific Convergence Sublayer ([SSCS](/mobilnisite/slovnik/sscs/)) nad ATM Adaptation Layer 5 ([AAL5](/mobilnisite/slovnik/aal5/)). Jeho hlavní funkcí je poskytovat spolehlivou, spojově orientovanou službu přenosu dat pro signalizační zprávy, zajišťující jejich doručení bez chyb, ve správném pořadí a bez ztráty nebo duplikace. Toho je dosaženo mechanismy jako číslování sekvencí, selektivní retransmise poškozených nebo ztracených Protocol Data Units ([PDU](/mobilnisite/slovnik/pdu/)) a řízení toku pro zabránění přetečení přijímacího bufferu.

SSCOP funguje tak, že před zahájením přenosu dat naváže potvrzené spojení mezi partnerskými entitami. Pro řízení přenosu používá protokol s plovoucím oknem, kde je každé PDU přiděleno pořadové číslo. Příjemce potvrzuje správně přijatá PDU a odesílatel po vypršení časového limitu přenese znovu všechna nepotvrzená PDU. SSCOP také zahrnuje keep-alive funkci pro sledování stavu spojení a proceduru pro obnovu po chybě protokolu. Nabízí jak zaručený (assured), tak nezaručený (unassured) režim přenosu; zaručený režim garantuje doručení, zatímco nezaručený režim poskytuje jednodušší, negarantovanou službu vhodnou pro některé řídicí funkce.

V rámci architektury 3GPP UMTS je SSCOP klíčovou součástí transportní síťové vrstvy pro signalizaci řídicí roviny napříč rozhraními Iu-CS (Circuit Switched), Iu-PS (Packet Switched) a Iur (inter-RNC). Nachází se pod Signaling Connection Control Part ([SCCP](/mobilnisite/slovnik/sccp/)) nebo jinými síťovými protokoly, čímž je izoluje od potenciální ztráty a neuspořádání buněk v podkladové ATM síti. Poskytnutím robustního, spojově orientovaného spoje SSCOP zajišťuje integritu a spolehlivost kritických signalizačních zpráv pro správu mobility, řízení hovorů a správu relací, čímž vytváří základní vrstvu pro stabilitu a výkon sítě.

## K čemu slouží

SSCOP byl vytvořen pro řešení potřeby spolehlivého transportu signalizace přes sítě Asynchronous Transfer Mode ([ATM](/mobilnisite/slovnik/atm/)), které byly primární transportní technologií pro rané verze 3G UMTS. ATM je samo o sobě spojově orientovaný protokol, ale funguje na úrovni buněk (53bytové buňky) a negarantuje spolehlivé doručení větších datových jednotek ve správném pořadí na vrstvě AAL5. Signalizační zprávy pro řízení hovorů a správu mobility jsou kritické a vyžadují zaručené doručení. Bez SSCOP by si protokoly vyšších vrstev musely samy implementovat složité mechanismy pro obnovu po chybě a uspořádání sekvencí, což by zvýšilo složitost a snížilo efektivitu.

Protokol řeší problém poskytnutí standardizované, robustní služby linkové vrstvy pro signalizaci přes rozhraní Iu. Abstrahuje nedokonalosti podkladového ATM transportu, jako je ztráta buněk nebo jejich neuspořádání způsobené zahlcením sítě nebo chybami, a vyšším vrstvám prezentuje spolehlivý datový proud. Toto oddělení odpovědností umožňuje návrhářům signalizačních protokolů soustředit se na aplikační logiku namísto spolehlivosti transportu. Jeho zavedení ve verzi Release 99 bylo nezbytné pro provozní integritu sítě UMTS, neboť zajišťovalo, že komunikace řídicí roviny mezi RAN a CN byla spolehlivá, což je základní pro služby jako hlasové hovory a paketové relace.

## Klíčové vlastnosti

- Poskytuje spolehlivý, spojově orientovaný přenos dat se zaručeným doručením ve správném pořadí
- Implementuje selektivní retransmisi na základě pořadových čísel a hlášení stavu od přijímače
- Obsahuje mechanismy řízení toku pro zabránění přetečení přijímacího bufferu
- Podporuje jak zaručený (assured), tak nezaručený (unassured) režim přenosu
- Nabízí navázání a uvolnění spojení s potvrzovacími procedurami
- Zahrnuje keep-alive funkci a procedury pro obnovu po chybě protokolu pro udržení zdraví spojení

## Související pojmy

- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)
- [AAL5 – ATM Adaptation Layer type 5](/mobilnisite/slovnik/aal5/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.432** (Rel-19) — Iub NBAP Signalling Transport Specification
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [SSCOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sscop/)
