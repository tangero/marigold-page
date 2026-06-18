---
slug: "sdf"
url: "/mobilnisite/slovnik/sdf/"
type: "slovnik"
title: "SDF – Service Data Flow"
date: 2026-01-01
abbr: "SDF"
fullName: "Service Data Flow"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sdf/"
summary: "Service Data Flow (SDF, tok služebních dat) je základní koncept v řízení politiky a účtování (PCC) 3GPP. Definuje množinu toků IP paketů odpovídajících specifickým filtrům, která se používá pro jednot"
---

SDF je množina toků IP paketů odpovídajících specifickým filtrům, používaná v řízení politiky a účtování 3GPP pro jednotné uplatňování politiky kvality služeb (QoS) a účtování.

## Popis

Service Data Flow (SDF, tok služebních dat) je úhelným kamenem architektury 3GPP Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), definovaným od vydání 6. Představuje soubor toků IP paketů, které jsou identifikovány sadou paketových filtrů (např. na základě zdrojových/cílových IP adres, portů, typu protokolu a volitelně informací z hloubkové kontroly paketů (DPI)). Primární funkcí SDF je sloužit jako podrobná entita, na kterou jsou jednotně uplatňovány síťové politiky – konkrétně pravidla kvality služeb (QoS) a účtování. Když pakety uživatelských dat procházejí sítí, jsou porovnávány s těmito předdefinovanými filtry SDF ve funkci vynucení politiky a účtování ([PCEF](/mobilnisite/slovnik/pcef/)), která se typicky nachází v Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)).

Architektura pro správu SDF je centralizovaná kolem funkce pravidel politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)). PCRF je mozkem systému PCC. Činí dynamická rozhodnutí o politice na základě informací o účastníkovi, požadavků na služby a stavu sítě přijatých z různých zdrojů, jako je Application Function ([AF](/mobilnisite/slovnik/af/)) a Subscription Profile Repository ([SPR](/mobilnisite/slovnik/spr/)). Tato rozhodnutí jsou převedena na PCC pravidla, z nichž každé obsahuje šablonu SDF (filtry) a odpovídající akce politiky. Tato PCC pravidla jsou poté zřízena do PCEF přes rozhraní Gx. PCEF tato pravidla vynucuje v reálném čase, provádějíc operace jako gating (povolování/blokování paketů), označování QoS (nastavení QoS Class Identifier) a monitorování využití pro účtování.

Role SDF je nedílná pro umožnění sofistikovaných servisních modelů. Umožňuje síti rozlišovat provoz nejen na uživatele nebo Access Point Name ([APN](/mobilnisite/slovnik/apn/)), ale i na konkrétní aplikaci nebo typ služby. Například provoz video streamování může být identifikován jako samostatný SDF a přidělen vyšší šířka pásma (garantovaný přenosový výkon) ve srovnání s best-effort provozem prohlížení webu. Z pohledu účtování může být SDF spojen s konkrétními účtovacími klíči a metodami (např. objemové, časové nebo událostní), což umožňuje flexibilní monetizační strategie jako sponzorovaná data nebo zero-rating. Abstrakce SDF tak odděluje servisní logiku od transportní vrstvy sítě a poskytuje operátorům mocný nástroj pro správu provozu a generování příjmů.

## K čemu slouží

Koncept SDF byl zaveden, aby řešil omezení dřívějších mobilních datových sítí, které primárně nabízely jednoduchý, best-effort přístup k internetu s paušálním účtováním. Jak se mobilní služby vyvinuly a zahrnuly VoIP, video streamování a podnikové aplikace, vznikla kritická potřeba, aby síť inteligentně identifikovala různé typy provozu a uplatňovala odpovídající kvalitní a účtovací zacházení. Před PCC bylo jakékoli vynucování politiky statické a konfigurované ručně na síťových bránách, bez dynamiky a povědomí o účastníkovi potřebného pro moderní služby.

Vytvoření rámce PCC se SDF v jeho jádru bylo motivováno potřebou standardizované, dynamické kontroly politiky. Řeší problém, jak bezproblémově integrovat požadavky služeb aplikační vrstvy (např. videohovor potřebující nízkou latenci) s možnostmi transportní sítě. Definováním provozu na úrovni podrobnosti SDF mohou operátoři vytvářet a monetizovat vrstvené servisní plány, zajistit optimální přidělování síťových zdrojů a poskytovat konzistentní kvalitu uživatelského zážitku pro specifické aplikace. Umožnilo to přechod od 'hloupé trubky' k 'chytré trubce' schopné servisní inovace.

## Klíčové vlastnosti

- Podrobná identifikace provozu pomocí IP 5-tice a DPI filtrů
- Základ pro dynamické vynucování politiky QoS (gating, šířka pásma, priorita)
- Základ pro flexibilní, na služby orientované účtování (online/offline)
- Centralizovaná kontrola přes PCRF s zřizováním pravidel v reálném čase
- Odděluje servisní logiku od transportní vrstvy sítě
- Umožňuje sponzorovaná data, zero-rating a vrstvené servisní plány

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TR 28.827** (Rel-18) — Technical Report on 5G Charging for Roaming Scenarios
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [SDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdf/)
