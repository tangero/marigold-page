---
slug: "irp"
url: "/mobilnisite/slovnik/irp/"
type: "slovnik"
title: "IRP – Integration Reference Point"
date: 2026-01-01
abbr: "IRP"
fullName: "Integration Reference Point"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/irp/"
summary: "IRP je rámec 3GPP pro standardizaci rozhraní pro správu mezi systémy provozní podpory (OSS) a síťovými prvky (NE) nebo systémy pro správu sítě (NMS). Definuje informační modely a protokoly (jako CORBA"
---

IRP je rámec 3GPP pro standardizaci rozhraní pro správu mezi systémy provozní podpory (OSS) a síťovými prvky (NE) nebo systémy pro správu sítě (NMS), který umožňuje interoperabilitu mezi různými dodavateli a automatizovanou správu sítě.

## Popis

Integration Reference Point (IRP) je komplexní soubor specifikací 3GPP, který standardizuje rozhraní pro správu mezi systémem manažera (typicky systém provozní podpory – [OSS](/mobilnisite/slovnik/oss/)) a systémem agenta (síťový prvek – [NE](/mobilnisite/slovnik/ne/) nebo doménový manažer). Jeho hlavním cílem je dosáhnout interoperability v prostředí správy telekomunikačních sítí s více dodavateli. IRP definuje tři klíčové aspekty: Informační službu, Řešení (Solution Set) a Protokol. Informační služba je abstraktní, na technologii nezávislý objektově orientovaný model popisující spravované prostředky (např. základnovou stanici, profil účastníka) a operace, které lze nad nimi provádět (např. vytvořit, smazat, notifikovat). To je specifikováno pomocí Unified Modeling Language ([UML](/mobilnisite/slovnik/uml/)).

Řešení (Solution Set) je konkrétní, implementovatelná vazba abstraktní Informační služby na specifickou technologii. 3GPP v průběhu času definovala několik řešení, nejvýznamněji Řešení [CORBA](/mobilnisite/slovnik/corba/) (Common Object Request Broker Architecture) a Řešení [XML](/mobilnisite/slovnik/xml/) (eXtensible Markup Language)/[SOAP](/mobilnisite/slovnik/soap/). Řešení CORBA mapuje třídy UML do CORBA Interface Definition Language ([IDL](/mobilnisite/slovnik/idl/)) a definuje, jak se operace a notifikace přenášejí pomocí CORBA. Řešení XML definuje XML Schema Definitions ([XSD](/mobilnisite/slovnik/xsd/)) pro informační model a používá pro přenos SOAP přes HTTP. Aspekt Protokolu definuje detailní sekvence zpráv, zpracování chyb a komunikační procedury pro zvolenou technologii.

Z architektonického hlediska jsou IRP kategorizovány podle oblastí správy. Mezi klíčové IRP patří Obecný IRP (základní rámec), IRP pro hromadnou konfiguraci (pro přenos velkého objemu dat), Notifikační IRP (pro hlášení událostí), IRP pro správu výkonnosti (pro čítače a měření), IRP pro správu poruch (pro alarmy) a technologicky specifické IRP, jako je IRP pro model síťových prostředků (NRM) UTRA pro 3G nebo IRP pro model síťových prostředků (NRM) E-UTRAN pro LTE. Každý definuje detailní objektový model pro spravované entity v dané doméně. Síťový prvek implementuje jedno nebo více rozhraní agenta IRP, což umožňuje OSS od libovolného dodavatele jej spravovat pomocí standardizovaných operací a informačních modelů.

V praxi rámec IRP umožňuje bezproblémovou integraci síťových zařízení od různých výrobců do jediného OSS. OSS operátora může objevovat, konfigurovat, monitorovat a přijímat alarmy ze základnové stanice Huawei, síťového uzlu jádra od Nokie a systému IMS od Ericssonu pomocí stejné sady standardizovaných rozhraní IRP (pro danou doménu). To výrazně snižuje náklady na integraci, zjednodušuje vývoj softwaru OSS a umožňuje operátorům budovat nejlepší možné sítě bez uzamčení do proprietárního systému správy jediného dodavatele. Rozsáhlá knihovna specifikací (např. série 32) dokumentuje každý IRP velmi podrobně.

