---
slug: "nr-mib"
url: "/mobilnisite/slovnik/nr-mib/"
type: "slovnik"
title: "NR-MIB – NR-Master Information Block"
date: 2025-01-01
abbr: "NR-MIB"
fullName: "NR-Master Information Block"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nr-mib/"
summary: "NR-MIB je minimální soubor základních systémových informací vysílaných gNB na NR-PBCH. Poskytuje klíčové parametry, jako je číslo systémového rámce a rozteč podnosných, a umožňuje počáteční vyhledání"
---

NR-MIB je minimální soubor základních systémových informací vysílaných gNB na NR-PBCH, který poskytuje klíčové parametry, jako je číslo systémového rámce, pro umožnění počátečního vyhledávání buňky, synchronizace a vstupu do sítě v 5G.

## Popis

NR-Master Information Block (NR-MIB) je základní zpráva vysílaná na broadcast kanálu, kterou vysílá Next Generation NodeB (gNB) na fyzickém broadcast kanálu (NR-PBCH). Je to klíčová součást rámce systémových informací ([SI](/mobilnisite/slovnik/si/)) 5G New Radio (NR), navržená tak, aby byla extrémně robustní a často vysílaná, a usnadňovala tak rychlé objevení buňky a počáteční přístup uživatelského zařízení (UE). NR-MIB je mapován na specifické zdrojové prvky v rámci [SS](/mobilnisite/slovnik/ss/)/[PBCH](/mobilnisite/slovnik/pbch/) bloku (SSB), který je vysílán s definovanou periodicitou, typicky 20 ms. Jeho vysílání je beamformované a více SSB může být vysíláno v různých prostorových směrech pro podporu správy beamů a počátečního výběru beamu pro UE.

Obsah NR-MIB je záměrně minimální a statický, aby bylo zajištěno spolehlivé dekódování i za špatných rádiových podmínek. Nese nejkritičtější parametry, které UE potřebuje pro zahájení komunikace s buňkou. Patří mezi ně číslo systémového rámce ([SFN](/mobilnisite/slovnik/sfn/)), konkrétně 6 nejvýznamnějších bitů z 10bitového SFN, přičemž zbývající bity jsou odvozeny ze scramblování užitečného zatížení PBCH. Dále udává rozteč podnosných ([SCS](/mobilnisite/slovnik/scs/)) společnou pro SSB a počáteční downlink šířku pásma ([BWP](/mobilnisite/slovnik/bwp/)). Signalizuje také konfiguraci Control Resource Set ([CORESET](/mobilnisite/slovnik/coreset/)) pro společný prohledávací prostor Type0-PDCCH, což je brána pro UE k nalezení a dekódování zbývajících bloků systémových informací ([SIB](/mobilnisite/slovnik/sib/)), jako je SIB1. MIB také obsahuje pole indikující, zda je informace o zákazu buňky (cell-barred) přítomna v SIB1.

Z architektonického hlediska je NR-MIB generován vrstvou Radio Resource Control (RRC) na gNB. Vrstva RRC zabalí informace MIB do RRC zprávy, která je pak předána dolů přes vrstvy Packet Data Convergence Protocol (PDCP), Radio Link Control (RLC) a Medium Access Control (MAC). Na fyzické vrstvě jsou bity MIB kanálově kódovány, scramblovány, modulovány (pomocí QPSK) a mapovány na zdrojové prvky PBCH v rámci SSB. Celý SSB, včetně PSS, SSS a PBCH (nesoucího MIB), je samostatný blok, který může UE detekovat a dekódovat, aby získala počáteční časování, frekvenční synchronizaci a tyto základní systémové parametry. Úspěšné dekódování NR-MIB je předpokladem pro všechny následné kroky v proceduře náhodného přístupu a připojení k síti.

## K čemu slouží

NR-MIB byl vytvořen pro potřeby vysoce spolehlivého a efektivního mechanismu pro vysílání nejkritičtějších systémových informací v sítích 5G NR. Na rozdíl od MIB v LTE, který byl relativně jednoduchý, musel NR-MIB podporovat mnohem širší škálu scénářů nasazení, včetně frekvencí milimetrových vln (mmWave) s beamformingem. Primární problém, který řeší, je umožnit UE rychle a spolehlivě získat absolutní časování buňky (prostřednictvím SFN) a potřebnou konfiguraci k nalezení řídicích kanálů, které nesou zbytek systémových informací. Bez MIB by UE nebylo schopno určit časovou strukturu buňky ani vědět, kde hledat PDCCH, který plánuje SIB1.

Historicky vysílané systémové informace v předchozích generacích (jako MIB v LTE) poskytovaly podobné funkce, ale nebyly navrženy pro flexibilní numerologii a beam-centric provoz 5G. Mezi motivace návrhu NR-MIB patří minimalizace doby synchronizace pro UE, což je klíčové pro snížení latence připojení – klíčového výkonnostního ukazatele 5G. Také musel být dekódovatelný z jediného SSB burstu, aby podpořil počáteční beam sweeping, kdy UE může během vyhledávání buňky spolehlivě přijímat vždy pouze jeden beam. Zabalením základních informací do malého, robustního užitečného zatížení a jejich vysíláním v rámci SSB NR-MIB zajišťuje, že UE mohou zahájit přístupovou proceduru s minimálním zpožděním, a to i v náročných rádiových prostředích nebo při použití vysokofrekvenčních pásem s direkčními beamy.

## Klíčové vlastnosti

- Nese 6 nejvýznamnějších bitů čísla systémového rámce (SFN)
- Udává rozteč podnosných pro SS/PBCH blok a počáteční downlink BWP
- Signalizuje konfiguraci CORESET pro společný prohledávací prostor Type0-PDCCH
- Vysílán na NR-PBCH v rámci SS/PBCH bloku (SSB)
- Pro spolehlivý příjem používá robustní modulaci QPSK a kanálové kódování
- Podporuje beamformované vysílání jako součást SSB pro mmWave a operace v FR2

## Související pojmy

- [CORESET – Control Resource Set](/mobilnisite/slovnik/coreset/)
- [SIB1 – System Information Block Type 1](/mobilnisite/slovnik/sib1/)

## Definující specifikace

- **TS 37.470** (Rel-19) — W1 Interface Introduction for ng-eNB
- **TS 38.470** (Rel-19) — F1 Interface Introduction

---

📖 **Anglický originál a plná specifikace:** [NR-MIB na 3GPP Explorer](https://3gpp-explorer.com/glossary/nr-mib/)
