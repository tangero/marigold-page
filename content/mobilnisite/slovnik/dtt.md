---
slug: "dtt"
url: "/mobilnisite/slovnik/dtt/"
type: "slovnik"
title: "DTT – Digital Terrestrial Television"
date: 2025-01-01
abbr: "DTT"
fullName: "Digital Terrestrial Television"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dtt/"
summary: "Digital Terrestrial Television (DTT, digitální pozemní televize) označuje vysílání digitálních televizních signálů prostřednictvím pozemních rádiových vln, na rozdíl od satelitního nebo kabelového pře"
---

DTT je vysílání digitálních televizních signálů prostřednictvím pozemních rádiových vln, což je v kontextu 3GPP relevantní pro studie o koexistenci a sdílení s mobilními sítěmi v pásmech jako UHF.

## Popis

Digital Terrestrial Television (DTT) je standard vysílací technologie pro doručování digitálního televizního obsahu k domácím přijímačům (televizorům) pomocí pozemních vysílačů. Zatímco samotný DTT je standardizován orgány jako [ITU-R](/mobilnisite/slovnik/itu-r/), [DVB](/mobilnisite/slovnik/dvb/) a [ATSC](/mobilnisite/slovnik/atsc/), 3GPP DTT rozsáhle studovalo v kontextu koexistence spektra a možné technické konvergence s mobilními širokopásmovými službami. Klíčové specifikace 3GPP, jako je TS 36.104 ([E-UTRA](/mobilnisite/slovnik/e-utra/) [BS](/mobilnisite/slovnik/bs/) radio transmission) a TS 37.104 (Multi-RAT base station requirements), zahrnují emisní masky a požadavky na koexistenci pro základnové stanice LTE/5G NR pracující v sousedství kanálů DTT vysílání, zejména v pásmech 700 MHz a 600 MHz.

Z architektonické perspektivy se sítě DTT zásadně liší od buněčných sítí. Používají vysílací architekturu s vysokým výkonem a vysokými věžemi, kde jediný vysílač (nebo síť synchronizovaných vysílačů v Single Frequency Network - SFN) pokrývá rozsáhlou geografickou oblast. Signál je vysílán jednosměrně všem přijímačům v dosahu. To je v kontrastu s buněčným modelem nízkovýkonového, malobuněčného, obousměrného a uživatelsky specifického přenosu. Primární standardy DTT odkazované ve studiích 3GPP jsou [DVB-T/T2](/mobilnisite/slovnik/dvb-t-t2/) (Digital Video Broadcasting - Terrestrial) a v některých regionech [ISDB-T](/mobilnisite/slovnik/isdb-t/) nebo ATSC.

Jak DTT funguje: zahrnuje kódování audia, videa a dat do [MPEG](/mobilnisite/slovnik/mpeg/) Transport Stream, který je následně modulován pomocí Orthogonal Frequency Division Multiplexing (OFDM) – techniky používané také LTE a 5G NR, ale s odlišnými parametry. OFDM signál je vysílán přes určený UHF kanál (např. široký 6, 7 nebo 8 MHz). Přijímače v pokryté oblasti naladí kanál, demodulují OFDM signál a dekódují transportní stream, aby zobrazily vybraný program. Klíčovými technickými parametry důležitými pro koexistenci jsou vysoký výstupní výkon vysílače (až desítky kW) a citlivost přijímače na rušení z blízkých mobilních základnových stanic, které pracují s mnohem nižším výkonem, ale na sousedních frekvencích.

Role 3GPP v souvislosti s DTT není definovat vysílací standard, ale zajistit, aby jeho mobilní standardy mohly harmonicky fungovat ve sdíleném nebo sousedním spektru. To zahrnuje důkladné studie zdokumentované v Technických zprávách (TR) jako 37.900, které vyhodnocují scénáře rušení. Práce zahrnuje definování požadavků na mobilní základnové stanice, aby omezily své mimopásmové emise (parazitní a únik sousedního kanálu) za účelem ochrany citlivých přijímačů DTT. Naopak studie také zkoumají dopad vysokovýkonných DTT přenosů na blízké buněčné přijímače. Tato analýza koexistence je klíčová pro regulátory plánující přerozdělení spektra (tzv. spectrum re-farming), jako je digitální dividenda (převedení pásma UHF z vysílání na mobilní služby), což umožňuje zavedení služeb jako LTE/5G v pásmu 28 (700 MHz) a n71/n28 (600/700 MHz) bez degradace stávajících televizních služeb.

## K čemu slouží

Zařazení studií DTT do specifikací 3GPP je motivováno globálním jevem přerozdělování spektra a potřebou koexistence mezi různými rádiovými službami. Historicky bylo pásmo UHF (470-862 MHz) převážně využíváno pro analogové a později digitální televizní vysílání. Toto spektrum je pro mobilní širokopásmové služby velmi cenné díky svým vynikajícím šířicím charakteristikám (dobré pokrytí a průnik budovami). Jak poptávka po mobilních datech explodovala, regulátoři po celém světě usilovali o převedení částí pásma UHF pro technologie IMT jako LTE a 5G – proces známý jako „digitální dividenda“.

Toto převedení vytvořilo přímý technický problém: jak nasadit vysokohustotní, nízkovýkonové mobilní sítě na frekvencích sousedících s vysokovýkonnými, rozlehlými vysílacími věžemi, aniž by došlo ke škodlivému rušení jedné či druhé služby. Původní přístupy před detailními studiemi koexistence byly konzervativní ochranná pásma, která plýtvala spektrem, nebo netestovaná nasazení riskující narušení služeb. Práce 3GPP na koexistenci s DTT byla motivována potřebou poskytnout solidní technický základ pro spektrální politiku. Cílem bylo definovat přesné technické podmínky (např. požadované separační vzdálenosti, emisní limity základnových stanic), za kterých je koexistence možná, a tím umožnit efektivní využití spektra.

Dále probíhal průzkum konvergence, jako je FeMBMS (Further evolved Multimedia Broadcast Multicast Service) v LTE a 5G Broadcast, které by teoreticky mohly nabízet služby podobné vysílání pomocí buněčné infrastruktury. Pochopení výkonu a požadavků stávající technologie DTT je pro vyhodnocení takových scénářů konvergence zásadní. DTT tedy v kontextu 3GPP existuje, aby řešilo kritický reálný problém mírumilovného a efektivního sdílení spektra mezi dvěma zcela odlišnými architekturami rádiových služeb, což usnadňuje zavádění mobilního širokopásmového připojení v hodnotném nízkofrekvenčním pásmu.

## Klíčové vlastnosti

- Vysokovýkonná, rozlehlá vysílací architektura využívající OFDM modulaci
- Provoz v pásmech UHF (např. 470-698 MHz), podléhajících přerozdělení digitální dividendy
- Používá standardizované systémy jako DVB-T/T2, ISDB-T nebo ATSC
- Schopnost Single Frequency Network (SFN) pro zlepšenou spektrální účinnost
- Náchylnost k rušení z emisí mobilních základnových stanic v sousedním pásmu
- Primární zaměření v 3GPP je na analýzu koexistence a definování ochranných kritérií

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TR 36.792** (Rel-18) — Technical Report
- **TS 36.895** (Rel-13) — 700 SDL Band for LTE Carrier Aggregation
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [DTT na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtt/)
