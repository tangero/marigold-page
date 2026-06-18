---
slug: "agw"
url: "/mobilnisite/slovnik/agw/"
type: "slovnik"
title: "AGW – Access Gateway"
date: 2025-01-01
abbr: "AGW"
fullName: "Access Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/agw/"
summary: "Přístupová brána (AGW) je funkční entita v sítích 3GPP, která zajišťuje konektivitu a správu relací pro uživatelské zařízení. Funguje jako brána mezi přístupovou a jádrovou sítí, zajišťuje přeposílání"
---

AGW je funkční bránová entita v sítích 3GPP, která propojuje přístupovou a jádrovou síť a poskytuje správu uživatelských relací, přeposílání dat, vynucování politik a správu mobility.

## Popis

Přístupová brána (AGW) je standardizovaná síťová funkce v architektuře 3GPP, konkrétně definovaná v kontextu vylepšení pro síťovou mobilitu IP toků (NB-IFOM) a funkci pro vyhledávání a výběr přístupové sítě ([ANDSF](/mobilnisite/slovnik/andsf/)). Z architektonického hlediska se nachází na rozhraní mezi bodem připojení uživatelského zařízení (např. 3GPP přístup jako LTE nebo 5G NR, nebo ne-3GPP přístup jako Wi-Fi) a paketovou jádrovou sítí (vylepšené paketové jádro nebo 5G jádro). Jejím hlavním operačním mechanismem je navázání a správa relací IP konektivity pro uživatelské zařízení, přičemž z pohledu zařízení funguje jako první IP uzel v síti operátora.

Funkčně AGW plní několik klíčových rolí. Slouží jako kotvící bod pro IP toky, což umožňuje plynulou mobilitu a kontinuitu relací při přechodu uživatelů mezi různými přístupovými sítěmi. Brána implementuje vynucování politik přijatých od funkce pravidel pro politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), aplikuje označení kvality služeb (QoS), omezení šířky pásma a pravidla účtování na uživatelský datový provoz. Také zajišťuje přidělování a správu IP adres pro připojená uživatelská zařízení, často ve spolupráci se serverem [DHCP](/mobilnisite/slovnik/dhcp/) nebo za použití síťových protokolů mobility.

Z protokolového hlediska rozhraní AGW s uživatelským zařízením přes různé přístupově specifické protokoly (např. [GTP-U](/mobilnisite/slovnik/gtp-u/) přes [S1-U](/mobilnisite/slovnik/s1-u/) pro LTE, rozhraní N3 pro 5G) a připojuje se k jádrové síti přes standardizovaná rozhraní. Ve specifikacích 3GPP je chování AGW detailně popsáno v souvislosti s podporou selektivního odklonu IP provozu ([SIPTO](/mobilnisite/slovnik/sipto/)) a místního IP přístupu ([LIPA](/mobilnisite/slovnik/lipa/)), což umožňuje směrování určitých toků provozu lokálně bez průchodu celou jádrovou sítí. Tato schopnost lokálního "breakoutu" snižuje latenci a zatížení jádrové sítě pro vhodné typy provozu.

Implementace AGW se liší v závislosti na přístupové technologii a síťové architektuře. V integrovaných nasazeních může být společná s jinými síťovými funkcemi, jako je servisní brána (SGW) v EPC nebo funkce uživatelské roviny (UPF) v 5GC. Jako logická entita zahrnuje klíčové komponenty: přeposílací engine pro směrování paketů, modul pro vynucování politik pro aplikaci QoS a účtovacích pravidel, modul správy mobility pro zvládnutí předávání mezi přístupovými body a řídicí rozhraní pro komunikaci s síťovými řadiči. Její distribuovaná povaha umožňuje operátorům nasazovat AGW blíže k okrajům sítě pro lepší výkon.

## K čemu slouží

Přístupová brána byla zavedena, aby řešila rostoucí složitost heterogenních síťových prostředí, kde se uživatelská zařízení mohou připojovat přes více přístupových technologií současně. Před její standardizací sítě zápasily s efektivním řízením provozu a správou mobility napříč 3GPP a ne-3GPP přístupy, často vyžadovaly samostatné brány pro každý typ přístupu s omezenou koordinací mezi nimi. To vedlo k neoptimálnímu využití zdrojů, zvýšené latenci při předávání a obtížím při implementaci konzistentních politik napříč různými přístupovými sítěmi.

Koncept AGW vznikl konkrétně pro podporu síťové mobility IP toků (NB-IFOM), která operátorům umožňuje dynamicky směrovat jednotlivé IP toky přes nejvhodnější přístupovou síť na základě politik, stavu sítě a požadavků aplikace. To byl významný pokrok oproti dřívějším přístupům, kdy veškerý provoz ze zařízení musel používat stejnou přístupovou síť nebo kdy řešení mobility fungovala na aplikační vrstvě místo na síťové vrstvě. Poskytnutím společné bránové funkce napříč přístupy umožňuje AGW podrobnější správu provozu při zachování kontinuity relace.

Dále AGW usnadňuje implementaci pokročilých mechanismů odklonu provozu, jako je selektivní odklon IP provozu (SIPTO) na místní síti, což se stalo stále důležitějším s explozivním nárůstem objemu mobilních dat. Bez standardizované funkce AGW čelili operátoři problémům s interoperabilitou při pokusech implementovat vícepřístupová řešení od různých dodavatelů. Standardizace AGW v rámci 3GPP zajistila konzistentní chování napříč implementacemi, umožnila bezproblémovou integraci s existujícími funkcemi jádrové sítě a podpořila vývoj směrem k flexibilnějším, na přístupu nezávislým síťovým architekturám.

## Klíčové vlastnosti

- Podpora vícepřístupové konektivity pro 3GPP a ne-3GPP sítě
- Vynucování síťové mobility IP toků (NB-IFOM)
- Vynucování pravidel pro politiky a účtování od PCRF/PCF
- Podpora místního IP přístupu (LIPA) a selektivního odklonu IP provozu (SIPTO)
- Správa a přidělování IP adres pro uživatelská zařízení
- Kontinuita relace při předávání mezi různými přístupy

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [SIPTO – Selected IP Traffic Offload](/mobilnisite/slovnik/sipto/)
- [LIPA – Local IP Access](/mobilnisite/slovnik/lipa/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions

---

📖 **Anglický originál a plná specifikace:** [AGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/agw/)
