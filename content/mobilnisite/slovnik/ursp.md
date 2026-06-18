---
slug: "ursp"
url: "/mobilnisite/slovnik/ursp/"
type: "slovnik"
title: "URSP – UE Route Selection Policy"
date: 2026-01-01
abbr: "URSP"
fullName: "UE Route Selection Policy"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ursp/"
summary: "Soubor pravidel poskytovaných 5G jádrem sítě uživatelskému zařízení (UE), který určuje, jak má UE směrovat různé aplikační toky dat. Umožňuje inteligentní, současné připojení k více datovým sítím (DNN"
---

URSP je soubor pravidel z 5G jádra sítě, který uživatelskému zařízení (UE) určuje, jak směrovat různé aplikační toky dat do více datových sítí a síťových řezů.

## Popis

UE Route Selection Policy (URSP, politika výběru trasy uživatelského zařízení) je klíčovým prvkem schopnosti 5G systému podporovat rozmanité služby s velmi odlišnými požadavky prostřednictvím síťových řezů a souběžného přístupu k více datovým sítím. Je to strukturovaná politika definovaná v 3GPP TS 23.503, kterou funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) poskytuje uživatelskému zařízení (UE) prostřednictvím funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)). URSP se skládá z prioritního seznamu pravidel URSP. Každé pravidlo obsahuje dvě hlavní složky: popisovač provozu a seznam popisovačů výběru trasy ([RSD](/mobilnisite/slovnik/rsd/)). Popisovač provozu definuje množinu aplikačního provozu, na kterou se pravidlo vztahuje. Může používat kritéria jako cílové adresy/předpony internetového protokolu (IP), čísla portů, identifikátory protokolů, dotazy [DNS](/mobilnisite/slovnik/dns/) nebo, což je nejdůležitější, identifikátor OS/aplikace, který přímo identifikuje konkrétní aplikaci na UE. Popisovač(e) výběru trasy pak definují síťové zdroje, které mají být pro odpovídající provoz použity. Jeden RSD může specifikovat kombinaci názvu datové sítě ([DNN](/mobilnisite/slovnik/dnn/)), pomocné informace pro výběr jednoho síťového řezu ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)) a režimu kontinuity relace a služby ([SSC](/mobilnisite/slovnik/ssc/)). Operační systém UE nebo funkce vynucování politik vyhodnocuje tato pravidla v pořadí podle priority pro každý nový aplikační tok nebo soketové spojení. Když dojde k shodě, UE použije informace v RSD k vytvoření relace [PDU](/mobilnisite/slovnik/pdu/) s příslušným DNN a síťovým řezem nebo ke směrování provozu přes existující odpovídající relaci PDU. To umožňuje, aby jedno UE mělo více aktivních relací PDU – například jednu pro rozšířené mobilní širokopásmové připojení (eMBB) k veřejnému internetovému DNN a další pro ultra-spolehlivou komunikaci s nízkou latencí (URLLC) k privátnímu průmyslovému síťovému řezu – přičemž aplikace jsou automaticky mapovány na správnou relaci. Mechanismus URSP přesouvá významnou inteligenci na UE, což umožňuje dynamický, na aplikaci citlivý výběr síťových zdrojů bez nutnosti neustálého zásahu sítě pro každý tok.

## K čemu slouží

URSP byla vytvořena, aby řešila zásadní výzvu efektivní podpory 5G vize jedné síťové infrastruktury sloužící masivně rozmanitým případům užití, od širokopásmového připojení přes IoT až po kritickou komunikaci. Před-5G sítě primárně spojovaly UE s jediným výchozím datovým připojením (připojením PDN v 4G). I když nějaká forma vyhrazených nosičů mohla poskytovat různou kvalitu služeb (QoS), výběr byl řízen sítí a omezeného rozsahu, bez hluboké znalosti aplikací. URSP to řeší poskytnutím flexibilního, programovatelného rámce politik, který umožňuje síťovému operátorovi instruovat UE, jak mapovat své nesčetné aplikace na příslušné síťové řezy a datové sítě. To umožňuje současnou konektivitu k více logickým sítím, optimální využití zdrojů a bezproblémový uživatelský zážitek, kdy například telematika vozidla využívá řez s nízkou latencí, zatímco jeho infotainment využívá řez s vysokou propustností. Motivací byla potřeba automatizace a škálovatelnosti; ruční konfigurace každé aplikace na UE nebo mikrořízení každého toku sítí je nepraktické. URSP umožňuje UE činit inteligentní lokální rozhodnutí o směrování na základě politik definovaných operátorem, což je zásadní pro naplnění plného ekonomického a technického potenciálu síťových řezů a architektury 5G založené na službách.

## Klíčové vlastnosti

- Umožňuje mapování aplikací na síťové řezy na základě politiky operátora
- Podporuje více souběžných relací PDU k různým DNN/S-NSSAI
- Používá popisovače provozu včetně identifikátoru OS/aplikace, IP deskriptorů a doménových jmen
- Obsahuje prioritní seznam pravidel URSP vyhodnocovaných UE
- Dynamicky poskytována PCF k UE prostřednictvím AMF
- Usnadňuje efektivní využití síťových řezů a zdrojů edge computingu

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)

## Definující specifikace

- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 23.791** (Rel-16) — NWDAF Data Collection & Analytics Framework
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [URSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ursp/)
