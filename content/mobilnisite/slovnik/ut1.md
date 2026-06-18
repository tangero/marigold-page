---
slug: "ut1"
url: "/mobilnisite/slovnik/ut1/"
type: "slovnik"
title: "UT1 – Universal Time No.1"
date: 2025-01-01
abbr: "UT1"
fullName: "Universal Time No.1"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ut1/"
summary: "UT1 je přesná forma univerzálního času korigovaná o polární pohyb, která představuje skutečný rotační úhel Země. V 3GPP se používá pro vysoce přesné časování v polohovacích a navigačních systémech, ja"
---

UT1 je přesná forma univerzálního času korigovaná o polární pohyb, používaná v 3GPP pro vysoce přesné časování v polohovacích systémech, jako je Assisted GNSS, pro zajištění přesného určení polohy.

## Popis

Universal Time No.1 (UT1) je konkrétní realizace univerzálního času, která zohledňuje polární pohyb – pohyb rotační osy Země vůči její kůře. Je odvozena z pozorování vzdálených kvasarů pomocí interferometrie s velmi dlouhou základnou (VLBI) a poskytuje vysoce přesné měření úhlu rotace Země. UT1 je zásadní, protože představuje skutečný sluneční čas a zohledňuje nepravidelnosti v rotaci Země, jako jsou variace délky dne a sezónní efekty. Na rozdíl od koordinovaného světového času ([UTC](/mobilnisite/slovnik/utc/)), který používá přestupné sekundy, aby se udržel blízko UT1, je samotné UT1 spojité časové měřítko bez diskontinuit, což jej činí ideálním pro vědecké a technické aplikace vyžadující plynulý průběh času. Ve specifikacích 3GPP je UT1 primárně odkazováno v dokumentech jako 36.355 a 37.355 pro služby určování polohy, zejména v protokolech Assisted Global Navigation Satellite System ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Umožňuje mobilním zařízením získat přesné časové informace ze sítě, což je klíčové pro výpočet polohy synchronizací se satelitními signály. Integrace UT1 do 3GPP zajišťuje, že telekomunikační sítě mohou poskytovat přesné časové asistence uživatelskému zařízení (UE), čímž zvyšují přesnost služeb založených na poloze. Toho je dosaženo prostřednictvím síťových prvků, jako jsou funkce pro správu polohy ([LMF](/mobilnisite/slovnik/lmf/)), které šíří data UT1 jako součást asistenčních informací. Role UT1 se rozšiřuje na scénáře synchronizace sítě, kde je vyžadováno časování vztažené k Zemi, podporující aplikace v letectví, námořnictví a dalších sektorech závislých na přesném rotačním čase.

## K čemu slouží

UT1 existuje, aby poskytoval vysoce přesný časový referenční systém založený na rotaci Země, který koriguje polární pohyb, a řeší tak potřebu přesného astronomického časování v telekomunikacích. Řeší problém sladění síťového časování se skutečnou rotací Země, což je kritické pro polohovací systémy jako [GNSS](/mobilnisite/slovnik/gnss/), které spoléhají na přesnou synchronizaci se satelity. Historicky byl UT1 vyvinut pro zpřesnění univerzálního času zohledněním výchylky osy, čímž nabízí stabilnější referenci pro vědecká pozorování a navigaci. V 3GPP byl UT1 od Release 9 začleněn pro vylepšení služeb určování polohy, což umožňuje sítím doručovat přesnou časovou asistenci mobilním zařízením pro rychlejší a přesnější určení polohy. Tím se řeší omezení dřívějších metod časování, které nemusely zohledňovat rotační variace, a zlepšuje se výkon v městských kaňonech nebo vnitřních prostorech, kde jsou satelitní signály slabé. Motivace pro zahrnutí UT1 vychází z rostoucí poptávky po spolehlivých aplikacích založených na poloze, jako jsou služby tísňového volání nebo sledování majetku, které vyžadují robustní časové reference pro efektivní fungování v globálních sítích.

## Klíčové vlastnosti

- Koriguje univerzální čas o polární pohyb
- Poskytuje spojité měření úhlu rotace Země
- Používá se v 3GPP pro časovou asistenci A-GNSS
- Zvyšuje přesnost služeb založených na poloze
- Podporuje synchronizaci sítě s astronomickým časem
- Odkazuje se na něj v polohovacích protokolech LTE a 5G

## Související pojmy

- [UT – Universal Time](/mobilnisite/slovnik/ut/)
- [UTC – Coordinated Universal Time](/mobilnisite/slovnik/utc/)

## Definující specifikace

- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [UT1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ut1/)
