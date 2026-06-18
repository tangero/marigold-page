---
slug: "pcu"
url: "/mobilnisite/slovnik/pcu/"
type: "slovnik"
title: "PCU – Packet Control Unit"
date: 2025-01-01
abbr: "PCU"
fullName: "Packet Control Unit"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pcu/"
summary: "Packet Control Unit (PCU) je síťový prvek v systémech 2G (GSM/GPRS) a 3G (UMTS), který spravuje paketově orientovaný datový provoz. Řídí rádiové zdroje pro GPRS/EDGE, zajišťuje plánování přenosu paket"
---

PCU je síťový prvek v systémech 2G a 3G, který řídí rádiové zdroje pro paketová data, zajišťuje plánování přenosu paketů a tvoří rozhraní mezi řadičem základnových stanic (BSC) a SGSN.

## Popis

Packet Control Unit (PCU) je kritická funkční entita zavedená v sítích GSM pro umožnění služby General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)) a Enhanced Data rates for GSM Evolution ([EDGE](/mobilnisite/slovnik/edge/)). Je odpovědná za všechny řídicí a uživatelské funkce související s paketovými daty v rámci rádiové přístupové sítě. Fyzicky může být PCU implementována jako samostatný síťový uzel nebo může být integrována do řadiče základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) v systémech 2G, případně do řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v sítích 3G UMTS pro určité funkce. Jejím hlavním úkolem je spravovat přidělování a uvolňování paketových datových kanálů ([PDCH](/mobilnisite/slovnik/pdch/)) na rádiovém rozhraní, což jsou časové sloty vyhrazené pro přenos paketově orientovaného provozu vedle hovorového provozu s přepojováním okruhů.

Z provozního hlediska se PCU logicky nachází mezi BSC a Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v páteřní síti. Přijímá datové pakety od SGSN přes rozhraní Gb a je odpovědná za jejich segmentaci na rádiové bloky vhodné pro přenos přes rozhraní vzduch. Naopak sestavuje rádiové bloky přijaté od mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) zpět do paketů pro přeposlání k SGSN. PCU implementuje klíčové protokoly vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a řízení rádiového spoje (RLC). Provádí funkce jako plánování přenosu paketů v uplinku a downlinku, opravu chyb pomocí automatického opakovaného dotazu (ARQ) a správu dočasných toků bloků (TBF), což jsou logická spojení pro přenos dat.

Zásadním architektonickým aspektem je kontrola rozdělování rádiových zdrojů ze strany PCU. V buňce GSM je k dispozici omezený počet časových slotů. PCU, často ve spolupráci s BSC, dynamicky přiděluje časové sloty buď pro přepojování okruhů (CS) pro hovory, nebo pro přepojování paketů (PS) pro data na základě poptávky. To umožňuje efektivní sdílené využití spektra. PCU také zajišťuje přecelování a aktualizace směrovací oblasti pro mobilitu v režimu přepojování paketů. V 3G UMTS se tento koncept vyvinul; většinu funkcí řízení paketů převzal RNC, ale termín PCU se někdy používá pro označení entity plánování paketů uvnitř RNC, zejména v raných vydáních UMTS podporujících kompatibilitu s GSM EDGE Radio Access Network (GERAN).

## K čemu slouží

PCU byla vytvořena za účelem zavedení schopností přepojování paketů do původně výhradně okruhově orientované sítě GSM. Před GPRS byly datové služby GSM omezeny na pomalá datová volání s přepojováním okruhů, která na celou dobu sezení vyhradila vyhrazený rádiový kanál, což vedlo k neefektivnímu využití spektra pro trhavý datový provoz. PCU tento problém vyřešila tím, že umožnila statistické multiplexování datových paketů více uživatelů na sdílených rádiových kanálech, což dramaticky zvýšilo efektivitu využití spektra a umožnilo 'vždy zapojené' připojení.

Její vývoj byl hnán rostoucí poptávkou po mobilním přístupu k internetu na konci 90. let 20. století. PCU řešila technickou výzvu správy sdíleného, konkurenčního rádiového zdroje pro data. Poskytla potřebnou inteligenci v rádiové síti pro zvládnutí segmentace paketů, retransmisí a plánování, které v hlasově orientovaném BSC chyběly. Oddělením logiky řízení paketů (v PCU) od logiky řízení hovorů (v BSC) mohli operátoři upgradovat své sítě na podporu dat bez kompletní přestavby. PCU položila základy pro veškerý následný vývoj mobilního širokopásmového přístupu, od EDGE přes 3G a dále, tím, že stanovila principy paketového řízení rádiových zdrojů.

## Klíčové vlastnosti

- Řízení rádiových zdrojů pro paketová data: Dynamicky přiděluje a spravuje paketové datové kanály (PDCH) z fondu časových slotů GSM.
- Segmentace a opětovné sestavení paketů: Převádí pakety z páteřní sítě na rádiové bloky pro přenos přes rozhraní vzduch a naopak.
- Správa dočasných toků bloků (TBF): Vytváří, udržuje a uvolňuje logická spojení pro jednotlivé datové přenosové relace.
- Funkce vrstev MAC a RLC: Zajišťuje plánování přenosu v uplinku/downlinku, řešení kolizí a opravu chyb pomocí protokolů ARQ.
- Zpracování rozhraní: Propojuje BSC (nebo RNC) s SGSN přes rozhraní Gb pro řídicí a uživatelský provoz.
- Dynamické přidělování časových slotů: Spolupracuje s BSC na rozdělování zdrojů buňky mezi provoz s přepojováním okruhů a provoz s přepojováním paketů v reálném čase.

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [PCU na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcu/)
