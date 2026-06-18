---
slug: "ndt"
url: "/mobilnisite/slovnik/ndt/"
type: "slovnik"
title: "NDT – MnS Network Digital Twin Management service"
date: 2026-01-01
abbr: "NDT"
fullName: "MnS Network Digital Twin Management service"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ndt/"
summary: "Služba správy (MnS) definovaná v 3GPP pro vytváření a správu digitálního dvojčete telekomunikační sítě. Umožňuje simulaci v reálném čase, analytiku a prediktivní optimalizaci chování sítě a podporuje"
---

NDT je služba správy (Management Service) podle 3GPP pro vytváření a správu digitálního dvojčete telekomunikační sítě, která umožňuje simulaci v reálném čase, analytiku a prediktivní optimalizaci pro automatizované provozní úkony.

## Popis

Služba správy digitálního dvojčete sítě (MnS Network Digital Twin Management service, NDT) je standardizované rozhraní služby definované v rámci architektury správy a orchestrace (Management and Orchestration, [MANO](/mobilnisite/slovnik/mano/)) 3GPP, konkrétně pod souborem služeb správy (Management Services, MnS). Poskytuje sadu operací a datových modelů pro vytváření, udržování a interakci s digitálním dvojčetem – tedy virtuální, dynamickou reprezentací – fyzické sítě nebo síťového segmentu. Architektura služby je typicky založena na vztahu producent-konzument, kde systém správy sítě nebo analytická funkce vystupuje jako producent nabízející službu NDT. Konzumenti, jako jsou nástroje pro plánování sítě, platformy pro trénink [AI/ML](/mobilnisite/slovnik/ai-ml/) nebo systémy zajištění služeb, pak mohou službu vyžádat, aby získali synchronizovaný digitální model sítě pro různé provozní úkoly.

Jádrová funkcionalita NDT se točí kolem životního cyklu digitálního dvojčete. To zahrnuje zřizování a instanciaci dvojčete na základě konfigurace fyzické sítě a dat o stavu v reálném nebo téměř reálném čase. Služba definuje mechanismy pro příjem dat, synchronizaci modelu a aktualizace stavu, aby bylo zajištěno, že dvojče přesně odráží svůj fyzický protějšek. Mezi klíčové spravované komponenty patří topologie sítě, konfigurace zdrojů, metriky výkonu, stavy poruch a modely provozu. Digitální dvojče není statický snímek, ale živý model, který může být napájen živou telemetrií, což mu umožňuje simulovat chování sítě za různých podmínek, předpovídat poruchy nebo testovat změny konfigurace před nasazením.

V provozu služba NDT umožňuje automatizaci se zpětnovazební smyčkou (closed-loop) a pokročilou analytiku. Inženýři mohou na dvojčeti spouštět scénáře typu „co kdyby“, jako je simulace dopadu nové softwarové aktualizace, náhlého nárůstu provozu nebo výpadku buňky, aniž by riskovali živou síť. To podporuje proaktivní údržbu, plánování kapacity a optimalizaci spotřeby energie. Její role je klíčová ve vývoji směrem k samoorganizujícím se sítím ([SON](/mobilnisite/slovnik/son/)) a správě založené na záměru (intent-based management), kde digitální dvojče slouží jako sandbox pro ověřování autonomních síťových rozhodnutí. Standardizací této služby 3GPP zajišťuje interoperabilitu mezi systémy správy a platformami digitálních dvojčat od různých dodavatelů, což usnadňuje automatizaci sítí v multivendorovém prostředí.

## K čemu slouží

Služba NDT byla zavedena, aby řešila rostoucí složitost moderních sítí 5G a novějších generací, které jsou softwarově definované, virtualizované a využívají síťové slicing. Tradiční správa sítí, spoléhající se na přímou konfiguraci zařízení a reaktivní monitorování, nedostačuje vzhledem k požadovanému rozsahu, dynamice a agilitě služeb. Manuální plánování a odstraňování problémů je časově náročné a riskuje narušení služeb. Koncept digitálního dvojčete, převzatý z výroby, nabízí řešení vytvořením virtuálního prostředí bez rizika pro síťovou analýzu a experimentování.

Jeho vytvoření bylo motivováno potřebou prediktivní a preskriptivní správy sítě. Před NDT operátoři používali izolované simulační nástroje nebo proprietární implementace digitálních dvojčat, které nebyly integrovány se standardizovanými rozhraními správy. Tento nedostatek standardizace bránil automatizaci a ztěžoval vytvoření komplexního síťového modelu v multivendorovém prostředí. Služba NDT standardizuje rozhraní pro správu digitálního dvojčete, což umožňuje koherentní modelování a přístup k síťovým datům z různých zdrojů autorizovanými aplikacemi. Řeší problém provozních izolovaných systémů (silosů) a umožňuje nové případy užití, jako je optimalizace řízená umělou inteligencí, kde lze z dvojčete bezpečně generovat obrovská množství tréninkových dat, a automatizované akce se zpětnovazební smyčkou lze ověřit před provedením v reálné síti.

## Klíčové vlastnosti

- Standardizovaná správa životního cyklu digitálních dvojčat sítě (vytvoření, aktualizace, odstranění, dotaz)
- Synchronizace topologie, konfigurace a stavových dat z fyzické sítě do dvojčete
- Podpora simulace a analýzy scénářů typu „co kdyby“ na modelu dvojčete
- Integrace s dalšími službami MnS pro automatizaci se zpětnovazební smyčkou a zajištění služeb
- Definice datových modelů pro reprezentaci síťových entit a vztahů v dvojčeti
- Rozhraní producent-konzument umožňující oddělené aplikace pro správu

## Související pojmy

- [MNS – Mobile Network Signalling](/mobilnisite/slovnik/mns/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)

## Definující specifikace

- **TS 28.561** (Rel-20) — Management and Orchestration; Network Digital Twin
- **TR 28.915** (Rel-19) — Management and orchestration; Study on Network Digital Twin

---

📖 **Anglický originál a plná specifikace:** [NDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ndt/)
