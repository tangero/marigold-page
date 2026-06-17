---
slug: "oscore"
url: "/mobilnisite/slovnik/oscore/"
type: "slovnik"
title: "OSCORE – Object Security for Constrained RESTful Environments"
date: 2025-01-01
abbr: "OSCORE"
fullName: "Object Security for Constrained RESTful Environments"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/oscore/"
summary: "Object Security for Constrained RESTful Environments (OSCORE) je bezpečnostní protokol poskytující koncové šifrování zpráv CoAP na aplikační vrstvě. Šifruje a autentizuje jednotlivá přenosová data a p"
---

OSCORE je bezpečnostní protokol poskytující koncové šifrování zpráv CoAP na aplikační vrstvě prostřednictvím šifrování a autentizace jednotlivých přenosových dat (payload) a parametrů (options) pro komunikaci v IoT.

## Popis

Object Security for Constrained RESTful Environments (OSCORE) je bezpečnostní protokol aplikační vrstvy standardizovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý 3GPP pro zabezpečení IoT komunikace, zejména té využívající Constrained Application Protocol (CoAP). Na rozdíl od zabezpečení na transportní vrstvě (TLS/[DTLS](/mobilnisite/slovnik/dtls/)), které chrání celý kanál, OSCORE aplikuje ochranu přímo na zprávu CoAP a transformuje ji na zabezpečenou 'zprávu OSCORE', která zapouzdřuje původní parametry a přenosová data CoAP. Tento proces je znám jako 'zabezpečení na úrovni objektu' (object security), protože ochrana je vázána na samotný objekt zprávy. Jádrem fungování OSCORE je použití formátu COSE ([CBOR](/mobilnisite/slovnik/cbor/) Object Signing and Encryption) pro kryptografické operace, konkrétně využití algoritmu AES-CCM pro zajištění důvěrnosti, integrity a autentizace chráněných polí zprávy.

OSCORE funguje na základě vytvoření sdíleného bezpečnostního kontextu mezi dvěma koncovými body (např. zařízením IoT a aplikačním serverem). Tento kontext zahrnuje hlavní tajemství (Master Secret), identifikátor odesílatele (Sender ID) a identifikátor příjemce (Recipient ID). Z hlavního tajemství jsou odvozovány klíče a inicializační vektor ([IV](/mobilnisite/slovnik/iv/)) pro každou zprávu. Každé zprávě je odesílatelem přiděleno jedinečné pořadové číslo (Sender Sequence Number), které je použito při odvozování IV, aby se zabránilo opakovaným útokům (replay attacks). Odesílatel zašifruje a ochrání integritu přenosových dat CoAP a určitých citlivých parametrů CoAP (jako Uri-Path), zatímco jiné parametry (např. ty potřebné pro směrování proxy) zůstávají nechráněné. Výsledná zpráva OSCORE obsahuje identifikátor odesílatele, částečný IV (odvozený z pořadového čísla) a šifrovaný text. Příjemce použije svůj bezpečnostní kontext, přijatý identifikátor odesílatele a částečný IV k rekonstrukci plného IV, dešifrování přenosových dat a ověření integrity.

V síti 3GPP je role OSCORE klíčová pro zabezpečení komunikace s koncovým šifrováním v IoT scénářích, zejména v rámci rozhraní Service Capability Exposure Function (SCEF) nebo Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) pro Non-IP Data Delivery ([NIDD](/mobilnisite/slovnik/nidd/)) a další služby pro omezená zařízení. Jeho hlavní architektonickou výhodou je, že umožňuje, aby zprávy zůstaly zabezpečené i při průchodu zprostředkovateli, jako jsou proxy CoAP nebo síťové brány, které mohou potřebovat číst nebo upravovat nechráněné parametry CoAP (např. pro ukládání do mezipaměti nebo směrování), ale nemají přístup k chráněným aplikačním datům. To jej činí ideálním pro sítě s nízkým výkonem a vysokými ztrátami (LLNs), kde mohou být relace zabezpečení na transportní vrstvě nákladné na udržování a kde zabezpečení mezi jednotlivými uzly (hop-by-hop) je nedostatečné pro zajištění důvěrnosti dat až k aplikačnímu serveru.

## K čemu slouží

OSCORE byl vytvořen, aby řešil specifické bezpečnostní výzvy vlastní Internetu věcí (IoT), kde jsou zařízení často výrazně omezena z hlediska výpočetního výkonu, paměti a energie. Tradiční bezpečnostní protokoly jako TLS/[DTLS](/mobilnisite/slovnik/dtls/), ačkoli robustní, mohou být pro taková zařízení příliš náročné, vyžadují značné prostředky pro navázání a udržování relace a mají vysokou režii na paket. Navíc v nasazeních IoT komunikace často prochází zprostředkovateli (proxy, brány) pro překlad protokolů nebo optimalizaci sítě. TLS poskytuje pouze zabezpečení mezi jednotlivými uzly (hop-by-hop), což znamená, že zprostředkovatel se stává důvěryhodnou entitou, která může vidět data v nešifrované podobě, což je pro koncové šifrování a soukromí nežádoucí.

Hlavním problémem, který OSCORE řeší, je jak poskytnout efektivní koncové šifrování pro přenosová data a kritická metadata zpráv CoAP bez nutnosti udržovat stavový tunel zabezpečení na transportní vrstvě. Byl motivován potřebou bezpečnostního řešení, které funguje v omezených prostředích, podporuje RESTful paradigma CoAP a umožňuje legitimní činnost zprostředkovatelů bez narušení zabezpečení. Tím, že zabezpečuje samotný 'objekt' (zprávu CoAP), OSCORE odděluje zabezpečení od podkladového transportu, což umožňuje bezpečnou komunikaci přes nespolehlivé transporty a skrz nedůvěryhodné uzly.

3GPP přijalo OSCORE pro zvýšení zabezpečení služeb IoT ve své architektuře, zejména pro služby vystavené přes [NEF](/mobilnisite/slovnik/nef/)/SCEF. Řeší omezení předchozích přístupů, kde mohla být data zařízení IoT chráněna pouze mezi zařízením a mobilní sítí, ale ne až k aplikačnímu serveru v cloudu. Povinným zavedením OSCORE pro určitá rozhraní 3GPP zajišťuje, že citlivá data IoT, jako jsou hodnoty ze senzorů nebo řídicí příkazy, zůstanou důvěrná a neporušená od omezeného zařízení až k jeho konečnému cíli, a to i při průchodu infrastrukturou sítě 3GPP a externími IP sítěmi.

## Klíčové vlastnosti

- Koncové šifrování pro přenosová data a vybrané parametry CoAP, nezávislé na transportu
- Používá odlehčený formát COSE s AES-CCM pro šifrování a integritu (AEAD)
- Ochrana přetrvává při přeposílání zprostředkovateli (proxy, brány)
- Nízká režie díky použití předem sdílených bezpečnostních kontextů a kompaktnímu formátování zpráv
- Ochrana proti opakování (replay protection) prostřednictvím pořadových čísel odesílatele zahrnutých do IV
- Selektivní ochrana umožňující zprostředkovatelům číst potřebné parametry pro směrování

## Definující specifikace

- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [OSCORE na 3GPP Explorer](https://3gpp-explorer.com/glossary/oscore/)
