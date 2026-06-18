---
slug: "cpbcch"
url: "/mobilnisite/slovnik/cpbcch/"
type: "slovnik"
title: "CPBCCH – Compact Packet Broadcast Control Channel"
date: 2025-01-01
abbr: "CPBCCH"
fullName: "Compact Packet Broadcast Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cpbcch/"
summary: "Logický kanál v GSM/EDGE rádiové přístupové síti (GERAN) používaný k vysílání základních systémových informací mobilním zařízením v paketovém režimu. Umožňuje efektivní výběr buňky, přístup k síti a m"
---

CPBCCH je logický kanál v sítích GSM/EDGE, který vysílá základní systémové informace v kompaktní formě mobilním zařízením pro efektivní přístup k paketovým službám a mobilitu.

## Popis

Compact Packet Broadcast Control Channel (CPBCCH) je logický vysílací kanál definovaný v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)) speciálně pro paketový ([PS](/mobilnisite/slovnik/ps/)) provoz. Funguje jako primární vysílací kanál pro [GPRS](/mobilnisite/slovnik/gprs/) a EDGE, obdobně jako Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) používaný pro služby s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). CPBCCH vysílá základní bloky systémových informací ([SIB](/mobilnisite/slovnik/sib/)), které musí mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) přečíst, aby získaly přístup a mohly pracovat v síti GPRS. Tyto informace zahrnují parametry pro identifikaci sítě a buňky, konfiguraci rádiového přístupu, seznamy sousedních buněk a řídicí parametry pro paketové datové protokoly. Kanál je mapován na fyzické rádiové zdroje, typicky s využitím Packet Data Traffic Channel (PDTCH) nebo Packet Broadcast Control Channel (PBCCH) v konkrétní, opakující se struktuře časového slotu, což zajišťuje, že mobilní zařízení mohou efektivně dekódovat vysílaná data bez nutnosti navázání vyhrazeného spojení.

Z architektonického hlediska je CPBCCH řízen podsystémem základnové stanice (BSS), konkrétně základnovou přenosovou stanicí (BTS) pod kontrolou řadiče základnové stanice (BSC). BSC naplňuje vysílané informace, které pocházejí z podpůrného uzlu pro GPRS (SGSN) v jádru sítě, včetně identit směrovací oblasti a parametrů řízení přístupu. Na rozhraní vzduchu (rozhraní Um) jsou informace CPBCCH přenášeny vysílacím způsobem v rámci definované struktury rádiového bloku v časovém slotu nakonfigurovaném pro paketové řízení. Mobilní stanice v pohotovostním stavu (GPRS standby) nebo ve stavu připravenosti tento kanál sledují, aby získaly kritická data pro výběr buňky, její převýběr a zahájení paketových datových relací prostřednictvím náhodného přístupového kanálu (PRACH) a kanálu pro povolení přístupu (PAGCH).

Provoz CPBCCH zahrnuje cyklické vysílání zpráv systémových informací, organizovaných do různých typů (např. PSI1, PSI2, PSI3 atd.), které nesou specifické sady parametrů. Tyto zprávy jsou vysílány s definovanou periodou opakování a plánováním, aby byla vyvážena režie a dostupnost. Klíčovým aspektem je jeho 'kompaktní' povaha, navržená tak, aby minimalizovala režii vysílání a spotřebu energie jak pro síť, tak pro mobilní zařízení ve srovnání s použitím plného CS BCCH pro PS informace. Mobilní stanice tyto informace používá k synchronizaci se sítí, určení vhodnosti buňky (na základě síly signálu a přístupových oprávnění) a k získání potřebných parametrů řízení rádiového spoje pro vytváření dočasných toků bloků (TBF) pro přenos dat.

V širším síťovém kontextu je CPBCCH nedílnou součástí procedur správy mobility a správy relací v GPRS/EDGE. Podporuje převýběr buňky tím, že poskytuje informace o sousedních buňkách, včetně jejich frekvencí a toho, zda podporují GPRS. Také vysílá parametry pro správu rádiových zdrojů (RR) v paketové doméně, jako je řízení časového předstihu a nastavení řízení výkonu. Spolehlivý příjem tohoto kanálu je klíčový pro plynulou dostupnost datových služeb, protože neschopnost dekódovat informace CPBCCH může zabránit zařízení v přístupu ke službám GPRS, i když jsou dostupné hlasové služby (prostřednictvím BCCH).

## K čemu slouží

CPBCCH byl zaveden, aby řešil základní potřebu vyhrazeného, efektivního vysílacího mechanismu pro systémové informace v paketové doméně sítí GSM, konkrétně pro služby GPRS a později EDGE. Před jeho zavedením se rané implementace GPRS mohly opírat o stávající kanál Broadcast Control Channel (BCCH) pro přenos některých paketových systémových informací, ale tento přístup byl neefektivní a omezený. BCCH byl optimalizován pro hlasové služby a jeho vysílací kapacita byla omezená; přidání rozsáhlých parametrů GPRS by spotřebovalo cennou šířku pásma potřebnou pro základní CS vysílání a mohlo by oddálit zavedení pokročilých PS funkcí. Navíc mobilní zařízení pracující v paketovém režimu vyžadovala rychlý přístup k parametrům specifickým pro PS bez nutnosti analyzovat informace zaměřené na CS, což mělo dopad na životnost baterie a doby přístupu.

Vytvoření CPBCCH tyto nedostatky vyřešilo tím, že poskytlo samostatný logický kanál přizpůsobený pro paketová data. To umožnilo strukturovanější a komplexnější vysílání všech potřebných systémových informací GPRS, včetně parametrů pro paketovou časovou synchronizaci, schémata kódování kanálu a síťové přístupové protokoly specifické pro datové služby. Umožnilo nezávislý vývoj a optimalizaci paketového vysílacího proudu. Filozofie 'kompaktního' návrhu si kladla za cíl minimalizovat režii rádiových zdrojů při zajištění spolehlivého a rychlého získání informací mobilními stanicemi, což je kritické pro efektivní převýběr buňky a rychlé navázání datových relací. To bylo obzvláště důležité pro podporu datových aplikací v režimu 'vždy připojen' a zlepšení uživatelského zážitku u služeb mobilního internetu.

Historicky byl CPBCCH součástí vylepšení GSM fáze 2+ standardizovaných ve 3GPP Release 6, která zdokonalila architekturu GPRS/EDGE pro lepší výkon a kapacitu. Jeho zavedení usnadnilo plné uskutečnění GPRS jako paralelní paketové sítě nadstavby na infrastruktuře GSM. Poskytnutím vyhrazeného vysílacího kanálu zajistil, že paketové datové služby mohou být nasazovány, řízeny a optimalizovány nezávisle na hlasových službách, čímž připravil cestu pro mobilní datové služby, které předcházely 3G UMTS a později 4G LTE.

## Klíčové vlastnosti

- Vyhrazený logický vysílací kanál pro systémové informace GPRS/EDGE v paketovém režimu
- Vysílá zprávy Packet System Information (PSI), nezbytné pro přístup k síti a mobilitu
- Umožňuje efektivní výběr a převýběr buňky pro zařízení v pohotovostním režimu GPRS
- Minimalizuje režii vysílání a spotřebu energie zařízení ve srovnání s použitím CS BCCH
- Podporuje parametry pro paketovou časovou synchronizaci, kódování kanálu a řízení rádiových zdrojů
- Usnadňuje nezávislý vývoj a správu paketových datových služeb v rámci GSM

## Související pojmy

- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [PBCCH – Packet Broadcast Control Channel](/mobilnisite/slovnik/pbcch/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CPBCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpbcch/)
