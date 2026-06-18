---
slug: "sftp"
url: "/mobilnisite/slovnik/sftp/"
type: "slovnik"
title: "SFTP – Secure File Transfer Protocol"
date: 2026-01-01
abbr: "SFTP"
fullName: "Secure File Transfer Protocol"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/sftp/"
summary: "SFTP je standardizovaný protokol používaný v rámci systémů správy 3GPP pro zabezpečený a spolehlivý přenos souborů mezi síťovými prvky a systémy správy. Je klíčový pro aktualizace softwaru, správu kon"
---

SFTP je standardizovaný protokol používaný v rámci systémů správy 3GPP pro zabezpečený a spolehlivý přenos souborů, který je klíčový pro aktualizace softwaru, správu konfigurace a sběr dat.

## Popis

V rámci architektury 3GPP se Secure File Transfer Protocol (SFTP) vztahuje k použití protokolu [SSH](/mobilnisite/slovnik/ssh/) File Transfer Protocol definovaného [IETF](/mobilnisite/slovnik/ietf/) pro účely telekomunikační správy. Je specifikován jako standardní mechanismus přenosu souborů v rámci architektury správy, provozu a údržby ([OAM](/mobilnisite/slovnik/oam/)). SFTP funguje přes zabezpečené SSH (Secure Shell) spojení, typicky využívající TCP port 22, a poskytuje šifrování přenášených dat a silné ověřování. V kontextu 3GPP se používá pro přenosy mezi síťovými prvky ([NE](/mobilnisite/slovnik/ne/)), jako jsou základnové stanice (gNB, [eNB](/mobilnisite/slovnik/enb/)), a systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)) nebo mezi EMS a síťovými systémy správy ([NMS](/mobilnisite/slovnik/nms/)).

Fungování SFTP v nasazení 3GPP zahrnuje model klient-server. Systém správy (např. NMS) často funguje jako klient SFTP, zatímco síťový prvek hostuje server SFTP. Protokol podporuje celou řadu operací se soubory včetně nahrávání, stahování, výpisu adresářů a mazání souborů. Při aktualizaci softwaru se NMS ověří na SFTP serveru gNB pomocí SSH klíčů nebo přihlašovacích údajů, naváže šifrovaný kanál a poté nahraje nový soubor softwarového balíčku. Naopak pro sběr dat o výkonu může gNB generovat logovací soubory, které NMS zabezpečeně stáhne prostřednictvím SFTP. Specifikace (např. TS 32.593 pro 5G) podrobně popisují přesné konvence pojmenování souborů, adresářové struktury a spouštěče přenosů, aby byla zajištěna interoperabilita.

Klíčové komponenty implementace SFTP v 3GPP zahrnují integraci s úložištěm dat správy ([MDR](/mobilnisite/slovnik/mdr/)) na síťovém prvku, kde jsou soubory lokálně uloženy. Úloha přenosu souborů (File Transfer Job) je spravovaný objekt definovaný v modelu síťových zdrojů (NRM), který lze nakonfigurovat pro plánování nebo spouštění přenosů SFTP. Zabezpečení je prvořadé; SSH spojení poskytuje důvěrnost a integritu a specifikace vyžadují podporu konkrétních šifrovacích algoritmů a metod výměny klíčů. Role SFTP spočívá v poskytování robustní, zabezpečené a standardizované alternativy ke starším, méně bezpečným metodám přenosu souborů (jako je FTP), což zajišťuje, že kritická OAM data a software nebudou během přenosu přes často nedůvěryhodné IP transportní sítě ohroženy.

## K čemu slouží

SFTP byl v rámci 3GPP standardizován, aby vyřešil rostoucí potřebu zabezpečeného, spolehlivého a automatizovaného mechanismu přenosu souborů pro správu sítě. Rané mobilní sítě často používaly proprietární protokoly nebo nezabezpečené metody, jako je standardní FTP, pro úlohy jako je nahrávání nového softwaru základnových stanic nebo sběr trasování hovorů. Tyto metody byly náchylné k odposlechu, manipulaci a postrádaly silné ověřování, což představovalo významná bezpečnostní rizika, jak se sítě stávaly více IP-bázovanými a vystavenými širším hrozbám. Zavedení SFTP tyto problémy vyřešilo využitím dobře zavedeného, kryptograficky zabezpečeného protokolu SSH.

Historický kontext zahrnuje posun směrem k automatizované a vzdálené správě v sítích 3G (UMTS) a 4G (LTE), což snížilo potřebu fyzických návštěv lokalit. To vyžadovalo protokol, který by mohl spolehlivě fungovat přes potenciálně přetížené a nezabezpečené sítě široké oblasti. Účelem SFTP je umožnit zabezpečenou vzdálenou správu softwaru (SWM) včetně záplat a upgradů, zabezpečené zálohování a obnovu konfigurace a zabezpečený sběr velkých objemů datových souborů měření výkonu (PM) a správy chyb (FM). Řeší omezení předchozích přístupů tím, že poskytuje jediný, standardizovaný a zabezpečený protokol pro všechny tyto souborové OAM funkce.

Dále motivací pro jeho zařazení do specifikací 3GPP bylo zajistit interoperabilitu mezi více dodavateli. Tím, že je SFTP povinným standardním rozhraním, mohou operátoři používat společný NMS pro správu základnových stanic a prvků jádra sítě od různých dodavatelů. Tím se snižuje provozní složitost a náklady. V éře 5G a síťového řezání se zabezpečený přenos souborů stává ještě kritičtějším pro správu životního cyklu instancí síťových řezů, kde je třeba specifické softwarové image a konfigurační soubory nasazovat a aktualizovat zabezpečeně a efektivně napříč distribuovanými cloudovými infrastrukturami.

## Klíčové vlastnosti

- Používá protokol SSH pro šifrovaná a ověřená spojení
- Podporuje zabezpečené nahrávání a stahování softwarových balíčků, konfiguračních souborů a logovacích dat
- Definuje standardizované adresářové struktury a konvence pojmenování souborů pro správu 3GPP
- Integruje se s úložištěm dat správy 3GPP (MDR) na síťových prvcích
- Umožňuje automatizované a plánované úlohy přenosu souborů jako součást pracovních postupů OAM
- Poskytuje spolehlivý přenos souborů s ošetřením chyb a ověřením integrity

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [SSH – Secure Shell](/mobilnisite/slovnik/ssh/)

## Definující specifikace

- **TS 32.341** (Rel-19) — File Transfer IRP Requirements
- **TS 32.593** (Rel-19) — HeNB OAM&P Procedure Flows for Type 1 Interface
- **TS 32.821** (Rel-9) — SON OAM Architecture for Home NodeB
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [SFTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sftp/)
