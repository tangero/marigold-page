---
slug: "sdu"
url: "/mobilnisite/slovnik/sdu/"
type: "slovnik"
title: "SDU – Signalling Data Unit"
date: 2025-01-01
abbr: "SDU"
fullName: "Signalling Data Unit"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sdu/"
summary: "Protokolová datová jednotka (PDU) používaná pro přenos signalizačních informací mezi partnerskými entitami v síti 3GPP. Jedná se o datovou jednotku předávanou mezi protokolovými vrstvami, která obsahu"
---

SDU (jednotka signalizačních dat) je datová jednotka předávaná mezi protokolovými vrstvami, která obsahuje signalizační informace řídicí roviny pro sestavení hovoru, správu mobility a řízení relace v síti 3GPP.

## Popis

Signalling Data Unit (SDU) je základní koncept ve vrstvené protokolové architektuře definované standardy 3GPP. Představuje datový paket, který je předáván z vyšší protokolové vrstvy na nižší vrstvu pro přenos. Z pohledu nižší vrstvy je SDU datová jednotka určená k transportu. Nižší vrstva k této SDU obvykle přidá svou vlastní hlavičku a/nebo zápatí specifické pro daný protokol a přemění ji tak na protokolovou datovou jednotku ([PDU](/mobilnisite/slovnik/pdu/)) pro tuto vrstvu. Tato PDU je pak předána dále po zásobníku nebo přenesena přes fyzické médium. Proces je obrácený na přijímací straně, kde nižší vrstva zpracuje příchozí PDU, odstraní svou vlastní hlavičku/zápatí a výslednou SDU doručí do vyšší vrstvy.

Rozlišení SDU/PDU je klíčové napříč všemi rozhraními a protokolovými zásobníky 3GPP, včetně rozhraní rádiového přístupu (Uu), rozhraní Iu mezi RAN a CN a rozhraní jádra sítě. Například ve vrstvě Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) je SDU přijatá od vrstvy Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) segmentována a/nebo konkatenována, je přidána RLC hlavička a jednotka se stane RLC PDU. Tato PDU je pak předána vrstvě Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)), kde se stane MAC SDU. Vrstva MAC může multiplexovat několik MAC SDU, přidat MAC hlavičku a vytvořit transportní blok (MAC PDU) pro přenos přes fyzickou vrstvu.

Integrita a správné zpracování SDU je prvořadé pro spolehlivost signalizace. Signalizační protokoly jako Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) a Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) spoléhají na podkladové vrstvy, že jejich SDU doručí přesně a ve správném pořadí. Mechanizmy v rámci každé vrstvy, jako je RLC Acknowledged Mode, zajišťují spolehlivé doručení signalizačních SDU. Velikost a formát SDU jsou definovány službou očekávanou vyšší vrstvou a možnostmi nižší vrstvy, přičemž specifikace detailně popisují maximální velikosti a postupy pro segmentaci a opětovné složení.

## K čemu slouží

Koncept SDU existuje pro formalizaci výměny dat mezi sousedními vrstvami ve standardizovaném protokolovém zásobníku, což umožňuje modulární návrh a interoperabilitu. Řeší problém, jak jsou informace z aplikace nebo řídicího procesu zabaleny, transportovány a spolehlivě doručeny přes komplexní síť, a to oddělením zodpovědností. Každá vrstva má specifickou funkci (např. oprava chyb, směrování, šifrování) a SDU je přesně definovaná datová jednotka, na které tato funkce operuje.

Historicky, bez jasného vrstveného modelu a abstrakce SDU/[PDU](/mobilnisite/slovnik/pdu/), byl návrh protokolů monolitický a nepružný. Tyto koncepty zavedl model Open Systems Interconnection (OSI), které převzala a upravila organizace 3GPP. SDU poskytuje čistý přístupový bod služby pro horní vrstvu a skrývá složitost přenosu v nižší vrstvě. To umožňuje nezávislý vývoj a optimalizaci různých protokolových vrstev (např. zavedení nového režimu RLC nebo nové technologie fyzické vrstvy) bez narušení signalizačních protokolů vyšších vrstev, pokud je zachována služba doručování SDU.

## Klíčové vlastnosti

- Představuje datovou jednotku vyměňovanou mezi sousedními protokolovými vrstvami.
- Definuje datovou jednotku služby pro službu konkrétní vrstvy.
- Je přeměněna na protokolovou datovou jednotku (PDU) přidáním řídicích informací specifických pro danou vrstvu.
- Základní pro všechny protokolové zásobníky 3GPP (Uu, Iu, Gn, N2, N3 atd.).
- Klíčová pro přenos signalizačních zpráv řídicí roviny (RRC, NAS, SIP).
- Podléhá procedurám specifickým pro danou vrstvu, jako je segmentace, konkatenace a šifrování.

## Související pojmy

- [PDU – Protocol Data Unit](/mobilnisite/slovnik/pdu/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.065** (Rel-4) — GPRS Subnetwork Dependent Convergence Protocol
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [SDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdu/)
