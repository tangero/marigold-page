---
slug: "cs-rnti"
url: "/mobilnisite/slovnik/cs-rnti/"
type: "slovnik"
title: "CS-RNTI – Configured Scheduling Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "CS-RNTI"
fullName: "Configured Scheduling Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cs-rnti/"
summary: "CS-RNTI je identifikátor specifický pro uživatelské zařízení (UE) používaný v 5G NR pro plánované (configured grant, CG) uplinkové přenosy. Umožňuje polo-perzistentní plánování bez nutnosti průběžné D"
---

CS-RNTI je identifikátor specifický pro uživatelské zařízení (UE) používaný v 5G NR pro umožnění plánovaných (configured grant) uplinkových přenosů, což snižuje režii řídicí signalizace a latenci pro periodické provozní vzorce jako je URLLC.

## Popis

Configured Scheduling RNTI (CS-RNTI) je klíčový identifikátor v rámci operací fyzické vrstvy a [MAC](/mobilnisite/slovnik/mac/) vrstvy 5G New Radio (NR), speciálně navržený pro podporu plánovaných (configured grant, [CG](/mobilnisite/slovnik/cg/)) přenosů typu 1 a 2. Jak je definováno ve specifikacích 3GPP 38.213 (Postupy fyzické vrstvy pro řízení) a 38.321 (Specifikace protokolu Medium Access Control), CS-RNTI slouží jako 16bitová hodnota specifická pro uživatelské zařízení (UE), která identifikuje UE pro účely plánovaných uplinkových přístupových práv (grants). Na rozdíl od dynamicky plánovaných přenosů, které vyžadují průběžnou signalizaci Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) pro každou přenosovou příležitost, CS-RNTI umožňuje polo-perzistentní plánování, kde jsou přenosové parametry předem nakonfigurovány prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) signalizace a aktivovány/deaktivovány prostřednictvím specifických formátů DCI.

Z architektonického hlediska CS-RNTI funguje uvnitř MAC plánovače gNB a MAC entity UE. Když je UE nakonfigurováno pro provoz s plánovaným přístupovým právem (configured grant), gNB přiřadí jedinečnou hodnotu CS-RNTI prostřednictvím RRC signalizace (SystemInformationBlockType1 nebo dedikované RRC signalizace). Tento identifikátor je pak použit pro skramblování [CRC](/mobilnisite/slovnik/crc/) specifických formátů DCI (Formát 0_0 nebo 0_1 se specifickými poli), které aktivují, deaktivují nebo iniciují retransmise plánovaných přístupových práv. CS-RNTI umožňuje UE rozpoznat, že přijaté DCI se týká jejích plánovaných přístupových prostředků, nikoli dynamického plánování, a spustit příslušné MAC procedury bez nutnosti explicitní alokace prostředků pro každý přenos.

U plánovaného přístupového práva typu 1 jsou všechny přenosové parametry (časové domény prostředků, frekvenční domény prostředků, [MCS](/mobilnisite/slovnik/mcs/) atd.) plně konfigurovány prostřednictvím RRC signalizace a CS-RNTI je používáno primárně pro příkazy aktivace/deaktivace a retransmise. U typu 2 jsou základní parametry konfigurovány prostřednictvím RRC, ale samotná aktivace využívá DCI formát 0_1 skramblovaný s CS-RNTI, což poskytuje dynamičtější kontrolu. CS-RNTI umožňuje hybridní automatické opakování na vyžádání ([HARQ](/mobilnisite/slovnik/harq/)) procesy specificky pro plánovaná přístupová práva, přičemž ID HARQ procesu je odvozeno z indexu konfigurace plánovaného přístupového práva a čísla systémového rámce, což umožňuje předvídatelné chování retransmise.

