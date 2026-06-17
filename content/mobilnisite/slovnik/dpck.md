---
slug: "dpck"
url: "/mobilnisite/slovnik/dpck/"
type: "slovnik"
title: "DPCK – MCData Payload Cipher Key"
date: 2026-01-01
abbr: "DPCK"
fullName: "MCData Payload Cipher Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dpck/"
summary: "DPCK je kryptografický klíč používaný ve službách Mission Critical Data (MCData) podle 3GPP k šifrování a dešifrování uživatelských dat datových zpráv. Zajišťuje důvěrnost citlivých informací vyměňova"
---

DPCK je kryptografický klíč používaný ve službách Mission Critical Data (MCData) podle 3GPP k šifrování a dešifrování uživatelských dat datových zpráv, čímž zajišťuje důvěrnost komunikací pro veřejnou bezpečnost.

## Popis

MCData Payload Cipher Key (DPCK) je bezpečnostní klíč definovaný v architektuře 3GPP pro služby Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)). Je generován a spravován jako součást hierarchie klíčů vytvořené během procedur autentizace a dohody o klíčích mezi uživatelským zařízením (UE) a sítí. DPCK je konkrétně odvozen pro použití s aplikacemi MCData za účelem poskytnutí ochrany důvěrnosti pro uživatelská dat (uživatelská data) zpráv MCData, jako jsou ty používané při přenosu souborů, textových zpráv nebo datových streamů v rámci operací veřejné bezpečnosti.

Provozně je DPCK používán kryptografickými funkcemi v UE a na aplikačním serveru MCData. Když uživatel MCData odešle zabezpečenou zprávu, aplikační vrstva použije DPCK (spolu se specifikovaným šifrovacím algoritmem) k zašifrování uživatelských dat zprávy před přenosem. Příslušný příjemcův UE, který disponuje stejným DPCK (který byl distribuován prostřednictvím zabezpečených protokolů pro správu klíčů), jej použije k dešifrování uživatelských dat po přijetí. Samotný klíč není s právou přenášen. Konkrétní šifrovací algoritmy (např. založené na [AES](/mobilnisite/slovnik/aes/)) jsou definovány v bezpečnostních specifikacích 3GPP.

DPCK existuje v rámci širší hierarchie klíčů. Typicky je odvozen z dlouhodobějšího kotvícího klíče, jako je KMCData, který je sám vytvořen z primárních autentizačních klíčů. K tomuto odvození se používají standardizované funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)). Životní cyklus DPCK – včetně jeho generování, distribuce, používání a zrušení – je řízen bezpečnostními funkcemi v systému MCData, často za účasti funkce pro správu klíčů (KMF) nebo analogických entit. Oddělení klíče pro šifrování uživatelských dat (DPCK) od klíčů pro ochranu signalizace je principem bezpečnostní segregace, který omezuje dopad případného kompromitování klíče.

## K čemu slouží

DPCK byl zaveden se službami 3GPP Mission Critical Data ve vydání 14, aby řešil přísné bezpečnostní požadavky komunikací veřejné bezpečnosti a kritických komunikací. Tradiční zabezpečení komerčních mobilních dat (např. v EPS) primárně chrání uživatelskou rovinu mezi UE a sítí pomocí klíčů jako je [CK](/mobilnisite/slovnik/ck/) (Ciphering Key). Služby [MC](/mobilnisite/slovnik/mc/) však vyžadují zabezpečení na aplikační vrstvě od konce ke konci pro skupinovou komunikaci, které zajišťuje důvěrnost i v rámci domény core sítě a aplikačního serveru.

Jeho zavedení bylo motivováno potřebou vyhrazeného, na službu specifického kryptografického klíče pro důvěrnost uživatelských dat MCData. Tento přístup poskytuje větší flexibilitu a bezpečnost ve srovnání s opětovným používáním stávajících klíčů přístupové vrstvy. Umožňuje nezávislou správu klíčů pro aplikaci MCData, což umožňuje funkce jako dopředné utajení (kdy kompromitovaný dlouhodobý klíč neohrozí minulou komunikaci) a možnost změny klíče pro šifrování uživatelských dat bez opětovné autentizace UE v přístupové síti. DPCK umožňuje zabezpečenou výměnu citlivých operačních dat (např. map, plánů budov, informací o pacientech) mezi záchranáři, což je základním požadavkem moderních operací kritických pro plnění úkolu.

## Klíčové vlastnosti

- Zajišťuje důvěrnost pro uživatelská dat aplikací MCData
- Odvozen z kotvícího klíče služby MCData (KMCData) jako součást hierarchie klíčů
- Používán se standardizovanými šifrovacími algoritmy (např. AES) v definovaných režimech
- Spravován a distribuován prostřednictvím zabezpečených protokolů pro správu klíčů (např. přes KMF)
- Umožňuje zabezpečení na aplikační vrstvě od konce ke konci pro data kritická pro plnění úkolu
- Podporuje bezpečnostní segregaci oddělením ochrany uživatelských dat od ochrany signalizace

## Definující specifikace

- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service

---

📖 **Anglický originál a plná specifikace:** [DPCK na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpck/)
