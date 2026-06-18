---
slug: "s8hr"
url: "/mobilnisite/slovnik/s8hr/"
type: "slovnik"
title: "S8HR – S8 Home Routing"
date: 2025-01-01
abbr: "S8HR"
fullName: "S8 Home Routing"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/s8hr/"
summary: "S8 Home Routing je architektonický model pro roaming v 5G, kde je spojení uživatelské roviny (S8-U) směrováno přímo z UPF navštívené PLMN na UPF domácí PLMN, zatímco řídicí signalizace (S8-C) prochází"
---

S8HR je roamingová architektura 3GPP pro 5G, ve které jsou uživatelská data směrována přímo z navštívené do domácí sítě na UPF, zatímco řídicí signalizace prochází přes domácí síť za účelem konzistentních služeb a vynucení politik.

## Popis

S8 Home Routing (S8HR) je roamingová architektura 5G systému (5GS) definovaná standardem 3GPP. Popisuje, jak se uživatelské zařízení (UE) roamující ve veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)) připojuje k jádru 5G sítě (5GC) své domácí veřejné pozemní mobilní sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)). Model je pojmenován podle rozhraní S8, což je referenční bod mezi [PLMN](/mobilnisite/slovnik/plmn/) sítěmi VPLMN a HPLMN. Pro S8HR je charakteristické domácí směrování provozu uživatelské roviny.

V této architektuře je signalizace řídicí roviny (konkrétně rozhraní N16 mezi [SMF](/mobilnisite/slovnik/smf/) VPLMN a SMF HPLMN, které odpovídá referenčnímu bodu S8-C) směrována zpět do domácí sítě. To umožňuje HPLMN udržovat kontrolu nad politikami, účtováním a daty předplatného. Zásadní je, že cesta uživatelské roviny je také směrována do domácí sítě. UE naváže [PDU](/mobilnisite/slovnik/pdu/) sezení zakotvené na [UPF](/mobilnisite/slovnik/upf/) (User Plane Function) ve VPLMN. Tento UPF VPLMN se následně připojí přes rozhraní S8-U (pomocí protokolu referenčního bodu N9) k UPF v HPLMN. Veškerý datový provoz uživatele je veden přes tento domácí UPF před dosažením externí datové sítě ([DN](/mobilnisite/slovnik/dn/)).

To je v kontrastu s roamingovým modelem Local Breakout ([LBO](/mobilnisite/slovnik/lbo/)), kde se uživatelská rovina připojuje k internetu přímo z VPLMN. S8HR zajišťuje, že domácí operátor může aplikovat konzistentní servisní politiky, provádět hlubokou kontrolu paketů, implementovat pravidla účtování a poskytovat hodnotově přidané služby (jako firewally nebo rodičovské kontroly) z domácí sítě, bez ohledu na polohu UE. Architektura se spoléhá na bezpečnostní mechanismy jako IPsec nebo TLS na rozhraní S8 a vyžaduje meziodběratelské dohody pro propojení N16 (S8-C) a N9 (S8-U).

## K čemu slouží

S8 Home Routing byl zaveden, aby poskytl standardizovanou, bezpečnou a na politiky založenou roamingovou architekturu pro 5G sítě. Před jeho formalizací v 5G existovaly podobné koncepty v roamingu 4G/EPC (S8 Home Routing). Vývoj směrem k 5G vyžadoval novou definici sladěnou se službami založenou architekturou (SBA) a oddělením řídicí roviny (SMF) a uživatelské roviny (UPF).

Řeší problém, jak umožnit roamujícímu účastníkovi přístup ke službám, a zároveň zajistit, že domácí operátor si zachová kontrolu nad uživatelským zážitkem ze služeb, účtováním a bezpečnostními politikami. V globálně propojeném ekosystému potřebují operátoři spolehlivou metodu, jak nabízet konzistentní služby svým účastníkům v zahraničí a zajistit, aby byl příjem z roamingu správně účtován. S8HR řeší omezení méně kontrolovaných breakout modelů tím, že garantuje průchod provozu přes body vynucení politik v domácí síti.

## Klíčové vlastnosti

- Domácí směrování provozu uživatelské roviny přes rozhraní S8-U (N9)
- Kontrola domácí sítě nad politikami a účtováním přes rozhraní S8-C (N16)
- Umožňuje konzistentní aplikaci služeb HPLMN pro roamující uživatele
- Vyžaduje bezpečnostní asociace mezi PLMN (např. IPsec)
- Podporuje jak 3GPP, tak i ne-3GPP typy přístupu pro roamující UE
- Kotví řízení PDU sezení v SMF HPLMN

## Související pojmy

- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TR 23.749** (Rel-14) — Study on S8 Home Routing for VoLTE
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.827** (Rel-14) — LI for S8 Home Routed VoLTE Roaming

---

📖 **Anglický originál a plná specifikace:** [S8HR na 3GPP Explorer](https://3gpp-explorer.com/glossary/s8hr/)
