---
slug: "sqrt"
url: "/mobilnisite/slovnik/sqrt/"
type: "slovnik"
title: "SQRT – SQuare RooT"
date: 2025-01-01
abbr: "SQRT"
fullName: "SQuare RooT"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sqrt/"
summary: "SQRT je matematická funkce používaná ve specifikacích 3GPP pro výpočty při zpracování signálu, zejména při testování výkonu a ověřování shody základnových stanic. Je definována v kontextu testovacích"
---

SQRT je matematická funkce používaná ve specifikacích 3GPP pro výpočty při zpracování signálu, zejména při testování výkonu a ověřování shody základnových stanic pro výpočet středních kvadratických hodnot (RMS).

## Popis

V rámci technických specifikací 3GPP, konkrétně TS 36.141, která definuje testování shody základnových stanic ([E-UTRA](/mobilnisite/slovnik/e-utra/)), se SQRT vztahuje k matematické operaci druhé odmocniny. Nejde o samostatný síťový protokol nebo funkci, ale o základní výpočetní prvek zabudovaný do testovacích postupů a vzorců požadavků na výkon. Jeho hlavní uplatnění je při výpočtu středních kvadratických hodnot ([RMS](/mobilnisite/slovnik/rms/)) pro různá měření rádiové frekvence ([RF](/mobilnisite/slovnik/rf/)), jako je velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)), únik nosné a emise v pásmu/mimo pásmo. Tyto výpočty jsou klíčové pro kvantifikaci kvality a čistoty vysílaného signálu z eNodeB nebo gNB.

Specifikace používá funkci SQRT ve složitých rovnicích, které definují kritéria vyhovění/nevyhovění pro charakteristiky vysílače a přijímače základnové stanice. Například při měření EVM – klíčového ukazatele přesnosti modulace – norma definuje měřicí období a metodu výpočtu chybového vektoru pro každý demodulovaný symbol. Střední kvadratická hodnota EVM se pak získá tak, že se vezme druhá odmocnina z průměru kvadrátů velikostí těchto chybových vektorů vzhledem k průměru kvadrátů velikostí referenčních symbolů. Tato přesná matematická definice zajišťuje standardizované, opakovatelné a srovnatelné výsledky testů mezi různými výrobci a testovacími laboratořemi.

Přestože se jedná o zdánlivě základní operaci, explicitní definice a konzistentní použití operace SQRT jsou zásadní pro interoperabilitu a shodu. Standardy 3GPP musí jednoznačně definovat každý parametr a výpočet, aby se předešlo rozdílům v interpretaci, které by mohly vést k zařazení nevyhovujícího zařízení do sítě. SQRT je tedy nedílnou součástí přísného matematického rámce, který podmiňuje požadavky na výkon fyzické vrstvy pro rádiová zařízení LTE a NR, a zajišťuje tak, že sítě poskytují zamýšlenou kvalitu služeb.

## K čemu slouží

Účelem explicitního definování funkce SQRT ve specifikacích 3GPP je zajistit absolutní matematickou jasnost a odstranit nejednoznačnost v postupech testování shody. Bezdrátové standardy musí definovat výkonnostní limity pomocí přesných a reprodukovatelných vzorců. Bez standardizované definice základních operací, jako je druhá odmocnina, by různí výrobci testovacích zařízení nebo základnových stanic mohli implementovat drobné odchylky v pořadí výpočtů nebo numerických metodách, což by vedlo k nekonzistentním výsledkům testů a potenciálním sporům o shodu.

Historicky, jak se buněčná technologie vyvíjela od 2G přes 3G k LTE a 5G NR, prudce rostla složitost modulačních schémat (jako 64-QAM, 256-QAM) a přísnost výkonnostních požadavků. Metriky jako [EVM](/mobilnisite/slovnik/evm/) se staly klíčovými pro zajištění vysokých přenosových rychlostí a spektrální účinnosti. Vytvoření podrobných testovacích specifikací, jako je TS 36.141, bylo motivováno potřebou garantovat, že všechny základnové stanice, bez ohledu na výrobce, splňují minimální výkonnostní práh, který zaručuje interoperabilitu sítě a uživatelský zážitek. Definice SQRT je malou, ale nezbytnou součástí budování tohoto rigorózního a jednoznačného testovacího základu.

Řeší omezení neformálních nebo implicitních matematických definic v technických specifikacích. Formálním uvedením SQRT v normativním textu zajišťuje 3GPP, že každá testovací laboratoř pro shodu na celém světě vypočítává kritické parametry [RF](/mobilnisite/slovnik/rf/) naprosto stejným způsobem. To podporuje spravedlivé konkurenční prostředí pro výrobce zařízení a dává provozovatelům sítí důvěru ve výkon nasazené infrastruktury, což je zásadní pro udržení celkové kvality a spolehlivosti sítě.

## Klíčové vlastnosti

- Matematická funkce pro výpočet střední kvadratické hodnoty (RMS)
- Definována v rámci specifikací pro testování shody základnových stanic
- Používá se pro výpočet velikosti chybového vektoru (EVM)
- Aplikována ve vzorcích pro měření kvality signálu vysílače
- Zajišťuje jednoznačné a opakovatelné výsledky testů
- Nedílná součást ověřování výkonu fyzické vrstvy LTE a NR

## Související pojmy

- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)

## Definující specifikace

- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [SQRT na 3GPP Explorer](https://3gpp-explorer.com/glossary/sqrt/)
