---
slug: "aich"
url: "/mobilnisite/slovnik/aich/"
type: "slovnik"
title: "AICH – Acquisition Indication Channel"
date: 2025-01-01
abbr: "AICH"
fullName: "Acquisition Indication Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aich/"
summary: "AICH je downlinkový fyzický kanál v UMTS používaný k indikaci, zda síť úspěšně detekovala náhodný přístupový preambuli vyslaný UE na PRACH. Poskytuje okamžitou zpětnou vazbu UE pokoušejícím se o počát"
---

AICH je downlinkový fyzický kanál v UMTS, který informuje UE, zda síť úspěšně detekovala jeho náhodný přístupový preambuli, a poskytuje tak okamžitou zpětnou vazbu pro efektivní přístupové procedury.

## Popis

Acquisition Indication Channel (AICH) je základní downlinkový fyzický kanál v rádiovém rozhraní UMTS/[WCDMA](/mobilnisite/slovnik/wcdma/), který funguje na fyzické vrstvě (Layer 1) architektury [UTRAN](/mobilnisite/slovnik/utran/). Slouží jako vyhrazený signalizační kanál speciálně navržený k poskytování rychlé zpětné vazby uživatelskému zařízení (UE) během kritické procedury náhodného přístupu. Když UE zahájí přístup k síti – ať už pro počáteční registraci, navázání spojení nebo předání spojení – nejprve vysílá náhodný přístupový preambuli na Physical Random Access Channel ([PRACH](/mobilnisite/slovnik/prach/)). AICH slouží jako mechanismus okamžité odezvy sítě, který informuje UE, zda jeho preambuli úspěšně detekoval Node B.

Z architektonického hlediska je AICH vysílán Node B a je úzce spojen s PRACH v párovém vztahu. Kanál funguje pomocí specifického rozprostíracího kódu a je časově synchronizován s odpovídající slotovou strukturou PRACH. Přenos AICH se skládá z posloupnosti indikátorů zachycení (Acquisition Indicators, AIs), z nichž každý odpovídá specifickému signaturnímu vzoru ze sady 16 dostupných signatur preambule definovaných ve specifikacích UMTS. Každý [AI](/mobilnisite/slovnik/ai/) je 32čipová posloupnost, která nese binární informaci: kladné potvrzení ([ACK](/mobilnisite/slovnik/ack/)), záporné potvrzení ([NACK](/mobilnisite/slovnik/nack/)) nebo žádný přenos. AICH zabírá 4096 čipů v rámci 10 ms rádiového rámce, rozdělených do 32 slotů po 128 čipech, přičemž skutečný přenos AI probíhá v konkrétních částech této struktury.

Z procesního hlediska, když UE vysílá náhodný přístupový preambuli s konkrétní signaturou, monitoruje po předem stanoveném časovém posunu odpovídající pozici signatury na AICH. Pokud Node B preambuli úspěšně detekuje, vysílá na AICH potvrzení ACK pomocí stejného indexu signatury. Toto ACK signalizuje UE, aby pokračovala ve vysílání zprávové části procedury náhodného přístupu na PRACH. Pokud Node B detekuje kolizi (více UE používajících stejnou signaturu) nebo nemůže požadavek zpracovat, může vyslat NACK, čímž nařídí UE ustoupit a opakovat pokus po náhodném zpoždění. Absence jakéhokoli přenosu na AICH po monitorovacím období znamená, že preambule nebyla detekována, což podnítí UE ke zvýšení výkonu vysílání preambule a opakování pokusu.

Fungování AICH zahrnuje přesné časové vztahy definované ve specifikacích 3GPP. Přenos AICH začíná přesně tři 1024čipové přístupové sloty (přibližně 2560 čipů) po skončení přenosu preambule na PRACH. Toto pevné časování umožňuje UE přesně vědět, kdy má monitorovat potvrzení. Kanál používá rozprostírací faktor 256 a je vysílán se stejným výkonem pro všechny signatury AICH, aby bylo zajištěno spolehlivé detekce. AICH je vždy vysílán bez uzavřené smyčky řízení výkonu, spoléhá místo toho na dostatečnou výkonovou rezervu k dosažení všech UE v oblasti pokrytí buňky.