Role CS-RNTI přesahuje pouhou identifikaci – umožňuje efektivní využití prostředků pro periodické provozní vzorce charakteristické pro průmyslovou automatizaci, hlasové služby přes NR (Voice over NR) a další aplikace s nízkou latencí. Tím, že odstraňuje potřebu žádostí o plánování (scheduling requests) a přijímání přístupových práv (grants) pro každý přenos, CS-RNTI snižuje režii řídicích kanálů, snižuje latenci (protože UE mohou vysílat okamžitě při příchodu dat) a šetří výkon UE minimalizací monitorování [PDCCH](/mobilnisite/slovnik/pdcch/) pro dynamická přístupová práva. Identifikátor je specifický pro buňku a je rekonfigurován během procedur předávání spojení (handover), čímž zajišťuje kontinuitu služeb s plánovaným přístupovým právem během událostí mobility.

## K čemu slouží

CS-RNTI bylo vytvořeno pro řešení omezení čistě dynamického plánování v 4G LTE pro aplikace vyžadující deterministickou komunikaci s nízkou latencí a periodickými provozními vzorci. V tradičním dynamickém plánování každý uplinkový přenos vyžaduje žádost o plánování (scheduling request) od UE, downlinkové přístupové právo (grant) od gNB a následný datový přenos – což zavádí významnou latenci (typicky 8-14 ms v LTE) a režii řídicích kanálů. Pro případy užití průmyslového IoT, tovární automatizace a ultra-spolehlivé komunikace s nízkou latencí (URLLC) v 5G byl tento přístup nedostatečný pro splnění přísných požadavků na latenci (často pod 1 ms) a efektivní využití prostředků pro předvídatelný provoz.

Motivace pro CS-RNTI vzešla z potřeby podpory polo-perzistentního plánování (SPS) v 5G NR s vylepšenou flexibilitou ve srovnání s LTE SPS. Zatímco LTE zavedlo SPS pro hlasové služby přes LTE (VoLTE), mělo to omezení v konfigurační flexibilitě a bylo primárně navrženo pro periodický provoz s pevnými intervaly. Mechanismus plánovaného přístupového práva (configured grant) v 5G NR, umožněný CS-RNTI, poskytuje dva typy konfigurace (Typ 1 plně konfigurovaný RRC a Typ 2 aktivovaný RRC+DCI), aby vyhověl různorodým požadavkům služeb. CS-RNTI konkrétně řeší problém, jak efektivně signalizovat příkazy aktivace, deaktivace a retransmise pro předem nakonfigurované prostředky bez nutnosti samostatných identifikátorů UE nebo složitých signalizačních procedur.

Historicky koncept navazuje na LTE SPS-C-RNTI, ale rozšiřuje ho o vylepšení specifická pro 5G. Vytvoření CS-RNTI bylo hnací silou práce 3GPP na NR URLLC v Release 15, kde bylo snížení latence a režie řídicí roviny prvořadé. Tím, že umožňuje UE vysílat okamžitě na předem nakonfigurovaných prostředcích identifikovaných jejich CS-RNTI, systém eliminuje cyklus žádost o plánování – přidělení přístupového práva, čímž přímo řeší požadavky na latenci a spolehlivost kritických komunikací při zachování efektivního využití spektra prostřednictvím statistického multiplexování prostředků plánovaného přístupového práva mezi více UEs.

## Klíčové vlastnosti

- Umožňuje plánované (configured grant) uplinkové přenosy typu 1 a 2 v 5G NR.
- Snižuje režii řídicích kanálů eliminací DCI signalizace na každý přenos.
- Podporuje komunikaci s nízkou latencí tím, že umožňuje okamžitý přenos na předem nakonfigurovaných prostředcích.
- Umožňuje efektivní provoz HARQ pro plánovaná přístupová práva s předvídatelnou identifikací procesu.
- Umožňuje úsporu energie na UE snížením požadavků na monitorování PDCCH pro dynamická přístupová práva.
- Podporuje příkazy aktivace, deaktivace a retransmise prostřednictvím DCI skramblovaného s CS-RNTI.

## Související pojmy

- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)

## Definující specifikace

- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CS-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cs-rnti/)
