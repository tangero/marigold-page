---
slug: "nds"
url: "/mobilnisite/slovnik/nds/"
type: "slovnik"
title: "NDS – Network Domain Security"
date: 2026-01-01
abbr: "NDS"
fullName: "Network Domain Security"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/nds/"
summary: "Komplexní bezpečnostní rámec 3GPP pro ochranu signalizace a výměny uživatelských dat uvnitř a mezi síťovými doménami. Navazuje bezpečnostní asociace, šifrování a ochranu integrity pro síťová rozhraní"
---

NDS je bezpečnostní rámec 3GPP pro ochranu signalizace a výměny uživatelských dat uvnitř a mezi síťovými doménami prostřednictvím navázání bezpečnostních asociací, šifrování a ochrany integrity.

## Popis

Network Domain Security (NDS) je klíčová bezpečnostní architektura 3GPP, která poskytuje důvěrnost, integritu a ochranu proti opětovnému přehrání pro řídicí rovinu (signalizaci) a uživatelská data procházející síťovými doménami. „Síťová doména“ je definována jako část sítě spravovaná jedinou správní autoritou, například jádro sítě operátora nebo síť partnera. NDS zajišťuje, aby komunikace mezi síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) nebo mezi síťovými prvky napříč různými doménami byly zabezpečené, a brání tak odposlechu, manipulaci a podvržení. Funguje primárně na IP vrstvě a zabezpečuje protokoly založené na IP používané v rámci architektury 3GPP.

Architektura NDS je postavena na konceptu Bezpečnostních bran (SEG) a aplikaci Internet Protocol Security ([IPsec](/mobilnisite/slovnik/ipsec/)). Ve své klasické podobě, používané pro mezilehlá rozhraní mezi operátory jako Za (mezi SEPP), provoz mezi bezpečnostními doménami prochází SEG na hranici každé domény. Tyto SEG navazují tunely IPsec Encapsulating Security Payload ([ESP](/mobilnisite/slovnik/esp/)) v režimu tunelování, což poskytuje koncové zabezpečení mezi branami. Uvnitř jedné důvěryhodné domény operátora lze použít [NDS/IP](/mobilnisite/slovnik/nds-ip/) (profil NDS), často s využitím IPsec v transportním režimu přímo mezi síťovými funkcemi, nebo se stále více spoléhá na Transport Layer Security (TLS), jak je specifikováno v moderních architekturách. NDS definuje bezpečnostní politiky, postupy správy klíčů (často s využitím protokolů Internet Key Exchange, jako IKEv1 nebo IKEv2) a kryptografické algoritmy, které mají být použity.

Jeho role je všudypřítomná a klíčová. NDS zabezpečuje zásadní rozhraní jako [N2](/mobilnisite/slovnik/n2/) (mezi (R)[AN](/mobilnisite/slovnik/an/) a [AMF](/mobilnisite/slovnik/amf/)), N3 (mezi (R)AN a [UPF](/mobilnisite/slovnik/upf/)), N4 (mezi SMF a UPF) a N6 (mezi UPF a datovou sítí). V architektuře založené na službách (SBA) pro 5G jsou principy NDS rozšířeny použitím TLS pro rozhraní založená na službách využívající HTTP/2 (např. N8, N10, N12) mezi producentskými a konzumentskými NF. Tento rámec zajišťuje, že i když je podkladová přenosová síť nedůvěryhodná, užitečné zatížení zůstává chráněno. Je to povinná obranná vrstva, která izoluje důvěryhodné jádro 3GPP od externích IP sítí a zabezpečuje vnitřní komunikaci proti hrozbám zevnitř.

## K čemu slouží

NDS byl vytvořen, aby řešil zásadní posun telekomunikačních sítí od uzavřených, okruhově přepínaných systémů používajících signalizaci SS7 k otevřeným, IP architekturám s paketovým přepínáním. Dědičné sítě SS7 měly inherentní fyzickou bezpečnost, ale byly zranitelné vůči logickým útokům. Migrace na IP od verze 3GPP Release 4 dále vystavila signalizaci a uživatelská dat všem hrozbám běžným na veřejném internetu, jako je zachycení, manipulace a útoky typu odepření služby. Bylo naléhavě potřeba standardizovaného, robustního bezpečnostního rámce pro síťovou vrstvu.

Před NDS byla bezpečnost často implementována ad-hoc nebo byla omezena na rádiový přístupový spoj (např. použitím algoritmů jako A5 v GSM). Nebyl žádný jednotný standard pro zabezpečení přenosu v jádru sítě a propojení mezi operátory. NDS to vyřešil přijetím a profilováním dobře zavedených protokolů IETF, jako jsou IPsec a IKE, a jejich přizpůsobením specifickým potřebám spolehlivosti, škálovatelnosti a interoperability sítí úrovně operátora. Poskytl jasný model pro zabezpečení hranic domén, umožnil bezpečné propojení mezi sítěmi různých operátorů (klíčový požadavek pro roaming) a vytvořil „uzavřenou zahradu“ důvěry pro vlastní infrastrukturu operátora, což se stalo stále kritičtějším s přechodem na plně IP sítě v 4G a 5G.

## Klíčové vlastnosti

- Koncové zabezpečení signalizace a uživatelských dat napříč síťovými doménami
- Založeno na IPsec (ESP) a IKE pro správu klíčů a navázání tunelu
- Definuje architekturu Bezpečnostní brány (SEG) pro mezidoménovou bezpečnost
- Specifikuje sady kryptografických algoritmů a bezpečnostní politiky
- Rozšířeno o podporu TLS pro rozhraní založená na službách (SBI) v 5G
- Poskytuje povinnou ochranu důvěrnosti a integrity pro specifikovaná rozhraní

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 29.229** (Rel-19) — Diameter Protocol for Cx/Dx Interfaces
- **TS 29.329** (Rel-19) — Diameter Protocol for Sh Interface
- **TS 29.335** (Rel-19) — Ud Interface Protocol for UDC (Stage 3)
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications
- **TS 32.372** (Rel-19) — Security Service for IRP Information Service
- **TS 32.843** (Rel-13) — PS Domain Online Charging in Roaming
- **TS 33.203** (Rel-19) — IMS Security Specification
- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TS 33.310** (Rel-19) — 3GPP Authentication Framework for Network Nodes
- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G
- **TR 33.969** (Rel-19) — Security for Public Warning System (PWS)
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [NDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nds/)