V širším síťovém kontextu hraje AICH klíčovou roli při řízení uplinkového rušení a přístupové konkurence. Poskytnutím okamžité zpětné vazby zabraňuje tomu, aby UE zbytečně vysílala zprávovou část svých pokusů o náhodný přístup, když preambule nebyla detekována, čímž snižuje uplinkové rušení. Rychlá odezva NACK v případech kolize pomáhá rychle řešit konkurenci, čímž se zlepšuje celková efektivita náhodného přístupu. Konstrukce AICH představuje pečlivě vyvážený kompromis mezi přístupovým zpožděním, signalizační režií a složitostí implementace, což z něj činí nezbytnou součást procedur náhodného přístupu v UMTS napříč více vydáními 3GPP.

## K čemu slouží

AICH byl vytvořen k řešení základních výzev v proceduře náhodného přístupu v sítích UMTS založených na [WCDMA](/mobilnisite/slovnik/wcdma/). V dřívějších mobilních systémech, jako je GSM, používal náhodný přístup jednodušší konkurenční přístupy s delší latencí. Technologie rozprostřeného spektra WCDMA přinesla nové komplikace: bez okamžité zpětné vazby by UE slepě vysílala celou přístupovou zprávu, i když preambule nebyla detekována, což vytvářelo zbytečné uplinkové rušení a plýtvalo výdrží baterie UE. AICH to vyřešil poskytnutím vyhrazeného downlinkového kanálu pro okamžité potvrzení, což umožnilo efektivní zvyšování výkonu a řešení kolizí.

Před zavedením AICH v UMTS Release 99 čelily systémy [CDMA](/mobilnisite/slovnik/cdma/) významným výzvám v efektivitě náhodného přístupu. V systémech IS-95 CDMA byly přístupové sondy vysílány s rostoucím výkonem, dokud nebylo přijato potvrzení, ale toto potvrzení přicházelo prostřednictvím signalizace vyšších vrstev s podstatným zpožděním. Tento přístup způsoboval nadměrné rušení během přístupové procedury a zvyšoval přístupovou latenci. Inovací AICH bylo přesunutí tohoto potvrzení na fyzickou vrstvu s přesně načasovanými odpověďmi, což ve srovnání s předchozími přístupy snížilo průměrné přístupové zpoždění o 50–70 % a minimalizovalo uplinkové rušení během přístupových pokusů.

AICH také řešil specifické požadavky rychlého řízení výkonu a schopnosti měkkého předání spojení ve WCDMA. V UMTS potřebují UE rychle stanovit počáteční řízení výkonu během přístupu a AICH poskytuje časový referenční bod pro tento přechod. Během předání spojení mezi buňkami umožňuje AICH rychlý přístup k cílovým buňkám bez čekání na signalizaci vyšších vrstev. Konstrukce kanálu specificky zohledňuje 10ms strukturu rádiového rámce a slotové časování WCDMA, což umožňuje hladkou integraci s ostatními fyzickými kanály. Řešením těchto základních přístupových problémů umožnil AICH efektivní náhodný přístup s nízkou latencí nezbytný pro hlasové a datové služby UMTS.

## Klíčové vlastnosti

- Poskytuje okamžité potvrzení detekce preambule PRACH na fyzické vrstvě.
- Používá 16 signaturních posloupností odpovídajících signaturám preambule PRACH.
- Pro každou pozici signatury vysílá ACK, NACK nebo žádný signál.
- Pevný časový vztah s PRACH (3 přístupové sloty po skončení preambule).
- Rozprostírací faktor 256 s konzistentním vysílacím výkonem.
- Umožňuje efektivní zvyšování výkonu a řešení kolizí v náhodném přístupu.

## Související pojmy

- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)
- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [S-CCPCH – Secondary Common Control Physical Channel](/mobilnisite/slovnik/s-ccpch/)
- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview

---

📖 **Anglický originál a plná specifikace:** [AICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/aich/)
