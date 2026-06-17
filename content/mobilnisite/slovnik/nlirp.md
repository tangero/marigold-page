---
slug: "nlirp"
url: "/mobilnisite/slovnik/nlirp/"
type: "slovnik"
title: "NLIRP – Notification Log Integration Reference Point"
date: 2025-01-01
abbr: "NLIRP"
fullName: "Notification Log Integration Reference Point"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nlirp/"
summary: "Standardizované rozhraní v rámci systému správy 3GPP, které definuje způsob přístupu a správy protokolů notifikací. Umožňuje systémům pro podporu provozu (OSS) konzistentním způsobem získávat historic"
---

NLIRP je standardizované 3GPP rozhraní pro správu určené pro přístup a správu protokolů notifikací, které umožňuje systémům OSS konzistentně získávat historické záznamy alarmů a událostí pro auditování, řešení problémů a dodržování předpisů.

## Popis

Notification Log Integration Reference Point (NLIRP) je specifický typ Integration Reference Point ([IRP](/mobilnisite/slovnik/irp/)) definovaný v řadě specifikací 3GPP Telecommunication Management. IRP standardizuje interakce mezi manažerem (např. [OSS](/mobilnisite/slovnik/oss/)) a agentem (např. síťový prvek nebo systém správy prvků) pro konkrétní oblast správy. NLIRP se výhradně zaměřuje na správu protokolů notifikací. Notifikace v tomto kontextu zahrnují alarmy, události změny stavu a další významné události hlášené síťovými prvky.

Z architektonického hlediska NLIRP definuje sadu operací, které může manažer vyvolat na protokolu notifikací agenta. Tyto operace jsou podrobně specifikovány v dokumentu TS 32.332 (Alarm IRP: Notification Log) a souvisejících dokumentech. Mezi klíčové operace patří 'getLogSize', která získá aktuální počet notifikací v protokolu; 'getLogInformation', která získá metadata o protokolu; a zásadní operace 'getNotifications', která umožňuje manažerovi získat filtrovanou množinu zaznamenaných notifikací na základě kritérií, jako je časové rozmezí, závažnost nebo třída objektu. Datový model pro samotné notifikace odpovídá definicím Alarm IRP a dalších relevantních definic notifikací.

NLIRP funguje tak, že poskytuje standardizované programové rozhraní pro přístup k protokolu. Namísto proprietárních mechanismů pro výpis protokolů nebo exportů databází od každého dodavatele NLIRP vyžaduje společnou sadu operací [CORBA](/mobilnisite/slovnik/corba/) (Common Object Request Broker Architecture) [IDL](/mobilnisite/slovnik/idl/) (Interface Definition Language) nebo jejich ekvivalent v pozdějších implementacích založených na webových službách (jako SOAP/XML). Agent udržuje cirkulární nebo perzistentní protokol notifikací podle své implementace. Když manažer vyvolá operaci 'getNotifications', agent dotazuje tento interní protokol, aplikuje případné dodané filtry a vrací výsledky ve standardizovaném formátu. Tím se OSS odděluje od konkrétní implementace úložiště protokolů každého síťového prvku.

Jeho role v síti je klíčová pro následnou analýzu a dodržování regulatorních požadavků. Operátoři sítí používají NLIRP k systematickému sběru historických dat o alarmech ze všech spravovaných prvků bez ohledu na dodavatele, a to pro analýzu hlavní příčiny výpadků, zhoršení výkonu nebo bezpečnostních incidentů. Standardizované rozhraní zajišťuje, že záznamy o činnosti jsou úplné a dostupné, což je často požadavek pro reportování smluv o úrovni služeb (SLA) a telekomunikační regulace. Je klíčovou součástí umožňující automatizované, rozsáhlé zajištění kvality sítě a analytiku.

## K čemu slouží

NLIRP byl vytvořen k řešení problému s fragmentovanými a nepřístupnými historickými daty notifikací v více-dodavatelských telekomunikačních sítích. Před jeho standardizací měl každý síťový prvek nebo [EMS](/mobilnisite/slovnik/ems/) dodavatele svou vlastní proprietární metodu pro ukládání a získávání protokolů alarmů. To velmi ztěžovalo centrálnímu [OSS](/mobilnisite/slovnik/oss/) sestavit jednotnou historii událostí v celé síti pro analýzu. Řešení rozsáhlých problémů vyžadovalo ruční sběr protokolů z desítek různých systémů, což byl pomalý a náchylný k chybám proces.

Motivace vycházela ze snahy 3GPP o provozní efektivitu a standardizovanou správu FCAPS (Fault, Configuration, Accounting, Performance, Security). Základním principem správy poruch je schopnost procházet minulé události za účelem identifikace vzorců a hlavních příčin. NLIRP poskytuje tuto schopnost způsobem nezávislým na dodavateli. Řeší omezení ad-hoc metod přístupu k protokolům definováním přesného rozhraní založeného na kontraktu, které musí podporovat všechny kompatibilní síťové prvky.

Historicky, zavedený ve vydání 8 spolu se širším rámcem Alarm [IRP](/mobilnisite/slovnik/irp/), NLIRP zaplnil konkrétní mezeru v interoperabilitě správy. Zatímco hlášení alarmů v reálném čase řešily jiné IRP, potřeba historického dotazování byla stejně důležitá. Umožnil vývoj pokročilých OSS aplikací pro analytiku protokolů, korelaci a dlouhodobou analýzu trendů bez nutnosti vlastní integrace pro každý nový typ síťového prvku, čímž se snížily provozní náklady a zvýšila spolehlivost sítě.

## Klíčové vlastnosti

- Standardizovaná sada operací pro získávání protokolu notifikací (getNotifications, getLogSize)
- Definuje rozhraní založené na kontraktu (např. CORBA IDL) mezi manažerem a agentem
- Podporuje filtrování dotazů na protokol na základě času, závažnosti a dalších kritérií
- Funguje ve spojení s Alarm IRP a dalšími definicemi notifikací
- Umožňuje centralizovanou, na dodavateli nezávislou analýzu historických událostí
- Nezbytný pro auditování sítě, řešení problémů a reportování pro dodržování předpisů

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 32.332** (Rel-19) — Notification Log IRP Information Service
- **TS 32.336** (Rel-19) — Notification Log IRP Solution Set Definitions
- **TS 32.337** (Rel-9) — Notification Log IRP SOAP Solution Set

---

📖 **Anglický originál a plná specifikace:** [NLIRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nlirp/)