## K čemu slouží

Rámec IRP byl vytvořen k řešení kritického problému složitosti správy sítí s více dodavateli. V počátcích telekomunikací každý dodavatel zařízení poskytoval proprietární rozhraní pro správu (jako TL1, SNMP MIBy), která byla jedinečná a nekompatibilní. To nutilo síťové operátory vyvíjet a udržovat samostatné integrace OSS pro zařízení každého dodavatele, což vedlo k enormním nákladům, dlouhým cyklům nasazení a provozní neefektivitě. Nedostatek standardizace byl hlavní překážkou konkurence a inovací.

3GPP zahájila práci na IRP, aby vytvořila jednotný, otevřený standard pro rozhraní správy, podobně jako standardizovala rádiové a síťové protokoly jádra. Cílem bylo umožnit 'plug-and-play' integraci síťových prvků do OSS operátora bez ohledu na dodavatele. To dává operátorům možnost vybírat síťová zařízení na základě technických a komerčních kvalit, aniž by byli omezeni problémy integrace OSS. Také snižuje vstupní bariéru pro nové dodavatele, protože mohou implementovat standardní IRP a být spravovatelní jakýmkoli kompatibilním OSS.

Historicky se rámec IRP vyvinul z dřívějších iniciativ TM Forum, ale byl 3GPP přizpůsoben a výrazně rozšířen, aby pokryl specifické potřeby sítí 3G, 4G a nyní i 5G. Řeší omezení obecných protokolů pro správu, jako je SNMP, kterým chybělo bohaté, objektově orientované datové modelování potřebné pro komplexní telekomunikační zařízení. Tím, že poskytuje úplnou definici – od abstraktního informačního modelu až po vazbu protokolu – IRP zajišťuje sémantickou interoperabilitu, což znamená, že manažer i agent mají přesné, společné porozumění tomu, co je objekt 'Cell' a co znamená jeho 'blokování', čímž se eliminují chyby v konfiguraci a nesprávné interpretace.

## Klíčové vlastnosti

- Technologicky neutrální abstraktní Informační služba definovaná pomocí UML modelů
- Více konkrétních Řešení (Solution Sets) (např. CORBA, XML/SOAP) pro flexibilitu implementace
- Komplexní pokrytí oblastí správy FCAPS (poruchy, konfigurace, účtování, výkonnost, bezpečnost)
- Podrobné modely síťových prostředků (NRM) pro každou technologickou doménu 3GPP (UTRAN, E-UTRAN, 5GC atd.)
- Standardizované mechanismy pro notifikace a hromadný přenos dat pro efektivní správu
- Umožňuje skutečnou interoperabilitu mezi různými dodavateli pro integraci OSS a automatizované operace

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [CORBA – Common Object Request Broker Architecture](/mobilnisite/slovnik/corba/)
- [SOAP – Simple Object Access Protocol](/mobilnisite/slovnik/soap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 28.601** (Rel-12) — Telecom management; CN and non-3GPP access NRM IRP Requirements
- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.611** (Rel-19) — EPC-WLAN Interworking NRM IRP Requirements
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.621** (Rel-19) — Generic Network Resource Model (NRM) IRP Requirements
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.624** (Rel-19) — State Management Data Definition IRP Requirements
- **TS 28.625** (Rel-19) — State Management Data Definition IRP Information Service
- **TS 28.626** (Rel-19) — State Management Data Definition IRP Solution Set
- **TS 28.629** (Rel-19) — SON Policy NRM IRP Solution Set Definitions
- **TS 28.631** (Rel-19) — Inventory Management NRM IRP Requirements
- **TS 28.632** (Rel-19) — Inventory Management NRM Integration Reference Point
- **TS 28.633** (Rel-19) — Inventory Management NRM IRP Solution Set definitions
- … a dalších 222 specifikací

---

📖 **Anglický originál a plná specifikace:** [IRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/irp/)
