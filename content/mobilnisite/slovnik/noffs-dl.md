---
slug: "noffs-dl"
url: "/mobilnisite/slovnik/noffs-dl/"
type: "slovnik"
title: "NOffs-DL – Downlink Offset"
date: 2025-01-01
abbr: "NOffs-DL"
fullName: "Downlink Offset"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/noffs-dl/"
summary: "Konstantní hodnota offsetu použitá ve vzorci pro výpočet downlink E-UTRA Absolute Radio Frequency Channel Number (EARFCN) z uplink EARFCN v LTE. Definuje pevné frekvenční oddělení mezi uplink a downli"
---

NOffs-DL je konstantní hodnota offsetu použitá ve vzorci pro výpočet downlink EARFCN z uplink EARFCN v LTE, která definuje pevné frekvenční oddělení mezi uplink a downlink nosnými kmitočty pro FDD.

## Popis

NOffs-DL je klíčový parametr v LTE systémech s duplexním provozem s frekvenčním dělením ([FDD](/mobilnisite/slovnik/fdd/)), který definuje vztah mezi uplink a downlink rádiovými kmitočty. Používá se v matematickém vzorci, který převádí [E-UTRA](/mobilnisite/slovnik/e-utra/) Absolute Radio Frequency Channel Number ([EARFCN](/mobilnisite/slovnik/earfcn/)) pro uplink na odpovídající EARFCN pro downlink. EARFCN je index odkazující na konkrétní středový kmitočet a vzorec zahrnující NOffs-DL zajišťuje správnou identifikaci spárovaného spektra pro FDD provoz.

Výpočet je definován jako: Downlink EARFCN (N_[DL](/mobilnisite/slovnik/dl/)) = Uplink EARFCN (N_UL) + NOffs-DL. Hodnota NOffs-DL je konstanta definovaná ve specifikacích 3GPP (TS 36.101). Jejím hlavním účelem je zohlednit pevný duplexní odstup – frekvenční mezeru mezi středy uplink a downlink nosných kmitočtů – který je charakteristický pro spárované spektrum FDD. Použitím tohoto offsetu mohou síť a uživatelské zařízení (UE) odvodit jedno číslo kanálu z druhého, což zjednodušuje konfiguraci a procedury vyhledávání buněk.

V praxi, když síť vysílá své downlink EARFCN na broadcast kanálu ([BCH](/mobilnisite/slovnik/bch/)), může UE nakonfigurované pro FDD režim vypočítat odpovídající uplink EARFCN odečtením NOffs-DL. To UE sděluje, který uplink kmitočet má použít pro vysílání. Parametr je základní pro LTE kmitočtovou mřížku kanálů a je kritický pro počáteční přístup UE, předávání spojení a konfigurace agregace nosných kmitočtů. Funguje ve spojení s dalšími parametry číslování kanálů, ale je specificky vázán na FDD duplexní režim.

## K čemu slouží

NOffs-DL byl zaveden, aby poskytl standardizovanou, jednoznačnou metodu pro mapování mezi uplink a downlink čísly kanálů v LTE [FDD](/mobilnisite/slovnik/fdd/). Řeší problém efektivní správy alokace spárovaného spektra. Před LTE mohly různé technologie používat ad-hoc metody nebo tabulky pro asociaci uplink a downlink kmitočtů. Vzorec založený na offsetu poskytuje jednoduchý, škálovatelný a implementačně přívětivý přístup.

Reaguje na potřebu jasného procedurálního vztahu mezi oběma směry nosného kmitočtu FDD, což je zásadní pro provoz UE. Při vyhledávání buňky UE detekuje downlink nosný kmitočet. Pro komunikaci musí znát spárovaný uplink kmitočet. Pevné zakódování všech možných párů by bylo neefektivní. Vzorec NOffs-DL to elegantně řeší definováním jediného offsetu pro celé pásmo, nebo v některých případech na provozní pásmo, jak je specifikováno ve standardech. Toto zjednodušuje plánování sítě, návrh UE a zajišťuje globální interoperabilitu pro FDD LTE zařízení roamující mezi různými síťovými operátory používajícími stejná kmitočtová pásma.

## Klíčové vlastnosti

- Definuje pevný offset mezi hodnotami uplink a downlink EARFCN pro FDD LTE
- Umožňuje výpočet čísla kanálu jednoho směru z druhého pomocí jednoduchého vzorce
- Hodnota je konstantní a specifikovaná na kmitočtové pásmo v 3GPP TS 36.101
- Zásadní pro počáteční přístup UE a uplink synchronizaci v režimu FDD
- Zjednodušuje konfiguraci sítě a informace vysílané buňkou
- Základní pro mřížku číslování kanálů LTE pro spárované spektrum

## Související pojmy

- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)

## Definující specifikace

- **TS 25.116** (Rel-19) — LCR TDD Repeater RF Characteristics
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TR 38.892** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NOffs-DL na 3GPP Explorer](https://3gpp-explorer.com/glossary/noffs-dl/)
