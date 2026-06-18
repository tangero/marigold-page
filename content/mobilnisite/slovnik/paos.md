---
slug: "paos"
url: "/mobilnisite/slovnik/paos/"
type: "slovnik"
title: "PAOS – Reversed HTTP binding for SOAP"
date: 2025-01-01
abbr: "PAOS"
fullName: "Reversed HTTP binding for SOAP"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/paos/"
summary: "PAOS je vazba SOAP, která obrací typické role HTTP klienta a serveru a umožňuje serveru odesílat SOAP požadavky klientovi. Je definována v 3GPP pro použití s protokoly Liberty Alliance Project (LAP) a"
---

PAOS je reverzní HTTP vazba pro SOAP, která umožňuje serveru odesílat SOAP požadavky klientovi, čímž umožňuje zabezpečené asynchronní interakce služeb v mobilních sítích 3GPP.

## Popis

PAOS (reverzní [HTTP](/mobilnisite/slovnik/http/) vazba pro [SOAP](/mobilnisite/slovnik/soap/)) je specifikace vazby protokolu, která obrací konvenční model HTTP požadavek-odpověď pro webové služby založené na SOAP. Ve standardním SOAP přes HTTP klient iniciuje HTTP požadavek obsahující SOAP obálku a server odpovídá HTTP odpovědí obsahující další SOAP obálku. PAOS toto obrací: server může odeslat HTTP odpověď, která sama obsahuje SOAP požadavek, a klient poté reaguje následným HTTP požadavkem obsahujícím SOAP odpověď. Tento mechanismus je formálně definován v 3GPP TS 33.980, který profiluje jeho použití pro protokoly Liberty Alliance Project ([LAP](/mobilnisite/slovnik/lap/)) a [SAML](/mobilnisite/slovnik/saml/) (Security Assertion Markup Language), zejména ve scénářích zahrnujících federaci identit a jednotné přihlašování ([SSO](/mobilnisite/slovnik/sso/)).

Z architektonického hlediska PAOS funguje v rámci víceúčastnického modelu důvěry. Klíčovým případem použití je jednotné přihlašování iniciované poskytovatelem identity (IdP) směrem k poskytovateli služby ([SP](/mobilnisite/slovnik/sp/)). Zde prohlížeč uživatele funguje jako HTTP klient. IdP, který v počáteční transakci vystupuje jako HTTP server, může vložit SOAP požadavek do své HTTP odpovědi prohlížeči. Prohlížeč pak podle pravidel vazby PAOS tento SOAP požadavek přepošle prostřednictvím nového HTTP požadavku na cílového SP. To umožňuje IdP asynchronně zasílat ověřovací aserce nebo dotazy na atributy přímo SP prostřednictvím uživatelského agenta, aniž by SP musel IdP dotazovat.

Fungování protokolu závisí na specifických HTTP hlavičkách a SOAP action [URI](/mobilnisite/slovnik/uri/), které označují reverzní vazbu. Počáteční HTTP odpověď ze serveru (např. IdP) obsahuje hlavičku jako `PAOS` s hodnotou identifikující podporované verze a funkce. SOAP obálka uvnitř této odpovědi je legitimní požadavek, který musí klient přeposlat. Tento návrh je klíčový pro umožnění plynulých a bezpečných interakcí ve scénářích federované identity definovaných v rámcích Liberty Alliance [ID-FF](/mobilnisite/slovnik/id-ff/) a ID-WSF, které byly integrovány do architektury Generic Bootstrapping Architecture (GBA) 3GPP a do raných mechanismů autentizace multimediálních služeb. PAOS umožňuje standardizovaný způsob komunikace autentizačních a autorizačních dat mezi síťovými entitami na pozadí, což zlepšuje uživatelský zážitek umožněním transparentního přístupu ke službám napříč různými doménami.

## K čemu slouží

PAOS byl vytvořen, aby vyřešil základní omezení standardního modelu interakce SOAP založeného na HTTP pro specifické scénáře federované identity a zabezpečených služeb. V tradičních webových službách typu klient-server dialog vždy iniciuje klient. Nicméně v protokolech federace identit, jako jsou ty od Liberty Alliance, existuje potřeba, aby poskytovatel identity (IdP) proaktivně komunikoval s poskytovatelem služby (SP) prostřednictvím uživatelského prohlížeče. Například během toku jednotného přihlašování potřebuje IdP po ověření uživatele odeslat SAML aserci SP, aby mu udělil přístup. Standardní HTTP přesměrování s tokenem zakódovaným v URL je jedna metoda, ale PAOS poskytuje strukturovanější, rozšiřitelnější a na SOAP založenou alternativu, která může přenášet bohatší, podepsané XML datové části.

Historický kontext představuje konvergence webových služeb a telekomunikací na počátku 21. století, kdy se 3GPP snažilo integrovat správu identit založenou na internetu do mobilních sítí. Projekt Liberty Alliance vyvinul specifikace pro federovanou identitu a 3GPP je přijalo a profilovalo ve své bezpečnostní architektuře, zejména pro GBA a ranou autentizaci služeb IMS (IP Multimedia Subsystem). Standardní vazba SOAP-over-HTTP byla nedostatečná, protože vyžadovala, aby SP (konečný příjemce autentizačních dat) vystupoval jako HTTP klient a dotazoval se IdP. PAOS to elegantně řeší tím, že umožňuje IdP 'posunout' SOAP požadavek prostřednictvím uživatelského agenta, což umožňuje přímou, zabezpečenou a synchronní výměnu mezi IdP a SP bez složitých backendových spojení, zjednodušuje nasazení a zvyšuje bezpečnost tím, že udržuje aserce v řízených SOAP zprávách.

## Klíčové vlastnosti

- Obrácení standardních rolí HTTP klienta a serveru pro zasílání zpráv SOAP
- Umožňuje doručování SOAP požadavků iniciovaných serverem prostřednictvím klientského agenta
- Definováno pro použití s protokoly Liberty Alliance Project (LAP) a SAML
- Podporuje asynchronní, push-based toky autentizace a autorizace
- Využívá specifické HTTP hlavičky (např. PAOS hlavičku) k vyjednání a označení vazby
- Usnadňuje federovanou identitu a jednotné přihlašování v architekturách síťových služeb 3GPP

## Související pojmy

- [SOAP – Simple Object Access Protocol](/mobilnisite/slovnik/soap/)
- [SAML – Security Assertion Markup Language](/mobilnisite/slovnik/saml/)
- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [PAOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/paos/)
