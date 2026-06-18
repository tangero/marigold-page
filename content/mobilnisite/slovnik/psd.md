---
slug: "psd"
url: "/mobilnisite/slovnik/psd/"
type: "slovnik"
title: "PSD – Power Spectral Density"
date: 2025-01-01
abbr: "PSD"
fullName: "Power Spectral Density"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/psd/"
summary: "Hustota výkonového spektra (Power Spectral Density, PSD) je měření toho, jak je výkon signálu rozložen mezi různé frekvenční složky, vyjádřené ve wattech na hertz (W/Hz). V 3GPP se jedná o klíčový par"
---

PSD je měření rozložení výkonu signálu v závislosti na frekvenci, vyjádřené ve W/Hz, používané v 3GPP ke specifikaci požadavků na vysílače/přijímače, definici emisních masek a řízení interference.

## Popis

Hustota výkonového spektra (Power Spectral Density, PSD) je základním konceptem fyzické vrstvy v bezdrátové komunikaci, který představuje rozložení výkonu signálu jako funkci frekvence. Matematicky, pro slabě stacionární náhodný proces, je to Fourierova transformace jeho autokorelační funkce. V praktických specifikacích 3GPP se PSD používá k definici spektrálních charakteristik vysílaných signálů a šumového/interferenčního prostředí pro přijímače. U vysílačů klíčové specifikace zahrnují vysílanou PSD, která definuje zamýšlené rozložení výkonu v rámci přiděleného kanálového pásma, a masky nežádoucích emisí, jako je poměr úniku do sousedního kanálu (Adjacent Channel Leakage Ratio, [ACLR](/mobilnisite/slovnik/aclr/)), což jsou v podstatě limity pro PSD mimo přidělený kanál za účelem kontroly interference do sousedních kanálů. Tyto masky jsou definovány jako maximální povolená úroveň PSD vztažená k PSD v pásmu přes specifikované odstupové frekvence. U přijímačů se PSD používá k definici referenčních úrovní citlivosti (minimální požadovaná hustota výkonového spektra přijímaného signálu pro správnou demodulaci) a charakteristik blokování (schopnost přijímat požadovaný signál za přítomnosti rušivého signálu na jiné frekvenci). Měření PSD se typicky provádí pomocí spektrálního analyzátoru nebo specializovaného testovacího zařízení, které vypočítá výkon ve specifikovaném rozlišovacím pásmu ([RBW](/mobilnisite/slovnik/rbw/)) a normalizuje jej na šířku pásma 1 Hz. V pokročilých technologiích, jako jsou LTE a NR, jsou koncepty jako hustota výkonového spektra klíčové pro funkce jako dynamické sdílení spektra, kde více technologií radiového přístupu (např. LTE a NR) nebo více operátorů sdílí stejné frekvenční pásmo, což vyžaduje přísnou kontrolu PSD pro řízení koexistence. Dále je pro uplinkové přenosy maximální výkon UE často definován jako maximální PSD za účelem kontroly interference v uplinku.

## K čemu slouží

Specifikace a kontrola hustoty výkonového spektra je motivována potřebou efektivně využívat vzácné rádiové spektrum a zajistit koexistenci více systémů a uživatelů. Bez limitů PSD by se emise vysílače mohly nadměrně rozlévat do přilehlých frekvenčních pásem a způsobovat škodlivou interferenci jiným systémům v těchto pásmech. To bylo zvláště důležité při přechodu na širší šířky pásma a složitější modulační schémata v 3G a novějších systémech. Specifikace PSD tento problém řeší tím, že poskytuje standardizovaný, měřitelný způsob, jak definovat spektrální tvar signálu a jeho nežádoucí emise. To umožňuje regulatorním orgánům stanovit masky spektrálních emisí pro licencování a výrobcům síťových zařízení a terminálů navrhovat produkty, které jsou spektrálně kompatibilní a interoperabilní. Historicky, jak se systémy vyvíjely od úzkopásmového GSM přes širokopásmový [CDMA](/mobilnisite/slovnik/cdma/) (UMTS) až po LTE a NR založené na [OFDMA](/mobilnisite/slovnik/ofdma/), metody pro specifikaci a testování PSD se staly sofistikovanějšími, aby řešily nové výzvy, jako je agregace více nosných a flexibilní číselné schéma. Kontrola PSD je také nezbytná pro funkce jako naslouchání před vysíláním (Listen-Before-Talk, [LBT](/mobilnisite/slovnik/lbt/)) v nelicencovaném spektru, kde je měření okolní PSD klíčové pro určení dostupnosti kanálu. V podstatě je PSD hlavním nástrojem pro převod abstraktního cíle 'minimalizace interference' na konkrétní, testovatelné technické požadavky, které zajišťují spolehlivý a efektivní provoz složitých, více-dodavatelských mobilních sítí.

## Klíčové vlastnosti

- Definuje rozložení výkonu signálu v závislosti na frekvenci, ve W/Hz nebo dBm/Hz.
- Používá se ke specifikaci masek nežádoucích emisí vysílače (např. ACLR, maska spektrální emise).
- Používá se k definici požadavků na referenční citlivost přijímače a charakteristiky blokování.
- Základní pro hodnocení a zajištění koexistence mezi různými systémy a operátory.
- Kritický parametr pro dynamické sdílení spektra a provoz ve sdíleném/nelicencovaném spektru.
- Měřením zjišťovaný parametr, typicky normalizovaný na šířku pásma 1 Hz pro srovnání.

## Související pojmy

- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)
- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [SC-FDMA – Single Carrier – Frequency Division Multiple Access](/mobilnisite/slovnik/sc-fdma/)

## Definující specifikace

- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 36.833** — 3GPP TR 36.833
- **TS 36.853** — 3GPP TR 36.853
- **TR 36.942** (Rel-19) — E-UTRA System Scenarios Specification
- **TS 37.808** (Rel-12) — PIM Handling for Base Stations Study
- **TR 38.805** (Rel-14) — Study on New Radio Access Technology; 60 GHz unlicensed spectrum
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TS 38.831** (Rel-16) — UE RF Requirements for FR2 Enhancements
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR
- **TR 38.877** (Rel-18) — Technical Report
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/psd/)
