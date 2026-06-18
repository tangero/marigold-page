---
slug: "e-otd"
url: "/mobilnisite/slovnik/e-otd/"
type: "slovnik"
title: "E-OTD – Enhanced Observed Time Difference"
date: 2025-01-01
abbr: "E-OTD"
fullName: "Enhanced Observed Time Difference"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e-otd/"
summary: "Metoda určování polohy založená na síti pro stanovení geografické polohy mobilního zařízení. Polohu vypočítává měřením časového rozdílu příjmu signálů z více základnových stanic. Tato technologie je k"
---

E-OTD je metoda určování polohy založená na síti, která stanovuje polohu mobilního zařízení měřením časového rozdílu příjmu signálů z více základnových stanic.

## Popis

Enhanced Observed Time Difference (E-OTD, Rozšířený naměřený časový rozdíl) je technika určování polohy standardizovaná v 3GPP, při níž síť poskytuje asistenci, ale výpočet je mobilní. Základní princip spočívá v tom, že mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) měří Observed Time Difference ([OTD](/mobilnisite/slovnik/otd/), Naměřený časový rozdíl) příjmu signálů z alespoň tří geograficky rozptýlených základnových stanic ([BTS](/mobilnisite/slovnik/bts/)). OTD je časový rozdíl, který MS pozoruje mezi příchodem burstů z různých BTS. Toto měření OTD je však ovlivněno relativními časovými rozdíly mezi samotnými BTS, známými jako Real Time Difference ([RTD](/mobilnisite/slovnik/rtd/), Skutečný časový rozdíl). K určení skutečných geometrických časových rozdílů síť poskytuje MS asistenční data, včetně hodnot RTD a přesných geografických souřadnic BTS. Tyto RTD může měřit MS nebo síťová jednotka Location Measurement Unit ([LMU](/mobilnisite/slovnik/lmu/)). Pomocí měření OTD, korekčních dat RTD a známých poloh BTS může MS (nebo síťový server) vypočítat svou polohu pomocí hyperbolické trilaterace, kde každá hodnota OTD minus RTD definuje hyperbolu možných poloh a průsečík více hyperbol určuje polohu zařízení. Architektura zahrnuje MS, obsluhující Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Serving Mobile Location Center ([SMLC](/mobilnisite/slovnik/smlc/)), který řídí koordinaci a výpočet, a LMU pro kalibraci RTD. E-OTD nabízí lepší přesnost než jednodušší metody Cell-ID a funguje bez nutnosti úprav hardwaru mobilu pro příjem satelitních signálů, což z ní činí základní technologii pro služby určování polohy před érou [GPS](/mobilnisite/slovnik/gps/) v sítích 2G a 3G. Její výkon závisí na hustotě BTS a přesnosti synchronizace.

## K čemu slouží

E-OTD byl vyvinut za účelem splnění regulatorních požadavků na lokalizaci tísňových volajících (např. E911 v USA) a pro umožnění komerčních služeb založených na poloze (LBS) v sítích GSM a UMTS. Před E-OTD byla hlavní metodou Cell-ID, která poskytovala přesnost pouze v řádu poloměru buňky, často několik kilometrů, což bylo pro tísňové služby nedostatečné. Časové metody jako Time of Arrival (TOA) vyžadovaly velmi přesnou synchronizaci všech základnových stanic, což bylo nákladné. E-OTD tento problém vyřešil použitím přístupu založeného na měření v mobilu, který mohl pracovat s existující, méně těsně synchronizovanou sítí BTS aktivním měřením a kompenzací Real Time Differences. Představoval významný vývoj oproti síťové TOA, přenášel výpočetní složitost na koncové zařízení a umožňoval škálovatelnější a přesnější určování polohy bez nutnosti kompletní rekonstrukce sítě. Jeho vznik motivoval rostoucí poptávka po aplikacích využívajících polohu a přísné požadavky na veřejnou bezpečnost.

## Klíčové vlastnosti

- Výpočet polohy s asistencí sítě, ale prováděný v mobilním zařízení
- Používá hyperbolickou trilateraci založenou na naměřených časových rozdílech příjmu signálů
- Vyžaduje měření z minimálně tří základnových stanic
- Využívá jednotky Location Measurement Unit (LMU) pro kalibraci Real Time Differences (RTD)
- Poskytuje přesnost typicky v rozsahu 50–200 metrů za dobrých podmínek
- Funguje nezávisle na satelitních navigačních systémech (např. GPS)

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [E-OTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-otd/)
