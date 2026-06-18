---
slug: "dft"
url: "/mobilnisite/slovnik/dft/"
type: "slovnik"
title: "DFT – Discrete Fourier Transform"
date: 2025-01-01
abbr: "DFT"
fullName: "Discrete Fourier Transform"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dft/"
summary: "DFT (Diskrétní Fourierova transformace) je základní matematický algoritmus používaný v systémech 3GPP k převodu časových signálů na kmitočtové reprezentace. Je klíčový pro formy vln Orthogonal Frequen"
---

DFT (Diskrétní Fourierova transformace) je základní matematický algoritmus používaný v systémech 3GPP k převodu časových signálů na kmitočtové reprezentace, což je klíčové pro formy vln OFDM a SC-FDMA v LTE a 5G NR.

## Popis

Discrete Fourier Transform (DFT) je klíčová technika zpracování signálu ve fyzické vrstvě 3GPP, konkrétně pro generování a demodulaci vln [OFDM](/mobilnisite/slovnik/ofdm/) a [SC-FDMA](/mobilnisite/slovnik/sc-fdma/). Na straně vysílače transformuje DFT blok komplexních modulačních symbolů z časové oblasti do kmitočtové oblasti. V uplink SC-FDMA v LTE je tento proces implementován přes fázi DFT-prekódování před mapováním na podnosné, což snižuje poměr špičkového k průměrnému výkonu ([PAPR](/mobilnisite/slovnik/papr/)) a zlepšuje účinnost výkonového zesilovače v uživatelském zařízení (UE). V downlink OFDM pro LTE i 5G NR se na straně vysílače používá Inverzní DFT ([IDFT](/mobilnisite/slovnik/idft/)) k převodu kmitočtově namapovaných symbolů na časový OFDM symbol pro přenos přes rozhraní vzduchu.

Architektonicky je operace DFT integrována do řetězce základní pásmové zpracování jak na straně gNB/NodeB (bázové stanice), tak na straně UE. Její implementace je často optimalizována jako Rychlá Fourierova transformace ([FFT](/mobilnisite/slovnik/fft/)), výpočetně efektivní algoritmus pro výpočet DFT. Velikost DFT, často označovaná jako velikost FFT, je klíčový parametr, který určuje počet podnosných a tím i šířku pásma systému. Například v LTE standardní velikosti FFT jako 128, 256, 512, 1024 a 2048 odpovídají různým šířkám kanálu od 1,4 MHz do 20 MHz. V 5G NR je tento koncept rozšířen flexibilnější číselnou řadou, která podporuje širší škálu rozestupů podnosných a odpovídajících velikostí DFT, aby uspokojila různé případy použití od rozšířeného mobilního širokopásmového připojení až po ultra-spolehlivou komunikaci s nízkou latencí.

Role DFT je klíčová pro umožnění ortogonálního multiplexování více uživatelů a datových toků. Převodem signálů do kmitočtové oblasti může systém přesně přidělit konkrétní podnosné různým uživatelům (jako v [OFDMA](/mobilnisite/slovnik/ofdma/)), což zajišťuje ortogonalitu a minimalizuje mezinosičovou interferenci. Na straně přijímače je DFT opět aplikována pro převod přijatého časového signálu zpět do kmitočtové oblasti, což umožňuje odhad kanálu, ekvalizaci a demodulaci vysílaných symbolů. Tato transformace je nezbytná pro zvládání kmitočtově selektivního útlumu v bezdrátových kanálech, protože umožňuje ekvalizaci na každé podnosné, což výrazně zjednodušuje návrh přijímače ve srovnání s časovými ekvalizéry pro širokopásmové signály.

Dále DFT tvoří základ klíčových postupů fyzické vrstvy. Používá se při generování referenčních signálů (jako [DM-RS](/mobilnisite/slovnik/dm-rs/) a [SRS](/mobilnisite/slovnik/srs/)) pro odhad kanálu a při implementaci pokročilých víceanténních technik, jako je prekódování pro MIMO. Účinnost a přesnost implementace DFT/FFT přímo ovlivňuje metriky výkonu systému, jako je propustnost, latence a spotřeba energie. Její výpočetní nároky také ovlivňují hardwarový návrh UE a bázových stanic, což z ní činí klíčový aspekt pro implementaci v křemíku.

## K čemu slouží

DFT byla začleněna do standardů 3GPP počínaje LTE (Rel-8) za účelem řešení omezení technologie Wideband Code Division Multiple Access (WCDMA) používané v 3G UMTS. WCDMA, technologie s přímým sekvenčním rozprostřením spektra, čelila výzvám s vysokým poměrem špičkového k průměrnému výkonu (PAPR) a složitostí ekvalizace širokopásmových signálů přes kmitočtově selektivní kanály. Tyto faktory omezovaly spektrální účinnost a zvyšovaly náklady a zátěž výkonového zesilovače v mobilních zařízeních. Přijetí přístupových schémat založených na OFDM (OFDMA downlink, SC-FDMA uplink) si vyžádalo DFT jako základní matematický nástroj pro umožnění efektivní více nosičové přenosu.

Primární problém, který DFT řeší, je efektivní a ortogonální oddělení signálů v kmitočtové oblasti. Použitím DFT mohou systémy 3GPP rozdělit dostupné spektrum na mnoho úzkopásmových, ortogonálních podnosných. Tato ortogonalita zabraňuje mezisymbolové interferenci v rámci periody symbolu a umožňuje flexibilní přidělování spektra. Pro uplink bylo specifické použití DFT-prekódování v SC-FDMA motivováno potřebou nízkopaprové formy vlny k prodloužení výdrže baterie UE a snížení nákladů a linearitních požadavků výkonového zesilovače UE, což je klíčová výhoda oproti čistému OFDMA.

Historická motivace vycházela z úsilí průmyslu směrem k vyšším přenosovým rychlostem a lepší spektrální účinnosti pro 4G a další generace. DFT, prostřednictvím své FFT implementace, poskytla výpočetně realizovatelnou metodu pro zvládnutí velkých šířek pásma potřebných pro vysokorychlostní přenos dat. Její integrace umožnila LTE a následně 5G NR podporovat škálovatelné šířky pásma, pokročilé anténní technologie a robustní výkon v náročných vícecestných prostředích, čímž vytvořila matematický základ fyzické vrstvy, který definuje moderní celulární širokopásmové připojení.

## Klíčové vlastnosti

- Umožňuje generování a demodulaci vln OFDM a SC-FDMA
- Klíčová komponenta pro implementaci DFT-prekódovaného SC-FDMA v uplink LTE pro nízký PAPR
- Umožňuje flexibilní přidělování zdrojů v kmitočtové oblasti (OFDMA)
- Umožňuje efektivní převod mezi časovou a kmitočtovou oblastí pro ekvalizaci kanálu
- Podporuje škálovatelnou šířku pásma systému prostřednictvím konfigurovatelných velikostí FFT
- Základní pro generování a zpracování referenčních signálů a prekódování MIMO

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [SC-FDMA – Single Carrier – Frequency Division Multiple Access](/mobilnisite/slovnik/sc-fdma/)
- [FFT – Fast Fourier Transformation](/mobilnisite/slovnik/fft/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.884** (Rel-13) — MMSE-IRC Receiver Performance for LTE BS
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz
- **TS 45.860** (Rel-11) — Precoded EGPRS2 Downlink Study

---

📖 **Anglický originál a plná specifikace:** [DFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/dft/)
