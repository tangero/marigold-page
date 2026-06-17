---
slug: "cpccch"
url: "/mobilnisite/slovnik/cpccch/"
type: "slovnik"
title: "CPCCCH – Compact Packet Common Control Channel"
date: 2025-01-01
abbr: "CPCCCH"
fullName: "Compact Packet Common Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cpccch/"
summary: "Specializovaný řídicí kanál v GSM/EDGE rádiové přístupové síti (GERAN) navržený pro efektivní vysílání systémových informací a pagingových zpráv v paketovém režimu. Umožňuje mobilním zařízením přístup"
---

CPCCCH je specializovaný řídicí kanál GSM/EDGE, který efektivně vysílá systémové informace a pagingové zprávy pro služby paketových dat, aby minimalizoval signalizační režii a šetřil rádiové prostředky.

## Popis

Compact Packet Common Control Channel (CPCCCH) je logický kanál definovaný v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)), který byl konkrétně zaveden pro podporu paketově orientovaných operací ve specifikacích 3GPP Release 8. Funguje jako vysílací kanál, který přenáší základní systémové informace a pagingové zprávy k mobilním stanicím ([MS](/mobilnisite/slovnik/ms/)), které jsou přihlášeny k buňce a jsou schopny nebo mají zájem o služby paketových dat. Na rozdíl od svého protějšku pro přepojování okruhů ([CCCH](/mobilnisite/slovnik/ccch/)) je CPCCCH optimalizován pro sporadickou a dávkovou povahu paketového datového provozu, což umožňuje efektivnější využití rádiových prostředků při podpoře technologií jako [GPRS](/mobilnisite/slovnik/gprs/) a EDGE.

Z architektonického hlediska je CPCCCH namapován na fyzické prostředky v rámci rámcové struktury GSM. Typicky využívá specifické časové sloty a rámce určené pro signalizaci paketového společného řízení. Kanál používá specifické kódovací a modulační schémata vhodné pro robustnost řídicí signalizace, často robustnější než schémata používaná pro přenos uživatelských dat, aby zajistil spolehlivý příjem i na okrajích buňky. Síť konfiguruje parametry CPCCCH, jako jsou míry opakování, plánování a přidružené logické kanály, prostřednictvím systémových informačních bloků (SIB) vysílaných na [BCCH](/mobilnisite/slovnik/bcch/), což umožňuje mobilním stanicím jej efektivně monitorovat podle svého provozního stavu (např. IDLE, READY).

Z procesního hlediska přenáší CPCCCH několik kritických typů zpráv. Především vysílá zprávy Packet System Information (PSI), které informují mobilní stanice o konfiguraci buňky, přístupových parametrech, informacích o sousedních buňkách a podrobnostech o směrovací oblasti specifických pro paketovou doménu. Za druhé přenáší Packet Paging Requests (PPCH) k upozornění mobilních stanic v režimu idle na příchozí paketové datové relace nebo k vyvolání aktualizací polohy. Návrh kanálu umožňuje mobilním stanicím se periodicky probouzet a naslouchat předdefinovaným pagingovým blokům, což výrazně prodlužuje výdrž baterie ve srovnání s nepřetržitým monitorováním.

CPCCCH pracuje v koordinaci s dalšími řídicími a přenosovými kanály. Je úzce spojen s Packet Broadcast Control Channel (PBCCH), který může nést další systémové informace specifické pro pakety, a s Packet Data Traffic Channel (PDTCH) používaným pro přenos skutečných uživatelských dat. Když mobilní stanice potřebuje zahájit paketovou datovou relaci, použije přístupové parametry přijaté přes CPCCCH k vysílání na Packet Random Access Channel (PRACH) nebo RACH. Obsah a plánování zpráv na CPCCCH řídí řadič základnové stanice ([BSC](/mobilnisite/slovnik/bsc/)) sítě a podpůrný uzel pro GPRS (SGSN) na základě topologie sítě, zatížení a populace zařízení podporujících pakety.

Jeho role v síti je zásadní pro správu mobility a navazování relací v paketových službách 2.5G/3G. Poskytnutím vyhrazeného, optimalizovaného kanálu pro paketovou řídicí signalizaci CPCCCH snižuje kolize a latenci při výběru buňky, převýběru a zahájení paketové datové relace. Tvoří základní kámen řídicí roviny pro GPRS/EDGE, což umožňuje efektivní podporu aplikací s trvalým připojením a bezproblémovou dostupnost datových služeb při pohybu uživatelů sítí.

## K čemu slouží

CPCCCH byl vytvořen, aby řešil specifické požadavky na řídicí signalizaci zavedené službami paketových dat v sítích GSM, konkrétně [GPRS](/mobilnisite/slovnik/gprs/) a EDGE. Před jeho zavedením byly sítě GSM primárně okruhově orientované a používaly Common Control Channels (CCCH) navržené pro navazování hlasových hovorů a službu krátkých zpráv. Tyto kanály byly neefektivní pro dávkovou, nespojovanou povahu paketových dat, která vyžadují časté, ale krátké řídicí zprávy pro paging, aktualizace buněk a přidělování prostředků. Stávající CCCH postrádal optimalizace pro úsporné cykly nespojitého příjmu (DRX), klíčové pro mobilní datová zařízení, a mohl se stát úzkým hrdlem s rostoucím počtem uživatelů paketových dat.

Motivace vycházela z komerčního nasazení služeb mobilního internetu na počátku 21. století, které odhalily omezení používání řídicích kanálů optimalizovaných pro hlas pro data. Bez vyhrazeného paketového řídicího kanálu musela paketová datová zařízení monitorovat kanály pro přepojování okruhů, což vedlo k zbytečnému vybíjení baterie, zvýšené signalizační zátěži a pomalejší odezvě při zahajování datových relací. CPCCCH to vyřešil poskytnutím samostatné, zjednodušené signalizační cesty, která mohla být optimalizována pro parametry, jako jsou cykly pagingových skupin, časování přístupu a opakování systémových informací specifických pro provozní stavy paketových dat.

Historicky bylo zavedení CPCCCH v 3GPP Release 8 (součást vývojových prací GSM/EDGE) klíčovým vylepšením, které zlepšilo výkon a kapacitu GERAN pro datové služby. Řešilo omezení dřívějších verzí, kde paketová signalizace často využívala prostředky pro přepojování okruhů nebo méně efektivní metody. Vytvořením samostatného kanálu umožnil síťovým operátorům dimenzovat a spravovat řídicí prostředky odděleně pro hlasový a datový provoz, čímž zlepšil celkovou efektivitu sítě a uživatelský komfort pro vznikající mobilní datové aplikace a připravil cestu pro pokročilejší paketové služby v rámci vývojové cesty GSM.

## Klíčové vlastnosti

- Optimalizované vysílání Packet System Information (PSI) pro konfiguraci sítě GPRS/EDGE
- Efektivní funkčnost Packet Paging Channel (PPCH) pro upozorňování datových zařízení v režimu idle
- Podpora nespojitého příjmu (DRX) pro výraznou úsporu energie mobilní stanice
- Vyhrazená struktura logického kanálu oddělená od CCCH pro přepojování okruhů, aby se zabránilo signalizačnímu zahlcení
- Mapování na specifické fyzické časové sloty/rámce v rámci TDMA struktury GSM pro spolehlivou řídicí signalizaci
- Koordinace s Packet RACH (PRACH) pro efektivní zahájení procedury náhodného přístupu mobilními stanicemi

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [CCCH – Common Control Channel](/mobilnisite/slovnik/ccch/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [CPCCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpccch/)
