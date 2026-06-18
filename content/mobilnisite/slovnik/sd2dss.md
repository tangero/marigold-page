---
slug: "sd2dss"
url: "/mobilnisite/slovnik/sd2dss/"
type: "slovnik"
title: "SD2DSS – Secondary D2D Synchronization Signal"
date: 2018-01-01
abbr: "SD2DSS"
fullName: "Secondary D2D Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sd2dss/"
summary: "Synchronizační signál používaný v LTE komunikaci typu zařízení-zařízení (D2D), konkrétně pro synchronizaci na sidelinku. Spolupracuje s primárním D2D synchronizačním signálem (PD2DSS) a umožňuje UE do"
---

SD2DSS je sekundární D2D synchronizační signál používaný v LTE sidelink komunikaci společně s PD2DSS k umožnění synchronizace zařízení pro přímou komunikaci.

## Popis

Sekundární [D2D](/mobilnisite/slovnik/d2d/) synchronizační signál (SD2DSS) je klíčový signál fyzické vrstvy definovaný pro LTE sidelink komunikaci, zavedený jako součást služeb Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) a funkce Device-to-Device (D2D) ve 3GPP Release 12. Tvoří jednu polovinu páru D2D synchronizačních signálů a doplňuje primární D2D synchronizační signál ([PD2DSS](/mobilnisite/slovnik/pd2dss/)). Primární funkcí těchto signálů je umožnit uživatelským zařízením (UE) dosáhnout a udržovat časovou a frekvenční synchronizaci se synchronizační referencí při provozu v režimu přímé komunikace na sidelinku (rozhraní PC5). Tato reference může být jiné UE (UE jako zdroj synchronizace), eNodeB (v pokrytí) nebo globální navigační satelitní systém ([GNSS](/mobilnisite/slovnik/gnss/)).

Technicky je SD2DSS vysílán společně s PD2DSS ve specifických podrámcích v rámci fondu zdrojů pro sidelink synchronizaci. Tyto signály mají definovanou periodicitu. PD2DSS poskytuje hrubé časování a pomáhá identifikovat základní typ zdroje synchronizace (např. v pokrytí vs. mimo pokrytí). SD2DSS nese dodatečné informace, které zpřesňují proces synchronizace. Konkrétně sekvence SD2DSS přenáší identitu sidelink synchronizace ([SLSS](/mobilnisite/slovnik/slss/) ID), což je klíčový parametr. SLSS ID, odvozený z kombinace sekvencí PD2DSS a SD2DSS, identifikuje konkrétní zdroj synchronizace a jeho charakteristiky. Přijímající UE provádí korelační vyhledávání, aby nejprve detekovala PD2DSS, a následně detekuje přidružený SD2DSS k dekódování celého SLSS ID.

Po detekci UE použije časování těchto signálů k zarovnání svého přijímače. Dosažená synchronizace je zásadní pro správnou funkci všech ostatních sidelink fyzických kanálů, jako je Physical Sidelink Broadcast Channel ([PSBCH](/mobilnisite/slovnik/psbch/)), který přenáší základní systémové informace, a Physical Sidelink Shared Channel ([PSSCH](/mobilnisite/slovnik/pssch/)) používaný pro přenos dat. Bez robustní synchronizace zajišťované PD2DSS/SD2DSS by sidelink komunikace trpěla závažným mezisymbolovým rušením a byla by nespolehlivá, zejména v mobilních scénářích jako je veřejná bezpečnost nebo [V2X](/mobilnisite/slovnik/v2x/). Návrh SD2DSS, včetně generování jeho sekvence a mapování na zdrojové elementy, byl pečlivě vypracován tak, aby zajistil nízkou složitost detekce, dobré autokorelační a vzájemně korelační vlastnosti a koexistenci s legacy LTE buněčnými signály, aby se předešlo rušení.

## K čemu slouží

SD2DSS byl vytvořen k řešení základní výzvy spočívající ve vytvoření společné časové reference pro přímou komunikaci mezi zařízeními v LTE sítích. Před standardizací ProSe se mohla LTE zařízení synchronizovat pouze k eNodeB. Pro přímou komunikaci, zejména ve scénářích mimo pokrytí klíčových pro veřejnou bezpečnost, potřebovala zařízení metodu, jak se vzájemně autonomně synchronizovat. Jednoduché rozšíření buněčných synchronizačních signálů bylo nedostatečné kvůli odlišným požadavkům a potenciálnímu rušení.

Zavedení vyhrazených D2D synchronizačních signálů (PD2DSS a SD2DSS) bylo motivováno potřebou flexibilního, hierarchického synchronizačního rámce pro sidelink. PD2DSS poskytuje počáteční kotvu, ale SD2DSS je nezbytný pro přenos SLSS ID, který umožňuje několik klíčových funkcionalit. Toto ID umožňuje zařízením rozlišit mezi více zdroji synchronizace (např. různými klastry zařízení), vybrat nejlepší zdroj (např. na základě priority nebo síly signálu) a šířit synchronizaci v síti zařízení způsobem s více skoky. Tím se řeší problém udržování síťového časování v decentralizovaných scénářích a umožňuje spolehlivá vysílací a skupinová komunikace pro služby kritické pro misi. Tvořil to synchronizační páteř pro LTE V2X v pozdějších releasech, což zajišťovalo, že vozidla mohou koordinovat přímou komunikaci i bez buněčného pokrytí.

## Klíčové vlastnosti

- Spolupracuje s PD2DSS a tvoří pár D2D synchronizačních signálů pro LTE sidelink
- Nese část identity sidelink synchronizačního signálu (SLSS ID)
- Umožňuje UE dosáhnout časové/frekvenční synchronizace s jinými UE nebo GNSS v přímém režimu
- Podporuje identifikaci a výběr zdroje synchronizace
- Nezbytný pro provoz sidelink vysílacích a sdílených kanálů (PSBCH, PSSCH)
- Navržen pro robustní detekci ve scénářích s vysokou mobilitou a mimo pokrytí

## Související pojmy

- [PD2DSS – Primary D2D Synchronization Signal](/mobilnisite/slovnik/pd2dss/)
- [PSBCH – Physical Sidelink Broadcast Channel](/mobilnisite/slovnik/psbch/)

## Definující specifikace

- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.843** (Rel-12) — D2D Proximity Services Feasibility Study
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services

---

📖 **Anglický originál a plná specifikace:** [SD2DSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sd2dss/)
