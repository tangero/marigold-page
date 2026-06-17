---
slug: "64qam"
url: "/mobilnisite/slovnik/64qam/"
type: "slovnik"
title: "64QAM – 64 Quadrature Amplitude Modulation"
date: 2025-01-01
abbr: "64QAM"
fullName: "64 Quadrature Amplitude Modulation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/64qam/"
summary: "64QAM je digitální modulační schéma, které kóduje 6 bitů na symbol změnou amplitudy i fáze nosného signálu. Poskytuje vyšší spektrální účinnost než modulace QAM nižšího řádu, což umožňuje zvýšení přen"
---

64QAM je digitální modulační schéma používané v mobilních sítích 3GPP, které kóduje 6 bitů na symbol pomocí změn amplitudy i fáze, čímž poskytuje vyšší spektrální účinnost pro zvýšení přenosových rychlostí.

## Popis

64QAM (64 Quadrature Amplitude Modulation) je sofistikovaná digitální modulační technika, která kombinuje amplitudovou a fázovou modulaci k přenosu více bitů na symbol. V 64QAM se konstelace skládá z 64 diskrétních bodů uspořádaných do mřížky 8×8, přičemž každý bod představuje jedinečnou kombinaci amplitudy a fáze. Toto uspořádání umožňuje každému symbolu nést 6 bitů informace (protože 2^6 = 64), což výrazně zvyšuje rychlost přenosu dat ve srovnání s jednoduššími modulačními schématy, jako je QPSK (2 bity na symbol) nebo [16QAM](/mobilnisite/slovnik/16qam/) (4 bity na symbol).

Technická implementace 64QAM spočívá v mapování skupin 6 bitů na konkrétní body konstelace. Fázová (I) a kvadraturní (Q) složka nosného signálu jsou nezávisle modulovány specifickými úrovněmi amplitudy. V typické implementaci jsou amplitudové úrovně rovnoměrně rozmístěny, s hodnotami jako ±1, ±3, ±5, ±7 pro obě složky I i Q. Tím vzniká čtvercový konstelační diagram, kde je každý bod jednoznačně identifikován svými souřadnicemi I a Q. Přijímač musí přesně detekovat amplitudu i fázi přijatého signálu, aby správně demoduloval přenesené bity.

V systémech 3GPP funguje 64QAM v rámci schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) fyzické vrstvy. Výběr 64QAM oproti jiným modulačním schématům je dynamicky řízen základnovou stanicí na základě ukazatelů kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) hlášených uživatelským zařízením. Když jsou podmínky v kanálu vynikající (vysoký poměr signálu k šumu a minimální interference), může systém použít 64QAM pro maximalizaci propustnosti. Za horších podmínek však systém přechází na robustnější, ale méně účinná modulační schémata, jako je 16QAM nebo QPSK.

Implementace 64QAM vyžaduje sofistikované zpracování signálu na straně vysílače i přijímače. Na straně vysílače digitální zpracování signálu generuje přesné průběhy I a Q odpovídající každému bodu konstelace. Na straně přijímače jsou nezbytné pokročilé ekvalizační techniky pro kompenzaci zkreslení kanálu a přesná obnova nosné je klíčová pro správnou detekci fáze. Kódování pro opravu chyb, zejména turbokódy a [LDPC](/mobilnisite/slovnik/ldpc/) kódy v pozdějších vydáních, spolupracuje s 64QAM, aby zajistilo spolehlivou komunikaci navzdory zvýšené náchylnosti k šumu a interferencím, která je vlastní modulačním schématům vyššího řádu.

V architektuře 3GPP je 64QAM implementována ve zpracovatelském řetězci fyzické vrstvy, konkrétně ve funkci modulačního mapovače. Toto schéma úzce spolupracuje s dalšími komponentami fyzické vrstvy včetně kanálového kódování, prokládání a mapování na zdroje. Výkon při použití 64QAM je vysoce závislý na přesném odhadu kanálu, regulaci výkonu a řízení interference, což z něj činí klíčovou součást celkové strategie adaptace spoje, která vyvažuje propustnost a spolehlivost na základě aktuálních podmínek v kanálu.

## K čemu slouží

64QAM byla zavedena ve vydání 3GPP Release 7 primárně k uspokojení rostoucí poptávky po vyšších přenosových rychlostech v mobilních širokopásmových službách. Jak se očekávání uživatelů vyvíjela od základních hlasových a textových služeb k aplikacím náročným na šířku pásma, jako je streamování videa, prohlížení webu a stahování souborů, stávající modulační schémata jako QPSK a [16QAM](/mobilnisite/slovnik/16qam/) přestala stačit k dosažení požadované propustnosti v omezených spektrálních zdrojích. 64QAM poskytla 50% nárůst spektrální účinnosti oproti 16QAM, což umožnilo operátorům přenášet více dat bez nutnosti přidělení dalšího kmitočtového spektra.

Vývoj 64QAM byl motivován potřebou maximalizovat využití dostupných rádiových zdrojů při zachování zpětné kompatibility s existujícími sítěmi. Před zavedením 64QAM byly sítě [HSPA](/mobilnisite/slovnik/hspa/) omezeny na 16QAM v downlinku, což omezovalo špičkové přenosové rychlosti na přibližně 14 Mbps. S 64QAM mohly sítě HSPA+ dosáhnout teoretických špičkových rychlostí 21 Mbps v downlinku, což představovalo významný skok v možnostech přenosu dat v celulárních sítích. Toto vylepšení bylo obzvláště důležité s tím, jak se chytré telefony rozšířily a vzorce spotřeby dat se posunuly směrem k multimediálnímu obsahu.

Z technického hlediska řešila 64QAM základní kompromis mezi spektrální účinností a robustností přenosu. Modulační schémata nižšího řádu, jako je QPSK, nabízela vynikající odolnost vůči šumu, ale nízkou spektrální účinnost, zatímco schémata vyššího řádu, jako je 64QAM, poskytovala vyšší spektrální účinnost za cenu zvýšené citlivosti na zhoršení podmínek v kanálu. Zavedení 64QAM se časově shodovalo s vylepšeními přijímací techniky, kódování pro opravu chyb a algoritmů pro odhad kanálu, která umožnila spolehlivý provoz s modulací vyššího řádu v mobilním prostředí. To umožnilo síťovým operátorům nasazovat 64QAM selektivně za dobrých rádiových podmínek, čímž optimalizovali celkovou kapacitu sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Přenáší 6 bitů na symbol, čímž poskytuje o 50 % vyšší spektrální účinnost než 16QAM
- Používá konstelaci 8×8 se 64 diskrétními kombinacemi amplitudy a fáze
- Vyžaduje vyšší poměr signálu k šumu (SNR) než modulační schémata nižšího řádu
- Dynamicky volitelná jako součást adaptivní modulace a kódování (AMC)
- Implementována v obou směrech – downlink i uplink – v pozdějších vydáních
- Spolupracuje s pokročilým kódováním pro opravu chyb pro zajištění spolehlivosti

## Související pojmy

- [16QAM – 16-Quadrature Amplitude Modulation](/mobilnisite/slovnik/16qam/)

## Definující specifikace

- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation

---

📖 **Anglický originál a plná specifikace:** [64QAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/64qam/)
