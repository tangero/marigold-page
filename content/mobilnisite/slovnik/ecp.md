---
slug: "ecp"
url: "/mobilnisite/slovnik/ecp/"
type: "slovnik"
title: "ECP – Enhanced Client or Proxy"
date: 2025-01-01
abbr: "ECP"
fullName: "Enhanced Client or Proxy"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ecp/"
summary: "Bezpečnostní entita definovaná v rámci frameworku Security Assertion Markup Language (SAML), používaná pro zabezpečenou správu identit a přístupu v sítích 3GPP. Funguje jako zprostředkovatel pro požad"
---

ECP je bezpečnostní entita SAML, která funguje jako zprostředkovatel pro požadavky na ověření a autorizaci za účelem zvýšení bezpečnosti a ochrany soukromí při přístupu ke službám sítí 3GPP.

## Popis

Enhanced Client or Proxy (ECP) je profil ve specifikaci Security Assertion Markup Language (SAML) 2.0, který je přijat a odkazován standardy 3GPP pro federaci identit a jednotné přihlašování (SSO) v telekomunikačních prostředích. SAML je XML framework pro výměnu dat ověření a autorizace mezi stranami, konkrétně mezi poskytovatelem identity (IdP) a poskytovatelem služeb (SP). Profil ECP je navržen pro scénáře, kdy klient (např. uživatelské zařízení nebo síťová funkce) není standardní webový prohlížeč, ale sofistikovanější entita, jako je specializovaná aplikace nebo síťový proxy server, která může přímo zpracovávat zprávy protokolu SAML. V architekturách 3GPP ECP usnadňuje zabezpečený přístup k síťovým službám a aplikacím tím, že umožňuje těmto rozšířeným klientům nebo proxy serverům účastnit se toků ověřování založených na SAML.

Architektonicky se ECP integruje do širšího rámce zabezpečení a správy identit 3GPP, často komunikuje s prvky jako je infrastruktura Authentication, Authorization, and Accounting ([AAA](/mobilnisite/slovnik/aaa/)) nebo systémy správy identit. Entita ECP funguje jako zprostředkovatel, který může iniciovat požadavky SAML, zpracovávat odpovědi SAML obsahující bezpečnostní tvrzení a spravovat bezpečnostní kontext pro koncového uživatele nebo zařízení. Podporuje vazbu SOAP (Simple Object Access Protocol) pro SAML, což umožňuje výměnu zpráv SAML v obálkách SOAP, což je vhodné pro webové služby a komunikaci mezi stroji běžné v telekomunikačních sítích. To umožňuje klientům, které nejsou prohlížeče, jako jsou zařízení IoT nebo funkce síťové automatizace, bezpečně se ověřit a získat autorizační tokeny pro přístup k chráněným prostředkům.

Klíčové komponenty v interakci ECP zahrnují klienta ECP (entitu iniciující požadavek), poskytovatele identity (který ověřuje subjekt a vydává tvrzení SAML) a poskytovatele služeb (který tvrzení spotřebovává k udělení přístupu). Pracovní postup typicky zahrnuje odeslání SAML <AuthnRequest> od ECP k IdP, často prostřednictvím back-channel volání SOAP. IdP ověří subjekt (což může zahrnovat interakci s mechanismy ověřování specifickými pro 3GPP, jako je 5G [AKA](/mobilnisite/slovnik/aka/)) a vrátí SAML <Response> obsahující tvrzení s výroky o ověření a atributy. ECP poté toto tvrzení předloží SP pro přístup ke službě. Tento proces odděluje ověření od přístupu ke službě, podporuje scénáře federované identity napříč různými administrativními doménami, což je klíčové pro roamingová a více-dodavatelská síťová prostředí.

Role ECP v sítích 3GPP spočívá především v umožnění zabezpečené, standardizované federace identit pro klienty, kteří nejsou prohlížeče, což je stále důležitější s rozšiřováním IoT a automatizovaných síťových služeb. Poskytuje mechanismus, jak tito klienti mohou využít silné, síťové ověření (jako přihlašovací údaje z USIM) pro přístup k webovým službám bez nutnosti vlastních bezpečnostních protokolů. Použitím SAML zajišťuje interoperabilitu s existujícími ekosystémy správy identit a podporuje ochranu soukromí prostřednictvím použití pseudonymních identifikátorů a mechanismů souhlasu. Specifikace jako 3GPP TS 33.980 podrobně popisují jeho aplikaci ve scénářích, jako je zabezpečený přístup k síťovým [API](/mobilnisite/slovnik/api/) nebo frameworkům pro vystavování služeb.

## K čemu slouží

Enhanced Client or Proxy (ECP) byl zaveden, aby řešil omezení standardních profilů SAML Web Browser SSO, které jsou navrženy pro lidské uživatele komunikující prostřednictvím webových prohlížečů. V telekomunikacích je mnoho klientů stroje, zařízení nebo síťové funkce, které vyžadují automatizovaný, programový přístup ke službám. Tito klienti, kteří nejsou prohlížeče, neměli standardizovaný způsob, jak se účastnit ověřování založeného na SAML, což vedlo k proprietárním řešením a bezpečnostním mezerám. ECP poskytuje profil SAML specificky přizpůsobený pro tyto rozšířené klienty, což jim umožňuje bezpečně získávat a používat tvrzení SAML pro přístup k chráněným prostředkům.

Historicky, jak se sítě 3GPP vyvíjely směrem k architekturám založeným na službách a otevřeným [API](/mobilnisite/slovnik/api/) (např. v 4G EPC a 5G Core), rostla potřeba federované správy identit a přístupu. Služby jako vystavení sítě, přístup aplikací třetích stran a správa zařízení IoT vyžadovaly bezpečný, škálovatelný způsob ověřování a autorizace různorodých klientů. ECP jako součást standardu SAML nabídl osvědčený, XML framework, který mohl být integrován do bezpečnostní infrastruktury 3GPP. Řeší problém umožnění ověřování mezi stroji (M2M) a mezi službami pomocí stejných principů federace identit aplikovaných na lidské uživatele, čímž zajišťuje konzistenci a snižuje složitost.

Přijetím ECP mohou sítě 3GPP využít existujících poskytovatelů identity a služeb, kteří podporují SAML, což usnadňuje interoperabilitu v prostředích s více doménami, jako jsou roamingová partnerství nebo poskytování služeb založené na cloudu. Řeší bezpečnostní požadavky interakcí, které nejsou prohlížeče, podporou silných metod ověřování a zabezpečené výměny zpráv prostřednictvím SOAP, čímž zmírňuje rizika jako je vystavení přihlašovacích údajů. Tato motivace je v souladu s cíli 3GPP zvýšit bezpečnost, umožnit nové modely služeb a podporovat různorodý ekosystém klientů v moderních mobilních sítích.

## Klíčové vlastnosti

- Profil SAML 2.0 pro klienty, kteří nejsou prohlížeče
- Vazba SOAP pro zabezpečenou výměnu zpráv
- Podpora federované identity a jednotného přihlašování
- Integrace s mechanismy ověřování 3GPP
- Umožňuje ověřování mezi stroji (M2M)
- Interoperabilita s existujícími systémy správy identit

## Definující specifikace

- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz

---

📖 **Anglický originál a plná specifikace:** [ECP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecp/)
