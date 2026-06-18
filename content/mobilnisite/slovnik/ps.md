---
slug: "ps"
url: "/mobilnisite/slovnik/ps/"
type: "slovnik"
title: "PS – Public Safety / Packet Switched"
date: 2026-01-01
abbr: "PS"
fullName: "Public Safety / Packet Switched"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ps/"
summary: "Termín s dvojím významem v rámci 3GPP. Primárně 'Packet Switched' (paketově spínaný) označuje doménu sítě pro přenos dat pomocí paketů, která je základem všech datových služeb. Sekundárně, v kontextu"
---

PS je v terminologii 3GPP termín s dvojím významem: označuje buď doménu paketově spínané sítě (Packet Switched) pro datové služby, nebo v kontextu sidelink komunikace oblast veřejné bezpečnosti (Public Safety) pro přímou, na infrastruktuře nezávislou komunikaci zařízení pro nasazení v krizových situacích.

## Popis

Termín 'PS' ve standardech 3GPP má dva odlišné a důležité významy, které se rozlišují podle kontextu.

Jako **Packet Switched (PS)** označuje architektonickou doménu a typ služby, kde jsou uživatelská data formátována do paketů pro přenos, na rozdíl od domény Circuit Switched ([CS](/mobilnisite/slovnik/cs/)) používané pro tradiční hlasové hovory. Doména PS je základem mobilního širokopásmového přístupu. V 5G je celá core síť založena na paketech (5GC), ale termín zůstává relevantní z historického hlediska a při propojování sítí. PS spojení zahrnuje vytvoření kontextu Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) v [GPRS](/mobilnisite/slovnik/gprs/)/UMTS nebo [PDN](/mobilnisite/slovnik/pdn/) Connection/EPS Bearer v LTE, což definuje datovou cestu mezi UE a externí paketovou datovou sítí (např. internetem). Mezi klíčové síťové funkce v doméně PS patří Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a Gateway GPRS Support Node (GGSN) ve 2G/3G, Serving Gateway ([S-GW](/mobilnisite/slovnik/s-gw/)) a Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) v LTE/EPC a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC. Tyto uzly zajišťují směrování paketů, kotvení mobility, vynucování politik a účtování.

Jako **Public Safety (PS)**, zejména ve specifikacích týkajících se sidelink (např. řada 23.xxx pro ProSe, 24.xxx pro protokoly), označuje aplikace a síťové funkce navržené pro nasazení v krizových situacích záchrannými složkami (policie, hasiči, záchranná služba) a dalšími vládními agenturami. Komunikace pro veřejnou bezpečnost vyžaduje vysokou spolehlivost, dostupnost, zabezpečení a provoz v přímém režimu, když je síťová infrastruktura poškozena nebo nedostupná. 3GPP standardizovalo funkce jako Proximity Services (ProSe) a Mission Critical Services (MCS), aby tyto požadavky splnilo. Klíčovým prvkem je komunikace zařízení přímo mezi sebou přes sidelink rozhraní PC5, umožňující přímou komunikaci UE-UE (PS-LTE, PS-NR) bez průchodu síťovou infrastrukturou. To zahrnuje funkce jako přímé objevování, přímá komunikace a UE-to-Network Relay.

Oba významy se v moderních sítích sbližují: služby veřejné bezpečnosti stále více spoléhají na paketově spínanou infrastrukturu pro širokopásmové datové aplikace (video, sdílení dat) a využívají doménu PS (Packet Switched) pro operace připojené k síti, zároveň však využívají přímý sidelink PS (Public Safety) pro odolnost.

## K čemu slouží

Význam **Packet Switched** (paketově spínaný) vychází ze zásadního vývoje mobilních sítí od hlasově orientovaných okruhově spínaných systémů k datově orientovaným paketově spínaným systémům. Rané sítě GSM byly optimalizovány pro okruhově spínaný hlas. Zavedení GPRS (General Packet Radio Service) ve 2G vytvořilo doménu PS, aby umožnilo efektivní 'vždy připojený' přístup k internetu prostřednictvím statistického sdílení síťových zdrojů. Tím se vyřešil problém neefektivních vyhrazených okruhů pro trhavý datový provoz, což umožnilo mobilní datovou revoluci. Každá generace (3G UMTS, 4G LTE, 5G NR) vylepšila doménu PS vyššími rychlostmi, nižší latencí a sofistikovanějším řízením kvality služeb (QoS).

Význam **Public Safety** (veřejná bezpečnost) vznikl z potřeby, aby komerční mobilní síťová technologie podporovala přísné požadavky komunikace záchranných složek. Tradičně se veřejná bezpečnost spoléhala na vyhrazené systémy pozemní mobilní rádiové komunikace (LMR), jako jsou TETRA nebo P25. Standardizace v 3GPP, počínaje Release 12 a významně rozšířená v Releases 13-15, si kladla za cíl využít výhod rozsahu a pokročilých schopností LTE (a později 5G) k poskytování širokopásmových služeb veřejné bezpečnosti. Tím se řešila omezení úzkopásmových LMR systémů, jako jsou nízké přenosové rychlosti a absence pokročilých multimediálních služeb. Práce na PS (Public Safety) v rámci 3GPP řeší problém poskytování služeb pro nasazení v krizových situacích, jako je mission-critical push-to-talk (MCPTT), video a data, s vysokou spolehlivostí, správou skupinové komunikace a – což je zásadní – schopností provozu přímo mezi zařízeními při ztrátě síťového pokrytí, což je životně důležitý požadavek v katastrofických scénářích.

## Klíčové vlastnosti

- **Packet Switched**: Umožňuje efektivní statistické multiplexování uživatelských datových paketů přes sdílené kanály.
- **Packet Switched**: Podporuje 'vždy připojenou' konektivitu a více souběžných datových relací (kontexty PDP/PDN spojení).
- **Packet Switched**: Je základem pro mobilní internet, IMS (VoLTE/VoNR) a všechny služby založené na IP.
- **Public Safety**: Umožňuje přímou komunikaci mezi zařízeními (sidelink) pro provoz nezávislý na síťové infrastruktuře.
- **Public Safety**: Podporuje služby pro nasazení v krizových situacích (MCPTT, MCVideo, MCData) s vysokou prioritou a možností přednostního přerušení.
- **Public Safety**: Poskytuje rozšířenou skupinovou komunikaci, zabezpečení a služby založené na blízkosti (ProSe).

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 22.127** (Rel-9) — Open Service Access (OSA) Requirements
- **TS 22.135** (Rel-19) — Multicall Supplementary Service Specification
- **TS 22.233** (Rel-19) — Packet-switched Streaming Service (PSS) Stage 1
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.803** (Rel-12) — Proximity Services (ProSe) Study
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- … a dalších 90 specifikací

---

📖 **Anglický originál a plná specifikace:** [PS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ps/)
