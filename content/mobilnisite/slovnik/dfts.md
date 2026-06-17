---
slug: "dfts"
url: "/mobilnisite/slovnik/dfts/"
type: "slovnik"
title: "DFTS – Discrete Fourier Transform Spread Orthogonal Frequency Division Multiplexing"
date: 2025-01-01
abbr: "DFTS"
fullName: "Discrete Fourier Transform Spread Orthogonal Frequency Division Multiplexing"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dfts/"
summary: "DFTS je modulační a mnohonásobný přístupový systém používaný pro uplink v LTE, který kombinuje DFT rozprostření s OFDM. Vytváří jednokanálový průběh s nízkým poměrem špičkového a průměrného výkonu (PA"
---

DFTS je modulační schéma pro uplink v LTE, které kombinuje DFT rozprostření s OFDM za účelem vytvoření jednokanálového průběhu s nízkým PAPR, což umožňuje efektivní provoz výkonového zesilovače v uživatelském zařízení.

## Popis

DFTS-OFDM, často označovaný jako Single-Carrier [FDMA](/mobilnisite/slovnik/fdma/) (SC-FDMA) v kontextu LTE, je základní přenosové schéma fyzické vrstvy pro uplink v LTE. Architektura začíná generováním komplexních modulačních symbolů (QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/)) ve frekvenční oblasti. Tyto symboly jsou následně mapovány na sadu souvislých nebo nesouvislých subnosičů přidělených konkrétnímu uživateli. Klíčovou součástí je M-bodový [DFT](/mobilnisite/slovnik/dft/) (Diskrétní Fourierova transformace) prekodér, který rozprostírá energii každého modulačního symbolu přes všechny přidělené subnosiče, čímž transformuje vícekanálový [OFDM](/mobilnisite/slovnik/ofdm/) signál na průběh podobný jednokanálovému.

Technický provoz zahrnuje několik fází: Nejprve vysílač provede M-bodovou DFT na blocích M modulačních symbolů, kde M odpovídá počtu přidělených subnosičů. Výsledné vzorky ve frekvenční oblasti jsou pak mapovány na vstupy N-bodové [IFFT](/mobilnisite/slovnik/ifft/) (Inverzní rychlá Fourierova transformace), kde N je celková šířka pásma systému v subnosičích. Pro nepřidělené subnosiče jsou vloženy nulové symboly. Po transformaci IFFT je přidána cyklická předpona pro zmírnění vícecestného rušení a časový signál je vysílán. Tento proces vytváří signál s vlastnostmi jednoho nosiče i přes použití OFDM infrastruktury.

Přijímač provádí inverzní operace: odstranění cyklické předpony, N-bodovou [FFT](/mobilnisite/slovnik/fft/) pro návrat do frekvenční oblasti, extrakci přidělených subnosičů a nakonec M-bodovou [IDFT](/mobilnisite/slovnik/idft/) pro obnovení původních modulačních symbolů. Jednokanálová charakteristika je zachována prostřednictvím DFT rozprostření, které zajišťuje, že všechny subnosiče nesou lineární kombinaci všech původních symbolů spíše než nezávislou modulaci na každém subnosiči. Tato architektura umožňuje DFTS-OFDM využívat odolnost OFDM vůči frekvenčně selektivnímu útlumu při zachování výhod nízkého PAPR přenosu s jedním nosičem.

V síťové architektuře LTE funguje DFTS-OFDM v rámci fyzického sdíleného kanálu uplinku (PUSCH) pro přenos dat a fyzického řídicího kanálu uplinku (PUCCH) pro signalizaci řízení. Schéma podporuje jak lokalizovaný přenos (souvislé subnosiče), tak distribuovaný přenos (nesouvislé subnosiče s přeskakováním frekvencí) pro zajištění frekvenční diverzity. Granularita přidělování zdrojů je jeden zdrojový blok (12 subnosičů × 0,5 ms slot) a jednomu uživateli může být přiděleno více zdrojových bloků pro podporu různých datových rychlostí. Integrace technologie s plánovacími mechanismy a přizpůsobováním spojení v LTE umožňuje dynamické přidělování zdrojů na základě stavu kanálu a požadavků na kvalitu služeb.

## K čemu slouží

DFTS-OFDM byl vyvinut speciálně pro uplink v LTE, aby řešil kritickou výzvu účinnosti výkonového zesilovače v uživatelském zařízení. Tradiční OFDM používaný pro downlink vykazuje vysoký poměr špičkového a průměrného výkonu (PAPR), což vyžaduje výkonové zesilovače s velkou rezervou, aby se předešlo nelineárnímu zkreslení. To vede k nízké účinnosti výkonu, což přímo ovlivňuje výdrž baterie v mobilních zařízeních. Vytvořením průběhu podobného jednokanálovému prostřednictvím DFT rozprostření dosahuje DFTS-OFDM výrazně nižšího PAPR (přibližně o 2–3 dB nižšího než OFDM), což umožňuje efektivnější provoz výkonového zesilovače a prodlouženou výdrž baterie.

Historický kontext vývoje DFTS-OFDM vznikl z omezení předchozích technologií 3GPP. WCDMA používané v UMTS mělo rozumné charakteristiky PAPR, ale trpělo nízkou spektrální účinností a omezenou podporou plánování ve frekvenční oblasti. Komunita 3GPP hledala technologii, která by mohla poskytnout výhody OFDM v prostředích s vícecestným šířením a plánování ve frekvenční oblasti, a zároveň překonat nevýhodu vysokého PAPR u OFDM pro přenos uplink. DFTS-OFDM představoval elegantní řešení, které zachovalo kompatibilitu se strukturami OFDM přijímačů, zatímco transformovalo charakteristiky vysílaného signálu.

Kromě energetické účinnosti řeší DFTS-OFDM omezení pokrytí v celulárních sítích. Zlepšená účinnost výkonového zesilovače se převádí na vyšší efektivní vysílací výkon při stejné spotřebě baterie, čímž se rozšiřuje pokrytí uplinku, zejména na okrajích buňky. To bylo obzvláště důležité pro cíl LTE poskytovat konzistentní vysokorychlostní pokrytí. Technologie také zjednodušila návrh přijímače na základnové stanici, protože jednokanálová vlastnost snížila citlivost na nelinearity zesilovače v uživatelském zařízení, což vedlo k předvídatelnější kvalitě signálu na přijímači.

## Klíčové vlastnosti

- Nízký poměr špičkového a průměrného výkonu (PAPR) pro účinnost výkonového zesilovače
- Vlastnosti jednokanálového průběhu s výhodami vícekanálového přenosu
- Schopnost ekvalizace ve frekvenční oblasti na přijímači
- Podpora lokalizovaného i distribuovaného přidělování zdrojů
- Kompatibilita s OFDM infrastrukturou a strukturami přijímačů
- Škálovatelná podpora šířky pásma od 1,4 MHz do 20 MHz

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [DFTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dfts/)
