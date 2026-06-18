---
slug: "bcu"
url: "/mobilnisite/slovnik/bcu/"
type: "slovnik"
title: "BCU – Bearer Control Unit"
date: 2025-01-01
abbr: "BCU"
fullName: "Bearer Control Unit"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bcu/"
summary: "Bearer Control Unit je funkční entita v architektuře 3GPP odpovědná za správu a řízení prostředků přenosových kanálů (bearerů) mezi jádrem sítě a externími paketovými datovými sítěmi. Zajišťuje proced"
---

BCU je funkční entita v architektuře 3GPP, která spravuje prostředky přenosových kanálů (bearerů), zajišťuje jejich zřízení, modifikaci a uvolnění, aby byla dodržena kvalita služeb (QoS) a uplatňování politik pro datové toky uživatele.

## Popis

Bearer Control Unit (BCU) je klíčová funkční komponenta v architektuře Evolved Packet Core (EPC) dle 3GPP, konkrétně definovaná ve specifikaci 3GPP TS 29.231. Funguje jako součást frameworku Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), spolupracuje s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a funkcí Bearer Binding and Event Reporting Function ([BBERF](/mobilnisite/slovnik/bberf/)) při správě datových bearerů mezi jádrem sítě a externími paketovými datovými sítěmi. Primární odpovědností BCU je převádět rozhodnutí politik vysoké úrovně na konkrétní akce na úrovni bearerů, čímž zajišťuje, že datové toky uživatele jsou zpracovávány odpovídajícím způsobem dle předplacených služeb a stavu sítě.

Z architektonického hlediska rozhraní BCU komunikuje s více síťovými elementy, včetně brány Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)), brány Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a entitou Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v sítích LTE. Obsahuje logiku pro operace vázání bearerů, které zahrnují mapování toků služebních dat ([SDF](/mobilnisite/slovnik/sdf/)) na příslušné EPS bearery na základě požadavků QoS a pravidel politik. Jednotka udržuje stavové informace o aktivních bearech, sleduje alokaci prostředků a koordinuje se systémy účtování, aby zajistila správnou korelaci účtování mezi využitím beareru a spotřebou služby. Její činnost je řízena referenčními body Gx a Gxx pro řízení politik a rozhraními S5/S8 pro správu bearerů.

BCU implementuje sofistikované algoritmy pro správu životního cyklu bearerů, včetně řízení přístupu (admission control), vyjednávání parametrů QoS a stanovování priorit bearerů při scénářích zahlcení. Zpracovává pravidla PCC přijatá od PCRF a rozhoduje, zda zřídit nové dedikované bearery, modifikovat stávající bearery, nebo uvolnit bearery, které již nejsou potřeba. Jednotka také zajišťuje vzájemnou spolupráci mezi různými přístupovými technologiemi (jako LTE a ne-3GPP přístupy) udržováním konzistentních politik bearerů napříč heterogenními sítěmi. Její rozhodování zahrnuje informace o síťové zátěži v reálném čase, data z profilů účastníků a požadavky specifické pro služby, aby optimalizovala využití prostředků při zachování kvality služeb.

V praktické implementaci je funkčnost BCU často integrována v rámci PGW v sítích LTE, ačkoli specifikace umožňuje distribuovaná nasazení, kde jsou funkce řízení bearerů odděleny od funkcí přeposílání dat. Jednotka udržuje podrobné kontextové informace o bearech, včetně parametrů QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)), Allocation and Retention Priority (ARP), Guaranteed Bit Rate (GBR) a Maximum Bit Rate (MBR). Podporuje také pokročilé funkce, jako je vytěsnění bearerů (bearer preemption), kdy mohou vysokoprioritní bearery získat zpět prostředky od bearerů s nižší prioritou při síťovém zahlcení, a rozdělení beareru (bearer splitting) pro scénáře s více připojeními, kdy jeden tok služebních dat může procházet více síťovými cestami.

## K čemu slouží

Bearer Control Unit byla zavedena ve verzi 3GPP Release 8 jako součást System Architecture Evolution (SAE) k řešení omezení dřívějších architektur 3GPP v efektivní správě paketových datových služeb. Před LTE/EPC používaly sítě 3G jednodušší mechanismy správy bearerů, které byly těsně provázány s paradigmaty okruhového přepojování a postrádaly potřebnou podrobnou kontrolu pro různé služby založené na IP. BCU byla navržena tak, aby poskytovala jednotný, politikami řízený přístup ke správě bearerů, který by dokázal podporovat širokou škálu požadavků na QoS od nově vznikajících aplikací mobilního širokopásmového připojení.

Primárním motivem pro vytvoření BCU bylo umožnit efektivní využití prostředků při zachování diferenciace služeb ve sítích plně založených na IP. Tradiční přístupy zacházely se vším paketovým datovým provozem podobně, což ztěžovalo garantovat výkon pro aplikace citlivé na zpoždění, jako je VoIP nebo video streaming, a současně zvládat best-effort prohlížení webu. BCU zavedla sofistikované mechanismy vázání a řízení bearerů, které operátorům umožnily implementovat alokaci prostředků s ohledem na služby, a zajistit tak, že kritické aplikace obdrží odpovídající síťové prostředky i v obdobích zahlcení.

Dalším klíčovým problémem, který BCU řeší, je složitost správy více souběžných služeb pro jedno uživatelské zařízení. Protože chytré telefony současně provozují více aplikací, z nichž každá má různé požadavky na QoS, síť potřebuje inteligentní mechanismy pro mapování těchto různorodých požadavků na vhodné přenosové bearery. BCU poskytuje tuto inteligenci analýzou toků služebních dat, aplikací pravidel politik a dynamickým zřizováním nebo modifikací bearerů, jak se mění požadavky služeb. Tato schopnost byla zvláště důležitá pro umožnění nových obchodních modelů, kde operátoři mohli nabízet služební plány s různými úrovněmi výkonnostních záruk.

## Klíčové vlastnosti

- Vázání a mapování bearerů mezi toky služebních dat a EPS bearey
- Dynamické zřizování, modifikace a uvolnění bearerů na základě pravidel politik
- Vynucování parametrů QoS včetně správy QCI, ARP, GBR a MBR
- Vzájemná spolupráce mezi 3GPP a ne-3GPP přístupovými technologiemi pro konzistentní politiky bearerů
- Řízení přístupu (admission control) a alokace prostředků při scénářích síťového zahlcení
- Integrace s frameworkem Policy and Charging Control prostřednictvím rozhraní Gx/Gxx

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TS 29.231** (Rel-19) — Application of SIP-I Protocols to CS Core Network

---

📖 **Anglický originál a plná specifikace:** [BCU na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcu/)
