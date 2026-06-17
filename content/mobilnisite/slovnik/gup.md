---
slug: "gup"
url: "/mobilnisite/slovnik/gup/"
type: "slovnik"
title: "GUP – Generic User Profile"
date: 2025-01-01
abbr: "GUP"
fullName: "Generic User Profile"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gup/"
summary: "Generic User Profile (GUP) od 3GPP je standardizovaný rámec pro správu uživatelských dat napříč síťovými doménami a aplikacemi. Poskytuje jednotný pohled a přístup k uživatelským informacím, umožňuje"
---

GUP je standardizovaný rámec pro správu uživatelských dat napříč síťovými doménami a aplikacemi, který poskytuje jednotný pohled pro konzistentní personalizaci služeb.

## Popis

Generic User Profile (GUP) od 3GPP je komplexní architektonický rámec definovaný pro standardizovanou správu uživatelských informací v celém systému 3GPP. Jeho hlavním cílem je poskytovat jednotný a konzistentní pohled na uživatelská data různým síťovým entitám, aplikacím a servisním platformám bez ohledu na fyzické umístění dat. Rámec GUP není jedinou databází, ale souborem principů, referenčních bodů a definic dat, které umožňují federaci a harmonizaci uživatelských dat uložených v různých síťových úložištích, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), aplikační servery a profily specifické pro služby.

Architektura GUP je založena na konceptu GUP Serveru, který funguje jako logická entita poskytující jediný přístupový bod pro autorizované klienty (známé jako GUP Clients) k dotazování a správě dat uživatelského profilu. Samotný GUP Server nemusí ukládat všechna data; místo toho komunikuje s různými Datovými repozitáři ([DR](/mobilnisite/slovnik/dr/)), kde jsou skutečná uživatelská data uložena. Tyto repozitáře mohou být specifické pro síť (např. HSS pro základní předplatitelská data) nebo pro službu. Rámec definuje standardizované referenční body (Rp) pro komunikaci mezi GUP Klienty, GUP Serverem a Datovými repozitáři. Klíčové jsou rozhraní Rp mezi GUP Klientem a Serverem a rozhraní Rd mezi GUP Serverem a Datovými repozitáři.

Datový model GUP je strukturován hierarchicky a je definován pomocí XML Schema Definitions (XSD). Organizuje uživatelské informace do komponent a subkomponent, pokrývajících širokou škálu datových typů včetně předplatitelských informací, nastavení služeb, preferencí, možností terminálu a informací o přístupové síti. Tento strukturovaný přístup umožňuje přesný přístup k datům a jejich manipulaci. Rámec také zahrnuje mechanismy pro synchronizaci dat, řízení soukromí a odběr notifikací při změnách dat profilu. Z pohledu síťové operace GUP usnadňuje nasazení konvergovaných služeb tím, že zajišťuje konzistentní a aktuální pohled na uživatele pro různé servisní enginy, což je klíčové pro personalizaci, kontinuitu služeb a efektivní správu vztahů se zákazníky.

## K čemu slouží

GUP byl vytvořen, aby řešil významnou výzvu fragmentace a izolace uživatelských dat v mobilních sítích. Před jeho standardizací byly uživatelské informace rozptýleny v mnoha síťových prvcích a servisních platformách, z nichž každá měla svůj vlastní proprietární datový model a rozhraní pro správu. Například předplatitelská data byla v [HLR](/mobilnisite/slovnik/hlr/)/[HSS](/mobilnisite/slovnik/hss/), preference specifické pro služby byly uloženy v aplikačních serverech (jako jsou servery pro zasílání zpráv nebo presence) a informace o terminálu mohly být spravovány samostatně. Tato fragmentace ztěžovala a prodražovala vytváření integrovaných, personalizovaných služeb, které vyžadovaly holistický pohled na uživatele, a komplikovala operace jako zřizování a aktualizace.

Motivace pro GUP vycházela z pohybu průmyslu směrem ke konvergenci služeb, IP Multimedia Subsystem (IMS) a vize poskytování bezproblémových, personalizovaných uživatelských zkušeností napříč množstvím služeb. Operátoři potřebovali způsob, jak tyto datové izoly prolomit bez nutnosti masivní a okamžité výměny všech stávajících systémů. Rámec GUP poskytl pragmatické řešení definováním standardizované vrstvy pro přístup a správu těchto distribuovaných dat. Umožnil postupnou integraci starších systémů a zároveň poskytl model připravený na budoucnost pro nové služby.

Řešením problému fragmentace dat GUP umožňuje klíčové schopnosti operátorů. Umožňuje centralizovanou správu politik uživatelských dat, zjednodušuje zavádění nových služeb poskytováním standardního [API](/mobilnisite/slovnik/api/) pro přístup k datům a zlepšuje uživatelský zážitek prostřednictvím konzistentní personalizace služeb napříč různými přístupovými sítěmi a zařízeními. Je to základní prvek pro dosažení principu 'napsat jednou, číst kdekoli' pro uživatelská data v ekosystému 3GPP.

## Klíčové vlastnosti

- Standardizovaný rámec pro federovanou správu uživatelských dat napříč síťovými doménami
- Definuje logickou entitu GUP Serveru jako jediný přístupový bod pro autorizované klienty
- Hierarchický datový model založený na XML pro organizaci různorodých komponent uživatelského profilu
- Standardizované referenční body (Rp, Rd) pro interoperabilitu mezi klienty, servery a datovými repozitáři
- Mechanismy pro synchronizaci dat, notifikace o změnách a řízení soukromí
- Umožňuje konzistentní personalizaci služeb a konvergenci poskytováním jednotného pohledu na uživatele

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.240** (Rel-19) — 3GPP Generic User Profile (GUP) Architecture
- **TS 23.241** (Rel-6) — Data Description Method for Generic User Profile
- **TR 23.941** (Rel-6) — 3GPP Generic User Profile Data Description
- **TS 29.240** (Rel-19) — 3GPP Generic User Profile (GUP) Stage 3 Protocol
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [GUP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gup/)
