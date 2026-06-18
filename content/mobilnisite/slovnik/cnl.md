---
slug: "cnl"
url: "/mobilnisite/slovnik/cnl/"
type: "slovnik"
title: "CNL – Co-operative Network List"
date: 2025-01-01
abbr: "CNL"
fullName: "Co-operative Network List"
category: "Management"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/cnl/"
summary: "Řídicí mechanismus, který umožňuje mobilnímu zařízení udržovat a stanovovat priority seznamu preferovaných sítí pro scénáře kooperativního roamingu. Umožňuje zařízením inteligentně vybírat sítě na zák"
---

CNL je řídicí mechanismus, který umožňuje mobilnímu zařízení udržovat a stanovovat priority seznamu preferovaných sítí pro scénáře kooperativního roamingu.

## Popis

Co-operative Network List (CNL, Seznam kooperativních sítí) je funkce správy sítě definovaná ve specifikacích 3GPP, která poskytuje mobilním zařízením strukturovaný přístup k výběru sítě v prostředí více operátorů. Na rozdíl od tradičních mechanismů výběru sítě, které spoléhají na jednoduché seznamy priorit nebo měření síly signálu, CNL zahrnuje obchodní vztahy a servisní dohody mezi operátory, aby usměrňovala chování zařízení. Seznam obsahuje informace o preferovaných sítích, které mají s operátorem domovské sítě uzavřené kooperativní dohody, což umožňuje zařízením činit inteligentnější roamingová rozhodnutí.

Architektonicky CNL funguje v rámci modulu [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module) a frameworku správy zařízení. Seznam je obvykle do USIM zřízen operátorem domovské sítě a může být aktualizován přes vzdušné rozhraní prostřednictvím protokolů správy zařízení. CNL obsahuje záznamy pro konkrétní veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)) spolu s přidruženými parametry, které definují povahu kooperativního vztahu. Tyto parametry mohou zahrnovat úrovně priority, omezení služeb, podmínky platnosti a preferované přístupové technologie pro každou uvedenou síť.

Když mobilní zařízení provádí výběr sítě, konzultuje CNL spolu s dalšími kritérii výběru sítě definovanými v 3GPP TS 23.122. Zařízení vyhodnocuje dostupné sítě vůči záznamům v CNL a dává přednost sítím uvedeným v CNL před těmi, které v něm nejsou zahrnuty. Mechanismus funguje ve spojení s dalšími seznamy pro výběr sítě, jako je Operator Controlled PLMN Selector ([OPLMN](/mobilnisite/slovnik/oplmn/)) a User Controlled PLMN Selector (UPLMN), přičemž CNL poskytuje dodatečnou inteligenci o vztazích mezi operátory. Tento hierarchický přístup zajišťuje, že zařízení vybírají sítě, které nejen poskytují pokrytí, ale také optimální kvalitu služeb a nákladovou efektivitu na základě dohod mezi operátory.

CNL hraje klíčovou roli při správě scénářů mezinárodního roamingu, zejména v příhraničních oblastech, kde může být dostupných více sítí různých operátorů. Tím, že usměrňuje zařízení k sítím s navázanými roamingovými dohodami, CNL pomáhá minimalizovat roamingové náklady, zlepšovat kontinuitu služeb a snižovat selhání výběru sítě. Mechanismus také podporuje diferenciaci služeb, což operátorům umožňuje nasměrovat zařízení k sítím, které podporují konkrétní služby nebo úrovně kvality. Tento kooperativní přístup k výběru sítě představuje významný pokrok oproti tradičním metodám, které považovaly všechny dostupné sítě za stejně vhodné možnosti.

## K čemu slouží

CNL byl vytvořen, aby řešil omezení tradičních mechanismů výběru sítě v stále složitějším prostředí více operátorů. Před implementací CNL mobilní zařízení pro výběr sítě primárně spoléhala na měření síly signálu a jednoduché seznamy priorit, což často vedlo k suboptimálnímu roamingovému zážitku. Zařízení se mohla připojit k sítím se silným signálem, ale s nevýhodnými roamingovými dohodami, což pro uživatele znamenalo vyšší náklady nebo omezenou dostupnost služeb. Rostoucí složitost mezinárodních roamingových dohod a rozšíření sdílení sítí vytvořily potřebu sofistikovanějšího usměrňování výběru sítě.

Primární motivací pro vývoj CNL bylo umožnit operátorům využít jejich obchodní vztahy a kooperativní dohody ke zlepšení uživatelského zážitku během roamingu. Tím, že zařízením poskytli informace o preferovaných partnerských sítích, mohli operátoři zajistit, že jejich účastníci obdrží nejlepší možnou službu, když jsou mimo pokrytí své domovské sítě. To bylo obzvláště důležité, protože mobilní služby se stávaly náročnějšími na přenos dat a uživatelé očekávali bezproblémové připojení bez ohledu na polohu. CNL umožnil operátorům implementovat diferencovanější roamingové strategie, které zohledňovaly faktory přesahující pouhou dostupnost signálu.

Dalším klíčovým účelem CNL bylo snížit selhání výběru sítě a zlepšit kontinuitu služeb během mezinárodního cestování. Tradiční mechanismy často vedly k tomu, že se zařízení pokoušela zaregistrovat v sítích s technickými nebo komerčními omezeními, což mělo za následek selhání registrace a přerušení služeb. Tím, že usměrňoval zařízení k sítím s navázanými kooperativními vztahy, CNL tato selhání snížil a zlepšil celkovou dostupnost sítě. Mechanismus také podpořil vývoj směrem k inteligentnějšímu výběru sítě, který se mohl přizpůsobovat měnícím se síťovým podmínkám a dohodám mezi operátory v čase.

## Klíčové vlastnosti

- Preference sítě definovaná operátorem na základě kooperativních dohod
- Úložiště a správa seznamů sítí založená na USIM
- Integrace se stávajícími mechanismy výběru sítě (OPLMN, UPLMN)
- Podpora hierarchických priorit výběru sítě
- Možnost aktualizace přes vzdušné rozhraní prostřednictvím správy zařízení
- Kompatibilita se scénáři mezinárodního roamingu a příhraničními oblastmi

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [OPLMN – Operator Controlled PLMN (Selector List)](/mobilnisite/slovnik/oplmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TS 29.415** (Rel-19) — Nb User Plane Protocol Specification
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [CNL na 3GPP Explorer](https://3gpp-explorer.com/glossary/cnl/)
