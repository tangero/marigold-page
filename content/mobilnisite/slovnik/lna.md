---
slug: "lna"
url: "/mobilnisite/slovnik/lna/"
type: "slovnik"
title: "LNA – Low Noise Amplifier"
date: 2025-01-01
abbr: "LNA"
fullName: "Low Noise Amplifier"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lna/"
summary: "Kritická RF komponenta v přijímacím řetězci základnové stanice nebo UE, která zesiluje slabé příchozí signály a přitom přidává minimální dodatečný šum. Je nezbytná pro udržení vysokého poměru signálu"
---

LNA (zesilovač s nízkým šumem) je kritická RF komponenta v přijímacím řetězci, která zesiluje slabé příchozí signály a přitom přidává minimální šum. Je nezbytná pro udržení vysokého poměru signálu k šumu (SNR) a citlivosti přijímače.

## Popis

Low Noise Amplifier (LNA, zesilovač s nízkým šumem) je specializovaný elektronický zesilovač používaný ve vstupní části (front-endu) rádiového přijímače. Jeho primární funkcí je zesílení extrémně slabých signálů zachycených anténou, aniž by došlo k výraznému zhoršení kvality signálu přidáním vlastního vnitřního šumu. To je kvantifikováno klíčovým parametrem zvaným šumové číslo ([NF](/mobilnisite/slovnik/nf/)), které představuje zhoršení poměru signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)) způsobené komponentami v [RF](/mobilnisite/slovnik/rf/) řetězci. Nižší šumové číslo je velmi žádoucí. LNA je typicky první aktivní stupeň za anténou a případným počátečním filtrováním, což činí jeho šumové vlastnosti prvořadými, protože šum přidaný tímto prvním zesilovacím stupněm je zesílen všemi následujícími stupni, což zásadně limituje celkovou citlivost přijímače.

Z architektonického hlediska je LNA klíčovou součástí dálkové rádiové hlavy ([RRH](/mobilnisite/slovnik/rrh/)) v základnové stanici nebo RF front-end modulu v uživatelském zařízení (UE). Je navržen pro provoz ve specifických kmitočtových pásmech definovaných 3GPP pro různé rádiové přístupové technologie ([RAT](/mobilnisite/slovnik/rat/)), jako jsou LTE a NR. Návrh zahrnuje pečlivý výběr polovodičové technologie (např. GaAs, SiGe) a topologie obvodu, aby bylo dosaženo optimální rovnováhy mezi nízkým šumovým číslem, dostatečným ziskem, linearitou (pro zpracování silných signálů bez zkreslení) a spotřebou energie. Jeho umístění je strategické; zesiluje signál předtím, než projde ztrátovými komponentami, jako jsou kabely a míchače, kde by jinak byl signál dále utlumen vzhledem k šumovému pozadí.

Jeho role v síti je zásadní pro výkon rádiového spoje. Zlepšením citlivosti přijímače LNA rozšiřuje efektivní oblast pokrytí buňky, zejména na jejích okrajích, kde jsou signály nejslabší. Také umožňuje příjem modulačních schémat vyššího řádu (jako 256-QAM nebo 1024-QAM), která vyžadují vysoký SNR, a tím podporuje vyšší špičkové datové rychlosti. V systémech [MIMO](/mobilnisite/slovnik/mimo/) a beamformingu má typicky každý anténní prvek svůj vlastní vyhrazený LNA, což činí výkon a shodu mezi LNA kritickými pro dosažení slibovaných zisků v spektrální účinnosti a spolehlivosti spoje. LNA je tedy základní hardwarovou komponentou, která podmiňuje metriky výkonnosti fyzické vrstvy specifikované v četných 3GPP technických specifikacích.

## K čemu slouží

LNA existuje, aby řešil základní problém citlivosti přijímače v bezdrátových komunikačních systémech. Příchozí signály ze vzdáleného vysílače jsou v okamžiku dopadu na přijímací anténu neuvěřitelně slabé a jsou často pohřbeny v šumovém pozadí. Pouhé zesílení tohoto signálu standardním zesilovačem by zesílilo i inherentní šum a přidalo by značný dodatečný šum ze samotného zesilovače, což by mohlo činit signál nepoužitelným pro demodulaci. Účelem LNA je poskytnout první stupeň 'čistého' zesílení, který zvýší výkon signálu vysoko nad šum zavedený následujícími stupni v přijímacím řetězci (jako jsou filtry, míchače a hlavní zesilovač středního kmitočtu/proměnného zisku).

Historicky, jak se buněčné systémy vyvíjely od 2G přes 3G a 4G až po současné 5G, tlak na vyšší datové rychlosti a efektivnější využití spektra posouval návrhy přijímačů na jejich limity. Modulační a kódovací schémata vyššího řádu vyžadují progresivně lepší [SNR](/mobilnisite/slovnik/snr/). LNA je klíčovým prvkem umožňujícím tuto evoluci. Jeho vznik a neustálé zdokonalování jsou motivovány potřebou překonat fyzikální omezení rádiového kanálu. Bez výkonného LNA by pokročilé techniky digitálního zpracování signálu používané v moderních systémech založených na [OFDM](/mobilnisite/slovnik/ofdm/) a OFDMA, jako jsou LTE a NR, byly neúčinné, protože počáteční analogový signál předkládaný analogově-digitálnímu převodníku (ADC) by byl příliš zkreslený šumem.

Navíc přechod k masivnímu MIMO a mmWave kmitočtům v 5G přináší nové výzvy. Na mmWave kmitočtech je útlum na dráze výrazně vyšší, což činí nízkou šumovou výkonnost LNA ještě kritičtější. Integrace LNA do modulů fázovaných anténních polí také vyžaduje miniaturizaci, energetickou účinnost a konzistentní výkon napříč velkým počtem paralelních přijímacích cest. LNA tedy řeší trvalou výzvu extrakce použitelného signálu ze šumového prostředí, což je problém, který roste s výkonnostními cíli každé generace.

## Klíčové vlastnosti

- Minimalizuje dodatečný šum díky nízkému šumovému číslu (NF)
- Poskytuje vysoký zisk v prvním zesilovacím stupni pro překonání následných ztrát
- Udržuje vysokou linearitu (IP3) pro zpracování silných signálů sousedních kanálů bez zkreslení
- Pracuje v definovaných 3GPP kmitočtových pásmech pro LTE a NR
- Navržen pro integraci do RRH a RF front-end modulů UE
- Kritický pro umožnění modulace vyššího řádu a maximální citlivosti přijímače

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.808** (Rel-12) — PIM Handling for Base Stations Study
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TR 38.803** (Rel-14) — Study on Coexistence and RF Feasibility for 5G NR
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [LNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lna/)
