---
slug: "mdas"
url: "/mobilnisite/slovnik/mdas/"
type: "slovnik"
title: "MDAS – Management Data Analytics Service"
date: 2026-01-01
abbr: "MDAS"
fullName: "Management Data Analytics Service"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mdas/"
summary: "Služební schopnost poskytující analýzy dat managementu. Jedná se o služební zpřístupnění analytických funkcí jako MDAF, které umožňuje autorizovaným konzumentům žádat o poznatky pro optimalizaci sítě,"
---

MDAS je služební schopnost poskytující analýzy dat síťového managementu, která zpřístupňuje funkce jako MDAF autorizovaným konzumentům pro optimalizaci, správu chyb a zajištění výkonu.

## Popis

Management Data Analytics Service (MDAS) je konceptuální vrstva služby, která představuje zpřístupnění analytických schopností pro data managementu v systému 3GPP. Zavedená ve vydání 15, není samostatnou síťovou funkcí, ale služebním rozhraním a souborem schopností, přes které jsou analýzy konzumovány. Hlavním poskytovatelem této služby je Management Data Analytics Function ([MDAF](/mobilnisite/slovnik/mdaf/)), zavedená později. MDAS definuje, jak mohou konzumenti, což mohou být jiné funkce managementu (např. Network Slice Management Function), síťové funkce nebo aplikace operačního podpůrného systému ([OSS](/mobilnisite/slovnik/oss/)), interagovat s producenty analýz.

Služba je definována souborem služebních operací, datových modelů a informačních modelů standardizovaných ve specifikacích 3GPP. Klíčové operace zahrnují odběr analytického proudu, vyžádání analytické zprávy na požádání a správu analytických odběrů. Služba zprostředkovává vyjednávání typů analýz, požadavků na vstupní data a výstupních formátů. Funguje na principu modelu producent-konzument, kde producent (např. MDAF) nabízí své dostupné analytické schopnosti a konzument je objevuje a vyvolává. Vyměňovaná data zahrnují analytický vstup (jako data o měření výkonu nebo upozornění na chyby) a analytický výstup (jako předpovědi, doporučení nebo identifikované anomálie).

Architektonicky je MDAS realizována prostřednictvím služebních rozhraní (SBI) v rámci managementového rámce 5G jádra sítě. Zajišťuje interoperabilitu mezi analytickými řešeními a systémy managementu různých dodavatelů. Služba pokrývá široký rozsah analýz, včetně analýz výkonu (např. předpovídání degradace klíčových ukazatelů výkonu), analýz chyb (např. analýza hlavní příčiny) a konfiguračních analýz (např. optimalizační doporučení). Jejím úkolem je oddělit implementaci analytické logiky od konzumentů a poskytovat standardizovaný, znovupoužitelný a škálovatelný způsob vkládání inteligence do pracovních postupů síťového managementu a orchestraci.

## K čemu slouží

MDAS byla vytvořena za účelem zavedení standardizovaného, flexibilního a otevřeného rámce pro konzumaci analýz v rámci ekosystému managementu 3GPP. Před její definicí se systémy managementu spoléhaly na proprietární rozhraní a vestavěné analýzy, což ztěžovalo integraci nejlepších analytických řešení nebo sdílení poznatků napříč různými doménami managementu. Tento izolovaný přístup bránil automatizovanému a koordinovanému síťovému managementu.

Účelem MDAS je vyřešit tento integrační problém definováním společné vrstvy služby. Umožňuje síťovým operátorům pořizovat analytické schopnosti od různých dodavatelů a nechat je bezproblémově konzumovat jejich stávajícími [OSS](/mobilnisite/slovnik/oss/) a funkcemi managementu. To podporuje inovace a konkurenci na analytickém trhu. Dále podporuje vizi 5G o automatizaci sítě tím, že poskytuje jasný mechanismus pro funkce managementu, jak získat daty řízené poznatky nezbytné pro autonomní rozhodnutí, jako je dynamické přizpůsobování zdrojů síťového řezu nebo preventivní řešení přetížení.

Historicky se systémy managementu posouvaly k více daty řízeným operacím, ale postrádaly jednotný model. MDAS spolu s pozdější [MDAF](/mobilnisite/slovnik/mdaf/) tento model poskytují. Řeší omezení předchozích ad-hoc integrací tím, že nabízí budoucně odolnou, službami orientovanou architekturu pro konzumaci analýz, která je klíčová pro zvládání složitosti 5G sítí a umožnění pokročilých případů užití, jako je síťový a služební management s nulovou obsluhou (ZSM).

## Klíčové vlastnosti

- Standardizované služební operace pro odběr a vyžádání analýz
- Podpora více typů analýz (výkon, chyby, konfigurace atd.)
- Mechanismus pro zjišťování dostupných analytických schopností
- Flexibilní datové modely pro analytický vstup a výstup
- Umožňuje integraci analýz do systémů managementu nezávislou na dodavateli
- Základ pro management založený na záměru a operace v uzavřené smyčce

## Související pojmy

- [MDAF – Management Data Analytics Function](/mobilnisite/slovnik/mdaf/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 28.104** (Rel-19) — Management Data Analytics (MDA)
- **TS 28.533** (Rel-19) — Management and orchestration; Architecture framework
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TR 28.809** (Rel-17) — Enhancement of Management Data Analytics (MDA) Study
- **TS 28.866** (Rel-19) — Study on Management Data Analytics (MDA) – Phase 3
- **TS 28.890** (Rel-16) — ONAP-3GPP 5G Management Compatibility Study
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TR 33.866** (Rel-17) — Security aspects of Network Automation enablers for 5GS

---

📖 **Anglický originál a plná specifikace:** [MDAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdas/)
