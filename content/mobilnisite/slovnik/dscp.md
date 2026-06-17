---
slug: "dscp"
url: "/mobilnisite/slovnik/dscp/"
type: "slovnik"
title: "DSCP – Differentiated Services Code Point"
date: 2025-01-01
abbr: "DSCP"
fullName: "Differentiated Services Code Point"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dscp/"
summary: "6bitové pole v hlavičce IP paketu (IPv4 a IPv6) sloužící ke klasifikaci a správě síťového provozu podle architektury Differentiated Services (DiffServ). V systémech 3GPP se používá k mapování QoS toků"
---

DSCP je 6bitové pole v hlavičce IP paketu používané v architektuře Differentiated Services pro klasifikaci provozu, což umožňuje systémům 3GPP mapovat QoS toky na IP třídy služeb za účelem konzistentního zacházení v transportní síti.

## Popis

Differentiated Services Code Point (DSCP) je standardizované pole v rámci bajtu Type of Service (ToS) hlavičky IPv4 nebo bajtu Traffic Class hlavičky IPv6. Využívá šest bitů, což umožňuje až 64 různých kódových bodů (hodnoty 0-63). V architektuře 3GPP je DSCP klíčovým nástrojem pro implementaci komplexní kvality služeb (QoS) napříč transportními segmenty, které propojují síťové funkce, například mezi eNodeB a S-GW/[UPF](/mobilnisite/slovnik/upf/) nebo uvnitř samotné jádrové sítě. Funguje jako součást širšího modelu [IETF](/mobilnisite/slovnik/ietf/) Differentiated Services (DiffServ), který poskytuje škálovatelnou diferenciaci služeb v IP sítích bez nutnosti udržovat stav pro každý jednotlivý tok na všech směrovačích.

Mechanismus pracuje tak, že pakety jsou označovány při vstupu do domény DiffServ (např. mobilní transportní sítě). Síťová funkce 3GPP, jako je Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) nebo User Plane Function (UPF), klasifikuje uplinkový a downlinkový uživatelský provoz na základě pravidel QoS asociovaných s EPS přenosovým kanálem nebo 5G QoS tokem. Tato klasifikace určuje příslušnou hodnotu DSCP, která se zapíše do IP hlavičky paketů uživatelské roviny. Směrovače a přepínače v transportní síti jsou pak nakonfigurovány s Per-Hop Behaviors (PHB), které odpovídají konkrétním hodnotám DSCP. Tyto PHB definují, jak jsou pakety zařazovány do front, plánovány a případně zahazovány, a poskytují chování jako Expedited Forwarding ([EF](/mobilnisite/slovnik/ef/)) pro provoz s nízkou latencí, Assured Forwarding ([AF](/mobilnisite/slovnik/af/)) pro garantovanou propustnost nebo Default (BE) pro best-effort.

V systémech 3GPP je mapování mezi parametry QoS rádiového přenosového kanálu ([QCI](/mobilnisite/slovnik/qci/) v 4G, [5QI](/mobilnisite/slovnik/5qi/) v 5G) a hodnotou DSCP klíčovou konfigurační položkou. To zajišťuje, že QoS zamýšlená rádiovou a jádrovou sítí je vhodně signalizována a respektována podkladovou IP transportní infrastrukturou. Například QoS tok pro Voice over NR (5G VoIP) s 5QI rovným 1 (konverzační hlas) by byl označen hodnotou DSCP odpovídající PHB EF (často DSCP 46), aby byl upřednostňován v transportní síti. Tím vzniká kohezivní hierarchie QoS od aplikační vrstvy přes rádiovou, jádrovou až po transportní vrstvu.

## K čemu slouží

DSCP bylo v rámci 3GPP přijato k řešení problému udržování konzistentního QoS zacházení s uživatelským provozem při jeho průchodu IP-based transportními sítěmi, které propojují uzly RAN a jádra sítě. Rané mobilní sítě měly monolitičtější, okruhově přepínaný transport, kde bylo QoS implicitní. S přechodem na all-IP architekturu ve 3GPP Release 5 a novějších byla nutná standardizovaná metoda značení na IP vrstvě pro signalizaci priority paketů směrovačům a přepínačům.

Jeho použití bylo motivováno potřebou škálovatelnosti. Model DiffServ využívající DSCP nevyžaduje, aby transportní směrovače udržovaly stav pro miliony jednotlivých uživatelských přenosových kanálů, na rozdíl od dřívějšího modelu Integrated Services (IntServ). To jej činí dokonale vhodným pro rozsáhlé mobilní sítě. DSCP umožňuje, aby byl složitý QoS rámec mobilní sítě (s [QCI](/mobilnisite/slovnik/qci/)/5QI, ARP atd.) plynule převeden na jednoduchý, široce podporovaný standard IP sítí, a zajišťuje tak, že provoz citlivý na latenci nebo s vysokou prioritou dostává odpovídající zacházení na každém směrovacím uzlu na své cestě páteřní sítí operátora.

## Klíčové vlastnosti

- 6bitové pole v IP hlavičce pro klasifikaci provozu
- Součást architektury IETF DiffServ pro škálovatelné QoS
- Mapuje parametry QoS 3GPP (QCI/5QI) na zacházení v transportní síti
- Umožňuje Per-Hop Behaviors (PHB) jako EF, AF a BE
- Konfigurovatelné značení bránami uživatelské roviny (P-GW/UPF)
- Klíčové pro komplexní QoS napříč IP transportními segmenty

## Související pojmy

- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 24.139** (Rel-19) — UE-EPC Procedures for Fixed Broadband Access
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.820** (Rel-11) — 3GPP-Fixed Broadband Interworking Procedures
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.128** (Rel-19) — MME/SGSN-SCEF Diameter Interfaces for PDN Interworking
- **TS 29.139** (Rel-19) — H(e)NB - SeGW Interface Specification
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.201** (Rel-19) — RESTful Rx Interface for AF-PC Communication
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- … a dalších 22 specifikací

---

📖 **Anglický originál a plná specifikace:** [DSCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dscp/)
