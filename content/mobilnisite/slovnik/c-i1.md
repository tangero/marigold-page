---
slug: "c-i1"
url: "/mobilnisite/slovnik/c-i1/"
type: "slovnik"
title: "C/I1 – Carrier to First (Strongest) Interferer Ratio"
date: 2025-01-01
abbr: "C/I1"
fullName: "Carrier to First (Strongest) Interferer Ratio"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/c-i1/"
summary: "C/I1 je klíčová metrika kvality rádiového spoje představující poměr výkonu požadovaného signálu nosné k výkonu nejsilnějšího rušivého signálu. Je zásadní pro posouzení výkonu omezeného rušením, zejmén"
---

C/I1 je poměr výkonu požadovaného signálu nosné k výkonu nejsilnějšího rušivého signálu, používaný v sítích GSM/EDGE pro vyhodnocení rušení a optimalizaci adaptace spojení, řízení výkonu a přechodů mezi buňkami.

## Popis

Carrier to First (Strongest) Interferer Ratio (C/I1) je základní měření na fyzické vrstvě systémů GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Kvantifikuje kvalitu rádiového spoje porovnáním úrovně výkonu požadovaného signálu nosné (C) s úrovní výkonu jediného nejsilnějšího rušivého signálu na stejném nebo sousedním kanále (I1) přítomného na přijímači. Na rozdíl od jednoduchého poměru Carrier-to-Interference ([C/I](/mobilnisite/slovnik/c-i/)), který může uvažovat souhrnné rušení, C/I1 konkrétně izoluje dominantní rušič, což poskytuje přesnější charakterizaci rušivého prostředí, když je jediný zdroj hlavním omezujícím faktorem výkonu. Tuto metriku měří mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) na downlinku a základnová stanice ([BTS](/mobilnisite/slovnik/bts/)) na uplinku, typicky je odvozena z měření síly signálu na kanálu pro přenos uživatelských dat a na sousedních buňkách.

Hodnota C/I1 je kritickým vstupem pro několik algoritmů správy rádiových prostředí (RRM) definovaných ve specifikacích 3GPP. Přímo ovlivňuje výběr modulačního a kódového schématu ([MCS](/mobilnisite/slovnik/mcs/)) prostřednictvím procesů adaptace spojení. Vysoká hodnota C/I1 indikuje čistý signál, což umožňuje použití modulací vyššího řádu, jako je [8-PSK](/mobilnisite/slovnik/8-psk/) pro EDGE, nebo méně robustního kódování pro maximalizaci datového propustnosti. Naopak nízká hodnota C/I1 spouští přechod na robustnější schémata s nižší propustností, jako je [GMSK](/mobilnisite/slovnik/gmsk/). Dále se měření C/I1 používají v algoritmech řízení výkonu k minimalizaci vysílacího výkonu při zachování kvality spoje, čímž se snižuje celkové rušení v síti a zlepšuje se výdrž baterie. Přispívají také k rozhodování o přechodech mezi buňkami, což síti pomáše nasměrovat spojení k buňce s příznivějším rušivým prostředím.

Z architektonického hlediska je odhad C/I1 integrován do měřicích procedur vrstvy 1. Přijímač provádí odhad kanálu a měření síly signálu na přiděleném časovém úseku pro přenos dat. Současně monitoruje majákové frekvence sousedních buněk, jak je definováno v seznamu BA (BCCH Allocation), aby identifikoval potenciální rušiče. Nejsilnější rušivý signál, často z buňky používající stejný kanál v jiném sektoru, je identifikován a změřen jeho výkon. Poměr je následně vypočítán, často časově filtrován, a nahlášen vyšším vrstvám (MS k BTS prostřednictvím Measurement Reports a BTS k BSC). Řadič základnových stanic (BSC) používá tyto hlášení spolu s dalšími metrikami k provádění funkcí RRM. V kontextu vývoje GSM/EDGE zůstává C/I1 základní metrikou pro srovnávací testy výkonu, optimalizaci sítě a funkce jako Dynamické přidělování frekvencí a kanálů (DFCA), které spoléhají na přesné vyhodnocení rušení v reálném čase, aby přidělily volání nebo datové relaci co nejčistší možný kanál.

## K čemu slouží

Metrika C/I1 byla vytvořena, aby řešila základní výzvu řízení rušení v celulárních sítích, zejména v hustě nasazených architekturách GSM s opakovaným využíváním frekvencí. Rané celulární systémy byly primárně omezeny šumem, ale jak sítě rostly a vzory opakovaného využití frekvencí se zpřísňovaly pro zvýšení kapacity, rušení se stalo dominantním faktorem omezujícím kvalitu signálu a kapacitu systému. Jednoduchý indikátor síly přijímaného signálu (RSSI) byl nedostatečný k rozlišení mezi silným požadovaným signálem v hlučném prostředí a středně silným signálem přehlušeným silným rušičem na stejné frekvenci. Poměr C/I1 byl zaveden, aby poskytl přímé a jednoznačné měření dopadu tohoto dominantního rušiče.

Jeho účelem je umožnit inteligentní správu rádiových prostředí s ohledem na rušení. Před existencí takto přesných metrik sítě spoléhaly na primitivnější měření, což vedlo k neoptimálním rozhodnutím. Například přechod mezi buňkami mohl být spuštěn pouze na základě síly signálu sousední buňky, aniž by se vědělo, zda kanál této buňky netrpí ještě horším rušením. Kvantifikací poměru k nejsilnějšímu rušiči umožňuje C/I1 síti činit kvalitnější rozhodnutí: volit modulační schémata odpovídající skutečné kapacitě kanálu omezené rušením, aplikovat přesně tolik řízení výkonu, kolik je potřeba k překonání konkrétního rušiče, a vybírat cílové buňky pro přechod, které nabízejí nejen silnější signál, ale i lepší poměr signálu k rušení. To přímo vede k vyšší spektrální účinnosti sítě, lepším datovým rychlostem pro koncové uživatele a spolehlivější kvalitě hovorů.

Specifikace C/I1 v dokumentech 3GPP Rel-8, jako jsou 45.913 a 45.914, formalizovala tuto metriku pro požadavky na výkon a testování, což zajistilo konzistentní implementaci napříč síťovými zařízeními a terminály. Poskytla standardizovaný způsob specifikace minimálních úrovní výkonu přijímačů ve scénářích omezených rušením, což vedlo ke zlepšením základnového zpracování a citlivosti přijímačů. To bylo obzvláště kritické pro vývoj EDGE a EDGE Evolution, kde dosažení vyšších datových rychlostí záviselo na schopnosti sítě přesně detekovat a zmírňovat rušení, což umožňovalo použití spektrálně účinnějších, ale méně robustních modulačních schémat pouze tehdy, když to podmínky C/I1 dovolily.

## Klíčové vlastnosti

- Kvantifikuje dopad jediného nejsilnějšího rušivého signálu na rádiový spoj
- Klíčový vstup pro výběr modulačního a kódového schématu (MCS) při adaptaci spojení
- Řídí algoritmy řízení výkonu k minimalizaci vysílacího výkonu a rušení v síti
- Podkládá rozhodnutí o přechodech mezi buňkami pro výběr buněk s lepšími podmínkami z hlediska rušení
- Měřeno jak mobilními stanicemi (downlink), tak základnovými stanicemi (uplink)
- Základní metrika pro specifikaci výkonu přijímačů v konformních testech 3GPP

## Související pojmy

- [C/I – Carrier-to-Interference Power Ratio](/mobilnisite/slovnik/c-i/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [C/I1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-i1/)
