---
slug: "naswm"
url: "/mobilnisite/slovnik/naswm/"
type: "slovnik"
title: "NASWM – Non-Automated Software Management"
date: 2025-01-01
abbr: "NASWM"
fullName: "Non-Automated Software Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/naswm/"
summary: "Koncept správy podle 3GPP pro ruční aktualizace softwaru a údržbové operace v telekomunikačních sítích. Definuje postupy pro člověkem řízené nasazení softwaru, jeho ověření a návrat k předchozí verzi,"
---

NASWM je koncept správy podle 3GPP pro ruční aktualizace softwaru a údržbové operace, který definuje člověkem řízené postupy pro nasazení, ověření a návrat k předchozí verzi, aby zajistil řízené změny síťových prvků.

## Popis

Non-Automated Software Management (NASWM) je rámec specifikovaný v rámci standardů správy 3GPP (TS 32.531), který řídí ruční procesy pro správu softwaru v síťových prvcích. Funguje v rámci širšího systému Operations, Administration, and Maintenance (OAM) a poskytuje strukturovaný, standardizovaný přístup, který operátorům umožňuje provádět softwarové aktivity bez spoléhání na plnou automatizaci. Architektura zahrnuje Network Manager ([NM](/mobilnisite/slovnik/nm/)) nebo Element Manager ([EM](/mobilnisite/slovnik/em/)) jako řídicí entitu, která vydává příkazy správy softwaru Managed Element ([ME](/mobilnisite/slovnik/me/)), jako je základnová stanice nebo uzel core sítě. ME tyto příkazy následně vykoná a hlásí zpět stav, ale zahájení, sledování kroků a rozhodování provádějí lidské obsluhy prostřednictvím rozhraní správy.

NASWM definuje sadu stavových postupů pokrývajících kompletní životní cyklus softwaru včetně stahování, instalace, aktivace a deaktivace softwaru. Mezi klíčové komponenty patří stavový automat Software Management State Machine uvnitř spravovaného prvku, který sleduje aktuální provozní stav (např. nečinný, stahování, nainstalováno, aktivní), a související objekty Management Information Base ([MIB](/mobilnisite/slovnik/mib/)), které reprezentují inventář softwaru a jeho stav. NM/EM komunikuje s těmito MIB objekty pomocí standardizovaných protokolů jako SNMP nebo rozhraní založená na [CORBA](/mobilnisite/slovnik/corba/) (podle Itf-N), vydává příkazy, které převádějí ME přes předdefinované stavy. Tím je zajištěno, že i ruční operace následují konzistentní, předvídatelný vzor, což snižuje riziko chyb a nestability sítě.

Jeho úlohou v síti je poskytovat záložní nebo alternativní řešení k Automated Software Management ([ASWM](/mobilnisite/slovnik/aswm/)) a vyhovět scénářům, kde regulační, politická nebo technická omezení brání plně automatizovaným aktualizacím. Například v bezpečnostně kritických sítích nebo při zásadních upgradech verzí mohou operátoři vyžadovat ruční ověření v každém kroku. NASWM zajišťuje, že tyto ruční procesy jsou stále integrovány do formálního OAM rámce, což umožňuje záznamy pro audit, reportování souladu a sladění s celkovým modelem Fault, Configuration, Accounting, Performance, and Security (FCAPS). Je zvláště relevantní pro správu softwaru zařízení Radio Access Network (RAN) a funkcí core sítě, kde musí být výpadek pečlivě plánován a kontrolován.

## K čemu slouží

NASWM byl vytvořen, aby řešil potřebu standardizovaného, operátorem řízeného procesu správy softwaru v sítích 3GPP. Před jeho specifikací byly softwarové aktualizace často proprietárními, ad-hoc postupy dodavatelů, kterým chyběla interoperabilita a konzistentní reportování. To činilo správu multi-vendor sítí komplexní a zvyšovalo riziko lidské chyby při kritických aktualizacích. NASWM poskytuje společný, na protokolu nezávislý rámec, který zajišťuje, že všechny kompatibilní síťové prvky 3GPP podporují základní sadu ručních správních operací, což operátorům umožňuje udržovat software na různorodých zařízeních od různých dodavatelů pomocí jednotného operačního modelu.

Tato technologie existuje, aby řešila problém řízených, auditovatelných změn softwaru v prostředích, kde plné automatizaci není důvěřováno nebo není technicky možné. Některá nasazení sítí, zejména v dřívějších verzích 3GPP nebo v regulovaných odvětvích, vyžadují ruční dohled nad jakoukoli softwarovou změnou. NASWM formalizuje tento dohled definováním přesných stavů, příkazů a notifikací. Také doplňuje [ASWM](/mobilnisite/slovnik/aswm/) tím, že poskytuje záložní mechanismus; pokud automatizovaný postup selže, operátoři se mohou vrátit k ručním procesům definovaným NASWM k obnovení systému. Jeho vytvoření bylo motivováno rostoucí softwarovou komplexností síťových prvků a operační potřebou tuto komplexnost spravovat bez obětování stability nebo kontroly.

## Klíčové vlastnosti

- Definuje standardizovaný stavový automat pro ruční operace životního cyklu softwaru
- Podporuje příkazy pro stahování, instalaci, aktivaci a deaktivaci softwaru
- Integruje se s architekturou OAM 3GPP prostřednictvím rozhraní NM-EM a EM-ME
- Poskytuje objekty Management Information Base (MIB) pro inventář softwaru a jeho stav
- Umožňuje záznamy pro audit a reportování souladu pro ruční změny
- Slouží jako záložní nebo alternativní řešení k Automated Software Management (ASWM)

## Související pojmy

- [ASWM – Automated Software Management](/mobilnisite/slovnik/aswm/)

## Definující specifikace

- **TS 32.531** (Rel-19) — 3GPP TS 32.531: SW Management Concepts & IRP Requirements

---

📖 **Anglický originál a plná specifikace:** [NASWM na 3GPP Explorer](https://3gpp-explorer.com/glossary/naswm/)
