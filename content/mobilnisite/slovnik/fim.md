---
slug: "fim"
url: "/mobilnisite/slovnik/fim/"
type: "slovnik"
title: "FIM – Federated Information Model"
date: 2025-01-01
abbr: "FIM"
fullName: "Federated Information Model"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/fim/"
summary: "Standardizovaný datový model pro správu telekomunikačních sítí napříč více doménami nebo operátory. Umožňuje konzistentní výměnu informací a jednotnou správu definováním společné sady spravovaných obj"
---

FIM je standardizovaný datový model pro správu telekomunikačních sítí napříč více doménami či operátory, který umožňuje konzistentní výměnu informací a jednotnou správu pomocí společných spravovaných objektů a vztahů.

## Popis

Federated Information Model (FIM) je komplexní rámec definovaný v rámci specifikací 3GPP, primárně v TS 32.107, určený k usnadnění správy složitých telekomunikačních sítí s více doménami. Funguje tak, že stanovuje standardizovanou sadu spravovaných objektů, jejich atributů, chování a vztahů, na nichž se dohodnou různé administrativní domény, síťoví operátoři nebo technologičtí dodavatelé. Tento model není jedinou fyzickou databází, ale logickým schématem, které zajišťuje, že všechny účastnické správní systémy interpretují a zpracovávají síťová data konzistentně. Architektonicky se FIM integruje s existujícími rámci správy, jako je Telecommunications Management Network (TMN) a pozdější přístupy, a působí jako sémantická vrstva propojující disparátní systémy Network Management Systems ([NMS](/mobilnisite/slovnik/nms/)), Element Management Systems ([EMS](/mobilnisite/slovnik/ems/)) a Operations Support Systems ([OSS](/mobilnisite/slovnik/oss/)). Jeho role spočívá v umožnění federovaných scénářů správy, například když operátor potřebuje spravovat virtualizované síťové funkce od různých dodavatelů nebo koordinovat s partnerským operátorem pro plynulé poskytování služeb, a to poskytnutím 'společného jazyka' pro správní data.

V jádru FIM funguje definováním informačních objektových tříd, které reprezentují síťové prostředky, služby a účastníky. Tyto třídy zahrnují podrobné specifikace atributů (např. stav, konfigurační parametry), operací (např. vytvořit, smazat, upravit) a notifikací (např. alarmy, metriky výkonu). Model využívá objektově orientované principy a je často implementován pomocí modelovacích jazyků, jako je Unified Modeling Language (UML), a datových formátů, jako jsou XML Schema Definitions (XSD). Klíčovými komponentami jsou samotné schéma FIM, které je rozšiřitelné pro akomodaci nových technologií, a související správní rozhraní (např. northbound rozhraní), která tyto objekty zpřístupňují systémům vyšší úrovně. V praxi, když správní systém v jedné doméně dotazuje nebo řídí prostředek v jiné doméně, používá zprávy založené na FIM, čímž zajišťuje, že přijímající systém přesně rozumí požadavku bez ohledu na svou vnitřní implementaci.

Význam FIM spočívá v jeho schopnosti podporovat automatizovanou a efektivní správu sítí v stále heterogennějších prostředích. S tím, jak se sítě vyvíjely a zahrnovaly cloud-nativní funkce, síťové slicing a spolupráce více operátorů, rostla potřeba federovaného přístupu. FIM to řeší snížením integračních nákladů, minimalizací chyb z nesprávné interpretace dat a umožněním škálovatelných správních operací. Hraje kritickou roli ve scénářích, jako je správa síťového slicing 5G, kde slice může zahrnovat více administrativních domén, z nichž každá má svůj vlastní správní systém. Dodržováním FIM mohou tyto systémy společně zřizovat, monitorovat a zajišťovat end-to-end slice bez manuální intervence. Dále FIM podporuje regulační a bezpečnostní požadavky poskytováním jasné auditní stopy a konzistentního vynucování politik napříč federovanými hranicemi.

## K čemu slouží

Federated Information Model byl vytvořen k řešení výzev spojených se správou telekomunikačních sítí, které se rozkládají přes více administrativních domén, dodavatelů nebo technologií. Historicky byla správa sítě izolovaná, přičemž každý operátor nebo dodavatel používal proprietární datové modely a rozhraní, což vedlo k vysokým integračním nákladům, provozní neefektivitě a chybám při koordinaci mezi doménami. Jak se sítě stávaly komplexnějšími s nástupem virtualizace, partnerství více operátorů a globálních nasazení služeb, tato fragmentace se stala významnou překážkou pro agilní a automatizované operace. FIM tyto limity řeší poskytnutím standardizovaného, dohodnutého informačního modelu, který mohou všechny strany přijmout, což umožňuje bezproblémovou výměnu dat a jednotnou správu.

Motivace pro FIM vycházela z posunu průmyslu směrem k federovaným síťovým architekturám, kde jsou prostředky sdíleny nebo orchestraci napříč hranicemi – jako např. ve scénářích roamingu, nastavení Mobile Virtual Network Operator ([MVNO](/mobilnisite/slovnik/mvno/)) nebo nasazení cloudových síťových funkcí. Bez společného modelu vyžadoval každý integrační bod vlastní adaptéry a mapování, které byly nákladné na vývoj a údržbu. FIM to zjednodušuje definováním jediného zdroje pravdy pro správní informace, čímž snižuje potřebu bilaterálních dohod a point-to-point integrací. Také podporuje nové trendy, jako je síťový slicing a edge computing, kde je dynamické přidělování prostředků napříč doménami nezbytné.

Zavedením FIM ve Release 11 měl 3GPP v úmyslu zajistit budoucí připravenost správních rámců pro vyvíjející se síťová paradigmata. Staví na dřívějších standardech správy, jako je pyramida TMN a koncepty Common Information Model ([CIM](/mobilnisite/slovnik/cim/)), ale se specifickým zaměřením na potřeby telekomunikací. Model umožňuje operátorům dosáhnout vyšší automatizace, zkrátit time-to-market pro nové služby a zlepšit kvalitu služeb konzistentním monitoringem a řízením. V konečném důsledku FIM existuje pro podporu interoperability a efektivity v prostředích s více zainteresovanými stranami, což je v moderních telekomunikačních ekosystémech stále častější.

## Klíčové vlastnosti

- Standardizované definice spravovaných objektů pro konzistentní interpretaci dat
- Podpora správy sítí s více doménami a více dodavateli
- Rozšiřitelné schéma pro akomodaci nových technologií a služeb
- Integrace s existujícími rámci TMN a OSS/BSS
- Objektově orientované modelování využívající UML a implementace založené na XML
- Umožňuje automatizované zřizování, monitoring a zajištění kvality napříč federovanými hranicemi

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [CIM – Common Information Model](/mobilnisite/slovnik/cim/)

## Definující specifikace

- **TS 32.107** (Rel-19) — Federated Network Information Model (FNIM)

---

📖 **Anglický originál a plná specifikace:** [FIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/fim/)
