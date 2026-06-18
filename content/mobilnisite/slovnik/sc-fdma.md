---
slug: "sc-fdma"
url: "/mobilnisite/slovnik/sc-fdma/"
type: "slovnik"
title: "SC-FDMA – Single Carrier – Frequency Division Multiple Access"
date: 2025-01-01
abbr: "SC-FDMA"
fullName: "Single Carrier – Frequency Division Multiple Access"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sc-fdma/"
summary: "SC-FDMA je schéma rádiového přístupu používané pro uplink LTE. Je to varianta OFDMA, která snižuje poměr špičkového a průměrného výkonu (PAPR), což umožňuje efektivnější využití výkonového zesilovače"
---

SC-FDMA je schéma rádiového přístupu používané pro uplink LTE, jedná se o variantu OFDMA, která snižuje poměr špičkového a průměrného výkonu (PAPR), což umožňuje efektivnější využití výkonového zesilovače v uživatelských zařízeních.

## Popis

Single Carrier – Frequency Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (SC-FDMA) je mnohonásobný přístup, který je zásadní pro uplink Long-Term Evolution (LTE) a 5G NR. Jedná se o hybridní schéma, které kombinuje nízký poměr špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)) charakteristický pro jednodrážový přenos s odolností vůči vícecestnému šíření a flexibilním přidělováním kmitočtů, které poskytuje Orthogonal Frequency Division Multiple Access ([OFDMA](/mobilnisite/slovnik/ofdma/)). Základní princip zahrnuje krok předkódování pomocí diskrétní Fourierovy transformace ([DFT](/mobilnisite/slovnik/dft/)) aplikovaný na komplexní modulační symboly (např. [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/)) předtím, než jsou namapovány na ortogonální podnosné modulátoru OFDMA. Toto DFT rozprostření efektivně převádí vícedrážový signál na vlnový průběh podobný jednodrážovému, což výrazně snižuje jeho kubickou metriku a PAPR.

Architektura vysílače SC-FDMA zahrnuje několik klíčových stupňů. Uživatelské datové bity jsou nejprve zakódovány, prokládány a namapovány na komplexní modulační symboly. Tyto symboly jsou seskupeny do bloků, z nichž každý prochází M-bodovou DFT. Výsledné vzorky ve kmitočtové oblasti jsou poté namapovány na konkrétní sadu souvislých nebo distribuovaných podnosných přidělených danému uživateli v rámci systémové šířky pásma. Tato namapovaná data jsou zpracována velkou inverzní rychlou Fourierovou transformací ([IFFT](/mobilnisite/slovnik/ifft/)) za účelem generování časového [OFDM](/mobilnisite/slovnik/ofdm/) signálu, ke kterému je přidána cyklická předpona. Přijímač provádí inverzní operace: odstraní cyklickou předponu, aplikuje FFT pro převod do kmitočtové oblasti, extrahuje a ekvalizuje uživatelovy podnosné, aplikuje IDFT k odstranění rozprostření signálu a nakonec demoduluje a dekóduje původní symboly.

Role SC-FDMA v síti je klíčová pro návrh vysílače uživatelského zařízení (UE). Snížený PAPR umožňuje, aby výkonový zesilovač UE pracoval blíže svému saturačnímu bodu s vyšší účinností, což přímo vede k nižší spotřebě energie a prodloužení výdrže baterie. Také zlepšuje pokrytí uplinku, protože UE může vysílat s vyšším průměrným výkonem bez zkreslení od výkonového zesilovače. Zatímco OFDMA se používá pro downlink díky své vynikající spektrální účinnosti a odolnosti vůči vícecestnému útlumu, omezení výkonu na uplinku činí SC-FDMA optimální volbou. V 5G NR se pro uplink používá podobný koncept známý jako DFT-s-OFDM (Discrete Fourier Transform spread OFDM), zejména pro scénáře s omezeným pokrytím, který zachovává stejné základní výhody pro zařízení s omezeným výkonem.

## K čemu slouží

SC-FDMA byl vyvinut, aby řešil kritické omezení OFDMA při aplikaci na uplink mobilních systémů: vysoký poměr špičkového a průměrného výkonu (PAPR). OFDMA, ačkoli je výborné pro downlink z základnových stanic, vytváří signály s velkými amplitudovými změnami. Vysílání takových signálů vyžaduje výkonový zesilovač s velkým lineárním rozsahem (nebo 'odstupem'), aby se předešlo zkreslení, což je velmi neefektivní. Pro uživatelská zařízení (UE) napájená baterií by tato neefektivnost drasticky snížila výdrž baterie a omezila maximální vysílací výkon, čímž by se zmenšila oblast pokrytí uplinku.

Historický kontext představuje přechod ze 3G (UMTS/HSPA) na 4G (LTE). 3G používalo Wideband Code Division Multiple Access (WCDMA), jednodrážovou rozprostřenou spektrální techniku s dobrou účinností výkonového zesilovače, ale s omezeními ve spektrální účinnosti a flexibilitě. Pro LTE bylo OFDMA zvoleno pro downlink pro jeho vysoký výkon. Byla potřeba nová uplinková technologie, která by mohla odpovídat plánovací flexibilitě a odolnosti vůči vícecestnému šíření OFDMA a zároveň byla vhodná pro mobilní zařízení. SC-FDMA bylo technicky navržené řešení, které zdědilo ortogonální strukturu podnosných a plánovací výhody OFDMA, ale s klíčovým krokem předkódování pro vytvoření jednodrážové vlastnosti.

Primární motivací pro SC-FDMA tedy bylo umožnit vysoké datové rychlosti a pokročilé funkce LTE bez kompromisů v ceně zařízení, výdrži baterie nebo dosahu uplinku. Vyřešilo základní problém přenesení výkonu podobného OFDMA na výkonově omezený uplink, čímž se vysokorychlostní mobilní širokopásmový přístup stal prakticky proveditelným pro spotřebitelské mobilní telefony. Přímo řeší ekonomická a praktická omezení návrhu telefonů, se kterými si čisté OFDMA neporadilo.

## Klíčové vlastnosti

- Nízký poměr špičkového a průměrného výkonu (PAPR) pro efektivní provoz výkonového zesilovače
- Využívá DFT předkódování před OFDMA modulací k vytvoření jednodrážové vlastnosti
- Podporuje jak lokalizované, tak distribuované mapování podnosných pro kmitočtovou diverzitu
- Umožňuje flexibilní plánování v kmitočtové oblasti a přidělování zdrojů
- Poskytuje inherentní odolnost vůči vícecestnému útlumu díky cyklické předponě
- Tvoří základ pro uplinkový vlnový průběh DFT-s-OFDM v LTE a 5G NR

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [PAPR – Peak-to-Average Power Ratio](/mobilnisite/slovnik/papr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TR 36.902** (Rel-9) — SON Use Cases and Solutions for LTE
- **TS 38.819** (Rel-16) — Band n65 for New Radio Technical Report
- **TS 45.820** (Rel-13) — CIoT for Internet of Things

---

📖 **Anglický originál a plná specifikace:** [SC-FDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc-fdma/)
