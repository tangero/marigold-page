---
slug: "cmise"
url: "/mobilnisite/slovnik/cmise/"
type: "slovnik"
title: "CMISE – Common Management Information Service Element"
date: 2025-01-01
abbr: "CMISE"
fullName: "Common Management Information Service Element"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/cmise/"
summary: "CMISE je standardizovaný prvek služby aplikační vrstvy OSI definovaný organizací 3GPP pro správu telekomunikačních sítí. Poskytuje společnou sadu služeb pro správu síťových prostředků, umožňuje operac"
---

CMISE je standardizovaný prvek služby aplikační vrstvy OSI definovaný organizací 3GPP pro interoperabilní a dodavateľsky neutrální správu síťových prostředků pomocí operací, jako je řízení objektů a hlášení událostí.

## Popis

Prvek služby CMISE (Common Management Information Service Element) je základní komponentou v rámci architektury Telekomunikační správní sítě (TMN) podle 3GPP, konkrétně na rozhraní mezi provozním systémem (OS) a síťovým prvkem ([NE](/mobilnisite/slovnik/ne/)). Funguje na aplikační vrstvě (vrstva 7) modelu [OSI](/mobilnisite/slovnik/osi/) a je vystavěn nad protokolem [CMIP](/mobilnisite/slovnik/cmip/) (Common Management Information Protocol). CMISE definuje komplexní sadu abstraktních služebních primitiv a souvisejících sémantik, které správní aplikace (manažery) používají k provádění operací nad spravovanými objekty v systémech agentů. Tyto spravované objekty jsou abstrakcemi fyzických nebo logických síťových prostředků, jako je základnová stanice, okruh nebo softwarový proces.

Architektonicky jsou služby CMISE vyvolány rolí Manažera a prováděny rolí Agenta. Služby jsou přenášeny pomocí protokolu CMIP, který běží nad spolehlivou spojově orientovanou prezentační vrstvou, typicky s využitím OSI prezentačních a relačních protokolů. Jádrem CMISE je jeho služební model, který zahrnuje operace pro manipulaci se spravovanými objekty. Klíčová služební primitiva zahrnují M-CREATE, M-DELETE, M-GET (pro získání hodnot atributů), M-SET (pro změnu hodnot atributů), M-ACTION (pro vyvolání specifických akcí) a M-EVENT-REPORT (pro informování manažera o událostech). Tyto operace jsou prováděny nad instancemi objektů identifikovanými ve Stromu správy informací ([MIT](/mobilnisite/slovnik/mit/)), což je hierarchický jmenný prostor.

CMISE funguje tak, že manažer odešle služební požadavek, například M-GET, specifikuje cílové instance objektů pomocí rozsahu a filtrování a atributy k získání. Tento požadavek je namapován do datové jednotky protokolu CMIP a přenesen agentovi. Agent požadavek interpretuje, přistoupí k lokální bázi správy informací ([MIB](/mobilnisite/slovnik/mib/)), kde jsou spravované objekty definovány, provede operaci a vrátí odpověď obsahující výsledky nebo potvrzení. Pro hlášení událostí agent autonomně generuje primitivum M-EVENT-REPORT, aby informoval manažera o změnách stavu, alarmech nebo jiných významných událostech. Tento paradigmata požadavek-odpověď a řízení událostmi tvoří základ pro správu poruch, konfiguraci, správu výkonu a zabezpečení (FCAPS) v sítích 3GPP.

Jeho role v síti 3GPP je kritická pro provoz, správu a údržbu (OAM) síťových prvků, zejména v páteřní síti a historicky při správě síťových prvků GSM a UMTS. Umožňuje standardizovanou vzdálenou správu různých zařízení od různých dodavatelů, čímž zajišťuje, že správní systém operátora může konfigurovat, monitorovat a přijímat alarmy ze všech síťových komponent konzistentně. Zatímco pozdější verze 3GPP začlenily jiné technologie správy jako SNMP a NETCONF/YANG, CMISE (s CMIP) zůstává základní a specifikovanou možností, zejména u starších rozhraní a v některých scénářích správy přenosových sítí.

