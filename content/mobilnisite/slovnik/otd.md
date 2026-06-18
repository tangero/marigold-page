---
slug: "otd"
url: "/mobilnisite/slovnik/otd/"
type: "slovnik"
title: "OTD – Observed Time Difference"
date: 2025-01-01
abbr: "OTD"
fullName: "Observed Time Difference"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/otd/"
summary: "Měření rozdílu v době příchodu signálů z různých základnových stanic, které provádí mobilní zařízení nebo síť. Je to základní měření používané v metodách určování polohy v mobilních sítích, jako je Ob"
---

OTD je základní měření, které provádí mobilní zařízení nebo síť, a představuje rozdíl v době příchodu signálů z různých základnových stanic. Používá se pro určování polohy v mobilních sítích.

## Popis

Observed Time Difference (OTD) je základní měření v mobilních rádiových sítích, které představuje rozdíl v čase příjmu downlink rádiových signálů ze dvou různých vysílačů buněk, měřený přijímačem (typicky uživatelským zařízením – UE). Je to klíčový parametr pro síťové a UE-asistované techniky určování polohy. Měření OTD není absolutní čas, ale relativní rozdíl, což eliminuje potřebu, aby měřící zařízení mělo dokonale synchronizované hodiny, protože společná chyba hodin se při výpočtu rozdílu vyruší.

V praxi pro účely určování polohy, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), měří UE OTD mezi referenční buňkou (obvykle obsluhující buňkou) a několika sousedními buňkami. Konkrétně měří Reference Signal Time Difference ([RSTD](/mobilnisite/slovnik/rstd/)), což je relativní časový rozdíl mezi okamžikem příjmu downlink positioning referenčního signálu ([PRS](/mobilnisite/slovnik/prs/)) ze sousední buňky a okamžikem příjmu PRS z referenční buňky. Síť poskytuje UE pomocná data, včetně identit a konfigurací PRS buněk, které má měřit, a jejich známých geografických poloh a přesných časů vysílání. UE naměřené hodnoty RSTD reportuje zpět síti.

Polohovací server v síti (např. Evolved Serving Mobile Location Centre – [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE nebo Location Management Function – [LMF](/mobilnisite/slovnik/lmf/) v 5G) tyto reportované OTD/RSTD měření využívá. Protože doba šíření signálu je úměrná vzdálenosti, každé měření OTD definuje hyperbolickou polohovou čáru (LOP), na které se UE musí nacházet. Průnik více takových hyperbolických LOP, odvozených z OTD měření s alespoň třemi geograficky rozptýlenými základnovými stanicemi, poskytuje odhad polohy UE. Přesnost určení polohy závisí na faktorech, jako je geometrie základnových stanic, přesnost měření OTD a přesnost synchronizace mezi vysílajícími základnovými stanicemi.

## K čemu slouží

Určování polohy založené na OTD bylo vyvinuto pro splnění regulatorních, komerčních a bezpečnostních požadavků na lokalizaci mobilních zařízení, zejména tam, kde nejsou dostupné signály globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)) (např. uvnitř budov nebo v městských kaňonech). Rané metody určování polohy v mobilních sítích, jako je Cell-ID, poskytovaly velmi hrubou přesnost (poloměr buňky) a techniky Angle of Arrival (AoA) vyžadovaly složitá anténní pole. Metody založené na OTD nabídly rozumný kompromis mezi přijatelnou přesností (desítky až stovky metrů) a využitím stávající síťové infrastruktury s relativně skromnými úpravami na straně UE a sítě.

Hlavní problém, který OTD řeší, je umožnění síťového určování polohy bez nutnosti úprav hardwaru UE pro specializovanou lokalizační technologii (jako byly rané GNSS). Využívá přesné časové synchronizace, která je již v mobilních sítích vyžadována (např. pomocí [GPS](/mobilnisite/slovnik/gps/) nebo [IEEE](/mobilnisite/slovnik/ieee/) 1588 pro základnové stanice), a přeměňuje tak síť samotnou na rozsáhlý lokalizační systém. To bylo klíčové pro plnění mandátů určení polohy u nouzových volání (např. E911 v USA) pro všechn mobilní zařízení. Dále OTD poskytuje záložní nebo hybridní zdroj polohy, který může asistovat nebo urychlit určení polohy pomocí GNSS tím, že poskytne počáteční hrubou polohu, nebo může pracovat společně s GNSS pro lepší odolnost a přesnost v náročném rádiovém prostředí.

## Klíčové vlastnosti

- Relativní měření časového rozdílu, které eliminuje společnou chybu hodin přijímače
- Základ pro metody určování polohy OTDOA a UTDOA (Uplink TDOA) ve standardech 3GPP
- Využívá downlink referenční signály (např. PRS v LTE/NR, CPICH v UMTS) speciálně navržené pro přesné časové měření
- Vyžaduje poskytnutí síťových pomocných dat pro UE pro efektivní měření (ID buněk, konfigurace PRS)
- Umožňuje hyperbolické určování polohy pomocí multilaterace při kombinaci měření z více buněk
- Výkon závisí na přesnosti synchronizace základnových stanic a na hustotě/geometrii rozmístění buněk

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 37.803** (Rel-11) — H(e)NB Mobility Enhancements Study

---

📖 **Anglický originál a plná specifikace:** [OTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/otd/)
