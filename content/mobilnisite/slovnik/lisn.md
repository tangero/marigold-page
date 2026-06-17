---
slug: "lisn"
url: "/mobilnisite/slovnik/lisn/"
type: "slovnik"
title: "LISN – Line Impedance Stabilising Networks"
date: 2025-01-01
abbr: "LISN"
fullName: "Line Impedance Stabilising Networks"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/lisn/"
summary: "LISN (Line Impedance Stabilising Networks, síť pro stabilizaci impedance vedení) jsou součásti testovacího vybavení používané při testování elektromagnetické kompatibility (EMC) telekomunikačních zaří"
---

LISN je součást testovacího vybavení používaná při testování elektromagnetické kompatibility, která poskytuje na napájecích vedeních standardizovanou, stabilní impedanci pro přesné měření emisí vysokofrekvenčního rušení.

## Popis

Line Impedance Stabilising Networks (LISN), známé také jako Artificial Mains Networks nebo V-Networks, jsou pasivní elektronické obvody definované ve specifikacích 3GPP pro testování, jako jsou TS 25.113 (pro UTRA), TS 34.124, TS 36.124 a TS 38.124 (pro testování shody koncových zařízení). Nejde o síťovou funkci, ale o klíčovou součást laboratorního testovacího vybavení používanou pro testování shody s požadavky na elektromagnetickou kompatibilitu ([EMC](/mobilnisite/slovnik/emc/)) uživatelských zařízení (UE) a zařízení základnových stanic. Jejich hlavní funkcí je představovat definovanou, stabilní vysokofrekvenční impedanci (typicky 50 Ohmů) mezi testovaným zařízením ([EUT](/mobilnisite/slovnik/eut/)) a napájecí sítí v širokém frekvenčním rozsahu (např. 150 kHz až 30 MHz nebo výše).

Z hlediska architektury je LISN zařazena do série na střídavém nebo stejnosměrném napájecím vedení k testovanému zařízení (EUT). Skládá se z cívek, kondenzátorů a rezistorů uspořádaných do specifické topologie sítě (často ve tvaru 'V', odtud V-Network). Cívky poskytují vysokou impedanci pro vysokofrekvenční šum z EUT, čímž brání jeho zpětnému toku do napájecí sítě a laboratorní rozvodné sítě, která má proměnnou a neznámou impedanci. Kondenzátory poskytují nízkou impedanci pro tento vysokofrekvenční šum, který je tak směrován na standardizovaný 50-Ohmový měřicí port, kam je připojen spektrální analyzátor nebo přijímač EMI.

Během testování je EUT napájeno přes LISN a provozováno v různých režimech za účelem generování potenciálních emisí. Veškeré vysokofrekvenční šumové proudy generované spínanými zdroji EUT, digitálními obvody nebo jinými zdroji putují po napájecích kabelech. LISN zajišťuje, že tyto proudy vidí na měřicím portu konzistentní zátěž 50 Ohmů bez ohledu na kolísání skutečné impedance sítě. Spektrální analyzátor měří napětí na tomto portu, které přímo koreluje s vedeným emisním proudem z EUT. Toto standardizované uspořádání umožňuje opakovatelná a srovnatelná měření mezi různými testovacími laboratořemi, což je nezbytné pro regulační certifikaci (např. [FCC](/mobilnisite/slovnik/fcc/), [CE](/mobilnisite/slovnik/ce/) značení).

Jejich role je zásadní pro zajištění toho, aby telekomunikační zařízení nevysílala nadměrné elektromagnetické rušení, které by mohlo narušit jiná elektronická zařízení nebo rádiové komunikace. Použitím LISN mohou testovací inženýři přesně kvantifikovat vedené emise na napájecích vedeních, což je jedna z klíčových cest pro elektromagnetické rušení. Specifikace v dokumentech 3GPP definují přesné parametry obvodů a požadavky na výkon pro LISN používané při testování zařízení 3G, 4G a 5G, což zajišťuje globální harmonizaci testovacích metod pro přístup na trh.

## K čemu slouží

LISN existují pro řešení základního problému v testování [EMC](/mobilnisite/slovnik/emc/): nepředvídatelné a proměnlivé impedance reálných střídavých napájecích sítí. Bez stabilizační sítě by vysokofrekvenční šumové proudy vysílané zařízením narazily v různých testovacích laboratořích nebo dokonce v různých časech ve stejné laboratoři na různé impedance, což by vedlo k výrazně odlišným měřením napětí na napájecím portu. To by způsobilo, že testování shody by nebylo opakovatelné a reprodukovatelné, což by podkopalo celý regulační rámec pro elektromagnetickou kompatibilitu.

Tato technologie byla vytvořena za účelem poskytnutí standardizované referenční impedance pro měření vedených emisí, jak vyžadují mezinárodní normy EMC jako CISPR (International Special Committee on Radio Interference). Vložením LISN mezi zařízení a napájecí síť se izolují emise zařízení od nestabilní impedance sítě a poskytuje se čistý, konzistentní 50-Ohmový měřicí bod. To umožňuje spravedlivé a objektivní porovnání úrovní emisí vůči stanoveným limitům.

Její začlenění do specifikací 3GPP (počínaje Rel-4 pro testování UTRA) bylo motivováno potřebou definovat přesné podmínky testování shody pro mobilní zařízení. Jak se zařízení stávala složitějšími a pracovala na vyšších frekvencích, řízení a měření jejich nezamýšlených emisí se stalo klíčovým pro zajištění, že nebudou rušit rádiové sítě, na kterých pracují, ani jiné služby. LISN je základním nástrojem, který umožňuje ověřit, že zařízení vyhovující specifikacím 3GPP splňují přísné předpisy EMC po celém světě, což usnadňuje globální přístup na trh a zajišťuje spolehlivost sítě.

## Klíčové vlastnosti

- Poskytuje standardizovanou, stabilní 50-Ohmovou impedanci pro měření vedených emisí v definovaném frekvenčním rozsahu
- Izoluje testované zařízení (EUT) od proměnné impedance napájecí sítě
- Směruje vysokofrekvenční šumové proudy z EUT na vyhrazený 50-Ohmový měřicí port pro připojení spektrálního analyzátoru
- Definována přesnými parametry obvodů (hodnoty indukčnosti, kapacity) ve specifikacích 3GPP pro testování
- Nezbytná pro opakovatelné a reprodukovatelné testování EMC v souladu s normami jako je CISPR
- Používá se při testování jak zařízení napájených střídavým, tak stejnosměrným proudem

## Definující specifikace

- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 34.124** (Rel-19) — EMC Requirements for 3G UTRA Terminals
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 38.124** (Rel-19) — NR UE EMC Requirements

---

📖 **Anglický originál a plná specifikace:** [LISN na 3GPP Explorer](https://3gpp-explorer.com/glossary/lisn/)
