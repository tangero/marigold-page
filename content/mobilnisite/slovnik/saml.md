---
slug: "saml"
url: "/mobilnisite/slovnik/saml/"
type: "slovnik"
title: "SAML – Security Assertion Markup Language"
date: 2025-01-01
abbr: "SAML"
fullName: "Security Assertion Markup Language"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/saml/"
summary: "Security Assertion Markup Language (SAML) je otevřený standard založený na XML pro výměnu autentizačních a autorizačních dat mezi stranami, konkrétně mezi poskytovatelem identity (IdP) a poskytovatele"
---

SAML je otevřený standard založený na XML pro výměnu autentizačních a autorizačních dat mezi poskytovatelem identity a poskytovatelem služeb, který je v 3GPP profilován pro federovanou správu identit a jednotné přihlašování (single sign-on).

## Popis

SAML je protokol, který používá [XML](/mobilnisite/slovnik/xml/) dokumenty nazývané aserce (assertions) k předávání bezpečnostních informací. V kontextu 3GPP je profilován tak, aby umožňoval federovanou identitu a jednotné přihlašování napříč administrativními doménami, například mezi operátorem mobilní sítě (vystupujícím jako Poskytovatel identity – IdP) a poskytovatelem aplikací nebo služeb třetí strany ([SP](/mobilnisite/slovnik/sp/)). Základními komponentami jsou Subjekt (uživatel), IdP (který uživatele autentizuje a generuje aserce) a SP (který se spoléhá na aserci od IdP při udělování přístupu). Tok protokolu typicky zahrnuje přesměrování prostřednictvím prohlížeče uživatele. Když se uživatel pokusí získat přístup ke službě u SP, SP vygeneruje SAML žádost o autentizaci a přesměruje uživatele na IdP. IdP uživatele autentizuje (často pomocí síťových autentizačních mechanismů, jako je autentizace založená na [SIM](/mobilnisite/slovnik/sim/) kartě) a poté vytvoří SAML odpověď obsahující aserci. Tato aserce, která je digitálně podepsána IdP, obsahuje tvrzení o autentizačním stavu uživatele, jeho atributech (např. identifikátor účastníka) a autorizačních rozhodnutích.

SAML odpověď je odeslána zpět do prohlížeče uživatele, který ji postuje na koncový bod služby pro příjem asercí (assertion consumer service) SP. SP ověří podpis IdP a podmínky aserce (např. časová razítka, zamýšlený příjemce). Po úspěšném ověření SP pro uživatele vytvoří lokální relaci a udělí přístup k požadované službě bez nutnosti samostatného přihlášení. Tím je oddělena aplikační logika služby od autentizačního mechanismu. Specifikace 3GPP TS 33.980 definuje specifický profil SAML 2.0 pro použití v IP Multimedia Subsystem (IMS) a dalších síťových službách. Podrobně popisuje, jak se používají SAML vazby (bindings, např. [HTTP](/mobilnisite/slovnik/http/) Redirect a POST), jak mapovat identifikátory účastníků 3GPP do SAML atributů a jak integrovat SAML s rámcem 3GPP Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)).

Tato integrace umožňuje výkonné případy užití, například když účastník použije svou identitu z mobilní sítě k plynulému přihlášení ke partnerské službě streamování videa nebo podnikové aplikaci, a využije tak silnou autentizaci mobilní sítě založenou na SIM kartě. SP důvěřuje IdP operátora, čímž vzniká federovaná doména důvěry, která zjednodušuje uživatelský zážitek a zvyšuje bezpečnost díky centralizaci autentizace u silné a důvěryhodné entity.

## K čemu slouží

SAML byl přijat 3GPP k řešení problému federace identit a zjednodušení přístupu ke službám napříč různými doménami důvěry. Jak se mobilní sítě vyvíjely v platformy služeb, rostla potřeba, aby se účastníci mohli přihlašovat k široké škále aplikací třetích stran (např. cloudové služby, obsahové portály) bez nutnosti spravovat mnoho samostatných uživatelských jmen a hesel. Tradiční metody vyžadovaly, aby poskytovatel služeb autentizaci zajišťoval přímo, což mohlo být méně bezpečné a vést ke špatnému uživatelskému zážitku.

Hlavním účelem profilování SAML v rámci 3GPP bylo využít silné autentizační prostředky operátora ([SIM](/mobilnisite/slovnik/sim/) kartu a domovskou síť) jako univerzální identifikační údaj. To umožňuje jednotné přihlašování ([SSO](/mobilnisite/slovnik/sso/)), kdy uživatel autentizovaný jednou své domovskou sítí může přistupovat k více externím službám. Řeší to omezení, jako je únava z hesel, slabá autentizace u poskytovatelů služeb a složitost zřizování uživatelských účtů napříč více službami. Pro operátory to vytváří novou hodnotu tím, že jim umožňuje vystupovat jako zprostředkovatel identit (Identity Broker). Pro poskytovatele služeb to znamená přesunutí složitého úkolu bezpečné autentizace na specializovanou, důvěryhodnou stranu. Tento federovaný model, standardizovaný prostřednictvím SAML, je základním kamenem pro zajištění bezpečného a uživatelsky přívětivého přístupu ke službám založeným na IMS a k partnerstvím v ekosystému s více dodavateli a operátory.

## Klíčové vlastnosti

- Aserce založené na XML: Používá strukturované XML dokumenty ke komunikaci rozhodnutí o autentizaci, atributech a autorizaci.
- Jednotné přihlašování (SSO): Umožňuje uživatelům přihlásit se jednou ke své domovské síti a přistupovat k více federovaným službám bez opětovného přihlašování.
- Federovaná správa identit: Vytváří vztah důvěry mezi Poskytovatelem identity (IdP – operátor) a Poskytovateli služeb (SP).
- Využití silné autentizace: Umožňuje poskytovatelům služeb třetích stran spoléhat se na silné autentizační mechanismy operátora (např. 3GPP AKA, založené na SIM kartě).
- Standardizované vazby a profily: 3GPP TS 33.980 definuje specifické vazby (bindings, např. HTTP Redirect/POST) a profily SAML 2.0 pro použití v telekomunikacích.
- Digitální podpisy: SAML aserce jsou digitálně podepisovány IdP, což zajišťuje integritu a autenticitu bezpečnostních informací.

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [SAML na 3GPP Explorer](https://3gpp-explorer.com/glossary/saml/)
