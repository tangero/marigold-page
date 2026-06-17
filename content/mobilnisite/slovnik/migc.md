---
slug: "migc"
url: "/mobilnisite/slovnik/migc/"
type: "slovnik"
title: "MIGC – MCPTT Imminent peril Group Call"
date: 2025-01-01
abbr: "MIGC"
fullName: "MCPTT Imminent peril Group Call"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/migc/"
summary: "Specifický typ skupinového hovoru zřízeného v rámci skupiny MCPTT pro bezprostřední ohrožení (MIG). Jedná se o skutečnou komunikační relaci zahájenou při aktivním stavu bezprostředního ohrožení, která"
---

MIGC je skupinový hovor s nejvyšší prioritou pro nouzovou hlasovou komunikaci, který je zřízen v rámci skupiny MCPTT pro bezprostřední ohrožení (MIG) při aktivním stavu bezprostředního ohrožení.

## Popis

[MCPTT](/mobilnisite/slovnik/mcptt/) Imminent peril Group Call (MIGC) je realizovaná komunikační relace asociovaná se skupinou MCPTT pro bezprostřední ohrožení ([MIG](/mobilnisite/slovnik/mig/)). Zatímco MIG definuje členství ve skupině a stav nouze, MIGC je aktivní skupinový hovor, který přenáší hlasová média, když je skupina aktivována v situaci bezprostředního ohrožení. Představuje realizaci prioritizovaného komunikačního kanálu, který koncept MIG slibuje.

Z architektonického hlediska je MIGC zřizován a řízen aplikačním serverem MCPTT na žádost autorizovaného uživatele MCPTT (klienta). Signalizace pro sestavení hovoru prochází vrstvou služby MCPTT, která instruuje podkladovou síť 3GPP, aby zřídila přenosové cesty (bearers) se specifickými charakteristikami kvality služby (QoS). Mezi klíčové komponenty patří klienti MCPTT všech členů skupiny, server MCPTT (řídící stav hovoru a řízení práva k mluvení) a prvky jádra sítě (PCRF, PGW/[UPF](/mobilnisite/slovnik/upf/), [SMF](/mobilnisite/slovnik/smf/)), které vynucují QoS politiky. Hovor je identifikován jako skupinový hovor pro bezprostřední ohrožení, což jej odlišuje od běžných skupinových hovorů MCPTT.

Provoz MIGC se řídí přísným postupem. Při zahájení server MCPTT rozpozná stav bezprostředního ohrožení skupiny a uplatní nejvyšší úroveň priority na sestavení hovoru a přenos médií. To typicky zahrnuje použití přednostní úrovně priority (pre-emptive Priority Level) v postupech řízení práva k mluvení MCPTT, což zajišťuje, že žádající uživatel okamžitě získá právo mluvit. Současně síť zřizuje vyhrazené přenosové cesty EPS nebo QoS toky s identifikátorem třídy QoS ([QCI](/mobilnisite/slovnik/qci/)) s vysokou prioritou a hodnotou priority pro přidělení a udržení ([ARP](/mobilnisite/slovnik/arp/)), která může přerušit jiné přenosové cesty. Pakety médií pro MIGC jsou odpovídajícím způsobem označeny a dostávají se prioritního zacházení v celé rádiové přístupové síti (RAN) a jádru sítě. MIGC zůstává aktivní, dokud není explicitně ukončen, a poskytuje tak nepřetržitý, chráněný kanál pro koordinaci krize. Jeho úlohou být definitivní, vysoce integritní hlasový kanál pro personál v ohrožení.

## K čemu slouží

MIGC existuje, aby uvedl koncept skupiny pro bezprostřední ohrožení do provozu, převáděje konfigurovanou definici skupiny na živou, prioritizovanou komunikační relaci. Samotné vymezení skupiny nestačí; systém musí zaručit, že když je v rámci této skupiny za podmínek ohrožení uskutečněn hovor, dostane se mu deterministického, vysoce prioritního zacházení od konce ke konci. Specifikace MIGC to zajišťuje definováním přesného typu hovoru a s ním spojeného chování sítě.

Řeší problém zajištění, aby volání během nouzové situace bez prodlení získalo potřebné síťové zdroje. Předchozí systémy mohly skupinu teoreticky prioritizovat, ale samotné sestavení hovoru mohlo být zpožděno v důsledku přetížení. MIGC nařizuje, že signalizace pro sestavení hovoru i následná přenosová rovina médií jsou obě prioritizovány. Tato prioritizace od konce ke konci je klíčová pro snížení latence od okamžiku stisknutí tlačítka pro vysílání do okamžiku, kdy všichni členové skupiny uslyší zvuk.

Vytvořen spolu s [MIG](/mobilnisite/slovnik/mig/) ve verzi 3GPP Release 13 jako součást [MCPTT](/mobilnisite/slovnik/mcptt/) fáze 1, jeho motivací bylo poskytnout kompletní, standardizovaný postup nouzové komunikace. Řeší omezení ad-hoc nouzových hovorů definováním formalizovaného typu relace, který sítě a zařízení mohou rozpoznat a zvláštním způsobem zpracovat. MIGC zajišťuje interoperabilitu mezi systémy MCPTT různých výrobců a sítěmi pro veřejnou bezpečnost, což garantuje, že hovor pro bezprostřední ohrožení ze zařízení jedné organizace dostane stejné urgentní zacházení v síti jiné organizace, což je zásadní pro přeshraniční incidenty nebo události vzájemné pomoci.

## Klíčové vlastnosti

- Vytvoření hovorové relace v rámci předdefinované skupiny pro bezprostřední ohrožení
- Prioritizace od konce ke konci jak signalizace řízení hovoru, tak médií v uživatelské rovině
- Použití přednostní úrovně priority (pre-emptive Priority Level) v postupech řízení práva k mluvení MCPTT
- Zřízení přenosových cest se zaručenou přenosovou rychlostí s hodnotami QCI/ARP s vysokou prioritou
- Explicitní oznámení všem účastníkům, že se jedná o skupinový hovor pro bezprostřední ohrožení
- Síťově vynucené přidělování zdrojů, které může přerušit jiné probíhající relace

## Související pojmy

- [MIG – MCPTT Imminent peril Group](/mobilnisite/slovnik/mig/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MIGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/migc/)
