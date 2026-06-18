---
slug: "sl-cs-rnti"
url: "/mobilnisite/slovnik/sl-cs-rnti/"
type: "slovnik"
title: "SL-CS-RNTI – Sidelink Configured Scheduling Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "SL-CS-RNTI"
fullName: "Sidelink Configured Scheduling Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-cs-rnti/"
summary: "Jedinečný identifikátor používaný v postranním spoji NR pro přenosy s nakonfigurovaným přístupem, který umožňuje polo-perzistentní plánování zdrojů postranního spoje bez dynamických přístupových opráv"
---

SL-CS-RNTI je jedinečný identifikátor používaný v postranním spoji NR pro přenosy s nakonfigurovaným přístupem, který umožňuje polo-perzistentní plánování zdrojů za účelem snížení režie řídicí signalizace pro předvídatelný provoz, jako jsou zprávy V2X.

## Popis

Sidelink Configured Scheduling [RNTI](/mobilnisite/slovnik/rnti/) (SL-CS-RNTI) je 16bitový dočasný identifikátor rádiové sítě specificky definovaný pro komunikaci postranním spojem v 5G systémech New Radio (NR). Tento identifikátor hraje klíčovou roli v režimu nakonfigurovaného přístupu (Typ 1 a Typ 2) postranního spoje NR, kde jsou zdroje přidělovány polo-perzistentně pro periodické nebo předvídatelné přenosové vzory bez nutnosti dynamických přístupových oprávnění pro každý přenos. SL-CS-RNTI je konfigurován sítí prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) a je používán uživatelským zařízením (UE) k identifikaci a validaci konfigurací nakonfigurovaného přístupu pro přenosy postranním spojem.

Z architektonického hlediska SL-CS-RNTI funguje v rámci vrstvy Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) protokolového zásobníku postranního spoje, jak je specifikováno v 3GPP TS 38.321. Funguje jako klíčová součást mechanismu nakonfigurovaného plánování, který je součástí rámce přidělování zdrojů postranního spoje. Když je UE nakonfigurováno s SL-CS-RNTI, může autonomně vysílat na předem nakonfigurovaných zdrojích postranního spoje podle definované periodicty a časově-frekvenčního vzoru bez nutnosti jednotlivých dynamických přístupových oprávnění od sítě nebo procedur výběru zdrojů založených na snímání. Identifikátor je asociován se specifickými konfiguracemi nakonfigurovaného přístupu, které definují parametry jako periodicita, časový posun, frekvenční zdroje, modulační a kódovací schéma a parametry řízení výkonu.

Při provozu síť nakonfiguruje UE jednou nebo více hodnotami SL-CS-RNTI spolu s odpovídajícími konfiguracemi nakonfigurovaného přístupu prostřednictvím dedikované signalizace RRC. Každý SL-CS-RNTI je jednoznačně asociován se specifickou konfigurací nakonfigurovaného přístupu uvnitř UE. Když má UE data k vysílání na postranním spoji, která odpovídají charakteristikám provozu konfigurace nakonfigurovaného přístupu, použije zdroje asociované s touto konfigurací bez žádosti o další přístupová oprávnění. SL-CS-RNTI slouží jako referenční bod pro aktivaci, deaktivaci nebo modifikaci konfigurací nakonfigurovaného přístupu prostřednictvím řídicích prvků MAC (MAC [CE](/mobilnisite/slovnik/ce/)) nebo formátů Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) specificky navržených pro nakonfigurované plánování postranního spoje.

Technická implementace zahrnuje specifické formáty DCI (jako je DCI formát 3_0), které jsou scramblovány pomocí SL-CS-RNTI. Když UE přijme DCI scramblované jejím nakonfigurovaným SL-CS-RNTI, interpretuje to jako příkaz související s jejími zdroji postranního spoje s nakonfigurovaným přístupem – buď aktivaci, deaktivaci nebo zdroje pro retransmisi. Tento mechanismus umožňuje síti zachovat kontrolu nad přenosy UE na postranním spoji i v režimu nakonfigurovaného přístupu, což umožňuje dynamickou adaptaci na měnící se rádiové podmínky nebo přenosové vzory při minimalizaci režie řídicí signalizace ve srovnání s plně dynamickým plánováním.

