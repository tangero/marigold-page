---
slug: "epc"
url: "/mobilnisite/slovnik/epc/"
type: "slovnik"
title: "EPC – Evolved Packet Core Network"
date: 2026-01-01
abbr: "EPC"
fullName: "Evolved Packet Core Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/epc/"
summary: "Evolved Packet Core (EPC) je architektura páteřní sítě definovaná pro systémy 4G LTE. Jedná se o plně IP, plochou architekturu navrženou pro poskytování vysokorychlostních paketově přepínaných datovýc"
---

EPC je plně IP architektura páteřní sítě pro systémy 4G LTE, která zajišťuje autentizaci, správu relací a mobilitu pro poskytování paketově přepínaných datových a hlasových služeb.

## Popis

Evolved Packet Core (EPC) je základní architektura páteřní sítě pro systém 3GPP 4G LTE, zavedená jako nový návrh pro podporu vysokorychlostních služeb paketových dat s nízkou latencí. Představuje výrazný odklon od okruhově přepínaných jader sítí 2G/3G a přijímá plně IP, zjednodušenou a plochou architekturu. Primární funkcí EPC je správa datových relací, zajištění konektivity mezi uživatelským zařízením (UE) a externími paketovými datovými sítěmi (jako je internet nebo IMS) a zvládání kritických operací řídicí a uživatelské roviny pro mobilitu a zabezpečení.

Architektonicky se EPC skládá z několika klíčových logických uzlů propojených standardizovanými rozhraními. Centrální entitou řídicí roviny je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), odpovědná za signalizaci, správu přenosových kanálů (bearer), autentizaci a sledování mobility. Serving Gateway (S-GW) funguje jako lokální kotva mobility, směruje a přeposílá pakety uživatelských dat a spravuje předávání spojení mezi eNodeB. Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) je výstupním a vstupním bodem pro provoz do externích sítí; provádí vynucování politik, účtování a přidělování IP adres. Pro data účastníků a autentizaci slouží jako centrální databáze Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Cesta uživatelské roviny je zefektivněna: data proudí z eNodeB přes S-GW do P-GW, čímž se minimalizuje latence. Řídicí rovina využívá rozhraní S1-MME pro připojení eNodeB k MME a rozhraní S11 mezi MME a S-GW pro správu relací.

Fungování EPC zahrnuje koordinovanou sekvenci procedur. Když se UE připojí k síti, zahájí proceduru s MME, které uživatele autentizuje prostřednictvím HSS. Po úspěšné autentizaci MME zřídí výchozí přenosový kanál (default bearer) komunikací se S-GW a P-GW, které UE přidělí IP adresu. Tento kanál představuje virtuální potrubí se specifickými charakteristikami kvality služby (QoS). Všechna následná uživatelská data procházejí touto cestou kanálu. Pro mobilitu, když se UE pohybuje, MME řídí předání spojení (handover) a aktualizuje kontext S-GW pro plynulé přesměrování datové cesty. EPC také podporuje vyhrazené přenosové kanály (dedicated bearers) pro služby vyžadující specifickou QoS, jako je VoIP. Jeho role je naprosto klíčová: je to inteligentní centrum, které umožňuje plynulou mobilitu, zajišťuje bezpečnost, vynucuje operátorské politiky a poskytuje bránu k širšímu internetu a servisním platformám, čímž umožňuje vysokovýkonný datový zážitek LTE.

## K čemu slouží

Evolved Packet Core byl vytvořen, aby řešil omezení předchozích páteřních sítí 3GPP, které byly postaveny na duální doménové architektuře se samostatnými okruhově přepínanými jádry pro hlas a paketově přepínanými jádry pro data. Toto oddělení bylo neefektivní pro rostoucí poptávku po mobilních širokopásmových datech a konvergovaných službách. Primární motivací pro EPC byla podpora vysokých přenosových rychlostí a nízké latence LTE rádiové přístupové sítě pomocí zjednodušeného, nákladově efektivního a škálovatelného jádra, které používalo internetový protokol (IP) pro všechny služby, včetně hlasu (přes VoLTE).

Historicky práce začaly v 3GPP Release 8, navazujíce na dřívější koncepty paketového jádra z [GPRS](/mobilnisite/slovnik/gprs/) a UMTS. EPC řešilo klíčové problémy: odstranilo síťovou složitost a náklady na udržování paralelních okruhových a paketových jader, snížilo latenci prostřednictvím plošší architektury s menším počtem uzlů a poskytlo budoucím službám odolný základ pro plně IP služby. Bylo navrženo od počátku tak, aby zvládlo masivní růst datového provozu, sofistikovanou QoS pro různé aplikace a plynulou mobilitu nejen v rámci LTE, ale také do a z legacy 3GPP a ne-3GPP sítí (jako je WiFi). Vytvoření EPC bylo strategickým krokem k tomu, aby mobilní operátoři mohli konkurovat poskytovatelům pevného širokopásmového připojení a podporovat novou éru chytrých telefonů a připojených zařízení.

## Klíčové vlastnosti

- Plně IP, plochá architektura minimalizující latenci a síťovou složitost
- Oddělení řídicí roviny (MME) a uživatelské roviny (S-GW, P-GW)
- Podpora plynulé mobility v rámci LTE a do/z jiného 3GPP a ne-3GPP přístupu
- Integrace řízení politik a účtování (PCC) pro dynamickou QoS a účtování
- Správa mobility založená na síti s využitím protokolu GTP v uživatelské rovině
- Základ pro Voice over LTE (VoLTE) prostřednictvím propojení s IP Multimedia Subsystem (IMS)

## Související pojmy

- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [P-GW – Packet Data Network Gateway](/mobilnisite/slovnik/p-gw/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.801** (Rel-12) — Study on Non-MTC Mobile Data Application Impacts
- **TS 23.041** (Rel-19) — Cell Broadcast Service and Public Warning System
- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.180** (Rel-19) — MC services support in IOPS mode
- **TS 23.261** (Rel-19) — IP Flow Mobility between 3GPP and WLAN
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.281** (Rel-20) — MCVideo Functional Architecture and Flows
- **TS 23.369** (Rel-19) — 5G System Architecture for Ambient IoT
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- … a dalších 94 specifikací

---

📖 **Anglický originál a plná specifikace:** [EPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/epc/)
