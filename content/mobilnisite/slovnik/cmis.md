---
slug: "cmis"
url: "/mobilnisite/slovnik/cmis/"
type: "slovnik"
title: "CMIS – Common Management Information Service"
date: 2025-01-01
abbr: "CMIS"
fullName: "Common Management Information Service"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/cmis/"
summary: "CMIS je standardizovaná sada služeb a protokolů definovaná 3GPP pro správu síťových prvků a zdrojů. Poskytuje společný rámec pro operace jako správa chyb, konfigurace, účtování, výkonu a zabezpečení ("
---

CMIS je standardizovaná sada služeb a protokolů definovaná 3GPP pro správu síťových prvků, poskytující společný rámec pro operace FCAPS za účelem zajištění interoperability mezi dodavateli.

## Popis

Služba společných informací pro správu (Common Management Information Service, CMIS) je klíčovou součástí rámce správy telekomunikační sítě (Telecommunications Management Network, [TMN](/mobilnisite/slovnik/tmn/)) podle 3GPP a poskytuje standardizované definice služeb aplikační vrstvy pro správu sítě. Vychází z doporučení řady [ITU-T](/mobilnisite/slovnik/itu-t/) X.700 a modelu správy systémů [OSI](/mobilnisite/slovnik/osi/). CMIS definuje sadu obecných služeb, jako jsou M-GET, M-SET, M-ACTION, M-CREATE, M-DELETE a M-EVENT-REPORT, které slouží k manipulaci a pozorování spravovaných objektů. Tyto spravované objekty jsou abstraktní reprezentace fyzických nebo logických síťových zdrojů (např. port, softwarový proces, čítač výkonu) definované v bázi informací pro správu (Management Information Base, [MIB](/mobilnisite/slovnik/mib/)). Služby fungují nad protokolem společných informací pro správu (Common Management Information Protocol, [CMIP](/mobilnisite/slovnik/cmip/)), který zajišťuje spolehlivý přenos požadavků a oznámení správy.

Z architektonického hlediska CMIS funguje v modelu manažer-agent. Řídící systém (manažer) vyvolává operace CMIS na spravovaném systému (agent), který obsahuje spravované objekty. Agent provede požadovanou operaci na lokální MIB a vrátí odpověď. Například manažer může použít M-GET k získání měření výkonu nebo M-SET k úpravě konfiguračního parametru. Hlášení událostí je asynchronní, kdy agent použije M-EVENT-REPORT k upozornění manažera na významné události, jako jsou chyby nebo překročení prahů. Tím je oddělena logika správy od podrobností základní komunikace.

Úlohou CMIS je poskytnout bohaté, objektově orientované a sémanticky výkonné rozhraní pro správu. Jeho síla spočívá v možnostech určování rozsahu (scoping) a filtrování, které umožňují, aby jediná operace působila na více spravovaných objektů odpovídajících specifickým kritériím, což snižuje síťový provoz ve srovnání se zjednodušenými protokoly typu požadavek-odpověď. Podporuje potvrzované i nepotvrzované režimy služeb, což nabízí flexibilitu pro různé scénáře správy. Přestože je CMIP/CMIS často spojován se zásobníkem protokolů OSI, v kontextech 3GPP lze tyto služby mapovat na různé podkladové transporty a informační model je klíčový pro definici standardizovaného způsobu správy síťových prvků v systému 3GPP.

## K čemu slouží

CMIS byl vytvořen, aby řešil kritickou potřebu interoperability mezi více dodavateli a efektivní, standardizované správy složitých telekomunikačních sítí. Před jeho přijetím byla správa sítě často proprietární, přičemž každý dodavatel zařízení poskytoval jedinečná rozhraní a protokoly. To činilo integraci systémů správy pro sítě postavené z vybavení více dodavatelů extrémně obtížnou, nákladnou a náchylnou k chybám, což vedlo k provozní neefektivitě a vysokým nákladům na životní cyklus.

Účelem CMIS jako součásti širšího rámce [TMN](/mobilnisite/slovnik/tmn/) je poskytnout jednotnou, technologicky neutrální služební vrstvu pro všechny činnosti správy. Řeší problém sémantické rozdílnosti definováním společného jazyka a sady operací (služeb), které musí podporovat všechny kompatibilní síťové prvky. To umožňuje jedinému systému správy sítě (Network Management System, [NMS](/mobilnisite/slovnik/nms/)) konfigurovat, monitorovat a přijímat alarmy od různorodých síťových prvků – jako jsou základnové stanice, přepínače a směrovače – pomocí stejné konzistentní metodologie. Jeho vytvoření bylo motivováno přechodem k otevřeným systémům a provozními požadavky rozsáhlých veřejných sítí, kde jsou spolehlivost a možnost správy prvořadé.

Tím, že abstrahuje zdroje jako spravované objekty s definovanými atributy, akcemi a oznámeními, CMIS umožňuje výkonné a automatizované pracovní postupy správy. Podporuje komplexní model správy FCAPS (Fault, Configuration, Accounting, Performance, Security), který je nezbytný pro udržení kvality služeb a provozní kondice. Přestože novější technologie správy, jako je [SNMP](/mobilnisite/slovnik/snmp/) a NETCONF/YANG, získaly v určitých doménách popularitu díky své jednoduchosti, definice služeb CMIS a jim podkladové principy objektově orientovaného informačního modelování zůstávají vlivné při návrhu rozhraní správy 3GPP a zajišťují robustní základ pro správu složitých vztahů a chování v mobilních sítích.

## Klíčové vlastnosti

- Standardizované objektově orientané primitivy služeb správy (M-GET, M-SET, M-ACTION atd.)
- Výkonné určování rozsahu (scoping) a filtrování pro provádění operací na více spravovaných objektech současně
- Podpora jak potvrzovaných, tak nepotvrzovaných režimů služeb pro flexibilní interakci
- Asynchronní hlášení událostí (M-EVENT-REPORT) pro alarmy a oznámení
- Integrace s rámcem a architekturou správy telekomunikační sítě (Telecommunications Management Network, TMN) 3GPP
- Základ pro definici spravovaných objektů a chování v bázích informací pro správu (Management Information Bases, MIBs) 3GPP

## Související pojmy

- [CMIP – Common Management Information Protocol](/mobilnisite/slovnik/cmip/)
- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)

## Definující specifikace

- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.602** (Rel-19) — Basic Configuration Management IRP Information Service
- **TS 32.662** (Rel-19) — Configuration Management (CM); Kernel CM IRP
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [CMIS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmis/)
