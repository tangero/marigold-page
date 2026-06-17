---
slug: "p-gw"
url: "/mobilnisite/slovnik/p-gw/"
type: "slovnik"
title: "P-GW – Packet Data Network Gateway"
date: 2025-01-01
abbr: "P-GW"
fullName: "Packet Data Network Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/p-gw/"
summary: "P-GW je uzel jádra sítě v 3GPP EPS, který slouží jako rozhraní mezi mobilní sítí a externími paketovými sítěmi (PDN), jako je internet. Provádí klíčové funkce včetně přidělování IP adres, uplatňování"
---

P-GW je uzel jádra sítě, který propojuje mobilní síť s externími paketovými sítěmi, jako je internet, a zajišťuje alokaci IP adres, uplatňování politik, účtování a filtrování paketů.

## Popis

Packet Data Network Gateway (P-GW) je základní součást architektury Evolved Packet Core (EPC) definované ve 3GPP Release 8 a novějších. Funguje jako hlavní brána mezi sítí mobilního operátora a externími Packet Data Networks (PDN), jako je veřejný internet, IMS nebo privátní firemní sítě. P-GW je vstupním a výstupním bodem pro veškerý IP provoz uživatelské roviny pro UE. Je zodpovědný za přidělení IP adresy UE (prostřednictvím [DHCP](/mobilnisite/slovnik/dhcp/) nebo jiných mechanismů) a správu kontextu IP přenosu pro každou datovou relaci. P-GW uplatňuje pravidla politiky a účtování přijatá od Policy and Charging Rules Function (PCRF), aplikuje na pakety blokování, filtrování a označování kvality služeb (QoS). Také provádí hlubokou kontrolu paketů (DPI) pro účtování a uplatňování politik s ohledem na službu.

Z architektonického hlediska P-GW komunikuje s několika klíčovými síťovými prvky. Na straně mobilní sítě se připojuje k Serving Gateway (S-GW) přes rozhraní S5/S8 (založené na [GTP](/mobilnisite/slovnik/gtp/) nebo PMIP) pro provoz uživatelské roviny a signalizaci řídicí roviny. Rozhraní S5 se používá, když jsou S-GW a P-GW v rámci stejné PLMN, zatímco S8 se používá pro roamingové scénáře mezi PLMN. Na straně externí sítě se P-GW připojuje k PDN přes rozhraní SGi, což je standardní IP rozhraní. Pro funkce řídicí roviny komunikuje P-GW s PCRF přes rozhraní Gx, aby přijímal dynamická pravidla politiky a řízení účtování (PCC). Také komunikuje s Online Charging Systems ([OCS](/mobilnisite/slovnik/ocs/)) přes rozhraní Gy a Offline Charging Systems ([OFCS](/mobilnisite/slovnik/ofcs/)) přes rozhraní Gz.

Kritickou úlohou P-GW je fungovat jako kotva pro mobilitu. Když se UE pohybuje mezi různými eNodeB nebo dokonce mezi 3GPP a ne-3GPP přístupovými sítěmi (jako Wi-Fi), P-GW zůstává stabilním připojovacím IP bodem. Tím je zajištěna kontinuita relace, protože IP adresa UE je zachována. P-GW také podporuje pokročilé funkce, jako je Traffic Detection Function (TDF) pro detekci a hlášení aplikací, a Bearer Binding and Event Reporting Function ([BBERF](/mobilnisite/slovnik/bberf/)) pro ne-3GPP přístupy. V novějších releasech 3GPP s příchodem 5G Core (5GC) byly mnohé funkce P-GW integrovány do nové User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), ale P-GW zůstává klíčovým prvkem nasazení 4G EPS a je důležitým prvkem při propojování sítí 4G a 5G.

## K čemu slouží

P-GW byl vytvořen jako součást System Architecture Evolution (SAE) ve 3GPP Release 8, aby řešil omezení předchozích architektur paketového jádra 3G, konkrétně Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN). GGSN v sítích 2G/3G zajišťovala podobné bránové funkce, ale byla součástí méně flexibilní, více monolitické architektury. EPC s P-GW jako samostatnou entitou zavedlo plošší, plně IP architekturu navrženou pro vyšší datovou propustnost, nižší latenci a efektivnější směrování paketů. To bylo zásadní pro podporu rostoucí poptávky po mobilních širokopásmových službách poháněných smartphony a novými aplikacemi.

P-GW řeší několik klíčových problémů. Centralizuje funkce uplatňování politik a účtování, což operátorům umožňuje implementovat sofistikované služební plány a strategie monetizace založené na uživateli, aplikaci nebo stavu sítě. Tím, že funguje jako jediný kotvící IP bod, zjednodušuje správu mobility a umožňuje plynulé předávání mezi různými rádiovými přístupovými technologiemi. Jeho design navíc podporuje hlubokou kontrolu paketů a schopnosti s ohledem na službu, což je klíčové pro implementaci rodičovských kontrol, podnikových VPN a optimalizovaného řízení provozu. Oddělení S-GW a P-GW také umožnilo flexibilnější nasazení sítě, kde může být S-GW distribuováno pro optimalizaci latence, zatímco P-GW může být centralizováno pro konzistentnost politik.

## Klíčové vlastnosti

- Přidělování a správa IP adres pro UE (IPv4, IPv6, duální zásobník)
- Policy and Charging Enforcement Function (PCEF) pro aplikaci QoS, blokování a limitů šířky pásma
- Kotvící bod pro mobilitu uživatelské roviny mezi 3GPP a ne-3GPP přístupy
- Filtrování, kontrola (DPI) a směrování paketů mezi rozhraními SGi a S5/S8
- Interakce s PCRF (Gx), OCS (Gy) a OFCS (Gz) pro dynamickou politiku a účtování
- Podpora více PDN připojení na UE a vyhrazených přenosů

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.468** (Rel-19) — MB2 Reference Point Protocol Definition
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 29.804** (Rel-8) — CT3 Aspects of System Architecture Evolution
- **TS 29.806** (Rel-12) — P-CSCF Restoration Analysis & Solutions
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 29.866** (Rel-19) — IMS Disaster Prevention & Restoration Enhancement
- **TS 31.829** (Rel-13) — ISIM Conformance Requirements Technical Report
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [P-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-gw/)
