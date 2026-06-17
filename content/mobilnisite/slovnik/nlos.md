---
slug: "nlos"
url: "/mobilnisite/slovnik/nlos/"
type: "slovnik"
title: "NLOS – Non Line of Sight"
date: 2025-01-01
abbr: "NLOS"
fullName: "Non Line of Sight"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nlos/"
summary: "NLOS označuje podmínky šíření rádiového signálu, kdy mezi vysílačem a přijímačem neexistuje přímá viditelná dráha, často kvůli překážkám. Jde o klíčový stav přenosového kanálu pro hodnocení a návrh od"
---

NLOS je stav šíření rádiového signálu, kdy mezi vysílačem a přijímačem neexistuje přímá viditelná dráha, obvykle kvůli překážkám, což nutí signály spoléhat na odraz, ohyb a rozptyl.

## Popis

Non Line of Sight (NLOS) je základní podmínka šíření rádiového signálu v bezdrátových komunikacích, kdy mezi vysílací a přijímací anténou neexistuje přímá, nezakrytá dráha. Signál musí cestovat alternativními mechanismy, jako je odraz od povrchů (např. budovy, stěny), ohyb kolem překážek a rozptyl od nerovných povrchů nebo malých objektů. To vede k vícecestnému prostředí, kde signál dorazí k přijímači po více drahách s různým zpožděním, fází a útlumem, což způsobuje jevy jako úniky, rozprostření zpoždění a mezisymbolové rušení. Ve standardech 3GPP jsou podmínky NLOS podrobně modelovány a studovány, zejména pro modelování kanálu a hodnocení výkonu technologií new radio (NR).

Z pohledu návrhu systému je provoz v podmínkách NLOS primárním aspektem pro zajištění spolehlivého pokrytí, zejména v hustě zastavěných městských, příměstských a vnitřních prostředích, kde je přímá viditelnost ([LOS](/mobilnisite/slovnik/los/)) jen zřídka zaručena. Výkon modulačních schémat, kódovacích technik a systémů s více anténami ([MIMO](/mobilnisite/slovnik/mimo/)) silně závisí na charakteristikách přenosového kanálu. Pokročilé techniky jako formování svazku, massive MIMO a pokročilé kanálové kódování (např. [LDPC](/mobilnisite/slovnik/ldpc/)) jsou navrženy tak, aby udržely robustní připojení a vysoké přenosové rychlosti i v náročných podmínkách NLOS. Schopnost efektivně fungovat v NLOS je zásadní pro dosažení cílů všudypřítomného pokrytí sítí 5G a budoucích generací.

Specifikace 3GPP, zejména v řadě 38.8xx (např. 38.828), definují podrobné modely kanálů, které zahrnují konkrétní scénáře NLOS pro různá nasazovací prostředí (např. Urban Micro, Urban Macro, Indoor Office). Tyto modely se používají pro testování shody, výkonnostní požadavky a hodnocení nových funkcí. Studium šíření v NLOS je také klíčové pro vyšší kmitočtová pásma, jako je mmWave (např. FR2), kde jsou signály náchylnější k blokování a útlumu, což činí spolehlivé spoje v NLOS významnou technickou výzvou. Nástroje pro plánování a optimalizaci sítí se silně spoléhají na přesné modely šíření NLOS pro predikci pokrytí a kapacity.

## K čemu slouží

Koncept šíření NLOS je ve standardech 3GPP řešen proto, aby bylo zajištěno, že technologie mobilních sítí jsou navrženy a hodnoceny za realistických provozních podmínek. Nasazení v reálném světě, zejména ve městech a uvnitř budov, jsou převážně NLOS. Proto musí metrika systémového výkonu, algoritmy správy rádiových zdrojů a procedury fyzické vrstvy zohledňovat zhoršení způsobená absencí přímé dráhy. Ignorování podmínek NLOS by vedlo k nerealisticky optimistickým predikcím výkonu a sítím, které by v praktických scénářích selhávaly.

Historicky, jak se buněčné systémy vyvíjely od venkovního pokrytí makrobuňkami k hustým heterogenním sítím zahrnujícím malé buňky a vnitřní systémy, rostl význam přesného modelování a zmírňování účinků NLOS. Rané systémy mohly předpokládat příznivější šíření, ale snaha o vyšší přenosové rychlosti a spolehlivé připojení všude si vyžádala důsledné řešení NLOS. Zavedení nových kmitočtových pásem, zejména milimetrových vln v 5G NR, toto dostalo do popředí, protože tyto vysokofrekvenční signály jsou snadno blokovány. Definování standardizovaných modelů kanálů NLOS a výkonnostních požadavků proto zajišťuje interoperabilitu a to, že zařízení od různých výrobců splňují konzistentní základní úroveň výkonu v těchto náročných prostředích.

## Klíčové vlastnosti

- Charakterizace vícecestného šíření prostřednictvím odrazu, ohybu a rozptylu
- Integrace do standardizovaných modelů kanálů 3GPP (např. TR 38.828) pro testování výkonu
- Kritická pro hodnocení výkonu MIMO a formování svazku v realistických nasazeních
- Základ pro plánování pokrytí a optimalizaci sítí v městských a vnitřních oblastech
- Klíčový aspekt pro návrh systémů ve vyšších kmitočtových pásmech (např. mmWave)
- Ovlivňuje návrh modulace, kódování a schémat opakovaného vysílání

## Související pojmy

- [LOS – Loss Of Signal](/mobilnisite/slovnik/los/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TR 38.828** (Rel-16) — CLI and RIM for NR

---

📖 **Anglický originál a plná specifikace:** [NLOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nlos/)
