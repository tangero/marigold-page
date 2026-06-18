---
slug: "sd"
url: "/mobilnisite/slovnik/sd/"
type: "slovnik"
title: "SD – Secondary stream ETFC Offset"
date: 2026-01-01
abbr: "SD"
fullName: "Secondary stream ETFC Offset"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sd/"
summary: "Parametr používaný při vysílání ve výstupním směru (uplink) v 5G NR, konkrétně pro vlnový tvar CP-OFDM s vypnutým transformačním předkódováním (transform precoding). Definuje výkonový posuv aplikovaný"
---

SD je parametr pro výstupní (uplink) směr v 5G NR pro CP-OFDM, který definuje výkonový posuv (offset) aplikovaný na sekundární datový proud (stream) vůči primárnímu proudu pro řízení výkonu u vícevrstvého (multi-layer) MIMO.

## Popis

Secondary stream ETFC Offset (SD) je technický parametr ve specifikacích fyzické vrstvy 5G New Radio (NR) pro řízení výkonu ve výstupním směru (uplink). Je použitelný, když je UE (uživatelské zařízení) nakonfigurováno pro vysílání ve výstupním směru s využitím vlnového tvaru [CP-OFDM](/mobilnisite/slovnik/cp-ofdm/) bez transformačního předkódování (tj. nepoužívá DFT-s-OFDM) a pracuje ve vícevrstvém ([MIMO](/mobilnisite/slovnik/mimo/)) scénáři. ETFC znamená 'Effective Target received power per [FFT](/mobilnisite/slovnik/fft/) bin per Channel'. Parametr SD, signalizovaný sítí prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) nebo [MAC](/mobilnisite/slovnik/mac/) [CE](/mobilnisite/slovnik/ce/), poskytuje hodnotu posuvu v decibelech (dB). Tento posuv se používá ve vzorci pro řízení výkonu ve výstupním směru k výpočtu vysílacího výkonu pro sekundární datový proud vůči primárnímu proudu. Výkon primárního proudu je určen na základě mechanismů řízení výkonu s otevřenou smyčkou (open-loop) a uzavřenou smyčkou (closed-loop), zahrnujících odhady útlumu na trase (pathloss) a [TPC](/mobilnisite/slovnik/tpc/) příkazy. Pro sekundární proud je jeho výkon odvozen aplikací posuvu SD na vypočtený výkon primárního proudu. Tento přístup umožňuje gNB jemně řídit relativní úrovně výkonu mezi více prostorovými vrstvami, což je klíčové pro optimalizaci výkonu MIMO ve výstupním směru, správu interference mezi vrstvami a zajištění spolehlivé demodulace na přijímači. Parametr je součástí sady úprav řízení výkonu, které umožňují efektivní využití spektra a adaptaci spoje v pokročilých nasazeních 5G NR.

## K čemu slouží

Parametr SD byl zaveden, aby řešil specifické potřeby uplink Multi-User [MIMO](/mobilnisite/slovnik/mimo/) (MU-MIMO) a single-user MIMO (SU-MIMO) v 5G NR, zejména při použití spektrálně efektivního vlnového tvaru CP-OFDM. V LTE bylo MIMO ve výstupním směru více omezené a často používalo DFT-s-OFDM (SC-FDMA), které má odlišné výkonové charakteristiky. S podporou CP-OFDM ve výstupním směru v 5G a pokročilejšími víceanténními technikami byl vyžadován jemnější mechanismus řízení výkonu. Různé prostorové proudy mohou zažívat různé efektivní kanály nebo podmínky interference. Aplikace stejného vysílacího výkonu na všechny proudy není optimální. Posuv SD umožňuje gNB nezávisle vyvažovat výkon mezi primárním a sekundárním proudem, čímž optimalizuje poměr signálu k šumu a interferenci (SINR) pro každou vrstvu. Tím se řeší problémy, jako je převládnutí jednoho proudu nad druhým nebo nedostatečný výkon pro sekundární proud při vysílání s hodností (rank) 2, což v konečném důsledku zlepšuje propustnost ve výstupním směru, výkon na okraji buňky a celkovou efektivitu MIMO v různých rádiových podmínkách.

## Klíčové vlastnosti

- Parametr pro řízení výkonu ve výstupním směru (uplink) v 5G NR CP-OFDM (bez transformačního předkódování)
- Definuje výkonový posuv v dB pro sekundární datový proud vůči primárnímu proudu
- Umožňuje nezávislou úpravu výkonu pro různé prostorové vrstvy v uplink MIMO
- Konfigurován sítí prostřednictvím RRC signalizace nebo MAC Control Element
- Použit při výpočtu vysílacího výkonu UE pro PUSCH
- Optimalizuje výkon pro scénáře uplink SU-MIMO a MU-MIMO

## Související pojmy

- [CP-OFDM – Cyclic Prefix Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/cp-ofdm/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)

## Definující specifikace

- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 31.105** (Rel-19) — Slice Subscriber Identity Module (SSIM) Application
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.818** (Rel-8) — SA5 MTOSI XML Harmonization Study
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.859** (Rel-18) — Technical Report
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [SD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sd/)
