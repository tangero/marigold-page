---
slug: "sbma"
url: "/mobilnisite/slovnik/sbma/"
type: "slovnik"
title: "SBMA – Service Based Management Architecture"
date: 2025-01-01
abbr: "SBMA"
fullName: "Service Based Management Architecture"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/sbma/"
summary: "SBMA je architektura správy pro sítě 5G využívající principy orientované na služby k automatizaci a orchestraci síťových funkcí. Poskytuje standardizovaná rozhraní pro konfigurační, výkonnostní a poru"
---

SBMA je architektura správy pro sítě 5G, která využívá principy orientované na služby a standardizovaná rozhraní k automatizaci, orchestraci a efektivnímu provozu síťových funkcí v cloud-nativních prostředích.

## Popis

Service Based Management Architecture (SBMA) je architektura správy definovaná 3GPP pro systém 5G, která aplikuje principy architektury orientované na služby ([SBA](/mobilnisite/slovnik/sba/)) na operace správy sítě. Nahrazuje tradiční, na elementy zaměřené přístupy správy cloud-nativním, API-řízeným modelem, kde jsou managementové služby vystaveny jako standardizovaná, znovupoužitelná [API](/mobilnisite/slovnik/api/). V SBMA jsou síťové funkce a zdroje spravovány prostřednictvím souboru managementových služeb, jako je správa konfigurace, správa výkonu, správa poruch a provisioning, které jsou spotřebovávány managementovými aplikacemi nebo orchestračními systémy. Tyto služby jsou postaveny na principech [HTTP](/mobilnisite/slovnik/http/)/2 a RESTful, používají [JSON](/mobilnisite/slovnik/json/) nebo [XML](/mobilnisite/slovnik/xml/) pro výměnu dat a jsou definovány ve specifikacích OpenAPI, aby byla zajištěna interoperabilita mezi dodavateli. Architektura zahrnuje klíčové komponenty, jako je Management Function ([MF](/mobilnisite/slovnik/mf/)), která poskytuje managementové služby, a Management Service Consumer ([MSC](/mobilnisite/slovnik/msc/)), který tyto služby využívá k provádění úloh správy.

SBMA funguje na principu oddělení managementové logiky od spravovaných síťových funkcí, což umožňuje centralizovaná nebo distribuovaná nasazení správy. Managementové služby jsou registrovány a objevovány prostřednictvím registru služeb, podobně jako Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)) v 5G Core, což umožňuje dynamické skládání služeb a škálovatelnost. Například služba správy výkonu může prostřednictvím standardizovaných rozhraní sbírat metriky z více síťových funkcí, agregovat data a poskytovat je analytickému modulu. Služby správy poruch se mohou přihlásit k odběru alarmů z různých funkcí a spouštět automatizované nápravné akce. Služby správy konfigurace umožňují konzistentní provisioning a aktualizaci parametrů síťových funkcí, čímž podporují zero-touch provisioning a síťovou automatizaci. SBMA se také integruje s širšími managementovými systémy, jako je Network Slice Management Function (NSMF) a Network Slice Subnet Management Function (NSSMF), pro správu životního cyklu síťových řezů od vytvoření po ukončení.

Úlohou SBMA v síti je umožnit efektivní, škálovatelnou a automatizovanou správu sítí 5G, které se vyznačují svou složitostí, dynamičností a využitím virtualizačních technologií. Použitím rozhraní orientovaných na služby SBMA snižuje úsilí při integraci různých managementových systémů a síťových funkcí, protože všechny interakce následují společný vzor. Podporuje správu založenou na záměrech (intent-based management), kde jsou vysoké obchodní cíle (např. "zajistit 99,9% spolehlivost pro řez X") převáděny na nízkou úroveň managementových akcí prostřednictvím politika-řízené automatizace. SBMA je nezbytná pro správu síťového řezání, protože poskytuje nástroje pro monitorování a úpravu výkonu řezů, dynamické přidělování zdrojů a zajištění izolace mezi řezy. Usnadňuje také integraci umělé inteligence a strojového učení pro prediktivní údržbu a optimalizaci tím, že poskytuje standardizovanou rovinu pro sběr dat a řízení.

## K čemu slouží

SBMA byla vytvořena, aby řešila výzvy správy, které přinesly sítě 5G, jež jsou ve srovnání s předchozími generacemi složitější, dynamičtější a více softwarově řízené. Tradiční managementové architektury, jako jsou ty založené na SNMP nebo proprietárních rozhraních, byly navrženy pro statické, hardwarové sítě a nedokázaly držet krok s agilitou vyžadovanou pro cloud-nativní nasazení, síťové řezání a edge computing. Tyto starší systémy často zahrnovaly manuální konfiguraci, izolované domény správy a vysokou provozní režii, což ztěžovalo škálování a automatizaci síťových operací.

Primární motivací pro SBMA bylo sladit správu sítě s architekturou orientovanou na služby 5G Core, což umožňuje jednotný, API-řízený přístup, který zjednodušuje integraci a automatizaci. Přijetím RESTful API a principů mikroslužeb umožňuje SBMA operátorům spravovat síťové funkce jako softwarové komponenty, které lze dynamicky orchestraovat. To je klíčové pro podporu případů užití, jako je síťové řezání, kde každý řez může mít jedinečné požadavky na správu, které musí být provisionovány a monitorovány v reálném čase. SBMA také řeší potřebu interoperability mezi více dodavateli, protože standardizovaná rozhraní snižují závislost na dodavatelsky specifických nástrojích správy.

Historicky se SBMA vyvinula z dřívějších managementových architektur 3GPP, jako je Telecommunications Management Network (TMN) a později koncepty Management and Orchestration (MANO) od ETSI NFV. Byla formálně představena ve 3GPP Release 16 jako součást specifikací správy pro 5G, navazujíc na úspěch SBA v řídicí rovině. Tím, že řeší problémy fragmentace a rigidity v síťové správě, umožňuje SBMA operátorům dosáhnout vyšší provozní efektivity, rychlejšího nasazování služeb a lepšího využití zdrojů, což je nezbytné pro monetizaci investic do 5G a podporu inovativních služeb.

## Klíčové vlastnosti

- Managementová rozhraní orientovaná na služby využívající RESTful API
- Podpora správy konfigurace, výkonu, poruch a provisioningu
- Integrace se síťovým řezáním pro správu životního cyklu řezů
- Umožňuje zero-touch provisioning a síťovou automatizaci
- Používá specifikace OpenAPI pro interoperabilitu mezi dodavateli
- Usnadňuje správu založenou na záměrech a politika-řízené operace

## Související pojmy

- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)
- [NSMF – Network Slice Management Function](/mobilnisite/slovnik/nsmf/)

## Definující specifikace

- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.111** (Rel-19) — Fault Management Service Specification
- **TS 28.533** (Rel-19) — Management and orchestration; Architecture framework
- **TR 28.834** (Rel-18) — Technical Report
- **TR 28.837** (Rel-18) — Technical Report on Trace/MDT Management
- **TS 28.871** (Rel-19) — Study on Service Based Management Architecture enhancement phase 3
- **TS 28.873** (Rel-19) — Study on Data Management, Subscriptions, and Reporting
- **TR 28.925** (Rel-19) — Enhancement of Service Based Management Architecture
- **TS 32.300** (Rel-19) — 3GPP Network Resource Naming Convention

---

📖 **Anglický originál a plná specifikace:** [SBMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbma/)
