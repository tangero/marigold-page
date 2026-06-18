---
slug: "lrf"
url: "/mobilnisite/slovnik/lrf/"
type: "slovnik"
title: "LRF – Location Retrieval Function"
date: 2026-01-01
abbr: "LRF"
fullName: "Location Retrieval Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lrf/"
summary: "Location Retrieval Function (LRF) je prvek jádra sítě v IP Multimedia Subsystem (IMS). Poskytuje informace o poloze uživatelského zařízení (UE) autorizovaným entitám, primárně pro tísňové služby (E911"
---

LRF je prvek jádra IMS sítě, který poskytuje informace o poloze uživatelského zařízení autorizovaným entitám, primárně pro tísňové služby, prostřednictvím interakce s funkcemi pro určení polohy v přístupové síti a databázemi účastníků.

## Popis

Location Retrieval Function (LRF) je klíčová funkční entita v architektuře IP Multimedia Subsystem (IMS) podle 3GPP, definovaná v několika specifikacích včetně TS 23.167 (tísňové relace IMS) a TS 23.271 (služby určení polohy). Architektonicky se LRF nachází v domovské IMS síti nebo ve visited síti a propojuje se s několika dalšími síťovými uzly. Její primární role je fungovat jako lokační server a brána pro získání a poskytnutí geografické polohy uživatelského zařízení (UE) autorizovaným aplikačním funkcím ([AF](/mobilnisite/slovnik/af/)), především Emergency Call Session Control Function ([E-CSCF](/mobilnisite/slovnik/e-cscf/)) během tísňové relace IMS.

LRF funguje prostřednictvím řady standardizovaných rozhraní a procedur. Když je prostřednictvím IMS zahájeno tísňové volání, E-CSCF požádá LRF o polohu volajícího. LRF pak orchestruje získání této informace o poloze. Může získat polohu přímo od UE, pokud toto podporuje hlášení polohy, nebo častěji komunikuje s infrastrukturou pro určení polohy v podkladové přístupové síti. Pro 3GPP přístup (jako LTE nebo 5G NR) to zahrnuje komunikaci s Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) přes rozhraní Le. LRF může také dotazovat Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Subscription Locator Function ([SLF](/mobilnisite/slovnik/slf/)), aby určila, který GMLC obsluhuje daného uživatele.

Jakmile je poloha získána (buď jako občanská adresa, nebo geodetické souřadnice), LRF ji naformátuje podle požadovaného protokolu (např. pomocí Presence Information Data Format - Location Object ([PIDF-LO](/mobilnisite/slovnik/pidf-lo/))) a doručí ji žadateli. Kromě tísňových služeb může LRF podporovat i další služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)), jak je definováno operátorem. Klíčové komponenty LRF zahrnují její servisní logiku pro zpracování požadavků na polohu, její rozhraní (Le směrem k GMLC, Ml směrem k E-CSCF atd.) a její integraci s IMS směrováním a databázemi účastníků. Její funkce je nepostradatelná pro splnění regulatorních požadavků na poskytnutí polohy tísňového volajícího (jako E911 v USA) v plně IP sítích IMS.

## K čemu slouží

LRF byla vytvořena k vyřešení problému poskytování přesné polohy volajícího v IP telefonních sítích, konkrétně v IMS, kterým chyběly inherentní možnosti určení polohy tradičních mobilních sítí s komutací okruhů. U legacy hovorů s komutací okruhů v sítích GSM/UMTS mohlo být ID buňky snadno předáno síti tísňových služeb. S migrací na plně IP jádrové sítě a oddělením servisní vrstvy (IMS) od přístupových sítí byl zapotřebí nový, standardizovaný mechanismus pro dotazování a získání polohy UE bez ohledu na její přístupovou technologii (3GPP, non-3GPP jako WiFi).

Hnací motivací byly regulatorní požadavky: vlády po celém světě nařizují, že tísňové služby musí obdržet polohu volajícího. LRF poskytuje standardizovanou, na přístupu nezávislou funkci v architektuře IMS, která tento požadavek splňuje. Řeší omezení dřívějších proprietárních nebo na přístupu závislých řešení definováním jednotného rozhraní (Ml) z jádra IMS k dedikovanému systému pro získání polohy. To umožňuje bezproblémovou funkčnost tísňových služeb napříč heterogenními přístupovými sítěmi a různými možnostmi zařízení a zajišťuje budoucí kompatibilitu rámce IMS pro tísňová volání s nástupem nových radiových technologií.

## Klíčové vlastnosti

- Komunikuje s E-CSCF přes rozhraní Ml pro přijímání požadavků na tísňovou polohu
- Získává polohu UE prostřednictvím interakce s GMLC přes rozhraní Le pro 3GPP přístup
- Podporuje jak síťově založené, tak UE asistované metody určení polohy
- Formátuje informace o poloze do standardního PIDF-LO pro signalizaci v IMS
- Umí dotazovat HSS/SLF pro směrování požadavků na polohu ke správnému GMLC
- Poskytuje polohu pro tísňové relace IMS a další autorizované služby založené na poloze

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [E-CSCF – Emergency – Call Session Control Function](/mobilnisite/slovnik/e-cscf/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [PIDF-LO – Presence Information Data Format Location Object](/mobilnisite/slovnik/pidf-lo/)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles

---

📖 **Anglický originál a plná specifikace:** [LRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lrf/)
