---
slug: "sbi"
url: "/mobilnisite/slovnik/sbi/"
type: "slovnik"
title: "SBI – Service Based Interfaces"
date: 2026-01-01
abbr: "SBI"
fullName: "Service Based Interfaces"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sbi/"
summary: "Moderní architektonické paradigma pro 5G Core Network (5GC), kde síťové funkce (NFs) zpřístupňují své schopnosti jako znovupoužitelné služby prostřednictvím HTTP/2 API. Nahrazuje tradiční rozhraní bod"
---

SBI je architektonický paradigma 3GPP pro 5G Core, kde síťové funkce (Network Functions) zpřístupňují své schopnosti jako znovupoužitelné služby prostřednictvím HTTP/2 API, čímž nahrazují tradiční rozhraní typu bod-bod.

## Popis

Service Based Interfaces (SBI) představují klíčový architektonický princip 5G Core Network (5GC) zavedený ve 3GPP Release 15. Na rozdíl od rozhraní bod-bod v 4G EPC (např. S1, S6a) SBI přijímá architekturu založenou na službách, kde každá síťová funkce ([NF](/mobilnisite/slovnik/nf/)) (např. [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UDM](/mobilnisite/slovnik/udm/)) vystupuje jako producent i konzument služeb. Tyto NFs zpřístupňují své schopnosti jako standardizované, znovupoužitelné služby prostřednictvím aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)), která primárně využívají protokol [HTTP](/mobilnisite/slovnik/http/)/2 s [JSON](/mobilnisite/slovnik/json/) datovou náplní a dodržují RESTful principy. Architektura se opírá o reprezentaci Service Based Interface, kde jsou interakce definovány operacemi služeb (např. Nudm_SubscriberDataManagement) spíše než přepojováním okruhů. Mezi klíčové komponenty patří Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)), která slouží jako registr služeb pro zjišťování a registraci NFs, a Service Communication Proxy (SCP) pro delegované zjišťování a vyrovnávání zatížení. Zabezpečení komunikace je vynucováno pomocí TLS. Princip fungování: Konzument služby (např. SMF), který potřebuje službu, se nejprve dotáže NRF (nebo použije SCP), aby zjistil instanci producenta služby (např. UDM). Poté přímo volá API endpoint producenta. Tento model umožňuje bezestavové NFs, horizontální škálování, automatizovaný správu životního cyklu a dynamické síťové segmenty (network slicing), čímž tvoří páteř cloud-nativního, softwarově definovaného 5GC.

## K čemu slouží

SBI bylo vytvořeno, aby vyřešilo nepružnost, problémy se škálovatelností a pomalý inovační cyklus modelu rozhraní bod-bod v 4G EPC. Tento model vyžadoval specifická rozhraní mezi každou dvojicí NFs, což vedlo ke složité integraci, závislosti na dodavateli a obtížím při zavádění nových služeb. Přechod na 5G si vyžádal architekturu podporující síťové segmenty (network slicing), edge computing, škálování na požádání a rychlé nasazování služeb. SBI to řeší aplikací cloud-nativních a mikroslužebních principů na core network. Umožňuje, aby NFs byly vyvíjeny, nasazovány a škálovány nezávisle. Použití standardních webových protokolů (HTTP/2, JSON) umožňuje snadnější integraci s IT systémy, CI/CD pipeline a aplikacemi třetích stran. Toto paradigma bylo motivováno potřebou provozní agility, podpory různých 5G případů užití od massive IoT po kritické komunikace a ekonomickou nutností nasazení na komerčně dostupném hardwaru ve virtualizovaných/kontejnerizovaných prostředích.

## Klíčové vlastnosti

- Komunikace mezi síťovými funkcemi (NFs) založená na HTTP/2 API
- Registrace a zjišťování služeb prostřednictvím Network Repository Function (NRF)
- Podpora bezestavového, cloud-nativního návrhu NFs
- Umožnění automatizovaného síťového segmentování (network slicing) a orchestraci služeb
- Použití JSON pro flexibilní a rozšiřitelné kódování zpráv
- Přímá komunikace mezi NFs nebo prostřednictvím Service Communication Proxy (SCP)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.540** (Rel-19) — 5G Service Based SMS Stage 2
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 28.203** (Rel-18) — Charging management
- **TS 29.501** (Rel-19) — 5GC SBI API Design Principles & Guidelines
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.543** (Rel-19) — 5G Data Transfer Policy Control Services Stage 3
- **TS 29.551** (Rel-19) — 5G PFD Management Service Stage 3
- **TS 29.554** (Rel-19) — 5G Background Data Transfer Policy Control Service
- **TS 29.562** (Rel-19) — HSS Services for IMS & GBA Interworking
- **TS 29.563** (Rel-19) — TS 29563: Nhss services for HSS-UDM interworking
- **TS 29.571** (Rel-19) — Common Data Types for 5G Service Based Interfaces
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [SBI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbi/)
