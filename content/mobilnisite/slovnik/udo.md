---
slug: "udo"
url: "/mobilnisite/slovnik/udo/"
type: "slovnik"
title: "UDO – Unbound Declarative Object"
date: 2025-01-01
abbr: "UDO"
fullName: "Unbound Declarative Object"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/udo/"
summary: "Objektový model definovaný v 3GPP pro reprezentaci a řízení dat deklarativním způsobem, nezávisle na konkrétních síťových funkcích nebo protokolech. Umožňuje flexibilní datové struktury pro služby jak"
---

UDO je objektový model definovaný v 3GPP pro reprezentaci a řízení dat deklarativním způsobem, nezávisle na konkrétních síťových funkcích, umožňující flexibilní datové struktury a standardizovaný výměnu informací mezi systémy.

## Popis

Unbound Declarative Object (UDO) je koncept datového modelování standardizovaný v 3GPP, primárně dokumentovaný v TS 26.953. Poskytuje framework pro definování datových objektů deklarativním způsobem, což znamená, že struktura a sémantika dat jsou popsány nezávisle na způsobu jejich zpracování nebo transportu. Tato abstrakce umožňuje UDO reprezentovat komplexní informace – jako popisy služeb, pravidla politik nebo analytická data – ve konzistentním formátu, který může být interpretován a manipulován různými síťovými funkcemi a externými aplikacemi. Model je navržen jako rozšiřitelný, podporující vnořené struktury a rozsáhlou metadata, což ho činí vhodným pro dynamické prostředí služeb, kde datové schémata mohou evolovat.

Architektonicky se UDO skládá ze souboru atributů a relací definovaných pomocí schéma jazyka, který může být založen na formátech jako [JSON](/mobilnisite/slovnik/json/) Schema nebo [XML](/mobilnisite/slovnik/xml/) Schema. Toto schéma určuje platné vlastnosti, datové typy a omezení objektu. V provozu jsou instance UDO vytvářeny, čteny, aktualizovány a mazány prostřednictvím [API](/mobilnisite/slovnik/api/), často exponovaných síťovými funkcemi jako Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo Application Functions (AFs). Aspekt 'unbound' (neomezený) značí, že tyto objekty nejsou inherentně svázané s konkrétním protokolovým bindingem nebo transportním mechanismem; mohou být serializovány do různých formátů (např. JSON, XML) a přenášeny přes různé interface, což podporuje interoperabilitu.

UDO mají klíčovou roli v moderních architekturách 3GPP, obzvláště v service-based interfaces a pro expozici síťových funkcí. Umožňují třetím stranám aplikací interagovat s síťovými funkcemi pomocí vysoké úrovně, sémanticky bohatých datových modelů namísto low-level protokolových zpráv. Například, ve scénářích edge computing, může UDO popsat kontext aplikace nebo požadavky na kvalitu služby, které síť může interpretovat a podle nich jednat. Standardizací takových objektových modelů 3GPP snižuje komplexnost integrace a akceleruje vývoj nových služeb, protože vývojáři mohou využívat společné datové vocabulary. Specifikace také řeší lifecycle management, zahrnující verzování a validaci, což zajistí robustnost UDO při evoluci síťových funkcí směrem k vyšší automatizaci a openness.

## K čemu slouží

Unbound Declarative Object byl zaveden pro řešení rostoucí potřeby flexibilní a standardizované datové reprezentace v 3GPP síťových funkcích, obzvláště s vzestupem service-based architektur a expozice síťových funkcí. Předchozí přístupy často závisely na rigidních, protokolově specifických datových formátech, které byly pevně svázané s konkrétními interface, což ztěžovalo sdílení informací mezi různými síťovými doménami nebo s externými aplikacemi. Toto omezení brzdilo inovace a zvýšilo náklady integrace nových služeb, protože každá integrace vyžadovala custom mapping a adaptace.

UDO řeší tento problém tím, že poskytuje deklarativní model, který odděluje sémantiku dat od transportních detailů, umožňující více agile a interoperabilní ekosystém. Byly motivované trendy jako network slicing, edge computing a open APIs, kde různorodé stakeholders – od síťových operátorů až po vývojáře aplikací – potřebují common language pro popis zdrojů, politik a požadavků služeb. Adopcí UDO, 3GPP zamýšlí facilitovat automatizované řízení síťových funkcí, podporovat dynamickou tvorbu služeb a zvýšit programovatelnost síťových funkcí 5G a dalších generací. To se shoduje s širšími industry movements směrem k model-driven engineering a intent-based networking, kde high-level deklarace jsou překládány do síťových konfiguraci bez manuální intervence.

## Klíčové vlastnosti

- Deklarativní datové modelování nezávislé na protokolových bindingech
- Podpora rozšiřitelných schémat s vnořenými struktury a metadata
- Serializace do více formátů jako JSON a XML
- Lifecycle management zahrnující verzování a validaci
- Integrace s service-based interfaces pro expozici síťových funkcí
- Umožňuje standardizovanou výměnu dat pro aplikace a síťové funkce

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [API – Application Programming Interface](/mobilnisite/slovnik/api/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [UDO na 3GPP Explorer](https://3gpp-explorer.com/glossary/udo/)
