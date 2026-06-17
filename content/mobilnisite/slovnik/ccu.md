---
slug: "ccu"
url: "/mobilnisite/slovnik/ccu/"
type: "slovnik"
title: "CCU – Channel Coding Unit"
date: 2025-01-01
abbr: "CCU"
fullName: "Channel Coding Unit"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ccu/"
summary: "Jednotka pro kódování kanálu (CCU) je funkční blok ve fyzické vrstvě odpovědný za aplikaci kódů pro detekci a korekci chyb na přenášená data. Je nezbytná pro zajištění spolehlivého přenosu dat přes šu"
---

CCU je funkční blok ve fyzické vrstvě, který aplikuje kódy pro detekci a korekci chyb na přenášená data, aby zajistil spolehlivou komunikaci přes šumivé rádiové kanály.

## Popis

Jednotka pro kódování kanálu (CCU) je základní součástí fyzické vrstvy (vrstvy 1) v bezdrátových systémech 3GPP, včetně GSM, UMTS a LTE. Jejím primárním účelem je implementace schémat kódování kanálu, která chrání uživatelská data a řídicí informace před chybami vznikajícími během přenosu přes rozhraní vzduchu. CCU funguje tak, že přebírá bloky informačních bitů z vyšších vrstev a systematicky přidává redundantní bity podle specifických kódovacích algoritmů. Tato redundance umožňuje přijímači detekovat a, což je důležitější, opravit určitý počet bitových chyb způsobených zhoršením kvality kanálu, jako je šum, interference a útlum. Návrh a výběr kódovacího schématu zahrnuje kritický kompromis mezi množstvím přidané redundance (režie) a výslednou schopností korekce chyb, což přímo ovlivňuje spektrální účinnost a odolnost spoje.

Z architektonického hlediska se CCU typicky nachází v řetězci základního pásma zpracování vysílače, po fázích zdrojového kódování a segmentace, ale před modulací a rozprostřením. Její činnost lze rozdělit na několik klíčových podfunkcí. Nejprve často přidává bity cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)) pro detekci chyb. Poté aplikuje hlavní algoritmus kódování kanálu, jako je konvoluční kódování, turbo kódování nebo kódování s nízkou hustotou parity ([LDPC](/mobilnisite/slovnik/ldpc/)), které zavádí redundanci pro korekci chyb. Následně zakódovaný bitový proud obvykle prochází přizpůsobením rychlosti, kde jsou bity propichovány (odstraňovány) nebo opakovány, aby odpovídaly specifické velikosti přenosového bloku přidělené pro přenos. Nakonec jsou zakódované bity prokládány, aby se rozložily potenciální shlukové chyby způsobené kanálem, což je činí lépe zvládnutelnými pro dekodér.

Přijímač obsahuje doplňkovou jednotku pro dekódování kanálu. Provádí inverzní operace: zpětné prokládání, zpětné přizpůsobení rychlosti a dekódování pomocí algoritmů, jako je Viterbiho algoritmus pro konvoluční kódy nebo iterační šíření přesvědčení pro turbo/LDPC kódy. Dekodér využívá redundanci k rekonstrukci původních informačních bitů a opravě chyb až do navrženého limitu kódu. Výkonnost CCU je kvantifikována metrikami, jako je kódový zisk, který měří snížení potřebného poměru signálu k šumu pro cílový [BER](/mobilnisite/slovnik/ber/) ve srovnání s nekódovaným systémem. Konkrétní kódovací schéma a parametry (např. kódová rychlost) jsou dynamicky vybírány řídicí vrstvou vyšší úrovně na základě podmínek kanálu a požadavků služby, čímž se vyvažuje spolehlivost a propustnost.

