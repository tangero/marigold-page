---
slug: "npdb"
url: "/mobilnisite/slovnik/npdb/"
type: "slovnik"
title: "NPDB – Number Portability Data Base"
date: 2025-01-01
abbr: "NPDB"
fullName: "Number Portability Data Base"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/npdb/"
summary: "Centralizovaný nebo distribuovaný databázový systém, který ukládá a poskytuje směrovací informace pro přenesená telefonní čísla. Umožňuje přenositelnost čísel (NP), což účastníkům umožňuje zachovat si"
---

NPDB je databáze, která ukládá směrovací informace pro přenesená telefonní čísla a umožňuje přenositelnost čísel, takže účastníci si mohou zachovat své číslo při změně poskytovatele služeb.

## Popis

Databáze pro přenositelnost čísel (NPDB) je základní síťový prvek specifikovaný v řadě technických specifikací 3GPP (např. TS 23.066, TS 28.702), který umožňuje služby přenositelnosti čísel (NP). Jejím primárním účelem je uchovávat mapování mezi volaným telefonním číslem účastníka ([MSISDN](/mobilnisite/slovnik/msisdn/)) a aktuálním síťovým operátorem nebo poskytovatelem služeb, který toto číslo obsluhuje. Když je číslo přeneseno z původní dárčí sítě do nové přijímající sítě, toto mapování se v NPDB aktualizuje. Z architektonického hlediska může být NPDB implementována jako jedna národní databáze, distribuovaný systém nebo soubor propojených databází operátorů, v závislosti na regulačním modelu přijatém danou zemí.

Jak to funguje, zahrnuje mechanismus dotazu a odpovědi. Když je uskutečněn hovor na přenesené číslo, řídicí prvek hovoru v síti volajícího (jako [MSC](/mobilnisite/slovnik/msc/) nebo [CSCF](/mobilnisite/slovnik/cscf/)) nemůže určit správnou cílovou síť pouze na základě prefixu čísla. Proto iniciuje dotaz, typicky pomocí signalizačních protokolů jako [MAP](/mobilnisite/slovnik/map/) nebo DIAMETER, k NPDB (nebo k směrovacímu zprostředkovateli, který k ní přistupuje). Dotaz obsahuje volané číslo. NPDB prokonzultuje své záznamy a vrátí odpověď udávající směrovací číslo aktuální obsluhující sítě (např. Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)) nebo specifické směrovací číslo jako Network Routing Number (NRN)). Volající síť pak použije tuto směrovací informaci k nasměrování hovoru na správnou bránu přijímající sítě k dokončení.

Klíčové komponenty systému NPDB zahrnují samotnou databázi, rozhraní pro dotazy (standardizovaná signalizační rozhraní jako Np) a systémy správy pro aktualizaci záznamů (často zahrnující samostatné Administrativní centrum pro přenositelnost čísel neboli NPAC). Její role je klíčová nejen pro hlasové hovory, ale také pro SMS, [MMS](/mobilnisite/slovnik/mms/) a další služby, které závisí na správném směrování čísel. Tím, že odděluje identitu čísla od jeho síťové příslušnosti, funguje NPDB jako centrální nervový systém pro přenositelnost čísel, zajišťuje uživatelům plynulou kontinuitu služeb a umožňuje efektivní mezispolečenské směrování. Musí být vysoce dostupná, zabezpečená a poskytovat odpovědi s nízkou latencí, aby nedocházelo k ovlivnění času navazování hovorů.

## K čemu slouží

Databáze pro přenositelnost čísel (NPDB) byla vytvořena k řešení základní překážky na telekomunikačním trhu: uzamčení zákazníků u konkrétního operátora, protože změna operátora znamenala ztrátu jejich telefonního čísla. Před zavedením přenositelnosti čísel bylo číslo účastníka neoddělitelně spojeno s operátorem, který je přidělil. To potlačovalo konkurenci, protože nepohodlí spojené se změnou čísla bylo pro uživatele významnou překážkou pro přechod k jinému poskytovateli, i když jinde byly dostupné lepší služby nebo ceny. NPDB umožňuje technickou implementaci přenositelnosti čísel, která byla celosvětově hnána regulačními požadavky na podporu volby spotřebitele a konkurence na trhu.

Jejím účelem je poskytnout spolehlivý, standardizovaný mechanismus pro směrování komunikací na číslo, které již není hostováno ve své původní „domovské“ síti. Řeší kritický problém síťového směrování, který nastává, když se změní síťový přípojný bod čísla. Bez NPDB by hovory na přenesené číslo stále směrovaly na dárčí síť, která by je pak musela (často neefektivně) přeposílat, nebo by hovor selhal. NPDB zavádí úroveň zprostředkování, která umožňuje všem sítím přímo zjistit aktuální obsluhující síť.

Historický kontext zahrnuje vývoj od jednoduchého směrování specifického pro operátora ke složitému směrování založenému na dotazech. Raná řešení jako přesměrování hovoru byla neefektivní a nákladná. NPDB, jak ji standardizovaly 3GPP a další orgány, poskytla optimalizované, škálovatelné řešení. Řeší omezení předchozích prostředí bez přenositelnosti vytvořením centralizované autority pro mapování číslo–operátor. Tato technická schopnost byla zásadní pro regulátory, aby mohly prosazovat konkurenční politiky, což činí z NPDB klíčového umožňovatele liberalizovaných telekomunikačních trhů a většího uživatelského komfortu.

## Klíčové vlastnosti

- Ukládá mapování přenesených čísel na aktuální obsluhující síť v reálném čase
- Poskytuje rozhraní dotaz/odpověď využívající standardizovanou signalizaci (např. MAP)
- Podporuje více typů přenositelnosti (mezi operátory, službami, geografická)
- Umožňuje řešení směrování s nízkou latencí pro navazování hovorů
- Integruje se se systémy správy pro zabezpečené aktualizace záznamů
- Navržena pro vysokou dostupnost a škálovatelnost pro zvládnutí národního objemu dotazů

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.140** (Rel-19) — Subscription Management (SuM) requirements
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service

---

📖 **Anglický originál a plná specifikace:** [NPDB na 3GPP Explorer](https://3gpp-explorer.com/glossary/npdb/)
