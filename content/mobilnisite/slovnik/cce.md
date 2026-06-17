---
slug: "cce"
url: "/mobilnisite/slovnik/cce/"
type: "slovnik"
title: "CCE – Control Channel Element"
date: 2025-01-01
abbr: "CCE"
fullName: "Control Channel Element"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cce/"
summary: "CCE je základní jednotkou zdrojů pro konstrukci downlink řídicích kanálů (PDCCH) v LTE a NR. Skládá se ze skupiny Resource Elements (REs) a je agregována pro vytváření řídicích zpráv různé velikosti,"
---

CCE je základní jednotkou zdrojů pro konstrukci downlink řídicích kanálů v LTE a NR, sestávající z agregovaných Resource Elements pro vytváření řídicích zpráv pro efektivní plánování a signalizaci.

## Popis

Control Channel Element (CCE) je logické seskupení fyzických zdrojů používané k přenosu Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). V LTE (od Rel-8) je CCE definováno jako sada 36 Resource Elements (REs), což odpovídá 9 Resource Element Groups (REGs) po 4 REs každá, s výjimkou těch použitých pro referenční signály. Tato struktura umožňuje konstrukci PDCCH agregací více CCE (např. 1, 2, 4 nebo 8 CCE) pro podporu různých formátů DCI a kódovacích rychlostí, což vyhovuje různým podmínkám kanálu a velikostem řídicích informací. Mapování CCE na konkrétní REGy v rámci řídicí oblasti subframu následuje předdefinovaný prokládací vzor pro zajištění odolnosti vůči útlumu a interferenci.

V 5G NR (od Rel-15) je koncept CCE zachován a upřesněn v rámci nového frameworku control resource set ([CORESET](/mobilnisite/slovnik/coreset/)). CCE v NR sestává z 6 Resource Blocks (RBs) ve frekvenční doméně po dobu trvání jednoho symbolu (nebo více symbolů, pokud je nakonfigurováno) v rámci CORESETu. Každé CCE je dále rozděleno na 6 Resource Element Groups (REGs), kde REG odpovídá jednomu RB v jednom symbolu. Tato struktura poskytuje flexibilitu v plánování řídicího kanálu napříč částí přenosového pásma. Úroveň agregace ([AL](/mobilnisite/slovnik/al/)), definující počet agregovaných CCE (1, 2, 4, 8, 16 nebo dokonce 32 pro rozšířené pokrytí), je dynamicky přizpůsobována na základě rádiových podmínek uživatele, které jsou určeny prostřednictvím informací o stavu kanálu a zvoleného formátu DCI.

Fungování CCE zahrnuje několik klíčových procesů. Nejprve je zpráva DCI, obsahující plánovací přiřazení nebo povolení, kanálově zakódována a přizpůsobena rychlosti. Tato zakódovaná bitová sekvence je pak namapována na přidělená CCE. Konkrétní indexy CCE pro uživatele jsou odvozeny z hash funkce založené na Radio Network Temporary Identifier (RNTI) uživatele, což zajišťuje pseudonáhodné rozložení pro minimalizaci kolizí blokování. Fyzické mapování REGů CCE na skutečné REs v rámci CORESETu následuje určený vzor, který může být prokládaný nebo neprokládaný, což nabízí kompromisy mezi diverzitou a lokalizovaným přenosem.

CCE jsou základní pro fungování řídicí roviny. Umožňují přenos kritické signalizace, jako jsou povolení pro uplink a downlink zdroje, příkazy pro řízení výkonu, indikace formátu slotu a indikátory předběžného obsazení. Schopnost škálovat úroveň agregace umožňuje systému zajistit spolehlivý příjem řídicího kanálu pro uživatele na okraji buňky (použitím vysoké AL) při zachování efektivity pro uživatele s dobrou kvalitou signálu (použitím nízké AL). Tato dynamická adaptace je základním kamenem spektrální efektivity a robustního výkonu sítí LTE a NR. Celý proces, od generování DCI po mapování CCE a přenos, je těsně integrován s plánovacími algoritmy v základnové stanici (gNB/[eNB](/mobilnisite/slovnik/enb/)).

## K čemu slouží

CCE bylo zavedeno v LTE Rel-8, aby poskytlo strukturovanou, škálovatelnou a efektivní metodu pro přenos downlink řídicích informací. Předchozí systémy postrádaly tak členěnou a flexibilní jednotku pro konstrukci řídicího kanálu, což omezovalo přizpůsobivost řídicí signalizace různým uživatelským podmínkám a velikostem řídicích zpráv. Architektura CCE řeší problém spolehlivého doručování plánovacích příkazů a další kritické signalizace v různorodých rádiových prostředích tím, že umožňuje agregaci více základních jednotek pro dosažení různých kódovacích rychlostí a úrovní robustnosti.

Hlavní motivací bylo oddělit návrh řídicího kanálu od pevných velikostí přenášených dat a umožnit adaptaci spojení specificky pro řídicí kanál. Definováním CCE jako základního stavebního bloku může systém dynamicky rozhodnout, kolik CCE (úroveň agregace) použít pro [DCI](/mobilnisite/slovnik/dci/) konkrétního uživatele. Toto přímo řeší výzvu udržení pokrytí řídicího kanálu napříč celou buňkou, od blízkosti základnové stanice až po okraj, bez plýtvání nadměrnými zdroji pro uživatele v dobrých podmínkách. Poskytuje rovnováhu mezi spolehlivostí a efektivitou.

Dále bylo strukturované mapování CCE na fyzické REs, využívající prokládací vzory, navrženo tak, aby využilo frekvenční a časovou diverzitu v rámci řídicí oblasti. To zmírňuje dopad úzkopásmových interferencí a útlumu kanálu, což zajišťuje, že řídicí informace zůstanou dekódovatelné i za nepříznivých podmínek. Koncept CCE tak podporuje dynamické plánování a robustní provoz celulární sítě a tvoří kritickou část architektury řídicí roviny rádiového rozhraní od LTE až po 5G NR.

## Klíčové vlastnosti

- Základní jednotka zdrojů pro konstrukci PDCCH
- Škálovatelné úrovně agregace (1,2,4,8,16,32) pro adaptaci spojení
- Logické seskupení mapované na fyzické Resource Elements (REs)
- Podporuje dynamické přidělování na základě RNTI uživatele a podmínek kanálu
- Využívá prokládací vzory pro diverzitu přenosu
- Integrální součást návrhu řídicího kanálu (CORESET) jak LTE, tak 5G NR

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [CORESET – Control Resource Set](/mobilnisite/slovnik/coreset/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TS 38.824** (Rel-16) — NR URLLC Physical Layer Enhancements Study
- **TR 38.830** (Rel-17) — NR Coverage Enhancements Study
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [CCE na 3GPP Explorer](https://3gpp-explorer.com/glossary/cce/)
