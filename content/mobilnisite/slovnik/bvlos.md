---
slug: "bvlos"
url: "/mobilnisite/slovnik/bvlos/"
type: "slovnik"
title: "BVLOS – Beyond Visual Line of Sight"
date: 2025-01-01
abbr: "BVLOS"
fullName: "Beyond Visual Line of Sight"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bvlos/"
summary: "BVLOS (Beyond Visual Line of Sight) je služba umožňující bezpilotním letadlům (UAV) nebo dronům provoz mimo přímé vizuální pozorování pilotem s využitím sítí 3GPP pro přenos povelů, řízení a komunikac"
---

BVLOS je služba umožňující dronům provoz mimo přímé vizuální pozorování pilotem s využitím sítí 3GPP pro přenos povelů, řízení a komunikaci.

## Popis

BVLOS (Beyond Visual Line of Sight) je standardizovaná služba v 3GPP, která umožňuje provoz bezpilotních letadel ([UAV](/mobilnisite/slovnik/uav/)) mimo přímý vizuální dosah lidského operátora s využitím mobilních sítí pro konektivitu. Architektura integruje UAV jako uživatelské zařízení (UE) v ekosystému 3GPP a připojuje je k jádru sítě přes rádiovou přístupovou síť (RAN). Mezi klíčové komponenty patří UAV, řadič UAV ([UAV-C](/mobilnisite/slovnik/uav-c/)) a poskytovatel služeb UAV ([USS](/mobilnisite/slovnik/uss/)), které vzájemně komunikují přes definovaná rozhraní, jako je PC5 pro přímou komunikaci a Uu pro mobilní spojení. Jádrová síť 5G poskytuje nezbytné funkce, jako je autentizace, správa mobility a vynucování kvality služeb (QoS), což zajišťuje bezpečný a spolehlivý přenos dat pro povelové a řídicí ([C2](/mobilnisite/slovnik/c2/)) spoje, telemetrii a datové přenosy užitečného zatížení.

Při provozu se BVLOS spoléhá na síť 3GPP k navázání a udržení komunikace mezi UAV a její pozemní řídicí stanicí nebo vzdáleným pilotem. UAV využívá rozhraní Uu pro připojení ke gNodeB (gNB) v RAN, které směrují provoz přes jádrovou síť 5G k UAV-C nebo USS. Síťové segmenty (network slicing) se používají k vytvoření vyhrazených řezů se specifickými parametry QoS, jako je ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) pro kritická C2 data a vylepšené mobilní širokopásmové připojení (eMBB) pro aplikace s vysokou propustností, jako je streamování videa. To zajišťuje, že operace BVLOS splňují přísné požadavky na latenci, spolehlivost a propustnost, a to i v dynamickém leteckém prostředí.

Bezpečnost a správa jsou v BVLOS prvořadé, přičemž specifikace 3GPP řeší identifikaci, autentizaci a autorizaci UAV prostřednictvím mechanismů, jako je vzdálená identifikace UAV (Remote ID) a zabezpečená výměna klíčů. Služba podporuje mobilitu přes hranice buněk pomocí procedur předávání hovoru optimalizovaných pro leteckou mobilitu, včetně výběru buňky na základě nadmořské výšky a omezení interference. Dále BVLOS zahrnuje funkce pro prevenci kolizí a správu vzdušného prostoru, rozhraní s externími systémy, jako je systém řízení provozu bezpilotních letadel ([UTM](/mobilnisite/slovnik/utm/)), pro koordinaci letových drah a zajištění souladu s předpisy. Tento komplexní rámec umožňuje škálovatelné, bezpečné a efektivní operace dronů v různých případech použití, od logistiky po veřejnou bezpečnost.

## K čemu slouží

BVLOS byl zaveden, aby řešil rostoucí poptávku po komerčních a průmyslových aplikacích dronů, které vyžadují provoz mimo vizuální dosah pilota, což bylo dříve omezeno regulačními a technologickými překážkami. Tradiční operace dronů se spoléhaly na krátkodosahové rádiové spoje (např. Wi-Fi nebo proprietární protokoly) s omezeným dosahem a spolehlivostí, což bránilo škálovatelnosti pro úkoly, jako je dálková přeprava, inspekce infrastruktury a zemědělský monitoring. Motivací pro BVLOS v 3GPP byla potřeba využít všudypřítomné mobilní sítě – zejména 5G – k poskytnutí plošného, bezpečného a výkonného připojení, což umožňuje autonomním a dálkově řízeným [UAV](/mobilnisite/slovnik/uav/) bezpečně provozovat v řízeném vzdušném prostoru.

Historicky čelily operace BVLOS výzvám, jako je rušení signálu, problémy s latencí a nedostatek standardizovaných komunikačních protokolů, což zvyšovalo riziko nehod a nedodržování předpisů. Normalizační snahy 3GPP, počínaje vydáním 17, měly za cíl překonat tato omezení integrací UAV do mobilního ekosystému a nabídnout vylepšené schopnosti, jako jsou síťové segmenty (network slicing), edge computing a přesné určování polohy. To umožňuje výměnu dat v reálném čase, dynamické plánování tras a soulad s požadavky leteckých úřadů, jako jsou Federální úřad pro letectví (FAA) nebo Agentura Evropské unie pro bezpečnost letectví (EASA). Řešením těchto problémů BVLOS otevírá nové ekonomické příležitosti a zlepšuje provozní efektivitu v odvětvích, jako je logistika, energetika a záchranné služby.

## Klíčové vlastnosti

- Podpora komunikace pro povely a řízení (C2) UAV přes sítě 3GPP
- Integrace se systémem řízení provozu bezpilotních letadel (UTM) pro koordinaci vzdušného prostoru
- Síťové segmenty (network slicing) pro vyhrazené profily QoS (např. URLLC pro spoje C2 s nízkou latencí)
- Vzdálená identifikace UAV (Remote ID) pro bezpečnost a soulad s předpisy
- Správa mobility optimalizovaná pro letadla, včetně předávání hovoru a řešení interference
- Bezpečné mechanismy autentizace a autorizace pro UAV a jejich řadiče

## Související pojmy

- [UAV – Uncrewed Aerial Vehicle](/mobilnisite/slovnik/uav/)
- [UTM – Uncrewed Aerial System Traffic Management](/mobilnisite/slovnik/utm/)

## Definující specifikace

- **TS 22.125** (Rel-19) — UAS Requirements via 3GPP System
- **TR 22.843** (Rel-19) — Study on Uncrewed Aerial Vehicle (UAV) Phase 3
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TR 23.755** (Rel-17) — Study on app layer support for UAS
- **TS 29.256** (Rel-19) — UAS-NF Stage 3 Protocol Specification
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)

---

📖 **Anglický originál a plná specifikace:** [BVLOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bvlos/)
