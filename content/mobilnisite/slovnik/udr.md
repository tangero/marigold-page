---
slug: "udr"
url: "/mobilnisite/slovnik/udr/"
type: "slovnik"
title: "UDR – Unified Data Repository"
date: 2026-01-01
abbr: "UDR"
fullName: "Unified Data Repository"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/udr/"
summary: "Centralizovaná funkce pro ukládání dat v 5G Core (5GC), která konsoliduje data účastníků a politiky. Poskytuje jediné sjednocené úložiště pro strukturovaná data, jako jsou data o předplatném, politiky"
infografika: "/assets/slovnik/udr.svg"
infografikaAlt: "Schéma architektury 5G sítě se zvýrazněním UDR"
---

UDR je centralizovaná funkce pro ukládání dat v 5G Core, která konsoliduje data účastníků, politiky a aplikací do jediného úložiště za účelem efektivní správy a přístupu síťovými funkcemi.

## Popis

Unified Data Repository (UDR) je klíčová komponenta v rámci architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 5G Core (5GC), definovaná standardy 3GPP. Funguje jako centralizovaná, standardizovaná entita pro ukládání strukturovaných dat, která odděluje ukládání dat od aplikační logiky. UDR ukládá různé datové profily, včetně dat o předplatném (používaných Unified Data Management, [UDM](/mobilnisite/slovnik/udm/)), dat politiky (používaných Policy Control Function, [PCF](/mobilnisite/slovnik/pcf/)), aplikačních dat (používaných Network Exposure Function, [NEF](/mobilnisite/slovnik/nef/)) a strukturovaných dat pro síťové řezy. Architektonicky UDR zpřístupňuje rozhraní směrem k vyšším vrstvám založené na službách (Nudr) využívající [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/), což umožňuje ostatním síťovým funkcím ([NF](/mobilnisite/slovnik/nf/)), jako jsou UDM, PCF a NEF, přistupovat k datům a spravovat je prostřednictvím standardizovaných [API](/mobilnisite/slovnik/api/) operací, jako jsou Nudr_DM (Správa dat) a Nudr_DR (Datové úložiště).

Interně UDR organizuje data do datových sad, což jsou kolekce dat určitého typu pro daného uživatele nebo službu. Například data o předplatném uživatele jsou uložena v konkrétní datové sadě. UDR zajišťuje konzistenci, integritu a dostupnost dat. Podporuje operace jako Vytvořit, Číst, Aktualizovat, Smazat a Dotaz (CRUDQ) nad těmito datovými sadami. Úložiště je navrženo jako vysoce škálovatelné a spolehlivé, často implementované s využitím distribuovaných databázových technologií, aby zvládlo obrovské objemy dat a požadavky na nízkou latenci v sítích 5G. Jeho role je čistě pro ukládání a vyhledávání; aplikační logika (např. rozhodnutí o autentizaci prováděná UDM) sídlí v konzumních síťových funkcích.

Implementace UDR umožňuje jasné oddělení mezi ukládáním dat a logikou jejich použití, což je klíčový princip architektury SBA 5GC. Toto oddělení umožňuje nezávislou škálovatelnost úložných a zpracovatelských funkcí, zjednodušuje aktualizace a podporuje inovace. Například UDM se může soustředit na logiku správy předplatného, zatímco pro trvalé ukládání spoléhá na UDR. UDR také podporuje síťové řezy ukládáním dat o předplatném a politikách specifických pro daný řez, což umožňuje různým řezům mít podle potřeby izolované nebo sdílené datové sady. Dále usnadňuje zpřístupňování dat autorizovaným aplikacím třetích stran prostřednictvím NEF, což umožňuje nové paradigma služeb.

## K čemu slouží

UDR byl vytvořen, aby řešil problémy fragmentace dat a izolovaného ukládání přítomné v předchozích generacích mobilních sítí, jako je 4G EPC. V EPC byla data často ukládána do vyhrazených, na funkci specifických úložišť (např. HSS pro předplatné, SPR pro politiky), což vedlo k duplikaci, nekonzistenci a složité integraci. Vize 5G vyžadovala agilnější, cloud-nativní a na služby orientované jádro sítě pro podporu různorodých případů užití od rozšířeného mobilního širokopásmového připojení přes hromadný IoT až po ultra-spolehlivou komunikaci s nízkou latencí.

UDR tyto problémy řeší tím, že poskytuje sjednocené, centralizované úložiště pro všechna strukturovaná data v 5GC. Tato konsolidace eliminuje redundanci dat, zajišťuje jediný zdroj pravdy a zjednodušuje operace správy dat. Přímo podporuje architekturu založenou na službách (SBA) 5GC tím, že nabízí standardizovanou službu ukládání dat, kterou může jakákoli autorizovaná síťová funkce konzumovat prostřednictvím API. Tento návrh je zásadní pro umožnění síťových řezů, protože každý řez může mít své vyhrazené datové profily uložené a spravované v rámci stejné infrastruktury UDR, což zajišťuje izolaci a efektivní využití zdrojů. UDR tak připravuje síť na budoucnost pro datově řízené služby a flexibilní nasazení služeb.

## Klíčové vlastnosti

- Centralizované úložiště pro strukturovaná data účastníků, politiky a aplikací
- Rozhraní založené na službách (Nudr) využívající HTTP/2 a JSON pro standardizovaný přístup
- Podpora více datových sad (např. pro předplatné, politiky, zpřístupnění)
- Odděluje ukládání dat od aplikační logiky konzumních síťových funkcí (NF), jako jsou UDM a PCF
- Umožňuje konzistenci dat a slouží jako jediný zdroj pravdy
- Usnadňuje síťové řezy prostřednictvím izolace a správy dat specifických pro daný řez

## Související pojmy

- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)

## Definující specifikace

- **TR 22.985** (Rel-19) — 3GPP User Data Convergence (UDC) concept
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.335** (Rel-19) — User Data Convergence (UDC) Procedures
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TS 23.862** (Rel-12) — Interworking Solutions for Mobile Operators & Data Apps
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TS 28.540** (Rel-20) — 5G Network Resource Model (NRM) Management
- **TR 28.840** (Rel-18) — Technical Report
- **TS 29.201** (Rel-19) — RESTful Rx Interface for AF-PC Communication
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- … a dalších 33 specifikací

---

📖 **Anglický originál a plná specifikace:** [UDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/udr/)
