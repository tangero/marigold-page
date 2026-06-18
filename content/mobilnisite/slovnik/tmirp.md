---
slug: "tmirp"
url: "/mobilnisite/slovnik/tmirp/"
type: "slovnik"
title: "TMIRP – Test Management Integration Reference Point"
date: 2025-01-01
abbr: "TMIRP"
fullName: "Test Management Integration Reference Point"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tmirp/"
summary: "Standardizované rozhraní 3GPP (IRP) pro správu testovacích operací a zdrojů v telekomunikační síti. Umožňuje automatizovanou konfiguraci, provádění a sběr výsledků pro testování síťových prvků a služe"
---

TMIRP je standardizované rozhraní 3GPP pro správu automatizovaných testovacích operací a zdrojů, umožňující konfiguraci, provádění a sběr výsledků pro validaci sítě a služeb.

## Popis

Test Management Integration Reference Point (TMIRP) je součást systému správy sítě ([NM](/mobilnisite/slovnik/nm/)) 3GPP, definovaný v rámci obecného frameworku Integration Reference Point ([IRP](/mobilnisite/slovnik/irp/)). Poskytuje standardizované severní rozhraní pro aplikace Operations Support System ([OSS](/mobilnisite/slovnik/oss/)) pro správu testovacích funkcí napříč síťovými prvky (NEs) nebo systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)). TMIRP abstrahuje složitost dodavatelsky specifických testovacích procedur, což síťovým operátorům umožňuje automatizovat a zefektivnit testovací pracovní postupy pro instalaci, uvedení do provozu, přijetí, diagnostiku chyb a periodické kontroly stavu. Jeho specifikace jsou primárně pokryty v 3GPP TS 32.325 (definice Solution Set ([SS](/mobilnisite/slovnik/ss/))) a TS 32.326 (požadavky).

Architektonicky TMIRP následuje standardní model IRP, který typicky používá paradigma manažer-agent přes protokoly jako Common Object Request Broker Architecture ([CORBA](/mobilnisite/slovnik/corba/)) nebo nověji webové služby/[HTTP](/mobilnisite/slovnik/http/). OSS funguje jako IRPManager, zatímco síťový prvek nebo jeho EMS implementuje IRPAgent pro TMIRP. Rozhraní definuje sadu spravovaných objektů, notifikací a operací. Klíčové spravované objekty zahrnují Test Subsystem, který reprezentuje testovací schopnosti síťového prvku, a specifické Test objekty, které modelují jednotlivé testovací instance, jejich konfigurace, plány a výsledky. Operace umožňují manažerovi vytvářet, plánovat, spouštět, zastavovat a mazat testy, stejně jako získávat výsledky a stav.

TMIRP podporuje širokou škálu typů testů, které lze široce kategorizovat. Patří mezi ně testy konektivity (např. loopback, ping), testy transportní vrstvy, testy shody protokolu, testy kvality služeb (např. pro hlasové nebo datové přenosy) a hardwarové diagnostiky. Kritickým aspektem jeho návrhu je koncept testovacích sad a testovacích případů, což umožňuje definovat a provádět složité, vícestupňové testovací procedury jako jednu spravovanou entitu. IRP také definuje notifikace (alarmy/události) pro hlášení změn stavu testu (např. test spuštěn, dokončen, selhal) a výsledků. To umožňuje OSS proaktivně monitorovat provádění testů a integrovat výsledky do širších procesů správy chyb a správy výkonu. Poskytnutím tohoto standardizovaného rozhraní TMIRP usnadňuje multi-vendorovou interoperabilitu v síťovém testování, snižuje provozní náklady spojené s manuálním testováním a zlepšuje rychlost a spolehlivost validace sítě a izolace chyb.

## K čemu slouží

TMIRP byl vyvinut k řešení provozních neefektivit a vysokých nákladů spojených s manuálními, dodavatelsky proprietárními testovacími procedurami v multi-vendorových telekomunikačních sítích. Před jeho standardizací se operátoři spoléhali na prvkově specifická rozhraní příkazového řádku ([CLI](/mobilnisite/slovnik/cli/)) nebo vlastní skripty pro konfiguraci a provádění testů, což ztěžovalo implementaci automatizovaných, celosíťových testovacích kampaní. Tento nedostatek standardizace vedl ke zvýšeným provozním výdajům (OPEX), delší době opravy chyb a nekonzistentním testovacím metodologiím napříč různými síťovými segmenty.

Jeho vytvoření bylo motivováno širším cílem 3GPP definovat standardizovaná rozhraní pro správu všech aspektů síťových operací jako součást frameworků Telecommunications Management Network (TMN) a později Enhanced Telecom Operations Map (eTOM). TMIRP konkrétně řeší problém fragmentace správy testů. Poskytuje jednotné, technologicky agnostické rozhraní, které umožňuje OSS ovládat testovací zdroje bez ohledu na dodavatele podkladového síťového prvku nebo technologii (2G, 3G, 4G atd.). To operátorům umožňuje budovat centralizované, automatizované testovací systémy pro end-to-end validaci služeb, proaktivní monitorování stavu sítě a rychlou diagnostiku chyb. Díky abstrakci testovacích schopností TMIRP také chrání investice do OSS do budoucna, protože nové síťové prvky nebo typy testů lze integrovat podporou stejného standardizovaného rozhraní, aniž by bylo nutné nákladné přepracování OSS.

## Klíčové vlastnosti

- Standardizované rozhraní pro vytváření, plánování a řízení provádění testů
- Podpora různorodých typů testů (konektivita, protokol, kvalita služeb, hardware)
- Definice spravovaných objektů pro testy, testovací sady a výsledky
- Notifikační mechanismus pro hlášení stavu testů a událostí v reálném čase
- Technologicky agnostický návrh použitelný napříč síťovými prvky 2G/3G/4G/5G
- Umožňuje automatizaci pracovních postupů pro uvedení sítě do provozu, přijetí a diagnostiku chyb

## Související pojmy

- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [CORBA – Common Object Request Broker Architecture](/mobilnisite/slovnik/corba/)

## Definující specifikace

- **TS 32.325** (Rel-9) — Test Management IRP XML Definitions
- **TS 32.326** (Rel-19) — Test Management IRP Solution Set Definitions

---

📖 **Anglický originál a plná specifikace:** [TMIRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmirp/)
