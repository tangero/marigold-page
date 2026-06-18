---
slug: "etc"
url: "/mobilnisite/slovnik/etc/"
type: "slovnik"
title: "ETC – Extreme Temperature Conditions"
date: 2025-01-01
abbr: "ETC"
fullName: "Extreme Temperature Conditions"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/etc/"
summary: "Soubor podmínek environmentálních testů a požadavků na výkon definovaných 3GPP pro koncové zařízení (UE) a základnové stanice pracující při mimořádně vysokých nebo nízkých teplotách. Zajišťuje spolehl"
---

ETC je soubor podmínek environmentálních testů a požadavků na výkon síťového zařízení definovaných 3GPP, který zajišťuje spolehlivost při mimořádně vysokých nebo nízkých teplotách mimo standardní rozsahy.

## Popis

Extreme Temperature Conditions (ETC, podmínky extrémních teplot) označují přísný soubor provozních environmentálních specifikací v rámci standardů 3GPP, které definují požadavky na výkon, testování a spolehlivost rádiového zařízení, především koncového zařízení (UE) a základnových stanic (eNodeB/gNB), při nasazení v nestandardních teplotních extrémech. Tyto podmínky jsou kategorizovány mimo běžný komerční teplotní rozsah (typicky -10°C až +55°C pro základnové stanice). Specifikace ETC jsou pokryty v řadě technických specifikací (TS), včetně testů shody pro rádiový přenos a příjem (např. TS 36.141 pro stanice [E-UTRA](/mobilnisite/slovnik/e-utra/), TS 38.141 pro stanice NR) a požadavků na výkon (např. TS 36.852, 36.895, 38.884).

Specifikace definují konkrétní teplotní pásma, jako je 'rozšířený' teplotní rozsah (např. -40°C až +55°C) a 'extrémní' teplotní rozsah (např. -40°C až +70°C nebo více pro určité komponenty). Pro každé pásmo standardy ukládají, že zařízení musí splňovat všechny své klíčové parametry [RF](/mobilnisite/slovnik/rf/) výkonu, včetně výkonu vysílače, chyby frekvence, přesnosti modulace ([EVM](/mobilnisite/slovnik/evm/)), citlivosti přijímače a charakteristik zablokování. Testování zahrnuje umístění zařízení do klimatické komory, stabilizaci na cílové extrémní teplotě a následné provedení komplexní sady testů fyzické vrstvy při udržování této teploty. Ověřuje se také schopnost zařízení naběhnout, synchronizovat se, udržovat spojení a provádět předání služby za těchto podmínek.

Z architektonického hlediska splnění požadavků ETC významně ovlivňuje hardwarový design. Vyžaduje použití komponent (oscilátorů, výkonových zesilovačů, filtrů, baterií) dimenzovaných pro rozšířený teplotní rozsah, robustní systémy tepelného managementu (topné články pro chlad, vylepšené chlazení pro horko) a volbu materiálů zabraňujících praskání nebo degradaci. U základnových stanic to může zahrnovat utěsněné, izolované skříně s aktivní regulací teploty. U UE to ovlivňuje chemii baterií a technologii displeje. Úlohou ETC v síti je zaručit flexibilitu nasazení, což operátorům umožňuje instalovat spolehlivé pokrytí mobilní sítí v geograficky náročných prostředích, jako jsou těžební provozy, odlehlé dálnice nebo strategická průmyslová místa, bez degradace služeb způsobené počasím.

## K čemu slouží

Specifikace ETC byly vytvořeny za účelem podpory globálního nasazení systémů 3GPP ve všech geografických a průmyslových prostředích, nejen v mírném podnebí. Před jejich formalizací byla zařízení typicky navrhována a testována pouze pro 'komerční' teplotní rozsahy, což omezovalo spolehlivé nasazení v oblastech s krutými zimami (např. Skandinávie, Kanada) nebo extrémním letním horkem (např. Blízký východ, Austrálie). To vytvářelo mezery v pokrytí a problémy se spolehlivostí pro kritickou komunikaci v těchto oblastech.

Motivace vycházela z požadavků operátorů, regulatorních požadavků na sítě veřejné bezpečnosti a potřeb vertikálních odvětví (energetika, doprava, těžba). Tyto zainteresované strany požadovaly garantovaný výkon pro aplikace kritické z hlediska mise, kde je selhání sítě v důsledku teploty nepřijatelné. Standardy ETC řeší problém interoperability a předvídatelnosti výkonu – zajišťují, že UE certifikované pro extrémní chlad od jednoho výrobce bude spolehlivě fungovat v síti používající základnové stanice od jiného výrobce, které jsou také v souladu s ETC.

Řeší omezení ad-hoc, výrobci specifického zpevnění tím, že poskytují společný, standardizovaný benchmark. To snižuje riziko pro operátory nasazující zařízení v drsných prostředích a podporuje konkurenční trh se specializovaným vybavením. Vývoj ETC v jednotlivých vydáních odráží expanzi do nových kmitočtových pásem (která se mohou s teplotou chovat odlišně), složitějších technologií ([MIMO](/mobilnisite/slovnik/mimo/), agregace nosných) a nových případů užití, jako je IoT, kde mohou být senzory nasazeny v nekontrolovaných prostředích po celé roky.

## Klíčové vlastnosti

- Definuje rozšířené provozní teplotní rozsahy (např. -40°C až +70°C) mimo standardní komerční specifikace
- Specifikuje postupy testů RF shody (výkon, citlivost, EVM) za stabilizovaných extrémních teplot
- Zahrnuje požadavky na výkon a spolehlivost základnových stanic i koncového zařízení (UE)
- Pokrývá provozní scénáře jak pro extrémně nízké, tak pro extrémně vysoké teploty
- Zajišťuje kontinuitu služeb pro kritickou komunikaci při nasazení v drsných podmínkách prostředí
- Ovlivňuje hardwarový design, což vyžaduje komponenty dimenzované na teplotu a systémy tepelného managementu

## Definující specifikace

- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.852** — 3GPP TR 36.852
- **TS 36.895** (Rel-13) — 700 SDL Band for LTE Carrier Aggregation
- **TS 37.806** (Rel-11) — Harmonized Frequency Variant Study for 806-894 MHz
- **TR 38.884** (Rel-18) — Technical Report
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [ETC na 3GPP Explorer](https://3gpp-explorer.com/glossary/etc/)
