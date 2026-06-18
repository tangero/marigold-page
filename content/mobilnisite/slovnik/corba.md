---
slug: "corba"
url: "/mobilnisite/slovnik/corba/"
type: "slovnik"
title: "CORBA – Common Object Request Broker Architecture"
date: 2025-01-01
abbr: "CORBA"
fullName: "Common Object Request Broker Architecture"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/corba/"
summary: "CORBA je standard pro objektově orientovaný middleware od skupiny Object Management Group (OMG), který umožňuje interakci distribuovaných softwarových komponent napříč různými platformami a programova"
---

CORBA je standard pro middleware, který umožňoval interakci distribuovaných softwarových komponent napříč platformami a byl používán 3GPP pro standardizované řídicí rozhraní v rámci provozu, správy a údržby sítě.

## Popis

CORBA (Common Object Request Broker Architecture) je specifikace vyvinutá skupinou Object Management Group ([OMG](/mobilnisite/slovnik/omg/)), která definuje standardizovaný objektově orientovaný rámec pro vytváření distribuovaných aplikací. V kontextu 3GPP sloužila CORBA jako klíčová middleware technologie pro implementaci řídicích rozhraní, umožňující komunikaci mezi systémy správy sítě (Network Management Systems - [NMS](/mobilnisite/slovnik/nms/)), systémy správy prvků (Element Management Systems - [EMS](/mobilnisite/slovnik/ems/)) a samotnými síťovými prvky (Network Elements - NEs). Její architektura je založena na zprostředkovateli objektových požadavků (Object Request Broker - [ORB](/mobilnisite/slovnik/orb/)), který funguje jako komunikační sběrnice usnadňující objektové požadavky mezi klienty a servery a abstrahuje podrobnosti o podkladové síti, operačních systémech a programovacích jazycích.

Jádrem fungování CORBA v řídicích systémech 3GPP je jazyk pro definici rozhraní (Interface Definition Language - [IDL](/mobilnisite/slovnik/idl/)). Technické specifikace 3GPP definují řídicí rozhraní pomocí CORBA IDL, které specifikuje operace, parametry a datové typy, které musí síťové prvky podporovat. Tato IDL definice je následně přeložena do klientských a serverových stubů (proxy a skeletonů) v cílovém programovacím jazyce (např. C++, Java). Za běhu klient (např. EMS) vyvolá operaci na vzdáleném objektu (hostovaném na [NE](/mobilnisite/slovnik/ne/)) prostřednictvím svého lokálního stubu. ORB se postará o zabalení požadavku do standardizovaného formátu (pomocí General Inter-ORB Protocol - GIOP, často přenášeného přes [TCP/IP](/mobilnisite/slovnik/tcp-ip/) jako [IIOP](/mobilnisite/slovnik/iiop/)), přenese jej přes síť a doručí na ORB serveru. ORB serveru požadavek rozbalí, vyvolá odpovídající metodu na skutečné implementaci objektu a vrátí odpověď stejnou cestou zpět.

Klíčovými komponentami v ekosystému CORBA 3GPP zahrnují jádro ORB, přenosný adaptér objektů (Portable Object Adapter - POA) pro správu životního cyklu objektů na serveru a úložiště rozhraní (Interface Repository) pro informace o typech za běhu. Specifikace 3GPP, zejména řada 32 (Management and Orchestration), definuje komplexní sadu tříd spravovaných objektů (Managed Object - MO) založených na CORBA, které modelují síťové zdroje jako základnové stanice, přepínače a spoje. Tyto MO jsou organizovány ve stromu řídicích informací (Management Information Tree - MIT) a operace na nich se provádějí prostřednictvím standardizovaných CORBA rozhraní, jako jsou ItfN, ItfG a ItfC pro oznámení, získání a nastavení operací. To umožňovalo jednotný programový způsob provádění správy poruch, konfigurace, výkonu a zabezpečení (FCAPS) napříč sítěmi více dodavatelů.

Role CORBA byla zásadní pro dosažení interoperability v řízení sítě. Umožňovala, aby zařízení od různých dodavatelů mohla být spravována jediným řídicím systémem, pokud dodržovala stejné specifikace CORBA IDL. Tímto byl oddělen řídicí logika v NMS/EMS od proprietárních implementací uvnitř každého síťového prvku. Architektura podporovala jak synchronní, tak asynchronní komunikaci, stejně jako oznamování událostí prostřednictvím služby CORBA Event Service, což bylo klíčové pro monitorování alarmů a výkonu. I když bylo její použití v pozdějších vydáních 3GPP (5G a dále) z velké části nahrazeno novějšími technologiemi, jako jsou NETCONF/YANG a RESTful API, CORBA tvořila páteř systémů OAM pro nasazení GSM, UMTS a raného LTE a umožňovala škálovatelnou a automatizovanou správu vyžadovanou pro rozsáhlé mobilní sítě.

