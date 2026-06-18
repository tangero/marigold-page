---
slug: "wls"
url: "/mobilnisite/slovnik/wls/"
type: "slovnik"
title: "WLS – Weighted Least Squares"
date: 2025-01-01
abbr: "WLS"
fullName: "Weighted Least Squares"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/wls/"
summary: "WLS je statistický odhadovací algoritmus používaný v mobilní lokalizaci pro výpočet polohy UE. Zpracovává naměřené parametry signálu (jako časování nebo sílu signálu) z více základnových stanic a váží"
---

WLS je statistický lokalizační algoritmus, který vypočítává polohu UE zpracováním a vážením měření signálu z více základnových stanic na základě jejich odhadované přesnosti.

## Popis

Weighted Least Squares (WLS) je základní matematická optimalizační technika používaná v rádiových přístupových sítích 3GPP pro mobilní lokalizaci. Jedná se o vylepšení standardního odhadu metodou nejmenších čtverců ([LS](/mobilnisite/slovnik/ls/)), navržené k řešení přeurčených soustav rovnic, kde cílem je odhadnout neznámé parametry – v tomto kontextu zeměpisné souřadnice (x, y a případně z) uživatelského zařízení (UE). Soustava rovnic je sestavena z geometrických vztahů založených na měřeních, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), Round Trip Time ([RTT](/mobilnisite/slovnik/rtt/)) nebo Angle of Arrival (AoA), pořízených mezi UE a více sousedními základnovými stanicemi (eNodeB/gNB) nebo naopak.

Algoritmus funguje tak, že formuluje cenovou funkci představující součet čtverců rozdílů mezi naměřenými parametry signálu (např. časovými rozdíly) a parametry predikovanými odhadem kandidátní polohy. Klíčovou inovací WLS oproti standardní LS je zavedení váhové matice. Tato matice přiřazuje různou váhu každé měřicí rovnici na základě odhadované spolehlivosti nebo rozptylu daného konkrétního měření. Měření s vyšší odhadovanou přesností (např. z bližší základnové stanice nebo se spojem přímé viditelnosti) mají větší váhu, zatímco měření s vyšší nejistotou (např. ze vzdálenější nebo silně zastíněné cesty) mají na konečné řešení menší vliv. Toto vážení je zásadní v reálných rádiových prostředích, kde chyby měření nejsou jednotné a jsou často korelované.

V architektuře 3GPP je algoritmus WLS typicky implementován v lokalizačním serveru (např. Evolved Serving Mobile Location Center - [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE nebo Location Management Function - [LMF](/mobilnisite/slovnik/lmf/) v 5G). Server shromažďuje hlášení o měřeních od UE a/nebo sítě, aplikuje algoritmus WLS (často iterativním způsobem pro zpracování nelineárních rovnic) a vypočítává konečný odhad polohy. Jeho role je ústřední pro síťové, UE-asistované a UE-bázované lokalizační metody definované napříč 2G, 3G, 4G a 5G. Poskytnutím robustního statistického rámce pro zmírnění chyb měření umožňuje WLS síti dosáhnout cílů přesnosti polohy vyžadovaných pro komerční služby (jako je navigace) a regulatorní nařízení (jako je lokalizace nouzových volajících).

## K čemu slouží

Algoritmus WLS byl do standardů 3GPP začleněn, aby řešil inherentní nepřesnosti a zkreslení přítomné v měřeních rádiového signálu používaných pro lokalizaci. Jednoduchá trilaterace nebo nevážené metody nejmenších čtverců předpokládají, že všechna měření mají stejné a nekorelované chyby, což je ve složitých městských nebo vnitřních rádiových prostředích kvůli mnohocestnému šíření, šíření bez přímé viditelnosti ([NLOS](/mobilnisite/slovnik/nlos/)) a různorodé kvalitě přijímače zřídka pravda. Tyto nepřesnosti vedou k významným lokalizačním chybám, což činí základní lokalizační metody nedostatečnými pro kritické aplikace.

Účelem WLS je statisticky optimalizovat odhad polohy tím, že bere v úvahu a kompenzuje různou kvalitu vstupních dat. Jeho vznik byl motivován potřebou splnit stále přísnější požadavky na přesnost pro nouzové služby (např. E-911 v USA) a rostoucím trhem pro lokalizační služby. Vážením měření podle jejich odhadované kovariance poskytuje WLS odhad maximální věrohodnosti za předpokladu Gaussovských chyb, což vede k přesnější a spolehlivější lokalizaci než u nevážených metod. Řeší problém, jak nejlépe kombinovat nedokonalá, heterogenní měření z více zdrojů (buněk) k vytvoření jediné, optimální souřadnice polohy, což je základní výzva v bezdrátové geolokalizaci.

## Klíčové vlastnosti

- Odhaduje polohu UE řešením přeurčené soustavy geometrických rovnic
- Zahrnuje váhovou matici pro zohlednění různých přesností měření
- Poskytuje řešení maximální věrohodnosti za předpokladu Gaussovských chyb
- Používá se pro lokalizační metody jako OTDOA, ECID a multi-RTT
- Implementován v síťových lokalizačních serverech (E-SMLC, LMF) pro centralizovaný výpočet
- Podporuje iterativní výpočet pro zpracování nelineárních měřicích modelů

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS

---

📖 **Anglický originál a plná specifikace:** [WLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/wls/)
