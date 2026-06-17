---
slug: "isi"
url: "/mobilnisite/slovnik/isi/"
type: "slovnik"
title: "ISI – Inter Symbol Interference"
date: 2025-01-01
abbr: "ISI"
fullName: "Inter Symbol Interference"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/isi/"
summary: "Inter Symbol Interference (mezisymbolové rušení) je jev zkreslení v digitální komunikaci, kdy vysílané symboly (impulsy) se v důsledku kanálových efektů, jako je vícecestné šíření, vzájemně překrývají"
---

ISI je jev zkreslení v digitální komunikaci, kdy vysílané symboly překrývají a interferují v důsledku kanálových efektů, jako je vícecestné šíření, což narušuje signál.

## Popis

Inter Symbol Interference (ISI) je zásadní porucha v digitálních komunikačních systémech přenášených přes pásmově omezené nebo časově disperzní kanály. V ideálním kanálu by vysílaný symbol (impuls reprezentující bit nebo skupinu bitů) dorazil k přijímači v dokonalém tvaru a omezený na svůj přidělený časový slot. Reálné kanály, zejména bezdrátové rádiové kanály, však nejsou ideální. Vykazují efekty, jako je vícecestné šíření, kdy signál putuje po více drahách různé délky, což způsobuje, že zpožděné kopie téhož symbolu dorazí k přijímači. Konečná šířka pásma kanálu navíc způsobuje časové rozplývání impulsu.

Základním mechanismem ISI je časové rozplývání vysílaného impulsu. Když se impuls rozplývá za svůj určený symbolový interval, překrývá se s časovými sloty následujících (a někdy i předchozích) impulsů. Toto překrytí znamená, že vzorkovací okamžik přijímače pro jeden symbol zachytí energii nejen z tohoto zamýšleného symbolu, ale také ze sousedních symbolů. Toto aditivní rušení narušuje amplitudu a fázi vzorkované hodnoty, což přijímači ztěžuje správné rozhodnutí o tom, který symbol byl vyslán. Výsledkem je zvýšená pravděpodobnost bitových chyb a degradace celkového výkonu systému.

V systémech 3GPP, jako jsou GSM, UMTS a LTE, je ISI významným problémem kvůli vysokým přenosovým rychlostem a složitému bezdrátovému prostředí. Kanál je modelován jako mající určitou impulsní odezvu. Vysílaný signál se s touto odezvou konvoluuje, čímž vzniká přijímaný signál s ISI. Pro potlačení ISI standardy 3GPP na fyzické vrstvě zahrnují několik technik. Patří mezi ně návrh modulačních schémat s vnitřní robustností, použití adaptivních ekvalizérů v přijímači (např. v GSM) a implementace pokročilých vícekanálových technik, jako je ortogonální frekvenční multiplex s dělením ([OFDM](/mobilnisite/slovnik/ofdm/)) používaný v LTE a 5G NR. OFDM efektivně mění vysokorychlostní širokopásmový kanál náchylný k ISI na mnoho nízkorychlostních úzkopásmových podkanálů, kde je ISI v rámci každého podkanálu minimální.

Ekvalizace přijímače je klíčový proces pro zmírnění ISI. Ekvalizér odhadne impulsní odezvu kanálu a poté na přijatý signál aplikuje inverzní filtr, aby 'odstranil' rozplývání a pokusil se rekonstruovat původní vysílané impulsy. Složitost ekvalizéru závisí na závažnosti ISI (rozptyl zpoždění kanálu) a na přenosové rychlosti. Řízení ISI je kritickou součástí adaptace spoje a návrhu systému, přímo ovlivňuje dosažitelnou přenosovou rychlost, pokrytí a kvalitu služby v mobilních sítích.

## K čemu slouží

ISI je zásadní fyzikální omezení, které vyplývá ze snahy přenášet digitální data vysokou rychlostí přes praktické kanály. S rostoucí přenosovou rychlostí se zkracuje symbolový interval (čas na symbol). Když se tento interval zkrátí natolik, že je kratší než časová disperze (rozptyl zpoždění) kanálu způsobená vícecestným šířením, symboly se přirozeně překrývají a vytvářejí rušení. Před rozšířeným použitím ekvalizace a [OFDM](/mobilnisite/slovnik/ofdm/) byla vysokorychlostní komunikace vážně omezena ISI, což omezovalo systémy na nižší přenosové rychlosti nebo vyžadovalo velmi jednoduché kanály.

Problém ISI motivoval vývoj klíčových technologií zpracování signálu v bezdrátových standardech. Rané mobilní systémy jako GSM čelily ISI v městském prostředí s výrazným vícecestným šířením. To vedlo k zařazení sofistikovaných ekvalizérů do GSM mobilních terminálů a základnových stanic. Omezení jednokanálového vysokorychlostního přenosu v disperzních kanálech později motivovalo změnu paradigmatu na vícekanálový přenos. OFDM, přijatý v LTE a 5G, byl speciálně navržen pro potlačení ISI tím, že symbolový interval na každém podkanálu je velmi dlouhý ve vztahu k rozptylu zpoždění kanálu, čímž se ISI v rámci podkanálu téměř eliminuje.

Pochopení a zmírňování ISI je tedy klíčové pro pokrok v mobilním širokopásmovém přenosu. Je to základní problém, který musí návrh fyzické vrstvy vyřešit, aby umožnil vyšší přenosové rychlosti, lepší spektrální účinnost a spolehlivou komunikaci v náročných rádiových prostředích. Vývoj od ekvalizérů v GSM přes techniky rozprostřeného spektra v UMTS k OFDM v LTE/5G představuje trvalé úsilí o překonání této poruchy.

## Klíčové vlastnosti

- Způsobeno časovým rozplýváním vysílaných impulsů v důsledku vícecestného šíření a omezení šířky pásma kanálu
- Výsledkem je překrývání symbolů ve vzorkovacích okamžicích přijímače
- Přímo zvyšuje míru bitových chyb (BER) a degraduje kvalitu signálu
- Závažnost závisí na rozptylu zpoždění kanálu a vysílané symbolové rychlosti
- Potlačováno ekvalizací přijímače a vícekanálovou modulací (např. OFDM)
- Klíčový faktor omezující maximální dosažitelnou přenosovou rychlost v daném kanálu

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [BER – Basic Encoding Rules](/mobilnisite/slovnik/ber/)

## Definující specifikace

- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [ISI na 3GPP Explorer](https://3gpp-explorer.com/glossary/isi/)
