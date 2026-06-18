---
slug: "impu"
url: "/mobilnisite/slovnik/impu/"
type: "slovnik"
title: "IMPU – IP Multimedia Public User Identity"
date: 2026-01-01
abbr: "IMPU"
fullName: "IP Multimedia Public User Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/impu/"
summary: "Veřejná SIP URI nebo TEL URI používaná k adresování uživatele pro multimediální komunikace v rámci IMS, například k uskutečnění hlasového nebo videohovoru. Jeden uživatel může mít více IMPU pro různé"
---

IMPU je veřejná SIP nebo TEL URI používaná v rámci IMS k adresování uživatele pro multimediální komunikace, přičemž jeden uživatel může mít zaregistrováno a přidruženo k soukromé IMPI více IMPU.

## Popis

IP Multimedia Public User Identity (IMPU) je veřejný identifikátor používaný pro směrování relací a zpráv k uživateli v rámci IMS. Má podobu [SIP](/mobilnisite/slovnik/sip/) Uniform Resource Identifier (SIP [URI](/mobilnisite/slovnik/uri/)), například sip:user@domain.com, nebo [TEL](/mobilnisite/slovnik/tel/) URI pro telefonní čísla, například tel:+1234567890. Na rozdíl od soukromé [IMPI](/mobilnisite/slovnik/impi/) se IMPU používá pro veškerou veřejnou komunikaci, například je uváděno v hlavičkách From a To SIP požadavků INVITE. K jednomu uživatelskému předplatnému, které je ukotveno jednou IMPI, může být přidruženo více IMPU, což umožňuje různé aliasy, typy služeb (např. pracovní, osobní) nebo skupinové identity. Během registrace v IMS uživatelský terminál (UE) zaregistruje jedno nebo více IMPU jejich přidružením k ověřené IMPI. Tato registrace je uložena v [S-CSCF](/mobilnisite/slovnik/s-cscf/), který si ze systému [HSS](/mobilnisite/slovnik/hss/) stáhne uživatelský profil služeb, včetně seznamu povolených IMPU a s nimi spojených filtračních kritérií (Initial Filter Criteria) pro spouštění aplikačních serverů. Při zahájení relace na určité IMPU dotazuje [I-CSCF](/mobilnisite/slovnik/i-cscf/) systém HSS, aby našel obsluhující S-CSCF pro tuto identitu, který následně provede uživatelskou servisní logiku. IMPU mohou být v různých stavech: registrovaná, neregistrovaná nebo blokovaná. Jsou také klíčovým prvkem pro funkce jako sady implicitní registrace, kde registrace jednoho IMPU automaticky zaregistruje další, nebo pro služby skrytí identity. Správa IMPU, včetně jejich blokování a propojení s profilem služeb, je ústřední pro poskytování a personalizaci služeb IMS.

## K čemu slouží

IMPU bylo vytvořeno, aby poskytlo flexibilní a uživatelsky přívětivé schéma adresování pro novou generaci IP multimediálních služeb v IMS, které překračuje závislost éry okruhového přepojování pouze na telefonní čísla E.164. Reaguje na potřebu bohaté sady identit, které mohou reprezentovat uživatele v různých kontextech (osobní, pracovní, specifický pro zařízení) a pro různé typy služeb (hlas, video, zasílání zpráv, stavová informace presence). Oddělení veřejné identity (IMPU) od soukromé identity ([IMPI](/mobilnisite/slovnik/impi/)) je klíčovým principem návrhu IMS, který zvyšuje bezpečnost a ochranu soukromí tím, že zajišťuje, že trvalý autentizační klíč není nikdy použit pro směrování. Tento model řeší problém, jak podporovat jak tradiční telefonii (prostřednictvím TEL URI), tak nativní internetovou komunikaci (prostřednictvím SIP URI) v rámci jednotné architektury. Byl motivován vizí konvergence, která uživatelům umožňuje být dostupní pod více identifikátory při zachování jediného předplatného a konzistentní uživatelské zkušenosti, čímž umožňuje pokročilé služby jako multimediální telefonie, instant messaging a stavová informace presence přes jakoukoli IP přístupovou síť.

## Klíčové vlastnosti

- Veřejná adresovací identita ve formátu SIP URI nebo TEL URI
- Používá se pro směrování SIP relací a zpráv v rámci IMS
- K jedné soukromé IMPI může být přidruženo více IMPU
- Spravována jako součást uživatelského profilu služeb v systému HSS
- Podporuje stavy registrace (registrováno/neregistrováno/blokováno) a sady implicitní registrace
- Umožňuje spouštění služeb prostřednictvím výchozích filtračních kritérií (Initial Filter Criteria, iFC) v S-CSCF

## Související pojmy

- [IMPI – IP Multimedia CN subsystem Private Identity](/mobilnisite/slovnik/impi/)
- [SIP-URI – SIP Uniform Resource Identifier](/mobilnisite/slovnik/sip-uri/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 31.829** (Rel-13) — ISIM Conformance Requirements Technical Report
- **TS 32.182** (Rel-19) — UDC Common Baseline Information Model (CBIM)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.141** (Rel-19) — Security for Presence Service (Ut reference point)
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [IMPU na 3GPP Explorer](https://3gpp-explorer.com/glossary/impu/)
