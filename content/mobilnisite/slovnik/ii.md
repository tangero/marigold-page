---
slug: "ii"
url: "/mobilnisite/slovnik/ii/"
type: "slovnik"
title: "II – Nu = 5 * (FUL – 1850.1 MHz)"
date: 2025-01-01
abbr: "II"
fullName: "Nu = 5 * (FUL – 1850.1 MHz)"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ii/"
summary: "Vzorec používaný v režimu UTRA TDD (TD-CDMA) pro výpočet nominálního čísla kanálu (Nu) z kmitočtu nosné uplinku (FUL) v pásmu 1900 MHz. Jde o klíčový parametr pro plánování rádiových kmitočtů a identi"
---

II je vzorec pro výpočet nominálního čísla kanálu z frekvence uplinku v pásmu 1900 MHz pro režim UTRA TDD.

## Popis

Parametr 'II', přesněji reprezentovaný vzorcem Nu = 5 * (FUL – 1850.1 MHz), je kritickou definicí v rámci specifikací 3GPP [UTRA](/mobilnisite/slovnik/utra/) (UMTS Terrestrial Radio Access), konkrétně pro režim Time Division Duplex ([TDD](/mobilnisite/slovnik/tdd/)), známý také jako [TD-CDMA](/mobilnisite/slovnik/td-cdma/). Tento vzorec slouží k výpočtu nominálního absolutního čísla rádiového kmitočtového kanálu UTRA ([UARFCN](/mobilnisite/slovnik/uarfcn/)) pro nosnou uplinku v určitých kmitočtových pásmech TDD. Proměnná 'Nu' představuje toto nominální číslo kanálu, zatímco 'FUL' je skutečný kmitočet nosné uplinku vyjádřený v MHz. Konstanta '1850.1 MHz' slouží jako referenční kmitočet a násobitel '5' definuje kmitočtový rastr kanálu, neboli rozestup mezi po sobě jdoucími čísly kanálů, z hlediska kmitočtu (každý krok v Nu odpovídá změně kmitočtu o 0.2 MHz). Tento vzorec platí konkrétně pro kmitočtové pásmo 1900 MHz (pásmo I pro UTRA TDD podle některých regionálních plánů). V praxi tento vzorec používají plánovači sítí k přiřazení jedinečného čísla kanálu každému nasazenému kmitočtu nosné. Toto číslo kanálu se pak používá v signalizačních zprávách a konfiguraci sítě namísto surové hodnoty kmitočtu, což zjednodušuje návrh systému a zajišťuje jednoznačnou identifikaci. UE (uživatelské zařízení) využívá znalost tohoto mapování k naladění svého přijímače na správný kmitočet, když mu síť nařídí použít konkrétní číslo kanálu. Vzorec je základní součástí definice kmitočtů fyzické vrstvy a zajišťuje, že všechny síťové prvky mají konzistentní a standardizovaný způsob odkazování na rádiové nosné.

## K čemu slouží

Účelem tohoto vzorce je poskytnout standardizovanou, jednoznačnou metodu pro identifikaci kmitočtů rádiových nosných v systémech [UTRA](/mobilnisite/slovnik/utra/) [TDD](/mobilnisite/slovnik/tdd/). Používání surových hodnot kmitočtů v signalizaci a konfiguraci je náchylné k chybám zaokrouhlování a rozdílům v implementaci. Definováním lineárního mapování mezi celočíselným číslem kanálu (Nu) a fyzickým kmitočtem zajišťuje 3GPP interoperabilitu. Vzorec řeší problém, jak efektivně signalizovat informace o kmitočtu mezi sítí a UE v rámci protokolových zpráv, které mají omezené bitové pole. Historickým kontextem je potřeba společného číslovacího schématu napříč všemi režimy UTRA ([FDD](/mobilnisite/slovnik/fdd/) a TDD) pro efektivní správu sítě a implementaci UE. Konkrétní konstanty (referenční kmitočet 1850.1 MHz a násobitel 5) byly zvoleny tak, aby poskytly vhodné celočíselné číslo kanálu pro určené kmitočtové pásmo, v souladu s kmitočtovým rastrem a plánem pásem. Řeší omezení ad-hoc identifikace kmitočtů a poskytuje čistý matematický vztah nezbytný pro automatizované plánování sítě, výběr buňky a procedury předávání spojení.

## Klíčové vlastnosti

- Definuje UARFCN pro nosné uplinku UTRA TDD v pásmu 1900 MHz
- Poskytuje lineární mapování mezi číslem kanálu (Nu) a kmitočtem nosné (FUL)
- Používá referenční kmitočet 1850.1 MHz a násobitel kmitočtového rastru 5
- Zajišťuje jednoznačnou identifikaci kmitočtu pro signalizaci a konfiguraci
- Zjednodušuje implementaci UE pro naladění kmitočtu nosné
- Standardizuje klíčový parametr pro plánování a optimalizaci rádiové sítě

## Související pojmy

- [UARFCN – UTRA Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/uarfcn/)
- [TD-CDMA – Time Division - Code Division Multiple Access](/mobilnisite/slovnik/td-cdma/)

## Definující specifikace

- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [II na 3GPP Explorer](https://3gpp-explorer.com/glossary/ii/)
