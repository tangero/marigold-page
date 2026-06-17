---
slug: "orb"
url: "/mobilnisite/slovnik/orb/"
type: "slovnik"
title: "ORB – Object Request Broker"
date: 2025-01-01
abbr: "ORB"
fullName: "Object Request Broker"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/orb/"
summary: "Komponenta middleware, standardizovaná skupinou Object Management Group (OMG), která usnadňuje komunikaci mezi distribuovanými softwarovými objekty v systému správy sítě. Funguje jako zprostředkovatel"
---

ORB (Object Request Broker) je komponenta middleware, která usnadňuje komunikaci mezi distribuovanými softwarovými objekty tím, že funguje jako zprostředkovatel pro řešení lokalizace objektů, směrování požadavků a marshalingu dat.

## Popis

Object Request Broker (ORB) je klíčový koncept architektury Common Object Request Broker Architecture ([CORBA](/mobilnisite/slovnik/corba/)) od skupiny Object Management Group ([OMG](/mobilnisite/slovnik/omg/)), na který odkazují specifikace 3GPP pro systémy telekomunikačního managementu. V kontextu 3GPP, zejména v architektuře Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)) nebo správy sítě, ORB poskytuje základní komunikační infrastrukturu pro distribuované softwarové komponenty. Tyto komponenty, reprezentující síťové elementy, řídicí funkce nebo databáze, jsou modelovány jako objekty s definovanými rozhraními. ORB umožňuje těmto objektům bezproblémově vyvolávat operace na sobě navzájem napříč různými hardwarovými a softwarovými platformami.

Architektura systému využívajícího ORB je ze své podstaty distribuovaná. Každá spravovaná entita nebo řídicí aplikace implementuje rozhraní definované v Interface Definition Language ([IDL](/mobilnisite/slovnik/idl/)). Runtime ORB je přítomen na každém uzlu, který hostuje tyto objekty. Když objekt (klient) chce vyvolat metodu na jiném objektu (serveru), který se může nacházet na vzdáleném stroji, nekomunikuje přímo. Místo toho zavolá svůj lokální ORB. ORB poté zpracuje celý proces vzdáleného volání. To zahrnuje lokalizaci cílového objektu (často prostřednictvím naming nebo trading služby), marshaling parametrů požadavku do standardizovaného formátu pro přenos, odeslání požadavku přes síť (často pomocí [IIOP](/mobilnisite/slovnik/iiop/) - Internet Inter-ORB Protocol), čekání na odpověď, unmarshaling dat odpovědi a jejich vrácení klientovi.

Fungování ORB je založeno na vzoru brokeru. Odděluje klienta a serverové objekty, což jim umožňuje být vyvíjeny nezávisle a nasazovány na heterogenních systémech. ORB poskytuje transparentnost: transparentnost lokalizace (klient nemusí vědět, kde se server nachází), transparentnost implementace (klient se nestará o programovací jazyk serveru) a transparentnost protokolu. V systémech správy 3GPP, jako jsou ty definované pro Performance Management (PM) nebo Fault Management ([FM](/mobilnisite/slovnik/fm/)) v sérii TS 32.xxx, může být komunikace založená na ORB použita pro interakce mezi agenti a manažery správy nebo mezi různými podsystémy správy. Jejím úkolem je standardizovat a zjednodušit integraci složitých, více-dodavatelských řídicích komponent, čímž zajišťuje interoperabilní a škálovatelné sítě správy.

## K čemu slouží

ORB, jako součást [CORBA](/mobilnisite/slovnik/corba/), byl přijat do standardů telekomunikačního managementu, aby řešil problém interoperability v prostředích distribuované správy sítě s více dodavateli. Rané systémy správy často používaly proprietární protokoly nebo přímá point-to-point spojení, což činilo integraci nákladnou a složitou. Jak sítě rostly a začleňovaly zařízení od různých výrobců, byla nezbytná standardizovaná cesta pro komunikaci softwarových komponent správy. ORB poskytuje tuto standardizovanou vrstvu middleware.

Historický kontext představuje posun k otevřeným, objektově orientovaným řídicím frameworkům na konci 90. let a začátku 21. století. Specifikace správy 3GPP se vyvíjely, aby takové technologie přijaly pro větší flexibilitu. Omezení předchozích přístupů zahrnovala těsné propojení mezi manažery a agenty, nedostatek znovupoužitelnosti a obtížnost přidávání nových řídicích funkcí. CORBA ORB je řeší tím, že poskytuje komunikační sběrnici nezávislou na dodavateli, programovacím jazyku a lokalizaci. Motivoval vytvoření modulárnějších a škálovatelnějších architektur správy, kde mohly být nové řídicí objekty nasazeny a integrovány bez narušení stávajících systémů.

## Klíčové vlastnosti

- Poskytuje transparentnost lokalizace a implementace pro distribuované objekty
- Používá Interface Definition Language (IDL) pro striktní smlouvy rozhraní
- Zpracovává marshaling požadavku, přenos a unmarshaling odpovědi
- Typicky komunikuje pomocí standardizovaného protokolu IIOP
- Integruje se s podpůrnými službami jako Naming Service a Trading Service
- Umožňuje interoperabilitu mezi heterogenními softwarovými a hardwarovými platformami

## Související pojmy

- [CORBA – Common Object Request Broker Architecture](/mobilnisite/slovnik/corba/)

## Definující specifikace

- **TS 32.150** (Rel-19) — IRP Concept and Definitions
- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.375** (Rel-9) — Security Services for IRP: File Integrity
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set

---

📖 **Anglický originál a plná specifikace:** [ORB na 3GPP Explorer](https://3gpp-explorer.com/glossary/orb/)
