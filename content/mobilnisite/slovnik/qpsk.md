---
slug: "qpsk"
url: "/mobilnisite/slovnik/qpsk/"
type: "slovnik"
title: "QPSK – Quadrature Phase Shift Keying"
date: 2025-01-01
abbr: "QPSK"
fullName: "Quadrature Phase Shift Keying"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qpsk/"
summary: "Základní schéma digitální modulace používané v systémech 3GPP (od UMTS po 5G NR), které přenáší data modulací fáze nosné vlny do čtyř různých stavů. Přenáší dva bity na symbol a nabízí robustní rovnov"
---

QPSK je základní schéma digitální modulace používané v systémech 3GPP, které přenáší data modulací fáze nosné vlny do čtyř různých stavů, přičemž přenáší dva bity na symbol, což poskytuje robustní rovnováhu mezi spektrální účinností a odolností proti šumu.

## Popis

Quadrature Phase Shift Keying (QPSK, kvadraturní fázová manipulace) je technika modulace fázovým posuvem, která kóduje dva bity dat do jednoho symbolu výběrem jednoho ze čtyř možných fázových posuvů nosné vlny: 0°, 90°, 180° nebo 270°. Ty odpovídají čtyřem bodům v komplexní rovině: (1,0), (0,1), (-1,0) a (0,-1), často reprezentovaným jako symboly 00, 01, 11 a 10. Modulace je realizována samostatnou modulací nosné vlny ve fázi (I) a kvadraturní nosné vlny (Q), které jsou fázově posunuty o 90 stupňů, binárními datovými toky. Tato ortogonalita umožňuje přenášet obě složky současně na stejné frekvenci bez vzájemného rušení, čímž se efektivně zdvojnásobí přenosová rychlost ve srovnání s binární fázovou manipulací ([BPSK](/mobilnisite/slovnik/bpsk/)) při stejné šířce pásma.

V systémech 3GPP je QPSK klíčové modulační schéma specifikované v řadě technických specifikací (TS). Z architektonického hlediska se nachází v modulačním mapperu fyzické vrstvy, který převádí zakódované bity z řetězce kanálového kódování na komplexní modulační symboly. Například v LTE (TS 36.211) se QPSK používá pro několik fyzických kanálů včetně Physical Broadcast Channel ([PBCH](/mobilnisite/slovnik/pbch/)), Physical Control Format Indicator Channel ([PCFICH](/mobilnisite/slovnik/pcfich/)) a Physical Hybrid [ARQ](/mobilnisite/slovnik/arq/) Indicator Channel ([PHICH](/mobilnisite/slovnik/phich/)), stejně jako pro řídicí informace na uplinku na [PUSCH](/mobilnisite/slovnik/pusch/). V 5G NR (TS 38.211) se QPSK obdobně používá pro řídicí kanály jako Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) a Physical Uplink Control Channel ([PUCCH](/mobilnisite/slovnik/pucch/)) a jako základní modulace pro datové kanály v náročných rádiových podmínkách.

Jeho funkce spočívá v mapování párů bitů (d_i, d_i+1) na komplexní symbol podle definovaného konstelace. Demodulátor na straně přijímače odhadne přenesenou fázi, aby obnovil bity. Klíčovou výhodou QPSK je jeho robustnost; fázové rozdíly mezi symboly jsou 90 stupňů, což poskytuje významnou rezervu proti fázovým chybám způsobeným šumem nebo interferencí ve srovnání s modulacemi vyššího řádu jako 16QAM nebo 64QAM. To jej činí nezbytným pro spolehlivý přenos kritických řídicích informací a pro udržení konektivity na okraji buňky, kde je poměr signálu k šumu (SNR) nízký. Jeho konzistentní použití od 3G UMTS až po 5G NR zdůrazňuje jeho zásadní roli při zajišťování pokrytí sítě a spolehlivosti řídicí roviny.

## K čemu slouží

QPSK bylo přijato v raných digitálních celulárních systémech za účelem zlepšení spektrální účinnosti oproti jednodušším schématům jako BPSK při zachování přijatelné chybovosti v šumovém mobilním prostředí. V kontextu 3GPP bylo standardizováno od prvních WCDMA-based UMTS releasů (R99) jako primární modulace pro vyhrazené kanály a řídicí signalizaci. Motivací bylo efektivní využití omezeného rádiového spektra přenosem více bitů na Hertz bez nadměrného kompromisu v link budgetu. Předchozí analogové systémy a základní digitální modulace nemohly uspokojit rostoucí poptávku po datových službách.

Jak se 3GPP vyvíjelo přes HSPA, LTE a NR, potřeba adaptivní modulace a kódování (AMC) se stala klíčovou pro optimalizaci propustnosti v různých kanálových podmínkách. QPSK slouží jako nejrobustnější modulace v této hierarchii a používá se, když modulace vyššího řádu nejsou udržitelné kvůli špatnému SNR. Řeší problém spolehlivého provozu řídicích kanálů a záložního přenosu dat, čímž zajišťuje, že základní konektivita a systémové informace mohou být dekódovány i v nepříznivých podmínkách. Jeho pokračující specifikace v desítkách dokumentů 3GPP podtrhuje jeho roli jako základní, spolehlivé modulace, která umožňuje pokrytí sítě a odolnost, a doplňuje tak modulace s vyšší účinností používané v dobrých rádiových podmínkách.

## Klíčové vlastnosti

- Kóduje dva bity na symbol, čímž zdvojnásobuje přenosovou rychlost oproti BPSK při stejné šířce pásma.
- Používá čtyři fázové posuvy (0°, 90°, 180°, 270°) odpovídající bodům na jednotkové kružnici.
- Moduluje ortogonální nosné vlny ve fázi (I) a kvadraturní (Q).
- Poskytuje vysokou odolnost proti šumu a interferenci díky 90° fázovému rozdílu mezi symboly.
- Široce používané pro řídicí kanály a přenos dat při nízkém SNR v systémech 3G/4G/5G.
- Tvoří základ pro pi/2-QPSK a další varianty v konkrétních uplinkových scénářích.

## Související pojmy

- [BPSK – Binary Phase Shift Keying](/mobilnisite/slovnik/bpsk/)
- [16QAM – 16-Quadrature Amplitude Modulation](/mobilnisite/slovnik/16qam/)
- [64QAM – 64 Quadrature Amplitude Modulation](/mobilnisite/slovnik/64qam/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [QPSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/qpsk/)
