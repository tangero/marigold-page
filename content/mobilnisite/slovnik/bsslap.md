---
slug: "bsslap"
url: "/mobilnisite/slovnik/bsslap/"
type: "slovnik"
title: "BSSLAP – Base Station System Application Part"
date: 2025-01-01
abbr: "BSSLAP"
fullName: "Base Station System Application Part"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bsslap/"
summary: "BSSLAP je signalizační protokol používaný pro služby určování polohy (LCS) v sítích GSM a raných sítích UMTS. Funguje mezi centrem pro určování polohy (SMLC) a řídicím systémem základnových stanic (BS"
---

BSSLAP je signalizační protokol používaný pro služby určování polohy v sítích GSM a raných sítích UMTS, který funguje mezi SMLC a BSC a umožňuje síti určit geografickou polohu mobilního zařízení.

## Popis

Base Station System Application Part (BSSLAP) je klíčový signalizační protokol definovaný ve standardech 3GPP pro sítě GSM a rané sítě UMTS, konkrétně pro služby určování polohy ([LCS](/mobilnisite/slovnik/lcs/)). Funguje jako aplikační protokol v protokolovém zásobníku [BSSAP](/mobilnisite/slovnik/bssap/) a zprostředkovává komunikaci mezi centrem pro určování polohy ([SMLC](/mobilnisite/slovnik/smlc/)) a řídicím systémem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)). SMLC je síťový uzel zodpovědný za výpočet polohy mobilní stanice ([MS](/mobilnisite/slovnik/ms/)), zatímco BSC spravuje rádiové zdroje a řídí více základnových přijímacích a vysílacích stanic ([BTS](/mobilnisite/slovnik/bts/)). BSSLAP poskytuje specializované zprávy potřebné pro to, aby SMLC mohl vyžadovat a přijímat měřicí data od BSC a BTS, což je nezbytné pro provádění lokalizačních výpočtů.

Z architektonického hlediska jsou zprávy BSSLAP přenášeny přes protokol BSSAP, který sám využívá Signalizační spojový řídicí podsystém ([SCCP](/mobilnisite/slovnik/sccp/)) přes rozhraní A (mezi [MSC](/mobilnisite/slovnik/msc/) a BSC) nebo rozhraní Iu v UMTS. BSSLAP však konkrétně definuje signalizaci typu point-to-point mezi SMLC a BSC pro postupy specifické pro určování polohy. Protokol podporuje různé lokalizační metody, přičemž jeho primární návrh je zaměřen na metodu Enhanced Observed Time Difference (E-OTD). V E-OTD mobilní stanice měří pozorované časové rozdíly příchodu signálů z více geograficky rozptýlených BTS. BSC prostřednictvím BSSLAP tato měření od MS shromažďuje a předává je SMLC. SMLC následně tato data spolu se známými souřadnicemi polohy BTS a časovými informacemi použije k triangulaci polohy MS.

Klíčovými součástmi BSSLAP jsou typy zpráv pro požadavky na měření polohy, odpovědi a procedury přerušení. Například SMLC odešle BSC zprávu BSSLAP Connection Oriented Information, aby inicioval lokalizační požadavek, a specifikuje parametry jako požadovanou kvalitu služby (QoS) pro přesnost. BSC následně koordinuje s MS a BTS shromáždění potřebných rádiových měření, jako jsou časové posuny nebo pozorované časové rozdíly. Tato měření jsou zapouzdřena do zpráv BSSLAP a odeslána zpět SMLC. Protokol také řeší chybové stavy a správu zdrojů, aby zajistil, že lokalizační požadavky nepříznivě neovlivní běžné hlasové a datové služby. Role BSSLAP je nedílnou součástí umožnění síťového a mobilním zařízením asistovaného určování polohy, poskytuje základní signalizaci pro nouzové služby, služby založené na poloze a zákonné odposlechy v sítích 2G a raných 3G.

