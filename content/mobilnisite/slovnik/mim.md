---
slug: "mim"
url: "/mobilnisite/slovnik/mim/"
type: "slovnik"
title: "MIM – Management Information Model"
date: 2025-01-01
abbr: "MIM"
fullName: "Management Information Model"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mim/"
summary: "Standardizovaný datový model definující spravované objekty, jejich atributy, vztahy a chování pro správu síťových prvků a služeb 3GPP. Poskytuje dodavatele neutrální, na technologii nezávislý rámec pr"
---

MIM je standardizovaný datový model definující spravované objekty, atributy a chování pro dodavatele neutrální správu síťových prvků a služeb 3GPP.

## Popis

Management Information Model (MIM, model informací pro správu) je klíčovým prvkem standardizace správy sítí v 3GPP a poskytuje abstraktní, informačně orientovaný pohled na všechny zdroje, které je třeba v systému 3GPP spravovat. Nejde o softwarovou implementaci, ale o konceptuální schéma, které definuje strukturu informací pro správu. MIM specifikuje spravované objekty (Managed Objects, [MO](/mobilnisite/slovnik/mo/)), což jsou reprezentace fyzických zdrojů (jako základnová stanice), logických zdrojů (jako softwarový modul) nebo entit souvisejících se službami (jako profil účastníka). Každý spravovaný objekt je charakterizován sadou atributů obsahujících data (např. provozní stav, administrativní stav, čítače výkonu), oznámení (alarmy, hlášení změny stavu), která může generovat, a operací správy (např. vytvořit, smazat, nastavit), které na něm lze provádět.

Architektura MIM je hierarchická a využívá objektově orientované principy. Jsou definovány třídy spravovaných objektů a konkrétní instance těchto tříd reprezentují skutečné spravované entity v síti. Vztahy mezi objekty, jako je obsahování (buňka je obsažena v základnové stanici) nebo závislost (služba závisí na síťovém řezu), jsou v rámci modelu také formálně definovány. Tento strukturovaný přístup umožňuje systémům správy procházet inventář sítě a chápat závislosti mezi komponentami. MIM je definován pomocí formálního modelovacího jazyka, typicky založeného na směrnicích [ITU-T](/mobilnisite/slovnik/itu-t/) a [ISO](/mobilnisite/slovnik/iso/), což zajišťuje přesnost a umožňuje generování konkrétních implementačních artefaktů.

V provozu slouží MIM jako předloha pro rozhraní mezi síťovými prvky ([NE](/mobilnisite/slovnik/ne/)) a systémy správy, jako jsou správci prvků ([EM](/mobilnisite/slovnik/em/)), systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo systémy provozní podpory ([OSS](/mobilnisite/slovnik/oss/)). Samotná komunikační správa je realizována prostřednictvím protokolů jako [CORBA](/mobilnisite/slovnik/corba/), SNMP nebo nověji NETCONF/YANG, které přenášejí data strukturovaná podle definic MIM. Například systém správy poruch přijímá oznámení (alarmy) definovaná jako atributy konkrétních MO, zatímco systém správy konfigurace manipuluje s hodnotami atributů, aby změnil chování síťových zdrojů. Úlohou MIM je zajistit, aby všechny strany v ekosystému správy – dodavatelé implementující síťové prvky a dodavatelé budující systémy správy – sdíleli společné chápání toho, co je spravováno a jak, což umožňuje interoperabilitu mezi více dodavateli a zjednodušenou integraci.

## K čemu slouží

MIM byl vytvořen, aby vyřešil kritický problém interoperability a složitosti správy telekomunikačních sítí s více dodavateli. V počátcích mobilních sítí každý dodavatel zařízení poskytoval proprietární rozhraní a datové modely pro správu svých síťových prvků. To operátorům velmi ztěžovalo integraci zařízení od různých dodavatelů do jednotného systému provozní podpory (OSS), což vedlo k vysokým provozním nákladům, manuálním procesům a závislosti na dodavateli. Účelem 3GPP MIM je definovat jediný, standardizovaný, na technologii nezávislý informační model, kterého se všichni dodavatelé musí u svých spravovaných produktů držet.

Tato standardizace, která byla vážně zahájena od 3GPP Release 4, byla motivována provozními požadavky rozsáhlých sítí GSM a UMTS a stala se ještě kritičtější se zavedením 3G a pozdějších technologií. Řeší potřebu společného jazyka pro správu sítě, který umožňuje NMS operátora konfigurovat, monitorovat a spravovat poruchy základnové stanice od Dodavatele A pomocí stejného logického modelu a operací jako u základnové stanice od Dodavatele B. Tím, že abstrahuje pohled správy od podkladové implementace, MIM umožňuje automatizaci, zkracuje dobu integrace nových síťových prvků a tvoří základ pro standardizovaná severní rozhraní (NBI) z EMS do NMS. Jeho vytvoření bylo zásadním krokem k dosažení cílů vrstvené architektury Telecom Management Network (TMN) v kontextu 3GPP.

## Klíčové vlastnosti

- Definuje třídy spravovaných objektů reprezentujících fyzické/logické zdroje a služby
- Specifikuje atributy, operace, oznámení a chování pro každý spravovaný objekt
- Formálně modeluje vztahy mezi objekty (obsahování, závislost)
- Poskytuje na technologii nezávislý a dodavatele neutrální rámec pro data správy
- Slouží jako základ pro implementaci standardizovaných rozhraní správy (Itf-N, Itf-S)
- Umožňuje interoperabilitu mezi více dodavateli pro správu poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS)

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 28.632** (Rel-19) — Inventory Management NRM Integration Reference Point
- **TS 28.652** (Rel-19) — UTRAN Network Resource Model (NRM) IRP Information Service
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 28.735** (Rel-19) — STN Interface NRM IRP Information Service
- **TS 32.600** (Rel-19) — 3GPP Configuration Management Specification
- **TS 32.601** (Rel-19) — Basic Configuration Management IRP Requirements
- **TS 32.602** (Rel-19) — Basic Configuration Management IRP Information Service
- **TS 32.611** (Rel-19) — Bulk CM IRP Requirements
- **TS 32.612** (Rel-19) — Bulk Configuration Management IRP: Information Service
- **TS 32.621** (Rel-11) — Generic Network Resources IRP Requirements
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM
- **TS 32.631** (Rel-11) — Core Network Resources IRP Requirements
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [MIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/mim/)
