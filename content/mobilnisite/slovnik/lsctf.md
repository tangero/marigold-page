---
slug: "lsctf"
url: "/mobilnisite/slovnik/lsctf/"
type: "slovnik"
title: "LSCTF – Location System Coordinate Transformation Function"
date: 2025-01-01
abbr: "LSCTF"
fullName: "Location System Coordinate Transformation Function"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lsctf/"
summary: "Síťová funkce, která převádí surová měřicí data o poloze (např. časování, úhly, družicové signály) na standardizované zeměpisné souřadnice. Zpracovává transformace dat, mapové projekce a převody jedno"
---

LSCTF je síťová funkce, která převádí surová měřicí data o poloze na standardizované zeměpisné souřadnice tím, že provádí transformace dat, mapové projekce a převody jednotek.

## Popis

Location System Coordinate Transformation Function (LSCTF) je klíčová výpočetní komponenta v architektuře služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) podle 3GPP. Její hlavní úlohou je působit jako výpočetní engine, který převádí surová, technologií specifická měření polohy na všeobecně srozumitelnou zeměpisnou polohu. Metody určování polohy, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), Uplink Time Difference of Arrival (U-TDOA) nebo Assisted [GNSS](/mobilnisite/slovnik/gnss/) ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), přímo nevytvářejí zeměpisnou šířku a délku. Místo toho produkují mezilehlá data: OTDOA poskytuje měření časových rozdílů mezi rádiovými signály, U-TDOA produkuje data o době příchodu signálu a A-GNSS dodává družicová pseudovzdálenostní data a data almanachu.

LSCTF přijímá tato surová měřicí data, typicky přes Location System Control Function ([LSCFS](/mobilnisite/slovnik/lscfs/)) v SAS. Obsahuje algoritmy a databáze nezbytné pro provádění složitých výpočtů. Pro OTDOA využívá známé zeměpisné souřadnice základnových stanic (eNodeBů/gNBů nebo Node B) a naměřené časové rozdíly k výpočtu polohy UE pomocí multilaterace. Pro A-GNSS používá efemeridní data družic k řešení navigačních rovnic. Klíčovou a často opomíjenou odpovědností LSCTF je transformace souřadnicových systémů.

Tvar Země je modelován různými geodetickými daty (např. WGS-84 používané [GPS](/mobilnisite/slovnik/gps/) versus lokální národní datové systémy). LSCTF převádí vypočítanou polohu z nativního datového systému vstupních dat (např. lokálního systému použitého při zaměření sítě) na systém požadovaný klientem LCS, nejčastěji WGS-84. Může také provádět převody mezi různými formáty souřadnic (např. kartézský na elipsoidický) a mapové projekce. Díky centralizaci této složité matematické procesní vrstvy LSCTF odstiňuje servisní vrstvu od složitosti technologií určování polohy a zajišťuje, že všichni klienti polohových služeb dostávají souřadnice v jednotném, požadovaném formátu bez ohledu na použítou podkladovou metodu určování polohy.

## K čemu slouží

LSCTF byla vytvořena k řešení kritické výzvy v oblasti interoperability a složitosti v mobilních systémech určování polohy. Různé technologie určování polohy (síťové, terminálové, hybridní) a různá nasazení sítě (používající různé geodetické reference pro umístění základnových stanic) vytvářela údaje o poloze v odlišných a nekompatibilních formátech. Bez standardizované transformační funkce by klienti [LCS](/mobilnisite/slovnik/lcs/) museli rozumět specifikům každé metody určování polohy a každého geodetického systému, což by vývoj aplikací činilo těžkopádným a náchylným k chybám.

Tato funkce řeší problém poskytování jednotného rozhraní pro polohu. Umožňuje síti využívat nejvhodnější metodu určování polohy pro daný scénář (na základě přesnosti, rychlosti nebo možností UE) a zároveň garantuje, že výstup bude ve formátu, který může požadující služba použít. To je obzvláště zásadní pro tísňové služby (např. E911, eCall), kde musí být údaje o poloze doručeny do center tísňového přijmu v předepsaném souřadnicovém systému. LSCTF také umožňuje pokročilé služby, jako je účtování na základě polohy, sledování vozových parků a navigace, tímže poskytuje jednotný zeměpisný základ a odděluje logiku služby od matematických složitostí geodézie a polohovacích algoritmů.

## Klíčové vlastnosti

- Provádí polohovací algoritmy (např. multilateraci, trilateraci) pro výpočet souřadnic ze surových měření
- Provádí geodetické transformace mezi různými referenčními systémy (např. z lokálního systému na WGS-84)
- Převádí mezi formáty souřadnic (např. elipsoidický, kartézský, UTM projekce)
- Podporuje více vstupních typů z různých metod určování polohy (OTDOA, U-TDOA, A-GNSS, Cell-ID)
- Poskytuje výpočet nadmořské výšky a odhad nejistoty (přesnosti) pro výsledné určení polohy
- Slouží jako abstrakční vrstva, která odstíňuje klienty LCS od detailů podkladové polohovací technologie

## Související pojmy

- [LSCFS – Location System Control Function in SAS](/mobilnisite/slovnik/lscfs/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LSCTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsctf/)
