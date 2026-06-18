---
slug: "scp"
url: "/mobilnisite/slovnik/scp/"
type: "slovnik"
title: "SCP – Service Communication Proxy"
date: 2026-01-01
abbr: "SCP"
fullName: "Service Communication Proxy"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/scp/"
summary: "Funkce jádra sítě, která poskytuje centralizovanou, bezpečnou a škálovatelnou proxy pro komunikaci na rozhraní založeném na službách (SBI) mezi síťovými funkcemi (NF) v 5G. Umožňuje jejich vyhledávání"
---

SCP je funkce jádra sítě, která slouží jako centralizovaná, bezpečná proxy pro komunikaci založenou na službách mezi síťovými funkcemi, umožňující v 5G sítích jejich vyhledávání, vyvažování zátěže a zabezpečení.

## Popis

Service Communication Proxy (SCP) je základním architektonickým prvkem v rámci 5G jádra sítě (5GC) fungujícím v architektuře založené na službách ([SBA](/mobilnisite/slovnik/sba/)). Slouží jako zprostředkovatel pro veškerou komunikaci na rozhraní založeném na službách ([SBI](/mobilnisite/slovnik/sbi/)) využívající [HTTP](/mobilnisite/slovnik/http/)/2 mezi producentskými a konzumerskými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)). SCP poskytuje centralizovanou komunikační vrstvu, která abstrahuje přímé propojení typu point-to-point. Jeho hlavní úlohou je správa vyhledávání a výběru služeb. Když konzumerská NF potřebuje vyvolat službu, odešle požadavek SCP. SCP následně konzultuje Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)), aby vyhledal vhodné instance produkčních NF, které požadovanou službu nabízejí, a přitom zvažuje faktory jako zátěž, umístění a kontext síťového řezu. Po vyhledání může SCP provést vyvážení zátěže výběrem vhodné instance produkční NF a bezpečně přeposlat požadavek. Tím se odstraňuje závislost konzumerských služeb na přímé znalosti instancí produkčních NF a jejich umístění.

Z architektonického hlediska je SCP definován jako nezávislá síťová funkce s vlastním rozhraním založeným na službách. Podporuje jak model směrování požadavků (request-routing), kdy funguje jako proxy pro všechny zprávy, tak model nepřímé komunikace (indirect communication), kdy poskytuje konzumerské NF informace pro vyhledávání, načež ta komunikuje přímo. SCP implementuje klíčové bezpečnostní funkce, jako je ukončení a znovunavázání zabezpečení transportní vrstvy ([TLS](/mobilnisite/slovnik/tls/)), čímž zajišťuje end-to-end zabezpečení napříč služební sítí (service mesh). Může také vynucovat přístupové politiky, validovat zprávy a poskytovat skrytí topologie (topology hiding) tím, že maskuje vnitřní strukturu sítě před externími entitami nebo mezi různými síťovými řezy.

Kromě vyhledávání a zabezpečení SCP zvyšuje spolehlivost a škálovatelnost sítě. Podporuje směrování a přeposílání zpráv na základě politik, informací o účastníkovi a identifikátorů síťových řezů. Může poskytovat odolnost prostřednictvím mechanismů jako opakované přenosy a alternativní směrování v případě selhání produkční NF. Centralizovaná povaha SCP zjednodušuje provoz sítě, protože politiky pro vyvažování zátěže, usměrňování provozu a zabezpečení lze spravovat v jednom logickém bodě namísto jejich distribuce napříč každou NF. To je klíčové pro rozsáhlá cloud-nativní nasazení, kde jsou NF dynamicky vytvářeny a škálovány. SCP je klíčovým prvkem pro efektivní síťové řezy (network slicing), protože dokáže směrovat požadavky k instancím NF patřícím do konkrétního řezu, čímž zajišťuje izolaci a přizpůsobené úrovně služeb.

## K čemu slouží

SCP byl zaveden, aby řešil složitosti přímé komunikace služba-služba v 5G architektuře založené na službách ([SBA](/mobilnisite/slovnik/sba/)). V dřívějších architekturách 3GPP, jako bylo 4G Evolved Packet Core (EPC), byla rozhraní primárně point-to-point a specifická pro daný protokol (např. [GTP](/mobilnisite/slovnik/gtp/), Diameter). Přechod na cloud-nativní, na mikroslužbách založené 5GC s rozhraními API využívajícími HTTP/2 vytvořil dynamické prostředí, kde jsou síťové funkce (NF) efemérní a škálovatelné. Přímá komunikace by vyžadovala, aby každá konzumerská NF neustále vyhledávala a spravovala spojení ke všem potenciálním produkčním NF, což by vedlo k významné signalizační režii, složité správě sítě služeb (mesh management) a snížené agilitě.

SCP tyto problémy řeší tím, že poskytuje centralizovanou komunikační strukturu (fabric). Abstrahuje vyhledávání služeb a směrování, což umožňuje, aby byly NF vyvíjeny a nasazovány nezávisle bez pevně zakódovaných závislostí. Tím se řeší problém vyhledávání NF v dynamicky se měnícím prostředí. Dále řeší kritické bezpečnostní a provozní potřeby. Poskytuje centrální bod pro implementaci bezpečnostních politik (jako je vzájemné TLS), řízení přístupu a skrytí topologie, což je zásadní pro zabezpečení operátora a při vystavování síťových schopností třetím stranám. Jeho vytvoření bylo motivováno potřebou škálovatelného, spravovatelného a bezpečného modelu vzájemného propojení, který podporuje automatizaci, síťové řezy (network slicing) a efektivní provoz disagregovaného, softwarově definovaného jádra sítě.

## Klíčové vlastnosti

- Centralizované vyhledávání a výběr služeb prostřednictvím interakce s NRF
- Vyvažování zátěže a usměrňování provozu napříč více instancemi produkční NF
- Vynucování end-to-end zabezpečení, včetně zprostředkování TLS a autorizace
- Skrytí topologie (topology hiding) k abstrakci vnitřní síťové struktury před konzumery
- Podpora modelů nepřímé komunikace a směrování požadavků
- Směrování a přeposílání zpráv na základě politik s podporou síťových řezů (network slicing)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.094** (Rel-19) — Follow Me (FM) Feature Stage 2
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.540** (Rel-19) — 5G Service Based SMS Stage 2
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TR 28.840** (Rel-18) — Technical Report
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 29.500** (Rel-19) — 5GC Service Based Architecture Specification
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 29.570** (Rel-19) — SCP Nscp Service Based Interface Stage 3
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [SCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/scp/)
