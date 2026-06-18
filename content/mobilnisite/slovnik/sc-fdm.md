---
slug: "sc-fdm"
url: "/mobilnisite/slovnik/sc-fdm/"
type: "slovnik"
title: "SC-FDM – Single-Carrier Frequency Division Multiplexing"
date: 2025-01-01
abbr: "SC-FDM"
fullName: "Single-Carrier Frequency Division Multiplexing"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sc-fdm/"
summary: "Single-Carrier Frequency Division Multiplexing (SC-FDM) je modulační a mnohonásobně přístupové schéma používané v uplinku standardů 4G LTE a 5G NR. Je podobné OFDM, ale využívá krok DFT-spread precodi"
---

SC-FDM je modulační schéma používané v uplinku sítí 4G a 5G, které využívá DFT-spread precoding k dosažení nižšího poměru špičkového a průměrného výkonu než OFDM, čímž zlepšuje energetickou účinnost zařízení a pokrytí.

## Popis

Single-Carrier Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) (SC-FDM) je digitální modulační schéma tvořící základ pro uplinkovou mnohonásobnou přístupovou techniku v LTE (kde je nazýváno DFT-spread [OFDM](/mobilnisite/slovnik/ofdm/) nebo DFT-s-OFDM) a 5G NR. Ačkoli sdílí ortogonální strukturu subnosných s Orthogonal Frequency Division Multiplexing (OFDM), jeho klíčovým rozdílem je fáze precodingu pomocí diskrétní Fourierovy transformace ([DFT](/mobilnisite/slovnik/dft/)) aplikovaná před konvenční OFDM modulací. Tento proces transformuje vícekanálový signál na časově podobný signál jediného nosného, který má příznivé charakteristiky poměru špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)).

Architektura SC-FDM vysílače zahrnuje specifický řetězec zpracování signálu. Nejprve je proud modulačních symbolů (např. [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/)) seskupen do bloků. Každý blok prochází operací DFT. Tento krok DFT-spread rozloží energii každého původního symbolu přes všechny subnosné ve frekvenční oblasti. Výstup DFT je následně namapován na podmnožinu dostupných ortogonálních subnosných v rámci systémové šířky pásma. Po tomto mapování subnosných je signál zpracován Inverzní rychlou Fourierovou transformací ([IFFT](/mobilnisite/slovnik/ifft/)), aby byl převeden zpět do časové oblasti, stejně jako ve standardním OFDM. Nakonec je přidána cyklická předpona ([CP](/mobilnisite/slovnik/cp/)) pro potlačení intersymbolového rušení způsobeného vícecestným šířením. Přijímač provádí inverzní operace: odstranění CP, FFT, demapování subnosných a následně Inverzní DFT (IDFT) pro obnovení původních modulačních symbolů.

Princip fungování SC-FDM zásadně závisí na vlastnostech DFT precodingu. V čistém OFDM je každý subnosný modulován nezávisle, což vede k časovému signálu, který je součtem mnoha sinusovek. To může mít za následek vysoký špičkový výkon, když se konstruktivně interferují, což vede k vysokému PAPR. Vysoký PAPR nutí výkonové zesilovače (PA) pracovat s velkou rezervou od jejich saturačního bodu, aby se předešlo zkreslení, což je velmi neúčinné. DFT precoding v SC-FDM vytváří korelaci mezi subnosnými. Tato korelace formuje časový výstup tak, aby připomínal signál jediného nosného, který má konstantnější obálku a tedy nižší PAPR. Nižší PAPR umožňuje PA v UE pracovat blíže saturaci s vyšší účinností, což se promítá do nižší spotřeby energie a/nebo vyššího vysílacího výkonu při stejné zátěži baterie.

