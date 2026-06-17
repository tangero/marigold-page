---
slug: "er"
url: "/mobilnisite/slovnik/er/"
type: "slovnik"
title: "ER – EAP Re-authentication"
date: 2026-01-01
abbr: "ER"
fullName: "EAP Re-authentication"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/er/"
summary: "ER je rozšíření bezpečnostního protokolu, které umožňuje efektivní opětovné ověření (re-authentication) uživatele nebo zařízení bez nutnosti provedení plné EAP autentizace. Snižuje signalizační režii"
---

ER je rozšíření bezpečnostního protokolu, které umožňuje efektivní opětovné ověření bez nutnosti plné EAP výměny, čímž snižuje signalizační režii a latenci pro rychlé předávání spojení a opětovná připojení v mobilních sítích.

## Popis

[EAP](/mobilnisite/slovnik/eap/) Re-authentication (ER) je mechanismus definovaný v rámci architektury Extensible Authentication Protocol (EAP), standardizovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý organizací 3GPP. Umožňuje žadateli (supplicant, např. UE) a autentizátoru (authenticator, např. síťovému přístupovému bodu) provést zjednodušené opětovné ověření založené na dříve navázaném kryptografickém materiálu z úplné EAP autentizace. Proces využívá EAP Re-authentication Protocol ([ERP](/mobilnisite/slovnik/erp/)) a používá odvozené klíče, jako je rRK (re-authentication Root Key) a rMSK (re-authentication Master Session Key), k zabezpečení výměny. Z architektonického hlediska se ER účastní EAP protistrana (peer), EAP autentizátor a EAP server, přičemž zprávy ERP jsou typicky přenášeny uvnitř zpráv EAP-Initiate a EAP-Finish. ER server, často umístěný společně s EAP serverem, spravuje stav opětovného ověření a klíčový materiál. Tento mechanismus je integrován do systémů 3GPP pro podporu plynulé mobility, zejména v přístupových sítích non-3GPP spolupracujících s 5G Core, a to minimalizací autentizační latence během předávání spojení. Funguje tak, že protistrana zahájí opětovné ověření zprávou EAP-Initiate/Re-auth-Start, což vede k vzájemné autentizaci a odvození klíčů bez nutnosti zapojení backendových autentizačních serverů pro úplné ověření přihlašovacích údajů. Mezi klíčové součásti patří hierarchie klíčů ERP, správa stavu na ER serveru a použití kryptograficky zabezpečených sekvenčních čísel k prevenci replay útoků. Jeho role je klíčová ve scénářích vyžadujících častou autentizaci, jako jsou hustá městská nasazení nebo zařízení IoT s omezeným výkonem, protože zajišťuje kontinuální zabezpečený přístup se sníženou signalizační zátěží prvků jádra sítě.

## K čemu slouží

ER byl vytvořen, aby řešil výkonnostní omezení úplných [EAP](/mobilnisite/slovnik/eap/) autentizačních procedur, které jsou výpočetně náročné a generují významný signalizační provoz. V mobilních sítích, zejména během předávání spojení mezi přístupovými body nebo opětovného připojení po krátkém přerušení, by provedení plné EAP výměny pokaždé zavedlo nepřijatelnou latenci a negativně ovlivnilo uživatelský komfort. Historicky, bez ER, vyžadovalo každé opětovné ověření komunikaci s domovským autentizačním serverem, což prodlužovalo dobu předání spojení a mohlo způsobit přerušení služby. Motivací byla potřeba rychlejších a efektivnějších bezpečnostních mechanismů v rozvíjejících se síťových architekturách, jako je integrace přístupu non-3GPP (např. Wi-Fi) v 3GPP, a požadavky služeb 5G s nízkou latencí. ER tyto problémy řeší tím, že umožňuje odlehčené opětovné ověření, které znovu využívá dříve navázanou důvěru, a snižuje tak časovou i zdrojovou náročnost. Řeší omezení dřívějších přístupů, kdy se často musela volit kompromisní řešení mezi bezpečností a efektivitou, a poskytuje standardizovanou metodu pro zachování robustní autentizace bez obětování výkonu, což je klíčové pro aplikace v reálném čase a masivní nasazení IoT.

## Klíčové vlastnosti

- Umožňuje rychlé opětovné ověření pomocí předem navázaných klíčů
- Snižuje signalizační režii a autentizační latenci
- Podporuje plynulá předání spojení v mobilních a non-3GPP přístupových sítích
- Využívá ERP pro zabezpečené odvozování a výměnu klíčů
- Integruje se s architekturou EAP a bezpečnostní architekturou 3GPP
- Zabraňuje replay útokům pomocí mechanismů sekvenčních čísel

## Související pojmy

- [EAP – Extensible Authentication Protocol](/mobilnisite/slovnik/eap/)

## Definující specifikace

- **TR 22.826** (Rel-17) — Study on 5G for Critical Medical Applications
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO

---

📖 **Anglický originál a plná specifikace:** [ER na 3GPP Explorer](https://3gpp-explorer.com/glossary/er/)
