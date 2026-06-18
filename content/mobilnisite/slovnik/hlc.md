---
slug: "hlc"
url: "/mobilnisite/slovnik/hlc/"
type: "slovnik"
title: "HLC – Higher Level Control functions"
date: 2025-01-01
abbr: "HLC"
fullName: "Higher Level Control functions"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hlc/"
summary: "HLC označuje funkce vyšší úrovně řízení v sítích 3GPP, které zahrnují schopnosti správy a orchestrace síťových prostředků, služeb a politik. Operuje nad fyzickou vrstvou a umožňuje efektivní síťový pr"
---

HLC je soubor funkcí vyšší úrovně řízení pro správu a orchestraci síťových prostředků, služeb a politik za účelem umožnění efektivního, automatizovaného provozu a poskytování služeb napříč více doménami.

## Popis

Funkce vyšší úrovně řízení (Higher Level Control, HLC) v systémech 3GPP představují soubor mechanismů správy a řízení, které dohlížejí a koordinují síťové operace na abstraktní úrovni, nad rámec bezprostředního řízení fyzické nebo spojové vrstvy. Tyto funkce jsou typicky implementovány v systémech správy sítě ([NMS](/mobilnisite/slovnik/nms/)), systémech správy prvků ([EMS](/mobilnisite/slovnik/ems/)) nebo orchestračních platformách, jako je orchestrátor virtualizace síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)). HLC zahrnuje činnosti jako správa životního cyklu služeb, vynucování politik, správa poruch, správa konfigurace a monitorování výkonu napříč základní sítí (CN) a rádiovou přístupovou sítí (RAN).

Architektonicky funkce HLC interagují s řídicími rovinami nižší úrovně (např. řídicí rovinou v jádru 5G) a s uživatelskými rovinami prostřednictvím standardizovaných rozhraní, jako jsou ta definovaná v řadách 3GPP TS 28 a TS 32 pro správu. Mezi klíčové komponenty patří funkce správy síťových řezů ([NSMF](/mobilnisite/slovnik/nsmf/)) pro správu síťových řezů, funkce analýzy síťových dat ([NWDAF](/mobilnisite/slovnik/nwdaf/)) pro daty řízené poznatky a funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) pro rozhodování o politikách. HLC funguje tak, že shromažďuje telemetrická data ze síťových prvků, aplikuje algoritmy nebo pravidla pro optimalizaci alokace prostředků a vydává příkazy pro dynamickou rekonfiguraci sítě – například škálování virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) nebo úpravu parametrů QoS.

Role HLC je klíčová pro dosažení automatizace, škálovatelnosti a přizpůsobivosti sítě v moderních nasazeních 3GPP, zejména s nástupem 5G a síťových řezů. Operátorům umožňuje rychle nasazovat služby, zajišťovat efektivní využití infrastruktury a dodržovat smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)). Díky abstrakci složitosti HLC usnadňuje interoperabilitu mezi více dodavateli a podporuje nové paradigmaty, jako jsou samoorganizující se sítě (SON) a správa sítě a služeb bez zásahu obsluhy (ZSM).

## K čemu slouží

Funkce HLC byly vyvinuty, aby řešily rostoucí složitost mobilních sítí, které se vyvinuly z jednoduchých hlasových systémů na platformy s více službami podporující data, IoT a aplikace s nízkou latencí. Rané sítě se spoléhaly na ruční, decentralizovanou správu, která se s rozsahem a dynamickými požadavky sítí 3G/4G stala neudržitelnou. HLC poskytuje centralizovaný, automatizovaný přístup k řízení chování sítě a řeší problémy jako neefektivní využití prostředků, pomalé nasazování služeb a nekonzistentní aplikace politik.

Historicky koncept získal na významu s 3GPP Release 99, které zavedlo sofistikovanější architektury základní sítě. V následujících vydáních se HLC rozšířilo o oblasti jako správa QoS, řízení bezpečnostních politik a později v 5G o síťové řezy a orchestraci NFV. Odstraňuje omezení předchozí ad-hoc správy standardizací rozhraní a funkcí, což umožňuje mezidoménovou koordinaci a schopnost přizpůsobení v reálném čase. Motivací je snížení provozních nákladů, zlepšení uživatelského zážitku prostřednictvím proaktivní správy a podpora inovativních služeb, které vyžadují agilní řízení sítě.

## Klíčové vlastnosti

- Centralizovaná orchestrace síťových prostředků a služeb
- Řízení založené na politikách pro správu QoS a zabezpečení
- Podpora správy životního cyklu síťových řezů
- Integrace s analytikou pro optimalizaci řízenou daty
- Automatizovaná správa poruch, konfigurace a výkonu
- Standardizovaná rozhraní pro interoperabilitu mezi více dodavateli

## Související pojmy

- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [HLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/hlc/)
