---
slug: "kbd"
url: "/mobilnisite/slovnik/kbd/"
type: "slovnik"
title: "KBD – Kaiser-Bessel Derived"
date: 2025-01-01
abbr: "KBD"
fullName: "Kaiser-Bessel Derived"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/kbd/"
summary: "KBD je okénková funkce používaná ve specifikacích 3GPP pro spektrální tvarování a filtrování, zejména při odhadu kanálu a zpracování vlnových forem OFDM/OFDMA. Poskytuje řízený kompromis mezi šířkou h"
---

KBD je okénková funkce používaná ve specifikacích 3GPP pro spektrální tvarování a filtrování, která optimalizuje kvalitu signálu kompromisem mezi šířkou hlavního laloku a potlačením postranních laloků.

## Popis

Funkce Kaiser-Bessel Derived (KBD) je specializovaná okénková funkce definovaná ve specifikacích 3GPP, nejvýznamněji v TS 26.403 pro testování audio kodeků. Je matematicky odvozena od Kaiser-Besselova okna, což je samo o sobě parametrizovaná okénková funkce známá svými téměř optimálními vlastnostmi koncentrace energie. KBD okno je konstruováno tak, že se vezme druhá odmocnina koeficientů diskrétního Kaiser-Besselova okna a následně se aplikuje odvozený sumární proces, což vede k oknu s vynikajícími charakteristikami ve frekvenční oblasti pro návrh filtrů s konečnou impulsní odezvou ([FIR](/mobilnisite/slovnik/fir/)) a spektrální analýzu. Její primární architektonická role spočívá v řetězci zpracování signálu fyzické vrstvy, kde funguje jako funkce zužování v časové oblasti aplikovaná na bloky signálu před jejich transformací do frekvenční oblasti, například v systémech s ortogonálním frekvenčním multiplexem ([OFDM](/mobilnisite/slovnik/ofdm/)) nebo během procedur odhadu kanálu.

Při provozu je KBD okno aplikováno na blok vzorků v časové oblasti, aby se snížilo spektrální rozlití způsobené nespojitostmi na okrajích bloku. To je klíčové u vícekanálových systémů, jako jsou LTE a NR, kde musí být zachována přesná ortogonalita subnosných, aby se zabránilo interferenci mezi nosnými ([ICI](/mobilnisite/slovnik/ici/)). Tvar okna je řízen parametrem, často alfa (α), který upravuje kompromis mezi šířkou hlavního laloku (ovlivňující frekvenční rozlišení) a útlumem postranních laloků (ovlivňující emise mimo pásmo a potlačení interference). Vyšší hodnota alfa zvyšuje útlum postranních laloků, ale rozšiřuje hlavní lalok. Funkce je typicky implementována v digitálních signálových procesorech ([DSP](/mobilnisite/slovnik/dsp/)) nebo specializovaném hardwaru v základnové jednotce uživatelského zařízení (UE) a gNodeB.

Klíčové komponenty zahrnující KBD zahrnují banky filtrů používané v modulaci a demodulaci, algoritmy odhadu kanálu vyžadující přesnou spektrální analýzu a audio procesní kodeky, kde definuje analytická a syntetická okna. Její role je zásadní pro zajištění, aby vysílané signály splňovaly požadavky spektrální masky, minimalizovaly poměr úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)) a zlepšovaly přesnost zpětné vazby o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)). Díky poskytnutí matematicky dobře definovaného a standardizovaného okna zajišťuje KBD interoperabilitu a konzistentní výkon napříč zařízeními různých výrobců, což je nezbytné pro spolehlivý provoz mobilních sítí.

## K čemu slouží

Okénková funkce KBD byla zavedena, aby uspokojila potřebu standardizované, vysoce výkonné techniky oken v digitálním zpracování signálu pro telekomunikace. Před její standardizací byly používány různé ad-hoc okénkové funkce (jako Hann, Hamming nebo Blackman), což vedlo k nekonzistencím ve výkonu filtrů, kontrole spektrálního rozlití a nakonec k výzvám v interoperabilitě mezi síťovými zařízeními různých výrobců. Kaiser-Besselovo okno bylo již v literatuře o zpracování signálu známé svou optimalitou v koncentraci energie a jeho odvozená verze (KBD) byla vybrána 3GPP, aby poskytla rigorózní referenční bod pro testování audio kvality a spolehlivý nástroj pro návrh fyzické vrstvy.

Historicky, jak se mobilní systémy vyvíjely směrem k rádiovým rozhraním založeným na [OFDM](/mobilnisite/slovnik/ofdm/) s LTE, výrazně vzrostla poptávka po přesném spektrálním tvarování. OFDM je citlivý na nespojitosti v časové oblasti, které mohou narušit ortogonalitu subnosných. KBD okno nabízí parametrizovatelné řešení, které mohou systémoví návrháři ladit tak, aby splňovalo specifické limity emisí mimo pásmo a požadavky na zkreslení v pásmu definované regulačními orgány. Jeho vytvoření bylo motivováno potřebou posunout se za jednodušší okna nabízející pevné kompromisy, což umožňuje optimalizaci přizpůsobenou specifickým šířkám pásma a podmínkám kanálu v systémech 3GPP.

Dále, v kontextu testování audio kodeků (jeho primární specifikace v TS 26.403), slouží KBD jako kritická komponenta pro objektivní měření percepční kvality. Používá se v percepčním hodnocení kvality řeči ([PESQ](/mobilnisite/slovnik/pesq/)) a dalších algoritmech k okenování audio signálů před transformací, což zajišťuje reprodukovatelnost testů a dobrou korelaci se subjektivními poslechovými testy u lidí. Tato standardizace zajišťuje konzistentnost hodnocení kvality hlasu v celém odvětví, což podporuje zlepšování v návrhu kodeků a plánování sítí pro hlasové služby.

## Klíčové vlastnosti

- Parametrizovatelný tvar řízený parametrem alfa (α) pro optimalizaci kompromisu
- Vynikající vlastnosti útlumu postranních laloků snižující emise mimo pásmo
- Téměř optimální koncentrace energie ve frekvenční oblasti
- Standardizovaná definice v 3GPP zajišťující interoperabilitu
- Používá se v okenování cyklické předpony OFDM/OFDMA a při odhadu kanálu
- Aplikována při testování audio kodeků pro měření percepční kvality

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)

## Definující specifikace

- **TS 26.403** (Rel-19) — Enhanced aacPlus AAC Encoder Specification

---

📖 **Anglický originál a plná specifikace:** [KBD na 3GPP Explorer](https://3gpp-explorer.com/glossary/kbd/)
