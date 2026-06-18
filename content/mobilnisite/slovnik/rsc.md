---
slug: "rsc"
url: "/mobilnisite/slovnik/rsc/"
type: "slovnik"
title: "RSC – Recursive Systematic Convolutional Coder"
date: 2026-01-01
abbr: "RSC"
fullName: "Recursive Systematic Convolutional Coder"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rsc/"
summary: "RSC je typ konvolučního kódu používaný pro dopřednou korekci chyb v systémech 3GPP, zejména v UMTS a raném LTE. Zlepšuje spolehlivost dat přidáním redundantních bitů v rekurzivní systematické formě, c"
---

RSC je konvoluční kód používaný pro dopřednou korekci chyb v systémech 3GPP, který přidává redundantní bity v rekurzivní systematické formě za účelem zlepšení spolehlivosti dat na šumových kanálech.

## Popis

Rekurzivní systematický konvoluční (RSC) kodér je komponenta pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)) používaná v radiových přístupových technologiích 3GPP, zejména v UMTS (3G) a některých aspektech LTE. Funguje jako konvoluční kodér, který generuje paritní bity ze vstupních datových proudů, a je charakteristický svou rekurzivní strukturou a systematickým výstupem – což znamená, že vstupní bity jsou přímo zahrnuty do zakódovaného proudu spolu s paritními bity. Tento návrh zlepšuje schopnosti korekce chyb při zachování kompatibility s iteračními dekódovacími algoritmy, jako je Viterbiho algoritmus nebo turbo dekódování. Ve specifikacích 3GPP se RSC často používá v rámci turbo kódovacích schémat, kde dva RSC kodéry pracují paralelně s prokladačem za účelem vytvoření vysoce spolehlivých kódů.

Architektura RSC v systémech 3GPP zahrnuje integraci do řetězce kódování kanálu fyzické vrstvy. Například v UMTS, jak je definováno v TS 25.212, jsou RSC kodéry součástí turbo kódu pro datové kanály a zpracovávají transportní bloky před modulací a přenosem. Kodér se skládá z posuvných registrů a zpětnovazebních smyček, přičemž parametry jako délka vazby a generující polynomy jsou specifikovány pro optimalizaci výkonu za různých podmínek kanálu. Mezi klíčové komponenty patří samotný kodér, prokladače pro promíchání datových sekvencí a jednotky propichování pro úpravu kódové rychlosti selektivním odstraněním paritních bitů, čímž se vyvažuje redundance a spektrální účinnost.

Při provozu RSC přijímá proud informačních bitů a propouští je lineárními zpětnovazebními posuvnými registry. Rekurzivní povaha znamená, že stav kodéru závisí na předchozích vstupech prostřednictvím zpětné vazby, což zlepšuje vzdálenostní vlastnosti kódu a zvyšuje jeho odolnost vůči chybám. Systematický aspekt zajišťuje, že původní data jsou transparentně dostupná, což zjednodušuje dekódování. Na straně přijímače soft-decision dekodéry využívají tuto strukturu ke korekci bitových chyb způsobených šumem, interferencí nebo útlumem. Role RSC je klíčová pro dosažení vysokých přenosových rychlostí a nízké latence vyžadovaných pro hlasové, video a datové služby, protože minimalizuje retransmise a zvyšuje celkovou spolehlivost spoje.

## K čemu slouží

RSC byl zaveden v 3GPP Release 4 pro UMTS, aby řešil potřebu efektivnější korekce chyb ve srovnání s nerekurzivními konvolučními kódy používanými v dřívějších systémech 2G. Předchozí kódy, jako například v GSM, měly omezené zisky výkonu a vyžadovaly vyšší poměr signálu k šumu pro přijatelné chybovosti. RSC, zejména v kombinaci v turbo kódech, nabídl výkon blízký Shannonově limitu, což umožnilo spolehlivou komunikaci na rušných rádiových kanálech s nižší spotřebou energie a lepší spektrální účinností.

Vznik RSC byl motivován rostoucí poptávkou po vysokorychlostních datových službách v sítích 3G, jako je videohovor a mobilní internet. Tradiční kódy nemohly podporovat vyšší přenosové rychlosti bez nadměrné režie nebo degradace kvality. Rekurzivní systematická forma RSC umožnila lepší iterační dekódování, což jej učinilo vhodným pro implementace turbo kódování, které výrazně zvýšily propustnost a pokrytí. Tento pokrok byl zásadní pro splnění výkonnostních cílů UMTS a později LTE a podporoval funkce jako adaptivní modulace a kódování ([AMC](/mobilnisite/slovnik/amc/)) a hybridní [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)).

Navíc zavedení RSC umožnilo robustnější scénáře mobility a předávání spojení, protože poskytovalo konzistentní ochranu proti chybám za různých podmínek kanálu. Jeho flexibilita v úpravě kódové rychlosti prostřednictvím propichování umožnila dynamickou adaptaci na kvalitu spoje a optimalizaci využití zdrojů. S vývojem 3GPP zůstal RSC relevantní v LTE pro některé řídicí kanály a podporu starších verzí, ačkoli novější kódy jako [LDPC](/mobilnisite/slovnik/ldpc/) a polární kódy od té doby převzaly dominantní úlohu v 5G NR pro datové kanály. Přesto RSC zůstává základní technologií v historii celulární korekce chyb.

## Klíčové vlastnosti

- Rekurzivní struktura se zpětnou vazbou pro vylepšenou korekci chyb
- Systematický výstup obsahuje původní datové bity spolu s paritou
- Používá se jako komponentní kodéry v turbo kódovacích schématech
- Podporuje proměnné kódové rychlosti prostřednictvím propichování
- Umožňuje iterační dekódování pro téměř optimální výkon
- Integruje se s prokladači pro odolnost vůči shlukovým chybám

## Související pojmy

- [FEC – Forward Erasure Correction / Forward Error Correction](/mobilnisite/slovnik/fec/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 23.304** (Rel-20) — 5G Proximity Services (ProSe) Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.555** (Rel-19) — 5G ProSe UE Policies Specification
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TR 33.740** (Rel-18) — Security and Privacy Aspects of Proximity Based Services in 5G System Phase 2

---

📖 **Anglický originál a plná specifikace:** [RSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsc/)
