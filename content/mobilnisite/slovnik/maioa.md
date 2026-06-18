---
slug: "maioa"
url: "/mobilnisite/slovnik/maioa/"
type: "slovnik"
title: "MAIOA – MAIO Allocation"
date: 2025-01-01
abbr: "MAIOA"
fullName: "MAIO Allocation"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/maioa/"
summary: "MAIO Allocation (přidělení MAIO) je parametr v sítích GSM/GPRS/EDGE, který přiřazuje mobilní stanici specifický posun indexu mobilní alokace (MAIO) pro přeskakování kmitočtu. Zajišťuje, aby více uživa"
---

MAIOA je parametr sítě GSM/GPRS/EDGE, který přiřazuje mobilní stanici specifický posun indexu mobilní alokace (Mobile Allocation Index Offset) pro koordinaci přeskakování kmitočtu mezi více uživateli na stejném časovém slotu, čímž snižuje interferenci.

## Popis

[MAIO](/mobilnisite/slovnik/maio/) Allocation (MAIOA) je klíčová součást mechanismu přeskakování kmitočtu definovaného ve specifikaci 3GPP TS 45.914 pro sítě GSM, [GPRS](/mobilnisite/slovnik/gprs/) a [EDGE](/mobilnisite/slovnik/edge/). Přeskakování kmitočtu je technika, při níž se kmitočet nosné rádiového přenosu periodicky mění podle předem dané posloupnosti. MAIO (Mobile Allocation Index Offset) je parametr, který určuje počáteční bod neboli posun v rámci této posloupnosti pro konkrétní mobilní stanici. MAIOA označuje proces nebo algoritmus, kterým síť přiřazuje jedinečnou hodnotu MAIO každé mobilní stanici pracující na daném časovém slotu a s danou posloupností přeskakování kmitočtu. Toto přiřazení typicky spravuje řadič základnové stanice ([BSC](/mobilnisite/slovnik/bsc/)) ve spolupráci s převodníkem základnové stanice ([BTS](/mobilnisite/slovnik/bts/)).

Architektura zahrnuje BSC, který přiděluje hodnoty MAIO na základě nakonfigurovaného čísla posloupnosti přeskakování ([HSN](/mobilnisite/slovnik/hsn/)) a dostupné sady kmitočtů (tzv. mobilní alokace, neboli seznam [MA](/mobilnisite/slovnik/ma/)). Když je mobilní stanici přidělen kanál pro přenos hovoru ([TCH](/mobilnisite/slovnik/tch/)) nebo paketový datový kanál (PDCH) využívající přeskakování kmitočtu, síť signalizuje hodnotu MAIO spolu s HSN a seznamem MA prostřednictvím zpráv o přiřazení kanálu. Hodnota MAIO je celé číslo v rozsahu od 0 do N-1, kde N je počet kmitočtů v seznamu MA. Každá mobilní stanice na stejném časovém slotu, ale s různými hodnotami MAIO, bude v každém TDMA rámci přeskakovat na různé kmitočty, čímž je zajištěna ortogonalita ve kmitočtové oblasti.

MAIOA funguje ve spojení s HSN, čímž definuje vzor přeskakování. Zatímco HSN určuje pořadí návštěv kmitočtů, MAIO tento vzor pro každého uživatele posouvá. Například při HSN rovném 0 (cyklické přeskakování) budou uživatelé s po sobě jdoucími hodnotami MAIO procházet seznamem MA postupným cyklickým způsobem. Pro nenulové hodnoty HSN (pseudonáhodné přeskakování) poskytuje MAIO jedinečný posun do pseudonáhodné posloupnosti. Toto koordinované přidělování zabraňuje kolizím, kdy by se dvě mobilní stanice pokoušely použít stejný kmitočet ve stejný čas, což je zásadní pro minimalizaci stejnovlnné a sousední kanálové interference, a tím pro zlepšení kvality signálu a kapacity systému.

