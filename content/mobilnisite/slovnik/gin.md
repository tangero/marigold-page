---
slug: "gin"
url: "/mobilnisite/slovnik/gin/"
type: "slovnik"
title: "GIN – Group ID for Network Selection"
date: 2026-01-01
abbr: "GIN"
fullName: "Group ID for Network Selection"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gin/"
summary: "Identifikátor zavedený v 5G pro reprezentaci skupiny sítí (např. roamingu konsorcia) pro prioritní výběr sítě a řízení přístupu. Umožňuje zařízením vybrat preferovanou síť ze skupiny, čímž zlepšuje už"
---

GIN je identifikátor v 5G, který reprezentuje skupinu sítí a umožňuje zařízením vybrat preferovanou síť z této skupiny za účelem zlepšení roamingu a řízení přístupu.

## Popis

Group ID for Network Selection (GIN) je síťový identifikátor definovaný ve specifikacích 5G systému počínaje 3GPP Release 17. Strukturně je součástí identifikátoru Public Land Mobile Network (PLMN) ID nebo je používán spolu s ním. PLMN ID se typicky skládá z Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)) a Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)). GIN poskytuje další úroveň seskupení, umožňující logicky spojit více různých PLMN (každý se svým vlastním MNC) pod jediný skupinový identifikátor. Tato skupina může reprezentovat konsorcium operátorů, podnikovou síť pokrývající více zemí nebo poskytovatele služeb s dohodami s několika přístupovými sítěmi. GIN je signalizován v blocích systémové informace (SIB) přes rádiové rozhraní a používá ho User Equipment (UE) během procedur výběru a převýběru buňky.

Architektonicky je GIN vysílán Radio Access Network (RAN) v SIB1 a dalších relevantních systémových informacích, jak je specifikováno v TS 38.331 (Radio Resource Control protokol). Uzel NG-RAN (gNB) je konfigurován tímto parametrem systémem Operation and Maintenance (OAM) nebo jádrem sítě. Když UE hledá vhodnou buňku, čte PLMN ID a pokud je přítomen, také GIN z vysílacích kanálů. Politika UE, která může být předkonfigurována v Universal Subscriber Identity Module (USIM) nebo poskytnuta sítí přes [ANDSP](/mobilnisite/slovnik/andsp/) (Access Network Discovery and Selection Policy), ji může instruovat, aby upřednostňovala buňky vysílající konkrétní GIN. Například UE patřící globálnímu podniku může být nakonfigurováno tak, aby vybíralo jakoukoli síť vysílající podnikový GIN bez ohledu na konkrétní MNC, což zajišťuje konektivitu na preferovaných partnerských sítích při roamingu.

Jak to funguje, zahrnuje jak síť, tak UE. Síťový operátor nakonfiguruje gNB patřící do konsorcia tak, aby vysílaly dohodnutou hodnotu GIN. UE během svého počátečního výběru PLMN nebo vyhledávání s vyšší prioritou vyhodnocuje nejen PLMN ID, ale také GIN. Pokud politika UE obsahuje záznam GIN s vyšší prioritou než registrovaný [HPLMN](/mobilnisite/slovnik/hplmn/) (Home PLMN) nebo jiné PLMN, může se pokusit připojit k buňce vysílající tento GIN. Tento mechanismus je detailně popsán v TS 23.501 (System Architecture) a TS 38.304 (User Equipment procedures in idle and inactive modes). GIN tedy přidává novou dimenzi k výběru sítě, posouvá se od striktního jedno-na-jedno PLMN identity k flexibilnějšímu modelu založenému na skupinách. To je zvláště výhodné pro neveřejné sítě ([NPN](/mobilnisite/slovnik/npn/)) a bezproblémové roamingové dohody, kde je kontinuita služeb a přístup řízený politikami prvořadý.

## K čemu slouží

GIN byl vytvořen, aby řešil omezení tradičního výběru sítě založeného na PLMN ve stále složitějších scénářích nasazení 5G. Před GIN vybíralo UE síť výhradně na základě jejího PLMN ID ([MCC](/mobilnisite/slovnik/mcc/)+[MNC](/mobilnisite/slovnik/mnc/)). To bylo nedostatečné pro moderní případy užití jako: 1) Globální podnik, který má servisní dohody s více lokálními operátory v různých zemích – bez GIN by každý operátor byl samostatný PLMN, vyžadující složité seznamy politik v UE. 2) Roamingová konsorcia, kde členové chtějí uživatelům nabídnout jednotnou "značku sítě". 3) Scénáře síťového krájení (network slicing), kde poskytovatel řezu může být jinou entitou než vlastník infrastrukturního PLMN. GIN poskytuje mechanismus logického seskupení k řešení těchto problémů.

Historicky byl výběr sítě řízen Home PLMN a seznamem Equivalent Home PLMN ([EHPLMN](/mobilnisite/slovnik/ehplmn/)). Šlo o rigidní, plochý seznam. Zavedení GIN v Rel-17, jako součást širších vylepšení pro efektivitu 5G systému a podporu neveřejných sítí, umožňuje hierarchickou nebo na štítcích založenou výběrovou politiku. Umožňuje dynamičtější a na uživatele zaměřené připojení k síti. Pro operátory zjednodušuje správu roamingových dohod a umožňuje nové obchodní modely, kde může být poskytování služeb odděleno od konkrétního MNC. Motivací bylo zlepšit mobilitu, zejména pro vertikální a podnikové uživatele, poskytnutím standardizovaného způsobu identifikace "skupiny sítí", které mají být zacházeno se společnou politikou, čímž se zlepší uživatelský zážitek během automatického výběru sítě.

## Klíčové vlastnosti

- Vysílán jako část systémové informace (např. SIB1) 5G RAN
- Používán UE v procedurách výběru a převýběru buňky spolu s PLMN ID
- Umožňuje politiky výběru sítě založené na skupinové příslušnosti namísto jednotlivého PLMN
- Podporuje roamingová konsorcia a seskupení podnikových sítí
- Definován v architektuře jádra sítě (TS 23.501) a RRC protokolu (TS 38.331)
- Zlepšuje podporu modelů nasazení neveřejných sítí (NPN)

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [GIN na 3GPP Explorer](https://3gpp-explorer.com/glossary/gin/)
