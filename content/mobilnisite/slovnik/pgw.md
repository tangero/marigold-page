---
slug: "pgw"
url: "/mobilnisite/slovnik/pgw/"
type: "slovnik"
title: "PGW – PDN Gateway"
date: 2026-01-01
abbr: "PGW"
fullName: "PDN Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pgw/"
summary: "PDN Gateway (PGW) je klíčový prvek jádrové sítě v systému Evolved Packet System (EPS). Slouží jako ukotvovací bod pro relaci uživatelského zařízení (UE) k externím paketovým datovým sítím (jako intern"
---

PGW je brána jádrové sítě, která ukotvuje relaci uživatele k externím paketovým datovým sítím, provádí přidělování IP adres, vynucování politik a účtování.

## Popis

[PDN](/mobilnisite/slovnik/pdn/) Gateway (PGW) je centrální uzel v architektuře 3GPP Evolved Packet Core (EPC), zavedené spolu s LTE ve verzi 8. Nachází se na hranici mezi důvěryhodnou sítí mobilního operátora a externími paketovými datovými sítěmi (PDN), jako je veřejný internet, síť IMS nebo podnikový intranet. Pro každé uživatelské zařízení (UE) je přidělen alespoň jeden PGW, který zpracovává jeho datové relace, známé jako PDN připojení. PGW vytváří tunel [GTP](/mobilnisite/slovnik/gtp/) ([GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol) s Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) pro přenos uživatelských dat a komunikuje s řídicími entitami, jako je [MME](/mobilnisite/slovnik/mme/) a [PCRF](/mobilnisite/slovnik/pcrf/).

Architektonicky plní PGW několik zásadních rolí. Je bodem přidělování IP adres pro UE, typicky pomocí [DHCP](/mobilnisite/slovnik/dhcp/) nebo funguje jako DHCP server. Vynucuje pravidla řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) přijatá od Policy and Charging Rules Function (PCRF), která určují, jak má být provoz zacházen (např. omezení šířky pásma, označování QoS) a jak má být účtován. PGW provádí hlubokou kontrolu paketů, filtrování paketů a zákonné odposlechy. Také slouží jako ukotvovací bod mobility pro uživatelskou rovinu, když se UE pohybuje mezi různými SGW, a zajišťuje kontinuitu relace. Pro přístupy mimo 3GPP (jako Wi-Fi přes rozhraní S2a/b/c) PGW slouží jako společný ukotvovací bod, umožňující plynulou mobilitu mezi 3GPP a důvěryhodnými/nedůvěryhodnými sítěmi mimo 3GPP.

Během provozu, když se UE připojí k síti, MME vybere PGW na základě Access Point Name (APN) požadovaného UE nebo předplaceného v HSS. PGW poté pro toto PDN připojení vytvoří výchozí přenosový kanál (default bearer), přidělí IP adresu a použije výchozí QoS a charakteristiky účtování. Když aplikace na UE generují provoz, PGW použije příslušné šablony toků provozu (TFT) ke směrování paketů na správný přenosový kanál, vynutí QoS politiky (nastavení značek DSCP) a generuje záznamy účtovacích dat (CDR) pro offline nebo online účtovací systémy. Je konečným směrovačem pro pakety směřující z UE na internet a prvním vstupním bodem pro pakety určené pro UE.

## K čemu slouží

PGW byl vytvořen jako součást 'System Architecture Evolution' (SAE) k řešení omezení před-LTE jádrové sítě GPRS. V GPRS sítích 2G/3G byly funkce brány rozděleny mezi SGSN (řízení) a GGSN (brána). GGSN byl často úzkým hrdlem a složitý na škálování. Architektura EPC měla za cíl plošší, plně IP síť se sníženou latencí a vyšší propustností, aby podpořila pokročilé rádiové schopnosti LTE. PGW konsolidoval a vylepšil funkce brány, jasněji oddělil řídicí a uživatelskou rovinu a umožnil flexibilnější vynucování politik.

Řeší několik klíčových problémů. Za prvé poskytuje stabilní ukotvovací bod pro mobilitu, skrývající pohyb UE v přístupové rádiové síti před externí PDN. IP adresa UE, přidělená PGW, zůstává konstantní, i když mění buňky nebo SGW. Za druhé umožňuje sofistikované řízení politik v reálném čase. Integrací s PCRF mohou operátoři implementovat služebně-aware účtování a QoS (např. upřednostňování VoIP provozu, omezování P2P provozu), což bylo v dřívějších architekturách obtížnější. Za třetí zjednodušuje integraci více přístupových technologií (LTE, 3G, Wi-Fi) tím, že poskytuje jediný, konzistentní IP ukotvovací bod. Jeho vytvoření bylo motivováno potřebou vysoce výkonného, škálovatelného a na politiky bohatého jádra sítě, aby se odemkl potenciál mobilního broadbandu a umožnily se nové služby generující příjmy.

## Klíčové vlastnosti

- Funguje jako IP ukotvovací bod, přiděluje IP adresy (IPv4/IPv6) uživatelským zařízením (UE) pro PDN konektivitu.
- Vynucuje pravidla řízení politik a účtování (PCC) přijatá od PCRF, aplikuje rozhodnutí o QoS a řízení přístupu.
- Slouží jako ukotvovací bod mobility pro uživatelskou rovinu během předávání mezi SGW a mezi systémy do/z přístupů mimo 3GPP.
- Provádí filtrování paketů, hlubokou kontrolu paketů a zákonné odposlechy podle požadavků.
- Generuje záznamy účtovacích dat (CDR) pro offline účtování a komunikuje s Online Charging Systems (OCS).
- Ukončuje rozhraní SGi a funguje jako směrovač mezi EPC a externími paketovými datovými sítěmi (Internet, IMS).

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 23.857** (Rel-11) — EPC Node Failure & Restoration Study
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 32.867** (Rel-15) — Management Impacts of EPC CUPS
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [PGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/pgw/)
