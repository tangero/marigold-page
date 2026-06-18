---
slug: "pc"
url: "/mobilnisite/slovnik/pc/"
type: "slovnik"
title: "PC – PerCeption of impairments"
date: 2026-01-01
abbr: "PC"
fullName: "PerCeption of impairments"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pc/"
summary: "Metodologie hodnocení kvality v 3GPP pro vyhodnocování uživatelského vnímání zhoršení multimediálních služeb, jako je degradace kvality zvuku/videa. Používá modely k predikci subjektivních skóre kvali"
---

PC (PerCeption of impairments) je metodologie hodnocení kvality podle 3GPP, která využívá modely k predikci uživatelsky vnímaných skóre multimediální kvality na základě parametrů sítě. Je klíčová pro správu QoS a optimalizaci uživatelského zážitku.

## Popis

PerCeption of impairments (PC) označuje rámec a soubor metodologií definovaných v 3GPP pro hodnocení kvality zážitku ([QoE](/mobilnisite/slovnik/qoe/)) u multimediálních služeb, konkrétně toho, jak uživatelé vnímají degradace jako ztráta paketů, zpoždění nebo jitter. Zahrnuje objektivní modely, které odhadují subjektivní metriky kvality, jako je střední známka kvality ([MOS](/mobilnisite/slovnik/mos/)), na základě měřitelných parametrů sítě a médií. Tyto modely jsou nezbytné pro síťové operátory k monitorování, řízení a optimalizaci kvality služeb bez nutnosti neustálého subjektivního testování uživateli.

Z architektonického hlediska je PC implementováno prostřednictvím algoritmů odhadu kvality, které mohou být nasazeny v síťových sondách, uživatelských zařízeních (UE) nebo funkcích jádra sítě. Tyto algoritmy berou jako vstupy parametry jako typ kodeku, datový tok, míra ztráty paketů, zpoždění a jitter, aby vypočítaly predikované skóre percepční kvality. V systémech 3GPP jsou modely PC specifikovány pro různé služby včetně hlasu (např. s použitím P.863 [POLQA](/mobilnisite/slovnik/polqa/)), streamování videa a konverzačního videa. Výstupy jsou vstupem pro systémy správy QoS, řízení politik a optimalizační nástroje sítě.

Jak to funguje, zahrnuje několik kroků: nejprve jsou během servisní relace shromažďovány parametry média a přenosu. Tyto parametry jsou následně zpracovány standardizovaným percepčním modelem (např. definovaným v [ITU-T](/mobilnisite/slovnik/itu-t/) nebo 3GPP), který napodobuje lidské sluchové nebo zrakové vnímání. Model vydá skóre, často na škále jako 1-5 MOS, udávající očekávanou spokojenost uživatele. Tato data lze využít v reálném čase pro adaptivní streamování s proměnným datovým tokem (např. v [DASH](/mobilnisite/slovnik/dash/)) nebo pro následnou analýzu při plánování sítě. V 3GPP specifikace podrobně popisují mapování parametrů, požadavky na měření a procedury reportování.

Její role v síti je nedílnou součástí zajištění kvality end-to-end. PC umožňuje proaktivní monitorování kvality, pomáhá při odstraňování zhoršení služby a podporuje dynamické přidělování zdrojů. Například v LTE a 5G mohou metriky PC ovlivňovat rozhodnutí funkce [PCRF](/mobilnisite/slovnik/pcrf/) (Policy and Charging Rules Function) o upřednostnění provozu nebo spouštění předávání spojení. Je klíčovou součástí samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)) a automatizace sítě, což operátorům umožňuje efektivně udržovat vysokou QoE.

## K čemu slouží

PC existuje proto, aby překlenula propast mezi objektivními síťovými měřeními a subjektivním uživatelským zážitkem. Tradiční síťové [KPI](/mobilnisite/slovnik/kpi/) (např. propustnost, latence) přímo nepřevádějí, jak uživatelé vnímají kvalitu služby. PC to řeší poskytováním standardizovaných modelů, které predikují percepční kvalitu, což operátorům umožňuje spravovat sítě na základě skutečné uživatelské spokojenosti, nikoli pouze technických metrik.

Historicky se hodnocení kvality spoléhalo na nákladné a pomalé subjektivní testování s lidskými panelem. Vývoj objektivních percepčních modelů, často z ITU-T (např. P.800, P.910), poskytl škálovatelnou alternativu. 3GPP tyto modely přijalo a specifikovalo pro mobilní prostředí, aby řešilo specifická zhoršení bezdrátových sítí, jako je proměnná šířka pásma a přerušení při předávání spojení. Toto bylo motivováno růstem multimediálních služeb (VoIP, streamování videa), kde kvalita přímo ovlivňuje udržení zákazníků.

Integrace do standardů 3GPP zajišťuje konzistenci mezi výrobci a operátory, usnadňuje interoperabilitu a srovnávání. Řeší omezení dřívějších přístupů, kterým chyběly standardizované percepční metriky, a umožňuje tak automatizovanou správu QoE v reálném čase v komplexních mobilních sítích.

## Klíčové vlastnosti

- Objektivní odhad subjektivní kvality (např. MOS)
- Modely pro audio, video a audiovizuální služby
- Vstupy z parametrů sítě (ztráta paketů, jitter, zpoždění)
- Standardizované algoritmy (např. založené na doporučeních ITU-T)
- Integrace s mechanismy QoS a řízení politik
- Podpora monitorování a reportování v reálném čase

## Související pojmy

- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.241** (Rel-6) — Data Description Method for Generic User Profile
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.941** (Rel-6) — 3GPP Generic User Profile Data Description
- … a dalších 22 specifikací

---

📖 **Anglický originál a plná specifikace:** [PC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pc/)
