---
slug: "il"
url: "/mobilnisite/slovnik/il/"
type: "slovnik"
title: "IL – Insertion Loss"
date: 2022-01-01
abbr: "IL"
fullName: "Insertion Loss"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/il/"
summary: "Insertion Loss (IL, útlum při vložení) kvantifikuje útlum výkonu signálu při vložení komponenty, jako je filtr nebo konektor, do přenosové trasy. Je klíčový pro zajištění integrity signálu a výpočty r"
---

IL je útlum výkonu signálu, ke kterému dochází při vložení komponenty do přenosové trasy, což je klíčové pro integritu signálu a výpočet rozpočtu spoje v rádiových sítích.

## Popis

Insertion Loss (IL, útlum při vložení) je základním parametrem v RF a mikrovlnné technice, definovaným jako poměr výkonu dodaného do zátěže před vložením a po vložení zařízení do přenosové linky, typicky vyjádřený v decibelech (dB). V kontextu specifikací 3GPP, zejména pro LTE a NR, je IL klíčovým metrikem výkonu pro pasivní i aktivní komponenty v rámci rádiové přístupové sítě (RAN). To zahrnuje komponenty jako duplexery, filtry, kombinátory, kabely, konektory a anténní systémy, které tvoří přenosovou cestu mezi transceiverem základnové stanice a anténou. Nižší útlum při vložení je žádoucí, protože znamená menší útlum signálu, což je zásadní pro udržení dostatečného vysílacího výkonu a citlivosti přijímače.

Měření a specifikace IL jsou nezbytné pro přesnou analýzu rozpočtu spoje, která určuje maximální přípustný útlum na trase mezi vysílačem a přijímačem pro udržení požadované kvality signálu. Při nasazování sítě musí inženýři zohlednit kumulativní IL všech komponent ve vysílacím a přijímacím řetězci, aby zajistili, že efektivní izotropně vyzářený výkon ([EIRP](/mobilnisite/slovnik/eirp/)) a výkon přijímače splňují regulatorní a systémové požadavky. Například u masivních [MIMO](/mobilnisite/slovnik/mimo/) anténních polí pro 5G NR musí být útlum při vložení každého anténního prvku a jeho napájecí sítě minimalizován a charakterizován, aby bylo dosaženo požadovaného zisku při formování svazku a energetické účinnosti.

Studijní položky a specifikace 3GPP, jako jsou ty v TS 36.852 (LTE) a TS 38.860 (NR), se zabývají IL v kontextu testování výkonu sítě, studií koexistence a definice požadavků. Například při hodnocení koexistence různých technologií rádiového přístupu (např. LTE a NR ve scénářích sdílení spektra) se útlum při vložení filtrů používaných pro izolaci stává kritickým faktorem. Specifikace mohou definovat maximální přijatelné hodnoty IL pro určité komponenty nebo konfigurace, aby byla zaručena celková výkonnost systému. Porozumění útlumu při vložení a jeho zmírnění je tedy nedílnou součástí návrhu, nasazení a optimalizace efektivních a spolehlivých bezdrátových sítí.

## K čemu slouží

Účelem specifikace a řízení Insertion Loss (IL, útlumu při vložení) v rámci standardů 3GPP je zajistit předvídatelný a optimální výkon rádiové přístupové sítě. Každá fyzická komponenta v signálovém řetězci zavádí určitý útlum a nezapočítaná nebo nadměrná ztráta může degradovat pokrytí, snížit přenosové rychlosti a zvýšit spotřebu energie. Formálním zahrnutím IL do technických specifikací poskytuje 3GPP společný rámec pro výrobce zařízení a provozovatele sítí pro návrh a nasazení interoperabilních komponent, které splňují přísná kritéria výkonnosti.

Historicky, jak se buněčné sítě vyvíjely od 2G k 5G, provozní frekvence se zvyšovaly a byla zaváděna nová kmitočtová pásma, což často vyžadovalo složitější architektury RF front-endu s filtry pro agregaci nosných a sdílení spektra. Tyto komponenty přirozeně zavádějí ztráty. Motivací pro jeho zahrnutí do standardů, jako jsou ty pro LTE-Advanced (Rel-12/13) a 5G NR, je řešení výzev hustších sítí, vyšších frekvencí (jako mmWave) a pokročilých anténních systémů, kde i malé ztráty mohou mít významný dopad. Bez standardizovaného zohlednění IL by se výkon sítě mohl stát velmi variabilním a obtížně předvídatelným, což by vedlo k mezerám v pokrytí a nekonzistentní uživatelské zkušenosti.

Dále je IL klíčovým faktorem ve studiích koexistence, jako jsou ty mezi LTE a NR ve sdíleném spektru nebo mezi zařízeními různých operátorů. Definování přijatelných úrovní IL pro izolační filtry nebo jiné komponenty pomáhá zajistit, že systémy mohou pracovat bez škodlivého rušení a zároveň splňovat své vlastní výkonnostní cíle. Specifikace IL tedy řeší praktický inženýrský problém vyvážení složitosti komponent, nákladů a výkonu v moderních, heterogenních bezdrátových sítích.

## Klíčové vlastnosti

- Kvantifikuje útlum výkonu signálu v decibelech (dB) způsobený vložením komponenty
- Kritický parametr pro výpočet rozpočtu RF spoje a plánování sítě
- Aplikuje se na pasivní komponenty jako filtry, duplexery, kabely a konektory
- Přímo ovlivňuje vysílací výkon základnové stanice a citlivost přijímače
- Nezbytný pro hodnocení výkonu ve scénářích koexistence
- Specifikován v dokumentech 3GPP pro testování a požadavky na RAN zařízení

## Definující specifikace

- **TS 36.852** — 3GPP TR 36.852
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 38.860** (Rel-17) — NR; Study on Extended 600 MHz NR band

---

📖 **Anglický originál a plná specifikace:** [IL na 3GPP Explorer](https://3gpp-explorer.com/glossary/il/)
