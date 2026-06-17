---
slug: "csg"
url: "/mobilnisite/slovnik/csg/"
type: "slovnik"
title: "CSG – Closed Subscriber Group"
date: 2025-01-01
abbr: "CSG"
fullName: "Closed Subscriber Group"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/csg/"
summary: "Skupina uzavřených účastníků (CSG) je sada účastníků oprávněných přistupovat k jedné nebo více CSG buňkám, které jsou typicky nasazovány jako femtobuňky nebo small cells na soukromých místech. Umožňuj"
---

CSG je skupina účastníků oprávněných přistupovat ke konkrétním buňkám, jako jsou femtobuňky, čímž vytváří omezené soukromé pokrytí pro podnikové nebo rezidenční použití.

## Popis

Skupina uzavřených účastníků (CSG) je základní koncept v sítích 3GPP, který definuje skupinu účastníků s oprávněním přistupovat ke konkrétním CSG buňkám. Tyto buňky jsou typicky nízkopříkonové přístupové body jako Home NodeBs ([HNB](/mobilnisite/slovnik/hnb/)) v UMTS nebo Home eNodeBs (HeNB) v LTE, nasazené v rezidenčním, podnikovém nebo kampusovém prostředí. Mechanismus CSG vytváří virtuální privátní síť uvnitř veřejné mobilní sítě, což operátorům umožňuje nabízet šité na míru řešení pokrytí a kapacity při zachování kontroly nad přístupovými právy.

Architektura se točí kolem CSG Identity (CSG ID), což je jedinečný identifikátor vysílaný CSG buňkou. Tento CSG ID je uložen v modulu Universal Subscriber Identity Module (USIM) účastníka v rámci CSG listu, který obsahuje všechny CSG ID, k nimž je účastník oprávněn přistupovat. Když se UE pokouší o přihlášení k buňce nebo o handover na ni, porovná vysílaný CSG ID se svým uloženým CSG listem. Jádrová síť, konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) v UMTS, ověřuje členství UE v CSG během procedur připojení a aktualizace oblasti sledování, přičemž se dotazuje Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), který uchovává CSG předplatitelská data účastníka.

CSG buňky pracují ve třech režimech: Uzavřený (Closed), Hybridní (Hybrid) a Otevřený (Open). V Uzavřeném režimu mají přístup k buňce pouze členové CSG. Hybridní režim umožňuje přístup jak členům CSG, tak nečlenům, ale členové mají prioritu nebo lepší QoS. Otevřený režim je v podstatě normální buňka bez CSG omezení. Koncept CSG je úzce integrován s mechanismy řízení přístupu, správou mobility a systémy účtování. Během procedur handoveru jsou přístupový režim cílové CSG buňky a členství UE v CSG kritickými faktory v rozhodovacích algoritmech handoveru prováděných zdrojovým eNodeB nebo Radio Network Controller (RNC).

Implementace vyžaduje koordinaci napříč více síťovými elementy. Systém Operation, Administration and Maintenance (OAM) spravuje konfiguraci CSG buněk a přiřazení CSG ID. Architektura policy and charging control (PCC) může aplikovat specifická pravidla pro CSG přístup. Dále CSG buňky často podporují funkce Self-Organizing Network (SON) pro automatickou konfiguraci a optimalizaci. Koncept se rozšiřuje na scénáře sdílení sítě, kde více operátorů může sdílet CSG infrastrukturu při zachování samostatných CSG listů pro své příslušné účastníky.

## K čemu slouží

Koncept CSG byl zaveden, aby řešil rostoucí potřebu řízeného buněčného přístupu v soukromém a polosoukromém prostředí, zejména s rozšířením femtobuněk a small cells. Před CSG nabízely buněčné sítě buď plně veřejný přístup (makro buňky), nebo zcela privátní systémy (jako tradiční PBX nebo [DECT](/mobilnisite/slovnik/dect/)), bez bezproblémové integrace mezi veřejnou a privátní doménou. Tato mezera omezovala schopnost operátorů poskytovat cílená řešení vnitřního pokrytí při zachování kontinuity služeb a řízení přístupu.

CSG řeší několik klíčových problémů: Umožňuje operátorům nabízet rezidenční femtobuňky, které poskytují výborné pokrytí uvnitř budov pro konkrétní domácnosti, aniž by umožňovaly přístup v celém sousedství. Pro podniky CSG umožňuje vytvářet podnikové buněčné sítě s řízeným přístupem pro zaměstnance při zachování integrace s veřejnou mobilní sítí. Technologie také řeší odlehčování kapacity přesměrováním autorizovaných uživatelů na vyhrazené small cells při efektivním řízení interference a alokace zdrojů.

Historicky vycházela motivace z revoluce femtobuněk v 3GPP Release 8, kde operátoři potřebovali mechanismy pro nasazení tisíců zařízení u zákazníků při zachování síťové bezpečnosti, možností zákonného odposlechu a správného účtování. CSG poskytlo standardizovaný rámec pro řízení přístupu, který byl škálovatelný, bezpečný a interoperabilní napříč zařízeními různých výrobců. Také umožnilo nové obchodní modely, jako je sponzorovaný přístup na místech konání akcí nebo zvýhodněné zacházení pro určité skupiny účastníků, které nebyly možné s tradičními buněčnými architekturami.

## Klíčové vlastnosti

- Definuje skupiny účastníků s autorizovaným přístupem ke konkrétním buňkám
- Používá CSG Identity (CSG ID) vysílanou buňkami a uloženou v USIM
- Podporuje tři režimy přístupu: Uzavřený (Closed), Hybridní (Hybrid) a Otevřený (Open)
- Integruje se s jádrovou sítí pro ověřování předplatného přes HSS
- Umožňuje řízené handovery na základě členství v CSG
- Podporuje automatické sousední relace a SON pro CSG buňky

## Související pojmy

- [CSG-ID – Closed Subscriber Group Identity](/mobilnisite/slovnik/csg-id/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.220** (Rel-19) — Home NodeB/Home eNodeB Service Requirements
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.012** (Rel-19) — Circuit Switched Location Management Procedures
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.285** (Rel-19) — Allowed CSG List Management Object
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- … a dalších 33 specifikací

---

📖 **Anglický originál a plná specifikace:** [CSG na 3GPP Explorer](https://3gpp-explorer.com/glossary/csg/)
