---
slug: "hrpd"
url: "/mobilnisite/slovnik/hrpd/"
type: "slovnik"
title: "HRPD – High Rate Packet Data"
date: 2025-01-01
abbr: "HRPD"
fullName: "High Rate Packet Data"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hrpd/"
summary: "HRPD je vysokorychlostní paketová rozhraní technologie vzdušného rozhraní založená na cdma2000, specifikovaná organizací 3GPP2 a standardizovaná pro spolupráci se systémy 3GPP. Poskytuje výhradně pake"
---

HRPD je vysokorychlostní paketová rozhraní technologie vzdušného rozhraní založená na cdma2000, specifikovaná organizací 3GPP2, která poskytuje výhradně paketovou, trvale připojenou širokopásmovou přístupovou síť a umožňuje evoluční cestu směrem k LTE/5G.

## Popis

High Rate Packet Data (HRPD), známé také jako CDMA2000 1xEV-DO (Evolution-Data Optimized), je paketově orientovaná radiová přístupová technologie definovaná standardizačním orgánem 3GPP2 a následně integrovaná do specifikací 3GPP pro spolupráci. Architektonicky se HRPD přístupová síť skládá ze dvou klíčových logických komponent: Evolved Access Network (eAN) a Packet Control Function ([PCF](/mobilnisite/slovnik/pcf/)). eAN je zodpovědná za správu rádiových zdrojů, správu mobility a fyzické a linkové protokoly přes vzdušné rozhraní. PCF funguje jako rozhraní mezi eAN a paketovou datovou jádrovou sítí, spravuje navazování a ukončování paketových datových relací a přeposílá uživatelská data.

Technologie pracuje na samostatném nosiči vyhrazeném výhradně pro paketová data a využívá pokročilé techniky, jako je adaptivní modulace a kódování ([AMC](/mobilnisite/slovnik/amc/)), hybridní automatické opakování požadavku ([HARQ](/mobilnisite/slovnik/harq/)) a rychlé plánování, aby maximalizovala spektrální účinnost a propustnost pro uživatele. Vzdušné rozhraní používá pro dopředný kanál multiplexování s časovým dělením ([TDM](/mobilnisite/slovnik/tdm/)), což umožňuje přidělit celou kapacitu kanálu v daném okamžiku jedinému uživateli, což je optimální pro přerušovaný vysokorychlostní datový provoz. Zpětný kanál využívá mnohonásobný přístup s kódovým dělením ([CDMA](/mobilnisite/slovnik/cdma/)). Mezi klíčové protokoly v rámci HRPD patří Radio Link Protocol ([RLP](/mobilnisite/slovnik/rlp/)) pro spolehlivost na linkové vrstvě a Radio Network Protocol (RNP) pro řídicí signalizaci mezi terminálem a sítí.

V rámci ekosystému 3GPP je primární role HRPD definována v kontextu spolupráce s přístupem mimo 3GPP. Připojuje se k 3GPP Evolved Packet Core (EPC) přes rozhraní S2a založené na protokolech Proxy Mobile IPv6 (PMIPv6) nebo [GTP](/mobilnisite/slovnik/gtp/), zprostředkované přes Evolved Packet Data Gateway (ePDG) nebo přímo přes Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)). Tato architektura umožňuje uživatelskému zařízení (UE) s dvourádiovými schopnostmi (např. LTE a HRPD) provádět předávání mezi těmito dvěma technologiemi, což je funkce standardizovaná jako Optimalizované předávání (eHRPD). Síť HRPD poskytuje UE trvalé IP připojení a podporuje širokou škálu IP multimediálních služeb.

## K čemu slouží

HRPD bylo vytvořeno, aby uspokojilo rostoucí poptávku po mobilních širokopásmových datových službách přesahujících možnosti sítí 2G a raných 3G CDMA (jako CDMA2000 1xRTT), které byly primárně spojově orientované a optimalizované pro hlas. Jeho vývoj byl motivován potřebou vysokorychlostního, efektivního, výhradně paketového vzdušného rozhraní, které by mohlo poskytovat internetový zážitek na mobilních zařízeních a podporovat aplikace jako streamování videa, stahování velkých souborů a prohlížení webu s nízkou latencí.

Integrace HRPD do standardů 3GPP, počínaje Release 8, byla hnána praktickou nutností globální mobility a plynulé služby. Jak se LTE od 3GPP stalo dominantní 4G technologií, mnoho operátorů s existujícími sítěmi CDMA/HRPD potřebovalo jasnou migrační cestu. Standardizace postupů spolupráce mezi EPC a HRPD umožnila těmto operátorům využít své stávající investice do rádiové sítě při přechodu účastníků na LTE, zajistila kontinuitu datových relací během předávání a konzistentní uživatelský zážitek. Tím se vyřešil kritický problém fragmentace sítí a umožnil plynulejší technologickou evoluci pro významnou část globálního trhu.

## Klíčové vlastnosti

- Výhradně paketové, trvale připojené vzdušné rozhraní optimalizované pro data
- Vysoká spektrální účinnost využívající TDM dopředný kanál a adaptivní modulaci
- Spolupráce s 3GPP EPC přes rozhraní S2a pro plynulou mobilitu
- Podpora Optimalizovaného předávání (eHRPD) do/z LTE
- Pokročilé rádiové funkce jako rychlý výběr buňky a hybridní ARQ
- Poskytuje migrační cestu ze sítí 3GPP2 CDMA k 3GPP LTE/5G

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.276** (Rel-19) — EPS S101/S121/S103 Interfaces Stage 3
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [HRPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/hrpd/)