Úlohou MAIOA v síti je umožnit efektivní opakované využití omezeného rádiového spektra. Tím, že zajišťuje, aby rušivé signály byly v čase náhodné a průměrované, zlepšuje odolnost spoje proti útlumu, interferenci a vícecestnému šíření. To je obzvláště důležité v hustých městských nasazeních, kde jsou vzory opakovaného využití kmitočtu těsné. MAIOA je základním aspektem správy rádiových zdrojů v GSM a přispívá k legendární spolehlivosti a kvalitě hovoru této technologie. Její principy ovlivnily pozdější technologie, ačkoli konkrétní implementace se vyvíjely v UMTS a LTE s odlišnými mechanismy přeskakování.

## K čemu slouží

MAIO Allocation (přidělení MAIO) bylo vytvořeno, aby řešilo zásadní výzvu řízení interference v celulárních sítích, konkrétně v systému GSM, který využívá vícečetný přístup s kmitočtovým dělením (FDMA) a vícečetný přístup s časovým dělením (TDMA). Před rozšířeným zavedením přeskakování kmitočtu trpěly sítě GSM konstantní stejnovlnnou interferencí kvůli pevnému přiřazení kmitočtu na buňku a časový slot. To vedlo ke špatné kvalitě hovoru v oblastech s vysokým provozem nebo na okrajích buněk, což omezovalo kapacitu sítě a uživatelský zážitek. Zavedení přeskakování kmitočtu, a tím i MAIOA, bylo motivováno potřebou využít diverzitu interference – přeměnit trvalou interferenci na náhodnou, průměrovanou interferenci, kterou lze zmírnit pomocí kanálového kódování a prokládání.

Tato technologie řeší problém předvídatelných vzorů interference tím, že zajišťuje změnu kmitočtu vysílání každé mobilní stanice v každém TDMA rámci (přibližně každých 4,615 ms). MAIOA je mechanismus, který tyto změny koordinuje mezi více uživateli sdílejícími stejný fyzický zdroj (časový slot). Bez správného přidělení MAIO by dvěma mobilním stanicím mohly být přiděleny stejné vzory přeskakování, což by vedlo k trvalým kolizím a přerušeným hovorům. Přidělením jedinečných posunů MAIO síť zaručuje, že uživatelé na stejném časovém slotu přeskakují na různé kmitočty, čímž efektivně rozprostírá interferenci v pásmu a zlepšuje poměr nosná/interference (C/I). To umožňuje těsnější vzory opakovaného využití kmitočtu, zvyšuje počet kanálů na jednotku plochy, a tím i celkovou kapacitu systému.

Historicky bylo MAIOA standardizováno ve 3GPP Release 8 jako součást vylepšených požadavků na výkon pro GSM Evolution (EDGE). Navázalo na dřívější koncepty přeskakování kmitočtu z GSM fáze 2 a poskytlo strukturovanější a škálovatelnější rámec pro přiřazování parametrů. Vytvoření MAIOA řešilo omezení manuálního kmitočtového plánování, které bylo složité a nepružné. Automatizací a optimalizací přidělování posunu mohli operátoři efektivněji nasazovat sítě, přizpůsobovat se měnícím se podmínkám provozu a poskytovat konzistentní kvalitu služeb. To byl klíčový faktor pro vysoce kapacitní a robustní hlasové a datové služby, které charakterizovaly vyspělé GSM sítě po celém světě.

## Klíčové vlastnosti

- Definuje počáteční posun v posloupnosti přeskakování kmitočtu pro mobilní stanici
- Funguje ve spojení s číslem posloupnosti přeskakování (HSN) a seznamem mobilní alokace (MA)
- Hodnoty jsou v rozsahu od 0 do N-1, kde N je počet kmitočtů v seznamu MA
- Přiděluje se řadičem základnové stanice (BSC) během přiřazování kanálu
- Zajišťuje ortogonální vzory přeskakování pro více uživatelů na stejném časovém slotu
- Snižuje stejnovlnnou a sousední kanálovou interferenci prostřednictvím průměrování interference

## Související pojmy

- [HSN – Hopping Sequence Number](/mobilnisite/slovnik/hsn/)
- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)

## Definující specifikace

- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [MAIOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/maioa/)
