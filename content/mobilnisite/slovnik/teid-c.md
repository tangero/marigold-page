---
slug: "teid-c"
url: "/mobilnisite/slovnik/teid-c/"
type: "slovnik"
title: "TEID-C – Tunnel Endpoint Identifier, control plane"
date: 2025-01-01
abbr: "TEID-C"
fullName: "Tunnel Endpoint Identifier, control plane"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/teid-c/"
summary: "Specifický typ TEID používaný výhradně v rámci protokolu GTP-Control (GTP-C). Identifikuje koncové body signalizačních tunelů mezi funkcemi řídicí roviny sítě (jako MME, SGW, PGW v 4G) a umožňuje spol"
---

TEID-C je identifikátor koncového bodu tunelu používaný výhradně v protokolu GTP-Control (řídicí rovina) k identifikaci koncových bodů signalizačních tunelů mezi funkcemi řídicí roviny sítě pro výměnu zpráv správy relace a mobility.

## Popis

TEID-C (Tunnel Endpoint Identifier, řídicí rovina) je specializovaný 32bitový identifikátor používaný v rámci [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol for the Control plane ([GTP-C](/mobilnisite/slovnik/gtp-c/)). Funguje na stejném základním principu jako obecný [TEID](/mobilnisite/slovnik/teid/), ale je striktně vyhrazen pro signalizační tunely mezi entitami řídicí roviny v Evolved Packet Core (EPC) a 5G Core síti. Z architektonického hlediska se GTP-C tunely vytvářejí mezi uzly jako [MME](/mobilnisite/slovnik/mme/) a [SGW](/mobilnisite/slovnik/sgw/) (rozhraní S11), SGW a [PGW](/mobilnisite/slovnik/pgw/) (rozhraní S5/S8 pro řídicí rovinu) a mezi [SGSN](/mobilnisite/slovnik/sgsn/) pro mezisystémovou mobilitu (S3/S4/S16). TEID-C jednoznačně identifikuje lokální koncový bod takového signalizačního tunelu na přijímajícím uzlu.

Jeho fungování je klíčové pro procedury správy relací a přenosových kanálů (bearer). Když entita řídicí roviny (např. MME) potřebuje zahájit signalizaci s jinou entitou (např. SGW), použije TEID-C protistrany jako cíl v hlavičce zprávy GTP-C. Tato hodnota TEID-C byla předtím vyměněna během počátečního nastavení uzlu nebo během předchozí procedury. Například během procedury připojení (LTE Attach) odešle MME požadavek Create Session Request na SGW. Tato zpráva obsahuje TEID-C MME pro řídicí rovinu na rozhraní S11, který si SGW uloží. Odpověď SGW obsahuje jeho vlastní TEID-C, což umožňuje obousměrnou komunikaci. Všechny následující zprávy pro toto konkrétní připojení [PDN](/mobilnisite/slovnik/pdn/) (např. Modify Bearer Request, Delete Session Request) budou používat tyto vzájemně dohodnuté hodnoty TEID-C k okamžitému spojení signalizace se správným kontextem UE.

Role TEID-C je odlišná od TEID pro uživatelskou rovinu (často označovaného jako TEID-U). Zatímco TEID-U identifikuje tunely pro uživatelské datové pakety, TEID-C identifikuje tunely pro signalizaci, která vytváří, upravuje a ruší tyto tunely uživatelské roviny. Toto oddělení identifikátorů řídicí a uživatelské roviny poskytuje jasné vymezení, zjednodušuje zpracování protokolu a zvyšuje bezpečnost a spolehlivost. V 5G Core, zatímco řídicí rovina primárně používá rozhraní založená na HTTP/2 (service-based interfaces), se GTP-C a TEID-C stále používají na určitých rozhraních, jako je N4 (mezi SMF a UPF) pro správu PFCP relací, což demonstruje jeho trvalou užitečnost pro přímé řízení uživatelské roviny.

## K čemu slouží

TEID-C byl vytvořen, aby vyřešil potřebu vyhrazeného, spolehlivého a kontextově orientovaného signalizačního kanálu mezi uzly řídicí roviny v paketovém jádru. Jak se mobilní sítě vyvíjely, aby podporovaly komplexní správu IP relací s více přenosovými kanály (bearer) a přísnými požadavky na QoS, výrazně se zvýšilo signalizační zatížení. Obecný signalizační přenos byl nedostatečný; signalizační zprávy bylo třeba přímo a jednoznačně spojit s kontextem relace konkrétního UE pro efektivní zpracování.

Zavedení TEID-C v rámci GTP-C to vyřešilo tím, že poskytlo mechanismus adresování řídicích zpráv přímo v přenosu (in-band). To bylo motivováno omezeními metod korelace mimo přenos (out-of-band) nebo nutností kontrolovat obsah každé signalizační zprávy. TEID-C umožňuje uzlu řídicí roviny okamžitě identifikovat příslušnou položku v databázi relací po přijetí paketu GTP-C, což umožňuje rychlé zpracování předávání spojení (handover), úprav přenosových kanálů a účtovacích událostí. Zajišťuje škálovatelnost řídicí roviny tím, že umožňuje jednomu síťovému rozhraní spravovat signalizaci pro miliony relací prostřednictvím jednoduchého demultiplexování založeného na TEID, což je návrh klíčový pro výkon vysokokapacitních 4G a 5G sítí s nízkou latencí.

## Klíčové vlastnosti

- 32bitový identifikátor používaný výhradně v protokolu GTP-Control (GTP-C)
- Jednoznačně identifikuje koncový bod signalizačního tunelu řídicí roviny
- Vyměňován během procedur zřizování relace (např. Create Session)
- Umožňuje přímé spojení signalizačních zpráv s kontextem relace konkrétního UE
- Odděluje adresování řídicí roviny od adresování uživatelské roviny (TEID-U)
- Nezbytný pro signalizaci správy relace, úprav přenosových kanálů (bearer) a mobility

## Definující specifikace

- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [TEID-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/teid-c/)
