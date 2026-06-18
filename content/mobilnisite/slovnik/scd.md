---
slug: "scd"
url: "/mobilnisite/slovnik/scd/"
type: "slovnik"
title: "SCD – Signal Conditioning Device"
date: 2025-01-01
abbr: "SCD"
fullName: "Signal Conditioning Device"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/scd/"
summary: "Zařízení definované v 3GPP pro sítě GSM, které upravuje charakteristiky signálu, například amplitudu nebo fázi, za účelem zlepšení kvality přenosu nebo splnění specifických požadavků rozhraní. Jedná s"
---

SCD je zastaralé zařízení GSM, které upravuje charakteristiky signálu, jako je amplituda nebo fáze, za účelem zlepšení kvality přenosu a zajištění kompatibility mezi síťovými prvky.

## Popis

Signal Conditioning Device (SCD) je funkční komponenta specifikovaná v technických specifikacích GSM, konkrétně v 3GPP TS 46.008. Funguje na fyzické vrstvě síťové architektury a primárně se zabývá manipulací s elektrickými nebo vysokofrekvenčními signály. Její základní funkcí je kondicionování signálů, což zahrnuje procesy jako zesílení, filtrování, útlum nebo fázový posuv, aby byly připraveny k přenosu médiem nebo k příjmu jiným síťovým prvkem. Toto kondicionování je klíčové pro zachování integrity signálu, minimalizaci zkreslení a zajištění, že úrovně signálu jsou v rámci provozních parametrů vyžadovaných následnými stupni komunikačního řetězce.

Architektonicky SCD není samostatný síťový uzel jako Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) nebo Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)), ale spíše funkční blok, který může být integrován v jiném síťovém zařízení nebo existovat jako samostatná fyzická jednotka. Typicky tvoří rozhraní mezi různými segmenty sítě, například mezi Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)) a BSC, nebo v rámci přenosových vedení. Zařízení funguje tak, že přijímá vstupní signál, aplikuje předem definovanou sadu kondicionačních operací na základě svého návrhu a konfigurace, a poté vysílá upravený signál. Tyto operace jsou deterministické a jsou navrženy tak, aby působily proti specifickým závadám vlastním přenosové cestě nebo aby adaptovaly signál na jiný standard rozhraní.

Klíčové komponenty implementace SCD zahrnují vstupně/výstupní rozhraní, obvody pro zpracování signálu (které mohou zahrnovat analogové komponenty jako zesilovače a filtry nebo digitální signální procesory) a řídicí logiku. Její role je v zásadě o adaptaci signálu a zajištění kvality. Kondicionováním signálu SCD pomáhá snižovat míru bitových chyb, prodlužovat efektivní přenosové vzdálenosti a zajišťovat interoperabilitu mezi zařízeními různých výrobců, která mohou mít mírně odlišné požadavky na úroveň signálu. Jedná se o základní, i když často neviditelný prvek, který podporuje spolehlivé fyzické propojení, na kterém závisí protokoly a služby vyšších vrstev.

## K čemu slouží

Signal Conditioning Device byl vytvořen k řešení základních výzev v analogových a raných digitálních telekomunikačních sítích, konkrétně v rámci GSM. Primární problém, který řeší, je degradace signálu a nekompatibilita mezi různými síťovými segmenty a zařízeními. Jak signály putují po měděných vedeních, mikrovlnných spojích nebo v rámci složitých vysokofrekvenčních systémů, jsou vystaveny útlumu, šumu, zkreslení a interferencím. Bez kondicionování by tyto vady mohly způsobit nepoužitelnost signálu na přijímací straně, což by vedlo k přerušeným hovorům nebo špatné kvalitě dat.

Historicky, před vysoce integrovanými digitálními systémy, síťová rozhraní často spoléhala na analogové signalizace se specifickými požadavky na napětí, proud nebo výkon. Zařízení různých výrobců nebo různé části sítě (např. rozhraní Abis mezi [BTS](/mobilnisite/slovnik/bts/) a [BSC](/mobilnisite/slovnik/bsc/)) mohly mít nekompatibilní očekávání ohledně těchto charakteristik signálu. SCD poskytuje standardizovaný způsob, jak popsat a implementovat potřebnou adaptaci. Funguje jako 'překladač signálu' nebo 'zesilovač', který zajišťuje, že signál opouštějící jedno zařízení je dokonale upraven pro příjem dalším zařízením v řetězci. To bylo obzvláště kritické při nasazování a rozšiřování sítí GSM, kde bylo pro spolehlivost služeb zásadní zajistit konzistentní výkon fyzické vrstvy napříč různými geografickými instalacemi a prostředími s více dodavateli.

Motivací pro jeho specifikaci ve standardech 3GPP bylo poskytnout jasnou, interoperabilní definici této funkčnosti. Standardizací konceptu mohli síťoví operátoři pořizovat kompatibilní zařízení a výrobci mohli navrhovat podsystémy se známými požadavky na rozhraní. I když jeho relevance poklesla s nástupem plně IP sítí a pokročilejšího digitálního zpracování signálu integrovaného přímo do moderních zařízení, SCD představuje důležité historické řešení technických výzev fyzické vrstvy raných mobilních sítí.

## Klíčové vlastnosti

- Zesílení signálu pro kompenzaci útlumu na přenosové cestě
- Filtrování pro odstranění mimopásmového šumu a interferencí
- Útlum signálu pro prevenci přetížení přijímače
- Impedanční přizpůsobení pro optimální přenos výkonu
- Tvarování vlnového průběhu (např. tvarování pulsů) pro digitální signály
- Adaptace rozhraní mezi různými typy fyzických médií

## Definující specifikace

- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [SCD na 3GPP Explorer](https://3gpp-explorer.com/glossary/scd/)
