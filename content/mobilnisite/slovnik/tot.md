---
slug: "tot"
url: "/mobilnisite/slovnik/tot/"
type: "slovnik"
title: "TOT – Time Offset Table"
date: 2025-01-01
abbr: "TOT"
fullName: "Time Offset Table"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tot/"
summary: "Tabulka časového posunu (TOT) je datová struktura definovaná v 3GPP pro polohovací služby, zejména pro metody určování polohy založené na UE. Poskytuje informace o časové korekci, například rozdíl mez"
---

TOT je datová struktura pro polohovací služby, která poskytuje informace o časové korekci, například rozdíl mezi systémovým časem GNSS a časem mobilní sítě, aby umožnila přesnější a rychlejší určení polohy.

## Popis

Tabulka časového posunu (TOT) je standardizovaná datová struktura specifikovaná v 3GPP TS 26.917 pro služby určování polohy. Je klíčovou součástí podpory určování polohy založeného na UE, kde uživatelské zařízení samo vypočítává svou polohu, často za použití signálů globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)), jako je [GPS](/mobilnisite/slovnik/gps/) nebo Galileo. Hlavní funkcí TOT je poskytovat přesné informace o časovém posunu. Tyto informace typicky popisují vztah mezi časovou stupnicí konstelace GNSS (např. systémový čas GPS) a univerzálním referenčním časem, jako je koordinovaný světový čas ([UTC](/mobilnisite/slovnik/utc/)), nebo potenciálně systémovým časem mobilní sítě. Tabulka obsahuje záznamy s parametry, jako je referenční čas (např. konkrétní týden GNSS a čas v týdnu), odpovídající hodnota posunu a často i rychlost změny tohoto posunu (drift).

Z architektonického hlediska je TOT doručena do UE jako pomocná data, typicky z polohového serveru, jako je Secure User Plane Location ([SUPL](/mobilnisite/slovnik/supl/)) Location Platform ([SLP](/mobilnisite/slovnik/slp/)) nebo server LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)). Toto doručení může proběhnout prostřednictvím protokolů řídicí roviny (např. LPP v LTE/5G) nebo protokolů uživatelské roviny (např. prostřednictvím SUPL). UE tuto tabulku přijme a uloží. Když UE provádí určení polohy založené na GNSS, používá satelitní signály, které jsou časově označeny ve vlastním systémovém čase GNSS. Pro výpočet přesné polohy v univerzálním souřadnicovém systému musí UE tyto časové značky převést na společný časový referenční bod. TOT poskytuje potřebné parametry pro tento převod.

Při provozu přijímač GNSS v UE měří pseudovzdálenosti k více satelitům. Tato měření jsou inherentně zatížena odchylkou způsobenou posunem mezi lokálním hodinovým signálem UE a systémovým časem GNSS. Aplikací korekcí z TOT může UE přesněji zarovnat svá měření na známý časový referenční bod, čímž se sníží časově závislé neznámé v polohovacích rovnicích. To přímo zlepšuje čas do prvního určení polohy ([TTFF](/mobilnisite/slovnik/ttff/)) a přesnost vypočítané polohy, zejména při studeném nebo teplém startu, kdy má UE omezené předchozí znalosti. TOT je součástí sady pomocných dat definovaných 3GPP a spolupracuje s dalšími daty, jako jsou efemeridové a almanachové modely, aby umožnila efektivní a vysoce výkonné určování polohy pro širokou škálu služeb od nouzových volání po aplikace založené na poloze.

## K čemu slouží

TOT byla zavedena, aby řešila potřebu rychlejšího a přesnějšího určování polohy založeného na UE v mobilních sítích. Před standardizovanými pomocnými daty, jako je TOT, mohlo být určování polohy UE založené na [GNSS](/mobilnisite/slovnik/gnss/) pomalé, zejména při studeném startu, protože UE potřebovala stáhnout úplná efemeridová data ze samotných satelitů, což je proces trvající desítky sekund. Mohlo být také méně přesné, pokud měl vnitřní hodinový signál UE významný drift vzhledem k času GNSS, což do výpočtu polohy zavádělo chyby.

Vytvoření TOT, zejména v kontextu vylepšení služeb určování polohy (LCS) v 3GPP, bylo motivováno požadavky služeb pro nouzové služby (E911/E112), komerční služby založené na poloze (LBS) a regulačními požadavky. Poskytnutím předem vypočítaných časových korekcí odvozených ze sítě umožňuje TOT, aby UE rychleji vyřešila časové nejistoty. To snižuje počet neznámých proměnných, které musí UE řešit, což vede k rychlejší konvergenci na určení polohy (zlepšený TTFF) a zvýšené přesnosti díky zmírnění chyb z hodinové odchylky. Řeší problém, že by si UE musela tento časový vztah odvodit nezávisle, což je výpočetně náročné a časově zdlouhavé.

Historicky, jak 3GPP vyvíjelo svou polohovací architekturu od metod založených na síti (jako Cell-ID a OTDOA) k sofistikovanějším metodám založeným na UE a asistovaným UE, se poskytování standardizovaných pomocných dat stalo klíčovým. TOT, zavedená ve vydání 14, byla součástí tohoto širšího úsilí o optimalizaci výkonu určování polohy, snížení spotřeby energie UE (zkrácením doby aktivního příjmu GNSS) a splnění stále přísnějších požadavků na přesnost a latenci pro nové případy užití, včetně těch, které se objevují v éře 5G pro IoT a vertikální aplikace.

## Klíčové vlastnosti

- Poskytuje parametry pro převod mezi systémovým časem GNSS a UTC nebo síťovým časem
- Doručována jako součást standardizovaných pomocných dat pro určování polohy (např. prostřednictvím LPP nebo SUPL)
- Obsahuje referenční časové body a odpovídající hodnoty posunu, často i s rychlostmi driftu
- Umožňuje rychlejší čas do prvního určení polohy (TTFF) pro určování polohy UE založené na GNSS
- Zlepšuje přesnost určení polohy korekcí známých odchylek časového referenčního bodu
- Podporuje více konstelací GNSS (GPS, Galileo atd.) prostřednictvím standardizovaných formátů

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [TTFF – Time To First Fix](/mobilnisite/slovnik/ttff/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [TOT na 3GPP Explorer](https://3gpp-explorer.com/glossary/tot/)
