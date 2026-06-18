---
slug: "bler"
url: "/mobilnisite/slovnik/bler/"
type: "slovnik"
title: "BLER – Block Error Rate"
date: 2025-01-01
abbr: "BLER"
fullName: "Block Error Rate"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bler/"
summary: "BLER je klíčová metrika výkonu fyzické vrstvy měřící poměr chybných transportních bloků k celkovému počtu vyslaných bloků. Přímo odráží kvalitu rádiového spoje a je zásadní pro adaptaci spojení, řízen"
---

BLER je poměr chybných transportních bloků k celkovému počtu vyslaných bloků a slouží jako klíčová metrika fyzické vrstvy pro hodnocení kvality rádiového spoje a umožňuje funkce jako adaptace spojení a předávání.

## Popis

Block Error Rate (BLER, česky míra chybovosti bloků) je základní metrika výkonu v bezdrátových komunikačních systémech 3GPP, která kvantifikuje spolehlivost přenosu dat přes rádiové rozhraní. Je definována jako poměr počtu chybně přijatých transportních bloků k celkovému počtu vyslaných transportních bloků v rámci určitého měřicího období. Transportní blok představuje základní jednotku dat vyměňovanou mezi vrstvou řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a fyzickou vrstvou, která obsahuje uživatelská data, řídicí informace nebo jejich kombinaci. Měření BLER se provádí po procesech dekódování kanálu a detekce chyb, typicky pomocí cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)) připojeného ke každému transportnímu bloku. Pokud kontrola CRC selže, je blok počítán jako chybný. Výsledná hodnota BLER, často vyjádřená jako procento nebo desetinný zlomek, poskytuje přímou indikaci kvality rádiového spoje a účinnosti přenosového schématu fyzické vrstvy.

Měření a hlášení BLER zahrnuje několik síťových prvků a protokolů. V downlinku uživatelské zařízení (UE) průběžně monitoruje přijaté transportní bloky od základnové stanice (NodeB v UMTS, eNodeB v LTE nebo gNB v NR) a vypočítává BLER na základě selhání CRC. Toto měření se typicky provádí na transportním kanálu (např. Downlink Shared Channel - [DL-SCH](/mobilnisite/slovnik/dl-sch/)) a lze jej nakonfigurovat pro specifické referenční kanály používané pro řídicí účely. UE hlásí tato měření síti prostřednictvím měřicích hlášení protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), která síť používá k posouzení kvality spoje. V uplinku základnová stanice provádí podobná měření BLER na blocích přijatých od UE. Síť konfiguruje parametry měření BLER prostřednictvím signalizace RRC, včetně měřicích období, průměrovacích oken a prahových hodnot pro spouštěcí události. Tyto konfigurace zajišťují, že měření BLER jsou statisticky významná a relevantní pro optimalizaci sítě.

BLER hraje klíčovou roli v mnoha algoritmech správy rádiových zdrojů. Pro adaptaci spojení síť využívá měření BLER k výběru nejvhodnějšího schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)), které udržuje cílovou hodnotu BLER (typicky 10 % pro počáteční přenosy v LTE/NR). Pokud naměřená BLER překročí cíl, síť může přejít na robustnější MCS s nižší přenosovou rychlostí, ale lepší ochranou proti chybám. Pro řízení výkonu pomáhají měření BLER určit, zda je třeba upravit vysílací výkon pro udržení kvality spoje při minimalizaci interference. V řízení mobility se BLER používá jako spouštěč pro rozhodování o předávání – trvale vysoká BLER může indikovat špatnou kvalitu signálu z obsluhované buňky, což spouští měření sousedních buněk a případné předání. Kromě toho jsou měření BLER nezbytná pro fungování hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)), kde je zpětná vazba potvrzení/negativního potvrzení ([ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)) založena na tom, zda byl každý transportní blok přijat správně.

