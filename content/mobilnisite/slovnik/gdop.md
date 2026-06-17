---
slug: "gdop"
url: "/mobilnisite/slovnik/gdop/"
type: "slovnik"
title: "GDOP – Geometric Dilution of Precision"
date: 2025-01-01
abbr: "GDOP"
fullName: "Geometric Dilution of Precision"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gdop/"
summary: "GDOP je metrika používaná v satelitních polohovacích systémech (jako GPS) a v polohování UE podle 3GPP pro kvantifikaci vlivu geometrie satelitů/vysílačů na přesnost vypočtené polohy. Nižší hodnota GD"
---

GDOP je metrika, která kvantifikuje, jak geometrické uspořádání satelitů nebo základnových stanic ovlivňuje přesnost vypočtené polohy, přičemž nižší hodnota značí vyšší přesnost polohy.

## Popis

Geometric Dilution of Precision (GDOP) je bezrozměrný kvalitativní faktor, který kvantifikuje, jak prostorová geometrie mezi uživatelským zařízením (UE) a referenčními body pro polohování (např. satelity [GNSS](/mobilnisite/slovnik/gnss/) nebo pozemní základnové stanice) ovlivňuje nejistotu vypočtené polohy. Jde o multiplikativní faktor; celková polohová chyba je přibližně rovna součinu měřicí chyby (např. chyby časování nebo měření vzdálenosti) a hodnoty GDOP. Proto i při přesných jednotlivých měřeních může nepříznivá geometrie (vysoký GDOP) výrazně zhoršit konečnou přesnost polohy. GDOP je odvozen z kovarianční matice řešení polohy, která je sama funkcí geometrické matice (nebo návrhové matice) tvořené jednotkovými vektory od UE ke každému referenčnímu bodu.

Výpočet GDOP je založen na lineární algebře a teorii odhadu, konkrétně na metodě nejmenších čtverců používané k řešení souřadnic UE (a často i časového posunu). Geometrická matice, označovaná jako H, obsahuje směrové kosiny od UE ke každému viditelnému satelitu nebo základnové stanici. Kovarianční matice odhadovaných chyb je úměrná matici (H^T * H)^{-1}. GDOP je definován jako druhá odmocnina stopy této kovarianční matice (součet rozptylů odhadovaných parametrů). Nižší hodnoty GDOP vznikají, když jsou referenční body široce rozptýleny po obloze vzhledem k UE, což poskytuje různorodé přímky výhledu. Naopak, pokud jsou všechny referenční body shluknuty v malé části oblohy, jsou přímky výhledu téměř rovnoběžné, což ztěžuje přesné určení polohy uživatele a vede k vysokému GDOP.

V kontextu 3GPP je GDOP zvláště relevantní pro metody polohování UE definované v technických specifikacích, jako je TS 25.305 pro UTRA a TS 36.355 pro LTE. Ačkoli je často spojován s polohováním pomocí globálních navigačních satelitních systémů (GNSS), koncept se vztahuje i na pozemní metody, jako je Observed Time Difference Of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) v LTE, kde referenčními body jsou sousední základnové stanice (eNodeB). U OTDOA může polohovací server ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) nebo UE vypočítat GDOP na základě známých poloh měřených eNodeB, aby vyhodnotil očekávanou kvalitu polohového údaje před jeho nahlášením. Vysoký GDOP může vyvolat snahu systému získat další měření nebo použít alternativní metodu polohování. GDOP tedy slouží jako interní kontrola kvality v rámci polohovacích algoritmů, informuje o rozhodnutích a poskytuje kontext pro nahlášenou nejistotu polohy, což je zásadní pro aplikace vyžadující vysokou spolehlivost, jako jsou tísňové služby (E911/E112).

## K čemu slouží

GDOP existuje proto, aby poskytoval standardizovanou matematickou míru kvality geometrické konfigurace v jakémkoli polohovacím systému založeném na multilateraci. Základní problém, který řeší, spočívá v tom, že přesnost vypočtené polohy není závislá pouze na přesnosti jednotlivých měření vzdálenosti (např. pseudovzdáleností v [GPS](/mobilnisite/slovnik/gps/)). Dvě sady měření se stejnými jednotlivými chybami mohou poskytnout polohové údaje s výrazně odlišnou přesností v závislosti na tom, jak jsou satelity nebo vysílače uspořádány na obloze vzhledem k přijímači. Bez GDOP by polohovací systém nebo aplikace neměly přímý způsob, jak posoudit tuto inherentní geometrickou náchylnost k chybám, což by mohlo vést k nevědomému použití vysoce nespolehlivých polohových dat.

Koncept vznikl a je ústřední pro satelitní navigační systémy jako GPS. Již v raném vývoji GPS bylo rozpoznáno, že geometrie satelitů je hlavním zdrojem chyb. GDOP poskytl jednoduchou metriku v podobě jediného čísla, kterou lze předpovědět na základě almanachových dat (budoucích poloh satelitů) a použít k výběru optimální sady satelitů pro přijímač, což je proces známý jako výběr satelitů. Toto zlepšuje jak přesnost, tak efektivitu zpracování. V pozemním buněčném polohování, které přijal 3GPP, platí stejný princip. U metod jako [OTDOA](/mobilnisite/slovnik/otdoa/) může být geometrie základnových stanic vůči UE velmi proměnná, zejména v městských kaňonech nebo venkovských oblastech s řídkým rozmístěním stanovišť. Výpočet GDOP umožňuje síti nebo UE pochopit omezení dostupné infrastruktury pro polohování.

Začleněním GDOP do polohovacích standardů umožňuje 3GPP inteligentnější a spolehlivější služby založené na poloze. Operátoři sítí a poskytovatelé polohových služeb mohou používat hodnoty GDOP k přiřazení úrovní spolehlivosti polohovým hlášením, rozhodovat o přechodu na jiné metody (např. z OTDOA na Cell-ID) nebo dokonce plánovat pokusy o polohování na časy, kdy se předpokládá lepší geometrie. Pro tísňové služby je nahlášení vysokého GDOP spolu s polohovým údajem klíčovou informací, která signalizuje, že poloha, byť nejlepší dostupná, může mít velkou elipsu chyb. GDOP tedy řeší problém kvantifikace jinak skrytého zdroje polohové chyby a umožňuje systémům a uživatelům činit informovaná rozhodnutí na základě kvality polohových dat.

## Klíčové vlastnosti

- Kvantifikuje multiplikativní vliv geometrie referenčních bodů na polohovou chybu
- Odvozeno z kovarianční matice řešení polohy metodou nejmenších čtverců
- Bezrozměrná skalární hodnota, kde nižší čísla značí lepší geometrii a vyšší potenciální přesnost
- Aplikovatelné jak na satelitní (GNSS), tak na pozemní (např. OTDOA) metody polohování
- Lze předem předpovědět pomocí známých efemerid nebo dat o polohách základnových stanic
- Používá se jako metrika kvality pro výběr optimálních referenčních bodů nebo spouštění záložních postupů

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [GDOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gdop/)
