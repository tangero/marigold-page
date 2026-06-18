---
slug: "to"
url: "/mobilnisite/slovnik/to/"
type: "slovnik"
title: "TO – Telecom Operations Map"
date: 2025-01-01
abbr: "TO"
fullName: "Telecom Operations Map"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/to/"
summary: "Rámec a soubor specifikací, které definují standardní procesy, rozhraní a informační modely pro správu telekomunikačních sítí a služeb. Poskytuje plán pro systémy podpory provozu (OSS) pro automatizac"
---

TO je rámec a soubor specifikací definujících standardní procesy, rozhraní a informační modely pro správu telekomunikačních sítí a služeb, který poskytuje plán pro systémy podpory provozu (OSS).

## Popis

Telecom Operations Map ([TOM](/mobilnisite/slovnik/tom/)), později rozšířený na Enhanced Telecom Operations Map (eTOM), je komplexní, procesně orientovaný rámec vyvíjený a spravovaný [TM](/mobilnisite/slovnik/tm/) Forum a přijatý 3GPP pro standardizační reference. Není to softwarový produkt, ale konceptuální model, který popisuje všechny obchodní procesy vyžadované poskytovatelem služeb. Tato mapa kategorizuje tyto procesy do hierarchické struktury, definuje, jak spolu interagují a jaké informace si vyměňují. Jejím hlavním cílem je poskytnout společný jazyk a strukturu pro návrh a implementaci systémů podpory provozu ([OSS](/mobilnisite/slovnik/oss/)) a systémů podpory obchodu ([BSS](/mobilnisite/slovnik/bss/)).

Architektonicky je TOM organizován do vertikálních a horizontálních skupin procesů. Vertikální skupiny, neboli end-to-end procesy, představují klíčové toky, jako je Zřízení (Fulfillment), Zajištění (Assurance) a Fakturace (Billing) (FAB). Ty sahají od interakcí se zákazníkem až po správu síťových zdrojů. Horizontální skupiny představují funkční vrstvy, jako je Správa vztahů se zákazníky (CRM), Správa a provoz služeb a Správa a provoz zdrojů (síťových a [IT](/mobilnisite/slovnik/it/)). Každý proces v mapě je definován svými vstupy, výstupy, spouštěči a interakcemi s jinými procesy. Pro implementaci je rámec doplněn sdílenými informačními modely, jako je Shared Information/Data Model ([SID](/mobilnisite/slovnik/sid/)), který standardizuje datové entity (např. Zákazník, Služba, Zdroj), na kterých procesy operují.

V praxi funguje tak, že telekomunikační operátoři a jejich dodavatelé používají TOM jako plán. Když chce operátor automatizovat nový tok zřizování služby, odkazuje se na TOM, aby identifikoval zapojené standardní procesy – jako je „Zpracování objednávky“, „Konfigurace služby“ a „Aktivace zdroje“. Poté navrhuje svůj OSS software a rozhraní tak, aby odpovídaly těmto definicím procesů a datovým modelům. Toto sladění umožňuje integraci systémů a interoperabilitu mezi OSS komponentami od různých dodavatelů. Jeho role je zásadní pro dosažení automatizovaných, efektivních a škálovatelných operací, což je klíčové pro správu komplexních moderních sítí, jako je 5G, a pro umožnění agilního poskytování služeb.

## K čemu slouží

Telecom Operations Map byl vytvořen, aby řešil kritický problém odvětví – provozní složitost a vysoké náklady spojené se správou telekomunikačních sítí. Před jeho rozšířeným přijetím si každý telekomunikační operátor navrhoval své provozní procesy a podpůrné [IT](/mobilnisite/slovnik/it/) systémy proprietárním, izolovaným způsobem. To vedlo k vážným problémům při integraci systémů od různých dodavatelů, automatizaci end-to-end toků služeb a rychlém uvádění nových služeb. Nedostatek standardizace vedl k dlouhým integračním projektům, vysokým provozním nákladům ([OPEX](/mobilnisite/slovnik/opex/)) a nepružným operacím.

TOM poskytuje standardizovaný, v odvětví dohodnutý rámec, který definuje, „jak“ by měl telekomunikační podnik fungovat. Řeší problém fragmentace procesů tím, že nabízí společný referenční model. To operátorům umožňuje zefektivnit své operace, konzistentně automatizovat procesy a snadněji integrovat prostředí s více dodavateli. Pro dodavatele snižuje potřebu přizpůsobení pro každého operátora, čímž snižuje náklady a urychluje nasazení.

Historicky byl jeho vývoj motivován posunem odvětví směrem ke konkurenci a deregulaci v 90. letech a na počátku 21. století. Operátoři potřebovali být agilnější a nákladově efektivnější. TM Forum, s příspěvky předních globálních operátorů a dodavatelů, vyvinulo TOM, aby tuto potřebu naplnilo. Jeho přijetí do specifikací 3GPP (např. pro architekturu správy) poskytlo formální propojení mezi technickými standardy sítě a obchodními operacemi, což zajišťuje, že rozhraní pro správu sítě mohou podporovat tyto standardizované provozní procesy.

## Klíčové vlastnosti

- Poskytuje standardizovaný, hierarchický rámec obchodních procesů pro poskytovatele telekomunikačních služeb.
- Definuje klíčové end-to-end procesní toky: Zřízení (Fulfillment), Zajištění (Assurance) a Fakturace (Billing) (FAB).
- Rozděluje procesy do funkčních vrstev: Strategie/Infrastruktura/Produkt, Operace a Řízení podniku.
- Umožňuje integraci a interoperabilitu mezi systémy OSS/BSS od různých dodavatelů.
- Slouží jako základ pro rámec Enhanced Telecom Operations Map (eTOM).
- Používá se jako reference pro návrh automatizovaných provozních workflow a systémových rozhraní.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 32.321** (Rel-19) — Test Management IRP: Requirements
- **TS 32.322** (Rel-19) — Test Management IRP Information Service
- **TS 32.326** (Rel-19) — Test Management IRP Solution Set Definitions
- **TS 32.327** (Rel-9) — Test Management IRP SOAP Solution Set
- **TS 36.766** (Rel-15) — LTE BS Interference Cancellation Receiver Study
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TR 38.812** (Rel-16) — Study on NOMA for NR

---

📖 **Anglický originál a plná specifikace:** [TO na 3GPP Explorer](https://3gpp-explorer.com/glossary/to/)
