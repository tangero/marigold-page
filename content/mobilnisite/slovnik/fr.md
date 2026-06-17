---
slug: "fr"
url: "/mobilnisite/slovnik/fr/"
type: "slovnik"
title: "FR – Full Rate (GSM Full Rate channel or speech codec)"
date: 2026-01-01
abbr: "FR"
fullName: "Full Rate (GSM Full Rate channel or speech codec)"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fr/"
summary: "Odkazuje na původní plnorychlostní hlasový kanál GSM (TCH/FS) nebo jeho přidružený hlasový kodek. Byl prvním standardem digitálního kódování hlasu pro GSM, který poskytoval základní hlasovou službu s"
---

FR je původní plnorychlostní hlasový kanál GSM (Full Rate speech traffic channel) nebo jeho přidružený hlasový kodek, který poskytuje základní digitální hlasovou službu při přenosové rychlosti 13 kbps.

## Popis

V systému GSM má 'FR' dva hlavní, vzájemně související významy. Za prvé označuje plnorychlostní hlasový kanál (TCH/[FS](/mobilnisite/slovnik/fs/)), což je přidělení fyzického rádiového zdroje. Jedná se o vyhrazený kanál přenášející uživatelská hlasová data s hrubou přenosovou rychlostí přibližně 22,8 kbps, která zahrnuje hlasové kódování, kanálové kódování pro ochranu proti chybám a další režii. Struktura kanálu spočívá v rozdělení nosné o šířce 200 kHz na 8 časových slotů (TDMA), přičemž TCH zabírá jeden časový slot v opakující se rámcové struktuře. Tento kanál se používá pro skutečný obousměrný hlasový hovor.

Za druhé, a konkrétněji, FR odkazuje na samotný hlasový kodek GSM Full Rate. Toto byl první digitální hlasový kodek standardizovaný pro GSM (specifikovaný v GSM 06.10, později 3GPP TS 06.10/TS 46.010). Jedná se o kodek založený na lineární prediktivní kódování ([LPC](/mobilnisite/slovnik/lpc/)) s pravidelnou pulzní excitační (RPE), často nazývaný kodek RPE-LTP (Long-Term Prediction). Kodek funguje tak, že analyzuje 20ms segmenty (160 vzorků) vstupního hlasového signálu. Extrahuje parametry reprezentující filtr hlasového traktu (LPC koeficienty), dlouhodobou korelaci základního tónu ([LTP](/mobilnisite/slovnik/ltp/)) a krátkodobý reziduální signál (RPE). Tyto parametry jsou každých 20 ms zakódovány do bloku o 260 bitech, což vede k čisté přenosové rychlosti 13 kbps. Před přenosem je tento 260bitový blok podroben kanálovému kódování, kde jsou přidány bity pro ochranu proti chybám, čímž se přenášená přenosová rychlost zvýší na 22,8 kbps pro TCH/FS.

Úloha kodeku FR a kanálu byla základní. Definoval referenční úroveň kvality hlasu pro rané digitální celulární sítě a nabídl výrazné zlepšení srozumitelnosti a odolnosti proti šumu ve srovnání s analogovými systémy. Jeho kvalita hlasu, často popisovaná jako 'syntetická' nebo 'robotická', však byla známým omezením. To vedlo k vývoji vylepšených kodeků, jako je Enhanced Full Rate ([EFR](/mobilnisite/slovnik/efr/)) a později adaptivní vícekódový kodek ([AMR](/mobilnisite/slovnik/amr/)). V provozu sítě zůstává kanál FR záložní možností pro kompatibilitu, zejména když se mobilní stanice pohybuje v síti, která podporuje pouze základní kodek, nebo když jsou rádiové podmínky příliš špatné na to, aby podporovaly pokročilejší a efektivnější kodeky vyžadující vyšší kvalitu kanálu.

## K čemu slouží

Kodek a kanál GSM Full Rate byly vytvořeny k vyřešení základního problému: umožnit efektivní, zabezpečenou a kapacitně vyšší digitální hlasovou komunikaci pro první celulární standard pro masový trh. Před GSM byly analogové systémy, jako NMT a AMPS, náchylné k odposlechu, poskytovaly špatnou kvalitu hlasu v hlučném prostředí a měly omezenou kapacitu. Přechod na digitální technologii byl revoluční. Účelem kodeku FR bylo digitalizovat a komprimovat lidský hlas na dostatečně nízkou přenosovou rychlost (13 kbps), aby umožnil více uživatelům sdílet stejnou rádiovou frekvenci prostřednictvím TDMA, což dramaticky zvýšilo kapacitu sítě ve srovnání s analogovými systémy [FDMA](/mobilnisite/slovnik/fdma/).

Jeho vývoj byl hnán potřebou kompromisu mezi kvalitou hlasu, složitostí (a tedy náklady a spotřebou energie raných digitálních signálových procesorů) a spektrální účinností. Algoritmus RPE-LTP byl zvolen, protože poskytoval přijatelnou kvalitu v rámci přísných výpočetních omezení technologie konce 80. let 20. století. I když byla jeho kvalita později překonána, kodek FR úspěšně prokázal životaschopnost digitálního celulárního hlasu, stanovil základní strukturu kanálu (TCH/[FS](/mobilnisite/slovnik/fs/)) a položil základy pro veškerý následný vývoj hlasových kodeků ve standardech 3GPP. Řešil původní obchodní a technický požadavek: poskytnout komerčně životaschopnou, standardizovanou hlasovou službu, kterou lze nasadit globálně.

## Klíčové vlastnosti

- Původní digitální hlasový kodek GSM s čistou přenosovou rychlostí 13 kbps
- Založen na kódovacím algoritmu RPE-LTP (Regular Pulse Excitation - Long Term Prediction)
- Zpracovává hlas v 20ms rámcích, přičemž vytváří 260 bitů na rámec
- Funguje na vyhrazeném plnorychlostním hlasovém kanálu (TCH/FS)
- Poskytoval základní kvalitu hlasu a kapacitu pro sítě GSM 2. generace
- Sloužil jako povinný základní kodek pro počáteční kompatibilitu koncových zařízení a sítí GSM

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TS 26.231** (Rel-19) — CTM Minimum Performance Requirements Testing
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TS 26.269** (Rel-19) — eCall In-band Modem Conformance Testing
- **TR 26.967** (Rel-19) — eCall via CTM Suitability Analysis
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- … a dalších 49 specifikací

---

📖 **Anglický originál a plná specifikace:** [FR na 3GPP Explorer](https://3gpp-explorer.com/glossary/fr/)
