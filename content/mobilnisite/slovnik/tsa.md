---
slug: "tsa"
url: "/mobilnisite/slovnik/tsa/"
type: "slovnik"
title: "TSA – Temporal Sub-layer Access"
date: 2025-01-01
abbr: "TSA"
fullName: "Temporal Sub-layer Access"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tsa/"
summary: "Temporal Sub-layer Access (TSA, přístup k časovým podvrstvám) je funkce definovaná v rámci 3GPP pro službu Multimedia Broadcast/Multicast Service (MBMS). Umožňuje doručování mediálního obsahu ve více"
---

TSA je funkce 3GPP MBMS, která umožňuje doručování médií ve více časových vrstvách, což přijímačům umožňuje přístup k různým úrovním kvality na základě stavu sítě a možností zařízení.

## Popis

Temporal Sub-layer Access (TSA, přístup k časovým podvrstvám) je technický mechanismus specifikovaný v rámci architektury 3GPP Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), primárně dokumentovaný v TS 26.906. Je navržen pro práci se škálovatelným kódováním videa ([SVC](/mobilnisite/slovnik/svc/)), kde je video proud zakódován do základní vrstvy a jedné či více zlepšujících vrstev. TSA konkrétně spravuje časový aspekt těchto vrstev. Základní vrstva poskytuje základní snímkovou frekvenci, zatímco časové zlepšující vrstvy přidávají snímky pro zvýšení plynulosti a vnímané kvality videa. Ve scénáři MBMS vysílání jsou tyto různé časové podvrstvy přenášeny jako samostatné logické kanály nebo v rámci strukturovaného transportního proudu.

Architektura zahrnuje MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) a vysílací/multicastovou servisní centrálu ([BM-SC](/mobilnisite/slovnik/bm-sc/)), které jsou zodpovědné za oznámení služby a doručování obsahu. BM-SC ve spolupráci s poskytovatelem obsahu připravuje škálovatelné mediální proudy. Informace o TSA jsou signalizovány v rámci popisu služby, což umožňuje uživatelskému zařízení (UE) porozumět struktuře dostupných časových vrstev. Přístupová síť (např. LTE eMBMS nebo 5G NR [MBS](/mobilnisite/slovnik/mbs/)) následně plánuje a vysílá tyto vrstvy, potenciálně s využitím různých modulačních a kódovacích schémat nebo přidělení zdrojů na základě priority.

Z pohledu UE TSA umožňuje adaptivní přehrávání. UE s dobrými signálovými podmínkami může přijímat a dekódovat více časových zlepšujících vrstev, což vede k videu s vyšší snímkovou frekvencí. Naopak, UE v oblasti se špatným pokrytím nebo s omezeným výpočetním výkonem může dekódovat pouze základní vrstvu, čímž je zajištěna kontinuita služby při nižší kvalitě. Síť může tuto strukturu využít také pro efektivní správu zdrojů, protože ne všechna UE potřebují přijímat proud nejvyšší kvality. Mechanismus funguje v součinnosti s dalšími funkcemi MBMS, jako je File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)) a forward error correction na aplikační vrstvě ([AL-FEC](/mobilnisite/slovnik/al-fec/)), aby bylo zajištěno spolehlivé doručení.

Role TSA je nedílnou součástí poskytování vysílací služby s řízenou kvalitou. Umožňuje, aby jediný vysílací přenos obsloužil heterogenní populaci zařízení s různými možnostmi a podmínkami příjmu, čímž optimalizuje jak uživatelský zážitek, tak využití síťových zdrojů. Je klíčovým prvkem pro efektivní mobilní [TV](/mobilnisite/slovnik/tv/), komunikace pro veřejnou bezpečnost a aktualizace softwaru přes vzduch (SOTA) vysílacím způsobem.

## K čemu slouží

TSA byla zavedena, aby řešila výzvy spojené s doručováním kvalitních video služeb masivnímu počtu uživatelů současně prostřednictvím vysílání/multicastu, což je hlavní cíl MBMS. Před škálovatelným kódováním videa a funkcemi jako TSA by vysílací služby typicky přenášely jediný proud pevné kvality. To bylo neefektivní, protože se nemohly přizpůsobit různorodým podmínkám příjmu uživatelů; uživatelé se špatným signálem by zažívali přerušení, zatímco síť plýtvala kapacitou vysíláním kvalitních proudů uživatelům, kteří je nemohli dekódovat nebo je nepotřebovali.

Hlavní problém, který TSA řeší, je efektivní využití vysílacího spektra a rádiových zdrojů při zachování konzistentního uživatelského zážitku. Umožněním časové škálovatelnosti může poskytovatel služeb vysílat jednu integrovanou proudovou strukturu, která uspokojí jak prémiové, tak základní úrovně služeb, nebo zařízení v centru buňky a na jejím okraji. Tím odpadá potřeba simultánního vysílání (simulcast) více nezávislých proudů různé kvality, což spotřebovává výrazně více šířky pásma.

Její vytvoření bylo motivováno vývojem standardů pro kódování videa, jako je H.264/SVC a později HEVC, které učinily škálovatelné kódování praktickým. 3GPP integrovalo podporu těchto kodeků do svých specifikací MBMS, aby se mobilní vysílání stalo životaschopnou a efektivní technologií pro aplikace jako živé přenosy sportovních událostí, vysílání zpráv a nouzová varování, kde je klíčové oslovit velké publikum s omezenými, sdílenými síťovými zdroji.

## Klíčové vlastnosti

- Umožňuje doručování časově škálovatelných video proudů (základní vrstva a zlepšující vrstvy)
- Umožňuje uživatelskému zařízení (UE) adaptivně dekódovat video na základě kvality přijímaného signálu a možností zařízení
- Podporuje efektivní využití vysílacích zdrojů tím, že obslouží heterogenní zařízení jedinou přenosovou strukturou
- Integruje se s architekturou 3GPP MBMS (BM-SC, MBMS-GW)
- Používá oznámení služby a signalizaci k informování UE o dostupných časových podvrstvách
- Usnadňuje služby mobilní TV a skupinové komunikace s řízenou kvalitou

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MBS – Frequency Selection Area Identity](/mobilnisite/slovnik/mbs/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [TSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsa/)
