---
slug: "raf"
url: "/mobilnisite/slovnik/raf/"
type: "slovnik"
title: "RAF – Repository Access Function"
date: 2025-01-01
abbr: "RAF"
fullName: "Repository Access Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/raf/"
summary: "Funkce správy v architektuře správy sítí dle 3GPP. Poskytuje standardizovaný přístup k úložišti informací o správě, jako jsou konfigurační data sítě, výkonnostní měření a záznamy o poruchách, což umož"
---

RAF je funkce správy dle 3GPP, která poskytuje standardizovaný přístup k úložišti (repository) informací o správě sítě. Umožňuje centralizované ukládání a vyhledávání konfiguračních, výkonnostních a poruchových dat pro síťové operace.

## Popis

Repository Access Function (RAF) je komponenta v rámci architektury Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)) a později Network Management ([NM](/mobilnisite/slovnik/nm/)) dle 3GPP, definovaná v souvisejících specifikacích Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)). Funguje jako standardizované rozhraní a funkční blok, který poskytuje přístup k úložišti nebo databázi obsahující informace související se správou sítě. Tyto informace mohou zahrnovat Network Resource Models ([NRM](/mobilnisite/slovnik/nrm/)), výkonnostní měření ([PM](/mobilnisite/slovnik/pm/)), záznamy správy poruch ([FM](/mobilnisite/slovnik/fm/)), data konfigurační správy ([CM](/mobilnisite/slovnik/cm/)) a další provozní data nezbytná pro administraci sítě. RAF v podstatě abstrahuje podkladové úložiště dat a nabízí konzistentní způsob přístupu pro další funkce správy, jako jsou systémy Network Management (NM), Domain Management ([DM](/mobilnisite/slovnik/dm/)) nebo Element Management (EM).

Architektonicky je RAF často umístěna jako součást Management Data Repository (MDR) nebo jako integrovaná funkce v rámci Operations Support System (OSS). Funguje tak, že vystavuje northbound rozhraní, typicky založená na protokolech jako CORBA, SNMP, nebo v novější době RESTful API dle specifikací 3GPP (např. pro Network Resource Model - NRM). Mezi klíčové komponenty patří definice rozhraní (Irp), datové modely (Information Service - IS) a samotné backendové úložiště. Když systém správy potřebuje získat historická výkonnostní data nebo konkrétní snapshot konfigurace, odešle požadavek na RAF. RAF následně dotazuje své úložiště, aplikuje případné filtrování nebo agregaci a vrátí výsledky ve standardizovaném formátu.

Její role je klíčová pro automatizaci sítě, její zajištění (assurance) a analytiku. Centralizací přístupu k datům správy RAF zabraňuje vytváření izolovaných úložišť dat napříč různými síťovými elementy nebo doménami správy. Podporuje funkce jako analýza výkonnostních trendů, analýza hlavní příčiny poruch, auditní stopy změn konfigurace a reportování shody. Specifikace jako TS 32.808 detailně popisují požadavky a řešení pro RAF, zajišťujíce interoperabilitu různých dodavatelských systémů správy se sdíleným úložištěm a usnadňujíce správu sítí s více dodavateli.

## K čemu slouží

RAF byla vytvořena, aby řešila rostoucí komplexitu správy celulárních sítí s více dodavateli a technologiemi. Raná správa sítí často zahrnovala proprietární manažery elementů přímo přistupující k síťovým prvkům, což vedlo k izolovaným úložištím dat, nekonzistentním rozhraním a obtížím při provádění mezidoménových analýz. RAF jako součást standardizované architektury správy dle 3GPP poskytuje jednotný přístupový bod ke konsolidovaným datům správy.

Toto řeší několik klíčových problémů: odděluje úložiště dat od konzumentů dat (umožňuje různým OSS aplikacím používat stejná data), standardizuje způsob získávání informací o správě (zlepšuje interoperabilitu) a umožňuje efektivní sdílení dat pro komplexní operace jako zajištění služeb (service assurance) a plánování kapacity. Historicky byl její vývoj motivován potřebou automatizovanějších a efektivnějších OSS systémů, jak se sítě vyvíjely od 2G/3G k 4G a 5G, kde objem a rozmanitost dat správy exponenciálně narostly. RAF poskytuje základní datovou vrstvu pro moderní, daty řízené síťové operace.

## Klíčové vlastnosti

- Poskytuje standardizovaný přístup k úložišti dat správy (MDR)
- Ukládá a vyhledává data Network Resource Model (NRM), Performance Measurement (PM) a Fault Management (FM)
- Definuje northbound rozhraní (např. CORBA, RESTful) pro integraci s OSS
- Podporuje filtrování, agregaci a historické dotazování dat
- Umožňuje centralizované ukládání dat pro správu sítí s více dodavateli
- Usnadňuje automatizaci sítě a analytiku tím, že slouží jako konzistentní zdroj dat

## Související pojmy

- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 23.240** (Rel-19) — 3GPP Generic User Profile (GUP) Architecture
- **TS 29.240** (Rel-19) — 3GPP Generic User Profile (GUP) Stage 3 Protocol
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [RAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/raf/)
