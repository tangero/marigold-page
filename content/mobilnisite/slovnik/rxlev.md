---
slug: "rxlev"
url: "/mobilnisite/slovnik/rxlev/"
type: "slovnik"
title: "RXLEV – Received Signal Level"
date: 2025-01-01
abbr: "RXLEV"
fullName: "Received Signal Level"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/rxlev/"
summary: "RXLEV je základní rádiové měření představující průměrnou úroveň přijímaného výkonu signálu. Je klíčové pro výběr buňky, rozhodování o předání spojení a správu rádiových prostředků v systémech GSM a od"
---

RXLEV je základní rádiové měření představující průměrnou úroveň přijímaného signálu, používané pro výběr buňky a rozhodování o předání spojení v sítích GSM a v odvozených mobilních sítích.

## Popis

Received Signal Level (RXLEV, úroveň přijímaného signálu) je klíčový parametr rádiového měření definovaný v systému GSM a přejatý do specifikací 3GPP. Kvantifikuje průměrný výkon přijímaného rádiového signálu, obvykle měřený v dBm, za stanovené měřící období. V architektuře sítě měří RXLEV mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) na downlinkových vysílacích kanálech, například na Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) z obsluhující a sousedních buněk, a základnová stanice ([BTS](/mobilnisite/slovnik/bts/)) na uplinku od MS. Měření se provádí na rádiovém kmitočtovém nosiči, často za použití filtru průměrujícího výkon pro potlačení vlivu rychlého úniku a získání stabilní hodnoty reprezentativní pro útlum na trase a rozlehlé stínování.

Procedura měření je pevně integrována do protokolového zásobníku GSM, konkrétně ve vrstvě správy rádiových prostředků ([RR](/mobilnisite/slovnik/rr/)). MS průběžně měří a hlásí hodnoty RXLEV síti. Tyto surové hodnoty se mapují na celočíselný index (RXLEV 0-63) pokrývající definovaný rozsah výkonu (např. -110 dBm až -48 dBm v GSM). Právě tato indexovaná hodnota se typicky uvádí v hlášeních o měření. Řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) sítě používá tato hlášení společně s dalšími parametry, jako je [RXQUAL](/mobilnisite/slovnik/rxqual/), k provádění klíčových funkcí správy rádiových prostředků.

Role RXLEV je zásadní pro udržení síťové konektivity a kvality. Je hlavním vstupem pro algoritmy výběru buňky (kritérium C1) a převýběru buňky, když je MS v režimu nečinnosti. V přenosovém režimu je klíčovým determinantem pro rozhodování o předání spojení; předání může být spuštěno, pokud RXLEV ze sousední buňky převyšuje RXLEV obsluhující buňky o určitou hysterezi. Dále se používá v algoritmech řízení výkonu, kde BSC nařizuje MS nebo BTS upravit svůj vysílací výkon, aby byla na přijímači zachována dostatečná úroveň RXLEV při minimalizaci rušení. RXLEV je tedy základní metrikou pro optimalizaci pokrytí, snížení rušení a celkovou stabilitu sítě.

## K čemu slouží

RXLEV byl vytvořen jako základní stavební kámen pro automatizované řízení buněčné sítě. Rané systémy mobilní rádiové komunikace vyžadovaly ruční ladění a nabízely omezenou mobilitu. Digitální systém GSM zavedl potřebu autonomní, sítí řízené mobility (předání spojení) a efektivního využívání prostředků. RXLEV poskytuje nezbytnou, kvantifikovatelnou metriku pro otázku "jak silný je signál", což je prvotní determinant toho, zda může mobil spolehlivě komunikovat se základnovou stanicí.

Řeší problém, jak umožnit mobilnímu zařízení automaticky vybrat nejlepší buňku pro připojení a jak při hovoru přenést spojení plynule do silnější buňky při pohybu uživatele. Před zavedením takových standardizovaných měření bylo udržení hovoru za pohybu velmi obtížné. RXLEV v kombinaci s [RXQUAL](/mobilnisite/slovnik/rxqual/) umožňuje síti činit informovaná rozhodnutí a vyvažovat cíle silného pokrytí signálem (pomocí RXLEV) a dobré integrity signálu (pomocí RXQUAL). Jeho vytvoření bylo motivováno potřebou jednoduchého, robustního a všeobecně implementovaného měření, které by pohánělo algoritmy pro výběr buňky, předání spojení a řízení výkonu – tedy základní funkce umožňující široce rozšířenou buněčnou mobilitu.

## Klíčové vlastnosti

- Měří průměrný přijímaný výkon RF nosiče v dBm
- Hlášen jako celočíselný index (např. 0–63) v normalizovaném rozsahu
- Měřen jak MS (downlink), tak BTS (uplink)
- Primární vstup pro výběr a převýběr buňky (kritéria C1/C2)
- Klíčový parametr pro rozhodování o předání spojení řízeném sítí
- Používá se jako vstup pro algoritmy řízení výkonu na uplinku a downlinku

## Související pojmy

- [RXQUAL – Received Signal Quality](/mobilnisite/slovnik/rxqual/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [RXLEV na 3GPP Explorer](https://3gpp-explorer.com/glossary/rxlev/)
