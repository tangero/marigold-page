---
slug: "vii"
url: "/mobilnisite/slovnik/vii/"
type: "slovnik"
title: "VII – UTRA Absolute Radio Frequency Channel Number (UARFCN) for Band VII"
date: 2025-01-01
abbr: "VII"
fullName: "UTRA Absolute Radio Frequency Channel Number (UARFCN) for Band VII"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/vii/"
summary: "VII je vzorec pro absolutní číslo rádiového kanálu UTRA (UARFCN) pro pásmo UMTS VII. Definuje mapování mezi čísly kanálů a kmitočty uplinku (FUL) pro toto konkrétní pásmo, což umožňuje přesné kmitočto"
---

VII je vzorec pro absolutní číslo rádiového kanálu UTRA (UARFCN) pro pásmo UMTS VII, který definuje mapování mezi čísly kanálů a kmitočty uplinku pro provoz v rozsahu 2600 MHz.

## Popis

VII představuje výpočetní vzorec pro absolutní číslo rádiového kanálu [UTRA](/mobilnisite/slovnik/utra/) ([UARFCN](/mobilnisite/slovnik/uarfcn/)) specificky definovaný pro pásmo UMTS VII, které pracuje v kmitočtovém rozsahu 2600 MHz. V 3GPP UTRA (UMTS Terrestrial Radio Access) je UARFCN systém číslování kanálů používaný k identifikaci konkrétních kmitočtů nosné pro přenosy v uplinku i downlinku. Vzorec pro pásmo VII, Nu = 5 * (FUL – 2150.1 MHz), vypočítává UARFCN pro uplink (Nu) na základě kmitočtu nosné v uplinku (FUL) v MHz. Konstanta 5 je krok čísla kanálu a 2150.1 MHz je referenční kmitočtový posun definovaný pro toto pásmo. Odpovídající UARFCN pro downlink (Nd) používá podobný vzorec s vlastní referenční frekvencí.

Tento systém číslování kanálů je klíčovou součástí specifikace fyzické vrstvy. Když se uživatelské zařízení (UE) napojí na buňku nebo provádí měření, používá UARFCN k identifikaci a naladění na správný kmitočet nosné. Operátoři sítí a nástroje pro plánování sítí používají tyto vzorce k přiřazení nepřekrývajících se čísel kanálů napříč různými buňkami a sektory, čímž řídí přidělování rádiových zdrojů a minimalizují interferenci. UARFCN poskytuje standardizovaný a jednoznačný způsob odkazování na rádiové kmitočty mezi různými síťovými elementy a v signalizačních zprávách.

Specifikace UARFCN pro pásmo VII je udržována v dokumentu 3GPP TS 25.141, který pokrývá testování shody základnových stanic ([BS](/mobilnisite/slovnik/bs/)). Zatímco základní vzorec zůstal konzistentní, jeho použití je vázáno na širší režim UTRA [FDD](/mobilnisite/slovnik/fdd/) (Frequency Division Duplex). Pásmo VII se primárně používá pro nasazení UMTS/[HSPA](/mobilnisite/slovnik/hspa/) v různých regionech a poskytuje dodatečnou kapacitu ve vyšších kmitočtových pásmech. Porozumění tomuto vzorci UARFCN je zásadní pro kmitočtové inženýry zapojené do nasazení, optimalizace a řešení problémů 3G sítí pracujících v tomto pásmu.

## K čemu slouží

Účelem definice vzorce [UARFCN](/mobilnisite/slovnik/uarfcn/) pro pásmo VII (a další pásma) je vytvořit standardizovanou, abstraktní metodu pro identifikaci kmitočtů rádiové nosné v sítích UMTS. Používání přímo hodnot kmitočtů (např. 2630 MHz) v signalizaci a konfiguraci sítě je méně efektivní a náchylnější k chybám. Systém UARFCN převádí tyto fyzické kmitočty na celočíselná čísla kanálů, čímž zjednodušuje plánování sítě, implementaci v UE a signalizační protokoly.

Historicky se podobné systémy číslování kanálů (jako [ARFCN](/mobilnisite/slovnik/arfcn/) v GSM) osvědčily pro správu rádiového prostředí s více pásmy a více operátory. Pro UMTS byl systém UARFCN nezbytný pro podporu rostoucího počtu kmitočtových pásem přidělených pro služby [IMT-2000](/mobilnisite/slovnik/imt-2000/) po celém světě. Pásmo VII v rozsahu 2600 MHz bylo určeno k poskytnutí dodatečného spektra pro UMTS, často používaného pro zvýšení kapacity. Konkrétní vzorec pro pásmo VII zajišťuje, že každý možný kmitočet nosné v uplinku v rámci definovaného rozsahu pásma (2500-2570 MHz pro uplink) je mapován na jedinečné celočíselné číslo kanálu, což umožňuje přesné a interoperabilní řízení kmitočtu.

Tato abstraktní vrstva řeší problémy interoperability zařízení a zjednodušuje soulad s regulacemi napříč různými geografickými regiony, které používají stejné pásmo s mírnými odchylkami. Umožňuje výrobcům UE implementovat jediný logický postup pro výběr kanálu a měření, který je pak přizpůsoben fyzickému RF front-endu pro konkrétní pásmo pomocí těchto standardizovaných vzorců. Bez takového systému by řízení kmitočtové agilita a handoverů mezi nosnými a pásmy bylo výrazně složitější.

## Klíčové vlastnosti

- Definuje výpočet UARFCN pro uplink pro pásmo UMTS VII (FDD pásmo 2600 MHz).
- Používá vzorec Nu = 5 * (FUL – 2150.1 MHz), kde FUL je kmitočet uplinku v MHz.
- Poskytuje standardizovaný celočíselný identifikátor pro kmitočty nosné, což zjednodušuje signalizaci.
- Nezbytný pro procedury vyhledávání, výběru a převýběru buňky uživatelským zařízením (UE).
- Používá se při plánování a konfiguraci sítě pro přidělování kmitočtů.
- Specifikováno v 3GPP TS 25.141 pro testování shody základnových stanic.

## Související pojmy

- [UARFCN – UTRA Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/uarfcn/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [VII na 3GPP Explorer](https://3gpp-explorer.com/glossary/vii/)
