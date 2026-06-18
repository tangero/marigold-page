---
slug: "ae"
url: "/mobilnisite/slovnik/ae/"
type: "slovnik"
title: "AE – Array Element"
date: 2025-01-01
abbr: "AE"
fullName: "Array Element"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ae/"
summary: "Array Element (AE) je základní vyzařovací jednotka v anténním poli, charakterizovaná svým individuálním vyzařovacím diagramem měřeným v dBi. Jedná se o klíčovou komponentu v systémech MIMO a beamformi"
---

AE (prvek anténního pole) je základní vyzařovací jednotka v anténním poli, charakterizovaná svým individuálním vyzařovacím diagramem a umožňující přesné prostorové řízení signálu pro systémy MIMO a beamforming.

## Popis

Array Element (AE) je základní, nedělitelná vyzařovací komponenta, která tvoří anténní pole v bezdrátovém komunikačním systému. V kontextu specifikací 3GPP, zejména pro [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) a pokročilé anténní systémy ([AAS](/mobilnisite/slovnik/aas/)), je AE definován svým individuálním vyzařovacím diagramem, který je typicky specifikován v jednotkách dBi (decibely vůči izotropnímu zářiči). Tento diagram popisuje, jak prvek vyzařuje výkon jako funkci směru v trojrozměrném prostoru při buzení. Každý AE je připojen k vyhrazenému řetězci rádiového transceiveru, což umožňuje nezávislé řízení fáze a amplitudy signálu. Fyzické uspořádání více AE – například v uniformním lineárním poli ([ULA](/mobilnisite/slovnik/ula/)), uniformním plošném poli ([UPA](/mobilnisite/slovnik/upa/)) nebo složitějších konformních polích – tvoří základní hardware pro prostorové zpracování signálu.

Fungování AE se řídí principy elektromagnetismu. Když je elektrický signál přiveden na prvek, přemění jej na elektromagnetické vlny šířící se prostorem. Konkrétní geometrie, velikost a materiál prvku určují jeho vnitřní charakteristiky, včetně impedanční šířky pásma, polarizace (např. lineární, duální nebo kruhová) a tvaru jeho vyzařovacího diagramu. V pasivním anténním poli jsou AE typicky pasivní zářiče, jako dipóly nebo plošné antény. V aktivním anténním systému (AAS) je každý AE integrován s aktivní komponentou (jako výkonový zesilovač nebo šumový zesilovač), čímž tvoří aktivní anténní jednotku ([AAU](/mobilnisite/slovnik/aau/)). Tato integrace umožňuje jemnější granularitu v řízení svazku a lepší energetickou účinnost.

Role AE v rámci síťové architektury je zásadní pro pokročilé techniky rádiového přístupu. V rádiové přístupové síti (RAN), zejména v gNB (pro 5G NR) a [eNB](/mobilnisite/slovnik/enb/) (pro LTE), je soubor AE řízen jednotkami pro zpracování základního pásma. Aplikací komplexních vahových vektorů (prekódovacích matic) na signály přiváděné na každý AE může systém syntetizovat složený vyzařovací diagram pro celé pole. To umožňuje klíčové technologie, jako je digitální beamforming, kde jsou úzké svazky s vysokým ziskem elektronicky nasměrovány na konkrétní uživatelské zařízení (UE), a massive MIMO, kde velký počet AE (např. 64, 128 nebo více) obsluhuje více uživatelů současně na stejném časově-frekvenčním zdroji. Výkon každého jednotlivého AE – jeho zisk, účinnost a konzistence diagramu – přímo ovlivňuje celkový zisk pole, úrovně postranních laloků a přesnost směrování svazku, což je klíčové pro dosažení vysokých přenosových rychlostí, rozšířeného pokrytí a robustního potlačení interference.

