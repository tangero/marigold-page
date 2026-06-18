---
slug: "cg-dfi"
url: "/mobilnisite/slovnik/cg-dfi/"
type: "slovnik"
title: "CG-DFI – Configured Grant - Downlink Feedback Information"
date: 2025-01-01
abbr: "CG-DFI"
fullName: "Configured Grant - Downlink Feedback Information"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cg-dfi/"
summary: "CG-DFI je zpětnovazební mechanismus v 5G NR pro uplinkové přenosy s nakonfigurovaným povolením (Configured Grant, CG). Umožňuje gNB poskytnout stanici UE potvrzující zpětnou vazbu (ACK/NACK) pro její"
---

CG-DFI je zpětnovazební mechanismus v 5G NR, kde gNB poskytuje stanici UE potvrzení (ACK/NACK) pro její uplinková data odeslaná prostřednictvím přenosů s nakonfigurovaným povolením (Configured Grant), čímž zvyšuje spolehlivost pro provoz bez nutnosti dynamického povolování a s nízkou latencí.

## Popis

Configured Grant - Downlink Feedback Information (CG-DFI) je signalizační mechanismus na fyzické vrstvě definovaný ve specifikacích 5G New Radio (NR). Funguje v kontextu uplinkových přenosů typu Configured Grant ([CG](/mobilnisite/slovnik/cg/)) Typ 1 a Typ 2, kde je uživatelské zařízení (UE) předem nakonfigurováno s periodickými zdroji pro přenos uplinkových dat bez nutnosti dynamického povolovacího příkazu ([DCI](/mobilnisite/slovnik/dci/)) pro každý přenos. Zatímco tento přístup bez nutnosti povolení minimalizuje latenci a režii řídicí signalizace, tradičně mu chyběl přímý kanál s nízkou latencí, kterým by gNB mohl potvrdit úspěšný příjem. CG-DFI tento problém řeší definováním vyhrazeného formátu Downlink Control Information (DCI), konkrétně formátu 0_2, který gNB může použít k předání Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)) zpětné vazby pro více CG přenosů od jedné nebo více stanic UE.

Mechanismus funguje tak, že každému nakonfigurovanému grantovému zdroji je přiřazen specifický HARQ proces. Když UE vysílá data na svých předem nakonfigurovaných [PUSCH](/mobilnisite/slovnik/pusch/) zdrojích, monitoruje vyhrazený prohledávací prostor pro DCI formát 0_2, scramblované specifickým Radio Network Temporary Identifier ([RNTI](/mobilnisite/slovnik/rnti/)), například Configured Scheduling RNTI ([CS-RNTI](/mobilnisite/slovnik/cs-rnti/)). Datová část DCI obsahuje zpětnovazební bitmapu. Každý bit v této bitmapě odpovídá konkrétní CG přenosové příležitosti nebo kombinaci CG konfigurace a HARQ procesu. Nastavený bit (např. '1') indikuje kladné potvrzení ([ACK](/mobilnisite/slovnik/ack/)) pro daný přenos, zatímco vynulovaný bit (např. '0') indikuje záporné potvrzení ([NACK](/mobilnisite/slovnik/nack/)), což vyzve UE k zahájení retransmise. Mapování mezi pozicemi v bitmapě a CG přenosy UE je konfigurováno signalizací vyšší vrstvy RRC, což zajišťuje, že UE může zpětnou vazbu správně interpretovat.

Z architektonického hlediska je CG-DFI funkcí Medium Access Control (MAC) a fyzické (PHY) vrstvy gNB. MAC vrstva gNB po dekódování PUSCH přenosu přijatého na CG zdroji určí stav ACK/NACK. Následně instruuje PHY vrstvu, aby vygenerovala a vyslala odpovídající DCI formát 0_2 na downlinkovém řídicím kanálu (PDCCH). Na straně UE PHY vrstva dekóduje DCI a MAC vrstva zpracuje HARQ zpětnou vazbu, čímž aktualizuje stav příslušného HARQ procesu. Tato zpětná vazba se zavřenou smyčkou je klíčová pro zvýšení spolehlivosti uplinku bez nutnosti povolování, který je inherentně méně spolehlivý než plánovaný přístup kvůli možným kolizím a absenci přizpůsobení spojení na přenos. Poskytnutím včasné HARQ zpětné vazby CG-DFI umožňuje rychlé retransmise, čímž zlepšuje úspěšnost doručování paketů pro služby citlivé na latenci, aniž by bylo nutné uchylovat se k retransmise na vyšších vrstvách, které zavádějí větší zpoždění.

## K čemu slouží

CG-DFI byl zaveden, aby vyřešil zásadní omezení původního schématu uplinku s nakonfigurovaným povolením (Configured Grant) v 5G NR. Configured Grant byl navržen pro podporu Ultra-Reliable Low-Latency Communications (URLLC) a massive Machine-Type Communications (mMTC) tím, že umožňoval stanicím UE vysílat okamžitě na předem nakonfigurovaných zdrojích, čímž eliminoval latenci výměny žádosti o plánování a povolení. Ve své původní podobě však gNB neměl efektivní metodu s nízkou latencí, jak informovat UE, zda byl přenos úspěšně přijat. UE by selhání zjistila až prostřednictvím časovačů retransmise na vyšších vrstvách (např. RLC), které jsou pro přísné požadavky na latenci URLLC (často 1 ms nebo méně) příliš pomalé. Tato mezera ztěžovala skutečně vysoce spolehlivou komunikaci pro uplink bez nutnosti povolování.

Zavedení CG-DFI bylo motivováno potřebou uzavřít tuto zpětnovazební smyčku na fyzické/MAC vrstvě s minimálním zpožděním. Řeší tento problém poskytnutím vyhrazeného downlinkového řídicího kanálu, který nese HARQ potvrzení specificky pro CG přenosy. To umožňuje rychlé retransmise na úrovni HARQ, což výrazně zlepšuje spolehlivost spojení při zachování výhody nízké latence přístupu bez nutnosti povolování. Řeší problém tichých selhání, kdy by UE opakovaně vysílala nová data, zatímco předchozí pakety byly ztraceny, což plýtvalo zdroji a degradovalo spolehlivost. Integrací HARQ zpětné vazby činí CG-DFI z Configured Grant životaschopné řešení pro kritické aplikace, jako je průmyslová automatizace, bezdrátové řízení a vozidlové komunikace, kde jsou ultra-nízká latence i vysoká spolehlivost nevyhnutelnými požadavky.

## Klíčové vlastnosti

- Poskytuje HARQ ACK/NACK zpětnou vazbu pro uplinkové přenosy s nakonfigurovaným povolením (Configured Grant) prostřednictvím DCI formátu 0_2
- Podporuje zpětnou vazbu pro více CG přenosových příležitostí a/nebo více stanic UE v rámci jedné DCI zprávy
- Používá konfigurovatelnou bitmapu pro mapování zpětné vazby, definovanou prostřednictvím RRC signalizace
- Umožňuje retransmise s nízkou latencí na MAC vrstvě, což je klíčové pro záruky služeb URLLC
- Je scramblováno identifikátory, jako je CS-RNTI, pro cílenou zpětnou vazbu konkrétním stanicím UE nebo skupinám
- Funguje s Configured Grant Typ 1 (plně konfigurovaným přes RRC) i Typ 2 (aktivovaným přes DCI)

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [CS-RNTI – Configured Scheduling Radio Network Temporary Identifier](/mobilnisite/slovnik/cs-rnti/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding

---

📖 **Anglický originál a plná specifikace:** [CG-DFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cg-dfi/)
