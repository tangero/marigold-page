---
slug: "gp"
url: "/mobilnisite/slovnik/gp/"
type: "slovnik"
title: "GP – Guard Period"
date: 2026-01-01
abbr: "GP"
fullName: "Guard Period"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gp/"
summary: "Ochranný interval (GP) je časový úsek vložený do rámců E-UTRA TDD, který zabraňuje překryvu přenosů v uplinku a downlinku. Je zásadní pro zvládání časových nejistot a zpoždění šíření mezi UE a eNodeB,"
---

GP (Guard Period) je ochranný interval, časový úsek v rámcích E-UTRA TDD, který zabraňuje překryvu přenosů v uplinku a downlinku tím, že zvládá časové nejistoty a zpoždění šíření, a zajišťuje tak spolehlivý provoz bez rušení.

## Popis

Ochranný interval (GP) je základní součástí struktury rámce s časovým duplexem ([TDD](/mobilnisite/slovnik/tdd/)) v [E-UTRA](/mobilnisite/slovnik/e-utra/) (Evolved UMTS Terrestrial Radio Access), jak je definováno ve specifikacích 3GPP. V TDD systémech je stejné frekvenční pásmo použito pro přenosy v uplinku ([UL](/mobilnisite/slovnik/ul/)) i downlinku ([DL](/mobilnisite/slovnik/dl/)), které jsou odděleny v čase. GP je vyhrazený časový interval uvnitř TDD rámce, konkrétně umístěný mezi downlinkové a uplinkové podrámce nebo speciální podrámce. Jeho primární technická funkce je poskytnout rezervu pro časové nepřesnosti, zpoždění šíření signálu a konečný přepínací čas potřebný pro přechod transceiverů mezi režimy vysílání a příjmu. Bez tohoto ochranného intervalu by se signály z uplinkových přenosů mohly překrývat s koncem downlinkových příjmů na eNodeB nebo jiných UE, což by způsobilo závažné rušení a degradaci výkonu systému.

Z architektonického hlediska je GP integrován do konfigurace TDD rámce definované parametry, jako je konfigurace speciálního podrámce. Speciální podrámec, který existuje v TDD, ale ne ve [FDD](/mobilnisite/slovnik/fdd/), typicky sestává ze tří částí: Downlink Pilot Time Slot (DwPTS), Guard Period (GP) a Uplink Pilot Time Slot (UpPTS). Délka GP je proměnná a je volena na základě velikosti buňky a scénáře nasazení. Pro větší buňky s většími zpožděními šíření je nutný delší GP, aby se vyrovnal čas oběhu signálu mezi eNodeB a vzdálenými UE. eNodeB konfiguruje příslušnou délku GP prostřednictvím vysílaných systémových informací, čímž zajišťuje, že všechna UE v buňce dodržují stejnou časovou strukturu.

Z provozní perspektivy GP funguje tak, že vytváří tiché období, během kterého nedochází k přenosu dat. To poskytuje čas, aby se poslední downlinkový signál rozšířil k UE a aby jej UE zpracovalo a přepnulo své obvody z režimu příjmu do režimu vysílání. Zároveň zajišťuje, že jakýkoli uplinkový přenos z UE nezačne dříve, než je downlinkový příjem na eNodeB zcela ukončen, s ohledem na vzdálenost UE. GP je také klíčový pro podporu funkcí jako je synchronizace uplinku, kde UpPTS následující po GP může být použit pro preambule náhodného přístupu. Jeho přesný výpočet a konfigurace jsou zásadní pro plánování sítě, což ovlivňuje pokrytí buňky, kapacitu a koexistenci s jinými TDD systémy.

## K čemu slouží

Ochranný interval existuje, aby řešil základní výzvu rušení v [TDD](/mobilnisite/slovnik/tdd/) rádiových systémech. Ve sdíleném frekvenčním pásmu, pokud nejsou uplinkové a downlinkové přenosy dokonale odděleny v čase, dojde ke kolizi, což učiní komunikaci nespolehlivou. Rané TDD systémy trpěly takovým rušením kvůli nedokonalému přepínání zařízení a zpožděním šíření signálu. GP byl zaveden jako strukturované, standardizované řešení pro vložení řízeného, předvídatelného intervalu ticha, který poskytuje potřebnou časovou rezervu pro tyto fyzikální a procedurální omezení.

Historicky, jak se mobilní systémy vyvíjely směrem k vyšším datovým rychlostem a efektivnějšímu využití spektra s LTE, získal TDD na významu díky své flexibilitě v alokaci kapacity mezi uplink a downlink. Tato flexibilita však zvýšila složitost časového sladění. GP překonal omezení předchozích, méně formalizovaných přístupů s ochranným pásmem tím, že jej přímo integroval do specifikace rámce. Umožňuje síťovým operátorům nasazovat buňky různé velikosti – od malých indoor femtobuněk po velké venkovské makrobuňky – pouhou úpravou délky GP v konfiguraci speciálního podrámce, čímž zajišťuje spolehlivý provoz ve všech scénářích nasazení.

## Klíčové vlastnosti

- Integrován do struktury speciálního podrámce E-UTRA TDD mezi DwPTS a UpPTS
- Konfigurovatelná délka pro podporu různých velikostí buněk a zpoždění šíření
- Zabraňuje překryvu a rušení mezi uplinkovými a downlinkovými přenosy
- Poskytuje čas pro přepínání transceiverů UE a eNodeB mezi režimy Tx a Rx
- Zásadní pro udržování časové synchronizace uplinku v síti
- Parametry definované ve specifikacích 3GPP pro konzistentní implementaci

## Související pojmy

- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [E-UTRA – Enhanced Universal Terrestrial Radio Access](/mobilnisite/slovnik/e-utra/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements
- **TR 38.812** (Rel-16) — Study on NOMA for NR

---

📖 **Anglický originál a plná specifikace:** [GP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gp/)
