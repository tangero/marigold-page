---
slug: "mbw"
url: "/mobilnisite/slovnik/mbw/"
type: "slovnik"
title: "MBW – Measurement Bandwidth"
date: 2025-01-01
abbr: "MBW"
fullName: "Measurement Bandwidth"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mbw/"
summary: "Definovaná šířka pásma používaná pro rádiová frekvenční měření k ochraně přilehlých kmitočtových pásem před interferencí. Zajišťuje přesné vyhodnocení výkonu vysílače a přijímače při zachování souladu"
---

MBW je definovaná šířka pásma používaná pro rádiové frekvenční měření za účelem ochrany přilehlých pásem před interferencí a zajištění přesného vyhodnocení výkonu vysílače a přijímače.

## Popis

Measurement Bandwidth (MBW) je klíčový parametr ve specifikacích 3GPP, který definuje šířku pásma, v jejímž rámci se provádějí rádiová frekvenční ([RF](/mobilnisite/slovnik/rf/)) měření jak pro uživatelské zařízení (UE), tak pro základnové stanice. Je specifikován pro různé testovací scénáře k vyhodnocení charakteristik vysílače a přijímače, jako je výstupní výkon, spektrální emise a citlivost. MBW je pečlivě volen tak, aby odpovídal šířce kanálu měřeného signálu, a zároveň bere v úvahu potřebu ochrany přilehlých kmitočtových pásem, známých jako chráněné pásmo. Tím se zajišťuje, že měření přesně odrážejí výkonnost bez zachycení nežádoucí interference ze sousedních kanálů.

V praxi se MBW uplatňuje v konformních testovacích sestavách, kde jsou testovací zařízení, jako jsou spektrální analyzátory nebo generátory signálu, konfigurována s konkrétním nastavením šířky pásma. Pro testy vysílače, jako jsou měření nežádoucích emisí, MBW definuje rozlišovací šířku pásma, přes kterou se integrují parazitní emise za účelem ověření souladu s požadavky masky. Pro testy přijímače, jako je referenční citlivost, MBW nastavuje šířku pásma, přes kterou se měří požadovaný signál, aby se vyhodnotila schopnost přijímače dekódovat data při nízké úrovni signálu. Hodnota MBW se liší v závislosti na šířce kanálu a kmitočtovém rozsahu, přičemž podrobné tabulky jsou uvedeny ve specifikacích jako 38.101 pro NR a 36.101 pro LTE.

Role MBW přesahuje pouhé měření; je nedílnou součástí zajišťování koexistence v spektru a souladu s regulacemi. Definováním vhodných měřicích šířek pásma zajišťuje 3GPP, že zařízení nezpůsobují škodlivou interferenci jiným systémům pracujícím v přilehlých pásmech. Například v testech mimopásmových emisí je MBW nastaveno tak, aby zachytilo emise, které by mohly zasáhnout chráněná pásma, jako jsou ta používaná satelitními nebo radarovými systémy. To zahrnuje měření jak uvnitř, tak vně šířky kanálu, s konkrétními limity aplikovanými na různé rozsahy odstupu. Parametr MBW tak propojuje technické hodnocení výkonnosti se spektrální politikou, což umožňuje harmonizované nasazení bezsítových sítí po celém světě.

## K čemu slouží

MBW bylo zavedeno za účelem standardizace postupů [RF](/mobilnisite/slovnik/rf/) měření napříč různými typy zařízení a kmitočtovými pásmy, což řeší nekonzistence v dřívějších testovacích metodologiích. Jak se mobilní sítě vyvíjely, aby podporovaly širší šířky kanálů a nové kmitočtové rozsahy, vznikla potřeba přesných definic, jak by měla být měření prováděna, aby bylo zajištěno spravedlivé a přesné hodnocení výkonnosti. Bez standardizovaného MBW by se výsledky testů mohly mezi laboratořemi lišit, což by vedlo ke sporům o shodu zařízení a potenciálním problémům s interferencí v síti.

Primární problém, který řeší, je přesná charakterizace emisí zařízení a jeho citlivosti v prostředí s více pásmy. V širokopásmových systémech, jako je 5G NR, mohou signály zabírat až 400 MHz v milimetrových pásmech, což ztěžuje měření výkonnosti bez ovlivnění přilehlých služeb. MBW poskytuje rámec pro definování měřicích intervalů, které jsou reprezentativní pro reálný provoz, a zároveň chrání ostatní uživatele spektra. To je obzvláště důležité pro scénáře koexistence, například když 5G sítě pracují v blízkosti leteckých nebo vědeckých pásem, kde musí být vynucovány přísné emisní limity.

MBW dále podporuje vývoj pokročilých funkcí, jako je agregace nosných a dynamické sdílení spektra. Specifikací měřicích šířek pásma pro každou komponentní nosnou a agregovanou šířku pásma umožňuje ověření složitých RF scénářů. Parametr se také přizpůsobuje novým případům užití, jako je integrovaný přístup a přenosová síť ([IAB](/mobilnisite/slovnik/iab/)) a mimozemské sítě ([NTN](/mobilnisite/slovnik/ntn/)), kde vznikají jedinečné konfigurace šířky pásma. Celkově MBW zajišťuje, že zařízení splňují jak technické, tak regulační požadavky, což usnadňuje globální interoperabilitu a efektivní využití spektra.

## Klíčové vlastnosti

- Definuje šířku pásma pro RF měření za účelem zajištění přesnosti a reprodukovatelnosti
- Chrání přilehlá kmitočtová pásma specifikací měřicích intervalů pro testy emisí
- Podporuje různé šířky kanálů a kmitočtové rozsahy od LTE po 5G NR
- Integruje se s konformním testováním výkonnosti vysílače a přijímače
- Je v souladu s regulačními maskami a požadavky na koexistenci spektra
- Umožňuje ověření scénářů s agregací nosných a širokopásmovým provozem

## Definující specifikace

- **TS 36.761** (Rel-15) — Extended-Band 12 Study Report
- **TS 37.717** — 3GPP TR 37.717
- **TS 37.718** — 3GPP TR 37.718
- **TS 37.719** (Rel-19) — 3GPP TR 37.719: Dual Connectivity Band Combinations
- **TR 37.829** (Rel-18) — Technical Report
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.755** (Rel-19) — NR FR1 DL Fragmented Carriers Study
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TS 38.793** (Rel-19) — Simultaneous Rx/Tx Band Combinations TR
- **TR 38.839** (Rel-17) — Simultaneous Rx/Tx band combinations
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec
- **TR 38.881** (Rel-18) — Technical Report on Lower MSD for Inter-band CA/EN-DC/DC
- **TR 38.894** (Rel-18) — Technical Report
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [MBW na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbw/)
