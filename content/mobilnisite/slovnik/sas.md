---
slug: "sas"
url: "/mobilnisite/slovnik/sas/"
type: "slovnik"
title: "SAS – Security Attributes Service"
date: 2025-01-01
abbr: "SAS"
fullName: "Security Attributes Service"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sas/"
summary: "Služba definovaná Object Management Group (OMG) a převzatá 3GPP pro standardizovanou specifikaci a správu bezpečnostních atributů. Poskytuje rámec pro popis bezpečnostních charakteristik systémových k"
---

SAS je služba převzatá 3GPP od OMG pro specifikaci a správu bezpečnostních atributů, které popisují bezpečnostní charakteristiky systémových komponent a umožňují interoperabilitu v zabezpečených distribuovaných systémech.

## Popis

Služba Security Attributes Service (SAS), jak je referencována ve specifikacích 3GPP, není protokolem původem z 3GPP, ale standardem modelu a rozhraní vyvinutým Object Management Group ([OMG](/mobilnisite/slovnik/omg/)) pro distribuované výpočetní prostředí. V kontextu 3GPP je převzata jako metoda pro formální popis a manipulaci s bezpečnostními atributy – metadaty, která definují bezpečnostní vlastnosti, požadavky a schopnosti síťových entit, subjektů (uživatelů) a objektů (dat/zdrojů). Rámec SAS poskytuje strukturovaný způsob definice atributů, jako jsou bezpečnostní štítky, stupně prověření, role, identity a kryptografické schopnosti, nezávislý na konkrétním systému.

Architektonicky je SAS často implementována jako middleware služba v servisně orientované architektuře ([SOA](/mobilnisite/slovnik/soa/)). Definuje rozhraní pro správu životního cyklu bezpečnostních atributů: vytváření, validaci, přiřazení, dotazování a odvolání. V systému 3GPP lze tento konceptuální model aplikovat pro správu bezpečnostních politik síťových funkcí, zejména ve virtualizovaném nebo cloud-nativním prostředí. Například může být použit k přiřazení bezpečnostních štítků instancím virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) nebo k definici bezpečnostního kontextu pro síťový slice. Služba funguje tak, že poskytuje standardizované [API](/mobilnisite/slovnik/api/) (např. založené na [CORBA](/mobilnisite/slovnik/corba/) nebo webových službách), přes které aplikace a síťové funkce mohou získávat a uplatňovat bezpečnostní atributy bez nutnosti znát detaily podkladové bezpečnostní infrastruktury.

Její role v sítích 3GPP, jak je zmíněno např. ve specifikacích jako TS 32.372 (Security Assurance for virtualized resources), spočívá v umožnění konzistentní správy zabezpečení napříč více-dodavatelskými, cloudovými nasazeními. Použitím standardizovaného modelu jako SAS mohou různé systémy řízení (např. [NFV](/mobilnisite/slovnik/nfv/) Orchestrátor, Security Manager) interpretovat a vynucovat bezpečnostní politiky jednotně. Pomáhá při automatizaci kontrol bezpečnostní shody, při zřizování zabezpečených zdrojů a při usnadňování auditních stop. Služba odděluje definici bezpečnostní politiky od jejího vynucení, což umožňuje flexibilnější a přizpůsobivější bezpečnostní architektury schopné vyhovět dynamickým potřebám moderních telekomunikačních sítí.

## K čemu slouží

SAS byla vytvořena [OMG](/mobilnisite/slovnik/omg/) k řešení základního problému v heterogenních distribuovaných systémech: absence společného jazyka a mechanismu pro vyjádření a výměnu bezpečnostních informací. Před existencí takových standardů si každá aplikace nebo podsystém definoval vlastní proprietární formát pro bezpečnostní atributy (jako uživatelské role nebo klasifikace dat), což vedlo k vážným integračním výzvám, nekonzistencím bezpečnostních politik a zvýšené složitosti při vynucování celopodnikových bezpečnostních pravidel.

Převzetí a reference na SAS ze strany 3GPP, zejména od Release 5, bylo motivováno potřebou správy zabezpečení v stále složitějších a otevřenějších síťových architekturách. Jak telekomunikační sítě začaly začleňovat více [IT](/mobilnisite/slovnik/it/) principů, middleware a později cloudové technologie, vyžadovaly robustní, standardizované způsoby manipulace s bezpečnostními metadaty. SAS poskytuje dodavatelsky neutrální model, který usnadňuje interoperabilitu mezi různými bezpečnostními produkty a systémy řízení v rámci domény operátora. To je klíčové pro dosažení automatizace zabezpečení a pro implementaci konceptů jako Security-as-a-Service ve virtualizovaných prostředích.

Tato technologie řeší omezení ad-hoc správy zabezpečení tím, že poskytuje formální, objektově orientovaný model. Umožňuje síťovým návrhářům specifikovat 'co' bezpečnostní atributy jsou, aniž by nařizovali 'jak' mají být uloženy nebo vynucovány, což nabízí implementační flexibilitu. V kontextu práce 3GPP na bezpečnostním zabezpečení a správě virtualizovaných zdrojů nabízí SAS konceptuální rámec pro označování zdrojů bezpečnostními vlastnostmi, což je zásadní pro automatizované vynucování bezpečnostních politik a ověřování shody v dynamických 5G core sítích.

## Klíčové vlastnosti

- Standardizovaný model pro definici bezpečnostních atributů (štítky, role, stupně prověření)
- Poskytuje rozhraní pro správu atributů (vytvořit, číst, aktualizovat, smazat)
- Podporuje interoperabilitu v více-dodavatelských bezpečnostních systémech
- Odděluje definici politiky od mechanismů jejího vynucení
- Aplikovatelný na virtualizované síťové funkce a cloudové zdroje
- Usnadňuje automatizovanou kontrolu shody s bezpečnostními politikami a auditování

## Související pojmy

- [OMG – Object Management Group](/mobilnisite/slovnik/omg/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 32.372** (Rel-19) — Security Service for IRP Information Service
- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set

---

📖 **Anglický originál a plná specifikace:** [SAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sas/)
