---
slug: "akma"
url: "/mobilnisite/slovnik/akma/"
type: "slovnik"
title: "AKMA – Authentication and Key Management for Applications"
date: 2026-01-01
abbr: "AKMA"
fullName: "Authentication and Key Management for Applications"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/akma/"
summary: "AKMA je bezpečnostní rámec 3GPP, který umožňuje aplikacím (AF) bezpečně autentizovat uživatelská zařízení (UE) a navázat s nimi klíče bez přímé autentizace. Využívá primární autentizaci 3GPP, což apli"
---

AKMA je bezpečnostní rámec 3GPP, který umožňuje aplikacím bezpečně autentizovat uživatelské zařízení a navázat s ním klíče opakovaným použitím přihlašovacích údajů z primární síťové autentizace.

## Popis

AKMA (Authentication and Key Management for Applications) je standardizovaná bezpečnostní architektura v rámci 3GPP, která poskytuje mechanismus pro aplikace ([AF](/mobilnisite/slovnik/af/)) k bezpečné autentizaci uživatelského zařízení (UE) a vytvoření kryptografických klíčů pro zabezpečení komunikace na aplikační vrstvě. Funguje tak, že opakovaně používá přihlašovací údaje a postupy autentizace z primární autentizace 3GPP (např. 5G-AKA nebo EAP-AKA'), čímž se vyhýbá potřebě samostatných aplikačně specifických autentizačních protokolů. Základní myšlenkou je odvození aplikačně specifických klíčů z dlouhodobého klíčového materiálu vytvořeného během počátečního připojení uživatelského zařízení k síti, což umožňuje efektivní a bezpečný bootstrap pro širokou škálu služeb.

Architektura zahrnuje několik klíčových funkčních entit: funkci AKMA Anchor (AAnF), funkci pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) a aplikační funkci (AF). AAnF, která je typicky umístěna společně s autentizační serverovou funkcí ([AUSF](/mobilnisite/slovnik/ausf/)) v domovské síti, je ústřední komponentou. Generuje a spravuje aplikační klíč AKMA (K_AF) pro konkrétní dvojici uživatelského zařízení a aplikace. K_AF je odvozen z kotvícího klíče (K_AKMA), který je sám odvozen z klíče primární autentizace (např. K_AUSF). NEF funguje jako zabezpečený zprostředkovatel, který umožňuje aplikaci (která může být umístěna v doméně třetí strany) požádat o K_AF od AAnF bez přímého přístupu k funkcím jádra sítě.

Procedura začíná, když uživatelské zařízení úspěšně dokončí primární autentizaci 3GPP. AUSF vygeneruje K_AKMA a poskytne jej AAnF. Uživatelské zařízení může stejný K_AKMA odvodit nezávisle. Když se uživatelské zařízení chce připojit ke službě od aplikace, poskytne jí identifikátor aplikačního klíče AKMA ([A-KID](/mobilnisite/slovnik/a-kid/)). Aplikace prostřednictvím NEF použije tento A-KID k vyžádání odpovídajícího K_AF od AAnF. AAnF vygeneruje K_AF specifický pro danou dvojici uživatelského zařízení a aplikace a poskytne jej aplikaci. Následně mají jak uživatelské zařízení (které může odvodit stejný K_AF), tak aplikace sdílený tajný klíč pro zabezpečení své komunikace, což umožňuje vzájemnou autentizaci a vytvoření dalších bezpečnostních kontextů na aplikační vrstvě (např. TLS-PSK).

Úlohou AKMA je oddělit bezpečnost aplikací od bezpečnosti přístupu k síti a poskytnout škálovatelnou a standardizovanou metodu pro poskytovatele služeb k nabízení zabezpečených služeb. Je zvláště cenná pro služby, které vyžadují trvalé zabezpečené relace nebo časté opakované autentizace, protože se vyhýbá opakovaným úplným síťovým autentizačním procedurám. Tím, že využívá robustní bezpečnost ekosystému 3GPP, AKMA posiluje důvěru v aplikace třetích stran a umožňuje nové obchodní modely pro síťové operátory a poskytovatele aplikací.

## K čemu slouží

AKMA byla vytvořena, aby řešila rostoucí potřebu bezpečné a efektivní autentizace a správy klíčů pro služby na aplikační vrstvě v mobilních sítích. Před AKMA musely aplikace často implementovat vlastní autentizační mechanismy, jako jsou uživatelské jméno/heslo, OAuth nebo vlastní metody založené na certifikátech. Tyto přístupy přinášely několik problémů: vytvářely fragmentované bezpečnostní prostředí, zvyšovaly složitost pro uživatele (více přihlašovacích údajů), způsobovaly významnou signalizační režii (samostatné autentizační běhy) a nevyužívaly inherentně silnou, na účastníka založenou autentizaci již provedenou mobilní sítí.

Historický kontext představuje vývoj směrem k architekturám založeným na službách v 5G a rozmach aplikací pro IoT a edge computing. Tyto služby vyžadují odlehčené, ale zároveň bezpečné metody pro autentizaci zařízení a vytvoření klíčů, aniž by zatěžovaly jádro sítě redundantním autentizačním provozem. AKMA to řeší opakovaným použitím důvěry navázané během počáteční přístupové autentizace 3GPP. Umožňuje aplikacím, ať už je provozuje síťový operátor nebo důvěryhodná třetí strana, bezpečně získat klíče odvozené z této počáteční autentizace, čímž zajišťuje end-to-end bezpečnost založenou na identitě účastníka a bezpečnostních přihlašovacích údajích sítě.

Tento přístup řeší omezení předchozích metod tím, že poskytuje standardizovaný bezpečnostní rámec ukotvený u síťového operátora. Snižuje latenci při přístupu ke službám, minimalizuje signalizační zátěž, zlepšuje uživatelský zážitek prostřednictvím plynulé autentizace (koncept jednotného přihlášení pro síťové služby) a poskytuje konzistentní bezpečnostní základnu napříč různými aplikacemi. Je klíčovým prvkem pro zabezpečené vystavení sítě a monetizaci síťových schopností prostřednictvím [API](/mobilnisite/slovnik/api/).

## Klíčové vlastnosti

- Opakovaně používá přihlašovací údaje z primární autentizace 3GPP pro zabezpečení aplikací
- Odvozuje aplikačně specifické klíče (K_AF) z kotvícího klíče sítě (K_AKMA)
- Využívá centrální funkci AKMA Anchor (AAnF) pro generování a správu klíčů
- Používá funkci pro vystavení sítě (NEF) pro zabezpečené doručení klíčů externím aplikacím
- Podporuje vzájemnou autentizaci mezi uživatelským zařízením a aplikací
- Umožňuje efektivní vytvoření klíčů bez dodatečných úplných autentizačních běhů

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.535** (Rel-19) — 5G AKMA Anchor Services Stage 3 Protocol
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TS 33.533** (Rel-19) — Security for 5G Ranging & Sidelink Positioning
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps
- **TS 33.700** — 3GPP TR 33.700
- **TR 33.739** (Rel-18) — Study on security enhancement of support for
- **TR 33.741** (Rel-18) — Home Network Triggered Authentication
- **TS 33.749** (Rel-19) — Study on security aspects of edge computing enhancement
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [AKMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/akma/)
