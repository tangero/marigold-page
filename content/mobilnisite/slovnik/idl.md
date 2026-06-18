---
slug: "idl"
url: "/mobilnisite/slovnik/idl/"
type: "slovnik"
title: "IDL – Interface Definition Language"
date: 2025-01-01
abbr: "IDL"
fullName: "Interface Definition Language"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/idl/"
summary: "Interface Definition Language (IDL), konkrétně odkazující na OMG (Object Management Group) IDL, je syntaxe nezávislá na programovacím jazyce používaná ve specifikacích 3GPP k formálnímu definování roz"
---

IDL je syntaxe nezávislá na programovacím jazyce používaná ve specifikacích 3GPP k formálnímu definování rozhraní a datových struktur síťových funkcí, což umožňuje jednoznačnou specifikaci API a interoperabilitu.

## Popis

Ve specifikacích 3GPP termín IDL označuje použití jazyka pro definici rozhraní (Interface Definition Language), převážně založeného na standardu definovaném Object Management Group ([OMG](/mobilnisite/slovnik/omg/)), k určení aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)) a datových modelů pro různá síťová rozhraní. IDL poskytuje způsob nezávislý na jazyku pro popis rozhraní, operací, parametrů, datových typů a výjimek. V 3GPP je hojně používán ve specifikacích rozhraní pro provoz a údržbu (O&M), zejména těch založených na architektuře [CORBA](/mobilnisite/slovnik/corba/) (Common Object Request Broker Architecture) v dřívějších vydáních, a později pro definici rozhraní založených na [XML](/mobilnisite/slovnik/xml/) a strukturovaných datových modelů.

Hlavní úlohou IDL v 3GPP je dosažení přesnosti a vyvarování se nejednoznačnosti v definicích rozhraní. Namísto popisu rozhraní pouze textově, který může být interpretován různě, poskytuje IDL formální, strojově čitelnou definici. Například soubor IDL definuje moduly (jmenné prostory), rozhraní (která jsou podobná třídám nebo servisním kontraktům) a v nich operace (metody) s přesnými typy vstupních a výstupních parametrů. Definuje také komplexní strukturované datové typy (struktury, sekvence, pole) a výčtové typy používané v těchto operacích. Tento formální popis slouží jako jediný zdroj pravdy jak pro psaný standard, tak pro automatizovanou generaci softwarových artefaktů.

Z architektonického pohledu použití IDL odděluje specifikaci rozhraní od jeho implementace. Dodavatelé síťových zařízení a vývojáři softwaru mohou vzít standardizované soubory IDL a použít IDL kompilátory ke generování kostry kódu (stubs a skeletons) ve zvoleném programovacím jazyce (např. C++, Java). To zajišťuje, že různé implementace správně dodržují stejné datové formáty a sémantiku vzdálených volání procedur ([RPC](/mobilnisite/slovnik/rpc/)), což je klíčové pro interoperabilitu v telekomunikačních sítích s více dodavateli. V 3GPP je na IDL často odkazováno ve specifikacích řady 32 (Telekomunikační management), jako jsou ty definující referenční bod Itf-N mezi Network Managerem ([NM](/mobilnisite/slovnik/nm/)) a Element Managerem ([EM](/mobilnisite/slovnik/em/)) nebo řídicí rozhraní pro síťové funkce.

Zatímco CORBA IDL převládal v řídicích rozhraních 3G a raného 4G, principy IDL se přenesly dál. Moderní řídicí rozhraní 3GPP, jako jsou ta pro servisně orientovanou architekturu ([SBA](/mobilnisite/slovnik/sba/)) 5G jádra sítě, často používají jazyk OpenAPI Specification (OAS) nebo YANG pro datové modelování, které slouží podobnému účelu – formálnímu definování RESTful API nebo konfiguračních datových modelů strojově čitelným způsobem. Základní koncept zůstává: formální, abstraktní jazyk pro definování kontraktů mezi komponentami systému, umožňující vývoj, validaci a testování podporované nástroji.

## K čemu slouží

Zavedení jazyka pro definici rozhraní (IDL) v rámci 3GPP bylo motivováno kritickou potřebou interoperability v komplexních telekomunikačních sítích s více dodavateli. V počátcích 3G byla řídicí síťová rozhraní často popisována neformálně, což vedlo k různým interpretacím výrobců zařízení. To mělo za následek nákladné integrační projekty, proprietární rozšíření a křehké systémy. Formální IDL poskytuje jednoznačný kontrakt, který snižuje čas integrace a chyby.

Historicky byla volba OMG IDL úzce spojena s přijetím CORBA jako middleware pro distribuované objekty pro řídicí rozhraní. CORBA poskytovala framework pro vzdálené operace nezávislý na platformě a jazyku a její doprovodný IDL byl přirozenou volbou pro definování objektových rozhraní. To umožnilo, aby Network Manager od jednoho dodavatele komunikoval s Element Managerem nebo síťovou funkcí od jiného dodavatele pomocí standardizovaného objektově orientovaného paradigmatu. Definice IDL pokrývaly vše od rozhraní pro správu chyb a výkonu až po rozhraní pro správu konfigurace.

Problém, který IDL řeší, je v podstatě problém jasnosti specifikace a automatizace. Ruční psaní a údržba kódu, který odpovídá textové specifikaci, je náchylné k chybám. IDL umožňuje automatické generování konzistentních vazeb kódu pro klienta a server, rutin pro marshalling/unmarshalling dat a dokumentace. To přesouvá důraz z implementačních detailů na samotný návrh rozhraní. Jak se architektury 3GPP vyvíjely směrem k webovým protokolům (HTTP/2, REST), konkrétní syntaxe se posunula od OMG IDL k YANG a OpenAPI, ale základní účel – poskytnutí formální, strojově zpracovatelné definice rozhraní – zůstává klíčovým kamenem pro dosažení spolehlivého, škálovatelného a interoperabilního síťového softwaru.

## Klíčové vlastnosti

- Syntaxe nezávislá na jazyku pro definování API, datových typů a operací
- Umožňuje jednoznačnou specifikaci řídicích a interních rozhraní 3GPP
- Usnadňuje automatizovanou generaci kostry kódu pro klienta/server (stubs/skeletons)
- Podporuje komplexní datové struktury (struktury, sekvence, unie, výčty)
- Integrální součást rozhraní O&M založených na CORBA v legacy systémech 3GPP
- Slouží jako formální základ pro interoperabilitu mezi více dodavateli

## Související pojmy

- [CORBA – Common Object Request Broker Architecture](/mobilnisite/slovnik/corba/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 26.347** (Rel-19) — MBMS Transport Protocol and API (TRAPI)
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.626** (Rel-19) — State Management Data Definition IRP Solution Set
- **TS 28.629** (Rel-19) — SON Policy NRM IRP Solution Set Definitions
- **TS 28.653** (Rel-19) — UTRAN NRM IRP Solution Set Definition
- **TS 28.656** (Rel-19) — GERAN NRM IRP Solution Set Definitions
- **TS 28.659** (Rel-19) — E-UTRAN NRM IRP Solution Set Definitions
- **TS 28.663** (Rel-19) — Generic RAN NRM IRP Solution Set Definitions
- **TS 28.673** (Rel-19) — HNS NRM IRP Solution Set Definitions
- **TS 28.676** (Rel-19) — HeNS NRM IRP Solution Set Definitions
- … a dalších 68 specifikací

---

📖 **Anglický originál a plná specifikace:** [IDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/idl/)
