---
slug: "dd"
url: "/mobilnisite/slovnik/dd/"
type: "slovnik"
title: "DD – Delay Diversity"
date: 2026-01-01
abbr: "DD"
fullName: "Delay Diversity"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dd/"
summary: "Delay Diversity (DD, diverzita se zpožděním) je technika vysílací diverzity používaná v bezdrátových systémech ke zvýšení odolnosti signálu proti únikům. Spočívá ve vysílání více kopií téhož signálu s"
---

DD je technika vysílací diverzity, která zlepšuje odolnost signálu vysíláním zpožděných kopií téhož signálu z více antén, čímž vytváří frekvenčně selektivní kanál pro zvýšení spolehlivosti příjmu.

## Popis

Delay Diversity (DD, diverzita se zpožděním) je základní technika vysílací diverzity implementovaná na fyzické vrstvě bezdrátových komunikačních systémů, zejména v rámci standardů 3GPP jako LTE a NR. Funguje tak, že z více vysílacích antén jsou vysílány identické datové toky, ale každý tok je záměrně zpožděn o specifický, předem definovaný cyklický posuv nebo časový offset vůči ostatním. Tento proces transformuje plochý únikový kanál na frekvenčně selektivní únikový kanál na straně přijímače. Přijímač, typicky vybavený jedinou anténou, vnímá tyto zpožděné kopie jako vícecestné složky. K využití této uměle vytvořené vícecestné diverzity jsou pak použity pokročilé techniky ekvalizace, jako je ekvalizace ve frekvenční oblasti (FDE) v systémech založených na [OFDM](/mobilnisite/slovnik/ofdm/), které signály konstruktivně kombinují, aby zmírnily hluboké úniky a zlepšily celkový poměr signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)).

Základní mechanismus DD spočívá v aplikaci cyklického zpoždění na základnový signál v časové oblasti před vysíláním. V systémech OFDM se cyklické zpoždění v časové oblasti převádí na fázový posuv ve frekvenční oblasti napříč podnosnými. Tento fázový posuv je lineární s frekvencí, čímž vytváří virtuální frekvenčně selektivní kanál. Odhadovač kanálu přijímače změří tuto efektivní odezvu kanálu a ekvalizér kompenzuje zavedenou frekvenční selektivitu. Klíčové parametry zahrnují hodnoty zpoždění (často specifikované ve vzorcích nebo časových jednotkách, jako jsou mikrosekundy) a počet vysílacích antén. Zpoždění jsou typicky volena tak, aby spadala do doby trvání cyklické předpony, aby se zabránilo intersymbolovému rušení ([ISI](/mobilnisite/slovnik/isi/)), a zůstala tak konstruktivními vícecestnými složkami, které přijímač dokáže rozlišit.

Z architektonického hlediska je DD implementována v rámci řetězce zpracování fyzické vrstvy základnové stanice (eNodeB v LTE, gNB v NR), konkrétně ve fázi předkódování nebo mapování na antény. Nevyžaduje explicitní zpětnou vazbu od uživatelského zařízení (UE), což z ní činí schéma otevřené smyčky vhodné pro scénáře vysokých rychlostí, kde je zpětná vazba o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) nespolehlivá. Tato technika je často specifikována ve spojení s jinými diverzitními metodami, jako je Space-Frequency Block Coding (SFBC), nebo je používána v módech jako Transmit Diversity (TxD) pro řídicí kanály a specifické referenční signály. Jejím úkolem je zvýšit odolnost vysílacích kanálů, synchronizačních signálů a kritických řídicích informací, čímž zajišťuje spolehlivé připojení na okrajích buňky nebo v náročných rádiových podmínkách.

Z pohledu standardů je DD podrobně popsána ve specifikacích 3GPP upravujících procedury fyzické vrstvy. Například v LTE (od verze Rel-8) se aplikuje pro vysílání na dvou nebo čtyřech anténních portech pomocí Cell-specific Reference Signals ([CRS](/mobilnisite/slovnik/crs/)). Konkrétní hodnoty cyklického zpoždění a jejich aplikace na zdrojové elementy jsou definovány tak, aby byla zajištěna interoperabilita. V NR, přestože převažuje beamforming, mohou být principy DD stále využívány v některých víceanténních vysílacích schématech pro zvýšení pokrytí, zejména pro signály počátečního přístupu jako [SS](/mobilnisite/slovnik/ss/)/[PBCH](/mobilnisite/slovnik/pbch/) bloky.

## K čemu slouží

Delay Diversity byla zavedena, aby bojovala proti škodlivým účinkům vícecestného úniku v bezdrátových kanálech, aniž by vyžadovala více přijímacích antén v uživatelském zařízení. Před jejím přijetím systémy silně spoléhaly na přijímací diverzitu nebo složitá schémata vysílací diverzity s uzavřenou smyčkou, což zvyšovalo náklady a složitost UE nebo vyžadovalo zpětnou vazbu s nízkou latencí. DD poskytuje jednoduché, efektivní řešení otevřené smyčky, které zlepšuje spolehlivost spojení a plochu pokrytí, což je nezbytné pro služby vyžadující konzistentní kvalitu, jako je streamování hlasu a videa.

Primární problém, který řeší, je degradace výkonu způsobená plochým únikem, kdy signál zažívá jednotné útlumy v celém svém pásmu, což vede k hlubokým únikům a vysokým chybovostem. Umělým vytvořením frekvenčně selektivního úniku prostřednictvím zpožděného vysílání DD zajišťuje, že různé frekvenční složky signálu únikají nezávisle. Tato diverzita ve frekvenční oblasti umožňuje mechanismům opravy chyb v přijímači efektivněji obnovit signál. Historicky, jak se mobilní sítě vyvíjely, aby podporovaly vyšší datové rychlosti a lepší spektrální účinnost s [OFDM](/mobilnisite/slovnik/ofdm/) v LTE, se techniky jako DD staly nedílnou součástí udržování robustního výkonu pro řídicí signalizaci a vysílací kanály, které jsou kritické pro provoz sítě a uživatelský zážitek.

Dále DD řeší výzvu implementace vysílací diverzity v prostředích s vysokou mobilitou. Techniky s uzavřenou smyčkou, které přizpůsobují předkódování na základě zpětné vazby od UE, se stávají neúčinnými, když se kanál rychle mění v důsledku vysokého Dopplerova rozprostření. Protože je DD otevřená smyčka a nezávisí na okamžitém CSI, zůstává robustní i za takových podmínek. To z ní učinilo základní technologii pro LTE již od jejího zavedení v Rel-8, zajišťující spolehlivé downlinkové vysílání pro pohybující se vozidla a rychle se pohybující uživatele, čímž se zvýšila celková spolehlivost sítě a kontinuita služeb.

## Klíčové vlastnosti

- Technika vysílací diverzity otevřené smyčky nevyžadující zpětnou vazbu od UE
- Přeměňuje plochý únikový kanál na frekvenčně selektivní únikový kanál pro zisk z diverzity
- Používá cyklická zpoždění aplikovaná v časové oblasti, kompatibilní s cyklickou předponou OFDM
- Zvyšuje odolnost řídicích kanálů a vysílacích signálů
- Vhodná pro scénáře s vysokou mobilitou díky nezávislosti na zpětné vazbě CSI
- Implementována s více vysílacími anténami na základnové stanici (eNodeB/gNB)

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.548** (Rel-19) — SEAL Data Delivery Server Services Stage 3
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TR 38.859** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [DD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dd/)
