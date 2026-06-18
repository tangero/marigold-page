---
slug: "lap"
url: "/mobilnisite/slovnik/lap/"
type: "slovnik"
title: "LAP – Liberty Alliance Project"
date: 2025-01-01
abbr: "LAP"
fullName: "Liberty Alliance Project"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/lap/"
summary: "Již zaniklý průmyslový konsorcium, které vyvíjelo otevřené standardy pro federovanou digitální identitu, jednotné přihlašování (SSO) a webové služby založené na identitě. Jeho specifikace, zejména Ide"
---

LAP je již zaniklý průmyslový konsorcium, které vyvíjelo otevřené standardy pro federovanou digitální identitu a ovlivnilo rané práce 3GPP na autentizaci pro IMS a přístup k síti.

## Popis

Liberty Alliance Project (LAP) nebyla technologie vytvořená 3GPP, ale externí standardizační orgán, jehož práce byla odkazována a přijímána v rámci určitých specifikací 3GPP, především těch zabývajících se zabezpečením a přístupem ke službám. Jeho klíčovým přínosem byl Liberty Identity Federation Framework ([ID-FF](/mobilnisite/slovnik/id-ff/)), který poskytoval sadu protokolů pro správu federované identity. Federace umožňuje, aby byla identita a přihlašovací údaje uživatele z jedné domény (poskytovatele identity, IdP) důvěryhodné a použitelné v jiné doméně (poskytovatele služby, [SP](/mobilnisite/slovnik/sp/)), což umožňuje bezproblémové jednotné přihlašování ([SSO](/mobilnisite/slovnik/sso/)) napříč doménami. V rámci 3GPP byl tento koncept integrován pro usnadnění zabezpečeného přístupu k IMS a dalším IP službám, zejména z přístupových sítí mimo 3GPP, jako je Wi-Fi.

Z architektonického hlediska rámec LAP zavedl klíčové role: Subjekt (uživatel), Poskytovatel identity (který spravuje hlavní přihlašovací údaje uživatele) a Poskytovatel služby. Protokoly umožňovaly vytvoření federovaného kontextu nebo "kruhu důvěry" mezi těmito entitami. Technicky to zahrnovalo přesměrování prohlížeče pomocí artefaktů nebo [SAML](/mobilnisite/slovnik/saml/) tvrzení pro přenos autentizačních výroků. V kontextu 3GPP mohl Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo vyhrazený server Authentication, Authorization, and Accounting ([AAA](/mobilnisite/slovnik/aaa/)) fungovat jako Poskytovatel identity. Webový portál nebo IMS Application Server mohl fungovat jako Poskytovatel služby. Když se uživatel pokusil o přístup ke službě, SP přesměroval uživatelův prohlížeč k IdP (3GPP síti) k provedení autentizace. Po úspěšné 3GPP autentizaci (např. pomocí přihlašovacích údajů [SIM](/mobilnisite/slovnik/sim/)) IdP odeslal kryptograficky podepsané tvrzení zpět SP, které potvrdilo identitu a stav autentizace uživatele, a udělilo přístup bez nutnosti samostatného hesla.

Tento mechanismus byl podrobně popsán ve specifikaci 3GPP TS 33.980, která profilovala použití Liberty ID-FF pro systémy 3GPP. Definovala, jak mají entity 3GPP sítě generovat a zpracovávat Liberty artefakty a tvrzení, mapující identifikátory účastníků 3GPP (jako [IMSI](/mobilnisite/slovnik/imsi/) nebo IMPI) do modelu federované identity. Rámec také podporoval navázání federace identity, jednotné odhlášení a jednoduché sdílení atributů založené na souhlasu. Zatímco samotný LAP byl nahrazen pozdějšími standardy, jako je SAML 2.0 a OpenID Connect, jeho základní koncepty federované identity se staly klíčovou součástí pro umožnění zabezpečeného a uživatelsky přívětivého přístupu k multimediálním službám napříč heterogenními přístupovými sítěmi v ekosystému 3GPP.

## K čemu slouží

Liberty Alliance Project byl založen v roce 2001 konsorciem společností za účelem vytvoření otevřené alternativy k proprietárním systémům jednotného přihlašování, především k Microsoft Passport (nyní Windows Live ID). Jeho hlavním cílem bylo řešit rostoucí potřebu zabezpečené, soukromí respektující a interoperabilní správy digitální identity napříč internetem. Před standardy federace museli uživatelé udržovat samostatná uživatelská jména a hesla pro každou službu, což vedlo ke špatné uživatelské zkušenosti a bezpečnostním rizikům, jako je opakované používání hesel. Pro síťové operátory a poskytovatele služeb byla správa těchto izolovaných identit obtížná a omezovala dosah služeb.

Přijetí specifikací LAP v 3GPP, počínaje Release 8, bylo motivováno potřebou bezpečně rozšířit 3GPP autentizaci (jako autentizaci založenou na SIM) na přístupové sítě a webové služby mimo 3GPP. S vývojem IMS a mobilních datových služeb uživatelé očekávali přístup ke stejným multimediálním službám z domácí Wi-Fi nebo veřejné hotspotové sítě jako ze své mobilní sítě. Problémem bylo, jak využít silné zabezpečení založené na SIM v doméně 3GPP v těchto nedůvěryhodných, IP založených doménách bez kompromisu v zabezpečení nebo uživatelském komfortu. Rámec federované identity LAP poskytl standardizované řešení.

Problém řešil tím, že umožnil 3GPP síti (domácímu operátorovi) fungovat jako důvěryhodný Poskytovatel identity. Uživatel se mohl jednou autentizovat u své domácí sítě a tato autentizace mohla být federována na jakéhokoli Poskytovatele služby (např. IMS aplikaci, partnerskou video službu), který důvěřoval IdP operátora. Tím odpadla potřeba služebně specifických hesel, zvýšilo se zabezpečení použitím robustních 3GPP autentizačních metod a umožnil se bezproblémový přístup ke službám napříč různými technologickými doménami. Byl to klíčový prvek pro ranou konvergenci pevných a mobilních sítí a vizi všudypřítomného přístupu k multimediálním službám.

## Klíčové vlastnosti

- Správa federované identity umožňující jednotné přihlašování (SSO) napříč různými administrativními doménami
- Použití tvrzení a artefaktů založených na SAML pro zabezpečený přenos autentizačních výroků
- Podpora toků SSO iniciovaných poskytovatelem identity (IdP) i poskytovatelem služby (SP)
- Mechanismy pro federované odhlášení k ukončení relací napříč všemi propojenými poskytovateli služeb
- Rámec pro vytváření kruhů důvěry mezi poskytovateli identity a služeb
- Mapování identit účastníků 3GPP (IMPI/IMPU) do protokolů federované identity

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [LAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lap/)
