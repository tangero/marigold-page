---
slug: "b-isdn"
url: "/mobilnisite/slovnik/b-isdn/"
type: "slovnik"
title: "B-ISDN – Broadband Integrated Services Digital Network"
date: 2026-01-01
abbr: "B-ISDN"
fullName: "Broadband Integrated Services Digital Network"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/b-isdn/"
summary: "Broadband ISDN (B-ISDN) je standardizovaná telekomunikační architektura navržená pro podporu vysokorychlostních multimediálních služeb přes digitální sítě. Rozšiřuje koncept ISDN pro zvládnutí širokop"
---

B-ISDN je standardizovaná telekomunikační architektura, která rozšiřuje ISDN o podporu vysokorychlostních multimediálních služeb, jako je videokonferencing, přes digitální sítě, a její koncepty ovlivnily rané definice širokopásmových služeb v 3GPP.

## Popis

Broadband Integrated Services Digital Network (B-ISDN) je komplexní síťová architektura standardizovaná [ITU-T](/mobilnisite/slovnik/itu-t/), na kterou se 3GPP odkazovalo v raných vydáních pro definice služeb a přenosových schopností. Byla koncipována jako evoluce úzkopásmového [ISDN](/mobilnisite/slovnik/isdn/) ([N-ISDN](/mobilnisite/slovnik/n-isdn/)) a navržena pro podporu širokého spektra služeb vyžadujících přenosové rychlosti výrazně vyšší než primární rozhraní (PRI) s 1,5 nebo 2 Mbps. Jádro B-ISDN je založeno na Asynchronous Transfer Mode ([ATM](/mobilnisite/slovnik/atm/)) jako své přepínací a multiplexní technologii. ATM používá buňky pevné velikosti (53 bajtů) k přenosu všech typů provozu – hlasu, dat a videa – a poskytuje jednotný spojově orientovaný transportní mechanismus. Tento buňkový přístup umožňuje efektivní statistický [multiplexing](/mobilnisite/slovnik/multiplexing/), poskytování kvality služeb (QoS) prostřednictvím parametrů provozní smlouvy jako Peak Cell Rate (PCR) a Sustainable Cell Rate (SCR) a podporu služeb s konstantní ([CBR](/mobilnisite/slovnik/cbr/)) i proměnnou (VBR) přenosovou rychlostí.

Referenční model protokolu B-ISDN je strukturován do tří rovin: Uživatelské roviny pro přenos uživatelských dat, Řídicí roviny pro řízení hovorů a spojení pomocí signalizačních protokolů jako Q.2931 a Roviny správy pro funkce správy sítě. Architektura je dále rozdělena na vrstvy: Fyzická vrstva, která definuje přenosová média a liniové kódy (např. Synchronous Digital Hierarchy - SDH); ATM vrstva, zodpovědná za zpracování hlaviček buněk, multiplexování a demultiplexování; a ATM Adaptation Layer ([AAL](/mobilnisite/slovnik/aal/)). AAL je klíčová, protože segmentuje protokoly vyšších vrstev do ATM buněk a na cíli je znovu sestavuje, přičemž různé typy AAL (např. [AAL1](/mobilnisite/slovnik/aal1/) pro emulaci okruhu, AAL5 pro data) jsou optimalizovány pro specifické třídy služeb.

V kontextu 3GPP je na B-ISDN odkazováno především v raných vydáních (od Rel-4) v souvislosti s přenosovými službami a teleslužbami, jak jsou definovány v specifikacích jako 22.101 a 22.105. Poskytla model pro popis širokopásmových přenosových schopností, které by mohly podporovat multimediální služby v UMTS a pozdějších systémech. Rámec služeb B-ISDN kategorizoval služby na interaktivní služby (např. konverzační, zasílání zpráv, vyhledávací) a distribuční služby (např. vysílání), což pomohlo utvářet rané požadavky na služby 3G. Zatímco sítě 3GPP nakonec přijaly transport založený na IP (GPRS, IMS) namísto nativního ATM/B-ISDN, koncepty z B-ISDN, jako jsou třídy QoS a spojově orientované přenosové služby, ovlivnily vývoj přenosových služeb UMTS a mechanismu PDP kontextu.

## K čemu slouží

B-ISDN byla vytvořena, aby řešila omezení úzkopásmového ISDN a rostoucí poptávku po vysokorychlostních integrovaných multimediálních službách na konci 80. a v 90. letech 20. století. Úzkopásmový ISDN s maximální rychlostí kolem 2 Mbps byl nedostatečný pro aplikace jako videokonference, přenos vysokorozlišujících obrazů a video na vyžádání, které vyžadují přenosové rychlosti v řádu desítek až stovek Mbps. Telekomunikační průmysl předvídal konvergenci služeb – hlasu, dat a videa – do jedné síťové infrastruktury a B-ISDN byla navržena jako standardizovaný rámec k dosažení tohoto cíle. Jejím záměrem bylo poskytnout budoucím výzvám odolnou, škálovatelnou digitální síť schopnou podporovat jakýkoli typ služby bez ohledu na její šířku pásma nebo charakteristiky provozu prostřednictvím jednotného buňkového transportního mechanismu.

Motivace pro B-ISDN byla hnací silou potřeby flexibilní, efektivní sítě, která by mohla garantovat kvalitu služeb pro různé aplikace. Předchozí okruhově přepínané sítě byly neefektivní pro trhavý datový provoz, zatímco paketově přepínané sítě jako X.25 postrádaly rychlost a záruky QoS pro média v reálném čase. B-ISDN s ATM ve svém jádře nabídla řešení: kombinovala spojově orientovanou povahu okruhového přepojování (zajišťující předvídatelný výkon) s efektivitou statistického multiplexování paketového přepojování. To umožnilo síťovým operátorům vybudovat jedinou infrastrukturu, která by mohla ekonomicky podporovat vše od tradiční telefonie po vznikající širokopásmové služby, optimalizovat využití zdrojů a zároveň splňovat přísné požadavky na zpoždění a ztrátu.

V 3GPP sloužila B-ISDN jako důležitý referenční model v raných vydáních pro definování služebních schopností sítí 3G. Při standardizaci UMTS existovala potřeba popsat přenosové služby, které by mohly podporovat multimediální aplikace. B-ISDN poskytovala dobře definovanou taxonomii a technický rámec pro takové služby, což pomohlo 3GPP specifikovat požadavky na přenosové služby UMTS. Ačkoli se 3GPP vyvíjelo směrem k plně IP jádrovým sítím (např. se zavedením IMS v Rel-5), počáteční závislost na konceptech B-ISDN pomohla překlenout propast mezi tradiční telekomunikací a službami založenými na paketech, což zajistilo, že systémy 3G mohly splňovat tehdejší očekávání širokopásmových služeb.

## Klíčové vlastnosti

- Založena na Asynchronous Transfer Mode (ATM) pro buňkové přepínání a multiplexování
- Podporuje vysoké přenosové rychlosti (typicky 155 Mbps a výše) využitím fyzických vrstev SDH/SONET
- Definuje komplexní třídy QoS a parametry správy provozu (např. PCR, SCR)
- Využívá vrstvový model protokolu s ATM Adaptation Layer (AAL) pro služebně specifickou segmentaci
- Poskytuje jednotný rámec pro integrované služby (hlas, video, data) přes jedinou síť
- Zahrnuje signalizační protokoly (např. Q.2931) pro dynamické vytváření a řízení spojení

## Související pojmy

- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)
- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 32.101** (Rel-19) — Management principles and high-level requirements

---

📖 **Anglický originál a plná specifikace:** [B-ISDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/b-isdn/)
