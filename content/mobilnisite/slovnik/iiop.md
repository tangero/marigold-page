---
slug: "iiop"
url: "/mobilnisite/slovnik/iiop/"
type: "slovnik"
title: "IIOP – Internet Inter-ORB Protocol"
date: 2025-01-01
abbr: "IIOP"
fullName: "Internet Inter-ORB Protocol"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/iiop/"
summary: "IIOP je protokol umožňující komunikaci mezi distribuovanými objekty využívající architekturu Common Object Request Broker Architecture (CORBA) přes sítě TCP/IP. V 3GPP se používá pro určitá rozhraní s"
---

IIOP je protokol umožňující komunikaci mezi distribuovanými objekty využívající CORBA přes sítě TCP/IP, používaný v 3GPP pro určitá rozhraní správy a účtování.

## Popis

Internet Inter-ORB Protocol (IIOP) je klíčový protokol definovaný skupinou Object Management Group ([OMG](/mobilnisite/slovnik/omg/)) pro architekturu Common Object Request Broker Architecture ([CORBA](/mobilnisite/slovnik/corba/)). Ve specifikacích 3GPP je IIOP přijat pro usnadnění standardizované, objektově orientované komunikace pro specifická rozhraní správy a operačních podpůrných systémů ([OSS](/mobilnisite/slovnik/oss/)), zejména v dřívějších vydáních. Funguje nad protokolem [TCP/IP](/mobilnisite/slovnik/tcp-ip/) a poskytuje spolehlivý transportní mechanismus pro zprávy General Inter-ORB Protocol (GIOP) architektury CORBA. To umožňuje softwarovým komponentám neboli objektům umístěným na různých síťových uzlech (potenciálně od různých dodavatelů) transparentně vyvolávat operace na sobě navzájem, jako by byly lokální. Protokol definuje standardizovanou reprezentaci dat ([CDR](/mobilnisite/slovnik/cdr/) - Common Data Representation) a formáty zpráv pro požadavky, odpovědi a další typy zpráv GIOP, čímž zajišťuje syntaktickou interoperabilitu.

V kontextu 3GPP byl IIOP primárně specifikován pro rozhraní související se správou sítě, jako je rozhraní Itf-N definované ve specifikacích řady 32 pro správu výkonu. Jeho použití zahrnuje model klient-server, kde systém správy (klient) může vzdáleně vyvolávat operace na spravovaném síťovém prvku (server) za účelem získání dat o výkonu, konfigurace parametrů nebo přijímání notifikací. Middleware CORBA využívající IIOP řeší všechny podkladové složitosti síťové komunikace, marshallingu/unmarshallingu dat a transparentnosti umístění. Tato architektura odděluje aplikace správy od specifických implementačních detailů spravovaných prostředků.

Zatímco IIOP poskytoval robustní, platformně nezávislý rámec pro distribuované výpočty, jeho složitost a režie vedly 3GPP k přechodu na jednodušší protokoly založené na webových službách (jako [SOAP](/mobilnisite/slovnik/soap/)/[XML](/mobilnisite/slovnik/xml/) a později RESTful [API](/mobilnisite/slovnik/api/)) pro rozhraní správy v pozdějších vydáních. Nicméně ve vydáních, kde byl aplikován, hrál IIOP klíčovou roli v umožnění více-dodavatelské interoperability pro určité funkce OSS. Specifikace protokolu v dokumentech 3GPP odkazuje na základní standardy OMG, čímž zajišťuje soulad s postupy širšího odvětví IT pro distribuované objektové systémy té doby.

## K čemu slouží

IIOP byl začleněn do standardů 3GPP, aby vyřešil problém interoperability dodavatelů v systémech správy sítě a účtování. Před jeho přijetím se často používaly proprietární protokoly, které uzamkly operátory do řešení od jediného dodavatele a ztížily a zdražily integraci více-dodavatelských sítí. Potřeba standardizovaného, otevřeného protokolu pro vzdálené správní operace byla poháněna rostoucí složitostí sítí 3G a požadavkem operátorů na flexibilní, nejlepší síťová nasazení.

Historický kontext spočívá v pozdních 90. a raných 2000. letech, kdy byla CORBA převládajícím průmyslovým standardem pro budování rozsáhlých, distribuovaných podnikových systémů. 3GPP využilo této existující, zralé technologie k řešení specifického požadavku na platformně a jazykově neutrální mechanismus vzdáleného volání procedur (RPC). IIOP poskytl nezbytnou abstrakci, která umožnila aplikacím správy napsaným v různých programovacích jazycích a běžícím na různých operačních systémech bezproblémově komunikovat s různorodými síťovými prvky. Řešil omezení předchozích ad-hoc nebo dodavatelsky specifických správních protokolů tím, že nabídl formální, objektově orientovaný model pro definování správních rozhraní (pomocí CORBA Interface Definition Language - IDL) a spolehlivý, standardizovaný protokol pro přenos.

## Klíčové vlastnosti

- Umožňuje interoperabilitu mezi objekty založenými na CORBA přes sítě TCP/IP
- Poskytuje jazykovou a platformní nezávislost pro distribuované aplikace
- Podporuje transparentní vzdálené vyvolání metod využívající protokol zpráv GIOP
- Používá Common Data Representation (CDR) pro standardizovaný marshalling dat
- Usnadňuje transparentnost umístění pro distribuované objekty správy sítě
- Definován pro specifické referenční body správy a účtování v 3GPP (např. Itf-N)

## Související pojmy

- [CORBA – Common Object Request Broker Architecture](/mobilnisite/slovnik/corba/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [TCP/IP – Transmission Control Protocol / Internet Protocol](/mobilnisite/slovnik/tcp-ip/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework

---

📖 **Anglický originál a plná specifikace:** [IIOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/iiop/)
