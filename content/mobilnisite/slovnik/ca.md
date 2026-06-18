---
slug: "ca"
url: "/mobilnisite/slovnik/ca/"
type: "slovnik"
title: "CA – Certification Authority"
date: 2026-01-01
abbr: "CA"
fullName: "Certification Authority"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ca/"
summary: "Důvěryhodná entita, která vydává a spravuje digitální certifikáty v sítích 3GPP a umožňuje bezpečné ověřování a komunikaci. Vytváří infrastrukturu veřejných klíčů (PKI) pro ověření identity síťových p"
---

CA je důvěryhodná entita, která vydává a spravuje digitální certifikáty za účelem zajištění bezpečného ověřování a komunikace, čímž vytváří infrastrukturu veřejných klíčů (PKI) pro ověřování identit v sítích 3GPP.

## Popis

Certifikační autorita (CA) je základní součástí infrastruktury veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) v bezpečnostních architekturách 3GPP. Jedná se o důvěryhodnou entitu třetí strany, která je odpovědná za vydávání, odvolávání a správu digitálních certifikátů. Tyto certifikáty spojují veřejný klíč s identitou účastníka, síťové funkce (jako je gNB nebo [AMF](/mobilnisite/slovnik/amf/)) nebo služby, což umožňuje kryptografické ověření. Základní činnost CA spočívá v ověření identity entity žádající o certifikát (subjektu), podepsání certifikátu svým soukromým klíčem za účelem vytvoření důvěryhodného pověření a publikování příslušného seznamu odvolaných certifikátů ([CRL](/mobilnisite/slovnik/crl/)) nebo podpoře protokolu [OCSP](/mobilnisite/slovnik/ocsp/) pro deklaraci neplatných certifikátů. Důvěra v celý systém závisí na bezpečném zabezpečení soukromého klíče CA a na důsledném auditu jejích provozních politik.

V ekosystému 3GPP může existovat více CA, které tvoří hierarchii. Kořenová CA, která je samopodepsaná a inherentně důvěryhodná, vydává certifikáty podřízeným, zprostředkujícím CA. Tyto zprostředkující CA pak vydávají certifikáty koncovým entitám, jako jsou síťové prvky a uživatelská zařízení (UE). Tento hierarchický model umožňuje škálovatelnou správu důvěry a omezuje vystavení kritického soukromého klíče kořenové CA. Ověření certifikátu zahrnuje ověření řetězce digitálních podpisů zpět k důvěryhodnému certifikátu kořenové CA, který je předem zřízen v úložišti důvěry ověřující entity. Tento proces je klíčový pro protokoly jako [TLS](/mobilnisite/slovnik/tls/)/[DTLS](/mobilnisite/slovnik/dtls/) pro zabezpečení rozhraní N1, [N2](/mobilnisite/slovnik/n2/) a N3 v 5G a pro ověřování ve scénářích, jako je architektura založená na službách síťových funkcí 5G.

Role CA přesahuje pouhé vydávání. Vynucuje certifikační politiku ([CP](/mobilnisite/slovnik/cp/)) a prohlášení o certifikační praxi (CPS), které definují bezpečnostní kontrolní mechanismy, postupy správy životního cyklu a rámce odpovědnosti. Klíčové obřady správy klíčů pro generování a ukládání klíčů CA se provádějí ve vysoce zabezpečených, často offline, hardwarových bezpečnostních modulech (HSM). V 3GPP CA podporují různé certifikační profily definované ve specifikacích, včetně profilů pro UICC, ochranu SUCI/SUPI a ověřování síťových funkcí. Integrita PKI, a tedy i bezpečnost ověřovacích a důvěrnostních mechanismů v sítích 3GPP, přímo závisí na správném a bezpečném provozu certifikační autority.

## K čemu slouží

Certifikační autorita existuje proto, aby řešila základní problém budování důvěry ve velkém měřítku v distribuovaném digitálním prostředí, jakým je mobilní síť. Před zavedením PKI bylo bezpečné distribuování klíčů pro symetrickou kryptografii obtížné a neškálovalo pro miliony účastníků a tisíce síťových uzlů. CA umožňuje asymetrickou kryptografii tím, že poskytuje ověřitelné a důvěryhodné spojení mezi veřejným klíčem a identitou. To umožňuje jakékoli entitě ověřit pravost jiné entity bez předchozího sdílení tajemství, což je nezbytné pro scénáře jako je počáteční připojení k síti, roaming a bezpečné zjišťování služeb.

Historicky, jak se sítě 3GPP vyvíjely od 2G (které používalo sdílené tajemství na SIM) přes 3G a dále, rostla potřeba flexibilnější, na služby orientované bezpečnosti. Zavedení služeb založených na IP, IMS a později cloud-nativních 5G jader sítí vyžadovalo standardizovanou, interoperabilní metodu pro ověřování a bezpečnou komunikaci mezi předtím neznámými stranami. CA a PKI toto poskytují tím, že oddělují navázání důvěry (spravované CA) od bezpečné komunikace (prováděné koncovými entitami pomocí certifikátů). Řeší tak omezení proprietárních nebo centralizovaných systémů správy klíčů tím, že poskytuje standardizovaný, škálovatelný a auditovatelný rámec pro digitální důvěru, který podporuje moderní bezpečnostní funkce 3GPP jako AKA, EAP-TLS a SEAL.

## Klíčové vlastnosti

- Vydává a podepisuje digitální certifikáty X.509, které spojují identity s veřejnými klíči
- Spravuje seznam odvolaných certifikátů (CRL) nebo podporuje OCSP pro ověřování stavu
- Funguje v rámci hierarchické struktury PKI s kořenovou a podřízenými CA
- Vynucuje definovanou certifikační politiku (CP) a prohlášení o certifikační praxi (CPS)
- Využívá hardwarové bezpečnostní moduly (HSM) pro bezpečné generování a ukládání klíčů
- Podporuje specifické certifikační profily 3GPP pro UE a síťové funkce

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TS 28.314** (Rel-20) — Management and Orchestration - Plug and Connect
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set
- **TS 32.501** (Rel-19) — Self-Configuration of Network Elements Concepts
- … a dalších 111 specifikací

---

📖 **Anglický originál a plná specifikace:** [CA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ca/)
