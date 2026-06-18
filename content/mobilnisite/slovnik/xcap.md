---
slug: "xcap"
url: "/mobilnisite/slovnik/xcap/"
type: "slovnik"
title: "XCAP – XML Configuration Access Protocol"
date: 2025-01-01
abbr: "XCAP"
fullName: "XML Configuration Access Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/xcap/"
summary: "Protokol založený na HTTP, definovaný IETF a přijatý 3GPP, který klientovi umožňuje číst, zapisovat a upravovat konfigurační data aplikací uložená na serveru ve formátu XML. Je klíčový pro správu nast"
---

XCAP je protokol založený na HTTP, který klientovi umožňuje číst, zapisovat a upravovat konfigurační XML data na serveru. Používá se v sítích 3GPP IMS pro správu nastavení služeb účastníka, jako jsou pravidla přesměrování hovorů.

## Popis

[XML](/mobilnisite/slovnik/xml/) Configuration Access Protocol (XCAP) je protokol typu klient-server, který klientovi umožňuje manipulovat s aplikačně specifickými konfiguračními daty uloženými na serveru ve formě XML dokumentů. V ekosystému 3GPP se XCAP primárně používá v rámci IP Multimedia Subsystem (IMS) jako standardní mechanismus pro správu uživatelských nastavení služeb. Protokol je postaven nad [HTTP](/mobilnisite/slovnik/http/)/1.1 a využívá standardní metody HTTP (GET, PUT, DELETE) k provádění operací nad uzly XML dokumentů, které jsou identifikovány hierarchickou [URI](/mobilnisite/slovnik/uri/) strukturou. Tento návrh jej činí přirozeně webovým a snadno integrovatelným s existující internetovou infrastrukturou.

XCAP server hostuje jednu nebo více „XCAP Application Usages“ (aplikačních použití). Každé použití definuje konkrétní XML schéma (datový model) a soubor konvencí pro strukturu, pojmenování a přístup k XML dokumentům. Například použití `org.openmobilealliance.pres-rules` definuje XML schéma pro autorizační pravidla přítomnosti (tzv. „ruleset document“). Klient, například UE nebo webový portál, může tento dokument získat pomocí HTTP GET požadavku na specifickou URI, upravit obsah XML lokálně a následně nahrát změny zpět na server pomocí HTTP PUT. Server před potvrzením změn ověří jejich platnost proti XML schématu a sémantice aplikačního použití.

Síla protokolu spočívá v jeho schopnosti cílit na konkrétní prvky nebo atributy v rámci XML dokumentu pomocí XPath výrazů vložených do HTTP URI. To umožňuje jemnozrnné úpravy bez nutnosti přenášet a parsovat celý dokument při každé změně. Například uživatel může upravit jediné pravidlo pro přesměrování hovoru bez ovlivnění zbytku své konfigurace zpracování hovorů. V sítích IMS je XCAP server často umístěn společně nebo integrován do Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo do vyhrazeného serveru pro konfiguraci služeb. Klient k němu přistupuje přes referenční bod Ut. Autentizace je typicky řešena pomocí IMS Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), což zajišťuje, že uživatelé mohou upravovat pouze svá vlastní data. Server také řeší řízení souběžnosti pomocí HTTP entity tags (ETags), aby zabránil konfliktním aktualizacím od různých klientů.

## K čemu slouží

XCAP byl vyvinut k řešení problému standardizované vzdálené správy uživatelsky specifických servisních dat v telekomunikačních službách nové generace, zejména těch založených na [SIP](/mobilnisite/slovnik/sip/) a IMS. Před XCAP byla konfigurace služeb často řešena proprietárními protokoly, systémy interaktivní hlasové odpovědi ([IVR](/mobilnisite/slovnik/ivr/)) nebo operátorskými webovými portály bez jednotného datového modelu. Tato roztříštěnost ztěžovala vytváření interoperabilních koncových zařízení a aplikací pro správu služeb od třetích stran. Hnací silou jeho přijetí v 3GPP byla potřeba flexibilního, rozšiřitelného a na internetových standardech založeného způsobu, jakým mohou účastníci spravovat komplexní IMS služby jako Přítomnost (Presence), Message Waiting Indication nebo Call Barring.

Protokol řeší omezení samotného SIP, což je signalizační protokol, který není navržen pro manipulaci s perzistentními konfiguračními daty. XCAP poskytuje chybějící článek: standardizované úložiště dat a rozhraní pro manipulaci. Umožňuje uživatelům konfigurovat služby z jakéhokoli zařízení s XCAP klientem, což poskytuje konzistentní zkušenost napříč mobilními telefony, [PC](/mobilnisite/slovnik/pc/) a webovými prohlížeči. Volba XML a HTTP byla strategická, aby se využila široce známá technologie, což snižuje implementační složitost a podporuje bohatý ekosystém nástrojů a vývojářů. Oddělením servisní logiky (v SIP Application Servers) od dat konfigurace služeb (v XCAP serveru) vytvořil čistou architekturu, která zjednodušila správu sítě a umožnila posílení role uživatele prostřednictvím samoobslužných portálů, jež se staly standardní součástí IMS nasazení.

## Klíčové vlastnosti

- Používá standardní metody HTTP (GET, PUT, DELETE) pro operace CRUD nad XML daty
- Podporuje jemnozrnnou manipulaci s XML elementy a atributy prostřednictvím XPath v URI
- Definuje „Application Usages“ (aplikační použití) pro specifikaci XML schémat a sémantiky pro různé služby
- Poskytuje vestavěné řízení souběžnosti prostřednictvím mechanismu HTTP ETag
- Využívá validaci XML pro zajištění integrity konfiguračních dat
- Umožňuje autentizaci uživatele pomocí IMS AKA přes referenční bod Ut

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)
- [HTTP – Hypertext Transfer Protocol](/mobilnisite/slovnik/http/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.337** (Rel-19) — IMS Inter-UE Transfer Protocol Specification
- **TS 24.423** (Rel-8) — PSTN/ISDN Simulation Services XCAP Protocol
- **TS 24.424** (Rel-19) — XCAP over Ut for Supplementary Services MO
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [XCAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/xcap/)
