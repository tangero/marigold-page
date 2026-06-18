---
slug: "tae"
url: "/mobilnisite/slovnik/tae/"
type: "slovnik"
title: "TAE – Time Alignment Error"
date: 2025-01-01
abbr: "TAE"
fullName: "Time Alignment Error"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tae/"
summary: "Chyba časového sladění (Time Alignment Error, TAE) je klíčový výkonnostní metrik při testování shody stanic základnové sítě 3GPP (NodeB, eNodeB, gNB). Měří přesnost časování mezi různými vysílacími vě"
---

TAE je měřená přesnost časového sladění mezi různými vysílacími větvemi nebo anténními porty ve stanici základnové sítě 3GPP, což je klíčový metrik pro zajištění správného beamformingu a kvality downlinkového signálu.

## Popis

Chyba časového sladění (Time Alignment Error, TAE) je klíčová charakteristika vysílače a požadavek testu shody definovaný ve specifikacích 3GPP pro základnové stanice ([BS](/mobilnisite/slovnik/bs/)), včetně NodeB ([UTRAN](/mobilnisite/slovnik/utran/)), eNodeB ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a gNB (NG-RAN). Kvantifikuje maximální časový rozdíl nebo nesladení mezi rádiovými signály vysílanými z různých vysílacích větví, anténních konektorů nebo anténních portů téže základnové stanice. Toto nesladení se měří na rozhraní vzduch vůči definovanému referenčnímu bodu. TAE není provozní signalizační parametr, ale výkonnostní metrik používaný během návrhu, výroby a certifikace k zajištění, že hardware základnové stanice splňuje přísné požadavky na časovou přesnost. Nízká hodnota TAE je klíčová, protože moderní základnové stanice využívají více antén pro technologie jako vícevstup-vícevýstup ([MIMO](/mobilnisite/slovnik/mimo/)), beamforming a agregaci nosných, kde je pro správnou funkci těchto technik nezbytné přesné relativní časování mezi vysílanými signály.

Měření TAE zahrnuje analýzu vysílaných vlnových forem testované základnové stanice. Specifikace jako TS 37.141 (pro testování shody E-UTRAN a NR) definují podrobné testovací postupy. Typicky testovací sestava používá vysoce přesný analyzátor signálu k současnému zachycení [RF](/mobilnisite/slovnik/rf/) signálů z více vysílacích větví. Analýza často využívá techniky vzájemné korelace k určení přesného časového posunu mezi měřenými signály. Limit TAE je specifikován jako maximální přípustná hodnota, často v nanosekundách (ns) nebo jako zlomek trvání symbolu (např. Ts). Požadavky se například liší pro souvislou agregaci nosných v rámci pásma (kde jsou signály na sousedních nosných) oproti nesouvislé nebo mezipásmové agregaci, přičemž pro souvislé scénáře jsou obvykle vyžadovány těsnější tolerance, aby se zabránilo interferenci mezi komponentními nosnými.

TAE ovlivňuje několik pokročilých rádiových funkcí. U MIMO, zejména u prostorového multiplexování, může časové nesladení mezi vrstvami zhoršit odhad kanálu na straně UE a zvýšit interferenci mezi vrstvami, čímž sníží propustnost. U beamformingu, který závisí na konstruktivní a destruktivní interferenci vln z více anténních prvků, mohou časové chyby zkreslit zamýšlený vyzařovací diagram, snížit zisk paprsku nebo jej nasměrovat špatným směrem. Při agregaci nosných může nesladení mezi primární a sekundární komponentní nosnou komplikovat zpracování v přijímači UE a degradovat výkon. Proto je řízení TAE prostřednictvím přesného hardwarového návrhu (např. kalibrované RF řetězce, synchronizované lokální oscilátory) a digitálního zpracování signálu základním aspektem implementace základnové stanice. Specifikace 3GPP definují samostatné požadavky na TAE pro různé třídy základnových stanic (např. pro širokou oblast, střední dosah, lokální oblast) a scénáře nasazení, s ohledem na to, že praktické tolerance se mohou lišit.

## K čemu slouží

Účelem definování a testování chyby časového sladění (TAE) je zajistit praktickou realizovatelnost a výkon pokročilých víceanténních vysílacích technik v celulárních sítích. Jak se standardy 3GPP vyvíjely od systémů s jednou anténou (Rel-99 UMTS) k [MIMO](/mobilnisite/slovnik/mimo/) a beamformingu (od [HSPA](/mobilnisite/slovnik/hspa/)+ a LTE dále), teoretické zisky těchto technologií silně závisely na fyzické implementaci vysílače základnové stanice. Bez specifikace a kontroly časového sladění mezi vysílacími cestami by nemohly být v reálných nasazeních garantovány slibované benefity zvýšených datových rychlostí, lepšího pokrytí a spektrální účinnosti.

Historicky, pro jednoduché vysílání s jednou nosnou a jednou anténou, byla hlavním zájmem absolutní časová přesnost (vůči rámcové hodině). Motivace pro zavedení specifikací TAE vznikla s adopcí vysílací diverzity, MIMO a později agregace nosných v Release 8 (LTE) a novějších. Tyto technologie vyžadují více koherentních [RF](/mobilnisite/slovnik/rf/) řetězců pracujících paralelně. Jakékoli nezáměrné časové zkreslení mezi těmito řetězci se stává zdrojem implementační nedokonalosti, která degraduje výkon systému. Normalizační úsilí 3GPP zahrnulo TAE, aby poskytlo jasnou, měřitelnou hranici pro tuto nedokonalost, což umožnilo výrobcům základnových stanic navrhovat zařízení ke společnému cíli a síťovým operátorům mít důvěru v interoperabilitu a výkon zařízení. Řeší omezení spočívající v předpokladu ideálního hardwaru vysílače v systémových simulacích a vývoji standardů, čímž překlenuje propast mezi teorií a praxí. Definováním TAE 3GPP zajišťuje, že pokročilé funkce fyzické vrstvy fungují konzistentně napříč zařízeními od různých výrobců, což je klíčové pro konkurenceschopný a interoperabilní ekosystém.

## Klíčové vlastnosti

- Definován jako metrik testu shody pro vysílače základnových stanic
- Měří maximální časový rozdíl mezi signály z více vysílacích větví/anténních portů
- Kritický pro výkon MIMO, beamformingu a agregace nosných
- Specifikován s různými limity pro různé třídy základnových stanic a scénáře nasazení
- Měřen v nanosekundách nebo jako zlomek základní časové jednotky (Ts)
- Testovací postupy podrobně popsány ve specifikaci shody základnových stanic (např. TS 37.141)

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TS 38.817** — 3GPP TR 38.817
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec
- **TS 48.061** (Rel-19) — BTS-TRAU Protocol for HR Speech/Data

---

📖 **Anglický originál a plná specifikace:** [TAE na 3GPP Explorer](https://3gpp-explorer.com/glossary/tae/)
