---
slug: "mgw"
url: "/mobilnisite/slovnik/mgw/"
type: "slovnik"
title: "MGW – Media Gateway"
date: 2025-01-01
abbr: "MGW"
fullName: "Media Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mgw/"
summary: "Síťový prvek, který převádí mediální toky mezi různými přenosovými formáty a protokoly, například mezi sítěmi s přepojováním okruhů (TDM) a sítěmi s přepojováním paketů (IP). Je nezbytný pro umožnění"
---

MGW je síťový prvek, který převádí mediální toky mezi různými přenosovými formáty a protokoly, například mezi sítěmi s přepojováním okruhů a sítěmi s přepojováním paketů, aby umožnil komunikaci mezi staršími a moderními sítěmi.

## Popis

Media Gateway (MGW) je klíčová funkční entita v jádru sítě podle 3GPP, konkrétně v doménách Circuit-Switched ([CS](/mobilnisite/slovnik/cs/)) a IP Multimedia Subsystem (IMS). Jejím hlavním úkolem je provádět konverzi a zpracování médií. Z architektonického hlediska je MGW řízen Media Gateway Controllerem ([MGC](/mobilnisite/slovnik/mgc/)) nebo v kontextu 3GPP Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) Serverem či Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pomocí řídicích protokolů jako H.248 (Megaco) nebo [SIP](/mobilnisite/slovnik/sip/). Samotný MGW zpracovává provoz v uživatelské rovině. Obsahuje koncové body pro různá síťová rozhraní: na jedné straně se připojuje ke starším sítím s přepojováním okruhů pomocí rozhraní s časovým multiplexem ([TDM](/mobilnisite/slovnik/tdm/)), jako je E1/T1; na druhé straně se připojuje k sítím s přepojováním paketů, jako jsou sítě založené na IP (např. IMS core nebo Internet), pomocí protokolu Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) přes IP. Mezi klíčové vnitřní komponenty patří kodeky pro překódování (např. převod mezi G.711 [PCM](/mobilnisite/slovnik/pcm/) a AMR), potlačovače ozvěn, generátory tónů a vyrovnávací paměti pro potlačení chvění (jitter). Jeho činnost spočívá v přijímání příkazů z řídicí roviny k vytvoření, změně a uvolnění terminací a kontextů (logických asociací terminací pro hovor). Pro hlasový hovor pocházející ze starého telefonu PSTN do VoIP klienta by MGW ukončil TDM trasu, dekódoval proud G.711, převedl jej na vhodný kodek (pokud je třeba), zabalil do paketů RTP a odeslal přes IP síť. Také provádí funkce přenosových zdrojů, jako je přehrávání hlášení a sběr DTMF tónů. V architektuře IMS je MGW často označován jako Media Resource Function Processor (MRFP), když poskytuje služby zpracování médií, jako je konferenční hovor a překódování. Jeho role je zásadní pro konvergenci sítí, protože umožňuje operátorům migrovat ze starých TDM sítí na plně IP infrastruktury při zachování kvality služeb a interoperability.

## K čemu slouží

MGW byl vytvořen, aby řešil základní výzvu vývoje a konvergence sítí. Historicky byly telekomunikační sítě postaveny na technologii s přepojováním okruhů (TDM), která je efektivní pro hlas, ale pro data je rigidní a nákladná. Vzestup internetu a služeb založených na IP si vyžádal flexibilnější a nákladově efektivnější infrastrukturu s přepojováním paketů. MGW řeší problém interoperability mezi těmito odlišnými síťovými doménami. Umožňuje síťovým operátorům zavádět jádrové sítě založené na IP (jako je IMS) postupně, aniž by okamžitě ztratili své masivní investice do staršího vybavení PSTN a 2G/3G s přepojováním okruhů. Před MGW vyžadovalo vzájemné propojení složité a drahé adaptéry a služby jako VoIP byly izolované. MGW pod řízením softswitchu (MSC Server) umožnil oddělení řízení hovoru (signalizace) od přenosu médií, což je klíčový princip sítí nové generace. Toto oddělení zvýšilo škálovatelnost, umožnilo centralizovanou inteligenci a usnadnilo zavádění nových multimediálních služeb. Vytvoření MGW bylo motivováno potřebou standardizovaného, mezi dodavateli interoperabilního způsobu propojení světů TDM a IP, což byl od Release 99 ústřední cíl 3GPP jako součást definice vize All-IP sítě pro UMTS a další generace.

## Klíčové vlastnosti

- Překódování mezi různými řečovými a audio kodeky (např. G.711, AMR, EVS)
- Vzájemné propojení mezi přenosovými sítěmi TDM (E1/T1) a IP (RTP/UDP/IP)
- Podpora řízení pomocí protokolu H.248 (Megaco) pro řízení mediální brány
- Integrované funkce zpracování médií, jako je potlačení ozvěn, generování tónů a vyrovnávací paměť pro potlačení chvění
- Funkce přenosových zdrojů pro přehrávání hlášení a sběr DTMF tónů v pásmu
- V architektuře IMS funguje jako Media Resource Function Processor (MRFP) pro konferenční hovory a překódování

## Související pojmy

- [MSS – Mobile Satellite Services](/mobilnisite/slovnik/mss/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRFC – Multimedia Resource Function Controller](/mobilnisite/slovnik/mrfc/)
- [MRFP – Multimedia Resource Function Processor](/mobilnisite/slovnik/mrfp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- **TS 24.628** (Rel-19) — Common Basic Communication Procedures in IMS
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TR 26.944** (Rel-19) — QoE, ESQoS and SQoS metrics for 3G multimedia services
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [MGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgw/)
