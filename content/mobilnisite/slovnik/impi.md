---
slug: "impi"
url: "/mobilnisite/slovnik/impi/"
type: "slovnik"
title: "IMPI – IP Multimedia CN subsystem Private Identity"
date: 2026-01-01
abbr: "IMPI"
fullName: "IP Multimedia CN subsystem Private Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/impi/"
summary: "Trvalý, globálně unikátní soukromý identifikátor uživatele v rámci IMS (IP Multimedia Subsystem). Používá se pro autentizaci a registraci, je uložen v HSS a aplikaci ISIM a není veřejně sdílen. Je zás"
---

IMPI je trvalý, globálně unikátní soukromý identifikátor uživatele používaný pro autentizaci a registraci v rámci IMS, bezpečně uložený v HSS a ISIM, a je zásadní pro zabezpečený přístup ke službám.

## Popis

IP Multimedia CN subsystem Private Identity (IMPI) je klíčový identifikátor v architektuře 3GPP IMS, definovaný jako trvalý a globálně unikátní přihlašovací údaj přiřazený uživateli. Je bezpečně uložen v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a v rámci aplikace IP Multimedia Services Identity Module ([ISIM](/mobilnisite/slovnik/isim/)) na uživatelově Universal Integrated Circuit Card (UICC). IMPI se používá výhradně pro autentizační a registrační procedury, nikdy pro směrování [SIP](/mobilnisite/slovnik/sip/) zpráv nebo veřejnou komunikaci. Typicky má formát Network Access Identifier ([NAI](/mobilnisite/slovnik/nai/)), například user@realm. Během registrace do IMS předloží User Equipment (UE) IMPI spolu s autentizačními vektory odvozenými ze sdíleného tajného klíče Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) prostřednictvím Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)). S-CSCF ověří přihlašovací údaje s HSS pomocí autentizačních protokolů jako Digest AKAv1-MD5 nebo pozdějších, bezpečnějších metod. Tento proces vytvoří zabezpečené registrační propojení mezi IMPI a IP adresou uživatele, což umožňuje následnou autorizaci služeb. Oddělení IMPI od veřejných identit zajišťuje, že soukromý autentizační klíč uživatele není nikdy vystaven v síti, a poskytuje tak základní vrstvu zabezpečení. Je vnitřně propojen s uživatelským předplatným a zůstává konstantní, na rozdíl od dočasných identifikátorů, a tvoří kotvu pro uživatelský profil služeb IMS a přidružené veřejné identity (IMPUs).

## K čemu slouží

IMPI bylo vytvořeno za účelem poskytnutí zabezpečeného, na předplatném založeného autentizačního mechanismu pro IMS, které bylo zavedeno ve 3GPP Release 5 pro umožnění IP multimediálních služeb přes paketové sítě. Před IMS používaly okruhově přepínané mobilní sítě pro autentizaci International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), ale pro SIP-based, plně IP servisní vrstvu, která je nezávislá na podkladové přístupové síti (např. [GPRS](/mobilnisite/slovnik/gprs/), WLAN, pevný broadband), byl potřebný nový identifikátor. IMPI řeší problém bezpečné identifikace a autentizace uživatele vůči jádru IMS bez odhalení trvalých přihlašovacích údajů během vyvolání služby. Umožňuje jednomu uživateli s více zařízeními nebo servisními profily mít konzistentní soukromou identitu pro autentizaci, zatímco udržuje více veřejných identit pro komunikaci. Jeho vytvoření bylo motivováno potřebou robustního bezpečnostního modelu, který odděluje autentizaci (soukromou) od adresování (veřejného), což je princip převzatý z internetových bezpečnostních architektur, aby se zabránilo zneužití identity a zajistilo, že pouze autorizovaní účastníci mohou přistupovat a používat služby IMS jako VoLTE, ViLTE a RCS.

## Klíčové vlastnosti

- Globálně unikátní a trvalý identifikátor pro uživatelský předplatný vztah IMS
- Bezpečně uložený v HSS a v aplikaci ISIM na UICC
- Používaný výhradně pro autentizaci a registraci, nikoli pro směrování
- Formátovaný jako Network Access Identifier (NAI), např. user@operator.com
- Slouží jako kotva pro uživatelský profil služeb IMS a přidružené veřejné identity (IMPUs)
- Umožňuje autentizaci pomocí sdíleného tajného klíče a protokolů typu challenge-response

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [IMPU – IP Multimedia Public User Identity](/mobilnisite/slovnik/impu/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [ISIM – IMS Subscriber Identity Module](/mobilnisite/slovnik/isim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.066** (Rel-19) — Mobile Number Portability Stage 1
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.829** (Rel-13) — ISIM Conformance Requirements Technical Report
- **TS 32.182** (Rel-19) — UDC Common Baseline Information Model (CBIM)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.141** (Rel-19) — Security for Presence Service (Ut reference point)
- **TS 33.203** (Rel-19) — IMS Security Specification
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [IMPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/impi/)
