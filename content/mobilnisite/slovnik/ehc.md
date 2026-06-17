---
slug: "ehc"
url: "/mobilnisite/slovnik/ehc/"
type: "slovnik"
title: "EHC – Ethernet Header Compression"
date: 2025-01-01
abbr: "EHC"
fullName: "Ethernet Header Compression"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ehc/"
summary: "EHC je protokol 3GPP, který komprimuje hlavičky ethernetových rámců přes rozhraní vzdušného přenosu za účelem snížení režie a zvýšení spektrální účinnosti. Je klíčový pro podporu služeb založených na"
---

EHC je protokol 3GPP, který komprimuje hlavičky ethernetových rámců přes rozhraní vzdušného přenosu (air interface) za účelem snížení režie a zvýšení spektrální účinnosti pro služby jako průmyslový IoT.

## Popis

Ethernet Header Compression (EHC) je protokol definovaný 3GPP pro efektivní přenos ethernetových rámců přes celulární rádiové přístupové sítě (RAN), konkrétně pro NR (New Radio) a LTE. Funguje tak, že před přenosem přes rozhraní Uu mezi uživatelským zařízením (UE) a stanicí gNB (v 5G) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE) komprimuje často redundantní pole v hlavičkách ethernetových rámců. Protokol je typicky implementován ve vrstvě PDCP (Packet Data Convergence Protocol), která je zodpovědná za kompresi hlaviček a šifrování. EHC funguje na principu vytvoření kontextu mezi kompresorem (odesílatel) a dekompresorem (příjemce) pro každý datový tok. Tento kontext obsahuje statické informace o polích ethernetové hlavičky, jako jsou zdrojové a cílové [MAC](/mobilnisite/slovnik/mac/) adresy, VLAN tagy a EtherType. Po odeslání úplné počáteční hlavičky pro vytvoření kontextu přenášejí následující pakety pouze komprimovanou hlavičku obsahující dynamická pole (jako čísla sekvence) a změny statických polí, což výrazně snižuje režii na paket.

Architektura zahrnuje entity EHC jak v UE, tak v základnové stanici (gNB/eNB). Komprese a dekomprese se provádějí na vrstvě PDCP. Síť konfiguruje parametry EHC prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), přičemž specifikuje profily a kontexty. EHC podporuje více profilů pro zpracování různých typů ethernetových rámců, včetně rámců s VLAN tagy i bez nich. Využívá principy robustní komprese hlaviček (ROHC) upravené pro Ethernet a používá zpětnovazební mechanismy pro zajištění spolehlivé synchronizace kontextu mezi kompresorem a dekompresorem i v podmínkách ztrátového rádiového spojení.

Role EHC je klíčová v architektuře systému 5G pro podporu služeb založených na Ethernetu, které vyžadují nízkou latenci a vysokou spolehlivost, jako jsou služby definované pro službu typu 5G [LAN](/mobilnisite/slovnik/lan/), průmyslovou automatizaci a integraci přenosu front-haulového/back-haulového provozu. Snížením velikosti hlavičky zkracuje dobu přenosu a zvyšuje efektivní datovou propustnost, což je zásadní pro splnění přísných požadavků scénářů využití URLLC (Ultra-Reliable Low-Latency Communication) a eMBB (enhanced Mobile Broadband). Umožňuje systému 5G nativně přenášet ethernetové rámce vrstvy 2, což usnadňuje integraci s existujícími průmyslovými sítěmi založenými na Ethernetu a podporuje síťové segmentování (network slicing) pro izolované segmenty služeb.

## K čemu slouží

EHC byl zaveden, aby řešil neefektivitu přenosu standardních ethernetových rámců, které mají minimální velikost hlavičky 14 bajtů (plus volitelné VLAN tagy), přes rozhraní vzdušného přenosu v sítích 4G a 5G, které je limitováno šířkou pásma a citlivé na latenci. Před zavedením EHC vyžadoval přenos ethernetového provozu přes celulární síť tunelovací protokoly jako [GTP-U](/mobilnisite/slovnik/gtp-u/), které přidávaly další režii, nebo přenos nekomprimovaných hlaviček, což plýtvalo cennými rádiovými prostředky. To bylo zvláště problematické pro nové scénáře využití 5G, jako je průmyslový IoT, komunikace vozidlo-se-vším (V2X) a mobilní přenos front-haulového provozu, kde je generováno mnoho malých, častých ethernetových paketů (např. pro senzorová data nebo řídicí signály), takže režie hlaviček tvořila významnou část celkového přenosu.

Vytvoření EHC bylo motivováno potřebou optimalizovat využití rádiových prostředků pro služby založené na Ethernetu, které jsou základními kameny mnoha vertikálních odvětví. 3GPP Release 16, který zavedl vylepšenou podporu pro vertikální [LAN](/mobilnisite/slovnik/lan/) služby a časově citlivé sítě, identifikoval přenos Ethernetu jako klíčový požadavek. EHC tuto funkcionalitu přímo podporuje minimalizací režie na rozhraní vzdušného přenosu, čímž zvyšuje spektrální účinnost, snižuje latenci a zvyšuje kapacitu pro ethernetové toky. Řeší problém efektivní integrace sítí vrstvy 2 založených na Ethernetu se systémy celulární komunikace 3GPP, což umožňuje, aby 5G fungovalo jako bezproblémový ethernetový most pro průmyslové a podnikové aplikace.

## Klíčové vlastnosti

- Komprese ethernetových MAC adres, VLAN tagů a polí EtherType
- Fungování ve vrstvě PDCP pro integraci s existujícími rádiovými protokoly
- Podpora více kompresních profilů pro různé typy ethernetových rámců
- Robustní mechanismy synchronizace kontextu mezi kompresorem a dekompresorem
- Konfigurace prostřednictvím signalizace RRC pro dynamickou kontrolu ze strany sítě
- Snížení režie na paket za účelem zlepšení spektrální účinnosti a latence

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)
- **TS 38.463** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [EHC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ehc/)