SL-CS-RNTI umožňuje efektivní využití zdrojů pro předvídatelné přenosové vzory postranního spoje běžně se vyskytující v aplikacích [V2X](/mobilnisite/slovnik/v2x/), průmyslovém IoT a komunikacích pro veřejnou bezpečnost. Tím, že odstraňuje potřebu průběžných žádostí o plánování a přístupových oprávnění pro periodický provoz, snižuje latenci pro časově kritické komunikace a snižuje režii řídicího kanálu. Identifikátor podporuje jak síťově plánovaný provoz (kde gNB konfiguruje zdroje), tak vylepšení autonomního výběru zdrojů (kde UE vybírá zdroje v rámci rámce nakonfigurovaného přístupu), čímž poskytuje flexibilitu pro různé scénáře nasazení a možnosti UE.

## K čemu slouží

SL-CS-RNTI byl zaveden v 3GPP Release 16, aby řešil potřebu efektivního přidělování zdrojů pro periodické a předvídatelné přenosové vzory v komunikacích postranním spojem NR. Před jeho zavedením se přidělování zdrojů postranního spoje primárně spoléhalo buď na plně dynamické plánování (vyžadující jednotlivá přístupová oprávnění pro každý přenos), nebo na zcela autonomní výběr zdrojů (kde UE nezávisle snímají a vybírají zdroje). Oba přístupy měly omezení pro aplikace s pravidelnými přenosovými vzory, jako jsou bezpečnostní zprávy [V2X](/mobilnisite/slovnik/v2x/), které jsou vysílány periodicky, ale s předvídatelným načasováním a požadavky na zdroje.

Motivace pro SL-CS-RNTI vzešla ze specifických požadavků pokročilých V2X aplikací definovaných v postranním spoji NR, kde vozidla potřebují periodicky vysílat základní bezpečnostní zprávy ([BSM](/mobilnisite/slovnik/bsm/)) (typicky každých 100 ms) s nízkou latencí a vysokými požadavky na spolehlivost. Tradiční dynamické plánování vytvářelo nadměrnou režii řídicí signalizace pro periodické bezpečnostní zprávy, zatímco zcela autonomní výběr postrádal dostatečnou síťovou kontrolu pro řízení interference v hustých nasazeních.

SL-CS-RNTI umožňuje provoz s nakonfigurovaným přístupem pro postranní spoj, podobně jako mechanismy nakonfigurovaného plánování dostupné pro uplink komunikace. Tento přístup řeší problém režie tím, že umožňuje UE používat předem nakonfigurované zdroje pro periodické přenosy bez jednotlivých přístupových oprávnění, a zároveň zachovává síťovou kontrolu prostřednictvím možnosti aktivovat, deaktivovat nebo modifikovat konfigurace pomocí identifikátoru SL-CS-RNTI. Tento vyvážený přístup poskytuje efektivitu polo-perzistentního plánování s flexibilitou síťového dohledu, což je zvláště důležité pro bezpečnostně kritické aplikace, kde musí být spolehlivá komunikace udržována i v přetížených scénářích.

## Klíčové vlastnosti

- 16bitový identifikátor specificky pro operace s nakonfigurovaným přístupem v postranním spoji NR
- Umožňuje polo-perzistentní plánování zdrojů postranního spoje bez dynamických přístupových oprávnění
- Asociován s konfiguracemi nakonfigurovaného přístupu definujícími periodicitu a vzory zdrojů
- Používán pro scramblování formátů DCI souvisejících s nakonfigurovaným plánováním postranního spoje
- Podporuje nakonfigurovaný přístup Typ 1 (konfigurovaný RRC) i Typ 2 (RRC + aktivovaný PDCCH)
- Umožňuje síťovou kontrolu nad aktivací, deaktivací a modifikací zdrojů postranního spoje

## Související pojmy

- [SL-RNTI – Sidelink Radio Network Temporary Identifier](/mobilnisite/slovnik/sl-rnti/)
- [SPS – Semi-Persistent Scheduling](/mobilnisite/slovnik/sps/)

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SL-CS-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-cs-rnti/)
