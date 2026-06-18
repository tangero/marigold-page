---
slug: "oidc"
url: "/mobilnisite/slovnik/oidc/"
type: "slovnik"
title: "OIDC – OpenID Connect"
date: 2026-01-01
abbr: "OIDC"
fullName: "OpenID Connect"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oidc/"
summary: "OpenID Connect (OIDC) je vrstva identity postavená na OAuthu 2.0, která umožňuje bezpečné ověřování a autorizaci uživatelů v sítích 3GPP. Umožňuje aplikacím ověřit identitu uživatele a získat základní"
---

OIDC je vrstva identity postavená na OAuthu 2.0, která umožňuje bezpečné ověřování a autorizaci uživatelů v sítích 3GPP a umožňuje aplikacím ověřit identitu a získat základní informace o profilu.

## Popis

OpenID Connect (OIDC) je identitní protokol standardizovaný OpenID Foundation a přijatý 3GPP pro správu identit. Funguje jako tenká vrstva nad autorizačním rámcem OAuth 2.0, kterou přidává identitní vrstvu. OIDC umožňuje klientům (spoléhajícím stranám) ověřit identitu koncového uživatele na základě autentizace provedené autorizačním serverem (OpenID Provider) a získat základní informace o profilu koncového uživatele interoperabilním a REST-like způsobem. Ústřední součástí je ID Token, což je [JSON](/mobilnisite/slovnik/json/) Web Token ([JWT](/mobilnisite/slovnik/jwt/)) obsahující nároky (claims) týkající se autentizační události a uživatele. Tento token je autorizačním serverem podepsán a volitelně šifrován. Protokol používá standardní toky OAuth 2.0 (Authorization Code, Implicit, Hybrid) k získání těchto tokenů. V 3GPP je OIDC integrován, aby umožnil bezpečný přístup k síťovým [API](/mobilnisite/slovnik/api/) a uživatelským datům poskytovatelům aplikací třetích stran s využitím autentizačních schopností sítě. Architektura zahrnuje uživatelské zařízení (UE), spoléhající stranu (aplikační server) a síť 3GPP, která funguje jako nebo je integrována s OpenID Providerem. Protokol definuje koncové body pro discovery, autorizaci, vydávání tokenů a informace o uživateli, čímž zajišťuje standardizovaný způsob dosažení jednotného přihlášení a federace identit napříč službami.

## K čemu slouží

OIDC bylo zavedeno jako odpověď na potřebu moderního, standardizovaného a bezpečného identitního protokolu pro internetové autentizace v mobilních sítích. Před jeho přijetím se pro přístup třetích stran k síťovým autentizačním tvrzením používaly proprietární nebo méně interoperabilní metody. Růst webových a mobilních aplikací vyžadujících bezpečné přihlašování uživatelů a sdílení profilů si vyžádal řešení založené na otevřených standardech. OIDC tento problém řeší tím, že staví na široce přijímaném rámci OAuth 2.0 a poskytuje definovaný způsob předávání identitních informací. Jeho vznik motivoval posun průmyslu směrem k vystavení sítě přes [API](/mobilnisite/slovnik/api/) (např. přes [SCEF](/mobilnisite/slovnik/scef/), [NEF](/mobilnisite/slovnik/nef/)) a potřeba bezpečně autorizovat aplikace třetích stran pro přístup k síťovým službám a uživatelským datům bez sdílení přihlašovacích údajů. Řeší omezení předchozích přístupů založených na [SAML](/mobilnisite/slovnik/saml/) tím, že je odlehčenější, založený na [JSON](/mobilnisite/slovnik/json/) a vhodný pro mobilní a RESTful API prostředí.

## Klíčové vlastnosti

- Vrstva identity na OAuthu 2.0
- ID Token jako podepsaný JWT
- UserInfo koncový bod pro data profilu
- Standardizovaný mechanismus discovery
- Podpora více toků (Code, Implicit, Hybrid)
- Schopnosti správy relací

## Související pojmy

- [JWT – JSON Web Token](/mobilnisite/slovnik/jwt/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 24.482** (Rel-19) — Mission Critical Services Identity Management
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.879** (Rel-13) — MCPTT Security Study

---

📖 **Anglický originál a plná specifikace:** [OIDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/oidc/)
