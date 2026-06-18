---
slug: "lcc"
url: "/mobilnisite/slovnik/lcc/"
type: "slovnik"
title: "LCC – Lower Camel Case"
date: 2026-01-01
abbr: "LCC"
fullName: "Lower Camel Case"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/lcc/"
summary: "LCC je konvence pojmenování používaná ve specifikacích 3GPP pro identifikátory a parametry. Zlepšuje čitelnost kódu a konzistenci v technické dokumentaci a softwarových implementacích použitím specifi"
---

LCC je konvence pojmenování používaná ve specifikacích 3GPP pro identifikátory a parametry za účelem zlepšení čitelnosti a konzistence použitím specifického formátu pro složená slova.

## Popis

Lower Camel Case (LCC) je typografická konvence pro zápis složených slov nebo frází, kde každé slovo kromě prvního začíná velkým písmenem a mezi slovy nejsou mezery nebo interpunkční znaménka. V kontextu specifikací 3GPP je tato konvence formálně definována a nařízena pro použití u určitých identifikátorů, názvů parametrů a datových struktur, zejména ve specifikacích pro správu a účtování, jako jsou TS 28.821 a TS 32.156. Její aplikace zajišťuje standardizovaný, strojově čitelný a lidsky čitelný formát pro pojmenování prvků napříč různými síťovými funkcemi a rozhraními.

Tato konvence je striktně aplikována při definici YANG datových modelů, definicích řídicích objektů a protokolových datových jednotkách ([PDU](/mobilnisite/slovnik/pdu/)), kde je konzistentní styl pojmenování klíčový pro interoperabilitu a automatizované zpracování. Například parametr reprezentující 'maximální přenosovou rychlost' by byl ve formátu LCC zapsán jako 'maxBitRate'. Tím se předchází nejednoznačnostem, které by mohly vzniknout z různých stylů pojmenování (jako snake_case nebo UpperCamelCase), a usnadňuje se parsování a generování kódu systémy pro správu sítí a vývojářskými sadami ([SDK](/mobilnisite/slovnik/sdk/)).

Z architektonického pohledu je použití LCC základním aspektem strategie datového modelování 3GPP. Podporuje principy jednotného rámce pro správu, kde severní rozhraní (jako například rozhraní pro správu sítě) prezentují data v předvídatelném, strukturovaném formátu. Tato konzistence snižuje složitost integrace v prostředí více dodavatelů a je nezbytná pro automatizovaný správu životního cyklu síťových funkcí, včetně konfigurace, monitorování výkonu a správy poruch v sítích 5G a budoucích generací.

## K čemu slouží

Primárním účelem standardizace Lower Camel Case v rámci 3GPP je vynutit konzistenci pojmenování napříč rozsáhlým ekosystémem technických specifikací vyvíjených různými pracovními skupinami. Před zavedením takových konvencí mohly specifikace používat ad-hoc styly pojmenování, což vedlo k nejasnostem, integračním chybám a prodloužení vývojového času u výrobců zařízení a softwarových vývojářů implementujících standardy. LCC poskytuje jasný, pravidly řízený přístup pro tvorbu názvů.

Tato konvence řeší problém syntaktické heterogenity v rozhraních pro komunikaci mezi stroji, zejména těch založených na moderních formátech serializace dat, jako jsou [JSON](/mobilnisite/slovnik/json/) a [XML](/mobilnisite/slovnik/xml/), které jsou rozšířené v architektuře založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 3GPP. Diktováním jednotného stylu zajišťuje, že datové modely pro správu a definice [API](/mobilnisite/slovnik/api/) jsou předvídatelné, což je klíčové pro vývoj automatizovaných nástrojů, generátorů kódu a pro zajištění, že různé síťové funkce mohou správně interpretovat vzájemná data. Řeší tak základní výzvu softwarového inženýrství v rámci standardizačního orgánu.

Historicky bylo motivací pro její formální zařazení do vydání, jako je Rel-11, stále více softwarově definovaná povaha telekomunikačních sítí. Jak specifikace 3GPP začaly začleňovat podrobnější datové modely pro správu a orchestraci, konzistentní lexikální styl se stal předpokladem pro škálovatelnost a interoperabilitu. Je klíčovým enablerem pro DevOps a GitOps praktiky aplikované na správu sítí, kde je infrastruktura definována a spravována prostřednictvím kódu, který musí být jednoznačný a konzistentní.

## Klíčové vlastnosti

- Definuje konzistentní lexikální konvenci pro složené identifikátory
- Stanovuje, že první slovo je psáno malými písmeny a následující slova začínají velkým písmenem
- Odstraňuje mezery a speciální interpunkci mezi slovy
- Zlepšuje lidskou čitelnost technických názvů parametrů
- Usnadňuje automatizované generování kódu a datových modelů
- Klíčová pro interoperabilitu v rozhraních pro správu a účtování

## Související pojmy

- [JSON – JavaScript Object Notation](/mobilnisite/slovnik/json/)

## Definující specifikace

- **TS 28.821** (Rel-13) — UML Model Repertoire for FMC Management
- **TS 32.156** (Rel-20) — UML Modeling for Network Management Systems

---

📖 **Anglický originál a plná specifikace:** [LCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcc/)
