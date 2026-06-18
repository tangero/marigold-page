---
slug: "csg-id"
url: "/mobilnisite/slovnik/csg-id/"
type: "slovnik"
title: "CSG-ID – Closed Subscriber Group Identity"
date: 2025-01-01
abbr: "CSG-ID"
fullName: "Closed Subscriber Group Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/csg-id/"
summary: "CSG-ID je jedinečný identifikátor přiřazený buňce uzavřené skupiny účastníků (CSG), který omezuje přístup na konkrétní skupinu účastníků. Umožňuje operátorům vytvářet soukromé nebo polosoukromé síťové"
---

CSG-ID je jedinečný identifikátor buňky uzavřené skupiny účastníků (Closed Subscriber Group), který omezuje přístup na konkrétní skupinu účastníků a umožňuje soukromé síťové buňky, jako jsou domácí NodeB.

## Popis

Identita uzavřené skupiny účastníků (CSG-ID) je základní identifikátor v sítích 3GPP, který jednoznačně identifikuje buňku uzavřené skupiny účastníků ([CSG](/mobilnisite/slovnik/csg/)). CSG buňka je buňka, která poskytuje omezený přístup předem definované sadě uživatelských zařízení (UE), známých jako členové CSG. CSG-ID je vysíláno buňkou v systémových informacích a UE jej používá k určení, zda má povolený přístup do dané konkrétní buňky. Tento identifikátor je nezbytný pro implementaci mechanismů řízení přístupu v heterogenních nasazeních sítí, zejména ve scénářích zahrnujících domácí eNodeB (HeNB) nebo femtobuňky.

Z architektonického hlediska je CSG-ID spravováno a zřizováno jádrem sítě a je asociováno s konkrétními profily účastníků na serveru [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server). Když se UE pokouší o přístup k CSG buňce, předloží svá předplatná data CSG, která obsahují seznam CSG-ID, ke kterým patří. Entita [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) provádí řízení přístupu ověřením, zda seznam předplatných CSG UE obsahuje CSG-ID cílové buňky. Toto ověření probíhá během počátečního připojení, aktualizace oblasti sledování nebo procedur předávání, čímž je zajištěno, že se k omezené buňce mohou připojit pouze autorizovaná UE.

CSG-ID funguje ve spolupráci s dalšími síťovými elementy a parametry, aby umožnilo flexibilní režimy přístupu. Kromě uzavřeného přístupu (kde mají přístup pouze členové CSG) mohou CSG buňky pracovat v hybridním režimu přístupu, což umožňuje připojení jak členům CSG, tak nečlenům, ale s prioritními službami pro členy. CSG-ID je zahrnuto v různých signalizačních zprávách, jako jsou zprávy protokolu [S1AP](/mobilnisite/slovnik/s1ap/) (S1 Application Protocol) a [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum), aby usnadnilo správné směrování a vynucování politik. Pravidla [PCC](/mobilnisite/slovnik/pcc/) (Policy and Charging Control), jak jsou definována v 3GPP TS 29.212, odkazují na CSG-ID pro uplatnění specifických politik QoS a účtování na základě typu přístupu a skupiny účastníků.

Z technického hlediska je CSG-ID 27bitová hodnota, která je jedinečně přiřazena v rámci [PLMN](/mobilnisite/slovnik/plmn/). Je součástí informačního elementu ([IE](/mobilnisite/slovnik/ie/)) CSG vysílaného v SIB1 (System Information Block Type 1) pro LTE buňky. Pro 5G NR existují podobné mechanismy s potřebnými adaptacemi. CSG-ID umožňuje síťovým operátorům nasazovat cílená řešení pokrytí, jako jsou rezidenční femtobuňky, podnikové small buňky nebo kampusové sítě, při zachování striktního řízení přístupu. Hraje také roli v řízení mobility, protože UE provádí specifický výběr a převýběr CSG buněk a síť může směrovat UE k CSG buňkám nebo od nich na základě předplatného a politiky.

## K čemu slouží

CSG-ID bylo zavedeno, aby řešilo rostoucí potřebu řízeného přístupu v nasazeních small buněk, zejména s rozšířením femtobuněk a domácích základnových stanic. Před jeho zavedením nabízely mobilní sítě primárně otevřený přístup, kde se jakýkoli účastník operátora mohl připojit k jakékoli buňce. Tento model byl nedostatečný pro scénáře, kde bylo třeba síťové prostředky vyhradit pro konkrétní uživatele, například v rezidenčním, podnikovém nebo kampusovém prostředí. CSG-ID umožňuje operátorům vytvářet soukromé nebo polosoukromé buňky, čímž zajišťuje, že k těmto prostředkům mají přístup pouze autorizovaní účastníci, a tím zlepšuje efektivitu sítě a uživatelský zážitek.

Historicky motivace pro CSG-ID vycházela z potřeby odlehčit provoz v makrosíti a poskytnout vylepšené vnitřní pokrytí prostřednictvím zařízení umístěných u zákazníka. Bez správného řízení přístupu by však taková nasazení mohla vést k rušení, neoprávněnému použití a suboptimální alokaci prostředků. CSG-ID tyto problémy řeší tím, že poskytuje standardizovaný mechanismus pro identifikaci a správu uzavřených skupin účastníků. Umožňuje operátorům nabízet diferencované služby, jako jsou vyšší datové rychlosti nebo vyhrazená kapacita, konkrétním skupinám uživatelů při zachování celistvosti sítě.

Dále CSG-ID usnadňuje hybridní přístupové modely, které vyvažují potřebu omezeného přístupu s flexibilitou obsluhy příležitostných návštěvníků nebo účastníků, kteří nejsou členy. To je obzvláště důležité v podnikovém prostředí, kde zaměstnanci (členové CSG) dostávají prioritní přístup, zatímco návštěvníci se mohou stále připojit se základními službami. CSG-ID tak umožňuje podrobnější a politikami řízený přístup k síti, podporuje širokou škálu obchodních modelů a scénářů nasazení, které nebyly možné s tradičními buňkami s otevřeným přístupem.

## Klíčové vlastnosti

- Jedinečný 27bitový identifikátor pro buňky uzavřené skupiny účastníků (CSG)
- Vysíláno v systémových informacích pro identifikaci UE
- Používáno při ověřování řízení přístupu entitou MME během připojování a předávání
- Podporuje uzavřený, hybridní a otevřený režim přístupu pro flexibilní nasazení
- Odkazováno v pravidlech PCC pro diferenciaci QoS a účtování
- Umožňuje specifické procedury výběru a převýběru CSG buněk

## Definující specifikace

- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol

---

📖 **Anglický originál a plná specifikace:** [CSG-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/csg-id/)
