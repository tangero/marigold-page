---
slug: "apc"
url: "/mobilnisite/slovnik/apc/"
type: "slovnik"
title: "APC – Antenna Phase Center"
date: 2025-01-01
abbr: "APC"
fullName: "Antenna Phase Center"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/apc/"
summary: "Antenna Phase Center (APC, fázový střed antény) je teoretický bod v prostoru, z něhož se zdánlivě šíří elektromagnetické vlny a který představuje efektivní počátek vyzařovacího diagramu antény. Je klí"
---

APC je teoretický bod, z něhož se zdánlivě šíří elektromagnetické vlny antény, klíčový pro přesné metody určování polohy, jako je OTDOA v mobilních sítích.

## Popis

Antenna Phase Center (APC, fázový střed antény) je základním konceptem v teorii antén a vysokofrekvenční technice, který představuje efektivní bod, z něhož se zdánlivě šíří elektromagnetické záření při vysílání, nebo do něhož se zdánlivě sbíhá při příjmu. Ve specifikacích 3GPP, zejména v kontextu technologií určování polohy, slouží APC jako referenční bod pro fázová měření a časové výpočty. U dané antény není APC nutně pevným fyzickým bodem, ale spíše matematickou konstrukcí, která se mění s frekvencí, polarizací a vyzařovacím diagramem. V praktických implementacích se APC určuje pečlivou charakterizací a kalibračními postupy antény.

V architekturách určování polohy podle 3GPP hraje APC klíčovou roli při měřeních rozdílu času referenčních signálů ([RSTD](/mobilnisite/slovnik/rstd/)) používaných pro určování polohy metodou [OTDOA](/mobilnisite/slovnik/otdoa/). Když uživatelské zařízení (UE) měří časové rozdíly mezi signály z různých základnových stanic, musí být tato měření vztažena ke konzistentním bodům v prostoru – k APC vysílacích antén. Specifikace 3GPP definují, jak by měly síťové elementy komunikovat informace o APC, aby umožnily přesné výpočty polohy. To zahrnuje souřadnice referenčního bodu antény ([ARP](/mobilnisite/slovnik/arp/)) a vektory posunu k APC pro každý anténní port.

Technická implementace zahrnuje několik komponent: fyzickou strukturu antény s jejími vyzařovacími prvky, kalibrační systém, který charakterizuje APC za různých podmínek, positioning protokol, který komunikuje parametry APC k positioning serverům, a výpočetní algoritmy, které kompenzují vliv APC v časových měřeních. U víceanténních systémů, jako jsou [MIMO](/mobilnisite/slovnik/mimo/) pole, může mít každý anténní prvek nebo port svůj vlastní APC, což vyžaduje složité kalibrační a kompenzační postupy. Koncept APC se vztahuje jak na antény základnových stanic (gNB v 5G, [eNB](/mobilnisite/slovnik/enb/) v LTE), tak potenciálně i na antény UE, ačkoli primární důraz ve specifikacích 3GPP je na APC na síťové straně pro určování polohy v downlinku.

Přesnost znalosti APC přímo ovlivňuje výkonnost určování polohy. Chyby v umístění APC se přímo převádějí na chyby ve vypočtené poloze UE. Pro požadavky na vysokou přesnost určení polohy (jako je přesnost na úrovni centimetrů pro průmyslový IoT nebo autonomní vozidla) musí kalibrace APC zohledňovat environmentální faktory, jako jsou teplotní změny, mechanické namáhání a stárnutí. Pokročilé implementace mohou zahrnovat systémy sledování a kompenzace APC v reálném čase, které upravují parametry APC na základě provozních podmínek. Integrace informací o APC s dalšími referenčními daty pro určování polohy vytváří komplexní rámec pro přesné lokalizační služby v sítích 5G a novějších.

## K čemu slouží

Koncept Antenna Phase Center byl do 3GPP zaveden, aby řešil rostoucí potřebu přesných schopností určování polohy v mobilních sítích. Jak se lokalizační služby vyvíjely od jednoduchých metod založených na Cell-ID k sofistikovanému určování polohy na úrovni centimetrů, staly se zřejmými omezení přístupu, který s anténami zachází jako s ideálními bodovými zdroji. Tradiční přístupy k určování polohy, které ignorovaly efekty APC, trpěly systematickými chybami, které omezovaly přesnost, zejména u pokročilých technik jako [OTDOA](/mobilnisite/slovnik/otdoa/), které spoléhají na přesná časová měření mezi více základnovými stanicemi.

Předchozí síťové implementace často používaly zjednodušené modely antén, které předpokládaly, že záření vychází z jediného pevného bodu, typicky fyzického středu anténního pole. Tato aproximace byla dostačující pro hrubé určení polohy, ale ukázala se jako nedostatečná pro přesnost požadovanou novými aplikacemi, jako jsou autonomní vozidla, průmyslová automatizace a rozšířená realita. Zavedení APC ve specifikacích 3GPP poskytlo standardizovaný způsob, jak charakterizovat a kompenzovat skutečné vyzařovací chování antén, což umožnilo přesnost určení polohy na úrovni pod metr a nakonec i centimetrů.

Motivace pro standardizaci nakládání s APC přišla z více směrů: regulatorní požadavky na lokalizaci volajících v nouzi, komerční požadavky na služby založené na poloze a technické potřeby pro optimalizaci sítě. Definováním přesných metod pro charakterizaci, komunikaci a aplikaci APC ve výpočtech polohy vytvořil 3GPP základ pro interoperabilní vysoce přesné určování polohy napříč různými zařízeními od různých dodavatelů a síťovými nasazeními. Tato standardizace byla obzvláště důležitá pro sítě 5G, kde je přesnost určení polohy klíčovým ukazatelem výkonu a umožňovatelem aplikací pro vertikální průmysly.

## Klíčové vlastnosti

- Referenční bod pro vyzařovací diagramy elektromagnetického záření
- Klíčový pro přesná časová měření při určování polohy
- Charakteristika závislá na frekvenci a citlivá na polarizaci
- Standardizovaná komunikace v positioning protokolech
- Umožňuje přesnost určení polohy na úrovni centimetrů
- Kompenzuje fázové variace specifické pro anténu

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [RSTD – Reference Signal Time Difference](/mobilnisite/slovnik/rstd/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [APC na 3GPP Explorer](https://3gpp-explorer.com/glossary/apc/)
