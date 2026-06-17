---
slug: "awgn"
url: "/mobilnisite/slovnik/awgn/"
type: "slovnik"
title: "AWGN – Additive White Gaussian Noise"
date: 2025-01-01
abbr: "AWGN"
fullName: "Additive White Gaussian Noise"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/awgn/"
summary: "AWGN je základní statistický model šumu používaný pro charakterizaci náhodného, aditivního rušení v komunikačních kanálech. Je klíčový pro simulaci a analýzu výkonu bezdrátových systémů a poskytuje re"
---

AWGN je základní statistický model šumu používaný pro charakterizaci náhodného, aditivního rušení v komunikačních kanálech při simulaci a analýze výkonu bezdrátových systémů.

## Popis

Aditivní bílý Gaussovský šum (Additive White Gaussian Noise, AWGN) je základní matematický model šumu v teorii komunikace a zpracování signálu. Je charakterizován třemi klíčovými vlastnostmi: „Aditivní“ znamená, že šumový signál se lineárně sčítá s požadovaným signálem. „Bílý“ značí, že šum má konstantní spektrální výkonovou hustotu ve všech frekvencích v rámci šířky pásma kanálu, což implikuje, že jeho vzorky jsou v čase nekorelované. „Gaussovský“ určuje, že okamžitá amplituda šumu se řídí Gaussovým (normálním) rozdělením pravděpodobnosti, což je důsledek centrální limitní věty, když se kombinuje mnoho nezávislých šumových zdrojů. Tento model není fyzickou součástkou, ale statistickou abstrakcí používanou k vyjádření souhrnného účinku různých tepelných a elektronických šumových zdrojů vlastních přijímačům a přenosovým médiím.

Ve specifikacích 3GPP slouží AWGN jako standardní referenční kanál pro testování výkonu a ověřování shody uživatelských zařízení (UE) a základnových stanic (např. NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB). Testovací specifikace (např. TS 36.521, TS 38.522) definují testy přijímače, kde testované zařízení musí správně demodulovat a dekódovat signály za přítomnosti řízené úrovně AWGN. Výkon šumu je přesně definován spektrální hustotou šumu (N0) a šířkou pásma systému, což umožňuje výpočet klíčového poměru signál-šum (SNR) nebo Eb/N0 (poměr energie na bit k spektrální hustotě výkonu šumu). Tyto metriky přímo souvisejí s teoretickými výkonnostními limity, jako je Shannonova kapacita, a praktickými metrikami, jako je bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)) a propustnost.

Role AWGN se rozprostírá na celý životní cyklus bezdrátového systému. Během návrhu systému a analýzy rozpočtu přenosového spoje inženýři používají AWGN k výpočtu potřebného vysílacího výkonu a citlivosti přijímače pro dosažení cílového pokrytí a kvality služby. Ve výkonnostních simulacích technologií od GSM po 5G NR se kanály AWGN používají k vytvoření základní výkonnostní úrovně pro modulační schémata (QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/) atd.) a kódovací rychlosti před zavedením složitějších, reálných zkreslení, jako je útlum (fading) a interference. Pro testování shody poskytuje reprodukovatelné a standardizované nejhorší možné šumové prostředí, které zajišťuje minimální výkon přijímače napříč všemi výrobci a zařízeními, a tím garantuje základní interoperabilitu a síťové pokrytí.

Zatímco AWGN představuje idealizovaný model šumu, je prvním krokem v hierarchii modelů kanálů. Pokročilejší modely, jako jsou ty definované v 3GPP TR 38.901, kombinují AWGN se specifickými profily vícecestného útlumu (např. modely s čárkovaným zpožděním pro scénáře Urban Macro, Rural Macro) k simulaci realistických podmínek šíření rádiového signálu. Jednoduchost a dobře prozkoumané statistické vlastnosti AWGN z něj činí nepostradatelný nástroj pro teoretickou analýzu, vývoj algoritmů (např. pro kanálové kódování a ekvalizaci) a základní benchmarkování všech digitálních komunikačních systémů specifikovaných 3GPP.

## K čemu slouží

AWGN existuje jako základní analytický a testovací nástroj pro abstrakci a kvantifikaci neodstranitelného náhodného šumu přítomného v jakémkoli komunikačním systému. Jeho primárním účelem je poskytovat konzistentní, matematicky zpracovatelnou základnu, vůči které lze hodnotit základní výkonnostní limity modulace, kódování a návrhů přijímačů. Před formálním přijetím takových modelů byla výkonnostní analýza ad-hoc a méně srovnatelná mezi různými systémy. Model AWGN řeší problém vytvoření společného referenčního bodu pro citlivost a odolnost, což inženýrům umožňuje oddělit vlastní výkonnost komunikačního schématu od dodatečných degradací způsobených specifickými účinky šíření, jako je vícecestný útlum (multipath fading).

Motivace pro jeho použití ve standardech 3GPP vychází z potřeby důkladného, opakovatelného testování shody. Definováním testů přijímače za podmínek AWGN zajišťuje 3GPP, že všechna kompatibilní zařízení splňují minimální výkonnostní práh v řízeném šumovém prostředí. To garantuje základní úroveň síťového pokrytí a kvality služby, protože zařízení musí být schopna správně fungovat na okraji pokrytí buňky, kde je signál nejslabší a šum je dominantním zkreslením. Historicky Shannon-Hartleyova věta, která definuje kapacitu kanálu za přítomnosti AWGN, stanovila teoretický význam tohoto modelu šumu, čímž se stal základním kamenem pro porovnávání spektrální účinnosti různých digitálních komunikačních technologií, od 2G GSM po 5G NR.

Zatímco reálné kanály zahrnují korelovaný útlum a negaussovské rušení, AWGN řeší základní omezení spočívající v absenci standardizovaného benchmarku. Představuje nejjednodušší, ale nejkritičtější zkreslení, které umožňuje odvodit základní vztahy, jako je kompromis mezi šířkou pásma, výkonem a datovou rychlostí. Jeho použití ve specifikacích zajišťuje, že hodnocení výkonnosti začíná na dobře prozkoumaném společném základě, na který jsou následně vrstveny dodatečné složitosti mobilních rádiových kanálů pro realističtější posouzení a optimalizaci.

## Klíčové vlastnosti

- Statistický model s vlastnostmi aditivnosti, bělosti a Gaussovského rozdělení
- Slouží jako standardní referenční kanál pro testování přijímačů UE a základnových stanic
- Umožňuje výpočet základních metrik jako SNR, Eb/N0 a kapacity kanálu
- Poskytuje reprodukovatelnou základnu pro výkonnost měřenou poměrem chybných bitů (BER) a blokovou chybovostí (BLER)
- Používá se v analýze rozpočtu přenosového spoje (link budget) k určení citlivosti přijímače a potřebného výkonu signálu
- Základní složka pokročilejších modelů kanálů, které zahrnují útlum (fading) a interferenci

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- … a dalších 35 specifikací

---

📖 **Anglický originál a plná specifikace:** [AWGN na 3GPP Explorer](https://3gpp-explorer.com/glossary/awgn/)
