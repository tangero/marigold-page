---
slug: "cldfb"
url: "/mobilnisite/slovnik/cldfb/"
type: "slovnik"
title: "CLDFB – Complex Low-delay Filter Bank"
date: 2025-01-01
abbr: "CLDFB"
fullName: "Complex Low-delay Filter Bank"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cldfb/"
summary: "CLDFB je signální procesní technika definovaná v 3GPP pro audio kodeky, umožňující efektivní časově-frekvenční analýzu s minimálním algoritmickým zpožděním. Rozkládá audio signály na subpásma pro komp"
---

CLDFB je signální procesní technika definovaná 3GPP pro audio kodeky, která rozkládá signál na subpásma s minimálním zpožděním, což umožňuje efektivní kompresi a vysokou kvalitu pro komunikaci v reálném čase s nízkou latencí.

## Popis

Complex Low-delay Filter Bank (CLDFB) je sofistikovaná struktura pro zpracování signálu specifikovaná v 3GPP Technických Specifikacích (TS) 26.249 a 26.253 pro pokročilé audio kódování. Funguje jako časově-frekvenční transformace, která rozkládá vstupní audio signál na více subpásem pomocí banky analýzních filtrů. Na rozdíl od jednodušších filtrů používá CLDFB zpracování s komplexními hodnotami, které poskytuje jak informaci o velikosti, tak o fázi pro každé subpásmo. Tato komplexní reprezentace umožňuje přesnější analýzu a syntézu signálu, zejména pro tranzientní a tónové složky audia. Banka filtrů je navržena s polyfázovou implementací pro optimalizaci výpočetní efektivity, což ji činí vhodnou pro zpracování v reálném čase na mobilních zařízeních.

Architektura CLDFB se skládá z několika klíčových komponent: banky analýzních filtrů, která rozděluje širokopásmový signál; modulu pro zpracování subpásem, kde probíhá kvantizace a kódování; a banky syntézních filtrů, která rekonstruuje signál z subpásem. Analýzní filtry jsou typicky navrženy jako modulované verze prototypového dolopropustného filtru, což zajišťuje dokonalou rekonstrukci v kombinaci se syntézními filtry. Charakteristika 'nízkého zpoždění' je dosažena pečlivým návrhem délky impulsní odezvy prototypového filtru a celkové latence systému, která je udržována na minimu pro podporu konverzačních aplikací. Komplexní povaha filtrů znamená, že pracují na bázi komplexních exponenciálně modulovaných bází, což poskytuje lepší frekvenční selektivitu ve srovnání s bankami filtrů s reálnými hodnotami.

Během provozu CLDFB zpracovává audio rámce nejprve okénkováním časově-doménového signálu pomocí funkce analýzního okna. Okénkovaný signál je poté transformován do frekvenční domény pomocí modifikované struktury diskrétní Fourierovy transformace ([DFT](/mobilnisite/slovnik/dft/)), která implementuje banku filtrů. Každý výstup subpásma reprezentuje specifickou frekvenční oblast a tato subpásma mohou být zpracována nezávisle – například aplikací rozdílného přidělení bitů v audio kodeku. Syntézní fáze tento proces obrací pomocí banky syntézních filtrů, která kombinuje zpracovaná subpásma zpět do časově-doménového signálu. Celý řetězec je navržen tak, aby minimalizoval aliasingové a zobrazovací artefakty, a zajišťoval tak vysokou audio věrnost.

V ekosystému 3GPP hraje CLDFB kritickou roli ve zvyšování výkonu audio kodeků, jako je Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) a budoucí formáty imerzivního audia. Jeho vlastnost nízkého zpoždění je zásadní pro zachování přirozeného průběhu konverzace v hlasových hovorech, protože nadměrná latence může způsobit překrývání mluvčích a zmatek. Komplexní banka filtrů poskytuje vynikající kódovací efektivitu, což umožňuje kodekům dosáhnout vyšší audio kvality při nižších bitech. Tato efektivita znamená úspory šířky pásma pro síťové operátory a lepší uživatelský zážitek. Návrh CLDFB také podporuje škálovatelné audio kódování, kde lze počet aktivních subpásem upravovat na základě dostupnosti šířky pásma nebo požadované kvality.

## K čemu slouží

CLDFB byl vyvinut k uspokojení rostoucí poptávky po vysoce kvalitní audio komunikaci s nízkou latencí v mobilních sítích. Tradiční audio kodeky často používaly banky filtrů s reálnými hodnotami, jako je Modified Discrete Cosine Transform ([MDCT](/mobilnisite/slovnik/mdct/)), které zaváděly významné algoritmické zpoždění kvůli dlouhým analýzním oknům. Toto zpoždění bylo problematické pro aplikace v reálném čase, jako jsou hlasové hovory, kde latence nad 100-150 milisekund začíná být vnímatelná a rušivá. Komplexní banka filtrů s nízkým zpožděním poskytuje řešení tím, že nabízí jemné frekvenční rozlišení s mnohem kratšími délkami oken, čímž snižuje end-to-end zpoždění při zachování kódovací efektivity.

Historický kontext ukazuje, že dřívější 3GPP kodeky jako [AMR-WB](/mobilnisite/slovnik/amr-wb/) používaly jednodušší banky filtrů s vyšší latencí. Jak se sítě vyvíjely pro podporu Voice over LTE (VoLTE) a Voice over NR (VoNR), stala se potřeba vylepšené hlasové kvality s minimálním zpožděním prvořadou. CLDFB umožňuje kodekům dosáhnout této rovnováhy a podporuje funkce jako high-definition voice a full-band audio. Také řeší omezení předchozích přístupů snížením artefaktů předozvěně – běžného problému v audio kódování, kdy se kvantizační šum šíří v čase – pomocí vylepšené časově-frekvenční lokalizace.

Vytvoření CLDFB bylo motivováno konvergencí telekomunikačních a multimediálních služeb, kde uživatelé očekávají studiovou kvalitu audia i na mobilních zařízeních. Řeší problém doručování imerzivních audio zážitků – jako je prostorové audio nebo 3D zvuk – přes omezené bezdrátové kanály. Poskytnutím flexibilní a efektivní transformační domény umožňuje CLDFB kodekům dynamicky se přizpůsobovat síťovým podmínkám a charakteristikám obsahu. Tato adaptabilita je klíčová pro úspěch vznikajících služeb, jako jsou komunikace v rozšířené realitě ([XR](/mobilnisite/slovnik/xr/)) nebo síťová produkce hudby.

## Klíčové vlastnosti

- Rozklad na subpásma s komplexními hodnotami pro přesné vyjádření fáze a velikosti
- Minimalizované algoritmické zpoždění prostřednictvím optimalizovaného návrhu prototypového filtru
- Vlastnost dokonalé rekonstruce zajišťující žádné zkreslení signálu při bezztrátovém kódování
- Polyfázová implementace pro výpočetní efektivitu na mobilních procesorech
- Podpora proměnného rozlišení časově-frekvenčního členění pro zpracování tranzientních a stacionárních signálů
- Kompatibilita s rámci škálovatelného audio kódování pro adaptivní streamování s proměnným datovým tokem

## Definující specifikace

- **TS 26.249** (Rel-19) — Immersive Audio Split Rendering (ISAR)
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [CLDFB na 3GPP Explorer](https://3gpp-explorer.com/glossary/cldfb/)
