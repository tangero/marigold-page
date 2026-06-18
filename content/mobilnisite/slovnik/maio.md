---
slug: "maio"
url: "/mobilnisite/slovnik/maio/"
type: "slovnik"
title: "MAIO – Mobile Allocation Index Offset"
date: 2025-01-01
abbr: "MAIO"
fullName: "Mobile Allocation Index Offset"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/maio/"
summary: "Parametr v GSM, který definuje specifický odstup časového slotu ve skupině frekvencí (Mobile Allocation), používaný k přiřazení vyhrazeného kanálu pro přenos hovoru mobilní stanici. Je klíčovou součás"
---

MAIO je parametr GSM, který definuje specifický odstup časového slotu ve skupině frekvencí pro přiřazení kanálu pro přenos hovoru, což umožňuje přeskakování kmitočtů (Frequency Hopping) ke snížení rušení a útlumu.

## Popis

Mobile Allocation Index Offset (MAIO) je základní parametr ve fyzické vrstvě GSM, konkrétně v rámci rámce přiřazování kanálů a přeskakování kmitočtů. Funguje ve spojení s Mobile Allocation ([MA](/mobilnisite/slovnik/ma/)), což je seznam rádiových kmitočtových kanálů přiřazených buňce, a Hopping Sequence Number ([HSN](/mobilnisite/slovnik/hsn/)), který definuje pseudonáhodný vzor přeskakování. Když je kanál pro přenos hovoru ([TCH](/mobilnisite/slovnik/tch/)) přidělen mobilní stanici, je jí přiřazena konkrétní hodnota MAIO. Tato hodnota MAIO, v rozsahu od 0 do N-1 (kde N je počet kmitočtů v seznamu MA), určuje výchozí odstup mobilní stanice v rámci sekvence přeskakování.

Funguje to následovně: Systém použije číslo rámce ([FN](/mobilnisite/slovnik/fn/)) a HSN ke generování pseudonáhodné sekvence indexů. Pro každý [TDMA](/mobilnisite/slovnik/tdma/) rámec tento algoritmus vytvoří index. Mobilní stanice poté vypočítá svůj skutečný kmitočet pro daný rámec tak, že vezme tento index, přičte svou přiřazenou hodnotu MAIO (modulo N) a výsledek namapuje na konkrétní kmitočet v seznamu MA. Zásadní je, že v rámci stejné buňky a při použití stejného HSN musí být různým mobilním stanicím přiřazeny různé hodnoty MAIO. To zajišťuje, že jsou vysílány na různých kmitočtech v jakémkoli daném časovém slotu, čímž se implementuje forma ortogonálního přeskakování kmitočtů a zabrání se společnému kanálovému rušení mezi uživateli ve stejné buňce.

Správu MAIO provádí řadič základnové stanice ([BSC](/mobilnisite/slovnik/bsc/)) jako součást procedury přiřazování kanálu. Při sestavování hovoru nebo během předávání spojení algoritmus správy rádiových zdrojů BSC vybere dostupný časový slot a vhodnou hodnotu MAIO z fondu pro danou buňku a sekvenci přeskakování. Zvolená hodnota MAIO a seznam MA jsou sděleny mobilní stanici ve zprávě IMMEDIATE ASSIGNMENT nebo HANDOVER COMMAND. Tato přesná koordinace umožňuje GSM využívat výhod rozmanitosti kmitočtů a průměrování rušení díky přeskakování kmitočtů, což je klíčové pro zlepšení kvality hovoru a kapacity systému, zejména v prostředích omezených rušením.

## K čemu slouží

MAIO byl vytvořen jako nedílná součást řešení přeskakování kmitočtů v GSM pro potírání dvou hlavních problémů šíření rádiového signálu: kmitočtově selektivního útlumu a společného kanálového rušení. V systému bez přeskakování by mobilní stanice uvízlá na kanálu s hlubokým útlumem nebo vysokým rušením trpěla špatnou kvalitou po celou dobu hovoru. Pevné přiřazení kanálů také vede k předvídatelným a trvalým vzorům rušení mezi buňkami, které znovu používají stejný kmitočet.

Přeskakování kmitočtů, umožněné parametry jako MAIO, [HSN](/mobilnisite/slovnik/hsn/) a [MA](/mobilnisite/slovnik/ma/), bylo zavedeno, aby tyto efekty randomizovalo. Tím, že přenos mobilní stanice 'přeskakuje' různé kmitočty, útlum nebo záchvat rušení na jednom kmitočtu ovlivní pouze jeden rámec a korekční kódování chyb to může napravit. Parametr MAIO konkrétně řeší problém koordinace více uživatelů v rámci stejné buňky. Přiřazením jedinečných hodnot MAIO systém zajišťuje, že dvě mobilní stanice ve stejné buňce a časovém slotu nikdy nepoužívají současně stejný kmitočet, čímž se eliminuje vnitrobuněčné společné kanálové rušení. To umožňuje těsnější vzory opakovaného využití kmitočtů, čímž se zvyšuje kapacita sítě. Bez MAIO pro ortogonální oddělení uživatelů by výhody přeskakování byly ztraceny kvůli kolizím uživatelů na stejném kmitočtu pro přeskakování.

## Klíčové vlastnosti

- Definuje jedinečný odstup uživatele v rámci sekvence přeskakování kmitočtů.
- Hodnota je v rozsahu od 0 do (počet kmitočtů pro přeskakování - 1).
- Přiřazuje ho BSC během přiřazování kanálu nebo předávání spojení.
- Zajišťuje ortogonalitu mezi uživateli ve stejné buňce používající stejný HSN.
- Kritický pro implementaci základního pásmového přeskakování kmitočtů (Baseband Frequency Hopping) v GSM.
- Sděleno MS prostřednictvím příkazů pro přiřazení nebo předání spojení.

## Související pojmy

- [HSN – Hopping Sequence Number](/mobilnisite/slovnik/hsn/)
- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [MAIO na 3GPP Explorer](https://3gpp-explorer.com/glossary/maio/)
