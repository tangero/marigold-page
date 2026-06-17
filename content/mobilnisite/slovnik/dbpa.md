---
slug: "dbpa"
url: "/mobilnisite/slovnik/dbpa/"
type: "slovnik"
title: "DBPA – Diameter Base Protocol Accounting"
date: 2025-01-01
abbr: "DBPA"
fullName: "Diameter Base Protocol Accounting"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dbpa/"
summary: "DBPA je rámec účtování (accounting) protokolu Diameter v sítích 3GPP, který umožňuje sběr, korelaci a přenos dat o využití pro fakturaci a účtování. Poskytuje standardizovanou, spolehlivou a bezpečnou"
---

DBPA je rámec účtování (accounting) protokolu Diameter Base Protocol v sítích 3GPP, který umožňuje standardizovaný, spolehlivý a bezpečný sběr a přenos dat o využití pro systémy fakturace a účtování (billing and charging).

## Popis

Diameter Base Protocol Accounting (DBPA) je nedílnou součástí sady protokolů Diameter, konkrétně definovanou pro účtovací (accounting) operace v sítích 3GPP. Funguje jako aplikace nad základním protokolem Diameter (RFC 6733), využívající jeho architekturu peer-to-peer, spolehlivý přenos přes TCP nebo SCTP a vestavěné bezpečnostní prvky jako TLS a [IPsec](/mobilnisite/slovnik/ipsec/). DBPA definuje konkrétní příkazy Diameter, páry atribut-hodnota ([AVP](/mobilnisite/slovnik/avp/)) a stavové automaty relací nezbytné pro sběr a hlášení dat o využití ze síťových elementů, jako je [P-GW](/mobilnisite/slovnik/p-gw/), S-GW nebo [MME](/mobilnisite/slovnik/mme/), k účtovacím funkcím, jako je Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) nebo Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)).

Protokol pracuje na modelu žádost-odpověď s využitím specifických kódů příkazů Accounting-Request ([ACR](/mobilnisite/slovnik/acr/)) a Accounting-Answer ([ACA](/mobilnisite/slovnik/aca/)). Síťový element fungující jako klient Diameter zahájí účtovací relaci odesláním zprávy ACR, která obsahuje klíčové AVP jako Session-Id, Accounting-Record-Type (START, INTERIM, STOP, EVENT) a četné služebně specifické AVP detailující využití prostředků (např. objem dat, doba trvání, parametry QoS). Přijímající účtovací server (např. Charging Data Function nebo CDF) žádost zpracuje, zkorreluje ji se správnou relací účastníka a vrátí zprávu ACA na potvrzení přijetí. To umožňuje hlášení událostí v reálném čase (online) nebo dávkové (offline).

Mezi klíčové architektonické komponenty patří stav účtovací relace, udržovaný pomocí Accounting-Record-Type a Session-Id, který umožňuje korelaci více průběžných aktualizací pro jednu relaci služby. DBPA podporuje jak účtování založené na událostech (pro okamžité, jednorázové poplatky), tak účtování založené na relacích (pro kontinuální služby, jako je datová relace). Návrh protokolu zajišťuje schopnosti převzetí služeb při selhání (failover) a návratu (failback) prostřednictvím mechanismů objevování a směrování partnerů Diameter, což garantuje, že účtovací data nebudou ztracena ani při selhání primárního serveru. Jeho role je klíčová v architektuře Charging Trigger Function (CTF), kde slouží jako standardizované rozhraní směrem nahoru (northbound) pro přenos záznamů účtovacích dat (CDR) nebo událostí kontroly kreditu.

Rozšiřitelnost DBPA je hlavní vlastností; zatímco specifikace 3GPP jako 32.299 definují základní sadu AVP pro telekomunikační služby, dodavatelé a další standardizační orgány mohou definovat nová, dodavatelsky specifická AVP pro přenos dodatečných informací. To činí DBPA adaptabilním i mimo jeho původní rámec 3GPP. Jeho integrace se širší infrastrukturou Diameter – včetně přenosových (relay), proxy a přesměrovacích (redirect) agentů – navíc umožňuje škálovatelné a řiditelné účtování napříč rozsáhlými distribuovanými sítěmi, čímž tvoří páteř moderních architektur politiky a účtování.

## K čemu slouží

DBPA byl vytvořen, aby řešil omezení svého předchůdce, účtovacího protokolu RADIUS, který nebyl navržen pro složité požadavky na vysokou spolehlivost sítí 3GPP. RADIUS trpěl omezeními škálovatelnosti, nedostatkem inherentní bezpečnosti (spoléhal se na sdílená tajemství mezi jednotlivými uzly) a omezenou podporou sofistikovaných modelů účtování založených na relacích a událostech, vyžadovaných pro IP služby mobilních sítí, jako je IMS a mobilní broadband. Přechod na plně IP jádrové sítě ve 3GPP Release 5 a novějších si vyžádal robustnější, flexibilnější a bezpečnější protokol pro přenos dat souvisejících s fakturací.

Primární problém, který DBPA řeší, je poskytnutí standardizovaného, provozovatelsky vhodného mechanismu, aby síťové elementy mohly spolehlivě a bezpečně hlásit informace o využití centralizovaným systémům účtování. To umožňuje přesné účtování různorodých služeb – od hlasových hovorů a SMS přes datové relace až po multimediální služby IMS – na základě detailní spotřeby prostředků. Jeho vytvoření bylo motivováno potřebou možností účtování v reálném čase pro podporu předplacených služeb a sofistikovaných tarifních modelů, které bylo s dřívějšími protokoly obtížné spolehlivě implementovat. Tím, že je DBPA součástí sady Diameter, také zajišťuje bezproblémovou integraci s paralelní aplikací Diameter Credit-Control Application (DCCA) používanou pro online účtování, čímž vytváří jednotný ekosystém protokolů pro řízení politiky a účtování.

## Klíčové vlastnosti

- Standardizovaná sada příkazů (ACR/ACA) pro účtovací operace
- Podpora typů účtovacích záznamů založených na relacích a na událostech
- Spolehlivý přenos přes TCP/SCTP s podporou převzetí služeb při selhání (failover)
- Rozšiřitelná struktura AVP (pár atribut-hodnota) pro přenos dat o využití
- Integrace s bezpečnostními prvky základního protokolu Diameter (TLS, IPsec)
- Korelace účtovacích záznamů prostřednictvím Session-Id a stavu účtovací relace

## Definující specifikace

- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 32.869** (Rel-15) — Diameter Overload Control for Charging Interfaces

---

📖 **Anglický originál a plná specifikace:** [DBPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dbpa/)
