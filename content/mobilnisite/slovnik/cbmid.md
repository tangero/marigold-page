---
slug: "cbmid"
url: "/mobilnisite/slovnik/cbmid/"
type: "slovnik"
title: "CBMID – Cell Broadcast Message Identifier"
date: 2025-01-01
abbr: "CBMID"
fullName: "Cell Broadcast Message Identifier"
category: "Identifier"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/cbmid/"
summary: "CBMID je jedinečný identifikátor pro zprávy buňkového vysílání (CB) v sítích 3GPP. Umožňuje síti a uživatelskému zařízení (UE) rozlišovat různé vysílané zprávy, jako jsou veřejná varování nebo informa"
---

CBMID je jedinečný identifikátor, který umožňuje síti a uživatelskému zařízení rozlišovat různé zprávy vysílané buňkovým vysíláním (Cell Broadcast), například veřejná varování, pro cílené doručování a filtrování.

## Popis

Identifikátor zprávy buňkového vysílání (CBMID) je základní parametr v architektuře služby buňkového vysílání ([CBS](/mobilnisite/slovnik/cbs/)) 3GPP, definovaný primárně v TS 31.111 (USIM Application Toolkit). Jedná se o číselný identifikátor, který jednoznačně označuje konkrétní zprávu nebo sérii zpráv buňkového vysílání v dané geografické oblasti a po definované časové období. CBMID je vysílán sítí jako součást struktury [CB](/mobilnisite/slovnik/cb/) zprávy a je ukládán a zpracováván uživatelským zařízením (UE), konkrétně aplikací USIM nebo logikou pro zpracování CB v mobilním zařízení.

Architektonicky CBMID funguje ve spojení s dalšími parametry CB, jako je Identifikátor zprávy (Message ID) a Sériové číslo (Serial Number). Zatímco Message ID označuje obecný typ nebo kategorii zprávy (např. varování před zemětřesením, komerční informace), CBMID poskytuje jemnější granularitu. Umožňuje identifikaci konkrétní instance nebo varianty zprávy v rámci dané kategorie. Síťový prvek odpovědný za CBS, Centrum buňkového vysílání ([CBC](/mobilnisite/slovnik/cbc/)), přiřazuje CBMID při zahájení žádosti o vysílání prostřednictvím rozhraní CBC-RNC (v UMTS) nebo CBC-eNodeB (v LTE/5G NR). Přístupová síť (RAN) pak tento identifikátor zahrne do bloků systémové informace (např. SIB5, SIB6, SIB7 v LTE) používaných pro přenos CB zpráv.

Jak to funguje, zahrnuje několik klíčových komponent. Nejprve CBC po přijetí žádosti o vysílání zprávy (např. od systému veřejného varování) zprávu naformátuje a přiřadí jí CBMID. Toto přiřazení je klíčové pro správu životního cyklu zprávy. Zpráva spolu se svým CBMID je odeslána do uzlů RAN (NodeB nebo eNodeB/gNB) obsluhujících cílové buňky. RAN naplánuje vysílání a přenese jej přes rozhraní rádiového přístupu. Na straně UE funkce příjmu CB monitoruje zprávy. UE může být nakonfigurováno se seznamem CBMID (nebo jejich rozsahů), na které má naslouchat; tento proces je často řízen USIM prostřednictvím proaktivního příkazu CBS (SETUP EVENT LIST). Když je CB zpráva přijata, UE zkontroluje její CBMID vůči svému uloženému seznamu. Pokud dojde ke shodě, zpráva je zpracována a případně zobrazena uživateli; pokud ne, je typicky zahozena, čímž se šetří prostředky UE.

