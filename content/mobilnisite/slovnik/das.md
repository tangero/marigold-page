---
slug: "das"
url: "/mobilnisite/slovnik/das/"
type: "slovnik"
title: "DAS – Downlink level A modulation and coding scheme"
date: 2017-01-01
abbr: "DAS"
fullName: "Downlink level A modulation and coding scheme"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/das/"
summary: "DAS je specifické modulační a kódovací schéma (MCS) definované pro downlink přenosy ve standardech 3GPP, primárně pro sítě GSM/EDGE. Představuje konkrétní kombinaci typu modulace a kódové rychlosti na"
---

DAS je specifický modulační a kódovací schéma pro downlink definovaný ve standardech 3GPP, primárně pro sítě GSM/EDGE, který optimalizuje spektrální účinnost a spolehlivost za určitých podmínek kanálu.

## Popis

Modulační a kódovací schéma úrovně A pro downlink (DAS) je technická specifikace v rámci fyzické vrstvy 3GPP, podrobně popsaná ve specifikacích jako 36.855, 45.860 a 45.871. Definuje přesný provozní bod v tabulce modulačních a kódovacích schémat ([MCS](/mobilnisite/slovnik/mcs/)) používané pro downlink přenosy dat. MCS je klíčový parametr, který určuje typ modulace (např. QPSK, 16-QAM, 64-QAM) a rychlost kódování pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)) aplikovanou na transportní blok před jeho mapováním na fyzické zdroje pro přenos. Výběr MCS, jako je DAS, je základní součástí procesu adaptace spoje, při kterém síť dynamicky upravuje přenosové parametry na základě odhadů kvality kanálu v reálném čase, jako je poměr signálu k šumu a interferenci (SINR) hlášený uživatelským terminálem (UE).

Z architektonického hlediska je DAS implementováno ve zpracovatelském řetězci fyzické vrstvy základnové stanice (eNodeB v LTE, [BTS](/mobilnisite/slovnik/bts/) v GSM). Když plánovač rozhodne o přenosu dat pro konkrétní UE, konzultuje hlášení indikátoru kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) od tohoto UE. Toto hlášení se mapuje na doporučený index MCS z předdefinované tabulky. DAS odpovídá jednomu konkrétnímu indexu v této tabulce. Zvolené MCS určuje, jak jsou data z vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) zpracována: nejprve je připojen cyklický redundantní součet ([CRC](/mobilnisite/slovnik/crc/)); poté je blok segmentován, kanálově zakódován (např. pomocí Turbo kódů nebo konvolučních kódů se specifikovanou rychlostí) a provede se přizpůsobení rychlosti. Nakonec jsou zakódované bity modulovány do komplexních symbolů podle specifikované konstelace (např. 16-QAM pro DAS, v závislosti na přesné definici).

Úloha DAS v síti spočívá v poskytnutí garantované, standardizované úrovně výkonu. Definováním konkrétních úrovní MCS zajišťuje 3GPP, že všechny kompatibilní UE interpretují fyzický downlink sdílený kanál ([PDSCH](/mobilnisite/slovnik/pdsch/)) nebo ekvivalentní správně. Výkon DAS je charakterizován jeho spektrální účinností (bity za sekundu na hertz) a robustností, která je funkcí řádu modulace a kódové rychlosti. Modulace vyššího řádu (jako 64-QAM) přenáší více bitů na symbol, což nabízí vyšší špičkové datové rychlosti, ale vyžaduje čistší kanál. Nižší kódová rychlost poskytuje větší redundanci a lepší korekci chyb za cenu snížené informační propustnosti. DAS představuje pečlivě zvolený kompromis mezi těmito dvěma faktory pro cílový provozní bod.

Během provozu není použití DAS statické. Je součástí adaptivního systému. Pokud jsou podmínky kanálu špatné, síť může zvolit robustnější MCS s nižším řádem modulace a/nebo nižší kódovou rychlostí než DAS. Naopak za výborných podmínek by bylo zvoleno MCS vyššího řádu pro maximalizaci propustnosti. Definice DAS a dalších úrovní MCS umožňuje jemně odstupňované řízení této adaptace. Konkrétní mapování bitů, kódová rychlost a výsledná velikost transportního bloku pro DAS jsou vyčerpávajícím způsobem tabelovány ve specifikacích 3GPP, aby se odstranily nejasnosti při implementaci a testování, a tvoří tak základ spolehlivé digitální bezdrátové komunikace.

## K čemu slouží

Účelem definování specifických modulačních a kódovacích schémat, jako je DAS, ve standardech 3GPP je vytvoření společného jazyka a provozního rámce pro adaptaci spoje ve všech síťových zařízeních a uživatelských terminálech. Bez takových standardizovaných definic by každý výrobce mohl implementovat vlastní tabulky [MCS](/mobilnisite/slovnik/mcs/), což by vedlo ke katastrofálním selháním interoperability, kdy by základnová stanice jednoho výrobce vysílala data ve formátu, který terminál od jiného výrobce nedokáže dekódovat. Standardizace zajišťuje, že když síť instruuje UE, aby přijímalo data pomocí 'DAS', obě entity mají totožné chápání modulační konstelace a procesu kanálového kódování, který má být použit.

Historicky, jak se buněčná technologie vyvíjela od základních hlasových služeb (GSM) k paketovým datům (GPRS, EDGE), potřeba efektivního a adaptivního přenosu dat se stala prvořadou. Rané systémy používaly pevná modulační schémata. Zavedení úrovní MCS, včetně kategorií jako DAS, bylo motivováno potřebou maximalizovat spektrální účinnost – vzácný a cenný zdroj – dynamickým přizpůsobováním přenosové techniky rychle se měnícímu rádiovému kanálu. Tím se řeší základní omezení přístupu 'jedna velikost pro všechny', který by buď plýtval kapacitou za dobrých podmínek, nebo trpěl vysokou chybovostí za špatných podmínek.

Navíc přesná definice úrovní MCS, jako je DAS, umožňuje přesné plánování systému, simulace a benchmarkování výkonu. Inženýři mohou modelovat pokrytí a kapacitu sítě díky znalosti přesného prahu SINR potřebného pro spolehlivý provoz s použitím DAS. Také usnadňuje konzistentní testování a certifikaci zařízení. Řešením problémů interoperability, adaptivní účinnosti a předvídatelného výkonu tvoří standardizované definice MCS nezbytný, i když často neviditelný, základ pro vysokorychlostní datové služby, které uživatelé dnes zažívají.

## Klíčové vlastnosti

- Standardizovaná kombinace typu modulace a kódové rychlosti
- Definováno pro downlink (síť-terminál) přenosy
- Umožňuje dynamickou adaptaci spoje na základě kvality kanálu
- Zajišťuje interoperabilitu mezi více výrobci pro dekódování fyzické vrstvy
- Poskytuje známý kompromis mezi datovou rychlostí a robustností přenosu
- Specifikuje přesné velikosti transportních bloků a mapování zdrojů

## Související pojmy

- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 45.860** (Rel-11) — Precoded EGPRS2 Downlink Study
- **TS 45.871** (Rel-14) — MIMO for GSM/EDGE Downlink Study

---

📖 **Anglický originál a plná specifikace:** [DAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/das/)
