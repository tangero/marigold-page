---
slug: "tow"
url: "/mobilnisite/slovnik/tow/"
type: "slovnik"
title: "TOW – Time of Week"
date: 2025-01-01
abbr: "TOW"
fullName: "Time of Week"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/tow/"
summary: "Time of Week (TOW) je základní časový parametr používaný v satelitních navigačních systémech, jako je GPS. Představuje uplynulý čas v rámci aktuálního týdne GPS, počínaje od okamžiku přetečení týdne."
---

TOW (Time of Week) je uplynulý čas v rámci aktuálního týdne GPS, používaný pro synchronizaci satelitních přenosů a výpočet polohy v satelitních navigačních systémech.

## Popis

Time of Week (TOW) je kontinuální časová míra používaná v rámci globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)), především Global Positioning System ([GPS](/mobilnisite/slovnik/gps/)). Je to skalární hodnota, která počítá počet sekund uplynulých od začátku aktuálního týdne GPS. Týden GPS je definován jako 604 800 sekund (7 dní * 24 hodin * 3600 sekund). Počítadlo TOW se vynuluje při přechodu mezi týdny GPS, k němuž dochází každou neděli v 00:00:00 času GPS (který je přibližně sladěn s [UTC](/mobilnisite/slovnik/utc/), ale nezahrnuje přestupné sekundy). TOW je přenášen v navigační zprávě od každého satelitu GPS, konkrétně v Handover Word ([HOW](/mobilnisite/slovnik/how/)) každého podrámce.

Z architektonického hlediska je TOW jádrovou součástí struktury signálu GNSS. Každý satelit vysílá svá navigační data v rámcích a podrámcích. HOW v každém podrámci obsahuje počítadlo TOW pro začátek následujícího podrámce. To umožňuje přijímači GNSS, jakmile dekóduje HOW z jednoho satelitu, synchronizovat svůj vnitřní časový základ s přesným systémovým časem GPS. Přijímač používá tuto informaci TOW k výpočtu přesného času vysílání dálkoměrných kódů (pseudonáhodných šumových kódů) z každého satelitu. Přesnost těchto časových razítek je zásadní pro výpočet doby šíření signálu neboli pseudodosahu ze satelitu k přijímači.

Během provozu přijímač GNSS provádí korelaci pro zachycení satelitních signálů. Jakmile je signál zachycen a sledován, přijímač dekóduje navigační zprávu, aby extrahoval TOW a další efemeridní data. TOW se používá k vyřešení celočíselné nejednoznačnosti v milisekundách u měřené fáze kódu. Znalostí přesného TOW odpovídajícího přijatému signálu může přijímač vypočítat plnou, jednoznačnou dobu šíření signálu. Tento proces je nezbytný pro výpočet přesné polohy. Time To First Fix ([TTFF](/mobilnisite/slovnik/ttff/)) je silně závislý na tom, jak rychle může přijímač získat platný TOW. Při studeném startu musí přijímač dekódovat alespoň celý podrámec (6 sekund) z jednoho satelitu, aby získal TOW, což je hlavní faktor počátečního TTFF. Asistenční data, jako předpovězené efemeridy a časové modely, mohou přijímači poskytnout přibližný TOW, což drasticky zkracuje tuto dobu akvizice.

## K čemu slouží

TOW existuje jako základní časový mechanismus v rámci architektur [GPS](/mobilnisite/slovnik/gps/) a podobných [GNSS](/mobilnisite/slovnik/gnss/), aby poskytoval společný, přesný a kontinuální časový odkaz pro všechny satelity a uživatele. Před zavedením celosystémového času, jako je TOW, by koordinace signálů z více nezávisle se pohybujících satelitů pro přesné dálkoměření byla nesmírně složitá. TOW řeší problém synchronizace přenosů z celé satelitní konstelace a poskytuje uživatelům kritické časové razítko potřebné pro měření zpoždění šíření signálu.

Historická motivace vychází ze základního principu satelitní navigace: poloha je odvozena z přesně změřených vzdáleností (dosahů) ke známým polohám satelitů. Pro měření vzdálenosti je nutné přesně vědět, kdy signál opustil satelit a kdy dorazil k přijímači. TOW poskytuje časové razítko „kdy opustil“ v univerzálním systémovém čase. Omezení spočívající v absenci takového synchronizovaného času by byla katastrofální – měření dosahů by byla nekoherentní a výpočet polohy nemožný. TOW spolu s číslem týdne GPS vytváří pro systém kontinuální, jednoznačnou časovou osu.

Jeho role v [TTFF](/mobilnisite/slovnik/ttff/) je obzvláště klíčová. Přijímač musí určit celkovou dobu šíření signálu, která zahrnuje neznámý celočíselný počet milisekund. Hodnota TOW, vysílaná každých 6 sekund, umožňuje přijímači tuto nejednoznačnost vyřešit. Potřeba dekódovat tento TOW z relativně pomalého (50 bps) navigačního datového spojení byla hlavním úzkým hrdlem pro rychlé určování polohy. Toto omezení přímo vedlo k vývoji technologií Assisted-GNSS (A-GNSS), kde síť poskytuje aktuální TOW (nebo jeho blízký odhad) UE jako asistenční data, což umožňuje TTFF pod sekundu a umožňuje lokalizační služby pro tísňová volání a spotřebitelské aplikace.

## Klíčové vlastnosti

- Počítá sekundy od 0 do 604 799 v rámci týdne GPS
- Přenášen v Handover Word (HOW) každého navigačního podrámce GPS
- Poskytuje přesný časový odkaz systému GPS pro časové označování satelitních signálů
- Nezbytný pro vyřešení celočíselné nejednoznačnosti v milisekundách u měření fáze kódu
- Základní parametr pro výpočet doby šíření satelitního signálu (pseudodosah)
- Primární determinant Time To First Fix (TTFF) v autonomním provozu GNSS

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [TTFF – Time To First Fix](/mobilnisite/slovnik/ttff/)

## Definující specifikace

- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS

---

📖 **Anglický originál a plná specifikace:** [TOW na 3GPP Explorer](https://3gpp-explorer.com/glossary/tow/)
