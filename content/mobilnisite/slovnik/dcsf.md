---
slug: "dcsf"
url: "/mobilnisite/slovnik/dcsf/"
type: "slovnik"
title: "DCSF – Data Channel Server Control Function"
date: 2026-01-01
abbr: "DCSF"
fullName: "Data Channel Server Control Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dcsf/"
summary: "Řídicí funkce v architektuře Data Channel Server sítě 5G Core. Je zodpovědná za správu a řízení zřizování, modifikace a uvolňování datových kanálů pro komunikaci specifickou pro aplikace, zejména pro"
---

DCSF je řídicí funkce v rámci Data Channel Server v síti 5G Core, která spravuje zřizování, modifikaci a uvolňování datových kanálů pro komunikaci specifickou pro aplikace.

## Popis

Data Channel Server Control Function (DCSF) je řídicí funkce sítě 5G Core zavedená jako součást architektury Data Channel Server ([DCS](/mobilnisite/slovnik/dcs/)). Architektura DCS je navržena pro poskytnutí vylepšené podpory pro doručování dat s ohledem na aplikace, zejména pro služby s náročnými požadavky, jako je rozšířená realita (XR), cloudové hraní a interaktivní média v reálném čase. DCSF funguje jako centrální řídicí prvek v této architektuře. Rozhraní k Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) zprostředkovává rozhraní Ndcsf a k Data Channel Server User Plane Function (DCSU) rozhraní Ndcsu. Z provozního hlediska DCSF přijímá od SMF požadavky a politiky týkající se relací. Tyto požadavky jsou spouštěny na základě žádostí Application Function ([AF](/mobilnisite/slovnik/af/)) nebo politik [PCF](/mobilnisite/slovnik/pcf/), které identifikují potřebu datového kanálu specifického pro aplikaci. DCSF je zodpovědná za logické řízení těchto datových kanálů. Mezi její klíčové úkoly patří výběr vhodné instance DCSU na základě vytížení, umístění a schopností a následné pokynutí této DCSU k zřízení, modifikaci nebo uvolnění datového kanálu pro konkrétní PDU Session nebo skupinu UE. Datový kanál je vyhrazená komunikační cesta mezi DCSU a UE (přes [UPF](/mobilnisite/slovnik/upf/) a RAN), která může být optimalizována pro specifické vzorce provozu, jako jsou periodické toky s nízkou latencí pro XR video. DCSF spravuje životní cyklus těchto kanálů, včetně vynucování QoS, pravidel pro směrování provozu a případné agregace více mediálních streamů. Dále zajišťuje koordinaci pro scénáře multicastového/broadcastového doručování dat. Tato funkce pracuje ve spolupráci s DCSU, která provádí skutečné zpracování, přeposílání a adaptaci paketů v uživatelské rovině podle pravidel nastavených DCSF. Samotná DCSF nezpracovává uživatelská datová pakety. Její role je čistě řídicí: převádí požadavky aplikace (např. snímkovou frekvenci, rozpočet latence) na příkazy pro síťové prostředky. Je klíčovým prvkem pro zpřístupnění možností sítě, což umožňuje systému 5G dynamicky vytvářet datové cesty přizpůsobené potřebám aplikací v reálném čase, což přesahuje statický model QoS Flow základní 5G.

## K čemu slouží

DCSF byla vytvořena, aby řešila omezení standardního modelu QoS v 5G při zpracování složitých, dynamických aplikací, jako jsou XR a cloudové hraní. Zatímco 5G zavedlo QoS Flows, jejich konfigurace je relativně statická a spravovaná na úrovni PDU session. Pokročilé interaktivní služby vyžadují rychlé zřizování a rušení více současných datových toků s odlišnými a náročnými požadavky (např. oddělené kanály pro video, audio a haptickou zpětnou vazbu), často synchronizované a vyžadující přesné směrování provozu. Účelem DCSF je poskytnout vyhrazenou řídicí funkci, která může na základě žádosti dynamicky spravovat tyto datové kanály specifické pro aplikace. Řeší problém rigidního řízení QoS na úrovni relace zavedením jemnější a agilnější vrstvy řízení kanálů. Motivace vychází z požadavků průmyslu na síťovou podporu, která je hluboce obeznámena s kontextem aplikace. Díky existenci řídicí funkce (DCSF), která komunikuje se [SMF](/mobilnisite/slovnik/smf/) a [PCF](/mobilnisite/slovnik/pcf/), může síť reagovat na žádosti [AF](/mobilnisite/slovnik/af/) v reálném čase a vytvářet optimalizované datové cesty, které snižují latenci, kolísání latence (jitter) a zlepšují efektivitu využití prostředků pro náročné služby. Řeší tak omezení předchozího přístupu, kde by taková optimalizace vyžadovala složitou interakci AF-SMF a potenciálně pomalou rekonfiguraci celé PDU session. DCSF poskytuje standardizovanou, škálovatelnou řídicí rovinu pro architekturu Data Channel Server, což umožňuje nové služby generující příjmy s vylepšenou kvalitou uživatelského zážitku.

## Klíčové vlastnosti

- Řídicí funkce pro správu datových kanálů specifických pro aplikace
- Komunikuje se SMF (Ndcsf) a DCSU (Ndcsu) pro komplexní řízení
- Řídí zřizování, modifikaci a uvolňování datových kanálů
- Podporuje dynamickou správu kanálů pro služby s nízkou latencí, jako je XR
- Umožňuje směrování provozu a vynucování QoS pro optimalizované doručování médií
- Usnadňuje zpřístupnění možností sítě a síťování s ohledem na aplikace

## Související pojmy

- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [AF – Authentication Framework](/mobilnisite/slovnik/af/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.392** (Rel-19) — MMTel Application Enablement
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 26.264** (Rel-19) — IMS-based AR Real-Time Communication
- **TS 26.567** (Rel-19) — IMS-based Split Rendering
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TS 28.851** (Rel-19) — Charging for Next Gen Real Time Communication Phase 2
- **TS 29.175** (Rel-19) — IMS AS Service-Based Interface Protocol
- **TS 29.330** (Rel-19) — Diameter-based Sc Interface Specification
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.562** (Rel-19) — HSS Services for IMS & GBA Interworking
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [DCSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcsf/)