## K čemu slouží

CORBA byla přijata 3GPP, aby vyřešila kritický problém interoperability více dodavatelů v řízení sítě. Rané telekomunikační sítě často používaly proprietární řídicí protokoly, což operátory uzamykalo do řešení jediného dodavatele nebo vyžadovalo složitou, vlastní integrační práci. To zvyšovalo náklady, zpomalovalo nasazení a rozšiřování sítě a bránilo inovacím. Hlavní motivací pro specifikaci rozhraní založených na CORBA bylo vytvoření standardizované, dodavatelsky neutrální vrstvy middleware, která by umožnila řídicím systémům komunikovat se síťovými prvky od jakéhokoli dodavatele, který standard implementoval.

Historicky, před rozšířeným přijetím CORBA, byla řídicí rozhraní často založena na TL1 (Transaction Language 1) nebo jednoduchém SNMP, která měla omezení ve vyjadřování složitých, objektově orientovaných modelů řídicích dat a operací. CORBA nabídla výkonnější a flexibilnější alternativu. Poskytovala definici rozhraní nezávislou na programovacím jazyku (IDL), podporu pro složité datové typy a vztahy mezi objekty a robustní mechanismus vzdáleného volání procedur (Remote Procedure Call - RPC). To bylo nezbytné pro modelování sofistikovaných zdrojů sítě 3GPP (jako NodeB nebo MME) jako objektů s atributy, operacemi a hierarchiemi dědičnosti.

Vytvoření specifikací CORBA 3GPP bylo hnací silou potřeby automatizovaných, efektivních systémů podpory provozu (Operations Support Systems - OSS). Jak sítě rostly ve velikosti a složitosti, ruční konfigurace a správa poruch se staly nemožnými. CORBA umožnila vývoj automatizovaných systémů pro zřizování služeb, sběr dat o výkonu a korelaci alarmů. Řešila omezení předchozích přístupů tím, že nabízela skutečný model distribuovaných objektů, silné typování prostřednictvím IDL (které snižovalo integrační chyby) a zralou sadu podpůrných služeb (pojmenování, události, transakce). To umožnilo 3GPP definovat komplexní model síťových zdrojů (Network Resource Model - NRM), kde každá spravovatelná entita v síti mohla být reprezentována a řízena konzistentním programovým způsobem, což položilo základy moderních architektur OSS/BSS v telekomunikacích.

## Klíčové vlastnosti

- Standardizovaný jazyk pro definici rozhraní (Interface Definition Language - IDL) pro specifikaci dodavatelsky neutrálního API
- Zprostředkovatel objektových požadavků (Object Request Broker - ORB) umožňující komunikaci napříč heterogenními platformami a jazyky
- Komplexní model síťových zdrojů (Network Resource Model - NRM) pro reprezentaci síťových prvků jako spravovaných objektů
- Podpora synchronních operací, asynchronních oznámení a služeb událostí
- Integrace se stromem řídicích informací 3GPP (Management Information Tree - MIT) pro hierarchickou organizaci zdrojů
- Základ pro funkce správy FCAPS (Fault, Configuration, Accounting, Performance, Security)

## Související pojmy

- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)
- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 28.303** (Rel-19) — LSA Controller IRP Solution Set Definitions
- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.626** (Rel-19) — State Management Data Definition IRP Solution Set
- **TS 28.629** (Rel-19) — SON Policy NRM IRP Solution Set Definitions
- **TS 28.633** (Rel-19) — Inventory Management NRM IRP Solution Set definitions
- **TS 28.653** (Rel-19) — UTRAN NRM IRP Solution Set Definition
- **TS 28.656** (Rel-19) — GERAN NRM IRP Solution Set Definitions
- **TS 28.659** (Rel-19) — E-UTRAN NRM IRP Solution Set Definitions
- **TS 28.663** (Rel-19) — Generic RAN NRM IRP Solution Set Definitions
- **TS 28.673** (Rel-19) — HNS NRM IRP Solution Set Definitions
- **TS 28.676** (Rel-19) — HeNS NRM IRP Solution Set Definitions
- **TS 28.703** (Rel-19) — Core Network NRM IRP Solution Set Definitions
- … a dalších 81 specifikací

---

📖 **Anglický originál a plná specifikace:** [CORBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/corba/)