Jeho role v síti je klíčová pro efektivní a cílené šíření informací. Použitím CBMID může síť spravovat více souběžných vysílacích kampaní bez konfliktů. Například různé záchranné složky mohou současně vysílat varování před povodněmi, požáry a únosy dětí, každé s odlišným CBMID, což zajišťuje, že je UE dokáží správně identifikovat a upřednostnit. CBMID také umožňuje aktualizaci a zrušení zprávy; nová zpráva se stejným CBMID může přepsat předchozí, nebo speciální zpráva o zrušení může cílit na konkrétní CBMID, aby zastavila jeho zobrazování. Tento identifikátor je tedy ústřední pro spolehlivost, škálovatelnost a uživatelské přizpůsobení služby buňkového vysílání a tvoří základ systémů veřejného varování, jako jsou EU-Alert a Wireless Emergency Alerts (WEA).

## K čemu slouží

CBMID byl vytvořen, aby řešil potřebu přesné identifikace a správy zpráv buňkového vysílání v sítích 3GPP. Před jeho standardizací byly mechanismy vysílání zpráv méně sofistikované a často postrádaly robustní způsob, jak rozlišit různé instance stejného typu zprávy nebo efektivně spravovat životní cyklus vysílací kampaně. Toto omezení bylo zvláště problematické pro systémy veřejného varování, kde je včasná, přesná a jednoznačná komunikace klíčová pro veřejnou bezpečnost. CBMID poskytuje potřebnou granularitu pro podporu těchto pokročilých případů užití.

Historicky, jak se mobilní sítě vyvíjely od základních hlasových služeb k platformám pro veřejné informace, stala se zřejmou potřeba spolehlivého systému hromadného oznamování. Události jako přírodní katastrofy poukázaly na nedostatky varování založených na SMS, která trpí zahlcením sítě a nedostatkem geografického cílení. Služba buňkového vysílání, vylepšená identifikátory jako je CBMID, byla vyvinuta jako řešení. Funguje nezávisle na provozu typu bod-bod a vysílá zprávy všem UE v sadě buněk bez přetížení signalizačních kanálů. CBMID konkrétně řeší problém nejednoznačnosti a správy zpráv. Bez něj by UE mohlo mít potíže určit, zda je nově přijatá zpráva aktualizací předchozího varování nebo zcela novou zprávou, což by vedlo k potenciálnímu zmatení uživatele nebo informačnímu přetížení.

Motivace pro jeho vytvoření byla hnána regulatorními a komerčními požadavky. Regulátoři hledali standardizovanou, síťově řízenou metodu pro doručování geograficky cílených nouzových výstrah. Komerční operátoři také viděli hodnotu ve využití [CBS](/mobilnisite/slovnik/cbs/) pro služby informací založené na poloze. CBMID umožňuje obojí tím, že umožňuje zprávy jednoznačně označovat, filtrovat a spravovat. Řeší omezení spočívající pouze v hrubém identifikátoru Message ID přidáním druhé vrstvy identifikace, která je nezbytná pro zvládání více současných vysílání, obnovování zpráv, jejich vypršení a zrušení. Tato schopnost zajišťuje, že systém [CB](/mobilnisite/slovnik/cb/) není jen jednoduchým vysílacím kanálem, ale spravovanou službou schopnou podporovat složité, dynamické scénáře varování.

## Klíčové vlastnosti

- Jednoznačně identifikuje konkrétní instanci nebo sérii zprávy buňkového vysílání v geografické oblasti.
- Umožňuje filtrování na straně uživatelského zařízení (UE) a selektivní příjem zpráv na základě předkonfigurovaných seznamů.
- Umožňuje správu životního cyklu zprávy, včetně aktualizací, nahrazení a zrušení.
- Spolupracuje s Identifikátorem zprávy (Message ID) a poskytuje tak dvouúrovňovou kategorizaci zpráv.
- Je vysílán jako součást systémové informace, což umožňuje síťově řízené šíření.
- Je nezbytný pro fungování standardizovaných systémů veřejného varování (např. EU-Alert, WEA).

## Definující specifikace

- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification

---

📖 **Anglický originál a plná specifikace:** [CBMID na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbmid/)
