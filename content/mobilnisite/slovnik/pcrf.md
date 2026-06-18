---
slug: "pcrf"
url: "/mobilnisite/slovnik/pcrf/"
type: "slovnik"
title: "PCRF – Policy and Charging Rules Function"
date: 2026-01-01
abbr: "PCRF"
fullName: "Policy and Charging Rules Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pcrf/"
summary: "PCRF je řídicím centrem („mozkem“) architektury Policy and Charging Control (PCC) v 3GPP sítích. Činí rozhodnutí o politikách v reálném čase pro datové toky služeb na základě profilů účastníků, stavu"
---

PCRF je síťová funkce, která provádí rozhodnutí o politikách a účtování v reálném čase na základě dat o účastníkovi a tyto pravidla zřizuje v prosazovacích bodech pro dynamické řízení služeb.

## Popis

Policy and Charging Rules Function (PCRF) je základní síťový prvek v rámci rámce Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) standardů 3GPP, zavedený v EPS (Evolved Packet System) a pokračující v 5G System (5GS). Funguje jako centrální bod pro rozhodování o politikách. PCRF přijímá vstupy z více zdrojů: data o účastníkovi z Subscription Profile Repository ([SPR](/mobilnisite/slovnik/spr/)) nebo Unified Data Repository ([UDR](/mobilnisite/slovnik/udr/)), informace o službě z Application Function ([AF](/mobilnisite/slovnik/af/)), jako je [P-CSCF](/mobilnisite/slovnik/p-cscf/), a stav sítě z Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)) nebo z vlastního monitorování. Tyto informace kombinuje s předdefinovanými politikami operátora, aby učinil závazná rozhodnutí v reálném čase o tom, jak mají být jednotlivé datové toky služeb zacházeny.

Tato rozhodnutí jsou zapouzdřena v pravidlech PCC (PCC rules), která jsou odesílána Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)), typicky umístěné společně s Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v 4G nebo s Session Management Function (SMF) v 5G. Pravidlo PCC obsahuje identifikátory pro datový tok služby (např. IP 5-tice), požadované parametry QoS (QCI, ARP, přenosové rychlosti) a pokyny k účtování (online, offline, charging key). PCEF tato pravidla následně instaluje a prosazuje jejich aplikaci odpovídajících paketových filtrů, značkování QoS (DSCP) a měření provozu pro účely účtování. PCRF může pravidla dynamicky měnit nebo odstraňovat během relace v reakci na události, jako je změna tarifní úrovně účastníka, zahlcení sítě nebo spuštění/zastavení sponzorované datové služby.

Architektonicky rozhraní PCRF s mnoha síťovými funkcemi prostřednictvím standardizovaných referenčních bodů. Rozhraní Rx se připojuje k AF (pro politik založené na službě), rozhraní Gx k PCEF (pro zřizování pravidel), rozhraní Sp k SPR/UDR (pro data účastníka) a rozhraní Sy k Online Charging System (OCS). V 5G je role PCRF z velké části převzata funkcí Policy Control Function (PCF), která následuje podobnou služebně orientovanou architekturu, ale s rozšířenými schopnostmi pro síťové řezy a edge computing. PCRF/PCF je klíčovým prvkem pro pokročilé obchodní modely, který operátorům umožňuje přejít od paušálního účtování k podrobnému, podle služeb diferencovanému účtování a zajišťování kvality.

## K čemu slouží

PCRF byl vyvinut, aby odstranil omezení statického, předkonfigurovaného řízení politik v dřívějších mobilních datových sítích (GPRS, raný 3G). V těchto sítích byly QoS a účtování z velké části určeny statickou konfigurací APN (Access Point Name) účastníka, což nabízelo malou flexibilitu pro přizpůsobení se konkrétním aplikacím nebo podmínkám sítě v reálném čase. Tento přístup „jedna velikost pro všechny“ bránil zpoplatnění nových služeb (jako VoIP, video streamování) a efektivnímu využití síťových zdrojů.

Hnací motivací bylo vytvořit dynamický rámec pro správu politik, který je citlivý na aplikace. PCRF umožňuje operátorům implementovat sofistikované služební plány (např. zero-rating pro sociální média, prémiové QoS pro cloudové hraní, omezování šířky pásma po překročení datového limitu). Řeší potřebu interakce v reálném čase mezi servisní vrstvou (aplikacemi) a transportní vrstvou (přenosovou sítí). Díky centralizaci rozhodování o politikách poskytuje PCRF konzistentní kontrolní bod a zajišťuje, že je politika uplatňována jednotně bez ohledu na přístupovou technologii uživatele (3G, 4G, non-3GPP). Jeho vznik byl úzce spjat s plně IP architekturou EPS, kde tradiční okruhově přepínaná doména pro hlas byla nahrazena paketově přepínaným IMS (IP Multimedia Subsystem), což vyžadovalo těsnou integraci signalizace služeb a správy přenosových kanálů pro zajištění kvality.

## Klíčové vlastnosti

- Centralizované rozhodování o politikách v reálném čase na základě dat o účastníkovi, službě a síti.
- Dynamické zřizování pravidel PCC (PCC rules) v prosazovacích bodech (PCEF) prostřednictvím rozhraní Gx.
- Podpora řízení QoS citlivého na službu, definující parametry jako QCI, GBR a MBR pro každý datový tok.
- Integrace se systémy účtování, určující pravidla a spouštěče pro online a offline účtování.
- Interakce s Application Functions (AF) prostřednictvím rozhraní Rx pro politiku založenou na službě (např. IMS).
- Schopnost aktualizace politik spouštěné událostmi (např. při změně lokace, denní době nebo dosažení prahu využití).

## Související pojmy

- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 23.768** (Rel-12) — Group Communication System Enablers for LTE
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- … a dalších 43 specifikací

---

📖 **Anglický originál a plná specifikace:** [PCRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcrf/)