Interpretace a použití BLER závisí na konkrétní technologii rádiového přístupu a scénáři nasazení. V 5G NR se cílové hodnoty BLER mohou lišit v závislosti na typu služby – ultra-spolehlivé komunikace s nízkou latencí (URLLC) mohou vyžadovat mnohem nižší cíle BLER (např. 10^-5) ve srovnání s rozšířeným mobilním širokopásmovým připojením (eMBB). Metodika měření také zohledňuje různé podmínky kanálu, přičemž BLER se typicky měří za specifických podmínek referenčního signálu. Operátoři sítě používají statistiky BLER pro monitorování výkonu, odstraňování problémů a optimalizaci, korelují BLER s dalšími metrikami, jako je Reference Signal Received Power (RSRP) a Signal-to-Interference-plus-Noise Ratio (SINR), aby identifikovali problémy s pokrytím, rušení nebo hardwarové závady. Správná optimalizace BLER vyvažuje spolehlivost a spektrální účinnost, což zajišťuje uživatelům konzistentní kvalitu služby při maximalizaci kapacity sítě.

## K čemu slouží

BLER existuje jako základní metrika kvality pro kvantifikaci a správu spolehlivosti přenosu dat přes náchylné k chybám bezdrátové kanály. Na rozdíl od jednoduchých měření síly signálu BLER přímo odráží výkonnost přenosu fyzické vrstvy od konce ke konci, včetně účinků modulace, kódování, interference a zpracování přijímače. To ji činí nezbytnou pro adaptivní systémy, které musí dynamicky reagovat na měnící se rádiové podmínky. Před standardizací sofistikovaných metrik, jako je BLER, se bezdrátové systémy spoléhaly primárně na měření síly signálu, která nedostatečně zachycují skutečný výkon přenosu dat, zejména v prostředích omezených interferencí.

Primární problém, který BLER řeší, je potřeba přesné, standardizované metody pro posouzení kvality přenosu, která může pohánět automatizované optimalizační algoritmy. Bezdrátové kanály zažívají rychlé výkyvy v důsledku útlumu, interference a mobility, což vyžaduje neustálou adaptaci přenosových parametrů. BLER poskytuje mechanismus zpětné vazby potřebný pro systémy s uzavřenou smyčkou, jako je adaptace spojení a řízení výkonu. Měřením skutečné míry chyb přijatých datových bloků mohou sítě činit informovaná rozhodnutí o tom, kdy zvýšit robustnost přenosu (prostřednictvím konzervativnějšího výběru MCS nebo vyššího výkonu) oproti situacím, kdy zvýšit spektrální účinnost (prostřednictvím agresivnějšího výběru MCS).

Historicky zavedení BLER ve 3GPP Release 99 představovalo významný pokrok oproti předchozím metrikám kvality používaným v systémech 2G. Starší technologie jako GSM používaly měření míry bitových chyb (BER), která byla méně vhodná pro paketové systémy s přenosem a kódováním na bázi bloků. Perspektiva BLER na úrovni bloků přirozeně odpovídá struktuře transportních bloků systémů 3GPP a zohledňuje výhody kódování kanálu a prokládání. Jak se systémy 3GPP vyvíjely přes LTE až k 5G NR, BLER zůstala klíčovou metrikou, přičemž její měřicí metodologie byla zdokonalena pro podporu nových funkcí, jako je agregace nosných, massive MIMO a různé požadavky služeb. Pokračující relevance BLER napříč generacemi dokazuje její zásadní význam pro zajištění spolehlivé bezdrátové komunikace.

## Klíčové vlastnosti

- Měří poměr chyb transportních bloků po dekódování kanálu
- Pro detekci chyb na transportní blok používá ověření CRC
- Konfigurovatelná měřicí období a průměrovací okna
- Spouští algoritmy adaptace spojení a výběru MCS
- Podporuje procesy řízení výkonu a rozhodování o předávání
- Hlášeno síti prostřednictvím signalizace měření RRC

## Související pojmy

- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)
- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.702** (Rel-12) — DCH Enhancements for UMTS Study
- … a dalších 34 specifikací

---

📖 **Anglický originál a plná specifikace:** [BLER na 3GPP Explorer](https://3gpp-explorer.com/glossary/bler/)
