---
slug: "crc"
url: "/mobilnisite/slovnik/crc/"
type: "slovnik"
title: "CRC – Cyclic Redundancy Check"
date: 2025-01-01
abbr: "CRC"
fullName: "Cyclic Redundancy Check"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/crc/"
summary: "CRC je kód pro detekci chyb používaný k odhalení náhodných změn v nezpracovaných datech během digitálního přenosu nebo ukládání. K datovému bloku připojuje krátkou kontrolní hodnotu pevné délky vypočt"
---

CRC je kód pro detekci chyb, který k datům připojuje krátkou kontrolní hodnotu vypočtenou z datových bitů, aby detekoval náhodné změny a zajistil integritu dat napříč rozhraními a protokoly 3GPP rádiového přístupu.

## Popis

Cyclic Redundancy Check (CRC) je nezabezpečená hašovací funkce navržená pro detekci náhodných chyb v digitálních datech. Funguje tak, že zprávu (datový blok) považuje za velké binární číslo, které je vyděleno předem definovaným generátorovým polynomem. Zbytek z tohoto polynomiálního dělení se stává kontrolním součtem CRC, který je připojen k původnímu datovému bloku před přenosem. Na přijímací straně je proveden stejný výpočet s přijatými daty (včetně připojeného CRC). Pokud je vypočtený zbytek nula, data jsou považována za bezchybná; nenulový zbytek indikuje, že jeden nebo více bitů bylo během přenosu poškozeno. Tento proces je formou binární polynomiální aritmetiky modulo-2, typicky efektivně implementovanou v hardwaru pomocí lineárních zpětnovazebních posuvných registrů (LFSR).

V systémech 3GPP je CRC aplikován na více vrstvách a pro různé typy kanálů. Například ve fyzické vrstvě LTE a NR je CRC připojeno k transportním blokům ([TB](/mobilnisite/slovnik/tb/) CRC) před kanálovým kódováním (jako jsou [LDPC](/mobilnisite/slovnik/ldpc/) nebo Polar kódy), aby detekovalo chyby po dekódování. Samostatné CRC je také připojeno k segmentům kódových bloků, když je transportní blok velký, čímž vznikají skupiny kódových bloků ([CBG](/mobilnisite/slovnik/cbg/)) pro efektivnější retransmise v NR. Délka CRC (např. 24 bitů, 16 bitů, 8 bitů) je volena na základě požadované pravděpodobnosti detekce chyby a velikosti datového bloku. Mezi běžné polynomy definované v specifikacích 3GPP patří CRC24A, CRC24B, CRC24C, CRC16 a CRC8.

Role CRC přesahuje pouhou detekci chyb. Je nedílnou součástí procesu hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)). Přijímač používá kontrolu CRC ke generování potvrzení [ACK](/mobilnisite/slovnik/ack/) (kladné) nebo [NACK](/mobilnisite/slovnik/nack/) (záporné), což spouští retransmise, pokud jsou detekovány chyby. Dále je CRC používáno pro řídicí signalizaci v pásmu. Například řídicí informace pro downlink ([DCI](/mobilnisite/slovnik/dci/)) na [PDCCH](/mobilnisite/slovnik/pdcch/) nese vlastní CRC, které je následně zamícháno s dočasným identifikátorem rádiové sítě (RNTI). To umožňuje UE ověřit, zda je řídicí zpráva určena právě jemu, protože úspěšná kontrola CRC po odšifrování s přiřazeným RNTI potvrzuje platnost adresy.

Z architektonického hlediska je výpočet CRC povinným krokem ve zpracovatelských řetězcích jak uživatelské roviny, tak řídicí roviny. Je podrobně specifikován pro fyzické kanály (PDSCH, PUSCH, PDCCH), transportní kanály (DL-SCH, UL-SCH) a logické kanály. Jeho implementace je klíčovým faktorem pro dosažení vysoké spolehlivosti a nízké latence, které jsou cílem 5G NR, zejména pro služby ultra-spolehlivé komunikace s nízkou latencí (URLLC), kde by neodhalené chyby mohly mít závažné důsledky.

## K čemu slouží

CRC existuje jako spolehlivý a nenáročný mechanismus pro detekci náhodných bitových chyb vzniklých během přenosu dat přes šumové komunikační kanály. V bezdrátových systémech jsou signály náchylné k rušení, útlumu a šumu, což činí detekci chyb prvořadou. Bez takového mechanismu by poškozená data byla předávána vyšším vrstvám, což by vedlo ke zkaženému obsahu, neúspěšným procedurám a nestabilitě systému. CRC tento problém řeší tím, že poskytuje vysokou pravděpodobnost detekce shlukových chyb běžných v rádiovém prostředí.

Motivace pro jeho použití v 3GPP, sahající až k Release 99, vychází z jeho vynikající rovnováhy mezi detekční schopností, výpočetní jednoduchostí a nízkou režií. Ve srovnání s jednoduššími kontrolními součty, jako jsou paritní bity, mohou být CRC polynomy navrženy tak, aby detekovaly všechny jednobitové chyby, všechny dvoubitové chyby, jakýkoli lichý počet chyb a jakoukoli shlukovou chybu kratší než je délka samotného CRC. To jej činí výrazně lepším pro ochranu paketových dat v UMTS, LTE a NR. Jeho hardwarově příznivá implementace pomocí LFSR umožňuje vysokorychlostní zpracování s nízkou latencí, což je zásadní pro splnění přísných časových požadavků zpracování rádiových rámců.

Před standardizovaným použitím CRC systémy spoléhaly na méně robustní detekci chyb nebo pouze na složitější kódy pro opravu chyb (FEC). CRC doplňuje schémata FEC (jako jsou Turbo nebo LDPC kódy) tím, že detekuje reziduální chyby, které dekodér FEC nedokázal opravit. Tento hybridní přístup – FEC pro opravu, CRC pro detekci – tvoří páteř moderní adaptace spojení a HARQ, což umožňuje efektivní využití rádiových prostředků tím, že spouští retransmise pouze v případě potřeby. Jeho vytvoření a standardizace byly hnací silou potřeby univerzálně použitelné, robustní vrstvy pro detekci chyb, která by zajistila integritu dat od konce ke konci ve vyvíjejících se systémech mobilní širokopásmové komunikace.

## Klíčové vlastnosti

- Detekuje náhodné a shlukové chyby s velmi vysokou pravděpodobností
- Implementováno pomocí binárního polynomiálního dělení s využitím lineárních zpětnovazebních posuvných registrů (LFSR)
- Podporuje více délek polynomů (např. 24, 16, 8 bitů) pro různé kanály a velikosti dat
- Nedílná součást procesu HARQ pro generování zpětné vazby ACK/NACK
- Používáno pro identifikaci UE zamícháním CRC s RNTI v řídicích kanálech
- Umožňuje retransmise založené na skupinách kódových bloků (CBG) v 5G NR pro snížení latence

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- … a dalších 45 specifikací

---

📖 **Anglický originál a plná specifikace:** [CRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/crc/)
