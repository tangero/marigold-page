---
slug: "acrr"
url: "/mobilnisite/slovnik/acrr/"
type: "slovnik"
title: "ACRR – Adjacent Channel Rejection Ratio"
date: 2025-01-01
abbr: "ACRR"
fullName: "Adjacent Channel Rejection Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/acrr/"
summary: "ACRR měří schopnost přijímače potlačit rušení od signálů v sousedních kmitočtových kanálech při příjmu požadovaného signálu. Jde o kritický parametr vysokofrekvenčního (RF) výkonu, který zajišťuje spo"
---

ACRR je schopnost přijímače potlačit rušení od signálů v sousedních kmitočtových kanálech při příjmu požadovaného signálu, což je klíčové pro spolehlivou komunikaci v hustých celulárních sítích.

## Popis

Adjacent Channel Rejection Ratio (ACRR) je kvantitativní míra schopnosti rádiového přijímače udržet správný příjem požadovaného signálu za přítomnosti silných rušivých signálů v bezprostředně sousedních kmitočtových kanálech. Vyjadřuje se jako poměr (v dB) mezi výkonem rušivého signálu v sousedním kanálu a výkonem požadovaného signálu v okamžiku, kdy poměr chybových bitů (BER) přijímače dosáhne stanovené prahové hodnoty. Tento parametr je zásadní pro kmitočtové plánování a efektivitu využití spektra v celulárních sítích.

V praktickém provozu testování ACRR zahrnuje aplikaci modulovaného požadovaného signálu na nominálním kmitočtu kanálu přijímače a současnou aplikaci modulovaného rušivého signálu v sousedním kanálu. Výkon rušivého signálu se zvyšuje, dokud se výkon přijímače nezhorší na stanovenou míru chybovosti, typicky měřenou jako Block Error Rate (BLER) pro datové kanály nebo Bit Error Rate (BER) pro řídicí kanály. Rozdíl mezi výkonem rušivého signálu a výkonem požadovaného signálu v tomto bodě degradace definuje hodnotu ACRR. Vyšší hodnoty ACRR indikují lepší selektivitu přijímače a schopnost potlačení rušení.

Specifikace ACRR se liší v závislosti na technologii rádiového přístupu (UMTS, LTE, NR) a konkrétních používaných kmitočtových pásmech. Specifikace 3GPP definují minimální požadavky ACRR pro přijímače uživatelského zařízení (UE) a základnových stanic napříč různými scénáři nasazení, včetně koexistence se sítěmi jiných operátorů a provozu na sousedních kanálech v rámci stejné sítě. Tyto požadavky zajišťují, že zařízení mohou spolehlivě fungovat v reálných prostředích, kde je spektrum sdíleno mezi více operátory s potenciálně různými úrovněmi vysílacího výkonu.

Prvky návrhu přijímače, které přispívají k výkonu ACRR, zahrnují kvalitu RF filtrů, linearitu šumových zesilovačů, charakteristiky fázového šumu lokálních oscilátorů a algoritmy digitálního zpracování signálu pro potlačení rušení. Selektivita na sousední kanál je primárně určena mezifrekvenčními (IF) filtry přijímače a kanálovými filtry v řetězci základního pásma. Moderní přijímače často využívají pokročilé techniky digitálního filtrování a potlačení rušení, aby překročily minimální požadavky ACRR při zachování energetické účinnosti.

V plánování sítě úvahy o ACRR přímo ovlivňují vzory opakování kmitočtů a požadavky na ochranná pásma mezi operátory. Operátoři s přijímači vykazujícími vynikající výkon ACRR mohou nasazovat sítě s menšími ochrannými pásmy, čímž zvyšují celkovou efektivitu využití spektra. To se stává obzvláště důležitým v milimetrových vlnách pro 5G NR, kde je spektrum cenné a řízení rušení ze sousedního kanálu je klíčové pro udržení vysokých přenosových rychlostí a spolehlivého připojení.

## K čemu slouží

ACRR existuje proto, aby zajistil spolehlivou celulární komunikaci v systémech s více přístupem s kmitočtovým dělením (FDMA), kde více operátorů sdílí sousední přidělení spektra. Bez dostatečné schopnosti potlačení sousedního kanálu by silné signály z přilehlých kanálů přehlušily přijímače, což by způsobovalo přerušení hovorů, snížení datové propustnosti a zhoršení kvality služeb. Tento problém se stává stále závažnějším, jak se spektrum stává přeplněnějším a operátoři nasazují sítě v těsnější kmitočtové blízkosti.

Historicky časné celulární systémy fungovaly s velkorysými ochrannými pásmy mezi přidělením spektra operátorů, aby zmírnily rušení ze sousedního kanálu. Jak se však spektrum stalo vzácným a cenným zdrojem, regulátoři usilovali o maximalizaci využití snížením ochranných pásem a umožněním těsnější kmitočtové koordinace mezi operátory. To vytvořilo potřebu standardizovaných požadavků na výkon přijímače, které by zaručily interoperabilitu a kvalitu služeb i přes snížené kmitočtové oddělení.

Vývoj specifikací ACRR v 3GPP řešil omezení dřívějších systémů, které se spoléhaly na nadměrné kmitočtové oddělení pro řízení rušení. Definováním minimálních požadavků ACRR umožnil 3GPP efektivnější sdílení spektra mezi více operátory při zachování kvality služeb. To bylo obzvláště důležité pro globální harmonizaci celulárních standardů, protože různé regiony měly odlišné přístupy k přidělování spektra a vyžadovaly společný rámec pro výkon přijímače, který by fungoval napříč různými regulačními prostředími.

## Klíčové vlastnosti

- Kvantifikuje schopnost přijímače potlačit rušení ze sousedního kanálu
- Definován jako poměr mezi výkonem rušivého signálu a výkonem požadovaného signálu při stanovené míře chybovosti
- Specifikován samostatně pro různé RAT (UMTS, LTE, NR) a kmitočtová pásma
- Zahrnuje požadavky na charakteristiky modulace jak požadovaného, tak rušivého signálu
- Zohledňuje různé scénáře nasazení včetně koexistence s jinými operátory
- Základní parametr pro kmitočtové plánování a stanovení ochranných pásem

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.116** (Rel-19) — LCR TDD Repeater RF Characteristics
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing

---

📖 **Anglický originál a plná specifikace:** [ACRR na 3GPP Explorer](https://3gpp-explorer.com/glossary/acrr/)
