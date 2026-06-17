---
slug: "8-psk"
url: "/mobilnisite/slovnik/8-psk/"
type: "slovnik"
title: "8-PSK – 8-state Phase Shift Keying"
date: 2025-01-01
abbr: "8-PSK"
fullName: "8-state Phase Shift Keying"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/8-psk/"
summary: "8-PSK je digitální modulační schéma používané v systémech 3GPP, zejména v EDGE (Enhanced Data rates for GSM Evolution). Přenáší 3 bity na symbol využitím osmi různých fázových stavů, což umožňuje vyšš"
---

8-PSK je digitální modulační schéma používané v 3GPP EDGE, které přenáší 3 bity na symbol využitím osmi různých fázových stavů pro vyšší datové rychlosti při zachování zpětné kompatibility se systémem GSM.

## Popis

8-PSK je fázová modulační technika, při níž je fáze nosného signálu posunuta do jednoho z osmi rovnoměrně rozložených úhlů (0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°) pro reprezentaci digitálních dat. Každý fázový stav odpovídá jedinečnému 3bitovému symbolu (od 000 do 111), což efektivně ztrojnásobuje spektrální účinnost ve srovnání s Gaussovskou modulací s minimálním fázovým posuvem ([GMSK](/mobilnisite/slovnik/gmsk/)) používanou v základním GSM, která přenáší 1 bit na symbol. Proces modulace zahrnuje mapování skupin tří bitů na konkrétní fázové posuvy, čímž vzniká signál s konstantní obálkou, který mohou efektivně zesilovat nelineární výkonové zesilovače běžně používané v mobilních zařízeních.

Ve specifikacích 3GPP je 8-PSK implementováno v rámci architektury Enhanced Data rates for GSM Evolution ([EDGE](/mobilnisite/slovnik/edge/)), definované jako součást GSM/EDGE Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Implementace fyzické vrstvy zachovává stejnou šířku kanálu 200 kHz a symbolovou rychlost (270,833 ksymbolů/s) jako GSM, čímž zajišťuje kompatibilitu se stávajícím plánováním kmitočtů. Klíčový rozdíl spočívá v konstelaci modulace: zatímco GMSK používá spojitou fázovou modulaci se dvěma stavy, 8-PSK využívá diskrétní fázové posuvy s osmi stavy, což vyžaduje sofistikovanější přijímací algoritmy pro detekci fáze a synchronizaci.

Technická implementace zahrnuje několik klíčových komponent: symbolový mapper převádí skupiny bitů na fázové úhly, filtr pro tvarování impulsu (obvykle využívající linearizované GMSK nebo jiné vhodné filtry) omezuje spektrální šířku pásma a kvadraturní modulátor generuje vlastní RF signál. Na přijímací straně je vyžadována koherentní detekce, zahrnující obnovu nosné, sledování fáze a ekvalizaci pro potlačení vlivu vícenásobného šíření. Zvýšená citlivost na fázový šum a změny amplitudy si vyžádala vylepšené kódování pro opravu chyb, což vedlo k vývoji nových schémat kódování kanálu v EDGE, včetně rodin [MCS](/mobilnisite/slovnik/mcs/) (Modulation and Coding Scheme), které adaptivně volí mezi GMSK a 8-PSK na základě stavu kanálu.

Úloha 8-PSK v síti je primárně vylepšením fyzické vrstvy GSM, které umožňuje vyšší špičkové datové rychlosti (až 59,2 kbit/s na časový slot oproti 22,8 kbit/s s GMSK) při zachování stejné struktury kanálu. To umožňuje síťovým operátorům upgradovat stávající infrastrukturu GSM pomocí softwarových aktualizací a menších hardwarových úprav namísto kompletní přestavby sítě. Tato technologie představuje klíčový evoluční krok mezi systémy 2G GSM a 3G UMTS a poskytuje nákladově efektivní cestu k vylepšeným mobilním datovým službám.

## K čemu slouží

8-PSK bylo vyvinuto pro řešení rostoucí poptávky po vyšších datových rychlostech v sítích GSM bez nutnosti zcela nových kmitočtových alokací nebo výměny infrastruktury. Jak na konci 90. let 20. století rostlo využívání mobilních dat, staly se zřejmými omezení modulace [GMSK](/mobilnisite/slovnik/gmsk/) – její účinnost 1 bit na symbol omezovala datový propust i přes vylepšení kódovacích schémat. 3GPP zavedlo 8-PSK ve vydání 5 jako součást [EDGE](/mobilnisite/slovnik/edge/), aby poskytlo zpětně kompatibilní cestu upgradu, která mohla ztrojnásobit spektrální účinnost v rámci stávajících parametrů kanálu GSM.

Primární motivací byly ekonomické důvody: mobilní operátoři potřebovali nabízet vylepšené datové služby, aby konkurovali vznikajícím 3G technologiím, a zároveň maximalizovat návratnost svých značných investic do infrastruktury GSM. 8-PSK to umožnilo tím, že stávající základnové stanice mohly být upgradovány novými jednotkami pro příjem a vysílání a softwarem, aniž by vyžadovaly kompletní výměnu lokalit. Tento přístup výrazně snížil kapitálové výdaje a prodloužil životnost sítí GSM během přechodu na 3G.

Technicky 8-PSK vyřešilo výzvu zvýšení datových rychlostí v omezených 200 kHz kanálech GSM. Předchozí přístupy, jako schémata kódování vyššího řádu, měly klesající výnosy kvůli omezením Shannonova limitu. Změnou základního modulačního schématu při zachování stejné symbolové rychlosti a struktury kanálu poskytlo 8-PSK efektivnější řešení. Vlastnost konstantní obálky byla obzvláště důležitá pro kompatibilitu s existujícími návrhy výkonových zesilovačů, i když vyžadovala lineárnější zesílení než GMSK, což představovalo kompromis mezi zlepšením datové rychlosti a složitostí implementace.

## Klíčové vlastnosti

- Přenáší 3 bity na symbol využitím osmi fázových stavů (0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°)
- Zachovává stejnou šířku kanálu 200 kHz a rychlost 270,833 ksymbolů/s jako GSM pro zpětnou kompatibilitu
- Umožňuje špičkové datové rychlosti až 59,2 kbit/s na časový slot v sítích EDGE
- Používá modulaci s konstantní obálkou vhodnou pro nelineární výkonové zesilovače
- Vyžaduje koherentní detekci s obnovou nosné a sledováním fáze na přijímači
- Implementováno s adaptivními modulačními a kódovacími schématy (MCS), která přepínají mezi GMSK a 8-PSK na základě stavu kanálu

## Související pojmy

- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [8-PSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/8-psk/)
