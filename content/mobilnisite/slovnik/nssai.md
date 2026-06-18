---
slug: "nssai"
url: "/mobilnisite/slovnik/nssai/"
type: "slovnik"
title: "NSSAI – Network Slice Selection Assistance Information"
date: 2026-01-01
abbr: "NSSAI"
fullName: "Network Slice Selection Assistance Information"
category: "Network Slicing"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nssai/"
summary: "NSSAI je klíčový parametr v 5G, který identifikuje síťové řezy, jež chce uživatelské zařízení (UE) používat. Skládá se z jednoho nebo více S-NSSAIs, z nichž každý jednoznačně identifikuje jeden řez. S"
---

NSSAI je parametr 3GPP, který identifikuje sadu síťových řezů požadovaných uživatelským zařízením (UE) a sestává z jednoho nebo více S-NSSAIs. Síť tento parametr používá k nasměrování spojení k příslušným funkcím podporujícím daný řez.

## Popis

Network Slice Selection Assistance Information (NSSAI) je základní koncept a datová struktura v architektuře 5G System (5GS), zavedená ve specifikaci 3GPP Release 15. Jedná se o mechanismus, kterým uživatelské zařízení (UE) komunikuje síti své požadované síťové řezy během procedur registrace a zřizování relace. NSSAI není jediný identifikátor, ale kolekce, která typicky obsahuje jeden nebo více prvků Single Network Slice Selection Assistance Information ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)). Každý S-NSSAI je jedinečný identifikátor konkrétní instance síťového řezu nebo typu řezu, ke kterému má UE povolen přístup.

Samotný S-NSSAI se skládá ze dvou částí: Slice/Service Type ([SST](/mobilnisite/slovnik/sst/)) a volitelného Slice Differentiator ([SD](/mobilnisite/slovnik/sd/)). SST je povinné 8bitové pole, které udává očekávané chování síťového řezu z hlediska funkcí a služeb (např. enhanced Mobile Broadband - eMBB, Ultra-Reliable Low Latency Communications - [URLLC](/mobilnisite/slovnik/urllc/), Massive IoT - MIoT). SD je volitelné 24bitové pole používané k rozlišení mezi více instancemi síťových řezů stejného SST, což umožňuje operátorovi nasadit několik řezů pro stejný typ služby, ale pro různé zákazníky nebo případy užití. UE získává S-NSSAIs, které smí používat, ze svého profilu předplatného, který je často konfigurován domovským operátorem.

Během úvodní registrační procedury UE zahrne Requested NSSAI (požadované NSSAI) do zprávy Registration Request odeslané funkci Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) přes (R)[AN](/mobilnisite/slovnik/an/). Requested NSSAI obsahuje S-NSSAIs, pro které se chce UE v aktuální registrační oblasti zaregistrovat. AMF ve spolupráci s Network Slice Selection Function ([NSSF](/mobilnisite/slovnik/nssf/)) a daty předplatného z Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) tyto požadavky ověří. Síť poté odpoví s Allowed NSSAI (povolené NSSAI), což je sada S-NSSAIs, které smí UE v aktuální registrační oblasti používat. UE si toto Allowed NSSAI uloží a do následných žádostí o registraci a zřizování PDU relace zahrne jeho podmnožinu nazvanou Configured NSSAI (nakonfigurované NSSAI) pro obsluhující veřejnou pozemní mobilní síť (PLMN). Tento proces zajišťuje, že je UE připojeno ke správným instancím AMF a Session Management Function (SMF), které podporují požadované řezy, čímž umožňuje přizpůsobené připojení a alokaci zdrojů, které definují síťové řezy.

## K čemu slouží

NSSAI bylo vytvořeno k vyřešení kritického problému výběru řezu a směrování v 5G síti, kde na sdílené fyzické infrastruktuře koexistuje více logických sítí (řezů). V systémech před 5G se UE jednoduše připojilo k "síti". Se síťovými řezy může UE potřebovat přístup k několika odlišným logickým sítím současně – například jedné pro běžné prohlížení internetu (eMBB), jedné pro podnikovou VPN a jedné pro službu hraní her s nízkou latencí. Síť potřebovala standardizovaný způsob, jakým může UE signalizovat, kterou z těchto logických sítí pro daný komunikační kontext vyžaduje.

Mechanismus NSSAI toto signalizování poskytuje. Řeší omezení dřívějších sítí, kterým chyběl nativní, standardizovaný identifikátor pro síťové oddíly specifické pro službu. Bez NSSAI by implementace řezů vyžadovala nestandardní, proprietární signalizaci nebo neefektivní nadstavbová řešení. NSSAI umožňuje efektivní využití síťových zdrojů tím, že umožňuje (R)AN a páteřní síti směrovat provoz ke konkrétní sadě síťových funkcí (AMF, SMF, UPF atd.) vytvořených pro daný řez. To je zásadní pro splnění různých klíčových výkonnostních ukazatelů (KPI) různých služeb, protože zajišťuje, že datová a řídicí rovina UE jsou zpracovávány funkcemi nakonfigurovanými s příslušnými politikami (např. latence, šířka pásma, zabezpečení). Jeho zavedení bylo klíčovým kamenem pro uskutečnění vize 5G o přizpůsobených logických sítích v praxi.

## Klíčové vlastnosti

- Skládá se ze sady prvků S-NSSAI, z nichž každý identifikuje síťový řez
- S-NSSAI zahrnuje povinný Slice/Service Type (SST) a volitelný Slice Differentiator (SD)
- Přenáší se v klíčových NAS zprávách, jako je Registration Request a PDU Session Establishment Request
- Zahrnuje Requested NSSAI (od UE), Allowed NSSAI (od sítě) a Configured NSSAI (uložené v UE)
- Používá se (R)AN pro směrování k příslušné AMF během počátečního přístupu
- Umožňuje síti vybrat instance páteřních síťových funkcí (SMF, UPF) specifické pro daný řez

## Související pojmy

- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [NSSF – Network Slice Selection Function](/mobilnisite/slovnik/nssf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [SST – Spectral Smoothing Technique](/mobilnisite/slovnik/sst/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TS 28.202** (Rel-19) — 5G Network Slice Management Charging
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.801** (Rel-15) — Management and Orchestration of Network Slicing
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [NSSAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nssai/)
