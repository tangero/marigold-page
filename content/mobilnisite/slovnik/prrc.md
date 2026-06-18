---
slug: "prrc"
url: "/mobilnisite/slovnik/prrc/"
type: "slovnik"
title: "PRRC – Pseudo-Range Rate Correction"
date: 2025-01-01
abbr: "PRRC"
fullName: "Pseudo-Range Rate Correction"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/prrc/"
summary: "Korekční parametr používaný v metodách určování polohy UE, konkrétně pro metodu OTDOA (Observed Time Difference of Arrival). Zlepšuje přesnost lokalizace zohledněním relativní rychlosti mezi UE a refe"
---

PRRC je korekční parametr používaný v určování polohy metodou OTDOA ke zlepšení přesnosti lokalizace zohledněním relativní rychlosti mezi UE a referenčními základnovými stanicemi a zpřesněním měření rychlosti změny pseudodosahu.

## Popis

Pseudo-Range Rate Correction (PRRC) je technický parametr definovaný v dokumentu 3GPP TS 25.305 pro určování polohy uživatelského zařízení (UE) v síti UMTS (a relevantní i pro pozdější technologie). Používá se v metodách určování polohy založených na měření časování signálu, nejvýznamněji v technice [OTDOA](/mobilnisite/slovnik/otdoa/) (Observed Time Difference of Arrival). Termín „pseudo-range rate“ označuje rychlost změny pseudodosahu, což je zdánlivá vzdálenost mezi UE a základnovou stanicí (Node B), odvozená z doby šíření signálu a zkreslená driftem hodin a dalšími chybami. Hodnota PRRC představuje korekci aplikovanou na tuto změřenou rychlost, která kompenzuje chyby vyvolané relativním pohybem (Dopplerův jev) a nepřesnostmi časování mezi UE a vysílající buňkou.

V architektuře určování polohy OTDOA měří UE rozdíl v čase příchodu referenčního signálu ([RSTD](/mobilnisite/slovnik/rstd/)) mezi signály přijatými z více sousedních základnových stanic. Poloha se vypočítá multilaterací pomocí těchto časových rozdílů. Pokud se však UE nebo základnová stanice pohybuje, dochází kvůli Dopplerovu jevu k posunu pozorované frekvence signálu, což ovlivňuje vnímané časování a tedy i výpočet pseudodosahu. Parametr PRRC, který může být síťou poskytnut pomocí asistenčních dat (např. v rámci protokolu LTE Positioning Protocol – [LPP](/mobilnisite/slovnik/lpp/)), umožňuje UE upravit svá měření. Síť PRRC vypočítává na základě známých nebo odhadovaných vektorů rychlosti UE (např. z předchozích lokalizací nebo síťového sledování) a geografických poloh buněk.

Aplikace PRRC spočívá v integraci této korekce do výpočetních algoritmů pro určování polohy v UE. Aplikací PRRC UE efektivně snižuje chybu měření rychlosti změny pseudodosahu, což vede k přesnějšímu odhadu skutečných časových rozdílů a následně k přesnější geografické lokalizaci. To je zvláště důležité pro určování polohy pohybujících se UE, jako jsou zařízení ve vozidlech, kde by nekompenzovaný Dopplerův jev mohl významně snížit přesnost. Tento parametr je součástí souboru asistenčních dat, která síť může poskytnout pro vylepšení režimů určování polohy realizovaných UE nebo s asistencí UE, a funguje ve spojení s dalšími korekcemi, jako jsou časové posuny (timing advances) nebo efemeridy pro satelitní metody, když je používáno i [A-GNSS](/mobilnisite/slovnik/a-gnss/).

## K čemu slouží

PRRC byl vyvinut pro řešení konkrétního zdroje chyb v určování polohy založeném na mobilních sítích: vlivu relativního pohybu na měření časování. Rané metody určování polohy, jako Cell-ID nebo základní [OTDOA](/mobilnisite/slovnik/otdoa/), poskytovaly omezenou přesnost, zejména pro mobilní uživatele, protože nedostatečně zohledňovaly Dopplerův posun a další dynamické efekty měnící charakteristiky šíření signálu. Jak služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)) a regulatorní požadavky (např. E911) začaly vyžadovat vyšší přesnost, staly se nezbytnými sofistikovanější korekční mechanismy.

Vytvoření PRRC bylo motivováno potřebou zlepšit výkon OTDOA v reálných, nestatických scénářích. Bez takových korekcí by měření rychlosti změny pseudodosahu obsahovala chyby úměrné relativní radiální rychlosti, což by vedlo k nepřesným lokalizacím pohybujících se UE. Poskytnutím korekce vypočítané sítí může systém tyto chyby zmírnit a umožnit tak spolehlivější a přesnější určování polohy pro navigaci, nouzové služby a komerční aplikace. Představuje evoluci od jednoduché geometrické trilaterace k dynamičtějšímu modelu určování polohy, který bere v potaz fyzikální jevy.

Představen v kontextu UMTS (Release 12, TS 25.305), koncept poskytování korekcí rychlosti položil základy pro vylepšené funkce určování polohy v LTE a 5G NR. Vyřešil omezení algoritmů určování polohy, které předpokládaly statické nebo pomalu se pohybující cíle, a umožnil mobilním sítím lépe konkurovat a doplňovat satelitní navigační systémy v náročném prostředí, jako jsou městské kaňony nebo vnitřní prostory, kde je dynamika signálů složitá a rychle se mění.

## Klíčové vlastnosti

- Opravuje měření rychlosti změny pseudodosahu pro chyby způsobené Dopplerovým jevem a nepřesnostmi časování.
- Používá se primárně v metodě určování polohy OTDOA.
- Poskytován UE jako součást síťových asistenčních dat pro určování polohy.
- Zlepšuje přesnost lokalizace pro pohybující se uživatelská zařízení (UE).
- Integruje se s protokoly pro určování polohy, jako je LPP.
- Vychází ze známých nebo odhadovaných rychlostí UE a základnových stanic.

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [RSTD – Reference Signal Time Difference](/mobilnisite/slovnik/rstd/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [PRRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/prrc/)
