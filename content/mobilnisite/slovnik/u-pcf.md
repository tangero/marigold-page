---
slug: "u-pcf"
url: "/mobilnisite/slovnik/u-pcf/"
type: "slovnik"
title: "U-PCF – UTRAN Position Calculation Function"
date: 2025-01-01
abbr: "U-PCF"
fullName: "UTRAN Position Calculation Function"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-pcf/"
summary: "Funkční entita v rámci UTRAN odpovědná za výpočet geografické polohy uživatelského zařízení (UE). Zpracovává měřicí data z UE a sítě pro určení polohy a podporuje služby jako tísňová volání a služby z"
---

U-PCF je funkční entita UTRAN odpovědná za výpočet geografické polohy uživatelského zařízení (UE) zpracováním měřicích dat pro podporu služeb, jako jsou tísňová volání.

## Popis

Funkce výpočtu polohy [UTRAN](/mobilnisite/slovnik/utran/) (U-PCF) je klíčovou součástí architektury UTRAN, speciálně navrženou pro mobilní určování polohy. Nachází se v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) a je odpovědná za výpočetní aspekty určení geografické polohy uživatelského zařízení (UE). U-PCF přijímá nezpracovaná měřicí data, která mohou zahrnovat časová měření jako doba zpátečního letu ([RTT](/mobilnisite/slovnik/rtt/)), měření pozorovaného časového rozdílu příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo data asistovaného globálního navigačního satelitního systému ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Tato data zpracovává pomocí specifických algoritmů určování polohy, jako je Cell-ID, OTDOA nebo časový rozdíl příchodu v uplinku ([U-TDOA](/mobilnisite/slovnik/u-tdoa/)), aby vypočítala souřadnice zeměpisné šířky, délky a nadmořské výšky. Funkce komunikuje s dalšími entitami UTRAN pro určování polohy, jako je funkce rádiové koordinace polohy UTRAN ([U-PRCF](/mobilnisite/slovnik/u-prcf/)), pro vyžádání měření a s jádrem sítě přes rozhraní Iupc pro příjem požadavků na lokalizační služby a doručení vypočítaných výsledků polohy. Její role je čistě výpočetní; sama nespravuje rádiové prostředky ani nekoordinuje postupy měření. Přesnost určení polohy závisí na zvolené metodě, dostupných měřeních a faktorech prostředí. U-PCF je nezbytná pro přeměnu síťových a satelitních signálů na využitelné informace o poloze.

## K čemu slouží

U-PCF byla zavedena, aby poskytla standardizovanou, na síti založenou metodu pro určení polohy mobilního zařízení v rámci 3GPP [UTRAN](/mobilnisite/slovnik/utran/). Před její specifikací byly lokalizační služby často proprietární nebo spoléhaly na méně přesné metody, jako je jednoduchý Cell-ID. Hnacím motorem byly regulační požadavky, jako je Enhanced 911 (E911) ve Spojených státech, které vyžadovaly přesnou polohu pro tísňová volání, a komerční poptávka po službách založených na poloze (LBS). U-PCF řeší potřebu spolehlivého, integrovaného výpočetního jádra pro určování polohy v rámci RAN, odděluje výpočetní logiku od koordinace měření a správy rádiových prostředků. Tento modulární přístup umožňuje implementaci různých technologií určování polohy (OTDOA, A-GNSS) pomocí společného funkčního rozhraní. Vyřešila problém, jak efektivně a přesně vypočítat polohu pomocí různorodých měřicích zdrojů dostupných v síti 3G, což umožnilo dodržování zákonných požadavků a odemklo operátorům nové příjmy ze služeb.

## Klíčové vlastnosti

- Provádí algoritmy určování polohy (např. Cell-ID, OTDOA, A-GNSS) pro výpočet souřadnic UE
- Zpracovává nezpracovaná měřicí data z UE a síťových prvků (Node B)
- Komunikuje s U-PRCF pro získání potřebných rádiových měření pro určení polohy
- Komunikuje s centrem obsluhy mobilní polohy (SMLC) jádra sítě přes rozhraní Iupc
- Podporuje více metod určování polohy pro vyvážení přesnosti, latence a zatížení sítě
- Poskytuje vypočítané informace o poloze (zeměpisná šířka, délka, nejistota) žádajícím entitám

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [U-PRCF – UTRAN Position Radio Co-ordination Function](/mobilnisite/slovnik/u-prcf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [U-PCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-pcf/)