Z pohledu specifikace a testování dokumenty 3GPP, jako jsou TR 37.840, TR 38.820 a TR 38.921, definují metodiky pro charakterizaci diagramů AE. Ty zahrnují požadavky na vedené a bezdrátové ([OTA](/mobilnisite/slovnik/ota/)) testy, aby bylo zajištěno, že používané modelové diagramy AE v systémových simulacích a požadavcích na výkon (např. pro vyzářený výkon a [EIRP](/mobilnisite/slovnik/eirp/)) jsou přesné. Diagram AE je klíčovým vstupem pro výpočet metrik, jako je efektivní izotropicky vyzářený výkon (EIRP) a celkový vyzářený výkon (TRP). Porozumění AE je proto nezbytné pro RF inženýry, návrháře antén a systémové integrátory pracující na optimalizaci fyzické vrstvy sítí 4G, 5G a budoucích 6G.

## K čemu slouží

Koncept Array Element (AE) existuje, aby poskytl standardizovaný, granularní stavební blok pro návrh a analýzu pokročilých anténních systémů. Před rozšířeným přijetím MIMO a beamformingu se mobilní sítě primárně spoléhaly na sektorové antény s pevnými, širokými vyzařovacími diagramy. Tyto tradiční antény nabízely omezenou schopnost soustředit energii, což vedlo k neefektivnímu využití spektra, špatnému výkonu na okraji buňky a náchylnosti k interferenci. AE tyto limity řeší tím, že umožňuje přechod od pasivního pokrytí makrosektory k aktivnímu, na uživatele zaměřenému doručování signálu. Definováním AE a jeho vlastností vytvořil 3GPP společný rámec pro specifikaci výkonu anténních polí, což je zásadní pro zajištění interoperability mezi dodavateli základnových stanic a pro stanovení realistických cílů výkonu na systémové úrovni ve standardech.

Historicky motivace pro formalizaci konceptu AE rostla se zavedením LTE-Advanced a jeho důrazem na MIMO. Jak anténní pole rostla na složitosti – od 2x2 MIMO k 8x8 a nakonec k massive MIMO se stovkami prvků – stalo se nepraktické specifikovat výkon pouze pro celou integrovanou anténu. Rozklad systému na jeho základní AE umožňuje flexibilnější a škálovatelnější návrh systému. Umožňuje použití modulárních architektur AAS, kde lze AE kombinovat v různých konfiguracích (např. různých velikostech a geometriích pole), aby vyhovovaly různým scénářům nasazení, od hustých městských makro buněk po indoorové small buňky. Definování diagramu AE je navíc klíčové pro přesné plánování a simulaci rádiové sítě. Simulace na systémové úrovni, které předpovídají pokrytí, kapacitu a interferenci, spoléhají na přesné modely vyzařování každého AE pro výpočet realistických zisků beamformingu a prostorových charakteristik.

V konečném důsledku je AE tím, co umožňuje zisky prostorového multiplexování a beamformingu, což jsou primární mechanismy pro zvýšení spektrální účinnosti a kapacity moderních mobilních sítí. Bez dobře definovaného AE by konzistentní implementace a ověřování výkonu technologií, jako je full-dimension MIMO (FD-MIMO), multi-user MIMO (MU-MIMO) a správa svazků v milimetrových vlnách, byly výrazně náročnější. Řeší problém, jak přesně řídit elektromagnetickou energii v prostoru, a mění anténu z jednoduchého vysílacího zařízení na sofistikovaný prostorový filtr, který je klíčový pro splnění rostoucích požadavků na přenosovou rychlost a konektivitu v 5G a dalších generacích.

## Klíčové vlastnosti

- Definován individuálním vyzařovacím diagramem specifikovaným v dBi
- Základní jednotka pro konstrukci anténních polí (ULA, UPA)
- Umožňuje nezávislé řízení fáze a amplitudy na každém řetězci transceiveru
- Klíčový pro algoritmy digitálního beamformingu a směrování svazku
- Integrován s aktivními komponentami v aktivním anténním systému (AAS)
- Klíčový vstup pro výpočet systémových metrik jako EIRP a TRP

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [EIRP – Effective Isotropic Radiated Power](/mobilnisite/slovnik/eirp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study
- **TR 38.921** (Rel-19) — IMT Parameters Study for 6.4-7.1 & 10-10.5 GHz
- **TR 38.922** (Rel-19) — Study on IMT Parameters for NR in Higher Bands

---

📖 **Anglický originál a plná specifikace:** [AE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ae/)
