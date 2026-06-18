---
slug: "iei"
url: "/mobilnisite/slovnik/iei/"
type: "slovnik"
title: "IEI – Information Element Identifier"
date: 2025-01-01
abbr: "IEI"
fullName: "Information Element Identifier"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/iei/"
summary: "Základní pole v protokolových zprávách 3GPP, které jednoznačně identifikuje konkrétní informační element (Information Element, IE) v rámci protokolové datové jednotky. Umožňuje přijímači interpretovat"
---

IEI je pole v protokolových zprávách 3GPP, které jednoznačně identifikuje konkrétní informační element (Information Element) a umožňuje přijímači interpretovat obsah, typ a strukturu následujících dat.

## Popis

Identifikátor informačního elementu (IEI) je klíčovou součástí kódování zpráv protokolových vrstev 3GPP. Jde o pole, typně o délce jednoho nebo dvou oktetů, umístěné na začátku informačního elementu ([IE](/mobilnisite/slovnik/ie/)) v rámci protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)). Informační element je kontejner pro konkrétní část dat, jako je příčinný kód, hodnota časovače, identita nebo složená vnořená struktura. IEI funguje jako jedinečný klíč nebo značka, která přijímající entitě sděluje, jaký typ dat následuje, jak mají být parsována a jaký je jejich významový obsah v kontextu daného protokolu.

Během provozu, když síťová funkce (např. [AMF](/mobilnisite/slovnik/amf/) nebo [MME](/mobilnisite/slovnik/mme/)) vytváří protokolovou zprávu, jako je zpráva [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) nebo [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), sestavuje řadu IE. Každý IE začíná svým IEI. Příjemce, který má k dispozici specifikaci protokolu definující všechny platné IEI a jejich odpovídající datové struktury, přečte IEI a použije jej jako vyhledávací klíč. To přijímači sděluje formát (např. délku obsahu IE, typ hodnoty jako celé číslo nebo řetězec oktetů a zda je element povinný nebo volitelný) a význam následujících bitů. Tento mechanismus umožňuje flexibilní a rozšiřitelný návrh protokolu; nové IE mohou být definovány s novými IEI v pozdějších vydáních protokolu bez narušení zpětné kompatibility, protože starší přijímače mohou jednoduše ignorovat IEI, kterým nerozumějí (pokud je IE definováno jako volitelné).

IEI je definováno pro každý protokol a je závislé na kontextu. Například hodnota IEI 0x57 může představovat IE „[5GMM](/mobilnisite/slovnik/5gmm/) Cause“ v 5G NAS zprávě, ale zcela jiný IE ve zprávě protokolu Diameter. Definice jsou pečlivě katalogizovány ve specifikacích 3GPP. TS 24.008 (pro NAS) a TS 36.331 (pro RRC) jsou příklady specifikací, které definují tabulky IEI. Uvedené specifikace jako 24.244 (3GPP TS 24.244 - Wireless [LAN](/mobilnisite/slovnik/lan/) control protocol) a 31.102 (Characteristics of the USIM application) také definují IEI pro své příslušné protokoly. Systém IEI je základním kamenem pro kódovací pravidla jako Abstract Syntax Notation One (ASN.1) nebo jiná používaná v 3GPP, což umožňuje efektivní binární komunikaci mezi síťovými uzly a UE.

## K čemu slouží

IEI existuje k vyřešení problému, jak strukturovat složité, proměnlivé délky a rozšiřitelné protokolové zprávy efektivním a jednoznačným způsobem. V telekomunikacích musí protokoly přenášet širokou škálu typů informací a musí se v čase vyvíjet, aby podporovaly nové funkce. Bez značkovacího mechanismu, jako je IEI, by protokoly spoléhaly na pevná, pozicovaná pole, která jsou nepružná a ztěžují přidávání nových parametrů bez narušení stávajících implementací. IEI umožňuje strukturu TLV (Type-Length-Value) nebo podobnou, kde „Type“ představuje právě IEI.

Historicky, jak se systémy 3GPP vyvíjely od GSM k 5G, počet parametrů a typů zpráv exponenciálně rostl. Mechanismus IEI, zavedený již na počátku standardizace 3GPP (Release 4 a dříve), poskytl škálovatelné řešení. Řeší omezení rigidních formátů zpráv tím, že umožňuje IE podle potřeby zařazovat nebo vynechávat, objevovat se v libovolném pořadí a zavádět nová IE plynule. To je zásadní pro podporu volitelných funkcí, rozšíření specifických pro dodavatele (v rámci definovaných rozsahů) a pro efektivní kódování, kdy se přenášejí pouze relevantní informace. Motivací je zajistit robustní interoperabilitu mezi zařízeními od různých výrobců a napříč různými generacemi sítě, protože parser protokolu se může zaměřit na IE, které rozpozná, a ostatní bezpečně přeskočit.

## Klíčové vlastnosti

- Jednoznačně identifikuje typ a formát následujícího informačního elementu
- Umožňuje kódování ve stylu TLV (Type-Length-Value) v protokolových zprávách
- Umožňuje rozšiřitelný návrh protokolu prostřednictvím přidávání nových IEI
- Podporuje volitelné a podmíněné zařazování parametrů
- Definice závislé na kontextu pro jednotlivé protokoly (např. NAS, RRC, Diameter)
- Usnadňuje zpětnou a dopřednou kompatibilitu v síťové signalizaci

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications

---

📖 **Anglický originál a plná specifikace:** [IEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/iei/)
