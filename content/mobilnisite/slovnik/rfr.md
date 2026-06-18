---
slug: "rfr"
url: "/mobilnisite/slovnik/rfr/"
type: "slovnik"
title: "RFR – Receive Frequency Response"
date: 2025-01-01
abbr: "RFR"
fullName: "Receive Frequency Response"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/rfr/"
summary: "Receive Frequency Response (RFR, frekvenční charakteristika přijímače) je klíčová metrika výkonu rádiového přijímače uživatelského zařízení (UE). Kvantifikuje změnu zesílení či útlumu v rámci provozní"
---

RFR je přijímací metrika, která kvantifikuje změnu zesílení v rámci frekvenčního pásma a charakterizuje schopnost UE (uživatelského zařízení) zpracovávat signály rovnoměrně pro konzistentní propustnost v systémech jako je 5G NR.

## Popis

Receive Frequency Response (RFR, frekvenční charakteristika přijímače) je standardizované měření definované ve specifikacích 3GPP pro vyhodnocení linearity a rovnoměrnosti frekvenční charakteristiky přijímače UE v rámci jeho určené šířky kanálu. Je to kritický parametr pro zajištění integrity signálu a minimalizaci zkreslení v přijímaném signálu. Měření RFR charakterizuje, jak se zesílení přijímače mění v závislosti na frekvenci v rámci aktivní šířky pásma, v podstatě mapuje přenosovou funkci přijímače. Rovnoměrná frekvenční charakteristika je žádoucí, neboť značí stejnoměrné zesílení napříč všemi subnosnými, což je zásadní pro systémy založené na ortogonálním frekvenčním multiplexu ([OFDM](/mobilnisite/slovnik/ofdm/)), jako je 5G New Radio (NR) a LTE. Významné změny nebo vlnění v RFR mohou vést k interferenci mezi nosnými ([ICI](/mobilnisite/slovnik/ici/)), degradaci přesnosti modulace ([EVM](/mobilnisite/slovnik/evm/)) a následně ke snížení propustnosti a zvýšení míry chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)).

Měření RFR se typicky provádí za kontrolovaných laboratorních podmínek pomocí standardizovaných testovacích modelů definovaných ve specifikacích 3GPP pro testy shody. Do UE je přiveden známý referenční měřicí kanálový ([RMC](/mobilnisite/slovnik/rmc/)) signál a přijatý signál je analyzován pro určení relativního zesílení v různých frekvenčních bodech. Výsledky jsou často prezentovány jako křivka zobrazující relativní výkon (v dB) v závislosti na frekvenčním odstupu od středu nosné. Specifikace definují maximální povolené tolerance nebo masky pro RFR, aby byla zajištěna interoperabilita a základní výkonnost. Pro 5G NR jsou požadavky podrobně popsány v TS 38.106 a zohledňují faktory jako šířka pásma, frekvenční rozsah (FR1 nebo FR2) a třída schopností UE.

Z architektonického hlediska je RFR ovlivněno několika komponentami v přijímacím řetězci UE, včetně antény, filtrů [RF](/mobilnisite/slovnik/rf/) předřadníku, šumového zesilovače ([LNA](/mobilnisite/slovnik/lna/)), mísičů a analogově-digitálního převodníku ([ADC](/mobilnisite/slovnik/adc/)). Nedokonalosti kterékoliv z těchto komponent mohou přispět k neideální frekvenční charakteristice. Zpracování základního pásma digitálním signálovým procesorem (DSP) může zahrnovat vyrovnávací filtry pro kompenzaci některých těchto analogových zkreslení, ale celková RFR je kombinovanou charakteristikou analogové a digitální domény. Operátoři sítí a výrobci UE používají data RFR k ověření návrhu, zajištění shody a řešení problémů s výkonem souvisejících s pokrytím nebo datovou rychlostí v konkrétních frekvenčních pásmech.

V širším systémovém kontextu je RFR jednou z několika charakteristik přijímače vedle parametrů, jako je referenční citlivost, selektivita sousedního kanálu (ACS) a blokování. Dobře řízená RFR zajišťuje, že UE může efektivně demodulovat modulační schémata vyššího řádu (např. 256QAM, 1024QAM) v celé šířce kanálu, čímž maximalizuje spektrální účinnost. Je obzvláště důležitá pro scénáře agregace nosných (CA), kde musí UE současně přijímat na více komponentních nosných, které mohou mít různá střední kmitočty a vyžadují konzistentní výkon v širší agregované šířce pásma.

## K čemu slouží

Účelem standardizace Receive Frequency Response (RFR, frekvenční charakteristiky přijímače) je stanovit společnou, kvantifikovatelnou metriku pro hodnocení linearity a rovnoměrnosti v pásmu u přijímačů UE. Před takovou standardizací se mohl výkon přijímače významně lišit mezi různými modely zařízení, což vedlo k nepředvídatelnému výkonu sítě a potenciálním problémům s interoperabilitou. Definováním konkrétních požadavků na RFR zajišťuje 3GPP minimální základní výkonnostní úroveň, kterou musí splňovat všechna kompatibilní UE, čímž podporuje spravedlivý a konzistentní uživatelský zážitek bez ohledu na výrobce zařízení.

RFR řeší technickou výzvu udržení věrnosti signálu v širokopásmových a vysokopropustných bezdrátových systémech. Jak se buněčné technologie vyvíjely z úzkopásmových systémů na širokopásmové systémy založené na OFDM (LTE a 5G NR), dopad neideálních frekvenčních charakteristik přijímače se stal výraznějším. Změny zesílení v pásmu mohou zkreslit ortogonální subnosné v OFDM, narušit jejich ortogonalitu a způsobit interferenci. To je zvláště kritické pro dosažení vysokých datových rychlostí slibovaných 5G, které se spoléhají na efektivní využití širokých šířek pásma a modulace vyššího řádu. Specifikace RFR pomáhají zmírnit tato zkreslení na úrovni zařízení.

Dále je testování RFR základní součástí schvalování typu UE a testů shody. Poskytuje regulátorům a operátorům sítí objektivní důkaz, že zařízení bude v živých sítích adekvátně fungovat. Z hlediska návrhu požadavky na RFR vedou RF inženýry UE při výběru komponent a návrhu filtrů a zesilovacích stupňů, které splňují přísné požadavky na rovnoměrnost bez nadměrných nákladů nebo spotřeby energie. Řeší problém nekontrolovaného zkreslení signálu způsobeného přijímačem, které by, pokud by zůstalo bez kontroly, omezilo praktické datové rychlosti a pokrytí, které může síť koncovým uživatelům poskytnout.

## Klíčové vlastnosti

- Kvantifikuje změnu zesílení přijímače v rámci provozní šířky kanálu
- Definována pomocí standardizovaných testovacích modelů a měřicích postupů ve specifikacích 3GPP
- Kritická pro výkon systémů založených na OFDM (LTE, 5G NR)
- Ovlivňuje přesnost modulace (EVM) a interferenci mezi nosnými (ICI)
- Požadavky specifikovány zvlášť pro různé frekvenční rozsahy (FR1, FR2) a šířky pásma
- Ovlivněna analogovým RF předřadníkem a zpracováním digitálního signálu v základním pásmu

## Související pojmy

- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)
- [ACS – Auto-Configuration Server](/mobilnisite/slovnik/acs/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TS 26.801** (Rel-19) — Testing UEs with Non-Traditional Earpieces
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception

---

📖 **Anglický originál a plná specifikace:** [RFR na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfr/)
