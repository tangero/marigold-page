---
slug: "bwsan"
url: "/mobilnisite/slovnik/bwsan/"
type: "slovnik"
title: "BWSAN – SAN Transponder Bandwidth"
date: 2025-01-01
abbr: "BWSAN"
fullName: "SAN Transponder Bandwidth"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bwsan/"
summary: "BWSAN definuje šířku pásma přidělenou transpondéru satelitní přístupové sítě (SAN). Jde o klíčový parametr zdroje v 5G neterestrických sítích (NTN), který určuje maximální dostupnou kapacitu rádiového"
---

BWSAN je šířka pásma přidělená transpondéru satelitní přístupové sítě (SAN), která určuje maximální kapacitu rádiového kmitočtového spektra pro komunikaci v 5G neterestrických sítích.

## Popis

BWSAN ([SAN](/mobilnisite/slovnik/san/) Transponder Bandwidth) je základní technický parametr definovaný ve standardech 3GPP pro neterestrické sítě ([NTN](/mobilnisite/slovnik/ntn/)). Odkazuje na celkovou šířku rádiového kmitočtového pásma přidělenou jednomu transpondéru na palubě satelitu v rámci satelitní přístupové sítě (SAN). Tato šířka pásma představuje maximální dostupný spektrální zdroj pro rádiové rozhraní mezi satelitem a uživatelskými zařízeními (UE) na zemi. Transpondér funguje jako kmitočtový převodník a zesilovač, který přijímá signály v uplinku od UE v určitém kmitočtovém pásmu, převádí je a retransponuje v downlinkovém pásmu. Parametr BWSAN zahrnuje celý tento přidělený spektrální zdroj pro provoz daného transpondéru.

Z architektonického hlediska je transpondér SAN klíčovou komponentou fyzické vrstvy v kosmickém segmentu. Nachází se v užitečném zatížení satelitu a komunikuje s jeho anténami. Šířka pásma definovaná BWSAN je sdíleným zdrojem pro všechna UE obsluhovaná satelitním svazkem nebo oblastí pokrytí spojenou s tímto transpondérem. Operátoři sítí a poskytovatelé satelitních služeb konfigurují tuto hodnotu na základě technických možností satelitu, regulačních přidělení spektra a zamýšleného profilu služeb (např. enhanced Mobile Broadband (eMBB) nebo IoT). Specifikace BWSAN v dokumentech 3GPP, jako je TS 38.108 (pro NTN založené na NR) a TS 36.181 (pro NTN založené na LTE), zajišťuje standardizovanou interoperabilitu a předvídatelný výkon pro implementace UE.

Role BWSAN v síti je klíčová pro plánování kapacity, výpočty rozpočtu spoje a plánovací algoritmy. Přímo omezuje celkovou datovou rychlost, kterou lze podpořit v satelitní buňce. Vyšší hodnoty BWSAN umožňují obsloužit více uživatelů, vyšší propustnost na uživatele nebo kombinaci obojího, jsou však omezeny hardwarovými možnostmi a licencováním spektra. Při návrhu systému je BWSAN klíčovým vstupem pro stanovení maximální dosažitelné spektrální účinnosti a pro dimenzování dalších síťových parametrů, jako je počet zdrojových bloků nebo subnosičů dostupných v [OFDM](/mobilnisite/slovnik/ofdm/) rádiovém rozhraní 5G NR-NTN nebo LTE-NTN.

Z procedurálního hlediska musí gNodeB (gNB) v architektuře NR-NTN, který může být umístěn na zemi (gNB-g) nebo částečně na satelitu (gNB-s), znát omezení BWSAN. Tato znalost ovlivňuje funkce správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)), jako je řízení přístupu, plánování paketů a konfigurace částí pásma ([BWP](/mobilnisite/slovnik/bwp/)). Plánovač uvnitř gNB přiděluje uživatelským zařízením (UE) fyzické zdrojové bloky ([PRB](/mobilnisite/slovnik/prb/)), ale celkový počet přidělitelných PRB je zásadně omezen hodnotou BWSAN. Přesná charakterizace a signalizace tohoto parametru jsou proto nezbytné pro efektivní a spravedlivé využití zdrojů v oblasti pokrytí satelitu.

## K čemu slouží

Specifikace BWSAN ve standardech 3GPP řeší kritickou potřebu modelovat a řídit jedinečné, omezené zdrojové prostředí satelitní komunikace v rámci 5G ekosystému. Před integrací [NTN](/mobilnisite/slovnik/ntn/) do 3GPP terestrické sítě pracovaly s předpoklady o šířce pásma vázanými na vysoce kontrolovaná, hustá nasazení základnových stanic s hojnou optickou páteřní sítí. Satelitní spoje jsou však charakterizovány omezenými, drahými a sdílenými zdroji šířky pásma na transpondéru, vysokou latencí a dynamickými podmínkami spoje. Definice BWSAN poskytuje standardizovaný způsob, jak tento primární omezení kvantifikovat, což umožňuje konzistentní simulaci systému, hodnocení výkonu a specifikaci chování UE napříč průmyslem.

K jejímu vytvoření vedla snaha o bezproblémovou integraci neterestrických sítí s 5G s cílem poskytnout všudypřítomné pokrytí včetně odlehlých a námořních oblastí. K dosažení tohoto cíle vyžadoval standardizační proces 3GPP přesné technické parametry pro popis schopností satelitního rádiového rozhraní. BWSAN slouží jako jeden z těchto základních parametrů a řeší problém, jak začlenit pevný limit [RF](/mobilnisite/slovnik/rf/) šířky pásma satelitního transpondéru do rámců správy zdrojů LTE a NR. Umožňuje optimalizovat síťové algoritmy a implementace UE pro známý kapacitní strop, čímž zlepšuje celkovou efektivitu systému a uživatelský zážitek v NTN scénářích.

Historicky satelitní komunikační systémy definovaly šířku pásma transpondéru nezávisle na standardech mobilních sítí. Zařazení BWSAN do Rel-17 představuje klíčový krok ve sbližování terestrických a neterestrických sítí pod jednotným standardem. Řeší omezení předchozích standardů mobilních sítí, kterým chyběl jakýkoli formální model pro zdroje satelitních spojů, tím, že poskytuje konkrétní, měřitelný atribut použitelný v rovnicích rozpočtu spoje, nástrojích pro plánování kapacity a stavových automatech protokolu. To umožňuje vývoj UE a síťových funkcí, které jsou skutečně vědomé a adaptivní na specifická omezení satelitního přístupu.

## Klíčové vlastnosti

- Definuje maximální RF šířku pásma jako zdroj satelitního transpondéru.
- Kritický vstup pro výpočet rozpočtu spoje a kapacity v NTN.
- Standardizovaný parametr pro interoperabilitu mezi sítí a UE.
- Základní omezení pro plánování ve správě rádiových zdrojů (RRM).
- Specifikován samostatně pro různé RAT (NR a LTE) v kontextech NTN.
- Umožňuje přesnou simulaci systému a benchmarkování výkonu pro satelitní spoje.

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)
- [SAN – Satellite Access Node](/mobilnisite/slovnik/san/)

## Definující specifikace

- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing

---

📖 **Anglický originál a plná specifikace:** [BWSAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/bwsan/)