## K čemu slouží

CMISE bylo vytvořeno, aby řešilo kritický problém interoperability mezi různými dodavateli v oblasti správy telekomunikačních sítí. Před jeho standardizací poskytoval každý výrobce zařízení proprietární rozhraní a protokoly pro správu, což nutilo síťové operátory nasazovat pro každé zařízení od jiného dodavatele samostatné, nekompatibilní systémy správy. To vedlo k vysokým provozním nákladům, složitosti a neefektivitě při správě rozsáhlých heterogenních sítí. Hnací motivací bylo umožnit jednotný, standardizovaný rámec, ve kterém by jeden systém správy mohl komunikovat se síťovými prvky od jakéhokoli kompatibilního dodavatele.

Historický kontext spočívá v širších mezinárodních snahách o standardizaci v 80. a 90. letech 20. století, zejména v rámci Mezinárodní telekomunikační unie ([ITU-T](/mobilnisite/slovnik/itu-t/)) a iniciativy Open Systems Interconnection ([OSI](/mobilnisite/slovnik/osi/)). 3GPP převzalo tyto standardy správy sítí OSI, včetně CMISE/[CMIP](/mobilnisite/slovnik/cmip/), jako základ své architektury TMN pro sítě 2G (GSM) a 3G (UMTS). CMISE poskytovalo nezbytné služby aplikační vrstvy potřebné k realizaci vrstveného modelu TMN a přesně definovaných informačních modelů pro síťové prostředky 3GPP. Vyřešilo problém, jak provádět komplexní, strukturované správní operace (nad rámec jednoduchého přístupu k proměnným) spolehlivým, spojově orientovaným způsobem, což byla v té době omezení jednodušších protokolů, jako je SNMPv1.

Definováním bohaté sady objektově orientovaných správních služeb (vytvořit, smazat, akce, hlášení událostí) umožnilo CMISE sofistikované pracovní postupy konfigurace a správy poruch, které byly nezbytné pro telekomunikační sítě úrovně operátora. Jeho vznik motivovala potřeba robustní, škálovatelné a sémanticky bohaté sady protokolů pro správu, která by dokázala zvládnout složité vztahy a chování telekomunikačních síťových prvků, od ústředen po rádiové základnové stanice, v rámci formalizovaného informačního modelu.

## Klíčové vlastnosti

- Objektově orientovaný model správy: Funguje na spravovaných objektech s atributy, oznámeními a akcemi, což poskytuje strukturovaný pohled na síťové prostředky.
- Komplexní služební primitiva: Definuje plnou sadu služeb včetně M-CREATE, M-DELETE, M-GET, M-SET, M-ACTION a M-EVENT-REPORT pro kompletní správu životního cyklu.
- Určení rozsahu a filtrování: Umožňuje provádět operace nad více objekty pomocí pokročilých schopností určení rozsahu (v rámci podstromu) a filtrování (na základě hodnot atributů).
- Spolehlivý, spojově orientovaný provoz: Vystavěn na prezentační a relační vrstvě OSI, zajišťuje spolehlivé a uspořádané doručování správních interakcí vhodných pro kritickou správu OAM.
- Standardizovaná interoperabilita: Umožňuje správu v prostředí více dodavatelů tím, že poskytuje standardizované služební rozhraní, oddělené od implementace podléhajícího protokolu (CMIP).
- Hlášení řízené událostmi: Podporuje asynchronní oznamování událostí (alarmy, změny stavu) od agentů k manažerům pomocí služby M-EVENT-REPORT.

## Související pojmy

- [CMIP – Common Management Information Protocol](/mobilnisite/slovnik/cmip/)
- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [CMISE na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmise/)
