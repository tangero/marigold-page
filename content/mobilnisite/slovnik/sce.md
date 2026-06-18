---
slug: "sce"
url: "/mobilnisite/slovnik/sce/"
type: "slovnik"
title: "SCE – Service Creation Environment"
date: 2025-01-01
abbr: "SCE"
fullName: "Service Creation Environment"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sce/"
summary: "Sada nástrojů a frameworků, která umožňuje síťovým operátorům a vývojářům třetích stran navrhovat, testovat a nasazovat nové telekomunikační služby a aplikace. Abstrahuje síťovou složitost, což umožňu"
---

SCE je sada nástrojů a frameworků, která umožňuje operátorům a vývojářům navrhovat, testovat a nasazovat nové telekomunikační služby abstrakcí síťové složitosti pro rychlou inovaci.

## Popis

Service Creation Environment (SCE) je komplexní platforma definovaná v ekosystému 3GPP pro vývoj a správu životního cyklu přidaných služeb v telekomunikačních sítích. Není to jedna síťová funkce, ale prostředí zahrnující vývojářské sady ([SDK](/mobilnisite/slovnik/sdk/)), aplikační programová rozhraní ([API](/mobilnisite/slovnik/api/)), grafická uživatelská rozhraní ([GUI](/mobilnisite/slovnik/gui/)), testovací nástroje a nasazovací frameworky. SCE poskytuje vyšší vrstvu abstrakce, která skrývá složité detaily signalizačních protokolů jádra sítě (jako [MAP](/mobilnisite/slovnik/map/), [CAP](/mobilnisite/slovnik/cap/) nebo [SIP](/mobilnisite/slovnik/sip/)) a umožňuje vývojářům soustředit se na služební logiku a uživatelský zážitek. Typicky funguje v doméně Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) nebo, v modernějším kontextu, v rámci IP Multimedia Subsystem (IMS) a platforem pro poskytování služeb.

Architektonicky je SCE často součástí větší Service Delivery Platform ([SDP](/mobilnisite/slovnik/sdp/)) nebo prostředí IMS Application Server (AS). Funguje tak, že nabízí předpřipravené komponenty, šablony a pracovní postupy pro běžné telekomunikační funkce, jako je řízení hovorů, zasílání zpráv, stavová informace (presence), lokalizace a účtování. Vývojář použije nástroje SCE k sestavení těchto komponent, definování obchodních pravidel (např. 'přepoj hovor na hlasovou schránku, pokud je účastník zaneprázdněn') a integraci s externími zdroji dat. Prostředí poté zkompiluje nebo interpretuje tento vysokourovňový návrh na nízkourovňové, síťově specifické instrukce a konfigurace potřebné k provádění služby na skutečných síťových prvcích. To může zahrnovat generování Service Logic Programs (SLP) pro IN, SIP servletů pro IMS nebo konfiguračních souborů pro pravidla politiky a účtování.

Klíčovými komponentami SCE jsou studio pro tvorbu služeb (integrované vývojové prostředí), testovací a simulační engine, který může emulovat síťové chování, úložiště pro správu aktiv služeb a verzí a nasazovací manažery rozhraněné se systémy správy sítě. Jeho úlohou je drasticky zkrátit dobu uvedení nových služeb na trh. Poskytnutím řízeného, standardizovaného prostředí zajišťuje, že vytvořené služby jsou kompatibilní se síťovými schopnostmi, dodržují provozní politiky a lze je spolehlivě zřizovat, aktivovat a monitorovat. Překlenuje propast mezi kreativním návrhem služeb a rigidním, spolehlivým prováděním vyžadovaným v sítích úrovně operátora.

## K čemu slouží

Service Creation Environment byl vytvořen, aby vyřešil kritický problém pomalé a drahé inovace služeb v tradičních telekomunikačních sítích. Historicky zavedení nové služby, jako je čekání na hovor, předplacené účtování nebo upozornění založené na lokalizaci, vyžadovalo hluboké, dodavatelem specifické znalosti programování ústředen a zahrnovalo dlouhé vývojové cykly vysoce specializovanými inženýry. Tento monolitický, uzavřený přístup dusil inovace, činil operátory závislými na dodavatelích zařízení pro nové funkce a vedl k nedostatku diferenciace služeb na trhu.

Vzestup konceptu Inteligentní sítě (IN) v 90. letech 20. století si kladl za cíl oddělit služební logiku od přepínací logiky. SCE je praktický nástroj, který toto oddělení umožňuje. Umožňuje operátorům – a později, prostřednictvím otevřených API, i vývojářům třetích stran – vytvářet služby nezávisle na podkladovém přepínacím hardwaru. Motivace byla ekonomická a konkurenční: urychlit tvorbu přidaných služeb generujících příjmy, rychle reagovat na tržní trendy a snížit vývojové náklady. Specifikace jako ty v 3GPP (např. TS 26.253 pro tvorbu multimediálních zprávových služeb) poskytly standardy pro tato prostředí, podporující interoperabilitu a předcházející závislosti na jediném dodavateli.

Jak se sítě vyvíjely směrem k IMS a all-IP architekturám, účel SCE se rozšířil. Nyní také řeší potřebu vytvářet konvergované služby, které kombinují hlas, video, zprávy a webový obsah. Řeší složitost orchestrace více IMS funkcí jádra (jako CSCF, HSS, PCRF) a integrace s IT systémy. SCE tedy existuje jako nezbytný inovační motor, transformující síť ze statického nástroje na programovatelnou platformu pro široký ekosystém poskytovatelů služeb.

## Klíčové vlastnosti

- Grafické rozhraní pro návrh služební logiky metodou přetáhni a pusť
- Knihovna znovupoužitelných síťových služebních enablerů (např. API pro řízení hovorů, zasílání zpráv)
- Integrované testování a simulace s emulací sítě
- Správa životního cyklu služby (návrh, test, nasazení, aktualizace, vyřazení)
- Podpora standardních jazyků pro tvorbu služeb (např. JAIN SLEE, SIP servlety)
- Nástroje pro balíčkování a nasazování služeb na aplikační servery

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.254** (Rel-19) — IVAS Rendering Functions Specification
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [SCE na 3GPP Explorer](https://3gpp-explorer.com/glossary/sce/)
