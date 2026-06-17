---
slug: "cpim"
url: "/mobilnisite/slovnik/cpim/"
type: "slovnik"
title: "CPIM – Common Presence and Instant Messaging"
date: 2025-01-01
abbr: "CPIM"
fullName: "Common Presence and Instant Messaging"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cpim/"
summary: "CPIM je služební prostředek 3GPP standardizující službu presence a instant messaging (IM) pro sítě IP Multimedia Subsystem (IMS). Definuje protokoly a procedury pro dostupnost uživatele, publikaci sta"
---

CPIM je standard služebního prostředku 3GPP, který standardizuje službu presence a instant messaging pro sítě IMS, definuje protokoly pro dostupnost uživatele, publikaci stavu a komunikaci textem v reálném čase, čímž umožňuje interoperabilní služby telekomunikační úrovně.

## Popis

Common Presence and Instant Messaging (CPIM) je komplexní služební rámec 3GPP, který poskytuje standardizované mechanismy pro službu presence a instant messaging v rámci IP Multimedia Subsystem (IMS). Nejde o jeden protokol, ale o soubor specifikací, které definují, jak se informace o přítomnosti (např. dostupnost uživatele, ochota komunikovat a schopnosti terminálu) spravují, publikují a k nim přihlašují, a jak se instantní zprávy směrují a doručují bezpečným, interoperabilním způsobem. Architektura využívá základní prvky IMS, jako je Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pro řízení a směrování relací a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro uživatelská data. Pro službu presence typicky využívá prezence server (presence server), který shromažďuje, agreguje a distribuuje informace o přítomnosti z různých zdrojů presence (jako uživatelské terminály nebo síťové prvky) autorizovaným pozorovatelům (odběratelům). Pro instant messaging definuje dva základní režimy: messaging založený na relaci (session-based), který pro výměnu zpráv vytváří SIP relaci, a stránkový režim (page-mode), který používá samostatné SIP MESSAGE požadavky pro okamžité doručení bez vytvoření relace.

Technická realizace CPIM je hluboce integrována s protokolem SIP (Session Initiation Protocol) a jeho rozšířeními, zejména SIP for Instant Messaging and Presence Leveraging Extensions (SIMPLE). Služba presence zahrnuje mechanizmus publikace, kde Presence User Agent (PUA) nebo Presence Network Agent (PNA) odesílá prezence serveru požadavky PUBLISH obsahující dokumenty ve formátu Presence Information Data Format (PIDF). Pozorovatelé se k těmto informacím přihlašují pomocí požadavků SUBSCRIBE a přijímají zprávy NOTIFY s aktualizovanými daty o přítomnosti. Prezence server funguje jako centrální agregátor a uplatňuje autorizační pravidla často uložená na serveru XML Document Management Server (XDMS). Pro instant messaging jsou zprávy ve stránkovém režimu odesílány jako SIP MESSAGE požadavky směrované přes jádro IMS ([P-CSCF](/mobilnisite/slovnik/p-cscf/), [I-CSCF](/mobilnisite/slovnik/i-cscf/), S-CSCF) k S-CSCF příjemce pro konečné doručení. Messaging založený na relaci zahrnuje úvodní SIP INVITE pro navázání relace messagingu, přičemž se v rámci navázané relace pro přenos vlastních zpráv často používá protokol Message Session Relay Protocol ([MSRP](/mobilnisite/slovnik/msrp/)), což poskytuje výhody jako hlášení o doručení a podporu větších zpráv nebo přenosů souborů.

Klíčovými komponentami v síti s podporou CPIM jsou Presence Server (PS), což je centrální entita pro operace služby presence; Resource List Server (RLS), který může zpracovávat odběry seznamů entit presence (presentities) za účelem snížení signalizační zátěže; a různé servery XDMS pro správu autorizace presence a skupinových seznamů. Jádro IMS (CSCF, HSS) poskytuje nezbytnou registraci, směrování a správu účastníků. Úlohou CPIM je poskytnout standardizovanou, škálovatelnou a bezpečnou služební vrstvu nad IMS, která zajišťuje konzistentní fungování služeb presence a [IM](/mobilnisite/slovnik/im/) napříč více-dodavatelskými sítěmi a různými poskytovateli služeb. Tvoří základ pro rozšířené komunikační služby a umožňuje funkce jako "see what I see" a integraci do širších scénářů služeb definovaných v pozdějších vydáních 3GPP.

## K čemu slouží

CPIM byl vytvořen k řešení nedostatku standardizovaných, interoperabilních služeb presence a instant messaging v mobilních sítích. Před jeho zavedením byly běžné proprietární nebo internetové služby [IM](/mobilnisite/slovnik/im/) a presence (např. od jednotlivých výrobců nebo over-the-top poskytovatelů), které však postrádaly integraci se základními síťovými schopnostmi, garantovanou kvalitu služeb, robustní zabezpečení a možnost operátorů službu monetizovat a kontrolovat. Tato roztříštěnost také bránila uživatelskému zážitku, protože služby od různých operátorů nebo na různých zařízeních často nemohly vzájemně spolupracovat. Motivací pro CPIM bylo využít vznikající architekturu IMS – standardizovanou platformu pro poskytování služeb založenou na IP – k definování rámce telekomunikační úrovně pro tyto služby komunikace v reálném čase, který je zpoplatnitelný a spolehlivý.

Historicky růst internetového messagingu a touha po bohatší, kontextovější komunikaci (možnost zjistit, zda je kontakt dostupný před voláním nebo odesláním zprávy) vedly k potřebě standardizovaného přístupu v rámci telekomunikačního ekosystému. 3GPP zahájilo práce na CPIM ve vydání Release 6, aby poskytlo operátorům nástroje k nabídce konkurenceschopných, přidaných služeb nad rámec základního hlasu a SMS. Vyřešil problém služebních sil definováním společné sady protokolů založených na standardech [IETF](/mobilnisite/slovnik/ietf/) (jako SIP/SIMPLE), ale přizpůsobených a profilovaných pro kontrolované prostředí sítě mobilního operátora. To umožnilo integraci se správou účastníků, autentizací, systémy účtování a síťovými politikami, čímž se řešila omezení služeb best-effort na internetu, jako je nedostatek garance doručení, slabé zabezpečení a absence bezproblémové podpory mobility.

CPIM navíc poskytl základní stavební kameny pro pokročilejší komunikační služby plánované pro budoucí vydání, jako je Rich Communication Services (RCS). Tím, že vytvořil standardizované jádro pro službu presence a IM, umožnil služební ekosystém, ve kterém lze funkce spolehlivě skládat a nasazovat, což podporuje inovace při zachování interoperability a síťové kontroly pro operátory.

## Klíčové vlastnosti

- Standardizovaná publikace a odběr služby presence s využitím protokolů SIP/SIMPLE
- Podpora jak stránkového režimu (samostatné SIP MESSAGE), tak instant messagingu založeného na relaci (SIP relace s MSRP)
- Integrace s jádrem IMS pro autentizaci, směrování a účtování (prostřednictvím CSCF a HSS)
- Centrální agregace a distribuce informací o přítomnosti prostřednictvím prezence serveru (Presence Server)
- Autorizace a kontrola soukromí pro informace o přítomnosti s využitím pravidel spravovaných v XDMS
- Podpora seznamů presence a odběrů seznamů zdrojů pro optimalizaci síťové signalizace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MSRP – Multiple Stream Registration Protocol](/mobilnisite/slovnik/msrp/)

## Definující specifikace

- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem
- **TS 29.311** (Rel-19) — Service Level Interworking for Messaging
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [CPIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpim/)
