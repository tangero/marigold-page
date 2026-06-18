---
slug: "xdm"
url: "/mobilnisite/slovnik/xdm/"
type: "slovnik"
title: "XDM – XML Document Management"
date: 2025-01-01
abbr: "XDM"
fullName: "XML Document Management"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/xdm/"
summary: "XML Document Management (XDM) je služební prvek (service enabler) 3GPP, který definuje společný mechanismus pro správu uživatelských služebních dat uložených ve formátu XML. Umožňuje síťovým aplikacím"
---

XDM je služební prvek (service enabler) 3GPP, který definuje společný mechanismus pro správu uživatelských služebních dat uložených ve formátu XML, umožňující přístup a manipulaci s konfiguračními daty napříč různými službami.

## Popis

[XML](/mobilnisite/slovnik/xml/) Document Management (XDM) je standardizovaná služební schopnost v architektuře IP Multimedia Subsystem (IMS) 3GPP, která poskytuje rámec pro ukládání, přístup a správu uživatelských služebních dat v XML dokumentech. Funguje prostřednictvím souboru funkčních entit, především XDM klienta ([XDMC](/mobilnisite/slovnik/xdmc/)) a XDM serveru ([XDMS](/mobilnisite/slovnik/xdms/)), které vzájemně komunikují pomocí protokolů jako XML Configuration Access Protocol ([XCAP](/mobilnisite/slovnik/xcap/)) přes [HTTP](/mobilnisite/slovnik/http/). XDM server, který zahrnuje komponenty jako Shared XDMS, Aggregation Proxy a Search Proxy, ukládá XML dokumenty v repozitářích a zpracovává požadavky na manipulaci s dokumenty. Tyto dokumenty obsahují služebně specifická data, jako jsou seznamy přítomnosti, definice skupin nebo uživatelské preference, což umožňuje aplikacím konzistentním způsobem získávat a aktualizovat uživatelské konfigurace.

Princip fungování XDM spočívá v modelu klient-server, kdy XDM klient, typicky vestavěný v uživatelském zařízení nebo aplikačních serverech, odesílá XCAP požadavky na XDM server, aby provedl operace jako vytvoření, čtení, aktualizace nebo smazání XML dokumentů. Aggregation Proxy funguje jako jednotný vstupní bod, který autentizuje požadavky a směruje je na příslušný XDMS na základě typu dokumentu. Například Presence XDMS spravuje dokumenty související s přítomností, zatímco Shared XDMS zpracovává společná data jako seznamy kontaktů. XDM server validuje požadavky vůči XML schématům a uplatňuje přístupové politiky, aby zajistil bezpečnost a integritu dat. Tato architektura umožňuje více službám sdílet a znovu používat uživatelská data, čímž snižuje redundanci a zlepšuje integraci služeb.

Klíčové komponenty XDM zahrnují protokol XCAP, který definuje metody pro manipulaci s XML dokumenty přes HTTP; referenční bod XDM-3, který specifikuje rozhraní mezi XDMC a XDMS; a různé typy XDMS přizpůsobené konkrétním službám. Rámec XDM také podporuje mechanismy odběru (subscription), které umožňují klientům dostávat oznámení o změnách dokumentů prostřednictvím [SIP](/mobilnisite/slovnik/sip/) notifikací. To umožňuje aktualizace v reálném čase napříč službami, například když uživatel změní své členství ve skupině. Role XDM je podrobně popsána ve specifikacích jako TS 24.484 pro použití protokolu XCAP a TS 32.808 pro aspekty správy, což zajišťuje interoperabilitu mezi různými síťovými implementacemi. Poskytnutím jednotné vrstvy pro správu dat XDM usnadňuje vytváření bohatých, personalizovaných služeb v sítích 3GPP, od základní telefonie po pokročilé multimediální aplikace.

## K čemu slouží

[XML](/mobilnisite/slovnik/xml/) Document Management (XDM) byl vytvořen, aby řešil potřebu standardizovaného způsobu správy uživatelských služebních dat v IP sítích, zejména v rámci architektury IMS. Před XDM byla služební data často ukládána v proprietárních formátech nebo izolována v rámci jednotlivých aplikací, což vedlo k fragmentaci, duplikaci a omezené interoperabilitě. To ztěžovalo nabízení integrovaných služeb, jako je zasílání zpráv obohacené o přítomnost nebo dynamická správa skupin. XDM tyto problémy řeší zavedením společného úložiště a přístupového mechanismu založeného na XML, což umožňuje sdílení dat napříč více službami a síťovými doménami.

Historicky, jak se telekomunikační služby vyvíjely z přepojování okruhů na architektury s přepojováním paketů, rostla poptávka po personalizovaných a konvergentních službách. XDM se objevil ve 3GPP Release 8 jako součást sady IMS, motivován úspěchem XML ve webových službách a potřebou flexibilní správy dat. Řeší omezení dřívějších přístupů tím, že poskytuje škálovatelný a rozšiřitelný rámec, který podporuje různé požadavky služeb, od jednoduchého ukládání konfigurace po komplexní agregaci dat. Například XDM umožňuje službám jako Push-to-talk over Cellular (PoC) a Rich Communication Services ([RCS](/mobilnisite/slovnik/rcs/)) konzistentně spravovat skupinové seznamy a uživatelské preference.

Účel XDM přesahuje základní ukládání dat; umožňuje služební prvky (enablers), které zlepšují uživatelský zážitek a provozní efektivitu. Centralizací správy XML dokumentů XDM snižuje vývojovou režii pro nové služby, protože ty mohou využívat existující data bez nutnosti znovuvytváření mechanismů ukládání. Také podporuje regulatorní požadavky, jako jsou kontroly soukromí prostřednictvím přístupových politik. S postupem sítí na 4G a 5G se role XDM rozšířila o podporu nových případů užití, jako je síťové dělení (network slicing) a správa služeb IoT, což demonstruje jeho přizpůsobivost a trvalou relevanci v ekosystémech 3GPP.

## Klíčové vlastnosti

- Standardizované ukládání a správa XML dokumentů pro uživatelská služební data
- Podpora protokolu XCAP pro manipulaci s dokumenty přes HTTP (operace CRUD)
- Aggregation Proxy pro centralizované směrování požadavků a autentizaci
- Více typů XDMS (např. Shared, Presence) pro služebně specifická data
- Mechanismy odběru (subscription) a oznamování pro aktualizace dokumentů v reálném čase
- Integrace s jádrem IMS pro bezproblémovou podporu služebních prvků (enablers)

## Definující specifikace

- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [XDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/xdm/)
