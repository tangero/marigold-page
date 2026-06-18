---
slug: "rxu"
url: "/mobilnisite/slovnik/rxu/"
type: "slovnik"
title: "RXU – Receiver Unit"
date: 2020-01-01
abbr: "RXU"
fullName: "Receiver Unit"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rxu/"
summary: "Funkční jednotka v základnové stanici zodpovědná za příjem vzestupných (uplink) rádiových signálů. Provádí klíčový RF procesing včetně zesílení, filtrace a analogově-digitálního převodu, což základnov"
---

RXU je přijímací jednotka v základnové stanici, která zpracovává vzestupné (uplink) rádiové signály prostřednictvím RF procesingu, jako je zesílení a analogově-digitální převod, a umožňuje dekódování přenosů od uživatele.

## Popis

Přijímací jednotka (RXU) je základní hardwarová komponenta v rádiové přístupové síti (RAN), konkrétně integrovaná v základnových stanicích jako NodeB, eNodeB nebo gNB. Je součástí architektury dálkové rádiové jednotky (RRU) nebo aktivní anténní jednotky ([AAU](/mobilnisite/slovnik/aau/)), která odděluje funkce radiofrekvenčního ([RF](/mobilnisite/slovnik/rf/)) okruhu od basebandového procesingu. Primární úlohou RXU je zpracování cesty vzestupného (uplink) signálu. Připojuje se k anténním elementům přes duplexer nebo cirkulátor, který odděluje vysílané a přijímané signály. Po příjmu analogového RF signálu od uživatelského zařízení (UE) RXU provádí šumově nízké zesílení ([LNA](/mobilnisite/slovnik/lna/)) pro zesílení slabého signálu při minimálním přidaném šumu. Následuje filtrace pro odstranění nežádoucího rušení mimo pásmo a převod na střední frekvenci ([IF](/mobilnisite/slovnik/if/)) nebo přímo na základovou kmitočtovou oblast (baseband). Nakonec RXU digitalizuje signál pomocí vysokorychlostních analogově-digitálních převodníků ([ADC](/mobilnisite/slovnik/adc/)), čímž připraví digitální vzorky ve fázi a kvadratuře (I/Q) pro další basebandové zpracování v distribuované jednotce ([DU](/mobilnisite/slovnik/du/)) nebo centrální jednotce.

Z architektonického hlediska je RXU navržena pro škálovatelnost a flexibilitu. V systémech s masivním [MIMO](/mobilnisite/slovnik/mimo/) může AAU obsahovat desítky až stovky RXU, přičemž každá je přiřazena ke konkrétnímu anténnímu elementu nebo subpoli. To umožňuje pokročilé techniky beamformingu a prostorového zpracování. Výkon RXU je charakterizován klíčovými parametry, jako je šumové číslo, které určuje citlivost; dynamický rozsah, který zvládá proměnlivou sílu signálu; a linearita, která zabraňuje zkreslení. Kalibrační mechanismy jsou často vestavěny pro zajištění fázové a amplitudové koherence napříč více RXU, což je zásadní pro přesné odhady kanálu a beamformingové algoritmy.

Při provozu sítě RXU spolupracuje s vysílací jednotkou ([TXU](/mobilnisite/slovnik/txu/)). Přijaté digitální vzorky jsou odesílány přes fronthaulové rozhraní, jako je Common Public Radio Interface (CPRI) nebo enhanced CPRI (eCPRI), do basebandové jednotky. Zde se provádějí složité úlohy digitálního zpracování signálu (DSP), jako je rychlá Fourierova transformace (FFT) pro OFDM demodulaci, odhad kanálu, ekvalizace a dekódování. Konstrukce RXU přímo ovlivňuje metriky výkonu v uplinku, jako je propustnost na okraji buňky, spolehlivost pokrytí a schopnost podporovat modulační schémata vyššího řádu. Její vývoj je úzce spjat s pokrokem v RF polovodičové technologii, který umožňuje širší šířky pásma, lepší energetickou účinnost a podporu nových kmitočtových pásem v každé verzi standardu 3GPP.

## K čemu slouží

RXU existuje za účelem fyzické realizace funkce přijímače v uplinku v buňkové základnové stanici. Její vznik je motivován základní potřebou zachytit slabé rádiové signály vysílané mobilními zařízeními, často na okraji buňky, a převést je do čistého digitalizovaného formátu pro následné zpracování. Bez výkonné RXU by základnová stanice nebyla schopna spolehlivě dekódovat uživatelská data, což by vedlo ke špatné kvalitě služeb a přerušeným spojením. Oddělení RXU do vzdálené jednotky, jako součásti architektury funkčního rozdělení RAN, bylo hnáno snahou umístit RF komponenty blíže k anténám. Tím se snižují ztráty v přívodních kabelech, zlepšuje se kvalita signálu a umožňuje efektivnější nasazení stanovišť, což je klíčové pro vysokofrekvenční pásma jako mmWave, kde je útlum signálu značný.

Historicky byly v raných buňkových systémech přijímací funkce integrovány do rozměrných skříní základnových stanic. Přechod k distribuovaným architekturám RAN, jako je Cloud RAN (C-RAN), si vyžádal oddělení rádiové jednotky. RXU jako klíčová část této jednotky řeší problém degradace signálu na dlouhých koaxiálních trasách tím, že provádí kritické analogové zpracování přímo na anténním stožáru. Její vývoj navíc reaguje na rostoucí nároky nových rádiových rozhraní. Například přechod z WCDMA na LTE a poté na 5G NR vyžadoval, aby RXU podporovaly širší kanálová pásma, složitější víceanténní schémata (MIMO) a přísnější požadavky na linearitu pro pokročilé modulace jako 256-QAM a 1024-QAM. RXU je tedy klíčovým prvkem umožňujícím dosažení vysokých přenosových rychlostí a nízké latence slibovaných moderními buňkovými standardy.

## Klíčové vlastnosti

- Provádí šumově nízké zesílení (LNA) vzestupných (uplink) RF signálů
- Provádí analogovou filtraci a převod na základovou kmitočtovou oblast (baseband)
- Digitalizuje analogový signál pomocí vysokorychlostních analogově-digitálních převodníků (ADC)
- Navržena pro integraci do dálkových rádiových hlav (RRH) nebo aktivních anténních jednotek (AAU)
- Podporuje kalibraci pro fázovou/amplitudovou koherenci v víceanténních systémech
- Komunikuje s basebandovými jednotkami přes fronthaulové protokoly jako CPRI/eCPRI

## Související pojmy

- [TXU – Transmitter Unit](/mobilnisite/slovnik/txu/)
- [AAU – Active Antenna Unit](/mobilnisite/slovnik/aau/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TS 38.809** (Rel-16) — IAB Radio Transmission & Reception Background
- **TS 38.817** — 3GPP TR 38.817

---

📖 **Anglický originál a plná specifikace:** [RXU na 3GPP Explorer](https://3gpp-explorer.com/glossary/rxu/)
