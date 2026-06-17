---
slug: "hs-pdsch"
url: "/mobilnisite/slovnik/hs-pdsch/"
type: "slovnik"
title: "HS-PDSCH – High Speed Physical Downlink Shared Channel"
date: 2025-01-01
abbr: "HS-PDSCH"
fullName: "High Speed Physical Downlink Shared Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hs-pdsch/"
summary: "Fyzický kanál, který přenáší High Speed Downlink Shared Channel (HS-DSCH) v UMTS HSPA. Jedná se o skutečnou rádiovou vlnovou formu, která vysílá vysokorychlostní paketová data uživatelům, využívá sdíl"
---

HS-PDSCH je fyzický kanál v UMTS HSPA, který přenáší vysokorychlostní paketová data uživatelům tím, že nese HS-DSCH jako rádiovou vlnovou formu, využívá sdílené kódy a adaptivní modulaci.

## Popis

High Speed Physical Downlink Shared Channel (HS-PDSCH) je realizací přenosového kanálu High Speed Downlink Shared Channel ([HS-DSCH](/mobilnisite/slovnik/hs-dsch/)) na fyzické vrstvě v UMTS High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)). Je to rádiový přenašeč, přes který jsou skutečné datové pakety uživatele přenášeny z Node B do User Equipment (UE). V daném Transmission Time Interval (TTI) může být jednomu UE přiděleno více HS-PDSCH kanálů pro dosažení vyšších datových rychlostí a tyto kanály jsou sdíleny mezi všemi UE v buňce na bázi TTI. HS-PDSCH se vyznačuje použitím pevného rozprostíracího faktoru (SF=16) a provozem na sekundárních skramblovacích kódech, což jej odlišuje od primárního skramblovacího kódu používaného pro společné a dedikované kanály.

Z pohledu fyzické vrstvy nese HS-PDSCH zakódované a modulované transportní bloky HS-DSCH. Kanál využívá adaptivní modulaci, přepínající mezi kvadraturní fázovou manipulací (QPSK), 16-kvadraturní amplitudovou modulací ([16QAM](/mobilnisite/slovnik/16qam/)) a později [64QAM](/mobilnisite/slovnik/64qam/) (od Release 7), na základě Channel Quality Indicator ([CQI](/mobilnisite/slovnik/cqi/)) hlášeného UE. Volba modulace a Transport Block Size (TBS) přímo určuje okamžitou datovou rychlost. Kanalizační kódy pro HS-PDSCH jsou čerpány z fondu kódů s rozprostíracím faktorem 16, odděleně od stromu kódů používaného pro dedikované kanály ([DCH](/mobilnisite/slovnik/dch/)). UE může být v rámci TTI přiděleno mezi 1 a 15 takových kódů, v závislosti na jeho schopnostech (kategorie UE), podmínkách na kanálu a rozhodnutí plánovače. Sada kódů je UE indikována prostřednictvím přidruženého [HS-SCCH](/mobilnisite/slovnik/hs-scch/).

Přenosový proces je těsně synchronizován. V každém 2ms TTI (subrámci) plánovač Node B rozhodne, kterému UE (kterým UE) bude obsluhovat, vybere modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) a přidělí konkrétní sadu kanalizačních kódů. Tyto řídicí informace jsou odesílány na HS-SCCH, který začíná dva sloty (přibližně 1,33 ms) před odpovídajícím přenosem HS-PDSCH. To dává UE čas na dekódování HS-SCCH a nastavení přijímače pro nadcházející přenos dat. Samotný HS-PDSCH nenese žádné explicitní řídicí informace; všechny potřebné parametry pro dekódování poskytuje HS-SCCH. Po pokusu o dekódování dat odešle UE HARQ potvrzení (ACK nebo NACK) na uplinkovém HS-DPCCH. Zpracování na fyzické vrstvě zahrnuje kanálové kódování (Turbo kód), segmentaci fyzického kanálu a prokládání, jak je definováno pro přenosový kanál HS-DSCH, před mapováním na symboly fyzického kanálu HS-PDSCH.

## K čemu slouží

HS-PDSCH byl vytvořen jako prvek fyzické vrstvy umožňující koncept vysokorychlostního sdíleného kanálu HSDPA. Před HSDPA byla downlinková uživatelská data v UMTS přenášena primárně na Dedicated Physical Channel (DPCH), což bylo pro přerušovaná paketová data neefektivní. DPCH používal proměnný rozprostírací faktor a vyžadoval trvalé přidělení kódu na uživatele, což vedlo k vyčerpání stromu kódů a omezeným špičkovým rychlostem. HS-PDSCH tyto nedostatky odstranil přijetím pevného, nízkého rozprostíracího faktoru (SF=16) a provozem na sekundárních skramblovacích kódech, čímž uvolnil primární strom kódů pro hlas a signalizaci. Tento návrh umožnil systému přidělit jednomu uživateli na velmi krátkou dobu (2 ms) velký souvislý blok kanalizačních kódů (až 15), což umožnilo velmi vysoké špičkové datové rychlosti.

Jeho zavedení vyřešilo základní problém fyzické vrstvy, který tvořil úzké hrdlo pro downlinkovou propustnost. Pevným nastavením rozprostíracího faktoru byla efektivně zvýšena čipová rychlost na symbol, což v kombinaci s modulací vyššího řádu umožnilo více datových bitů na symbol. Použití sekundárních skramblovacích kódů vytvořilo paralelní, vyhrazený fond zdrojů pro vysokorychlostní data, který nenarušoval provoz starších kanálů Release 99. Krátké TTI a oddělení řízení (HS-SCCH) od dat (HS-PDSCH) navíc umožnily rychlé a flexibilní plánování a adaptaci spoje, které jsou charakteristickými rysy HSPA. HS-PDSCH je tedy fyzickým pracovním nástrojem, který přeměnil vylepšení přenosového kanálu HSDPA na hmatatelné zisky v rádiovém výkonu, čímž učinil UMTS konkurenceschopným vůči ostatním technologiím bezdrátového širokopásmového přístupu.

## Klíčové vlastnosti

- Pevný rozprostírací faktor 16, provoz na sekundárních skramblovacích kódech
- Podpora adaptivní modulace (QPSK, 16QAM, 64QAM) na základě CQI od UE
- Transmission Time Interval (TTI) o délce 2 ms (3 sloty)
- Dynamicky přidělovaná sada kanalizačních kódů (1 až 15 kódů na UE)
- Nese uživatelskou datovou náplň přenosového kanálu HS-DSCH
- Vždy je asociován s řídicím kanálem HS-SCCH pro parametry dekódování

## Související pojmy

- [HS-DSCH – High Speed Downlink Shared Channel](/mobilnisite/slovnik/hs-dsch/)
- [HS-SCCH – High Speed Physical Downlink Shared Control Channel](/mobilnisite/slovnik/hs-scch/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [HS-PDSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/hs-pdsch/)
