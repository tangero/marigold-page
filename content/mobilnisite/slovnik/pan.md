---
slug: "pan"
url: "/mobilnisite/slovnik/pan/"
type: "slovnik"
title: "PAN – Piggy-backed Ack/Nack message"
date: 2025-01-01
abbr: "PAN"
fullName: "Piggy-backed Ack/Nack message"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pan/"
summary: "Zpráva používaná v GSM/EDGE Radio Access Network (GERAN) k potvrzení (ACK) nebo negativnímu potvrzení (NACK) přijatých datových bloků. Je vysílána navázáním řídicí informace na vzestupný datový blok,"
---

PAN je řídicí zpráva v síti GERAN, která potvrzuje nebo negativně potvrzuje přijaté datové bloky tím, že je tato informace přenášena navázána (piggy-backed) na vzestupný datový blok za účelem zlepšení spektrální účinnosti.

## Popis

Zpráva Piggy-backed Ack/Nack (PAN) je základním řídicím mechanismem v protokolovém stacku GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), konkrétně ve vrstvách Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). Funguje v přenosu dat v potvrzovaném režimu (acknowledged mode) pro zajištění spolehlivého doručování rádiových bloků přes rozhraní vzduchu. Když mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) přijme sestupný rádiový blok obsahující RLC data, musí o úspěchu či neúspěchu tohoto příjmu informovat síť. Namísto využití samostatného rádiového bloku pouze pro tuto řídicí zpětnou vazbu je zpráva PAN připojena k vzestupnému RLC datovému bloku, který má MS již naplánován k odeslání. Tento mechanismus navázání (piggy-backing) je klíčovou vlastností protokolu RLC/MAC v GERAN, podrobně popsanou v řadě specifikací 3GPP týkajících se požadavků na služby, architektury a rádiových aspektů.

Technické fungování zahrnuje vygenerování zprávy PAN v MS, která obsahuje bitmapu odpovídající dříve přijatým sestupným blokům. Každý bit v bitmapě představuje stav potvrzení pro konkrétní pořadové číslo bloku. Zpráva je následně multiplexována s uživatelskou datovou náplní vzestupného rádiového bloku před kanálovým kódováním a vysíláním. Příjmová část [BSS](/mobilnisite/slovnik/bss/) (Base Station Subsystem) sítě po přijetí tohoto bloku demultiplexuje informaci PAN. BSS používá tuto zpětnou vazbu k rozhodnutí, zda retransmitovat negativně potvrzený blok, nebo posunout přenosové okno. Tento proces je úzce spojen se správou dočasného toku bloků (Temporary Block Flow - [TBF](/mobilnisite/slovnik/tbf/)) pro přenos paketových dat.

Mezi klíčové architektonické komponenty patří entita RLC v MS a BSS, která spravuje procedury segmentace, opětovného sestavení a potvrzování, a vrstva MAC, která zajišťuje multiplexování řídicích zpráv a dat. Zpráva PAN je kritickým prvkem pro implementaci selektivního opakování [ARQ](/mobilnisite/slovnik/arq/) (Automatic Repeat reQuest) v GERAN. Její návrh přímo ovlivňuje metriky jako propustnost a latenci, protože efektivní zpětná vazba minimalizuje režii protokolu a spotřebu prostředků rozhraní vzduchu. Specifikace PAN pokrývá oblast od požadavků na služby (22. řada) až po podrobný popis rádiového přenosu a protokolů (44., 45. řada), což zajišťuje interoperabilitu napříč vývojovou cestou GSM včetně GPRS a EDGE.

## K čemu slouží

Zpráva PAN byla vytvořena, aby řešila inherentní neefektivitu využívání vyhrazených rádiových prostředků pro řídicí signalizaci v paketově přepínaných sítích GSM (GPRS). Předchozí služby přepojování okruhů pro hlas využívaly vyhrazené kanály, kde se řídicí signalizace mohla plánovat odlišně, ale trhaná (bursty) povaha paketových dat si vyžádala spektrálně účinnější metodu potvrzování. Vysílání samostatných zpráv ACK/NACK by spotřebovávalo celé rádiové bloky, což by významně snížilo efektivní datovou propustnost dostupnou uživateli, zejména u asymetrického provozu, kde jsou vzestupná potvrzení častá vzhledem k sestupným datům.

Její zavedení spolu s GPRS (a pozdějšími vylepšeními v EDGE) bylo motivováno potřebou co nejlepšího využití vzácného rádiového spektra při poskytování spolehlivých datových služeb. Koncept navázání využívá skutečnosti, že MS má často k odeslání vzestupná data krátce po přijetí dat sestupných. Kombinací potvrzení s těmito daty se systém vyhne samostatnému přidělení plánovacího grantu a přenosu, čímž snižuje latenci zpětnovazební smyčky a zvyšuje celkovou kapacitu sítě. Tento návrh byl klíčovým prvkem pro nákladově efektivní služby mobilního internetu přes sítě 2G a 2.5G.

Tato technologie řeší problém správy režie v prostředí sdílených kanálů založeném na soutěži (contention-based). Umožňuje vrstvě RLC udržovat robustní mechanismus ARQ – nezbytný pro zvládání náchylného k chybám rádiového kanálu – bez uvalení nadměrné režie, která by negovala výhody propustnosti plynoucí z paketového přepínání. Tato účinnost byla zásadní pro komerční životaschopnost raných mobilních datových služeb.

## Klíčové vlastnosti

- Přenos navázaný (piggy-backed) na vzestupné RLC datové bloky za účelem šetření rádiových prostředků
- Podporuje jak potvrzení (ACK), tak negativní potvrzení (NACK) pro selektivní opakování ARQ
- Používá formát bitmapy k potvrzení více sestupných bloků v rámci jedné zprávy
- Integrální součást správy dočasného toku bloků (Temporary Block Flow - TBF) pro paketové datové relace
- Snižuje režii řídicích kanálů a zlepšuje spektrální účinnost
- Definována pro provoz přes rádiová rozhraní GSM, GPRS a EDGE (EGPRS)

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)
- [EGPRS – Enhanced GPRS](/mobilnisite/slovnik/egprs/)

## Definující specifikace

- **TS 22.258** (Rel-7) — All-IP Network Service Requirements
- **TS 22.259** (Rel-19) — Personal Network Management Requirements
- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.259** (Rel-19) — Personal Network Management (PNM) Procedures
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 45.001** (Rel-19) — GSM Physical Layer Introduction
- **TS 45.003** (Rel-19) — Channel Coding and Multiplexing for GSM/EDGE
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [PAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/pan/)