Během provozu BSSLAP spolupracuje s dalšími LCS protokoly, jako je Radio Resource LCS Protocol (RRLP) a Mobile Application Part (MAP). Zatímco RRLP zajišťuje signalizaci mezi MS a SMLC přes rádiové rozhraní, BSSLAP spravuje signalizaci v pevné síti mezi SMLC a BSC. Toto oddělení umožňuje efektivní distribuci zpracování: BSC zvládá koordinaci rádiových zdrojů, zatímco SMLC provádí složité výpočty polohy. Zprávy BSSLAP jsou typicky malé a nečasté, optimalizované pro minimalizaci signalizační zátěže. Protokol obsahuje funkce pro indikaci šifrování a podporu různých lokalizačních metod, i když jeho možnosti jsou omezenější ve srovnání s pozdějšími protokoly, jako je LTE Positioning Protocol (LPP) v sítích 4G. Přes svůj věk je porozumění BSSLAP důležité pro údržbu starších sítí a pro pochopení vývoje technologií určování polohy v mobilních sítích.

## K čemu slouží

BSSLAP byl vytvořen, aby řešil rostoucí potřebu přesného určování polohy mobilních zařízení v sítích GSM, poháněnou primárně regulatorními požadavky na nouzové služby (např. E911 ve Spojených státech) a komerční poptávkou po službách založených na poloze (LBS). Před jeho zavedením sítím GSM chyběl standardizovaný, efektivní signalizační mechanismus mezi síťovými entitami zodpovědnými za určování polohy. Rané lokalizační metody byly primitivní, často spoléhaly na Cell-ID (který poskytuje pouze oblast obsluhované buňky) nebo vyžadovaly proprietární implementace, které bránily interoperabilitě mezi zařízeními různých výrobců. BSSLAP poskytl standardizovaný protokol v rámci frameworku 3GPP, který umožnil konzistentní a spolehlivou komunikaci mezi SMLC a BSC pro pokročilé lokalizační techniky, jako je E-OTD.

Protokol řešil klíčové technické problémy definováním jasného rozhraní pro vyžádání a doručení rádiových měřicích dat nezbytných pro určování polohy založené na triangulaci. Bez BSSLAP by SMLC neměl standardizovaný způsob, jak instruovat BSC ke shromáždění specifických časových měření od mobilní stanice a základnových stanic, ani jak tato data přijímat ve strukturovaném formátu. Tato standardizace byla klíčová pro síťové operátory nasazující více-výrobcové sítě, protože zajišťovala, že služby určování polohy mohou bezproblémově fungovat napříč různými implementacemi BSC a SMLC. BSSLAP také pomohl optimalizovat síťové zdroje tím, že umožnil SMLC specifikovat parametry QoS pro určování polohy, takže BSC mohl lokalizační požadavky odpovídajícím způsobem upřednostnit bez narušení hovorů nebo jiných služeb.

Historicky se vývoj BSSLAP v 3GPP Release 7 (ačkoliv vycházel ze starších specifikací GSM) časově shodoval s dozráváním sítí GSM a počátečním nasazením UMTS. Představoval významný krok vpřed od základní lokalizace Cell-ID, umožňující přesnější určování polohy (typicky v rozmezí 50-150 metrů pro E-OTD) potřebné pro záchranné služby a komerční aplikace, jako je navigace a sledování majetku. Zatímco pozdější technologie, jako je U-TDOA (Uplink Time Difference of Arrival) a GNSS asistované metody, nakonec nabídly lepší přesnost, BSSLAP položil základy pro architektury síťového určování polohy. Jeho vytvoření bylo motivováno omezeními předchozích ad-hoc přístupů a poskytlo škálovatelné, standardy založené řešení, které podporovalo regulatorní a komerční imperativy mobilního průmyslu počátku 21. století.

## Klíčové vlastnosti

- Standardizovaná signalizace mezi SMLC a BSC pro služby určování polohy
- Podpora metody určování polohy Enhanced Observed Time Difference (E-OTD)
- Přenos přes protokolový zásobník BSSAP využívající spojení SCCP
- Definice typů zpráv pro požadavky na měření, odpovědi a procedury přerušení
- Zahrnutí parametrů kvality služby (QoS) pro přesnost určování polohy
- Zpracování indikací šifrování a chybových stavů

## Související pojmy

- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [E-OTD – Enhanced Observed Time Difference](/mobilnisite/slovnik/e-otd/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [BSSAP – Base Station Subsystem Application Part](/mobilnisite/slovnik/bssap/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [BSSLAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bsslap/)