V širším kontextu sítě je CCU klíčovým prvkem pro dosažení cílů kvality služeb (QoS) definovaných pro různé služby, od hlasových hovorů po vysokorychlostní data. Její účinnost přímo ovlivňuje kapacitu buňky a uživatelský zážitek. Zatímco její základní principy zůstávají konstantní, implementace a podporované algoritmy se významně vyvíjely napříč vydáními 3GPP, aby podpořily vyšší datové rychlosti, nižší latenci a rozmanitější případy užití, přičemž pokročilé kódy, jako jsou polární kódy, byly zavedeny v 5G NR.

## K čemu slouží

Jednotka pro kódování kanálu existuje proto, aby bojovala proti inherentní nespolehlivosti bezdrátového komunikačního kanálu. Na rozdíl od drátových médií je rádiový kanál náchylný k šumu, interferenci, vícecestnému útlumu a Dopplerovým posunům, které narušují přenášený signál a způsobují bitové chyby. Bez této ochrany by tyto chyby učinily digitální komunikaci nepoužitelnou pro většinu aplikací. Základním problémem, který CCU řeší, je, jak přenášet digitální informace spolehlivě přes nespolehlivé médium. Toho dosahuje aplikací principů teorie informace, konkrétně kódování kanálu, které zavádí řízenou redundanci, aby přijímač mohl obnovit původní zprávu, i když jsou některé bity přijaty chybně.

Historicky používaly rané digitální mobilní systémy, jako je GSM, ve své CCU relativně jednoduché konvoluční kódy. S rostoucími požadavky na datovou rychlost u UMTS a nástupem mobilního širokopásmového přístupu se limity těchto kódů staly zřejmými, zejména pro vyšší datové rychlosti, kde nabízely klesající návratnost. To motivovalo vytvoření a standardizaci výkonnějších kódovacích schémat, nejvýznamněji turbo kódování, které bylo zavedeno v 3GPP Release 4 pro UMTS. Turbo kódy se mohly přiblížit teoretické Shannonově hranici mnohem blíže než konvoluční kódy, poskytovaly významný kódový zisk a umožňovaly efektivní vysokorychlostní datové služby. Neustálá snaha o vyšší spektrální účinnost a podpora nových služeb (jako je URLLC s nízkou latencí nebo hromadná komunikace mezi stroji v 5G) byla hlavní motivací pro pokračující vývoj schopností CCU.

Vytvoření a zdokonalování CCU řeší základní kompromis v digitálních komunikacích: spolehlivost versus účinnost. Přidání větší redundance (nižší kódová rychlost) zlepšuje spolehlivost, ale snižuje čistou informační rychlost pro danou šířku pásma kanálu. CCU prostřednictvím pokročilých algoritmů a adaptivního řízení umožňuje síťovým operátorům dynamicky optimalizovat tento kompromis na základě podmínek kanálu v reálném čase a požadavků služby. Tato přizpůsobivost je klíčová pro maximalizaci kapacity sítě a zajištění konzistentního uživatelského zážitku v různých rádiových prostředích, od středů buněk po jejich okraje.

## Klíčové vlastnosti

- Implementuje mechanismy detekce chyb, jako je připojení CRC
- Aplikuje kódy pro dopřednou korekci chyb (FEC), jako jsou konvoluční, turbo nebo LDPC kódy
- Provádí přizpůsobení rychlosti pomocí propichování nebo opakování, aby odpovídalo velikostem přenosových bloků
- Zahrnuje prokládání ke zmírnění dopadu shlukových chyb na rádiovém kanálu
- Podporuje více kódovacích schémat a kódových rychlostí dynamicky vybíraných řídicí vrstvou vyšší úrovně
- Umožňuje významný kódový zisk, což snižuje potřebný poměr signálu k šumu pro spolehlivou komunikaci

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TS 46.061** (Rel-19) — GSM EFR Frame Substitution and Muting Procedure
- **TS 48.061** (Rel-19) — BTS-TRAU Protocol for HR Speech/Data

---

📖 **Anglický originál a plná specifikace:** [CCU na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccu/)
