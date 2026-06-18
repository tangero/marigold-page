---
slug: "id-wsf"
url: "/mobilnisite/slovnik/id-wsf/"
type: "slovnik"
title: "ID-WSF – Identity Web Services Framework"
date: 2025-01-01
abbr: "ID-WSF"
fullName: "Identity Web Services Framework"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/id-wsf/"
summary: "Webový služební framework profilovaný z projektu Liberty Alliance, který definuje standardizované protokoly pro bezpečné a soukromí respektující vyhledávání, volání a správu webových služeb souvisejíc"
---

ID-WSF je webový služební framework profilovaný Liberty Alliance, který definuje standardizované protokoly pro bezpečné a soukromí respektující vyhledávání, volání a správu webových služeb souvisejících s identitou.

## Popis

Identity Web Services Framework (ID-WSF) je komplexní soubor specifikací, rovněž pocházejících z projektu Liberty Alliance ([LAP](/mobilnisite/slovnik/lap/)) a přijatých konsorciem 3GPP, který staví na Identity Federation Framework ([ID-FF](/mobilnisite/slovnik/id-ff/)). Zatímco ID-FF řeší federaci a autentizaci, ID-WSF poskytuje infrastrukturu pro bezpečný, autorizovaný a na soukromí dbající přístup k webovým službám, které zpřístupňují nebo spotřebovávají informace související s identitou. V podstatě definuje architekturu orientovanou na služby ([SOA](/mobilnisite/slovnik/soa/)) pro data identity, což aplikacím umožňuje interagovat s uživatelským profilem, preferencemi nebo dalšími atributy uloženými u různých poskytovatelů.

Z architektonického hlediska zavádí ID-WSF klíčové role: Subjekt (uživatel), Poskytovatel identity (IdP), Poskytovatelé služeb ([SP](/mobilnisite/slovnik/sp/)) a Služby objevování. Ústředním konceptem je Služba identity, což je webová služba poskytující přístup k nějakému aspektu dat identity subjektu (např. služba adresáře kontaktů, služba stavu dostupnosti, lokalizační služba). Framework specifikuje základní komponenty: Službu objevování ([DS](/mobilnisite/slovnik/ds/)), která funguje jako registr pro zjištění, jaké služby identity jsou pro daného uživatele dostupné a jak k nim přistupovat; vazbu na bázi [SOAP](/mobilnisite/slovnik/soap/) s WS-Security pro zabezpečenou výměnu zpráv; a podrobné protokoly pro volání služeb, autorizaci a správu souhlasu.

Jeho fungování zahrnuje několik kroků. Nejprve klientská aplikace (tzv. WSF Relying Party) potřebuje přístup k uživatelské službě identity. Obrátí se na uživatelovu Službu objevování (často hostovanou IdP), předloží bezpečnostní token (např. [SAML](/mobilnisite/slovnik/saml/) assertion z ID-FF). DS po ověření tokenu a kontrole autorizačních politik vrátí referenci na koncový bod služby ([URL](/mobilnisite/slovnik/url/)) a nezbytné bezpečnostní požadavky pro přístup k požadované službě identity. Klient pak tuto službu přímo volá pomocí zpráv SOAP zabezpečených pomocí WS-Security, v souladu s uživatelskými preferencemi soukromí a pravidly řízení přístupu služby. Tím je odděleno objevování služeb od jejich volání a je vynuceno uživatelsky orientované řízení.

V kontextu 3GPP je ID-WSF profilován tak, aby bezproblémově spolupracoval s autentizací 3GPP a frameworkem ID-FF. Umožňuje mobilním síťovým operátorům zpřístupňovat data účastníků (s výslovným souhlasem uživatele) důvěryhodným poskytovatelům aplikací třetích stran kontrolovaným a standardizovaným způsobem. Například uživatel může navigační aplikaci udělit oprávnění pro přístup k její hrubé lokalizaci odvozené ze sítě prostřednictvím standardizované lokalizační služby ID-WSF, aniž by aplikace potřebovala přímý proprietární přístup k síťovým uzlům. To vytváří bohatý ekosystém služeb využívajících identitu při zachování bezpečnosti a soukromí uživatele.

## K čemu slouží

Účelem ID-WSF je řešit výzvu bezpečného a programového přístupu k distribuovaným informacím o identitě ve světě orientovaném na služby. Před existencí takových frameworků aplikace, které potřebovaly uživatelská data (jako kontakty nebo polohu), buď musela tato data sama ukládat (což vytvářelo datová úložiště a redundanci), nebo vyvíjet vlastní křehká propojení s každým zdrojem dat (jako je síť mobilního operátora). To bylo neefektivní, nezabezpečené a uživatelům poskytovalo malou kontrolu nad tím, jak jsou jejich data sdílena.

Profilace ID-WSF v rámci 3GPP byla vedena vizí mobilního operátora jako důvěryhodného centra pro identitu a osobní data. Umožňuje operátorům vytvářet nové zdroje příjmů tím, že mohou nabízet data identity jako službu třetím stranám. Vývojářům aplikací poskytuje standardizovaný, jednotný framework podobný API pro přístup k bohatému kontextu uživatelských informací (s oprávněním), což zjednodušuje vývoj a umožňuje bohatší a personalizovanější služby.

Řeší kritické problémy interoperability a soukromí. Standardizací protokolů pro objevování služeb, jejich volání a zabezpečení umožňuje, aby jakákoli kompatibilní služba (od jakéhokoli poskytovatele) byla objevena a použita jakýmkoli kompatibilním klientem. Jeho vestavěné mechanismy souhlasu a autorizace staví uživatele do role rozhodujícího činitele, vyžadují výslovné povolení pro sdílení dat a umožňují jim nastavovat podrobná pravidla. Tento uživatelsky orientovaný model byl klíčovým pokrokem oproti předchozím, více na poskytovatele orientovaným modelům přístupu k datům.

## Klíčové vlastnosti

- Definuje standardizovaný framework pro objevování a volání webových služeb souvisejících s identitou
- Ústřední role Služby objevování (DS) pro dynamické vyhledávání koncových bodů služeb
- Používá standardy SOAP/WS-* s WS-Security pro zabezpečenou a spolehlivou výměnu zpráv
- Začleňuje robustní mechanismy autorizace a souhlasu uživatele pro kontrolu soukromí
- Umožňuje mobilnímu operátorovi hostovat a nabízet služby identity (např. profil, lokalizaci)
- Podporuje interoperabilitu oddělením spotřebitelů služeb od jejich poskytovatelů prostřednictvím DS

## Související pojmy

- [ID-FF – Identity Federation Framework](/mobilnisite/slovnik/id-ff/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [ID-WSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/id-wsf/)
