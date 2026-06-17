---
slug: "ike"
url: "/mobilnisite/slovnik/ike/"
type: "slovnik"
title: "IKE – Internet Key Exchange"
date: 2026-01-01
abbr: "IKE"
fullName: "Internet Key Exchange"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ike/"
summary: "Internet Key Exchange (IKE) je protokol používaný k navázání zabezpečeného, autentizovaného komunikačního kanálu a k vyjednání bezpečnostních asociací (SAs) pro IPsec. V 3GPP se používá pro zabezpečen"
---

IKE je protokol používaný v 3GPP k navázání zabezpečených, autentizovaných kanálů a vyjednání bezpečnostních asociací (Security Associations) pro IPsec, čímž se zabezpečují rozhraní mezi síťovými funkcemi a data uživatelské roviny.

## Popis

Internet Key Exchange (IKE), konkrétně IKEv1 a IKEv2 definované [IETF](/mobilnisite/slovnik/ietf/) (RFC 2409, RFC 7296), je protokol používaný v systémech 3GPP k automatizaci navazování [IPsec](/mobilnisite/slovnik/ipsec/) bezpečnostních asociací (SAs). SA definuje parametry pro zabezpečený IPsec tunel, včetně kryptografických algoritmů (např. [AES](/mobilnisite/slovnik/aes/) pro šifrování, SHA-256 pro integritu), klíčů a režimu protokolu (Transportní nebo Tunelový). IKE provádí vzájemnou autentizaci mezi dvěma partnery, vyjednává kryptografické sady a bezpečně navazuje sdílené tajné klíče pro použití IPsec. Funguje ve dvou fázích: Fáze 1 navazuje samotný zabezpečený, autentizovaný kanál (IKE SA) a Fáze 2 tento kanál využívá k vyjednání IPsec SAs (často nazývaných Child SAs), které budou chránit vlastní uživatelská nebo signalizační data.

V architekturách 3GPP je IKE klíčovou součástí Network Domain Security ([NDS/IP](/mobilnisite/slovnik/nds-ip/)), která zabezpečuje komunikaci mezi síťovými uzly přes rozhraní založená na IP. Může být například použita k zabezpečení rozhraní [N2](/mobilnisite/slovnik/n2/) (mezi (R)[AN](/mobilnisite/slovnik/an/) a [AMF](/mobilnisite/slovnik/amf/)) nebo rozhraní N3 (mezi (R)AN a [UPF](/mobilnisite/slovnik/upf/)) v 5G systémech při nasazení přes nedůvěryhodné IP sítě. Protokol podporuje různé autentizační metody odkazované v 3GPP, včetně předem sdílených klíčů (PSK) a digitálních certifikátů (často s využitím certifikátů X.509). Diffie-Hellmanova výměna klíčů v IKE poskytuje dokonalé utajení dopředu (PFS), což znamená, že kompromitace dlouhodobého klíče neohrozí klíče předchozích relací.

Operace zahrnuje výměnu IKE zpráv (obvykle přes UDP port 500 nebo 4500 pro NAT traversal). Během Fáze 1 partneři dohodnou šifrovací a integritní algoritmy pro IKE SA, provedou Diffie-Hellmanovu výměnu pro vygenerování sdíleného tajemství a vzájemně se autentizují. Výsledkem je sada klíčů použitých k ochraně následných IKE zpráv. Ve Fázi 2, pod ochranou IKE SA, partneři vyjednají parametry pro IPsec SAs, včetně selektorů provozu, které definují, který IP provoz bude SA chránit. IKEv2 oproti IKEv1 proces zjednodušuje kombinací některých kroků. Specifikace 3GPP profilují použití IKE a IPsec, určují povinně podporované algoritmy a doporučené autentizační metody pro různá rozhraní.

## K čemu slouží

IKE bylo v 3GPP přijato k vyřešení problému ruční konfigurace a správy IPsec bezpečnostních asociací, což je v rozsáhlých, dynamických mobilních sítích nepraktické a náchylné k chybám. Jak se sítě 3GPP vyvíjely k plně IP architekturám (od Release 5), signalizace a uživatelská data procházela IP sítěmi, u kterých se nemohlo předpokládat fyzické zabezpečení (např. mezi různými provozními lokalitami nebo přes segmenty veřejného internetu). Byl potřebný standardizovaný, automatizovaný mechanismus pro poskytnutí hop-by-hop důvěrnosti, integrity a autentizace pro tento IP provoz.

Motivace vycházela z omezení spoléhání se na fyzické zabezpečení nebo proprietární bezpečnostní řešení. IKE jako zavedený IETF standard poskytlo řešení pro dynamickou správu klíčů s možností vzájemné spolupráce dodavatelů. Řeší specifické požadavky mobilních sítí, jako je potřeba podpory častých aktualizací bezpečnostních asociací (např. při předávání spojení nebo modifikacích relace) a integrace se síťovou autentizací (jako použití certifikátů vydaných operátorem). Jeho použití v NDS/IP umožňuje operátorům budovat zabezpečené IP páteřní sítě propojující síťové funkce jádra od různých dodavatelů umístěné na různých fyzických lokalitách, čímž zmírňuje hrozby jako odposlech, falšování identity a modifikace zpráv na těchto kritických vnitřních rozhraních.

## Klíčové vlastnosti

- Automatizuje vyjednávání a navazování IPsec bezpečnostních asociací (SAs)
- Poskytuje vzájemnou autentizaci pomocí metod jako předem sdílené klíče nebo certifikáty
- Podporuje dokonalé utajení dopředu (PFS) prostřednictvím Diffie-Hellmanovy výměny klíčů
- Definuje dvoufázovou výměnu (zřízení IKE SA následované vyjednáváním Child SA)
- Standardizováno IETF (IKEv1/IKEv2) a profilováno 3GPP pro NDS/IP
- Používá se k zabezpečení rozhraní mezi uzly v jádru sítě (např. N2, N3, N4)

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [NDS/IP – Network Domain Security for IP based Protocols](/mobilnisite/slovnik/nds-ip/)

## Definující specifikace

- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 29.368** (Rel-19) — Tsp Reference Point Stage 3 Specification
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 33.203** (Rel-19) — IMS Security Specification
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TS 33.234** (Rel-19) — 3GPP-WLAN Interworking Security
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.545** (Rel-19) — Security for NR Femto Subsystem
- **TS 33.820** (Rel-8) — Home NodeB/eNodeB Security Architecture
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G
- **TS 36.463** (Rel-19) — XwAP Protocol Specification
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [IKE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ike/)
