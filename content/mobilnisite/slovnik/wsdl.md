---
slug: "wsdl"
url: "/mobilnisite/slovnik/wsdl/"
type: "slovnik"
title: "WSDL – Web Services Description Language"
date: 2025-01-01
abbr: "WSDL"
fullName: "Web Services Description Language"
category: "Interface"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/wsdl/"
summary: "WSDL je rozhraním popisný jazyk založený na XML, standardizovaný konsorciem W3C a hojně používaný v 3GPP k definici operací, datových typů a síťových koncových bodů webových služeb. Slouží jako strojo"
---

WSDL je rozhraním popisný jazyk založený na XML, používaný v 3GPP k definici operací, datových typů a koncových bodů webových služeb, který slouží jako strojově čitelná smlouva pro automatické generování klientů a zajištění interoperability.

## Popis

Web Services Description Language (WSDL) je základní technologie v rámci 3GPP pro definici technického rozhraní síťových webových služeb vystavených navenek. Jedná se o [XML](/mobilnisite/slovnik/xml/) schéma, které poskytuje formální, strojově čitelný popis toho, jak lze službu volat, jaké parametry očekává a jaké datové struktury vrací. V architekturách 3GPP se dokumenty WSDL používají k specifikaci severních a jižních aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)) pro četné síťové funkce, zejména v doménách provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)), řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) a provizioningu síťových prvků.

Z architektonického hlediska se dokument WSDL 1.1 (verze převážně odkazovaná v 3GPP) skládá z několika klíčových sekcí. Sekce 'types' definuje složité datové struktury (pomocí XML Schema – [XSD](/mobilnisite/slovnik/xsd/)), které se vyměňují v rámci zpráv. Sekce 'message' definuje abstraktní obsah komunikace, seskupuje části do vstupních a výstupních zpráv. 'portType' (podobný rozhraní v programování) seskupuje související operace, z nichž každá specifikuje vstupní a/nebo výstupní zprávu. Sekce 'binding' konkrétně specifikuje protokol (např. [SOAP](/mobilnisite/slovnik/soap/) přes [HTTP](/mobilnisite/slovnik/http/)) a datový formát (např. document/literal) pro portType. Nakonec sekce 'service' definuje síťovou adresu ([URL](/mobilnisite/slovnik/url/)), na které lze k navázanému rozhraní přistoupit.

V praxi funguje tak, že síťová funkce vystupující jako poskytovatel webové služby (např. Home Subscriber Server – HSS pro provizioning) publikuje svůj WSDL dokument. Klientský systém neboli konzument webové služby (např. systém správy sítě – NMS) tento WSDL získá. Pomocí standardních vývojářských nástrojů může konzument automaticky vygenerovat klientský kód (stub), který přesně ví, jak vytvořit platný SOAP požadavek, na který koncový bod jej odeslat a jak analyzovat SOAP odpověď. Tato automatizace výrazně snižuje úsilí na integraci a chyby. Jeho role v síti 3GPP spočívá v tom, že je základním kamenem návrhu síťových rozhraní orientovaných na služby s primárním důrazem na smlouvu (contract-first), což umožňuje interoperabilitu mezi více dodavateli, dynamické vyhledávání služeb a sladění správy telekomunikačních sítí s běžnými postupy integrace v IT.

## K čemu slouží

WSDL byl přijat 3GPP k vyřešení kritického problému přesné a jednoznačné definice programových rozhraní pro síťové funkce vystavené jako webové služby. Před jeho použitím byly definice rozhraní často předávány prostřednictvím rozsáhlých textových dokumentů (specifikací čitelných člověkem), což vedlo k chybám v interpretaci, nekonzistentním implementacím mezi různými dodavateli a ruční, náchylné k chybám integrační práci. To zvyšovalo náklady, oddalovalo nasazení a vytvářelo křehké sítě s více dodavateli.

Historickým hybatelem byl přechod 3GPP k plně IP sítím a snaha využít široce přijímané IT technologie pro správu sítí (počínaje Release 8 s SAE). Webové služby nabídly standardizovaný komunikační rámec, ale služba je pouze tak interoperabilní, jaká je její definice. WSDL jako standard W3C poskytl chybějící díl: formální, platformně neutrální smlouvu. Jeho vznik byl motivován potřebou jazyka, který může být zpracován stroji za účelem automatizace generování klientského a serverového kódu, což zajišťuje, že obě strany komunikace dodržují stejné datové formáty a procedurální pravidla.

Odstranil tak omezení předchozích přístupů, jako jsou proprietární API nebo protokoly popsané pouze v textové podobě. Použitím WSDL mohlo 3GPP specifikovat rozhraní způsobem, který byl zároveň čitelný člověkem (jako XML) a přímo využitelný vývojářskými sadami (SDK). To umožnilo metodologii 'návrhu podle smlouvy' (design by contract), kde je rozhraní definováno nejprve a implementace se staví tak, aby mu vyhovovaly. To bylo zásadní pro dosažení interoperability typu 'zapoj a používej' (plug-and-play) vyžadované pro moderní, automatizované a virtualizované sítě, což podporuje klíčové iniciativy jako virtualizace síťových funkcí (NFV) a řízení a orchestrace (MANO), kde dynamické skládání služeb závisí na standardizovaných, objevitelných rozhraních.

## Klíčové vlastnosti

- Formát založený na XML pro popis rozhraní webových služeb nezávislý na platformě
- Definuje abstraktní operace (portType) a konkrétní vazby protokolů (např. SOAP/HTTP)
- Používá XML Schema (XSD) v sekci 'types' k definici složitých datových struktur
- Specifikuje umístění síťového koncového bodu (URL) pro přístup ke službě
- Umožňuje automatické generování klientského a serverového kódu (stubů) z definice rozhraní
- Podporuje přístup návrhu s primárním důrazem na smlouvu (contract-first) pro architekturu orientovanou na služby

## Související pojmy

- [SOAP – Simple Object Access Protocol](/mobilnisite/slovnik/soap/)
- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 28.303** (Rel-19) — LSA Controller IRP Solution Set Definitions
- **TS 28.669** (Rel-19) — RPTA IRP Solution Set (SS)
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 32.153** (Rel-19) — IRP Technology-Specific Templates Specification
- **TS 32.306** (Rel-19) — Configuration Management Notification IRP Solution Set
- **TS 32.307** (Rel-9) — Notification IRP SOAP Solution Set
- **TS 32.316** (Rel-19) — Generic IRP Management Solution Set Definitions
- **TS 32.317** (Rel-9) — Generic IRP management SOAP Solution Set
- **TS 32.346** (Rel-19) — File Transfer IRP Solution Set Definitions
- **TS 32.347** (Rel-9) — File Transfer IRP SOAP Solution Set
- … a dalších 16 specifikací

---

📖 **Anglický originál a plná specifikace:** [WSDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/wsdl/)
