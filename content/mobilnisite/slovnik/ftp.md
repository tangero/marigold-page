---
slug: "ftp"
url: "/mobilnisite/slovnik/ftp/"
type: "slovnik"
title: "FTP – File Transfer Protocol"
date: 2026-01-01
abbr: "FTP"
fullName: "File Transfer Protocol"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ftp/"
summary: "Standardní síťový protokol používaný v systémech 3GPP pro přenos souborů mezi síťovými prvky, řídicími systémy a uživatelskými zařízeními. Slouží pro softwarové aktualizace, správu konfigurace, získáv"
---

FTP je standardní síťový protokol používaný v systémech 3GPP pro spolehlivý přenos souborů, jako jsou softwarové aktualizace, konfigurace a logy, mezi síťovými prvky, řídicími systémy a uživatelskými zařízeními.

## Popis

V rámci architektury 3GPP se termín File Transfer Protocol (FTP) vztahuje k použití standardního [IETF](/mobilnisite/slovnik/ietf/) FTP (a jeho zabezpečených variant, jako je FTPS) jako spolehlivého mechanismu pro doručování dat pro funkce provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)) i pro některé přenosy dat související se službami. Nejde o protokol vynalezený 3GPP, ale je profilován a povinně používán pro konkrétní případy užití napříč různými síťovými rozhraními. FTP funguje na modelu klient-server a využívá samostatná řídicí (TCP port 21) a datová spojení pro umožnění výpisu, nahrávání a stahování souborů.

Klíčové architektonické aplikace zahrnují přenos souborů s výkonnostními měřeními ([PM](/mobilnisite/slovnik/pm/)) ze síťových prvků ([NE](/mobilnisite/slovnik/ne/)), jako jsou NodeB, eNodeB nebo gNB, do centrálního síťového řídicího systému ([NMS](/mobilnisite/slovnik/nms/)) nebo systému správy prvků ([EMS](/mobilnisite/slovnik/ems/)). Tyto soubory obsahují čítače a měření klíčová pro monitorování a optimalizaci sítě. FTP je také specifikováno pro doručování legálně odposlouchaného ([LI](/mobilnisite/slovnik/li/)) obsahu, kde je odposlouchaný komunikační obsah a informace související s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) zabaleny do souborů a odeslány od zprostředkovací funkce (MF) k monitorovacímu zařízení orgánu činného v trestním řízení (LEMF). Dále je FTP používáno pro správu softwaru, například pro stahování nových softwarových verzí nebo záplat do základnových stanic a prvků jádra sítě.

Protokol funguje tak, že klient naváže řídicí spojení se serverem, provede autentizaci a vydává příkazy (např. LIST, RETR, STOR). Pro přenos dat je navázáno samostatné datové spojení. V kontextech 3GPP je bezpečnost prvořadá; proto je často vyžadováno použití FTP přes TLS (FTPS) nebo v rámci zabezpečených VPN tunelů, zejména pro citlivá data jako LI nebo software. Specifikace podrobně popisují adresářové struktury, konvence pojmenování souborů, požadavky na kompresi a spouštěcí mechanismy (např. na základě plánu nebo události) pro FTP relace, aby byla zajištěna interoperabilita mezi zařízeními různých výrobců.

## K čemu slouží

FTP bylo do standardů 3GPP zavedeno, aby řešilo základní problém automatizovaného, spolehlivého a standardizovaného hromadného přenosu souborů mezi síťovými entitami. S růstem komplexity a automatizace mobilních sítí vznikla kritická potřeba přenášet velké datové soubory – výkonnostní logy, zálohy konfigurací, odposlouchaná data a softwarové image – bez manuálního zásahu. Před standardizací výrobci používali proprietární metody, což bránilo interoperabilitě mezi více výrobci a zvyšovalo provozní náklady operátorů.

Jeho začlenění od Release 99 dál poskytlo dobře známý, široce implementovaný protokol pro tyto OAM datové toky. Vyřešilo omezení ad-hoc přenosových metod tím, že nabídlo funkce jako autentizace, výpis adresářů a možnost obnovení přerušených přenosů. Pro legální odposlech poskytl FTP robustní a auditovatelný mechanismus pro doručování důkazního materiálu. Pro správu výkonu umožnil konsolidaci dat z tisíců síťových prvků do centrálních systémů pro analýzu. Volba FTP byla motivována jeho vyspělostí, jednoduchostí pro automatizované skriptování a schopností spolehlivě zvládnout velké soubory přes někdy nestabilní IP spoje, což vytvořilo páteř mnoha automatizovaných procesů provizioningu, asurance a dodržování předpisů v moderních mobilních sítích.

## Klíčové vlastnosti

- Standardizovaný mechanismus pro hromadný přenos souborů v kontextech OAM a LI
- Podporuje jak push, tak pull modely pro doručování souborů
- Definuje konkrétní adresářové struktury a konvence pojmenování souborů pro interoperabilitu
- Často používán s TLS (FTPS) nebo v zabezpečených tunelech pro ochranu dat
- Umožňuje automatizovaný přenos souborů s výkonnostními měřeními, správou poruch a softwarových souborů
- Poskytuje schopnost obnovení pro pokračování přerušených přenosů

## Definující specifikace

- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.297** (Rel-19) — Charging Data Record File Transfer
- **TS 32.341** (Rel-19) — File Transfer IRP Requirements
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.406** (Rel-19) — Performance Management for CN PS Domain
- **TS 32.411** (Rel-19) — PM IRP Requirements
- **TS 32.583** (Rel-19) — HNB OAM&P Procedure Flows for Type 1 Interface
- **TS 32.593** (Rel-19) — HeNB OAM&P Procedure Flows for Type 1 Interface
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [FTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ftp/)
