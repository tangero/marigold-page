---
slug: "scef"
url: "/mobilnisite/slovnik/scef/"
type: "slovnik"
title: "SCEF – Service Capability Exposure Function"
date: 2026-01-01
abbr: "SCEF"
fullName: "Service Capability Exposure Function"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/scef/"
summary: "Funkce jádra sítě zavedená pro buněčný internet věcí (CIoT), která bezpečně zpřístupňuje síťové služby a možnosti (jako je spouštění zařízení, monitorování a přenos malých objemů dat) autorizovaným ap"
---

SCEF je funkce jádra sítě, která bezpečně zpřístupňuje služby a možnosti sítí pro buněčný internet věcí (např. spouštění zařízení) autorizovaným serverům třetích stran prostřednictvím řízené brány.

## Popis

Service Capability Exposure Function (SCEF) je klíčový síťový prvek definovaný od 3GPP Release 13, který byl speciálně navržen pro podporu buněčného internetu věcí (CIoT) a komunikace typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)). Nachází se v jádru sítě, typicky v rámci architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 5G Core, ačkoli byl původně představen pro Evolved Packet Core (EPC). Hlavní úlohou SCEF je fungovat jako bezpečná severovýchodní [API](/mobilnisite/slovnik/api/) brána, která abstrahuje a zpřístupňuje definovanou sadu síťových možností externím aplikačním serverům ([AS](/mobilnisite/slovnik/as/)) patřícím poskytovatelům služeb nebo podnikům. Poskytuje standardizované RESTful API (založené na [HTTP](/mobilnisite/slovnik/http/)/[JSON](/mobilnisite/slovnik/json/)) definované v 3GPP TS 29.122 (Nnef).

Z architektonického hlediska SCEF interně komunikuje s řadou funkcí jádra sítě. Mezi klíčová rozhraní patří rozhraní T6a k [MME](/mobilnisite/slovnik/mme/) (pro spouštění a monitorování zařízení bez IP), rozhraní S6t k [HSS](/mobilnisite/slovnik/hss/) (pro odebírání změn údajů o účastnících) a rozhraní k PCRF/PGW pro řízení zásad a účtování. Když externí AS potřebuje odeslat downlink zprávu spícímu IoT zařízení (Device Triggering), pošle HTTP požadavek na API SCEF. SCEF požadavek ověří a autorizuje a poté použije rozhraní T6a, aby instruovalo MME k vyvolání zařízení a navázání spojení, aby mohla být data doručena. Podobně pro monitorování může AS požádat o upozornění, když se zařízení stane dostupné (dosáhnutelnost) nebo se přesune (reportování polohy), a SCEF spravuje tato odebírání s HSS a MME.

Jak to funguje, zahrnuje několik klíčových komponent: vrstvu pro zpřístupnění API (API Exposure Layer), která zpracovává externí REST API; funkci zabezpečení a vynucování zásad (Security and Policy Enforcement), která ověřuje přihlašovací údaje AS a uplatňuje zásady řízení přístupu; orchestrátor síťových funkcí (Network Function Orchestrator), který překládá API požadavky do příslušných signalizačních zpráv starších systémů nebo SBA (např. Diameter nebo HTTP/2); a správce odebírání (Subscription Manager), který sleduje aktivní monitorovací požadavky od AS. Jeho úlohou je umožnit efektivní, síťově optimalizované služby IoT. Díky centralizovanému zpřístupňování umožňuje síti nabízet cenné služby, jako je doručování ne-IP dat (NIDD) přes řídicí rovinu, což je klíčové pro nízkopříkonové, nepravidelné přenosy dat, při zachování přísné bezpečnosti, ochrany soukromí a kontroly síťových zdrojů. Je základním kamenem architektury pro zpřístupňování sítě 3GPP pro IoT.

## K čemu slouží

SCEF byl vytvořen k řešení specifických výzev při masivním nasazení IoT zařízení přes buněčné sítě. Tradiční buněčné architektury byly navrženy pro komunikaci zaměřenou na člověka, která je neustále online a má vysoké přenosové rychlosti. IoT zařízení jsou naopak často napájena bateriemi, posílají velmi malé objemy dat nepravidelně a mohou po dlouhou dobu setrvávat v klidovém stavu. Stávající metoda zpřístupňování možností – často prostřednictvím přímých, na míru vytvořených integrací s PGW nebo PCRF – byla nejistá, neefektivní a neškálovatelná pro miliony zařízení. Nebyl zde standardizovaný, bezpečný způsob, jak by například služba třetí strany pro meteosenzory mohla požádat o síťové probuzení svého zařízení nebo zkontrolovat jeho stav připojení.

Omezení předchozích přístupů byla zřejmá: nedostatek jednotného bodu zpřístupnění vedl k bezpečnostním slabinám, složitým integračním projektům pro každou novou službu a neschopnosti využít síťové optimalizace, jako je optimalizace CIoT EPS přes řídicí rovinu. SCEF tyto problémy řeší tím, že poskytuje jediný, standardizovaný a bezpečný bod zpřístupnění. Abstrahuje složité, na signalizaci náročné síťové procedury do jednoduchých API volání. To umožňuje poskytovatelům služeb IoT snadno vytvářet aplikace, které komunikují s jejich zařízeními, aniž by potřebovali rozumět protokolům jádra sítě, jako je Diameter, GTP a další.

Historicky byl jeho vznik motivován prací 3GPP na optimalizacích CIoT v Release 13. SCEF spolu s koncepty jako NIDD a optimalizace CIoT EPS přes uživatelskou rovinu tvořil ucelený balíček, který učinil buněčné sítě vhodnými pro nízkonákladový, nízkopříkonový IoT. Umožňuje nové obchodní modely a služby, jako je prediktivní údržba, chytré měření a sledování majetku, tím, že poskytovatelům služeb dává řízený přístup k výkonné síťové inteligenci a možnostem správy zařízení, čímž proměňuje buněčnou síť v platformu umožňující IoT.

## Klíčové vlastnosti

- Bezpečné RESTful API (Nnef) pro aplikační servery třetích stran
- Služba spouštění zařízení (Device Triggering) pro probouzení spících IoT zařízení
- Monitorování založené na odebírání událostí dosáhnutelnosti a polohy zařízení
- Podpora doručování ne-IP dat (NIDD) přes řídicí rovinu
- Ověřování, autorizace a omezení rychlosti pro spotřebitele API
- Orchestrace interakcí s MME, HSS, PCRF a SMSC

## Definující specifikace

- **TS 22.830** (Rel-16) — Business Role Models for Network Slicing
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.538** (Rel-19) — MSGin5G Service Protocol Specification
- … a dalších 30 specifikací

---

📖 **Anglický originál a plná specifikace:** [SCEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/scef/)
