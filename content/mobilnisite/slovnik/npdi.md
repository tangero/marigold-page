---
slug: "npdi"
url: "/mobilnisite/slovnik/npdi/"
type: "slovnik"
title: "NPDI – Number Portability Database Dip Indicator"
date: 2025-01-01
abbr: "NPDI"
fullName: "Number Portability Database Dip Indicator"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/npdi/"
summary: "Parametr používaný v signalizaci SIP v subsystému IP multimédií (IMS). Indikuje, zda byl proveden dotaz do databáze přenosu čísel (NPDB) za účelem určení aktuální sítě přeneseného telefonního čísla. T"
---

NPDI je signalizační parametr SIP v IMS, který indikuje, zda bylo provedeno dotazování do databáze přenosu čísel (NPDB) s cílem zjistit aktuální síť přeneseného čísla.

## Popis

Number Portability Database Dip Indicator (NPDI) je signalizační parametr definovaný v protokolu SIP (Session Initiation Protocol) pro použití v sítích IMS standardu 3GPP. Je přenášen v konkrétních polích hlaviček SIP, zejména v hlavičce P-Charging-Vector definované v 3GPP TS 24.229 a dále specifikované v TS 29.163. NPDI není databází, nýbrž příznakem či indikátorem (typicky logické hodnoty), který sděluje výsledek dotazu do databáze. Jeho hodnota signalizuje následujícím uzlům v cestě hovoru, zda byl předchozím uzlem (například [I-CSCF](/mobilnisite/slovnik/i-cscf/) nebo [BGCF](/mobilnisite/slovnik/bgcf/)) proveden dotaz („dip“) do externí databáze přenosu čísel ([NPDB](/mobilnisite/slovnik/npdb/)).

Hlavní architektonická role NPDI spočívá v funkcích směrování hovorů a účtování v IMS. Při uskutečnění hovoru na telefonní číslo musí výchozí síť určit aktuální síť volaného účastníka, zejména pokud bylo číslo přeneseno od původního operátora. Uzel IMS vybavený příslušnou funkcionalitou provede dotaz do NPDB (často prostřednictvím systému [ENUM](/mobilnisite/slovnik/enum/)/[DNS](/mobilnisite/slovnik/dns/) nebo přímého protokolu jako SOAP/XML). Po přijetí odpovědi tento uzel vloží parametr NPDI do SIP požadavku (např. INVITE) a nastaví jeho hodnotu na „ano“ (dotaz byl proveden), případně doplní směrovací číslo (RN) přeneseného čísla.

Jak se SIP požadavek šíří sítí, následné uzly, včetně S-CSCF a účtovacích systémů jako [OCS](/mobilnisite/slovnik/ocs/) nebo [OFCS](/mobilnisite/slovnik/ofcs/), hodnotu NPDI kontrolují. Tato informace je zásadní z několika důvodů. Zaprvé zabraňuje redundantním a nákladným dotazům do NPDB ze strany následných uzlů, čímž optimalizuje dobu navazování hovoru a snižuje signalizační zatížení. Zadruhé poskytuje nezbytná data pro přesné účtování. Informace o tom, že číslo bylo přeneseno, a příslušné směrovací údaje mohou ovlivnit tarif aplikovaný na hovor. NPDI tedy funguje jako klíčová metadata, která v prostředí s povinným přenosem čísel zajišťují efektivní, správné a účtovatelné směrování hovorů mezi více operátory.

## K čemu slouží

NPDI byl zaveden, aby vyřešil provozní a technické výzvy vyplývající z implementace přenosu čísel v plně IP sítích, konkrétně v IMS. Přenos čísel umožňuje účastníkům zachovat si své telefonní číslo při přechodu k jinému poskytovateli služeb, čímž ruší původní vazbu mezi číselnou předvolbou a sítí. V tradiční komutované telefonii to řešily vyhrazené signalizační systémy. S přechodem na IMS a řízení založené na SIP byl potřeba standardizovaný mechanismus pro předávání výsledku kontroly přenosu čísel mezi různými síťovými funkcemi a potenciálně i mezi operátory.

Bez indikátoru jako je NPDI by každý uzel IMS podílející se na směrování hovoru mohl nezávisle dotazovat [NPDB](/mobilnisite/slovnik/npdb/), což by vedlo k neefektivitě signalizace, prodloužení doby navazování hovoru a zbytečné zátěži systémů NPDB. Kritičtější je, že bez standardizovaného způsobu předání informace o přenositelnosti by mohlo docházet k chybám směrování nebo nesprávnému účtování. NPDI poskytuje jednoduché řešení s přenosem informací v rámci signalizace, které tyto problémy odstraňuje. Umožňuje výchozí síti provést dotaz pouze jednou, sdílet výsledek s celou cestou hovoru a zajistit, aby účtovací systémy měly povědomí o stavu přenositelnosti pro přesné fakturační účely, což je základním regulatorním i obchodním požadavkem. Jeho zavedení bylo motivováno potřebou interoperability a efektivity při vývoji základní sítě od TDM k VoIP a IMS.

## Klíčové vlastnosti

- Parametr SIP přenášený v hlavičkách, jako je P-Charging-Vector
- Indikuje, zda byl proveden dotaz do NPDB pro volané číslo
- Zabraňuje redundantním dotazům do databáze v signalizační cestě
- Poskytuje nezbytný vstup pro přesná rozhodnutí o účtování a fakturaci
- Podporuje interoperabilitu mezi různými uzly IMS a operátory
- Umožňuje správné směrování hovorů na přenesená telefonní čísla

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [ENUM – E.164 telephone NUmber Mapping](/mobilnisite/slovnik/enum/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [NPDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/npdi/)
