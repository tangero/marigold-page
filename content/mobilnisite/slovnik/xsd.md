---
slug: "xsd"
url: "/mobilnisite/slovnik/xsd/"
type: "slovnik"
title: "XSD – XML Schema Definition"
date: 2025-01-01
abbr: "XSD"
fullName: "XML Schema Definition"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/xsd/"
summary: "XSD je standard Konsorcia World Wide Web (W3C) pro definování struktury, obsahu a datových typů XML dokumentů. V 3GPP je hojně využíván k formální specifikaci datových modelů pro rozhraní správy, konf"
---

XSD je standard W3C pro definování struktury a datových typů XML dokumentů, používaný v 3GPP k formální specifikaci datových modelů pro rozhraní správy a protokolové zprávy za účelem zajištění interoperability.

## Popis

[XML](/mobilnisite/slovnik/xml/) Schema Definition (XSD) není protokol vynalezený 3GPP, ale standard [W3C](/mobilnisite/slovnik/w3c/), který 3GPP přijalo pro datové modelování a validaci. Poskytuje výkonný jazyk pro popis povolených stavebních bloků XML dokumentu, včetně elementů a atributů, které se mohou vyskytovat, jejich datových typů (např. řetězec, celé číslo, datum), počtu a pořadí podřízených elementů a výchozích či pevných hodnot. V rámci ekosystému 3GPP jsou soubory XSD klíčové pro definování přesné struktury dat založených na XML, které se vyměňují napříč různými rozhraními, zejména v doménách správy a orchestrace. Například v kontextu severního rozhraní (NBI) systému správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo systému správy prvku ([EMS](/mobilnisite/slovnik/ems/)) definují XSD schémata pro soubory dat správy výkonu ([PM](/mobilnisite/slovnik/pm/)), oznámení správy poruch ([FM](/mobilnisite/slovnik/fm/)) a datové modely správy konfigurace ([CM](/mobilnisite/slovnik/cm/)). Když síťový prvek vygeneruje XML soubor obsahující měření výkonu, musí odpovídat příslušnému XSD schématu. Systémy správy tato XSD používají k validaci příchozích XML dat, čímž zajišťují, že jsou data dobře formátovaná a obsahují očekávané informace ve správném formátu před zpracováním. Tato validace je klíčová pro automatizované systémy, aby mohly data správně analyzovat bez chyb. Dále se XSD v 3GPP používají k definování struktury zpráv [SOAP](/mobilnisite/slovnik/soap/) pro rozhraní založená na webových službách a datových modelů pro architekturu CORBA nebo později pro RESTful API v některých specifikacích. Slouží jako formální kontrakt mezi různými softwarovými komponentami, což umožňuje tvorbu nástrojů pro automatickou generaci kódu, datovou vazbu a dokumentaci.

## K čemu slouží

Zavedení XSD v rámci specifikací 3GPP řeší kritickou potřebu standardizovaných, jednoznačných a strojově čitelných datových definic v síťové správě a poskytování služeb. Před jeho rozšířeným používáním byly datové formáty často popsány v textu standardizačních dokumentů, což vedlo k možnému nesprávnému výkladu a implementačním nejednotnostem mezi zařízeními různých dodavatelů. XSD tento problém řeší tím, že poskytuje přísnou, formální definici, kterou lze přímo zpracovávat softwarem. Jeho účelem je zajistit interoperabilitu v sítích s více dodavateli tím, že garantuje, že všechny strany se shodnou na přesné syntaxi a sémantice vyměňovaných dat. To je zvláště důležité pro automatizované zřizování, správu poruch a reportování výkonu v komplexních sítích 3G/4G/5G. Historický kontext zahrnuje přechod k výměně dat založené na XML pro rozhraní správy (např. ve 3GPP Release 8 a novějších pro správu LTE/EPC), což vyžadovalo robustní schéma jazyk. XSD bylo zvoleno, protože se jednalo o doporučený standard W3C, nabízející silnou typizaci, podporu jmenných prostorů a mechanismy opětovného použití, což byly omezení starších schéma jazyků jako Document Type Definition (DTD). Usnadňuje vývoj kompatibilních systémů, snižuje dobu integrace a zvyšuje spolehlivost toků dat správy.

## Klíčové vlastnosti

- Definuje strukturu, elementy, atributy a datové typy platných XML dokumentů.
- Umožňuje automatickou validaci instančních XML dokumentů vůči schématu pro syntaktickou správnost.
- Podporuje jmenné prostory pro zamezení konfliktů pojmenování v komplexních integrovaných systémech.
- Umožňuje definici komplexních typů rozšiřováním nebo omezováním jiných typů, což podporuje opětovné použití.
- Poskytuje formální, strojově čitelný kontrakt pro výměnu dat mezi síťovými prvky a systémy správy.
- Široce používáno v 3GPP pro specifikaci formátů datových souborů PM, FM a CM a struktur zpráv webových služeb.

## Související pojmy

- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [SOAP – Simple Object Access Protocol](/mobilnisite/slovnik/soap/)
- [CORBA – Common Object Request Broker Architecture](/mobilnisite/slovnik/corba/)

## Definující specifikace

- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.633** (Rel-19) — Inventory Management NRM IRP Solution Set definitions
- **TS 28.659** (Rel-19) — E-UTRAN NRM IRP Solution Set Definitions
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 32.153** (Rel-19) — IRP Technology-Specific Templates Specification
- **TS 32.695** (Rel-9) — Inventory Management XML File Format Definition
- **TS 32.696** (Rel-11) — Inventory Management NRM IRP Solution Set
- **TS 32.765** (Rel-9) — E-UTRAN NRM IRP XML Definitions
- **TS 32.766** (Rel-11) — E-UTRAN NRM IRP Solution Set Definitions

---

📖 **Anglický originál a plná specifikace:** [XSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/xsd/)
