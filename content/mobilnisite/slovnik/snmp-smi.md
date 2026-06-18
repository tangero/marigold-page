---
slug: "snmp-smi"
url: "/mobilnisite/slovnik/snmp-smi/"
type: "slovnik"
title: "SNMP/SMI – Simple Network Management Protocol / Structure of Management Information"
date: 2025-01-01
abbr: "SNMP/SMI"
fullName: "Simple Network Management Protocol / Structure of Management Information"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/snmp-smi/"
summary: "Standardizovaný rámec pro správu a monitorování síťových prvků v systémech 3GPP. Definuje protokol (SNMP) pro komunikaci a informační model (SMI) pro strukturování spravovaných dat, což umožňuje centr"
---

SNMP/SMI je standardizovaný rámec pro správu a monitorování síťových prvků 3GPP, který definuje protokol SNMP pro komunikaci a informační model SMI pro strukturování spravovaných dat.

## Popis

[SNMP](/mobilnisite/slovnik/snmp/)/[SMI](/mobilnisite/slovnik/smi/) je komplexní rámec správy přijatý organizací 3GPP pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)) síťových prvků. Vychází ze standardů [IETF](/mobilnisite/slovnik/ietf/) pro SNMP (Simple Network Management Protocol) a přidružený model SMI (Structure of Management Information). Architektura je typu klient-server, kde centrální systém správy sítě ([NMS](/mobilnisite/slovnik/nms/)) funguje jako manažer (klient) a spravované síťové prvky, jako jsou NodeB, eNodeB, gNB nebo funkce core sítě, vystupují jako agenti (servery). Manažer komunikuje s agenty pomocí SNMP zpráv (GET, [SET](/mobilnisite/slovnik/set/), TRAP atd.) přes [UDP](/mobilnisite/slovnik/udp/)/IP za účelem získání nebo změny informací o správě.

Jádrem rámu je báze správy ([MIB](/mobilnisite/slovnik/mib/)), což je virtuální databáze popisující spravované objekty v rámci zařízení. SMI definuje pravidla, jak jsou tyto spravované objekty pojmenovávány, typovány a strukturovány v rámci MIB. Používá podmnožinu Abstract Syntax Notation (ASN.1) k definici typů objektů a využívá hierarchickou stromovou strukturu pro identifikátory objektů (OID). To umožňuje standardizovaný, nezávislý na dodavateli způsob reprezentace parametrů, jako jsou čítače rádiových spojů, stav hardwaru, verze softwaru a stav alarmů.

V kontextu 3GPP specifikace jako 3GPP TS 32.101 definují požadavky a rámec pro použití SNMP/SMI, často specifikují 3GPP-specifické MIB moduly. Manažer periodicky dotazuje agenty za účelem sběru dat o výkonu (PM) a přijímá asynchronní zprávy TRAP nebo INFORM pro správu poruch (alarmy). Tato data jsou klíčová pro monitorování sítě, plánování kapacit a odstraňování závad. Role rámce spočívá v poskytnutí jednotného, interoperabilního rozhraní pro správu prvků, které tvoří základní vrstvu v modelu správy telekomunikačních sítí (TMN) používaném operátory.

## K čemu slouží

SNMP/SMI byl zaveden, aby řešil kritickou potřebu standardizované, interoperabilní správy sítě ve stále složitějších a více dodavatelských sítích 3GPP. Před jeho formálním přijetím byly běžné proprietární rozhraní správy, což vedlo k vysokým nákladům na integraci, provozní neefektivitě a závislosti na dodavateli u síťových operátorů. Rámec řeší problém, jak jednotně monitorovat a řídit různorodé síťové vybavení od různých výrobců.

K jeho vytvoření vedl úspěch SNMP ve světě IP (IETF). 3GPP uznala hodnotu zavedeného, široce používaného protokolu pro správu IP-based transportu a stále více IP-centrických aspektů mobilních sítí. SNMP/SMI poskytuje odlehčený, flexibilní mechanismus pro výměnu dat správy v reálném čase a periodicky, což je nezbytné pro zajištění dostupnosti, výkonu a bezpečnosti sítě. Vytvořil společný jazyk (prostřednictvím MIB) pro popis spravovatelných zdrojů, což je předpoklad pro automatizované systémy OAM.

## Klíčové vlastnosti

- Standardizovaný protokol (SNMPv1, SNMPv2c, SNMPv3) pro komunikaci manažer-agent
- Struktura správy informací (SMI) pro definování syntaxe a sémantiky spravovaných objektů
- Hierarchická báze správy (MIB) s unikátními identifikátory objektů (OID)
- Podpora pro dotazování (GET, GETNEXT) a asynchronní oznámení událostí (TRAP, INFORM)
- Integrace do architektury OAM 3GPP pro správu poruch, konfigurace, účtování, výkonu a bezpečnosti (FCAPS)
- Definice 3GPP-specifických MIB modulů pro správu parametrů rádiové a core sítě

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)

## Definující specifikace

- **TS 32.101** (Rel-19) — Management principles and high-level requirements

---

📖 **Anglický originál a plná specifikace:** [SNMP/SMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/snmp-smi/)
