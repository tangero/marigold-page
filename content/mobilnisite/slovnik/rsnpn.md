---
slug: "rsnpn"
url: "/mobilnisite/slovnik/rsnpn/"
type: "slovnik"
title: "RSNPN – Registered SNPN"
date: 2025-01-01
abbr: "RSNPN"
fullName: "Registered SNPN"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rsnpn/"
summary: "RSNPN je identifikátor sítě pro samostatnou neveřejnou síť (SNPN), u níž je UE úspěšně registrované. Umožňuje zabezpečený a izolovaný přístup k privátní síti, což je klíčové pro podniková a průmyslová"
---

RSNPN je identifikátor sítě pro samostatnou neveřejnou síť (Standalone Non-Public Network), u které je uživatelské zařízení úspěšně registrované, což umožňuje zabezpečený a izolovaný přístup k privátní síti.

## Popis

RSNPN (Registered [SNPN](/mobilnisite/slovnik/snpn/)) je klíčový identifikátor v architektuře systému 5G pro samostatné neveřejné sítě (SNPN). SNPN je síť nasazená pro soukromé použití (např. podnikem nebo továrnou), která funguje nezávisle na přihlašovacích údajích veřejných síťových operátorů (jako jsou [PLMN](/mobilnisite/slovnik/plmn/)). RSNPN konkrétně označuje danou SNPN, u níž uživatelské zařízení (UE) úspěšně dokončilo procedury registrace a autentizace. Tento registrační proces je definován v dokumentu 3GPP TS 24.501, který specifikuje Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) protokol pro systémy 5G. Po úspěšné registraci si UE a síť vzájemně uznají identitu RSNPN a vytvoří tak zabezpečený kontext pro následnou komunikaci.

Architektura podporující RSNPN zahrnuje funkce jádra sítě jako Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)). Když se UE pokouší o přístup k SNPN, poskytne identifikátor sítě ([NID](/mobilnisite/slovnik/nid/)) kombinovaný s PLMN ID (který má pro SNPN vyhrazenou, standardizovanou hodnotu). AMF ve spolupráci s AUSF autentizuje UE na základě přihlašovacích údajů specifických pro danou privátní síť, jako jsou údaje od operátora SNPN nebo držitele přihlašovacích údajů. Úspěšná autentizace a registrace vedou k vytvoření kontextu RSNPN. Tento kontext se používá pro správu relací, správu mobility a vynucování pravidel v rámci této konkrétní privátní sítě.

Role RSNPN je zásadní pro výběr sítě, řízení přístupu a kontinuitu služeb v privátních nasazeních 5G. Zajišťuje, že UE přistupuje pouze ke službám a prostředkům autorizovaným pro danou konkrétní SNPN. Identifikátor se používá v NAS signalizačních zprávách k udržení registračního stavu a je klíčový při událostech mobility, jako je předávání spojení mezi buňkami patřícími ke stejné SNPN. Umožňuje síti aplikovat specifické síťové řezy, QoS politiky a bezpečnostní nastavení nakonfigurované pro tuto privátní síť. Pro síťové operátory a podniky poskytuje RSNPN jasnou demarkační linii, umožňující koexistenci více izolovaných privátních sítí bez vzájemného ovlivňování, i když sdílejí podkladovou fyzickou infrastrukturu.

## K čemu slouží

RSNPN byl zaveden v 3GPP Release 16, aby reagoval na rostoucí poptávku po soukromých, samostatných sítích 5G. Před příchodem [SNPN](/mobilnisite/slovnik/snpn/) často privátní síťová nasazení spoléhala na řezy veřejných sítí nebo izolované [PLMN](/mobilnisite/slovnik/plmn/), což mohlo znamenat závislost na veřejných mobilních síťových operátorech. Motivací bylo umožnit odvětvím, jako je výroba, logistika nebo energetika, nasadit a provozovat své vlastní sítě 5G zcela nezávisle, s plnou kontrolou nad zabezpečením, výkonem a správou uživatelů. Koncept RSNPN řeší problém jednoznačné identifikace a řízení přístupu pro UE v rámci těchto autonomních sítí.

Řeší omezení dřívějších řešení pro privátní přístup, jako jsou Closed Access Groups (CAG) pro Neveřejné sítě (NPN) nasazené s podporou veřejné sítě, která stále vyžadovala infrastrukturu veřejné sítě. RSNPN umožňuje čistý model privátní sítě, který eliminuje jakoukoli závislost na veřejném PLMN pro funkce jádra sítě. To je zásadní pro případy užití vyžadující maximální izolaci, suverenitu nad daty a přizpůsobené síťové charakteristiky. Vytvoření identifikátoru RSNPN formalizuje stav registrace a zajišťuje, že procedury správy mobility a relací jsou správně ukotveny v kontextu privátní sítě, což umožňuje spolehlivou a zabezpečenou komunikaci pro průmyslové IoT a aplikace s kritickými požadavky.

## Klíčové vlastnosti

- Jednoznačně identifikuje konkrétní SNPN, u níž je UE registrované a autentizované
- Umožňuje striktní řízení přístupu a izolaci pro nasazení privátních sítí
- Používá se v NAS procedurách pro správu registrace a mobility v rámci SNPN
- Podporuje výběr sítě a její opětovný výběr směrem k registrované SNPN
- Umožňuje aplikaci síťových řezů a QoS politik specifických pro danou SNPN
- Umožňuje nezávislý provoz bez nutnosti závislosti na přihlašovacích údajích veřejného síťového operátora

## Související pojmy

- [SNPN – Standalone Non-Public Network](/mobilnisite/slovnik/snpn/)
- [NID – Network Identifier](/mobilnisite/slovnik/nid/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [CAG – Closed Access Group](/mobilnisite/slovnik/cag/)
- [NPN – Non-Public Network](/mobilnisite/slovnik/npn/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification

---

📖 **Anglický originál a plná specifikace:** [RSNPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsnpn/)
