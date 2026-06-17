---
slug: "mcbts"
url: "/mobilnisite/slovnik/mcbts/"
type: "slovnik"
title: "MCBTS – Multi-Carrier BTS"
date: 2025-01-01
abbr: "MCBTS"
fullName: "Multi-Carrier BTS"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mcbts/"
summary: "Multi-Carrier BTS (MCBTS) je základnová stanice schopná vysílat a přijímat na více rádiových kmitočtových nosných současně. Jedná se o základní technologii pro zvýšení kapacity sítě a spektrální účinn"
---

MCBTS je základnová stanice schopná vysílat a přijímat na více rádiových kmitočtových nosných současně za účelem zvýšení kapacity sítě a spektrální účinnosti, zejména v sítích GSM/EDGE.

## Popis

Multi-Carrier Base Transceiver Station (MCBTS) je klíčovým prvkem v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)). Na rozdíl od tradiční jednonosné [BTS](/mobilnisite/slovnik/bts/), které je přidělen jeden specifický rádiový kmitočtový kanál pro její provoz, je MCBTS navržena tak, aby zvládala více RF nosných v rámci stejné jednotky základnové stanice. Každá nosná představuje odlišný kmitočtový kanál a MCBTS je může provozovat současně, aby paralelně obsluhovala více uživatelů. Tato architektura je klíčová pro rozšíření kapacity buněčné lokality bez nutnosti proporcionálního nárůstu fyzických instalací hardwaru.

Architektonicky se MCBTS skládá ze sdíleného společného vybavení (jako např. napájecí zdroje, řadiče a rozhraní pro backhaul) a více jednotek transceiverů (TRX). Každý TRX je zodpovědný za zpracování jedné nosné. Tyto TRX jsou těsně integrovány, což jim umožňuje sdílet zdroje jako antény, kombinátory a infrastrukturu lokality. Řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) spravuje MCBTS a přiřazuje přenosové a signalizační kanály napříč dostupnými nosnými na základě vytížení a dostupnosti zdrojů. Z rádiového hlediska MCBTS vysílá a přijímá na všech svých nakonfigurovaných nosných současně, čímž efektivně vytváří více logických 'buněk' (často na stejné anténě) z jedné fyzické lokality.

Jeho provoz zahrnuje sofistikované sdružování zdrojů a vyvažování zatížení. Když mobilní stanice zahájí hovor nebo datovou relaci, BSC ve spolupráci s MCBTS vybere volný časový slot na jedné z nečinných nosných. To umožňuje buňce podporovat mnohem více současných spojení než jednonosný systém. Pro datové služby jako EDGE mohou být nosné sdružovány a dynamicky přidělovány pro paketově přepínaný provoz, což zlepšuje propustnost. MCBTS také hraje klíčovou roli ve schématech přeskakování kmitočtů a řízení interference, protože více nosných poskytuje větší diverzitu a možnosti pro optimalizaci rádiového spoje.

Role MCBTS v síti je primárně škálování kapacity a hustoty. Jedná se o nákladově efektivní řešení pro zhušťování sítě, zejména v městských oblastech s vysokou hustotou uživatelů. Nasazením MCBTS může operátor znásobit kapacitu stávajícího místa buňky jednoduše přidáním softwarových licencí a hardwarových modulů TRX, namísto výstavby zcela nových lokalit. Tato technologie byla klíčová pro vývoj sítí GSM/EDGE a zvládnutí počátečního nárůstu mobilního datového provozu před rozšířeným nasazením 3G UMTS a 4G LTE.

## K čemu slouží

MCBTS byl vyvinut k řešení základních kapacitních omezení raných buněčných sítí. Počáteční nasazení GSM často používala jednonosné [BTS](/mobilnisite/slovnik/bts/), které mohly podporovat pouze omezený počet současných hovorů (typicky 8 na nosnou s technologií TDMA). S růstem počtu účastníků, zejména v hustě obydlených městských prostředích, se sítě potýkaly s přetížením, což vedlo k blokování hovorů a špatné kvalitě služeb. Výstavba nových míst buněk pro každou novou nosnou byla drahá a logisticky náročná kvůli problémům se získáváním lokalit a územním plánováním.

Primární motivací bylo zvýšení spektrální účinnosti a kapacity lokality škálovatelným a ekonomickým způsobem. MCBTS umožnil operátorům přidávat kapacitu instalací dalších transceiverů na stávajících lokalitách s využitím sdílené infrastruktury, jako jsou věže, skříně a napájení. Tím se řešil problém 'únavy' z dělení buněk a vysokých kapitálových výdajů. Také zjednodušil plánování sítě a její rozvoj, protože kapacitní upgrady mohly být provedeny rychleji.

Historicky koncept dozrával prostřednictvím 3GPP Releases, přičemž Rel-12 poskytlo významná vylepšení pro vývoj GSM. Umožnil pokročilejší funkce, jako je vícekanálové plánování paketů pro [EDGE](/mobilnisite/slovnik/edge/), což bylo klíčové pro zlepšení datových rychlostí a uživatelského zážitku v éře před všudypřítomným 3G/4G. Koncept MCBTS položil základy pro pozdější vícekanálové technologie v LTE (Carrier Aggregation) a 5G NR, čímž demonstroval trvalý princip kombinace více kmitočtových kanálů pro zvýšení výkonu.

## Klíčové vlastnosti

- Současný provoz na více RF nosných z jedné jednotky BTS
- Sdílené společné hardwarové zdroje (napájení, backhaul, infrastruktura lokality)
- Dynamické přidělování provozu a vyvažování zatížení napříč nosnými
- Podpora zvýšených datových rychlostí prostřednictvím vícekanálového EDGE (ECSD, EGPRS)
- Umožnění rozšíření kapacity bez proporcionálního nárůstu fyzických lokalit
- Základ pro pokročilé rádiové funkce, jako je přeskakování kmitočtů a redukce interference

## Související pojmy

- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [MCBTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcbts/)
