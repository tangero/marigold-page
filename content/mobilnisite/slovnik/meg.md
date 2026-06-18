---
slug: "meg"
url: "/mobilnisite/slovnik/meg/"
type: "slovnik"
title: "MEG – MCPTT Emergency Group"
date: 2025-01-01
abbr: "MEG"
fullName: "MCPTT Emergency Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/meg/"
summary: "Předdefinovaná skupina uživatelů určená pro nouzovou komunikaci v rámci služby MCPTT. Umožňuje rychlé, prioritní skupinové hovory pro záchranné složky a personál veřejné bezpečnosti během kritických u"
---

MEG je předdefinovaná skupina uživatelů v rámci služby MCPTT určená pro rychlou, prioritní nouzovou komunikaci, která zajišťuje spolehlivou koordinaci pro záchranné složky během kritických událostí.

## Popis

[MCPTT](/mobilnisite/slovnik/mcptt/) Emergency Group (MEG) je klíčová funkční entita v architektuře služby Mission Critical Push-To-Talk (MCPTT) standardizované 3GPP. Nejde o fyzický síťový prvek, ale o logickou definici skupiny uloženou na aplikačním serveru MCPTT a v přidružených databázích. MEG je předkonfigurovaný, statický nebo dynamický soubor identit uživatelů MCPTT (jednotlivců nebo jiných skupin) oprávněných účastnit se komunikací souvisejících s nouzovými stavy. Definice zahrnuje parametry skupiny, jako je jedinečné Group ID, seznam členů, přidružené úrovně priority a specifické servisní politiky, které řídí, jak jsou nouzové skupinové hovory zřizovány a spravovány.

Operačně, když uživatel MCPTT zahájí nouzový skupinový hovor, cílí požadavek na konkrétní identifikátor MEG. Aplikační server MCPTT po přijetí žádosti o hovor ověří autorizaci uživatele k zahájení hovoru do této MEG a poté pokračuje ve zřízení relace média typu jeden-k-více. Server použije seznam členů MEG k určení sady koncových bodů, kterým musí být doručen mediální proud (typicky hlas). Tento proces zahrnuje signalizaci s podkladovou sítí 3GPP (např. 4G EPC nebo 5G Core), aby bylo zajištěno, že hovor obdrží potřebnou prioritu Quality of Service (QoS), jako jsou přenosy s garantovanou přenosovou rychlostí ([GBR](/mobilnisite/slovnik/gbr/)) a vhodné hodnoty QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)), aby přednostně vytlačil běžný provoz.

Úloha MEG v síti spočívá v poskytování deterministického a rychlého mechanismu pro mobilizaci komunikace mezi specifickou sadou uživatelů během nouzových stavů. Její architektura je těsně integrována s bezpečnostním rámcem služby MCPTT, což zajišťuje, že pouze autorizovaní uživatelé mohou vyvolat nebo se účastnit komunikací MEG. Koncept MEG je zásadní pro transformaci komerčních sítí LTE a 5G na spolehlivé platformy pro veřejnou bezpečnost, posunem za tradiční systémy pozemní mobilní rádiové komunikace ([LMR](/mobilnisite/slovnik/lmr/)) díky nabídce multimédií, integrace s datovými službami mobilních sítí a síťově řízené priority.

## K čemu slouží

MEG byla vytvořena, aby řešila kritickou potřebu okamžité a koordinované hlasové komunikace mezi týmy záchranných složek (např. policie, hasiči, záchranná služba) během nouzových situací. Před standardizací 3GPP se komunikace pro veřejnou bezpečnost silně spoléhala na proprietární systémy pozemní mobilní rádiové komunikace ([LMR](/mobilnisite/slovnik/lmr/)), které často trpěly omezenou kapacitou, izolovanými sítěmi a neschopností snadno se integrovat se širokopásmovými datovými službami nebo koordinovat napříč různými agenturami. Koncept MEG v rámci [MCPTT](/mobilnisite/slovnik/mcptt/) využívá infrastrukturu komerčních mobilních sítí k poskytnutí standardizovaného, interoperabilního a funkčně bohatého systému skupinové komunikace.

Primární problém, který MEG řeší, je zpoždění a nejistota při navazování komunikace s konkrétním týmem na počátku události. Díky předdefinování skupin lze nouzový hovor zahájit jedinou akcí, která okamžitě dosáhne všech určených členů bez ohledu na jejich polohu v rámci pokrytí sítě. Tím odpadá potřeba ručního vytáčení nebo koordinace rádiového kanálu během vysoce stresových scénářů. Dále řeší omezení dřívějších hlasových služeb v mobilních sítích (jako VoLTE), kterým chyběly standardizované, sítí vynucované prioritní mechanismy pro specifické skupiny uživatelů v nouzových scénářích, a zajišťuje, že hovory MEG obdrží potřebné síťové zdroje, aby uspěly i v podmínkách přetížení.

## Klíčové vlastnosti

- Předkonfigurované členství ve skupině pro rychlé zřízení hovoru
- Integrace s procedurami a prioritizací nouzových hovorů MCPTT
- Podpora statických i dynamických seznamů členů
- Asociace se síťovými politikami QoS pro garantované zdroje
- Zabezpečená autorizace a autentizace pro přístup ke skupině
- Základ pro službu MCPTT Emergency Group Call (MEGC)

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [MEGC – MCPTT Emergency Group Call](/mobilnisite/slovnik/megc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MEG na 3GPP Explorer](https://3gpp-explorer.com/glossary/meg/)
