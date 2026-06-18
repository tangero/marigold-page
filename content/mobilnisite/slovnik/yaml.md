---
slug: "yaml"
url: "/mobilnisite/slovnik/yaml/"
type: "slovnik"
title: "YAML – Yet Another Markup Language"
date: 2025-01-01
abbr: "YAML"
fullName: "Yet Another Markup Language"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/yaml/"
summary: "YAML (Yet Another Markup Language) je čitelný datový serializační formát používaný ve specifikacích 3GPP pro konfigurační a řídicí data. Umožňuje strukturované vyjádření síťových parametrů, politik a"
---

YAML je čitelný datový serializační formát používaný ve specifikacích 3GPP pro strukturované vyjádření konfiguračních a řídicích dat za účelem usnadnění automatizace a interoperability.

## Popis

YAML (Yet Another Markup Language) je datový serializační formát přijatý ve specifikacích 3GPP počínaje Release 15 pro vyjádření konfiguračních, řídicích a dat politik ve čitelném textovém formátu. Používá odsazení a jednoduchou syntaxi k definování hierarchických struktur, což inženýrům usnadňuje zápis a porozumění ve srovnání s formáty jako [XML](/mobilnisite/slovnik/xml/) nebo [JSON](/mobilnisite/slovnik/json/). V rámci 3GPP je YAML specifikován v řadě technických dokumentů, včetně TS 26.517, TS 26.857, TS 28.536, TS 29.122 a TS 29.501, kde se používá pro scénáře jako šablony síťových řezů, správu služeb a definice [API](/mobilnisite/slovnik/api/).

Technicky YAML funguje tak, že data reprezentuje jako páry klíč-hodnota, seznamy a vnořená mapování, která mohou být analyzována softwarovými nástroji pro generování nebo interpretaci síťových konfigurací. Například v síťovém řezání 5G mohou soubory YAML definovat charakteristiky řezu, jako je šířka pásma, latence a úrovně izolace, které jsou následně použity řídicími funkcemi k vytvoření řezů. Formát podporuje datové typy jako řetězce, čísla, logické hodnoty a sekvence, což umožňuje efektivní modelování složitých struktur. Často se používá ve spojení s datovými modely YANG, kde YAML slouží jako serializace pro schémata definovaná v YANG, což umožňuje konzistentní výměnu dat mezi síťovými prvky a řídicími systémy.

V architektuře 3GPP se YAML využívá v komponentách správy a orchestrace, jako je Network Slice Selection Function ([NSSF](/mobilnisite/slovnik/nssf/)), Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)). Tyto funkce používají data ve formátu YAML ke komunikaci politik, požadavků služeb a konfiguračních detailů. Například TS 29.122 specifikuje YAML pro Northbound API, což umožňuje externím aplikacím žádat o síťové služby. Čitelnost formátu snižuje chyby při ruční úpravě a podporuje automatizaci prostřednictvím nástrojů jako Ansible nebo Kubernetes, které YAML nativně rozumí pro skripty nasazení.

Úloha YAML v sítích 3GPP spočívá ve zjednodušení řídicích operací, zejména v cloud-nativních prostředích, kde je dynamická konfigurace klíčová. Umožňuje deklarativní konfigurace, kde jsou požadované stavy sítě specifikovány v souborech YAML a automatizované systémy je vynucují. To je zásadní pro škálovatelnost a agilitu 5G, podporující případy užití jako síťové řezy, edge computing a IoT. Standardizací na YAML zajišťuje 3GPP interoperabilitu napříč dodavateli a snižuje složitost integrace, protože je široce podporován v softwarovém průmyslu.

## K čemu slouží

YAML byl zaveden v 3GPP Release 15, aby řešil rostoucí složitost správy sítí v systémech 5G, které vyžadují flexibilní, automatizované konfigurace pro funkce jako síťové řezy a servisně orientovaná architektura. Před jeho přijetím byla řídicí data často vyjádřena ve formátu [XML](/mobilnisite/slovnik/xml/) nebo proprietárních formátech, které mohly být rozvláčné a obtížně čitelné pro člověka, což bránilo rychlému vývoji a odstraňování problémů. Čitelný design YAML tyto procesy zjednodušuje, což inženýrům umožňuje rychle psát a upravovat konfigurace bez rozsáhlého nástrojového vybavení.

Vznik YAML v 3GPP byl motivován potřebou lehkého, interoperabilního formátu, který podporuje automatizaci a postupy DevOps v telekomunikacích. Jak se sítě vyvíjejí směrem k softwarově definovaným a cloud-nativním paradigmatům, tradiční přístupy ke správě se staly nedostatečnými kvůli své rigiditě a pomalým časům zřizování. YAML tyto problémy řeší tím, že poskytuje standardní způsob definování politik a služeb, které lze snadno verzovat, testovat a nasazovat pomocí [CI](/mobilnisite/slovnik/ci/)/CD pipeline. Tím se řeší omezení předchozích přístupů, které spoléhaly na ruční konfigurace CLI nebo složitá schémata XML, která byla náchylná k chybám a méně agilní.

Historicky YAML vznikl ve vývojářské komunitě jako konfigurační jazyk pro aplikace a získal popularitu díky své jednoduchosti. 3GPP rozpoznalo jeho potenciál pro správu sítí, což je v souladu s průmyslovými trendy směrem k infrastruktuře jako kódu. Začleněním YAML umožňuje 3GPP bezproblémovou integraci s cloudovými platformami a orchestračními nástroji, čímž podporuje dynamickou povahu služeb 5G. Usnadňuje správu síťových řezů, politik QoS a expozičních funkcí, což v konečném důsledku snižuje provozní náklady a urychluje nasazení služeb.

## Klíčové vlastnosti

- Čitelná syntaxe využívající odsazení a prostý text
- Podporuje hierarchické datové struktury pro složité konfigurace
- Integruje se s datovými modely YANG pro standardizovaná schémata
- Umožňuje deklarativní správu sítě a automatizaci
- Široce přijat v cloud-nativních nástrojích jako Kubernetes a Ansible
- Specifikován v řadě technických specifikací 3GPP pro konzistenci

## Související pojmy

- [NSSF – Network Slice Selection Function](/mobilnisite/slovnik/nssf/)

## Definující specifikace

- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.501** (Rel-19) — 5GC SBI API Design Principles & Guidelines

---

📖 **Anglický originál a plná specifikace:** [YAML na 3GPP Explorer](https://3gpp-explorer.com/glossary/yaml/)
