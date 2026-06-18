---
slug: "ntp-utc"
url: "/mobilnisite/slovnik/ntp-utc/"
type: "slovnik"
title: "NTP-UTC – Network Time Protocol – Coordinated Universal Time"
date: 2026-01-01
abbr: "NTP-UTC"
fullName: "Network Time Protocol – Coordinated Universal Time"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ntp-utc/"
summary: "Bezpečnostní mechanismus definovaný v 3GPP pro zabezpečenou distribuci koordinovaného světového času (UTC) pomocí protokolu NTP (Network Time Protocol). Poskytuje ověřenou a integritu chráněnou synchr"
---

NTP-UTC je bezpečnostní mechanismus 3GPP, který využívá protokol NTP (Network Time Protocol) k zajištění ověřené a integritu chráněné distribuce koordinovaného světového času (UTC) pro zabezpečenou synchronizaci sítě.

## Popis

NTP-UTC je bezpečnostní rámec standardizovaný v 3GPP TS 33.180 pro zabezpečenou distribuci koordinovaného světového času ([UTC](/mobilnisite/slovnik/utc/)) v telekomunikačních sítích. Řeší kritickou potřebu důvěryhodných, přesných a proti neoprávněným zásahům chráněných časových referencí napříč síťovými funkcemi. Architektura zahrnuje funkci distribuce času (Time Distribution Function, [TDF](/mobilnisite/slovnik/tdf/)), která slouží jako zabezpečený časový zdroj a distribuuje čas spotřebitelským entitám, jako jsou systémy pro zákonné odposlechy (Lawful Interception, [LI](/mobilnisite/slovnik/li/)), funkce pro logování bezpečnostních událostí a síťové prvky vyžadující synchronizované časové značky pro forenzní a provozní integritu.

Protokol funguje tak, že TDF získává UTC z důvěryhodného externího zdroje, jako je národní časová služba nebo [GNSS](/mobilnisite/slovnik/gnss/). Tento čas je následně formátován do paketů [NTP](/mobilnisite/slovnik/ntp/). Základní bezpečnostní mechanismus spočívá v digitálním podepisování těchto paketů NTP pomocí soukromého klíče TDF, čímž vzniká token časové značky (Time Stamp Token, TST). Tento token, který obsahuje časovou hodnotu a digitální podpis, je připojen k paketu NTP. Spotřebitelské entity, které disponují odpovídajícím veřejným certifikátem TDF, mohou ověřit podpis k autentizaci časového zdroje a zajistit, že časové informace nebyly během přenosu pozměněny.

Klíčové součásti zahrnují funkci distribuce času (TDF) jako zabezpečený zdroj, token časové značky (TST) jako nástroj pro zajištění integrity a autentizace a infrastrukturu veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) pro správu klíčů. TST je generován podle profilů [RFC](/mobilnisite/slovnik/rfc/) 3161 (Time-Stamp Protocol). Tato zabezpečená distribuce času je klíčová pro korelaci událostí v různých síťových doménách, zajištění právní přijatelnosti logů a udržování synchronizace pro funkce jako LI, kde je přesné načasování odposlechnuté komunikace zákonně vyžadováno. Brání útokům typu man-in-the-middle, při kterých by mohl být čas falšován, což by ohrozilo forenzní analýzu a právní procesy.

## K čemu slouží

NTP-UTC byl zaveden k vyřešení problému nespolehlivé a neověřené časové synchronizace v telekomunikačních sítích, zejména pro právně a provozně kritické funkce. Před jeho standardizací sítě spoléhaly na standardní [NTP](/mobilnisite/slovnik/ntp/) bez inherentní bezpečnosti, což činilo časové značky zranitelnými vůči manipulaci nebo falšování. To představovalo významné riziko pro zákonné odposlechy, kde musí mít důkazy prokazatelnou integritu a přesné načasování pro právní přijatelnost. Nepřesné nebo neověřené časové značky by také mohly bránit korelaci bezpečnostních incidentů a odstraňování závad v síti.

Historický kontext zahrnuje rostoucí regulatorní požadavky na zabezpečené a auditovatelné odposlechové schopnosti po celém světě. Motivací pro NTP-UTC bylo definovat standardizovanou, kryptograficky zabezpečenou metodu distribuce času, kterou mohou všichni síťoví výrobci a operátoři implementovat jednotně. Řeší omezení předchozích přístupů tím, že ukládá povinnost silné autentizace a ochrany integrity časových paketů, což přesahuje rámec best-effort synchronizace běžného NTP. Tím je zajištěno, že všechny síťové prvky, zejména ty zapojené do bezpečnosti a odposlechů, pracují na společné, důvěryhodné časové ose, což je základním předpokladem pro dodržování předpisů, forenzní šetření a koordinované reakce síťové bezpečnosti.

## Klíčové vlastnosti

- Zabezpečená distribuce koordinovaného světového času (UTC) pomocí ověřeného NTP
- Digitální podepisování časových hodnot pomocí tokenů časové značky (TST) podle RFC 3161
- Integrace s infrastrukturou veřejných klíčů (PKI) pro autentizaci zdroje
- Podpora přenosových sítí IPv4 i IPv6
- Návrh specificky pro požadavky zákonných odposlechů (LI) a bezpečnostního logování
- Ochrana proti opakovanému přehrání a útokům typu man-in-the-middle na synchronizaci času

## Definující specifikace

- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service

---

📖 **Anglický originál a plná specifikace:** [NTP-UTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ntp-utc/)
