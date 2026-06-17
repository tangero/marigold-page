---
slug: "ipsec"
url: "/mobilnisite/slovnik/ipsec/"
type: "slovnik"
title: "IPSec – Internet Protocol Security"
date: 2025-01-01
abbr: "IPSec"
fullName: "Internet Protocol Security"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ipsec/"
summary: "Internet Protocol Security (IPSec) je soubor protokolů pro zabezpečení IP komunikace prostřednictvím autentizace a šifrování každého IP paketu v datovém toku. V 3GPP se používá k ochraně signalizace ř"
---

IPSec je soubor protokolů používaných v sítích 3GPP pro zabezpečení IP komunikace prostřednictvím autentizace a šifrování paketů, které chrání signalizaci řídicí roviny i data uživatelské roviny při přenosu přes nedůvěryhodné transportní sítě.

## Popis

Internet Protocol Security (IPSec) je rámec otevřených standardů, definovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý 3GPP, který poskytuje bezpečnostní služby na IP vrstvě. Funguje tak, že přidává bezpečnostní hlavičky (Authentication Header - [AH](/mobilnisite/slovnik/ah/) a Encapsulating Security Payload - [ESP](/mobilnisite/slovnik/esp/)) k IP paketům, což může poskytnout autentizaci původu dat, integritu, důvěrnost (šifrování) a ochranu proti opětovnému přehrání. V architekturách 3GPP je IPSec implementován ve dvou hlavních režimech: Transportním režimu, který zabezpečuje užitečné zatížení IP paketu, a Tunelovém režimu, který zapouzdřuje a zabezpečuje celý původní IP paket uvnitř nového IP paketu, čímž vytváří zabezpečený tunel.

Uvnitř sítě 3GPP IPSec funguje tak, že mezi dvěma koncovými body, jako je například mezi gNB a funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) 5G Core, nebo mezi síťovými funkcemi v rámci Service-Based Architecture (SBA), naváže tzv. Bezpečnostní asociaci (SA). SA definuje kryptografické algoritmy (např. [AES](/mobilnisite/slovnik/aes/) pro šifrování, SHA-256 pro integritu), klíče a další parametry pro zabezpečený kanál. Protokol Internet Key Exchange (IKEv2) se typicky používá pro automatizované vyjednávání a správu těchto SA. Klíčovými komponentami jsou síťové funkce s podporou IPSec, démon IKEv2 pro správu klíčů a bezpečnostní politiky, které určují, jaký provoz musí být chráněn.

Jeho role je klíčová pro síťové slicing, CUPS (Control and User Plane Separation) a pro propojení mezi síťovými operátory nebo mezi RAN a core sítí přes nedůvěryhodné IP sítě (např. veřejný internet pro přenos fronthaul/backhaul). Zajišťuje, že citlivá signalizace řídicí roviny (např. rozhraní [N2](/mobilnisite/slovnik/n2/), N4) a uživatelská data nemohou být odposlechnuta, modifikována nebo falšována. V 5G, s jeho cloud-nativním a službami založeným jádrem, je IPSec základním nástrojem pro implementaci bezpečnostního principu „zero-trust“, který zajišťuje zabezpečenou komunikaci mezi distribuovanými, potenciálně cloudovými síťovými funkcemi.

## K čemu slouží

IPSec byl integrován do standardů 3GPP, aby řešil rostoucí potřebu robustního, standardizovaného zabezpečení pro IP provoz s vývojem mobilních sítí. Rané mobilní sítě spoléhaly na zabezpečení primárně na rádiovém rozhraní (např. šifrování A5 v GSM) a uvnitř uzavřených, důvěryhodných domén operátora. Přechod na plně IP sítě, použití nedůvěryhodného přenosu (jako je veřejný internet pro backhaul) a oddělení řídicí a uživatelské roviny vytvořily nové vektory hrozeb, kde mohla být data zranitelná na spojení mezi síťovými uzly.

Vznik a přijetí IPSec bylo motivováno nutností chránit samotnou síťovou infrastrukturu. Řeší problém zabezpečení komunikace mezi síťovými prvky přes potenciálně nezabezpečené IP sítě, který nebyl dostatečně řešen zabezpečením na vrstvě spojení nebo fyzickým zabezpečením kabelů. To se stalo obzvláště kritickým u LTE a 5G, kde mohou být síťové funkce geograficky rozptýlené a hostované v datových centrech. IPSec poskytuje řešení na vrstvě 3, které je nezávislé na podkladové transportní technologii, a nabízí flexibilní a účinný způsob autentizace síťových prvků a zajištění soukromí a integrity veškeré komunikace mezi uzly, což je zásadní pro legální odposlech, integritu účtování a ochranu před útoky typu denial-of-service a man-in-the-middle.

## Klíčové vlastnosti

- Poskytuje důvěrnost dat prostřednictvím šifrování (ESP)
- Zajišťuje integritu dat a autentizaci původu (AH/ESP)
- Podporuje ochranu proti opětovnému přehrání pro detekci duplikace paketů
- Funguje jak v Transportním, tak v Tunelovém režimu pro flexibilitu
- Používá IKEv2 pro automatizovanou správu Bezpečnostních asociací a klíčů
- Integruje se s architekturou sítě 3GPP pro ochranu rozhraní N2, N3, N4, N6

## Definující specifikace

- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 34.229** (Rel-19) — IMS SIP/SDP UE Conformance Testing for 5GS

---

📖 **Anglický originál a plná specifikace:** [IPSec na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipsec/)
