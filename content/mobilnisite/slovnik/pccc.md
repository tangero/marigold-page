---
slug: "pccc"
url: "/mobilnisite/slovnik/pccc/"
type: "slovnik"
title: "PCCC – Parallel Concatenated Convolutional Code"
date: 2025-01-01
abbr: "PCCC"
fullName: "Parallel Concatenated Convolutional Code"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pccc/"
summary: "PCCC, běžně známé jako Turbo kódování, je výkonné schéma pro dopřednou korekci chyb (FEC) používané ve standardech bezdrátových sítí 3GPP. Využívá dva paralelní konvoluční kodéry oddělené prokladačem"
---

PCCC je schéma pro dopřednou korekci chyb, známé jako Turbo kódování, které využívá dva paralelní konvoluční kodéry a prokladač k zajištění téměř optimální spolehlivosti dat v bezdrátových systémech 3GPP.

## Popis

Parallel Concatenated Convolutional Code (PCCC), všeobecně uznávaný jako základ Turbo kódování, je sofistikované schéma kódování kanálu. Jeho architektura je postavena na paralelní konkatenaci dvou identických, jednoduchých rekurzivních systematických konvolučních ([RSC](/mobilnisite/slovnik/rsc/)) kodérů. Klíčovou inovací je prokladač (Π) umístěný před druhý kodér. Vstupní datová sekvence (blok k bitů) je přímo přivedena do prvního RSC kodéru a také do prokladače, který pseudonáhodně přeuspořádá bity. Tato promíchaná sekvence je pak vstupem pro druhý RSC kodér.

Tento proces produkuje tři výstupní sekvence: původní systematické bity (nezměněné vstupní bity) a dvě sady paritních bitů – jedna z každého kodéru. Ty jsou následně multiplexovány a vysílány. Dekodér používá iterativní zpětnovazební mechanismus, typicky s využitím algoritmu BCJR (Bahl, Cocke, Jelinek, Raviv) nebo [MAP](/mobilnisite/slovnik/map/) (Maximum A Posteriori) implementovaného ve struktuře se dvěma dekodéry typu soft-input soft-output ([SISO](/mobilnisite/slovnik/siso/)). Každý SISO dekodér odpovídá jednomu z dílčích kodérů. Vyměňují si v iterativní smyčce pravděpodobnostní informace (extrinsic informaci) o každém bitu. První dekodér využívá přijaté systematické bity a své paritní bity spolu s počátečními odhady k produkci měkkých výstupů. Tyto výstupy, po odečtení vstupní informace (aby vznikla extrinsic informace), jsou prokládány a podávány jako apriorní informace druhému dekodéru. Druhý dekodér zpracovává prokládané systematické bity a druhou sadu paritních bitů spolu s touto novou informací, aby vytvořil zpřesněné měkké výstupy. Tato extrinsic informace je pak zpětně deprokládána a vrácena prvnímu dekodéru pro další iteraci. Tato iterativní výměna umožňuje dekodérům postupně korigovat vzájemné nejistoty a po několika iteracích konvergovat k vysoce spolehlivému odhadu původních dat.

Jeho role v síti je zásadní na fyzické vrstvě rozhraní vzduchu. V 3G UMTS je to primární schéma kódování kanálu pro vysokorychlostní datové kanály (např. [DCH](/mobilnisite/slovnik/dch/), [HS-DSCH](/mobilnisite/slovnik/hs-dsch/)). V LTE se používá pro Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)), Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)) a Physical Broadcast Channel ([PBCH](/mobilnisite/slovnik/pbch/)). Díky poskytování extrémně robustní korekce chyb umožňuje PCCC systému pracovat s vyššími kódovými rychlostmi (menší redundancí) pro danou cílovou chybovost nebo udržovat spolehlivou komunikaci při mnohem nižších poměrech signálu k šumu. To přímo vede k vyšší datové propustnosti, většímu pokrytí buňky a lepšímu výkonu na jejím okraji, což je klíčové pro zajištění konzistentního uživatelského zážitku.

## K čemu slouží

PCCC byl vyvinut k vyřešení zásadní výzvy přiblížení se Shannonově limitě – teoretické maximální kapacitě šumového kanálu – s praktickou výpočetní složitostí. Před jeho vynálezem v roce 1993 byly standardem konvoluční kódy a Reed-Solomonovy kódy, ale jejich výkon zaostával za Shannonovou limitou o několik decibelů. Uzavření této mezery vyžadovalo buď nadměrně složité kódy, nebo nižší spektrální účinnost. PCCC/Turbo kódování představovalo průlom, dosahující výkonu do 0,5 dB od limitu s přijatelným iterativním dekódováním, což umožnilo realizovat vysoce účinnou digitální komunikaci přes velmi šumové kanály.

Primární problém, který řeší, je spolehlivý přenos vysokorychlostních digitálních dat přes inherentně nespolehlivý a náchylný k interferencím bezdrátový rádiový kanál. Pro 3G UMTS, které slibovalo multimediální a internetové služby, bylo tradiční kódování nedostatečné pro poskytnutí požadované kvality služby pro paketová data. PCCC umožnilo rozhraní Wideband CDMA (W-CDMA) podporovat proměnné a vysoké datové rychlosti s robustním výkonem spoje. Jeho přijetí bylo motivováno potřebou kódovacího schématu, které by se dokázalo přizpůsobit rychle se měnícím podmínkám kanálu (rychlé úniky) při zachování dobré bitové chybovosti (BER) bez nutnosti nadměrného vyzařovacího výkonu, který by způsoboval více interference.

Dále PCCC poskytlo potřebný výkonnostní rezervu pro podporu pokročilých rádiových funkcí jako Hybrid ARQ (HARQ). V HARQ se při neúspěchu prvního dekódování vysílá přírůstková redundance. Iterativní povaha Turbo dekódování dokonale synergizuje s HARQ, protože každá retransmise poskytuje dodatečné paritní bity, které lze bezproblémově začlenit do iterativního dekódovacího procesu, což vede k výkonným ziskům společného kombinování. Tato kombinace se stala základním kamenem pro vysokorychlostní paketový přístup v downlinku a uplinku (HSDPA/HSUPA) v 3G a byla přenesena jako základní technologie do LTE a 5G NR, umožňující vysokou spektrální účinnost, která definuje moderní mobilní broadband.

## Klíčové vlastnosti

- Paralelní konkatenace dvou rekurzivních systematických konvolučních (RSC) kodérů
- Použití pseudonáhodného prokladače k promíchání dat mezi kodéry
- Iterativní dekódování využívající dva dekodéry typu soft-input soft-output (SISO)
- Výměna extrinsic informace mezi dekodéry pro zpřesnění bitových odhadů
- Výkon blízký Shannonově limitě s praktickou složitostí
- Generuje systematický výstup plus dva proudy paritních bitů pro přenos

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification

---

📖 **Anglický originál a plná specifikace:** [PCCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pccc/)
