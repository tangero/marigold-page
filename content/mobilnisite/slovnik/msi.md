---
slug: "msi"
url: "/mobilnisite/slovnik/msi/"
type: "slovnik"
title: "MSI – MCH Scheduling Information"
date: 2025-01-01
abbr: "MSI"
fullName: "MCH Scheduling Information"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msi/"
summary: "MSI je řídicí informace používaná v Multimedia Broadcast Multicast Service (MBMS) LTE k plánování dat na Multicast Channel (MCH). Informuje uživatelské zařízení (UE) o přidělení podrámců a modulačním"
---

MSI je řídicí informace v LTE MBMS, která plánuje data na Multicast Channel tím, že informuje uživatelské zařízení o přidělení podrámců a modulačním a kódovacím schématu pro vysílání broadcast/multicast přenosů.

## Popis

[MCH](/mobilnisite/slovnik/mch/) Scheduling Information (MSI) je klíčový řídicí prvek v LTE Radio Access Network (RAN) pro provoz služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Přenáší se jako součást informace [MCCH](/mobilnisite/slovnik/mcch/) (MBMS Control Channel) na MCH (Multicast Channel). MSI poskytuje detailní plánovací mapu pro přidružené přenosy dat na [MTCH](/mobilnisite/slovnik/mtch/) (MBMS Traffic Channel). Konkrétně obsahuje MSI [MAC](/mobilnisite/slovnik/mac/) Control Element, který uvádí podrámce přidělené každé službě MBMS (identifikované pomocí Temporary Mobile Group Identity, TMGI) v rámci konkrétního MCH Scheduling Period ([MSP](/mobilnisite/slovnik/msp/)). To umožňuje UE přesně vědět, kdy má aktivovat svůj přijímač pro dekódování požadovaných dat služby MBMS, aniž by muselo kanál nepřetržitě sledovat, čímž šetří energii baterie.

Architektura MSI je zabudována do vrstvy MAC LTE pro MBMS. eNodeB, který funguje jako MBMS Gateway pro rozhraní rádiového přístupu, určuje plánování pro MTCH na základě požadavků služby a zatížení sítě. Tato plánovací informace je následně zabalena do MSI a periodicky vysílána na MCCH. UE po získání řídicích informací MBMS včetně konfigurace [MBSFN](/mobilnisite/slovnik/mbsfn/) Area a MCCH dekóduje MSI, aby si vytvořilo plán příjmu. Informace zahrnuje stop rámec a stop podrámec pro přenos každé služby, čímž efektivně definuje časové okno pro příjem.

Klíčové součásti mechanismu MSI zahrnují MCH Scheduling Period (MSP), což je konfigurovatelný časový interval (např. 160 ms, 320 ms) definující periodu opakování plánovacího vzoru, a MCH Subframe Allocation Pattern (MSAP), který je odvozen z MSI a udává konkrétní podrámce použité pro MTCH. Úlohou MSI je umožnit dynamické a efektivní sdílení rádiových zdrojů MCH mezi více souběžnými službami MBMS. Bez MSI by UE vyžadovala semi-statické, předem konfigurované plánování nebo by musela provádět pokusy o dekódování naslepo, což by vedlo k neefektivní spotřebě energie a potenciálním selháním při získávání služby. Jeho fungování je zásadní i pro SC-PTM (Single Cell Point To Multipoint), kde podobné plánovací principy platí na bázi jednotlivých buněk.

## K čemu slouží

MSI bylo vytvořeno, aby řešilo konkrétní výzvu efektivního doručování plánovaného broadcast a multicast obsahu v LTE sítích. Před [MBMS](/mobilnisite/slovnik/mbms/) byly mobilní sítě optimalizovány pro unicast (point-to-point) komunikaci. Vysílání obsahu, jako je mobilní TV, by bylo vysoce neefektivní, pokud by bylo považováno za více současných unicast streamů. Architektura MBMS zavedla sdílené kanály (MCH, MTCH), ale byl potřebný mechanismus, který by informoval potenciálně obrovské množství nečinných UE o tom, kdy budou přenášena data jejich požadované služby.

Účelem MSI je vyřešit tento problém oznamování plánování. Umožňuje síti dynamicky přidělovat rádiové zdroje mezi různé služby MBMS a spolehlivě sdělovat toto přidělení všem UE v oblasti MBSFN. To řeší několik klíčových problémů: umožňuje úsporu energie UE prostřednictvím nespojitého příjmu (DRX) pro multicast služby, umožňuje flexibilní a sítí řízené rozdělování zdrojů mezi MBMS a unicast provoz a podporuje multiplexování služeb na jediném rádiovém kanálu. Jeho vytvoření bylo motivováno potřebou učinit broadcast služby ekonomicky životaschopnými na mobilních sítích maximalizací spektrální účinnosti a minimalizací spotřeby energie UE, což je klíčové pro přijetí služeb uživateli, jako je živé video vysílání.

## Klíčové vlastnosti

- Poskytuje dynamické informace o přidělení podrámců pro MTCH v rámci MCH Scheduling Period
- Umožňuje úsporu energie UE prostřednictvím plánovaného příjmu, vyhýbá se nepřetržitému sledování
- Podporuje multiplexování více služeb MBMS (různých TMGI) na jediném MCH
- Přenáší se jako součást řídicích informací MCCH pro spolehlivé získání
- Používá MAC Control Elements pro efektivní kódování a přenos
- Základní pro operace MBMS typu MBSFN (vícebuněčné) i SC-PTM (jednobuněčné)

## Související pojmy

- [MCH – Multast Channel](/mobilnisite/slovnik/mch/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/msi/)
