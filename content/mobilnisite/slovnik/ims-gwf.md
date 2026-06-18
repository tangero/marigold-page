---
slug: "ims-gwf"
url: "/mobilnisite/slovnik/ims-gwf/"
type: "slovnik"
title: "IMS-GWF – IMS Gateway Function"
date: 2025-01-01
abbr: "IMS-GWF"
fullName: "IMS Gateway Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ims-gwf/"
summary: "Funkce fakturační brány v rámci IMS, která shromažďuje fakturační informace z prvků IMS sítě, provádí jejich korelaci a formátování a předává je offline fakturačnímu systému. Jedná se o klíčovou kompo"
---

IMS-GWF je IMS Gateway Function, fakturační brána, která shromažďuje, koreluje a formátuje fakturační informace z prvků IMS pro předání do offline fakturačního systému.

## Popis

IMS Gateway Function (IMS-GWF) je standardizovaná síťová funkce odpovědná za offline účtování v rámci IP Multimedia Subsystem (IMS). Funguje jako prostředník mezi různými IMS Charging Trigger Functions ([CTF](/mobilnisite/slovnik/ctf/)) – jako jsou [P-CSCF](/mobilnisite/slovnik/p-cscf/), [I-CSCF](/mobilnisite/slovnik/i-cscf/), [S-CSCF](/mobilnisite/slovnik/s-cscf/), Application Servers ([AS](/mobilnisite/slovnik/as/)) a Media Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)) – a centrálním fakturačním systémem operátora sítě, známým jako Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)). Primární rolí IMS-GWF je shromažďovat, agregovat, korelovat a formátovat fakturační informace před jejich předáním k dlouhodobému uložení a fakturačnímu zpracování.

Z architektonického hlediska IMS-GWF přijímá fakturační události přes referenční bod Rf, který používá protokol Diameter. Každý prvek IMS sítě fungující jako CTF generuje pro služební relaci zprávy Accounting Request ([ACR](/mobilnisite/slovnik/acr/)) (Start, Interim, Stop). Tyto zprávy obsahují podrobnosti jako identifikátory relace, zúčastněné strany, objemy dat služby a časová razítka. IMS-GWF tyto Diameter ACR zprávy zpracovává. Kritickým úkolem je korelace: spojuje více fakturačních událostí z různých síťových prvků (např. S-CSCF pro signalizaci a AS pro aplikační logiku), které všechny patří do stejné koncové uživatelské relace. K provedení této korelace používá identifikátory jako IMS Charging Identifier (ICID) a Access Network Charging Identifier.

Po korelaci a případném potřebném formátování nebo konsolidaci IMS-GWF předává kompletní fakturační informace CDF přes referenční bod Ga. Rozhraní Ga typicky používá souborový přenosový protokol jako FTP nebo SFTP a data jsou strukturována podle formátu 3GPP Charging Data Record (CDR) definovaného ve specifikaci 32.297. IMS-GWF může také vykonávat funkce jako předzpracování CDR, zpracování chyb a distribuce zátěže. Zajišťuje, aby byla fakturační data z prostředí IMS reálného času spolehlivě převedena na standardizované záznamy vhodné pro offline, dávkově orientované fakturační systémy.

V architektuře IMS účtování IMS-GWF odděluje prvky řízení relací v reálném čase od backendové fakturační infrastruktury. Toto oddělení umožňuje jádru IMS soustředit se na doručování relací, zatímco náročné úkoly sběru a formátování fakturačních dat deleguje na vyhrazenou bránu. IMS-GWF je základní komponentou pro monetizaci služeb IMS, která umožňuje operátorům účtovat za komplexní multimediální relace, které mohou zahrnovat hlas, video, zasílání zpráv a další obohacené komunikační služby, na základě podrobných záznamů o využití.

## K čemu slouží

IMS-GWF byla vytvořena, aby řešila potřebu standardizovaného, škálovatelného a spolehlivého mechanismu offline účtování pro IP Multimedia Subsystem. Před IMS měly sítě s přepojováním okruhů pro hlas dobře definované fakturační mechanismy, ale paketově orientovaná, relacemi založená povaha IMS přinesla nové složitosti. Relace IMS mohly zahrnovat více síťových prvků (různé CSCF, AS), více mediálních komponent a dynamické změny během relace, což ztěžovalo vytvoření jediného, přesného fakturačního záznamu.

Účelem IMS-GWF je vyřešit problém sběru a korelace fakturačních dat v distribuovaném, více-dodavatelském prostředí IMS. Bez centralizované brány by každý síťový prvek musel být přímo propojen s fakturačním systémem, což by vedlo ke složitosti, možné ztrátě dat a nekonzistentnímu formátování záznamů. IMS-GWF poskytuje jediný, logický bod sběru. Abstrahuje heterogenitu jádra IMS od fakturační domény a zajišťuje, že fakturační záznamy jsou kompletní, provázané napříč různými síťovými funkcemi a doručované v jednotném formátu.

Její zavedení bylo motivováno komerčním požadavkem na účtování za služby IMS. Umožňuje operátorům implementovat flexibilní fakturační modely (časově, objemově nebo událostně založené, či jejich kombinace) pro nové multimediální služby. Standardizací rozhraní Rf (sběr) a Ga (doručení) IMS-GWF zajišťuje interoperabilitu mezi zařízeními od různých dodavatelů, což je klíčové pro více-dodavatelský ekosystém nasazení IMS. Tvoří jádrovou část architektury offline účtování 3GPP a umožňuje operátorům efektivně monetizovat jejich investice do IMS.

## Klíčové vlastnosti

- Sběr Diameter Rf Accounting Requests z IMS CTF
- Korelace fakturačních událostí z více prvků IMS sítě
- Generování a formátování standardizovaných Charging Data Records (CDR)
- Předávání CDR do CDF přes rozhraní Ga (souborově založené)
- Zpracování chyb a logování fakturačních dat
- Podpora událostního, relací založeného a objemového účtování

## Definující specifikace

- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- **TS 32.281** (Rel-19) — Announcement Service for Online Charging

---

📖 **Anglický originál a plná specifikace:** [IMS-GWF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ims-gwf/)
