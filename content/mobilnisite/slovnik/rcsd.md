---
slug: "rcsd"
url: "/mobilnisite/slovnik/rcsd/"
type: "slovnik"
title: "RCSD – Reverse Call Setup Direction"
date: 2025-01-01
abbr: "RCSD"
fullName: "Reverse Call Setup Direction"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rcsd/"
summary: "Mechanismus v okruhově přepínaných sítích, kde je směr sestavování hovoru obrácen, což umožňuje volané straně iniciovat zřízení cesty hovoru. Optimalizuje směrování a alokaci prostředků, zejména v mez"
---

RCSD je mechanismus v okruhově přepínaných sítích, kde volaná strana iniciuje zřizování cesty hovoru za účelem optimalizace směrování a alokace prostředků, čímž zvyšuje efektivitu a snižuje prodlevy při sestavování.

## Popis

Reverse Call Setup Direction (RCSD) je funkce definovaná 3GPP pro okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) jádrové sítě, primárně v systémech GSM a UMTS. Obrácením tradičního směru sestavování hovoru, kde volající strana iniciuje zřizování cesty, umožňuje, aby síť volané strany spustila sestavení spojení hovoru. Tento mechanismus se používá v konkrétních scénářích, jako je mezinárodní roaming nebo hovory mezi operátory, pro optimalizaci směrování a minimalizaci signalizační zátěže. Proces zahrnuje aktivní roli mobilní ústředny ([MSC](/mobilnisite/slovnik/msc/)) volané strany při zřizování přenosové cesty, často na základě předem dohodnutých ujednání mezi síťovými operátory.

RCSD funguje tak, že mění standardní sekvenci sestavování hovoru definovanou v protokolech jako [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part). Při typickém hovoru vysílá zdrojová MSC zprávy pro sestavení směrem k cílové MSC. S RCSD může cílové MSC po přijetí počáteční adresové zprávy ([IAM](/mobilnisite/slovnik/iam/)) rozhodnout o obrácení směru a iniciovat nové sestavení zpět směrem k volajícímu. Toto rozhodnutí je založeno na faktorech, jako je optimalizace nákladů, topologie sítě nebo vyrovnávání zatížení. Mezi klíčové komponenty patří MSC na obou koncích, sítě signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)) a řídicí body služeb, které mohou ovlivňovat logiku obrácení. Funkce vyžaduje koordinaci mezi operátory pro zajištění kompatibility a zabránění smyčkám.

V jádrové síti hraje RCSD roli při zvyšování efektivity zpracování okruhově přepínaných hovorů, zejména s vývojem sítí pro podporu globálního roamingu a složitých propojení. Pomáhá snižovat prodlevu po vytočení a optimalizovat využití přenosových prostředků výběrem optimálních tras. Ačkoli je primárně spojována s legacy CS doménami, porozumění RCSD je relevantní pro inženýry zabývající se migrací na IP systémy, neboť ilustruje historické strategie směrování. Funkce je dokumentována ve specifikacích 3GPP napříč více vydáními, což odráží její trvání v CS infrastruktuře až do vyřazení takových sítí.

## K čemu slouží

RCSD byla zavedena za účelem řešení neefektivit v tradičním sestavování okruhově přepínaných hovorů, zejména pro mezinárodní nebo mezioperátorské hovory, kde mohly být směrovací cesty suboptimální. V raných sítích GSM sestavování hovoru vždy začínalo na straně volajícího, což někdy vedlo k delším signalizačním cestám a vyšším nákladům, zvláště když byla volaná strana v jiné zemi nebo síti. To mohlo mít za následek zvýšenou latenci a plýtvání prostředky, což ovlivňovalo uživatelský zážitek a ekonomiku operátorů.

Motivace pro RCSD vycházela z potřeby optimalizovat využití síťových prostředků a snížit signalizační režii v rostoucím globálním mobilním ekosystému. Tím, že umožnila síti volané strany iniciovat cestu hovoru, mohli operátoři implementovat přímější strategie směrování založené na komerčních dohodách nebo stavu sítě. Tím se řešila omezení statických směrovacích protokolů a umožnila dynamická vylepšení zpracování hovorů. Historicky, jak se roaming stal běžnějším, funkce jako RCSD pomohly zefektivnit interakce mezi operátory a připravily cestu pro pozdější inovace v IP multimediálních subsystémech. I když je méně relevantní v moderních plně IP sítích, RCSD představuje důležitý vývoj v efektivitě telekomunikační signalizace.

## Klíčové vlastnosti

- Obrácení směru sestavování hovoru ze sítě volané strany
- Optimalizace směrovacích cest pro okruhově přepínané hovory
- Snížení signalizační zátěže a prodlevy po vytočení
- Podpora mezinárodních a mezioperátorských scénářů
- Koordinace mezi MSC prostřednictvím signalizace SS7
- Zvýšení efektivity alokace prostředků

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization

---

📖 **Anglický originál a plná specifikace:** [RCSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/rcsd/)
