---
slug: "cpagch"
url: "/mobilnisite/slovnik/cpagch/"
type: "slovnik"
title: "CPAGCH – Compact Packet Access Grant Channel"
date: 2025-01-01
abbr: "CPAGCH"
fullName: "Compact Packet Access Grant Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cpagch/"
summary: "Compact Packet Access Grant Channel (CPAGCH) je downlink řídicí kanál v GSM/EDGE rádiové přístupové síti (GERAN), který efektivně alokuje uplink paketové zdroje. Používá se v kontextu Enhanced General"
---

CPAGCH je downlink řídicí kanál v sítích GSM/EDGE, který efektivně přiděluje uplink paketové zdroje v kompaktním formátu za účelem snížení signalizační režie v rámci EGPRS.

## Popis

Compact Packet Access Grant Channel (CPAGCH) je specifický logický kanál definovaný v 3GPP TS 43.064 pro GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiovou přístupovou síť ([GERAN](/mobilnisite/slovnik/geran/)). Funguje na downlinku jako součást Packet Common Control Channel (PCCCH) nebo, při jeho absenci, na Common Control Channel ([CCCH](/mobilnisite/slovnik/ccch/)). Jeho primární funkcí je přenášet zprávy Packet Uplink Assignment, které přidělují zdroje pro uplink dočasný tok bloků (TBF) mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) iniciující přenos paketových dat. Označení 'Compact' odkazuje na jeho optimalizovaný formát zprávy, který je navržen tak, aby byl efektivnější než standardní Packet Access Grant Channel (PAGCH) používaný na PCCCH, čímž šetří cenné rádiové zdroje.

Z architektonického hlediska se zprávy CPAGCH přenášejí na specifických časových slotech a rámečcích podle konfigurace řídicího kanálu buňky. Pokud PCCCH v buňce není nasazen, může být CPAGCH namapován na CCCH, konkrétně s využitím časových slotů Access Grant Channel ([AGCH](/mobilnisite/slovnik/agch/)). Toto mapování je definováno specifickými parametry vysílanými v systémové informaci, což umožňuje síti flexibilně podporovat služby paketových dat i v buňkách bez vyhrazeného PCCCH. Kanál používá specifický formát zprávy, který zahrnuje pro MS nezbytné informace, jako je přidělený časový slot, počáteční rámeček a rádiové parametry (např. kódové schéma a řízení výkonu) pro uplink TBF.

Z procedurálního hlediska, když MS potřebuje odeslat paketová data, odešle Packet Channel Request na PRACH (nebo RACH, pokud PCCCH chybí). Síť odpoví zprávou Packet Uplink Assignment na CPAGCH. Tato zpráva MS přesně instruuje, které fyzické zdroje (rádiové bloky na specifických časových slotech) má použít pro svůj uplink přenos. Kompaktní formát této přidělovací zprávy je klíčový; minimalizuje počet potřebných bitů, což umožňuje efektivnější umístění zprávy do jediného rádiového bloku nebo uvolnění kapacity pro jinou řídicí signalizaci. Tato efektivita je kritická v přetížených buňkách nebo v sítích s omezeným spektrem.

CPAGCH hraje zásadní roli v celkovém navazování datové relace [EGPRS](/mobilnisite/slovnik/egprs/). Je to přímá odpověď sítě na žádost o kanál, která umožňuje rychlé zřízení uplink TBF. Jeho efektivní provoz přímo ovlivňuje metriky jako doba zřízení spojení, zatížení řídicích kanálů signalizací a celkovou kapacitu sítě pro uživatele paketových dat. Zatímco jeho význam je nejvyšší v čistých nasazeních GERAN, pochopení CPAGCH je nezbytné pro pochopení vývoje mechanismů přidělování paketových zdrojů od 2G/2.5G přes 3G a dále.

## K čemu slouží

CPAGCH byl zaveden, aby řešil neefektivnost počáteční signalizace [EGPRS](/mobilnisite/slovnik/egprs/), zejména ve scénářích, kde nebyl nasazen vyhrazený Packet Common Control Channel (PCCCH). Rané implementace EGPRS spoléhaly na použití stávajícího Common Control Channel ([CCCH](/mobilnisite/slovnik/ccch/)) pro přidělení paketového přístupu, ale standardní formát zprávy Packet Access Grant Channel (PAGCH) byl poměrně rozsáhlý. To vytvářelo signalizační zahlcení na CCCH, který byl již zatížen provozem zřizování okruhově komutovaných hovorů, což vedlo ke zvýšené latenci a potenciálnímu blokování jak hlasových, tak datových služeb.

Vytvoření CPAGCH bylo motivováno potřebou optimalizovat využití rádiových zdrojů pro služby paketových dat bez povinného nasazení PCCCH v každé buňce. PCCCH vyžaduje vyhrazené časové sloty, což představuje trvalé vynaložení kapacity, které nemusí být ospravedlnitelné ve všech síťových konfiguracích, zejména v raných nasazeních EDGE nebo v oblastech s nízkým provozem. CPAGCH poskytl mezilehlé řešení: umožnil sítím podporovat efektivní přístup k paketovým datům s využitím stávající infrastruktury CCCH prostřednictvím použití kompaktnějšího formátu zpráv pro uplink přidělení. Tím bylo vyřešeno klíčové kompromisní rozhodování operátorů mezi náklady a kapacitou.

Snižováním signalizační režie na jedno uplink přidělení CPAGCH zvýšil kapacitu řídicího kanálu. To znamenalo, že síť mohla zvládnout více současných pokusů o paketový přístup, snížit kolize a zkrátit dobu, po kterou MS čeká na přidělení zdroje. Tato optimalizace byla klíčová pro zlepšení uživatelského zážitku u raných mobilních datových aplikací a pro maximální využití dostupného spektra v sítích GSM/EDGE, čímž prodloužila jejich životnost pro datové služby v době zavádění technologií 3G.

## Klíčové vlastnosti

- Optimalizován pro přenos na CCCH při absenci PCCCH
- Přenáší zprávy Packet Uplink Assignment v kompaktním formátu
- Snižuje signalizační režii ve srovnání se standardním PAGCH
- Umožňuje efektivní zřízení uplink TBF v EGPRS
- Definován specifickými parametry mapování v systémové informaci
- Zvyšuje kapacitu řídicího kanálu a snižuje přístupovou latenci

## Související pojmy

- [EGPRS – Enhanced GPRS](/mobilnisite/slovnik/egprs/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [CPAGCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpagch/)
