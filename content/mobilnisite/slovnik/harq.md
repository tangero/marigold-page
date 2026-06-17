---
slug: "harq"
url: "/mobilnisite/slovnik/harq/"
type: "slovnik"
title: "HARQ – Hybrid Automatic Repeat Request"
date: 2025-01-01
abbr: "HARQ"
fullName: "Hybrid Automatic Repeat Request"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/harq/"
summary: "Klíčová technika řízení chyb kombinující kódování s opravou chyb (FEC) a automatický opakovaný dotaz (ARQ). Zlepšuje spolehlivost přenosu dat a spektrální účinnost přes bezdrátové kanály tím, že umožň"
---

HARQ je klíčová technika řízení chyb, která kombinuje kódování s opravou chyb (FEC) a automatický opakovaný dotaz (ARQ) za účelem zlepšení spolehlivosti přenosu dat a spektrální účinnosti tím, že umožňuje rychlé retransmise na fyzické vrstvě v mobilních sítích.

## Popis

Hybrid Automatic Repeat Request (HARQ) je základní mechanismus řízení chyb používaný na fyzické vrstvi 3GPP rádiových přístupových technologií, včetně UMTS ([HSPA](/mobilnisite/slovnik/hspa/)), LTE a 5G NR. Funguje na principu integrace dvou klasických metod řízení chyb: kódování s opravou chyb (Forward Error Correction, [FEC](/mobilnisite/slovnik/fec/)) a automatického opakovaného dotazu (Automatic Repeat Request, [ARQ](/mobilnisite/slovnik/arq/)). Jeho 'hybridní' povaha vychází právě z této kombinace. Při provozu vysílač odešle datový paket zakódovaný pomocí FEC. Příjemce se jej pokusí dekódovat. Pokud dekódování selže, příjemce místo zahození poškozeného paketu jej uloží a odešle vysílači záporné potvrzení (Negative Acknowledgement, [NACK](/mobilnisite/slovnik/nack/)). Po přijetí NACK vysílač odešle retransmisi. Příjemce následně před dalším pokusem o dekódování zkombinuje měkká data (např. logaritmy věrohodnostních poměrů) z počátečního přenosu a retransmise. Tento proces, známý jako měkké kombinování (soft combining), výrazně zvyšuje pravděpodobnost úspěšného dekódování ve srovnání s přístupem, kdy se každý přenos zpracovává nezávisle.

HARQ je implementován pomocí více paralelních procesů, známých jako HARQ procesy, aby byla zachována kontinuální datová přenosová cesta. Každý proces zpracovává přenos a případnou retransmisi jednoho transportního bloku. Zatímco jeden proces čeká na potvrzení ([ACK](/mobilnisite/slovnik/ack/)/NACK), jiný proces může vysílat nová data, čímž se skryje latence doby zpátečního přenosu. Protokol je řízen vrstvou řízení přístupu k médiu (Medium Access Control, [MAC](/mobilnisite/slovnik/mac/)), která zpracovává generování zpětné vazby ACK/NACK, plánování retransmisí a správu HARQ vyrovnávacích pamětí. Fyzická vrstva je zodpovědná za vlastní kódování, modulaci a operaci měkkého kombinování.

Klíčové varianty zahrnují Chase Combining, kde jsou retransmitovány identické kopie paketu, a přírůstkovou redundanci (Incremental Redundancy, [IR](/mobilnisite/slovnik/ir/)), kde každá retransmise obsahuje různé paritní bity, čímž se s každým pokusem efektivně zvyšuje kódová rychlost. HARQ je úzce propojen s adaptivní modulací a kódováním (Adaptive Modulation and Coding, [AMC](/mobilnisite/slovnik/amc/)). Počáteční přenos používá schéma modulace a kódování (Modulation and Coding Scheme, MCS) vybrané na základě ukazatelů kvality kanálu (Channel Quality Indicator, CQI). HARQ poskytuje druhou linii obrany, pokud se kanál po výběru MCS neočekávaně zhorší. Jeho role je naprosto zásadní pro dosažení vysoké spolehlivosti a cílů spektrální účinnosti moderních celulárních systémů, protože umožňuje systému pracovat blíže kapacitnímu limitu kanálu díky efektivnímu zotavení z chyb.

## K čemu slouží

HARQ byl vytvořen, aby řešil základní výzvu spolehlivého přenosu dat přes inherentně nespolehlivé a časově proměnné bezdrátové kanály. Tradiční schémata ARQ, která jednoduše zahazují chybné pakety a žádají o retransmise, jsou pro bezdrátové spoje neefektivní kvůli vysoké latenci a plýtvání šířkou pásma. Čistá schémata FEC, která přidávají velkou redundanci pro opravu chyb, jsou zase neefektivní za dobrých podmínek na kanálu. Účelem HARQ je synergicky kombinovat to nejlepší z obou přístupů: proaktivní schopnost opravy chyb FEC pro zvládnutí běžných změn kanálu a reaktivní obnovu chyb ARQ pro zvládnutí hlubokých útlumů nebo neočekávaných interferencí, avšak mnohem efektivnějším způsobem než samostatný ARQ.

Jeho zavedení v 3GPP Release 5 s technologií High-Speed Downlink Packet Access (HSDPA) bylo klíčovým okamžikem pro umožnění vysokorychlostního mobilního broadbandu. Předchozí systémy 3G spoléhaly na ARQ na RLC vrstvě, které měly vyšší latenci a byly méně efektivní pro služby v reálném čase. HARQ, fungující na fyzické/MAC vrstvě s mnohem kratší dobou zpátečního přenosu, drasticky snížil zpoždění retransmise a zlepšil propustnost. To bylo nezbytné pro podporu aplikací citlivých na latenci, jako je hlas přes IP (VoIP) a interaktivní video. Vývoj přes LTE a 5G NR dále zdokonalil HARQ pro podporu složitějších scénářů, jako je agregace nosných, masivní MIMO a ultra-spolehlivá komunikace s nízkou latencí (Ultra-Reliable Low-Latency Communication, URLLC), kde je jeho rychlá a spolehlivá oprava chyb základním kamenem technologie.

## Klíčové vlastnosti

- Kombinuje FEC a ARQ pro efektivní řízení chyb
- Používá na straně přijímače měkké kombinování (Chase Combining nebo přírůstkovou redundanci)
- Využívá více paralelních HARQ procesů ke skrytí latence doby zpátečního přenosu
- Funguje na MAC/fyzické vrstvě pro minimální zpoždění retransmise
- Pracuje v úzké součinnosti s adaptivní modulací a kódováním (AMC)
- Podporuje jak synchronní, tak asynchronní režimy provozu

## Související pojmy

- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)
- [FEC – Forward Erasure Correction / Forward Error Correction](/mobilnisite/slovnik/fec/)
- [HARQ-ACK – Hybrid Automatic Repeat Request Acknowledgement](/mobilnisite/slovnik/harq-ack/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- … a dalších 40 specifikací

---

📖 **Anglický originál a plná specifikace:** [HARQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/harq/)
