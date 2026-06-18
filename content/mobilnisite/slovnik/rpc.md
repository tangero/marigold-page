---
slug: "rpc"
url: "/mobilnisite/slovnik/rpc/"
type: "slovnik"
title: "RPC – Remote Procedure Control"
date: 2026-01-01
abbr: "RPC"
fullName: "Remote Procedure Control"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/rpc/"
summary: "Řídicí protokol a architektura používaná v sítích 3GPP pro vzdálené operace a konfiguraci síťových prvků. Umožňuje řídicímu systému vyvolávat procedury na spravovaných uzlech, jako je odstranění poruc"
---

RPC je řídicí protokol a architektura používaná v sítích 3GPP pro vzdálené operace a konfiguraci síťových prvků, která umožňuje řídicímu systému vyvolávat procedury na spravovaných uzlech.

## Popis

Remote Procedure Control (RPC) v 3GPP označuje standardizovaný mechanismus v rámci architektury Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), který umožňuje řídicímu systému (např. Network Manager, Element Manager) vzdáleně provádět specifické řídicí procedury na spravovaném síťovém prvku ([NE](/mobilnisite/slovnik/ne/)). Nejde o jediný protokol, ale o konceptuální model a sadu rozhraní, často implementovaných pomocí protokolů jako [SNMP](/mobilnisite/slovnik/snmp/) nebo [CORBA](/mobilnisite/slovnik/corba/)/[IDL](/mobilnisite/slovnik/idl/) a v novějších verzích sladěných s NETCONF/YANG. Základní myšlenkou je definovat sadu 'procedur' nebo 'operací', které může síťový prvek na příkaz provést, například resetovat komponentu, spustit diagnostický test nebo aplikovat konfigurační šablonu.

Z architektonického hlediska jsou RPC operace definovány ve specifikacích Integration Reference Point ([IRP](/mobilnisite/slovnik/irp/)) systému správy 3GPP. Řídicí a spravovaná entita komunikují přes standardizovaná rozhraní jako Itf-N nebo northbound rozhraní Element Management System ([EMS](/mobilnisite/slovnik/ems/)). Řídicí systém odešle RPC požadavek obsahující název operace a potřebné parametry. Spravovaná entita proceduru provede a vrátí odpověď s výsledkem a případnými daty. Tím se liší od prosté konfigurace nebo monitorování; RPC slouží k vyvolání aktivních procesů, které mají vedlejší účinky na stav nebo chování síťového prvku.

Klíčové komponenty zahrnují samotnou definici RPC (určující signaturu operace, parametry a chování), vazbu na podkladový komunikační protokol a model zpracování chyb. RPC se používají napříč různými doménami správy: správou poruch (např. 'clearAlarm'), správou konfigurace (např. 'softwareDownload'), správou výkonnosti (např. 'requestPerformanceDataReport') a dalšími. Jejich role je klíčová pro automatizaci složitých, vícestupňových úloh OAM bez manuálního zásahu na síťovém prvku, což umožňuje efektivní správu rozsáhlých sítí. Specifikace jako TS 32.158 (Generic IRP: RPC) poskytují společný rámec, zatímco technologicky specifická IRP (např. pro LTE nebo 5G) definují konkrétní RPC použitelné pro příslušné síťové prvky.

## K čemu slouží

RPC bylo zavedeno, aby řešilo rostoucí složitost a rozsah sítí 3GPP, což činilo manuální, místní správu síťových prvků nepraktickou a nákladnou. Před standardizovanými RPC mechanismy se řídicí systémy často spoléhaly na proprietární příkazové řádky ([CLI](/mobilnisite/slovnik/cli/)) nebo jednoduché přenosy konfiguračních souborů, což vedlo k problémům s integrací, závislosti na dodavateli a omezeným možnostem automatizace. Hlavním problémem, který RPC řeší, je poskytnutí jednotného, interoperabilního způsobu, jak mohou řídicí systémy aktivně ovládat a přikazovat síťovým prvkům nad rámec pasivního monitorování.

Vytvoření RPC architektury v rámci standardů OAM 3GPP bylo motivováno potřebou robustního odstranění poruch, automatizované správy softwaru a hromadných konfiguračních operací. Například místo toho, aby se technik přihlašoval do základnové stanice a ručně mazal přetrvávající alarm, mohl by centrální Network Manager vyvolat RPC 'reset'. To umožňuje kratší střední dobu opravy (MTTR) a snižuje provozní náklady (OPEX). Historicky, jak se sítě vyvíjely od 3G přes 4G až k 5G s rostoucím počtem malých buněk a virtualizovaných funkcí, se potřeba takového vzdáleného, automatizovaného řízení stala kritickou. Model RPC poskytl základní abstrakci, kterou bylo možné přizpůsobit různým technologiím řídicích rozhraní, od raných řešení založených na CORBA až po moderní přístupy řízené datovými modely využívající NETCONF a RESTCONF.

## Klíčové vlastnosti

- Standardizované definice operací napříč řídicími IRP
- Umožňuje aktivní řízení a provádění příkazů na spravovaných NE
- Podporuje synchronní a asynchronní vyvolávání operací
- Obsahuje komplexní validaci parametrů a hlášení chyb
- Usnadňuje automatizaci složitých pracovních postupů OAM
- Vazby na více transportních protokolů (např. CORBA, SNMP, NETCONF)

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- **TS 29.891** (Rel-16) — CT4 Aspects of 5G System Phase 1
- **TS 32.158** (Rel-20) — Management and Orchestration REST Solution Sets
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.583** (Rel-19) — HNB OAM&P Procedure Flows for Type 1 Interface
- **TS 32.593** (Rel-19) — HeNB OAM&P Procedure Flows for Type 1 Interface
- **TS 32.818** (Rel-8) — SA5 MTOSI XML Harmonization Study
- **TS 32.824** (Rel-9) — SOA and IRP Gap Analysis

---

📖 **Anglický originál a plná specifikace:** [RPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rpc/)
