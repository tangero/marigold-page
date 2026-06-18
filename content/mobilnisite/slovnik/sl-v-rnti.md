---
slug: "sl-v-rnti"
url: "/mobilnisite/slovnik/sl-v-rnti/"
type: "slovnik"
title: "SL-V-RNTI – Sidelink V2X Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "SL-V-RNTI"
fullName: "Sidelink V2X Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-v-rnti/"
summary: "SL-V-RNTI je dočasný identifikátor přidělený sítí UE pro plánování a řízení přenosů V2X přes postranní spojení (sidelink). Používá se v řídicích informacích na downlinku k označení zdrojů pro sidelink"
---

SL-V-RNTI je dočasný identifikátor přidělený sítí UE pro plánování a řízení přenosů V2X přes postranní spojení (sidelink) prostřednictvím řídicích informací na downlinku.

## Popis

Sidelink [V2X](/mobilnisite/slovnik/v2x/) Radio Network Temporary Identifier (SL-V-RNTI) je 16bitový identifikátor definovaný ve specifikacích 3GPP, primárně používaný na vrstvě Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) pro plánování sidelink přenosů ve scénářích komunikace vozidlo se vším (V2X). Slouží jako jedinečná adresa, kterou síť (např. gNB v NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE) používá k nasměrování řídicích informací na konkrétní UE zapojené do sidelink V2X komunikace. Když je UE nakonfigurováno pro V2X sidelink provoz, síť přiřadí SL-V-RNTI prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/), typicky během sidelink konfigurace nebo procedury výběru režimu. Tento identifikátor se pak používá ke skramblování kontrolního součtu cyklickou redundancí ([CRC](/mobilnisite/slovnik/crc/)) řídicích informací na downlinku ([DCI](/mobilnisite/slovnik/dci/)) přenášených na fyzickém kanálu řídicích informací na downlinku ([PDCCH](/mobilnisite/slovnik/pdcch/)). UE monitoruje PDCCH pro formáty DCI, které obsahují jeho SL-V-RNTI; při detekci dekóduje DCI, aby získalo přístupová práva k prostředkům sdíleného kanálu postranního spoje ([PSSCH](/mobilnisite/slovnik/pssch/)), včetně parametrů jako přidělení časových a frekvenčních zdrojů, schéma modulace a kódování a výkon přenosu.

Z architektonického hlediska SL-V-RNTI funguje v rámci řídicího rámce radiozdrojů rozhraní Uu (mezi UE a sítí), ale přímo ovlivňuje operace na postranním spoji (rozhraní PC5). Je klíčovou součástí režimu 1 (síťově plánovaného) přidělování sidelink zdrojů, kde síť centrálně spravuje zdroje, aby se předešlo interferencím a optimalizovalo využití. UE používá SL-V-RNTI k identifikaci relevantních zpráv DCI, které mohou plánovat počáteční přenosy nebo opakované přenosy pro sidelink data. Identifikátor je dočasný a může být překonfigurován nebo uvolněn při ukončení sidelink relace UE nebo při předání spojení. V LTE je definován v 36.321 (specifikace MAC protokolu) a podobné principy platí v NR s vylepšeními pro 5G V2X. SL-V-RNTI se odlišuje od jiných RNTI, jako je C-RNTI (pro buněčný provoz) nebo SL-RNTI (pro ne-V2X sidelink), což zajišťuje oddělené zacházení s plánováním V2X.

Role SL-V-RNTI je klíčová pro efektivní a spolehlivou sidelink V2X komunikaci, zejména v přetížených scénářích, jako je městský provoz. Díky umožnění síťově řízeného plánování pomáhá řídit kolize zdrojů, upřednostňovat bezpečnostní zprávy a zajišťovat kvalitu služeb (QoS) pro kritické aplikace. Síť může dynamicky přidělovat zdroje na základě stavu provozu, mobility UE a úrovní interference, přičemž SL-V-RNTI používá jako cílovací mechanismus. Tento identifikátor podporuje jak vysílání (broadcast), tak skupinové vysílání (groupcast) ve V2X, což síti umožňuje plánovat zdroje pro více UE koordinovaným způsobem. Jeho použití snižuje latenci a nejistotu spojenou s autonomním výběrem zdrojů (režim 2), což jej činí vhodným pro bezpečnostně kritické V2X služby vyžadující garantovaný přístup ke zdrojům.

## K čemu slouží

SL-V-RNTI bylo zavedeno v 3GPP Release 14 pro podporu síťově plánovaného přidělování zdrojů pro LTE V2X sidelink komunikaci, čímž reagovalo na potřebu řízeného a efektivního využití spektra ve vozidlových sítích. Před standardizací V2X používal sidelink v LTE (původně pro ProSe) autonomní výběr zdrojů (režim 2), což mohlo vést k přetížení a kolizím paketů v hustém vozidlovém prostředí a ohrozit spolehlivost bezpečnostních zpráv. Vytvoření SL-V-RNTI umožnilo provoz v režimu 1, kde síť koordinuje zdroje, a řeší tak problémy řízení interference a zajištění QoS pro vysokoprioritní V2X provoz.

Historicky, jak se V2X vyvíjelo z D2D komunikace, se pro bezpečnostní aplikace, jako jsou zprávy o kooperativním povědomí (CAM) nebo decentralizované zprávy o oznamování prostředí (DENM), které vyžadují nízkou latenci a vysokou úspěšnost doručení, ukázala jako problematická omezení distribuovaného plánování. SL-V-RNTI poskytlo mechanismus, aby síť mohla přímo plánovat sidelink přenosy, využívajíc existující buněčnou infrastrukturu ke zlepšení výkonu. To bylo motivováno požadavky automobilového průmyslu na deterministickou komunikaci na podporu pokročilých asistenčních systémů řízení vozidla (ADAS) a budoucího autonomního řízení. V průběhu releasů bylo SL-V-RNTI zachováno a vylepšeno pro podporu nových funkcí, jako je NR V2X, agregace sidelink nosných a vylepšená spolehlivost, což zajišťuje zpětnou kompatibilitu a bezproblémový provoz napříč LTE a 5G sítěmi.

## Klíčové vlastnosti

- 16bitový dočasný identifikátor přidělený sítí pro plánování sidelink V2X
- Používá se ke skramblování CRC DCI na PDCCH pro přístupová práva k sidelink zdrojům
- Podporuje režim 1 (síťově plánované) přidělování sidelink zdrojů ve V2X
- Umožňuje cílenou řídicí signalizaci pro konkrétní UE za účelem efektivního řízení zdrojů
- Odlišné od jiných RNTI, aby oddělilo plánování V2X od buněčného nebo ne-V2X sidelink provozu
- Konfigurovatelné prostřednictvím signalizace RRC a může být aktualizováno během událostí mobility

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)

## Definující specifikace

- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SL-V-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-v-rnti/)
