---
slug: "ma"
url: "/mobilnisite/slovnik/ma/"
type: "slovnik"
title: "MA – PDU Multi-Access PDU"
date: 2026-01-01
abbr: "MA"
fullName: "PDU Multi-Access PDU"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ma/"
summary: "Protokolová datová jednotka podporující vícepřístupové připojení, která umožňuje jedné datové relaci současně využívat více typů síťového přístupu. Je zásadní pro ATSSS (řízení, přepínání a rozdělován"
---

MA je protokolová datová jednotka podporující vícepřístupové připojení, která umožňuje jedné datové relaci současně využívat více typů síťového přístupu.

## Popis

[PDU](/mobilnisite/slovnik/pdu/) Multi-Access PDU (MA PDU) je protokolová datová jednotka navržená pro současný provoz přes více podkladových přístupových sítí, jako je 3GPP přístup (např. 5G NR) a non-3GPP přístup (např. Wi-Fi). Je klíčovým prvkem pro funkci [ATSSS](/mobilnisite/slovnik/atsss/) (řízení, přepínání a rozdělování přístupového provozu) definovanou v 3GPP, která umožňuje síti a uživatelskému zařízení inteligentně distribuovat datové toky přes více dostupných přístupů. MA PDU funguje na vrstvě nad jednotlivými přístupově specifickými vrstvami [PDCP](/mobilnisite/slovnik/pdcp/) (Packet Data Convergence Protocol) nebo ekvivalentními vrstvami a poskytuje jednotnou relací vrstvu, která může agregovat, směrovat nebo přepínat provoz na základě politik, kvality spojení a požadavků aplikace.

Z architektonického hlediska je MA PDU spravován kotvou Multi-Access PDU Session, což je funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v 5G Core síti. Tato kotva ukončuje relaci MA PDU a je zodpovědná za integraci provozu z více přístupů. V uživatelském zařízení (UE) odpovídající vícepřístupová (MA) protokolová vrstva, často realizovaná jako adaptační vrstva nebo v rámci frameworku ATSSS, zpracovává konstrukci a zpracování MA PDU. Tato vrstva komunikuje s nižšími vrstvami specifickými pro každou přístupovou technologii, přijímá data z aplikační vrstvy a na základě pravidel ATSSS rozhoduje, kterou přístupovou síť (sítě) použít pro přenos, případně rozděluje jediný tok.

Provoz zahrnuje aplikaci režimů směrování MA vrstvou – jako je aktivní-rezervní, nejmenší zpoždění, vyrovnávání zátěže nebo na základě priority – k nasměrování provozu. Pro rozdělování může segmentovat pakety vyšší vrstvy do více dílčích toků, z nichž každý je přiřazen jinému přístupu, s mechanismy pro číslování sekvencí a opětovné sestavení pro zvládnutí doručení mimo pořadí. Samotná MA PDU nese nezbytné řídicí informace, případně včetně sekvenčních čísel a identifikátorů přístupových sítí, aby umožnila správné opětovné sestavení a monitorování na přijímací straně. Její role je klíčová pro zlepšení uživatelského zážitku prostřednictvím vyšší spolehlivosti, větší agregované šířky pásma a bezproblémové mobility mezi heterogenními sítěmi, čímž tvoří základní součást koncepce konvergence 5G.

## K čemu slouží

MA [PDU](/mobilnisite/slovnik/pdu/) byla vytvořena pro řešení rostoucí potřeby bezproblémového a efektivního využití více technologií síťového přístupu dostupných zařízení. Historicky se zařízení mohla připojovat k různým sítím (např. mobilní a Wi-Fi), ale obvykle je používala vzájemně výlučným způsobem pro každou datovou relaci, přičemž přepínání často způsobovalo přerušení relace. To omezovalo schopnost využít kombinované zdroje pro lepší výkon nebo spolehlivost. Rozšíření heterogenních přístupových sítí a požadavky na ultra-spolehlivé služby s vysokou šířkou pásma v 5G si vyžádaly integrovanější přístup.

Primární problém, který řeší, je pevné svázání PDU relace s jediným typem přístupu. Zavedením MA PDU umožňuje 3GPP vytvoření jediné PDU relace přes více přístupů současně. To umožňuje směrování, přepínání a rozdělování provozu na základě dynamických síťových podmínek, politik a potřeb aplikací. Motivovaly ji případy užití vyžadující vylepšenou mobilitu (bezproblémový předávání mezi 3GPP a non-3GPP), lepší spolehlivost prostřednictvím redundance a zvýšení propustnosti pomocí agregace. Technologie řeší omezení předchozích jednopřístupových relací a neintegrovaných řešení vícekonektivity a poskytuje standardizovaný, síťově řízený rámec pro správu více přístupů.

## Klíčové vlastnosti

- Umožňuje současné využití 3GPP a non-3GPP přístupových sítí v rámci jediné PDU relace
- Podporuje režimy směrování ATSSS: aktivní-rezervní, nejmenší zpoždění, vyrovnávání zátěže a na základě priority
- Umožňuje rozdělení jediného IP toku přes více přístupů pro agregaci šířky pásma
- Poskytuje mechanismy pro číslování sekvencí a zajištění doručení ve správném pořadí přes heterogenní cesty
- Umožňuje síťově řízené politiky směrování provozu prostřednictvím 5G Core
- Zvyšuje kontinuitu a spolehlivost relace prostřednictvím přístupové redundance

## Související pojmy

- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.606** (Rel-19) — MWI Service Protocol Description
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [MA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ma/)
