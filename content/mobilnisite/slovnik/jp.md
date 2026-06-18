---
slug: "jp"
url: "/mobilnisite/slovnik/jp/"
type: "slovnik"
title: "JP – Joint Predistortion"
date: 2025-01-01
abbr: "JP"
fullName: "Joint Predistortion"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/jp/"
summary: "Technika digitálního zpracování signálu používaná v bezdrátových vysílačích k linearizaci výkonových zesilovačů aplikací inverzní distorze na vstupní signál. Kompenzuje nelinearity a paměťové efekty v"
---

JP (Joint Predistortion, společná predistorze) je technika digitálního zpracování signálu používaná v bezdrátových vysílačích k linearizaci výkonových zesilovačů aplikací inverzní distorze na vstupní signál, čímž se zlepšuje kvalita signálu a spektrální účinnost.

## Popis

Joint Predistortion (JP, společná predistorze) je pokročilá metoda digitální predistorze ([DPD](/mobilnisite/slovnik/dpd/)), která koriguje nelineární zkreslení ve vysokofrekvenčních ([RF](/mobilnisite/slovnik/rf/)) výkonových zesilovačích ([PA](/mobilnisite/slovnik/pa/)). Výkonové zesilovače jsou ze své podstaty nelineární, zejména při provozu blízko saturace pro vysokou účinnost, což způsobuje nežádoucí efekty jako spektrální růst, intermodulační zkreslení a zhoršení poměru úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)). JP funguje tak, že na vstupní signál v základním pásmu před jeho dosažením k PA aplikuje predistorzor – digitální filtr s inverzní nelineární charakteristikou. Tento predistorzovaný signál po zesílení vede k linearizovanému výstupu, který věrně odpovídá původnímu zamýšlenému signálu, čímž se snižuje zkreslení a zlepšuje celkový výkon vysílače.

Aspekt 'Joint' (společný) odkazuje na simultánní zohlednění více faktorů nebo signálů v procesu predistorze. Na rozdíl od jednoduché predistorze bez paměti, která řeší pouze okamžité nelinearity, JP zohledňuje paměťové efekty způsobené tepelnou dynamikou, modulací obvodů předpětí a kmitočtově závislým chováním zesilovače. Typicky využívá adaptivní algoritmy, jako je metoda nejmenších čtverců ([LMS](/mobilnisite/slovnik/lms/)) nebo rekurzivní metoda nejmenších čtverců ([RLS](/mobilnisite/slovnik/rls/)), pro průběžnou aktualizaci koeficientů predistorzoru na základě zpětné vazby z výstupu PA. Tato zpětná vazba je získávána přes vazební člen, který vzorkuje zesílený signál; ten je následně převeden do základního pásma, digitalizován a porovnán se vstupem pro odhad modelu zkreslení.

V systémech 3GPP je JP relevantní pro základnové stanice (eNodeB v LTE, gNB v 5G NR) a uživatelská zařízení (UE) s vysíláním vysokého výkonu. Umožňuje splnění přísných požadavků na spektrální masku definovaných v specifikacích jako 3GPP TS 36.104 a TS 38.104, které omezují mimopásmové emise. Linearizací PA umožňuje JP zesilovačům pracovat na vyšších výkonových úrovních s lepší účinností, čímž snižuje spotřebu energie a tepelné ztráty. To je klíčové pro nasazení massive [MIMO](/mobilnisite/slovnik/mimo/) a milimetrových vln v 5G, kde se používají pole PA, a linearita přímo ovlivňuje propustnost a pokrytí.

Klíčové komponenty systému JP zahrnují blok digitálního predistorzoru v procesoru základního pásma, řetězec zpětnovazebního přijímače a adaptační logiku. Predistorzor je často implementován pomocí modelů jako Volterrova řada, paměťový polynom nebo zobecněný paměťový polynom, které dokážou zachytit komplexní nelinearity s pamětí. JP je integrována do fyzické vrstvy bezdrátových systémů a spolupracuje s dalšími technikami, jako je redukce činitele špičkovosti ([CFR](/mobilnisite/slovnik/cfr/)), pro řízení poměru špičkového a středního výkonu (PAPR). Její účinnost se měří metrikami, jako je zlepšení velikosti chybového vektoru (EVM) a redukce ACLR, což zajišťuje, že signály splňují standardy kvality pro modulační schémata až do 256-QAM v LTE a 1024-QAM v 5G NR.

## K čemu slouží

Joint Predistortion byla vyvinuta k řešení kompromisu mezi účinností a linearitou výkonového zesilovače v bezdrátové komunikaci. Tradiční PA jsou nejúčinnější blízko saturace, ale to zavádí závažná nelineární zkreslení, která degradují integritu signálu a způsobují interferenci v sousedních kanálech. Raná řešení využívala provoz s výkonovou rezervou (snížení výkonu pro setrvání v lineární oblasti), což však obětovalo účinnost a vedlo k vyšším energetickým nákladům a tepelným problémům, zejména u základnových stanic. JP to řeší tím, že umožňuje PA pracovat účinně při zachování linearity prostřednictvím digitální korekce.

Historická motivace vychází z vývoje standardů 3GPP směrem k modulacím vyššího řádu a širším šířkám pásma, jako v LTE-Advanced a 5G NR. Tato vylepšení vyžadují vynikající věrnost signálu pro dosažení vysokých přenosových rychlostí, což činí linearitu PA kritickou. Předchozí metody predistorze byly bez paměti nebo omezeného rozsahu a nedokázaly kompenzovat dynamické paměťové efekty u širokopásmových signálů. JP se objevila jako komplexnější přístup, který společně řeší jak nelineární, tak paměťová zkreslení, což se stalo nezbytným s vícekanálovými signály, jako je OFDM používaný v 4G a 5G.

V sítích 3GPP je JP zásadní pro splnění regulatorních standardů emisí a maximalizaci spektrální účinnosti. Umožňuje operátorům nasazovat husté sítě s minimální interferencí a podporuje funkce jako agregace nosných a massive MIMO. Tato technologie také snižuje provozní náklady zlepšením účinnosti PA, což je významný faktor v celkových nákladech na vlastnictví mobilních sítí. Jak se 5G rozšiřuje do pásem milimetrových vln, kde mají PA jedinečné nelineární charakteristiky, JP se dále vyvíjí a zajišťuje spolehlivý výkon v bezdrátových systémech příští generace.

## Klíčové vlastnosti

- Kompensuje jak nelinearity, tak paměťové efekty ve výkonových zesilovačích
- Používá adaptivní algoritmy (např. LMS, RLS) pro aktualizaci koeficientů v reálném čase
- Podporuje širokopásmové signály a vícekanálové přenosy, jako je OFDM
- Zlepšuje poměr úniku do sousedního kanálu (ACLR) a velikost chybového vektoru (EVM)
- Umožňuje vyšší účinnost PA tím, že povoluje provoz blízko saturace
- Integruje se s redukcí činitele špičkovosti (CFR) pro řízení poměru špičkového a středního výkonu (PAPR)

## Související pojmy

- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)
- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [JP na 3GPP Explorer](https://3gpp-explorer.com/glossary/jp/)
