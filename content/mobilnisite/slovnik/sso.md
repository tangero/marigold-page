---
slug: "sso"
url: "/mobilnisite/slovnik/sso/"
type: "slovnik"
title: "SSO – Single Sign-On"
date: 2026-01-01
abbr: "SSO"
fullName: "Single Sign-On"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sso/"
summary: "Single Sign-On (SSO) je mechanismus autentizace uživatele, který umožňuje uživateli přístup k více aplikacím nebo službám s jedinou sadou přihlašovacích údajů. Zvyšuje uživatelský komfort a bezpečnost"
---

SSO (Single Sign-On) je mechanismus autentizace uživatele, který umožňuje přístup k více síťovým a službám třetích stran s jedinou sadou přihlašovacích údajů, čímž zvyšuje pohodlí a bezpečnost.

## Popis

Single Sign-On (SSO) v 3GPP je bezpečnostní rámec, který umožňuje uživateli provést autentizaci jednou a získat přístup k více, potenciálně nezávislým službám, aniž by bylo nutné se pro každou službu znovu přihlašovat. Funguje na principu vytvoření vztahu důvěry mezi poskytovatelem identity (IdP) a různými poskytovateli služeb ([SP](/mobilnisite/slovnik/sp/)). Základní mechanismus spočívá v tom, že IdP po úspěšné počáteční autentizaci vydá bezpečnostní token nebo tvrzení, které je následně předloženo SP pro udělení přístupu. Tento token, často založený na standardech jako Security Assertion Markup Language ([SAML](/mobilnisite/slovnik/saml/)) nebo OAuth, obsahuje ověřená tvrzení o identitě uživatele.

Architektura typicky zahrnuje zařízení uživatele, domácí síť fungující jako nebo integrovanou s IdP a externí poskytovatele služeb. Když se uživatel pokusí o přístup ke službě, je v případě neexistence platné relace přesměrován k IdP k autentizaci. IdP autentizuje uživatele pomocí přihlašovacích údajů, jako je metoda založená na [SIM](/mobilnisite/slovnik/sim/) kartě (např. Generic Bootstrapping Architecture - [GBA](/mobilnisite/slovnik/gba/)), uživatelské jméno/heslo nebo certifikát. Po úspěchu IdP vygeneruje podepsané tvrzení a přesměruje uživatele zpět k poskytovateli služby s tímto tokenem. SP před udělením přístupu ověří podpis tvrzení a důvěryhodnost IdP.

Klíčové komponenty zahrnují Autentizační proxy, která zpracovává přesměrování a výměnu tokenů, a SSO Server v rámci IdP, který spravuje uživatelské autentizační relace a vydávání tokenů. Rámec se opírá o zabezpečené protokoly pro komunikaci, jako je [HTTPS](/mobilnisite/slovnik/https/), a definovaná rozhraní mezi IdP a SP. Jeho úlohou v síti je zjednodušit přístup ke službám, zejména pro služby IP Multimedia Subsystem (IMS), aplikace třetích stran a portály operátorů sítí, při zachování konzistentního bezpečnostního postavení.

Integrace SSO v 3GPP často využívá stávající bezpečnostní infrastruktury, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro data uživatelského profilu a Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)) pro dohodu klíčů při autentizaci založené na GBA. To umožňuje silnou, sítí podporovanou autentizaci, kterou lze znovu použít napříč službami. Systém podporuje scénáře federované identity, kdy IdP a SP patří do různých administrativních domén, což umožňuje přístup ke službám napříč doménami bez kompromitace bezpečnosti.

## K čemu slouží

SSO bylo zavedeno, aby řešilo rostoucí složitost a bezpečnostní výzvy spojené se správou více přihlašovacích údajů pro různé služby v mobilních sítích. Před SSO uživatelé často potřebovali samostatná uživatelská jména a hesla pro každou službu, což vedlo k únavě z hesel, slabým zvyklostem při tvorbě hesel a zvýšeným nákladům na podporu pro obnovu přihlašovacích údajů. Tento roztříštěný přístup také představoval bezpečnostní rizika, protože kompromitované přihlašovací údaje pro jednu službu nebylo možné centrálně spravovat nebo zneplatnit napříč ostatními.

Motivace pro SSO v 3GPP vycházela z rozšíření nabídky služeb mimo základní hlas a [SMS](/mobilnisite/slovnik/sms/) o služby založené na IMS (jako VoLTE), aplikace třetích stran a podniková řešení. Byl potřebný standardizovaný mechanismus SSO, aby poskytoval bezproblémový a bezpečný uživatelský zážitek a podporoval přijetí služeb. Umožňuje síťovým operátorům využít jejich silné autentizační prostředky (jako je SIM karta) k umožnění bezpečného přístupu k externím službám, čímž vytváří nové obchodní modely a partnerství.

Historicky vyvíjely rané internetové služby proprietární řešení SSO, což vedlo k problémům s interoperabilitou. 3GPP standardizovalo SSO, aby zajistilo konzistenci napříč mobilními ekosystémy a umožnilo operátorům nabízet jednotný přihlašovací zážitek. Řeší problém opakovaných výzev k autentizaci, které zhoršují uživatelský zážitek, a zvyšuje bezpečnost snížením prostoru pro útok spojeného s více úložišti hesel. Centralizací autentizace také zjednodušuje soulad s regulatorními požadavky na správu identit.

## Klíčové vlastnosti

- Centralizovaná autentizace prostřednictvím důvěryhodného poskytovatele identity (IdP)
- Podpora federované identity napříč různými administrativními doménami
- Opětovné použití silných síťových autentizačních metod (např. založených na SIM kartě prostřednictvím GBA)
- Vydávání a ověřování bezpečnostních tokenů/tvrzení (např. SAML)
- Snížení únavy z hesel a zlepšení uživatelského komfortu
- Vylepšená bezpečnost díky centralizované správě a zneplatňování přihlašovacích údajů

## Definující specifikace

- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.258** (Rel-7) — All-IP Network Service Requirements
- **TS 22.895** (Rel-12) — 3GPP SSO Framework Integration Study
- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 33.804** (Rel-12) — Non-UICC SSO using SIP Digest credentials
- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines
- **TR 33.995** (Rel-19) — Study on SSO Security Integration with 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [SSO na 3GPP Explorer](https://3gpp-explorer.com/glossary/sso/)
