---
slug: "nsi"
url: "/mobilnisite/slovnik/nsi/"
type: "slovnik"
title: "NSI – Network Slice Instance Identifier"
date: 2026-01-01
abbr: "NSI"
fullName: "Network Slice Instance Identifier"
category: "Network Slicing"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nsi/"
summary: "Jedinečný identifikátor pro instanci síťového řezu (NSI), což je nasazená sada síťových funkcí a prostředků poskytující kompletní logickou síť pro konkrétní typ služby nebo klienta. Je to klíčový iden"
---

NSI je jedinečný identifikátor pro nasazenou sadu síťových funkcí a prostředků, která poskytuje kompletní logickou síť pro konkrétní typ služby nebo klienta (tenanta) v systémech 5G.

## Popis

Identifikátor instance síťového řezu (NSI ID) je klíčovou součástí architektury síťového řezování 5G, definovanou ve specifikacích 5G systému. Instance síťového řezu je skutečná, instanciovaná logická síť, která poskytuje specifické síťové schopnosti a charakteristiky. NSI ID je jedinečný klíč používaný systémy správy (konkrétně funkcí správy síťových řezů ([NSMF](/mobilnisite/slovnik/nsmf/)) a funkcí správy komunikačních služeb (CSMF)) k identifikaci, správě a orchestraci konkrétní instance řezu po celý její životní cyklus – od vytvoření a aktivace přes modifikaci, dohled až po vyřazení. Identifikátor se používá v rámci roviny správy a orchestrace ([MANO](/mobilnisite/slovnik/mano/)), jak je definováno 3GPP a často integrováno s [ETSI](/mobilnisite/slovnik/etsi/) [NFV](/mobilnisite/slovnik/nfv/) MANO. Je odkazován v datech předplatného a výběru síťových řezů, což síti umožňuje asociovat UE se správným řezem. NSI ID se liší od [S-NSSAI](/mobilnisite/slovnik/s-nssai/) (informace pro pomoc při výběru jednoho síťového řezu), kterou používají UE a přístupová síť pro výběr řezu během registrace a zřizování relace. S-NSSAI odkazuje na typ síťového řezu a síť interně mapuje tuto žádost na konkrétní NSI pomocí NSI ID. NSI ID spojuje všechny virtualizované a fyzické prostředky – včetně funkcí jádra sítě (jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/)), komponent RAN a segmentů přenosové sítě – které společně realizují řez. Jeho jedinečnost je zásadní pro zajištění přísné izolace mezi řezy, přesného účtování, správy poruch a monitorování výkonu na řez.

## K čemu slouží

NSI ID byl zaveden se síťovým řezováním 5G, aby vyřešil problém správy více, izolovaných, logických sítí běžících na sdílené fyzické infrastruktuře. Před5G sítě byly z velké části monolitické, navržené pro univerzální model služeb (primárně mobilní širokopásmový přístup). Nástup různorodých případů užití – jako masivní IoT, ultra-spolehlivá komunikace s nízkou latencí (URLLC) a vylepšené mobilní širokopásmové připojení (eMBB) – vyžadoval schopnost vytvářet přizpůsobené sítě se specifickými výkonnostními, bezpečnostními a funkčními charakteristikami. Síťové řezování je architektonickou odpovědí, ale vyžaduje robustní systém identifikace a správy. NSI ID poskytuje základní úchop pro orchestraci a správu životního cyklu. Řeší omezení spočívající v neexistenci standardizovaného, síťově globálního identifikátoru pro sledování konkrétní instance řezu napříč všemi doménami správy (RAN, Transport, Jádro). To umožňuje automatizované zřizování řezů, granulární alokaci prostředků, nezávislý provoz a škálování řezů a správu specifickou pro klienta, což je zásadní pro vizi 5G podporovat vertikální odvětví a nové obchodní modely.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro konkrétní instanciovaný síťový řez.
- Používá se primárně v doméně správy a orchestrace (MANO) pro operace životního cyklu.
- Umožňuje mapování mezi požadavky na řez na úrovni služby (S-NSSAI) a nasazenou síťovou instancí.
- Zásadní pro izolaci prostředků, správu poruch a monitorování výkonu na řez.
- Odkazován v datech předplatného síťového řezu a v procedurách jeho výběru.
- Podporuje víceklientský provoz tím, že umožňuje různým klientům mít své vlastní identifikované instance řezů.

## Související pojmy

- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)
- [NSMF – Network Slice Management Function](/mobilnisite/slovnik/nsmf/)
- [NSSF – Network Slice Selection Function](/mobilnisite/slovnik/nssf/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.202** (Rel-19) — 5G Network Slice Management Charging
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.545** (Rel-17) — Fault Supervision for 5G Networks
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 28.801** (Rel-15) — Management and Orchestration of Network Slicing
- **TS 28.805** (Rel-16) — Management of Communication Services in 5G
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [NSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsi/)
