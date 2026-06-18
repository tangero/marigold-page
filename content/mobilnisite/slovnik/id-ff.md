---
slug: "id-ff"
url: "/mobilnisite/slovnik/id-ff/"
type: "slovnik"
title: "ID-FF – Identity Federation Framework"
date: 2025-01-01
abbr: "ID-FF"
fullName: "Identity Federation Framework"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/id-ff/"
summary: "Rámec, jak jej profiloval projekt Liberty Alliance (LAP), který umožňuje bezpečnou federaci identit napříč různými administrativními doménami a poskytovateli služeb. Umožňuje uživatelům používat jedin"
---

ID-FF je rámec projektu Liberty Alliance, který umožňuje bezpečnou federaci identit napříč různými doménami, takže uživatelé mohou přistupovat k více službám s jedinou sadou přihlašovacích údajů.

## Popis

Identity Federation Framework (ID-FF) je soubor specifikací, původně vyvinutý projektem Liberty Alliance ([LAP](/mobilnisite/slovnik/lap/)), který 3GPP přijalo a profilovalo pro použití v mobilních sítích, zejména v rámci IP Multimedia Subsystem (IMS). Jeho hlavní funkcí je vytvoření důvěryhodného rámce pro federaci identit, jednotné přihlašování ([SSO](/mobilnisite/slovnik/sso/)) a webové služby založené na identitě. Federace je proces propojení digitální identity uživatele napříč více různými systémy správy identit, který umožňuje, aby ověření provedené v jedné doméně (poskytovatel identity, IdP) bylo důvěryhodné a přijaté v jiné doméně (poskytovatel služeb, [SP](/mobilnisite/slovnik/sp/)).

Z architektonického hlediska ID-FF definuje role jako Subjekt (uživatel), Poskytovatel identity (IdP) a Poskytovatel služeb (SP). Specifikuje protokoly a schémata pro vytváření federovaných identit, správu identifikátorů jmen a šíření autentizačních tvrzení. Klíčovou součástí je použití tvrzení Security Assertion Markup Language ([SAML](/mobilnisite/slovnik/saml/)), což jsou tokeny založené na [XML](/mobilnisite/slovnik/xml/), které přenášejí výroky o ověření a autorizaci subjektu. Rámec definuje, jak se tato tvrzení vytvářejí, podepisují a vyměňují mezi IdP a SP za účelem vytvoření bezpečnostního kontextu bez nutnosti opětovného ověření uživatele.

Jak to funguje: začíná to, když se uživatel pokusí přistoupit ke službě u SP. Pokud uživatel nemá místní účet, může SP přesměrovat jeho požadavek na důvěryhodného IdP (s nímž je uživatelova identita federována). IdP uživatele ověří (např. pomocí autentizace založené na [SIM](/mobilnisite/slovnik/sim/) kartě v kontextu 3GPP) a poté vygeneruje podepsané SAML tvrzení obsahující ověřenou identitu a atributy uživatele. Toto tvrzení je doručeno zpět SP, a to buď prostřednictvím prohlížeče uživatele (vazba artifact nebo POST), nebo přes back-channel. SP ověří podpis tvrzení a důvěryhodný vztah s IdP a poté uživateli udělí přístup na základě deklarované identity. Tento proces umožňuje bezproblémový přístup napříč doménami.

V ekosystému 3GPP, zejména pro služby založené na IMS, je ID-FF klíčové pro umožnění poskytovatelům služeb mimo přímou kontrolu mobilního operátora (např. poskytovatelům aplikací třetích stran) využívat silné ověření poskytované sítí operátora. Síť 3GPP zde funguje jako silný IdP a využívá přihlašovací údaje uložené na UICC (SIM kartě). To uživatelům umožňuje přistupovat k široké škále webových a IMS služeb s konzistentní, bezpečnou identitou odvozenou od jejich mobilního předplatného, což zlepšuje jak uživatelský zážitek, tak bezpečnost.

## K čemu slouží

Účelem ID-FF v 3GPP je vyřešit problém izolovaných identit a roztříštěného přihlašování uživatelů v rostoucím světě mobilního internetu a služeb IMS. Před federací museli uživatelé udržovat samostatná uživatelská jména a hesla pro každého poskytovatele služeb, což vedlo ke špatné uživatelské zkušenosti, únavě z hesel a slabším bezpečnostním praktikám (např. opakované používání hesla). Pro poskytovatele služeb bylo implementování a správa vlastních autentizačních systémů nákladné a složité.

Přijetí ID-PP ze strany 3GPP bylo motivováno potřebou využít inherentní silné autentizační schopnosti mobilní sítě (založené na [SIM](/mobilnisite/slovnik/sim/) kartě) pro služby přesahující základní přístup k síti. Umožňuje mobilním operátorům stát se důvěryhodnými zprostředkovateli identit. To vytváří nové obchodní modely, jako je identita jako služba, a umožňuje bezpečný a pohodlný přístup k množství služeb třetích stran – od streamování a her po podnikové aplikace – s využitím mobilní identity jako klíče.

Řeší omezení předchozích ad-hoc nebo proprietárních řešení jednotného přihlašování tím, že poskytuje standardizovaný, interoperabilní rámec založený na otevřených specifikacích (Liberty Alliance/[SAML](/mobilnisite/slovnik/saml/)). Tato standardizace je klíčová pro vytvoření škálovatelného ekosystému, kde se může jakýkoli poskytovatel služeb integrovat s jakoukoli platformou identit operátora. Dále zlepšuje ochranu soukromí prostřednictvím mechanismů, jako jsou pseudonymní identifikátory a souhlas uživatele se sdílením atributů, což uživatelům dává kontrolu nad tím, jak se jejich identifikační informace šíří napříč různými službami.

## Klíčové vlastnosti

- Umožňuje federaci identit mezi různými administrativními doménami (IdP a SP)
- Podporuje jednotné přihlašování (SSO), čímž snižuje opakované výzvy k ověření
- Využívá tvrzení založená na SAML pro bezpečný přenos výroků o ověření a atributech
- Definuje protokoly pro vytvoření federace, jednotné odhlášení a správu identifikátorů jmen
- Umožňuje mobilnímu síťovému operátorovi fungovat jako silný poskytovatel identity (IdP)
- Podporuje ochranu soukromí použitím neprůhledných, párových pseudonymních identifikátorů pro uživatele

## Související pojmy

- [ID-WSF – Identity Web Services Framework](/mobilnisite/slovnik/id-wsf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [ID-FF na 3GPP Explorer](https://3gpp-explorer.com/glossary/id-ff/)
