---
slug: "sd-av"
url: "/mobilnisite/slovnik/sd-av/"
type: "slovnik"
title: "SD-AV – SIP Digest Authentication Vector"
date: 2025-01-01
abbr: "SD-AV"
fullName: "SIP Digest Authentication Vector"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sd-av/"
summary: "Sada kryptografických parametrů používaných v sítích 3GPP k ověřování uživatelů pro přístup k IMS prostřednictvím služeb založených na SIP. Umožňuje bezpečné, standardizované ověřování pro hlas, video"
---

SD-AV je sada kryptografických parametrů používaných v sítích 3GPP k ověřování uživatelů pro přístup k IMS prostřednictvím služeb založených na SIP, jako je hlas, video a zasílání zpráv přes IP.

## Popis

[SIP](/mobilnisite/slovnik/sip/) Digest Authentication Vector (SD-AV) je základní bezpečnostní konstrukce v architektuře IP Multimedia Subsystem (IMS) standardu 3GPP, konkrétně navržená pro ověřování uživatelského zařízení (UE), které se pokouší o přístup ke službám IMS. Funguje v rámci SIP (Session Initiation Protocol) digest ověřování, jak je definováno v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 3261 a profilováno 3GPP. SD-AV generuje Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) na žádost Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) během procedury registrace do IMS. Obsahuje klíčová kryptografická data typu challenge-response potřebná k ověření identity uživatele bez přenosu dlouhodobého tajemství uživatele (hesla) čitelného formou přes síť.

Samotný vektor se skládá z několika klíčových komponent, včetně nonce (náhodného čísla použitého jednou), domény ověřování (realm) a specifikace algoritmu. Zásadně obsahuje očekávanou hodnotu odpovědi, kterou vypočítá HSS pomocí sdíleného tajemství (uloženého v HSS a v [ISIM](/mobilnisite/slovnik/isim/) aplikaci UE) a parametrů výzvy. Když S-CSCF obdrží počáteční SIP REGISTER požadavek od UE, požádá HSS o SD-AV. S-CSCF poté odešle UE odpověď SIP 401 Unauthorized obsahující výzvu (nonce, realm atd.) ze SD-AV. UE použije své sdílené tajemství k výpočtu odpovědi a tuto odpověď zahrne do nového REGISTER požadavku. S-CSCF porovná vypočítanou odpověď od UE s očekávanou odpovědí ze SD-AV; shoda udělí přístup k IMS.

Tento mechanismus je nedílnou součástí procedur IMS Authentication and Key Agreement (IMS [AKA](/mobilnisite/slovnik/aka/)), přičemž SD-AV představuje metodu digest ověřování, která je alternativou k plnému IMS AKA založenému na autentizačních vektorech UMTS/LTE. Jeho úlohou je poskytnout robustní, standardizovanou metodu ověřování uživatelů pro služby založené na SIP, která tvoří první obrannou linii pro zabezpečení komunikace v IMS. Zajišťuje, že pouze legitimní účastníci mohou využívat síťové prostředky pro služby jako VoLTE, ViLTE a [RCS](/mobilnisite/slovnik/rcs/), čímž udržuje důvěrnost a integritu jádra IMS.

## K čemu slouží

SD-AV byl zaveden, aby řešil kritickou potřebu bezpečného ověřování uživatelů v plně IP prostředí pro poskytování služeb IP Multimedia Subsystem (IMS). Před IMS se okruhově přepínané hlasové služby spoléhaly na odlišné autentizační mechanismy vázané na okruhové jádro. Jak se sítě 3GPP vyvíjely k poskytování multimediálních služeb přes paketově přepínané sítě, byla vyžadována standardizovaná, nativně IP autentizační metoda. SIP, jakožto základní signalizační protokol pro IMS, potřeboval bezpečný autentizační mechanismus, který by se mohl integrovat s databází účastníků 3GPP (HSS) a fungovat v rámci architektury IMS.

Vytvoření SD-AV bylo motivováno omezeními přímého použití generického HTTP digest ověřování, kterému chyběla těsná integrace s bezpečnostními přihlašovacími údaji a síťovými funkcemi 3GPP. SD-AV poskytuje verzi profilovanou 3GPP, která zajišťuje interoperabilitu mezi UE, jádrem IMS (CSCF) a HSS. Řeší problém ověření identity uživatele pro registraci do IMS a zahájení relace, chrání před zosobněním a neoprávněným přístupem ke službám. Využitím sdíleného tajemství uloženého na ISIM poskytuje silný základ pro ověřování, aniž by vyžadoval, aby UE podporovalo plnou kryptografickou sadu IMS AKA, a nabízí tak životaschopnou alternativu pro určitá nasazení nebo typy zařízení.

## Klíčové vlastnosti

- Umožňuje SIP digest ověřování v rámci architektury IMS 3GPP
- Generován HSS a využit S-CSCF během registrace do IMS
- Obsahuje parametry výzvy (nonce, realm) a očekávanou hodnotu odpovědi
- Chrání dlouhodobé tajemství uživatele pomocí mechanismu challenge-response
- Integruje se s aplikací ISIM na UE pro ukládání přihlašovacích údajů a výpočet
- Poskytuje standardizovanou autentizační metodu jako alternativu k plnému IMS AKA

## Související pojmy

- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [ISIM – IMS Subscriber Identity Module](/mobilnisite/slovnik/isim/)

## Definující specifikace

- **TS 33.203** (Rel-19) — IMS Security Specification
- **TS 33.804** (Rel-12) — Non-UICC SSO using SIP Digest credentials

---

📖 **Anglický originál a plná specifikace:** [SD-AV na 3GPP Explorer](https://3gpp-explorer.com/glossary/sd-av/)
