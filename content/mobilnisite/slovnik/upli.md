---
slug: "upli"
url: "/mobilnisite/slovnik/upli/"
type: "slovnik"
title: "UPLI – UE Provided Location Information"
date: 2025-01-01
abbr: "UPLI"
fullName: "UE Provided Location Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/upli/"
summary: "Funkce definovaná ve specifikaci 3GPP Release 14, při níž uživatelské zařízení (UE) poskytuje síti vlastní polohu nebo měření související s polohou. Zlepšuje služby založené na poloze využitím schopno"
---

UPLI je funkce 3GPP, při níž uživatelské zařízení (UE) poskytuje síti vlastní polohu nebo měření polohy, čímž zlepšuje služby a snižuje zatížení sítě.

## Popis

UE Provided Location Information (UPLI) je servisní schopnost zavedená ve specifikacích 3GPP, především v TS 23.271, která umožňuje uživatelskému zařízení (UE) autonomně určit a nahlásit svou zeměpisnou polohu nebo poskytnout síti nezpracovaná měřicí data. Na rozdíl od tradičních síťových metod určování polohy, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo Enhanced Cell ID ([E-CID](/mobilnisite/slovnik/e-cid/)), přenáší UPLI výpočetní zátěž na UE. UE může využít své vnitřní schopnosti, jako jsou přijímače globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/), např. [GPS](/mobilnisite/slovnik/gps/), Galileo), inerciální senzory (akcelerometry, gyroskopy), měření Wi-Fi přístupových bodů nebo Bluetooth majáků, k výpočtu své polohy.

Proces typicky zahrnuje žádost sítě o informace o poloze prostřednictvím protokolů řídicí nebo uživatelské roviny, jako je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo [SUPL](/mobilnisite/slovnik/supl/) (Secure User Plane Location). UE odpoví buď vypočteným odhadem polohy (zeměpisná šířka, délka, nadmořská výška, nejistota), nebo měřicími daty (např. GNPS pseudovzdálenosti, Wi-Fi [RSSI](/mobilnisite/slovnik/rssi/)), která může síťový Location Server (např. Evolved Serving Mobile Location Center - [E-SMLC](/mobilnisite/slovnik/e-smlc/)) použít k výpočtu polohy. V 5G je toto rozšířeno o Location Management Function (LMF) a New Radio Positioning Protocol (NRPPa).

UPLI podporuje různé parametry QoS, včetně přesnosti, doby odezvy a rychlosti. Umožňuje hybridní určování polohy, při kterém jsou data poskytnutá UE kombinována se síťovými měřeními pro vyšší spolehlivost, zejména v náročných prostředích, jako jsou interiéry nebo městské kaňony. Tato funkce je nedílnou součástí tísňových služeb (např. E911, eCall), kde je rychlá a přesná lokalizace kritická, stejně jako komerčních aplikací, jako je navigace, sledování majetku nebo reklama založená na poloze. Přispívá také k plnění regulatorních požadavků na hlášení polohy.

## K čemu slouží

UPLI bylo vyvinuto k řešení omezení síťově orientovaných lokalizačních technologií, které mohou být náročné na infrastrukturu, méně přesné v určitých prostředích a nemusí být efektivně škálovatelné pro služby masového trhu. Předchozí metody se silně spoléhaly na síťová měření, která mohla být ovlivněna hustotou nasazení, podmínkami šíření signálu a vyžadovala značnou signalizační režii. Rozšíření chytrých telefonů s pokročilými GNSS a senzorickými schopnostmi představovalo příležitost využít prostředky UE pro přesnější a efektivnější určování polohy.

K jejímu vytvoření motivovala rostoucí poptávka po službách určování polohy s vysokou přesností pro tísňové služby, komerční aplikace a sledování v rámci internetu věcí (IoT). Pro tísňové služby mohou rychlejší a spolehlivější informace o poloze zachraňovat životy. Pro komerční využití umožňuje inovativní aplikace, jako je rozšířená realita, geofencing a personalizované služby. UPLI také snižuje signalizační zátěž sítě tím, že umožňuje UE vypočítat polohu lokálně, což je zvláště výhodné pro zařízení IoT s omezenou životností baterie nebo ve scénářích s omezeným pokrytím sítě. Představuje posun směrem ke kolaborativnějšímu ekosystému určování polohy.

## Klíčové vlastnosti

- Určování polohy založené na UE s využitím GNSS, senzorů nebo Wi-Fi
- Podpora doručování jak řídicí rovinou (LPP), tak uživatelskou rovinou (SUPL)
- Hybridní metody určování polohy kombinující data z UE a sítě
- Konfigurovatelné parametry QoS pro přesnost a latenci
- Využití pro tísňové služby (např. E911, eCall) a komerční aplikace
- Snížená signalizační režie sítě ve srovnání se síťovými metodami

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [UPLI na 3GPP Explorer](https://3gpp-explorer.com/glossary/upli/)
