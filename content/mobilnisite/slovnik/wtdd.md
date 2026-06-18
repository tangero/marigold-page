---
slug: "wtdd"
url: "/mobilnisite/slovnik/wtdd/"
type: "slovnik"
title: "WTDD – Wideband Time Division Duplexing"
date: 2025-01-01
abbr: "WTDD"
fullName: "Wideband Time Division Duplexing"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wtdd/"
summary: "Metoda duplexování, při níž se přenosy v uplinku a downlinku dělí o stejný kmitočtový pás, ale střídají se v čase, s využitím širšího kanálového pásma. Umožňuje flexibilní a asymetrický tok dat a běžn"
---

WTDD je metoda duplexování s časovým dělením využívající široké pásmo, při níž se přenosy v uplinku a downlinku dělí o stejný kmitočtový pás, ale střídají se v čase, což umožňuje flexibilní a asymetrický tok dat.

## Popis

Wideband Time Division Duplexing (WTDD) je technika přístupu k rádiovému rozhraní, při níž komunikace v obou směrech (uplink od zařízení k síti a downlink od sítě k zařízení) probíhá na stejné nosné frekvenci, ale je oddělena v čase. Označení „Wideband“ (širokopásmový) odkazuje na použití širšího kanálového pásma, typicky 1,6 MHz nebo 5 MHz v kontextu standardů 3GPP, ve srovnání s užšími variantami [TDD](/mobilnisite/slovnik/tdd/). Čas je rozdělen na opakující se rámce, které se dále dělí na časové sloty. Přidělení těchto slotů pro uplink nebo downlink může být asymetrické a dynamicky konfigurováno sítí na základě požadavků provozu.

Z pohledu fyzické vrstvy WTDD funguje tak, že vysílá dávky dat v přidělených časových slotech. Klíčovou součástí je přepínací bod mezi režimem vysílání (Tx) a příjmu (Rx) na základnové stanici a uživatelském zařízení. To vyžaduje přesnou časovou synchronizaci v celé síti, aby všechna zařízení v buňce vysílala ve svých přidělených uplinkových slotech a nezasahovala do downlinkových slotů sousedních buněk. Mezi časové sloty jsou vkládány ochranné intervaly, které kompenzují zpoždění šíření a umožňují čas na přepnutí rádiového obvodu. Širší pásmo umožňuje vyšší datové rychlosti a lepší výkon prostřednictvím kmitočtové diverzity a podporuje pokročilé modulační a kódovací schémata.

V síťové architektuře je WTDD klíčovou vlastností rádiového rozhraní Time Division - Synchronous Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([TD-SCDMA](/mobilnisite/slovnik/td-scdma/)), což byl standard 3G převážně nasazovaný v Číně. Základnová stanice (Node B) řídí konfiguraci časových slotů a vysílá vzor přidělení pro uplink/downlink. Tato flexibilita umožňuje operátorům optimalizovat využití spektra pro provoz, který je inherentně asymetrický, jako je prohlížení internetu, kde dominuje downlinkový provoz. Úkolem WTDD je poskytnout efektivní metodu duplexování s flexibilním využitím spektra, která nevyžaduje spárovaná kmitočtová pásma (na rozdíl od [FDD](/mobilnisite/slovnik/fdd/)), což je výhodné pro operátory s omezenými nebo nespárovanými přiděleními spektra.

## K čemu slouží

WTDD byl vyvinut, aby poskytl metodu duplexování s vysokou kapacitou a efektivním využitím spektra pro sítě 3G, a to zejména pro uspokojení potřeby flexibilního přidělování šířky pásma v nespárovaných kmitočtových pásmech. Tradiční duplexování s kmitočtovým dělením ([FDD](/mobilnisite/slovnik/fdd/)) vyžaduje dvě samostatná, spárovaná kmitočtová pásma s ochranným pásmem mezi nimi, což může být neefektivní, pokud je provoz vysoce asymetrický. Metody [TDD](/mobilnisite/slovnik/tdd/) existovaly, ale WTDD zavedl širší kanálové pásmo pro podporu vyšších datových rychlostí vyžadovaných multimediálními službami 3G.

Vznik WTDD byl do značné míry poháněn iniciativou standardu [TD-SCDMA](/mobilnisite/slovnik/td-scdma/), jejímž cílem bylo nabídnout řešení 3G optimalizované pro specifické potřeby trhu, včetně efektivního využití dostupného spektra a nižších nákladů na nasazení. Vyřešil problém pevně daného rozdělení kapacity pro uplink a downlink, který je vlastní FDD. S WTDD mohou síťoví operátoři dynamicky upravovat poměr časových slotů přidělených pro uplink a downlink na základě vzorců provozu v reálném čase, například přesunout více kapacity do downlinku během špičky streamování videa. Tato přizpůsobivost jej činí vysoce efektivním pro přerušovaný, IP-based datový provoz. Navíc použití jediného kmitočtového pásma zjednodušuje konstrukci rádiového rozhraní a může snížit složitost zařízení ve srovnání s FDD, které potřebuje duplexery k oddělení současných vysílacích a přijímacích frekvencí.

## Klíčové vlastnosti

- Používá jediné kmitočtové pásmo pro uplink i downlink, které jsou odděleny časovými sloty
- Podporuje široká kanálová pásma (např. 1,6 MHz, 5 MHz) pro vyšší datové rychlosti
- Umožňuje asymetrické a dynamické přidělování časových slotů mezi uplink a downlink
- Vyžaduje přesnou synchronizaci v celé síti pro správu přechodů mezi časovými sloty
- Odstraňuje potřebu spárovaného spektra, což umožňuje využití nespárovaných pásem
- Zahrnuje ochranné intervaly pro zvládnutí zpoždění šíření a doby přepnutí zařízení

## Související pojmy

- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)
- [FDD – Frequency Division Duplexing](/mobilnisite/slovnik/fdd/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [WTDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/wtdd/)