Role SC-FDM v síti je klíčová pro výkon uplinku, zejména z pohledu nákladů a pokrytí. Uživatelská zařízení (UE), jako jsou smartphony, jsou zařízení s omezeným výkonem a méně sofistikovanými, cenově výhodnými výkonovými zesilovači. Nízký PAPR SC-FDM je klíčovým předpokladem pro praktický návrh uplinku v širokopásmových celulárních systémech. Umožňuje UE vysílat s vyšším průměrným výkonem bez překročení limitů linearity, čímž rozšiřuje dosah uplinkového pokrytí a datové rychlosti na okraji buňky. V 5G NR je SC-FDM (označované jako CP-OFDM s DFT-s-OFDM precodingem) podporováno jako volitelná uplinková vlna, což poskytuje flexibilitu. Pro vysokofrekvenční pásma nebo pro scénáře s omezeným pokrytím činí jeho výhody v energetické účinnosti tuto vlnu preferovanou volbou, zajišťující spolehlivé uplinkové připojení, které je zásadní pro symetrické služby a Internet věcí (IoT).

## K čemu slouží

SC-FDM bylo vyvinuto k řešení kritického problému v návrhu LTE uplinku: vysokého poměru špičkového a průměrného výkonu (PAPR), který je vlastní standardní OFDM modulaci. Vysoký PAPR je škodlivý pro uživatelská zařízení napájená baterií. Nutí výkonový zesilovač (PA) zařízení pracovat neúčinně ve své lineární oblasti, aby se předešlo zkreslení signálu, což plýtvá výdrží baterie a snižuje efektivní vysílací výkon. To omezuje uplinkové pokrytí, datové rychlosti a výdrž baterie zařízení. Účelem SC-FDM je poskytnout mnohonásobně přístupové schéma, které zachovává výhody odolnosti vůči vícecestnému šíření a spektrální účinnosti OFDM, zatímco dramaticky snižuje PAPR pro uplinkový vysílač.

Historický kontext a motivace jsou přímo spojeny s volbou OFDM pro LTE downlink. OFDM bylo zvoleno pro svou vynikající výkonnost v kanálech s frekvenčně selektivním útlumem a jednoduchost ekvalizace. Použití stejné vlny pro uplink však bylo shledáno jako nepraktické kvůli výše popsaným omezením PA v UE. Předchozí systémy jako UMTS používaly Wideband CDMA (WCDMA), které má spojitou fázi a dobrý PAPR, ale jiná omezení ve spektrální účinnosti a složitosti ekvalizace pro široká pásma. SC-FDM bylo vytvořeno jako inovativní kompromis, spojující výhody jediného nosného s flexibilní alokací zdrojů OFDMA.

SC-FDM konkrétně řeší omezení jak čistých systémů s jediným nosným, tak čistého OFDM. Překonává vysokou složitost ekvalizace širokopásmových systémů s jediným nosným při silném vícecestném šíření využitím jednoduchosti ekvalizace ve frekvenční oblasti struktury OFDM po FFT v přijímači. Současně překonává vysoký PAPR OFDM pomocí DFT precodingu. Toto inženýrské řešení bylo motivováno potřebou dosáhnout vysokých uplinkových datových rychlostí a kapacity v LTE, aniž by se návrh UE stal nepřiměřeně drahým nebo energeticky náročným. Jeho vytvoření bylo zásadní pro uskutečnění výkonných, pro spotřebitele přívětivých zařízení 4G a i nadále slouží stejnému účelu v 5G NR, zejména pro případy použití kritické na pokrytí a omezené výkonem.

## Klíčové vlastnosti

- DFT precoding vytváří časový signál podobný signálu jediného nosného
- Významně nižší poměr špičkového a průměrného výkonu (PAPR) než u OFDM
- Umožňuje účinný provoz výkonového zesilovače v uživatelském zařízení (UE)
- Zachovává ortogonální strukturu subnosných a flexibilní alokaci zdrojů (DFT-s-OFDMA)
- Pro jednoduchost využívá ekvalizaci ve frekvenční oblasti na straně přijímače
- Podporováno jako primární/uplinková vlna v LTE a jako volitelná vlna v 5G NR

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [PAPR – Peak-to-Average Power Ratio](/mobilnisite/slovnik/papr/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)

## Definující specifikace

- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SC-FDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc-fdm/)
