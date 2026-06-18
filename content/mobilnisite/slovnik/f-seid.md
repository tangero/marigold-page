---
slug: "f-seid"
url: "/mobilnisite/slovnik/f-seid/"
type: "slovnik"
title: "F-SEID – Fully Qualified Session Endpoint Identifier"
date: 2025-01-01
abbr: "F-SEID"
fullName: "Fully Qualified Session Endpoint Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/f-seid/"
summary: "Globálně jednoznačný identifikátor koncového bodu relace v síti 5G Core, který kombinuje identifikátor koncového bodu relace (SEID) s IP adresou uzlu. Umožňuje přesné směrování a správu relací napříč"
---

F-SEID je globálně jednoznačný identifikátor v 5G Core, který kombinuje identifikátor koncového bodu relace (Session Endpoint Identifier) s IP adresou uzlu, a tím umožňuje přesné směrování a správu relací napříč distribuovanými síťovými funkcemi.

## Popis

Plně kvalifikovaný identifikátor koncového bodu relace (F-SEID) je klíčová datová struktura definovaná v architektuře založené na službách ([SBA](/mobilnisite/slovnik/sba/)) sítě 5G Core. Slouží jako globálně jednoznačná adresa pro specifický koncový bod relace, například pro [PDU](/mobilnisite/slovnik/pdu/) relaci ukotvenou u funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) nebo u funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)). F-SEID je vytvořen spojením dvou hlavních komponent: identifikátoru koncového bodu relace ([SEID](/mobilnisite/slovnik/seid/)) a IP adresy síťové funkce hostující tento koncový bod. SEID sám o sobě je lokálně významný identifikátor přiřazený síťovou funkcí, ale v kombinaci s IP adresou uzlu se stává globálně jednoznačným v rámci celé sítě. Tato složená struktura je zásadní pro rozhraní založená na službách využívající [HTTP](/mobilnisite/slovnik/http/)/2 (např. N4, N7) mezi funkcemi řídicí roviny, jako je SMF a UPF.

Architektonicky se F-SEID používá v kontextu relace protokolu [PFCP](/mobilnisite/slovnik/pfcp/) (Packet Forwarding Control Protocol), zejména na rozhraní N4 mezi SMF (řídicí rovina) a UPF (uživatelská rovina). Když SMF zřizuje PDU relaci, vytvoří PFCP relaci a přiřadí F-SEID pro koncový bod této relace na UPF. Tento F-SEID je pak použit ve všech následných PFCP zprávách (např. pro zřízení, modifikaci nebo zrušení relace), aby jednoznačně identifikoval relaci a konkrétní instanci UPF, která ji obsluhuje. Komponenta IP adresy zajišťuje, že zprávy jsou správně směrovány na fyzickou nebo virtualizovanou instanci síťové funkce, a to i v cloud-nativním, distribuovaném nasazení, kde může existovat více instancí UPF.

Role F-SEID přesahuje pouhou identifikaci; je nedílnou součástí správy relací, mobility a síťových segmentů (network slicing). Při událostech mobility, jako je předání spojení (handover), může SMF potřebovat přesměrovat provoz aktualizací F-SEID tak, aby ukazoval na jinou UPF. U síťových segmentů pomáhá F-SEID asociovat relaci s konkrétní instancí segmentu, protože UPF může být specifická pro daný segment. Identifikátor také podporuje pokročilé funkce, jako jsou režimy kontinuity relace a služby ([SSC](/mobilnisite/slovnik/ssc/)), kde se může změnit bod ukotvení PDU relace (a tedy i F-SEID). Jeho návrh je v souladu s principem oddělení řídicí a uživatelské roviny v 5G Core a umožňuje flexibilní škálování a nasazování prostředků uživatelské roviny.

## K čemu slouží

F-SEID byl zaveden, aby řešil potřebu jednoznačné identifikace koncového bodu relace v distribuované, cloud-nativní architektuře 5G Core. Předchozí architektury 4G EPC používaly identifikátory jako plně kvalifikovaný TEID (F-TEID) na rozhraních založených na GTP, ty však byly vázány na protokol GPRS Tunnelling Protocol. S přechodem 5G na architekturu založenou na službách (SBA) a zavedením nových protokolů, jako je PFCP pro rozhraní N4, byl vyžadován nový mechanismus identifikace. F-SEID poskytuje standardizovaný způsob, jak jednoznačně identifikovat koncový bod relace napříč potenciálně mnoha geograficky rozptýlenými instancemi síťových funkcí, čímž řeší problém směrování a správy relací v dekomponované síti.

Jeho vytvoření bylo motivováno omezeními dřívějších identifikátorů, které nebyly plně kvalifikované nebo byly vázané na konkrétní protokol. V monolitické síti mohly lokálně významné identifikátory stačit, ale v 5G Core založeném na mikroslužbách potřebují funkce řídicí roviny (jako SMF) komunikovat s konkrétními instancemi uživatelské roviny (UPF) bez nejednoznačnosti. F-SEID zajišťuje, že i když více instancí UPF používá stejnou hodnotu lokálního SEID, kombinace s IP adresou zabrání kolizím. To je klíčové pro automatizaci, orchestraci a izolaci chyb, protože umožňuje síťovým operátorům přesně určit, kde je relace ukotvena. F-SEID tak podporuje cíle 5G v oblasti škálovatelnosti, odolnosti a diferenciace služeb, včetně síťových segmentů (network slicing) a edge computingu.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor kombinující SEID a IP adresu
- Klíčový pro správu PFCP relací na rozhraní N4
- Umožňuje přesné směrování na distribuované instance UPF
- Podporuje síťové segmenty (network slicing) asociací relací s UPF specifickými pro daný segment
- Usnadňuje mobilitu relací a přesun bodu ukotvení (anchor relocation)
- Soulad s principy architektury 5G založené na službách (SBA)

## Související pojmy

- [SEID – Session Endpoint Identifier](/mobilnisite/slovnik/seid/)
- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [F-TEID – Fully Qualified Tunnel Endpoint Identifier](/mobilnisite/slovnik/f-teid/)

## Definující specifikace

- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [F-SEID na 3GPP Explorer](https://3gpp-explorer.com/glossary/f-seid/)
