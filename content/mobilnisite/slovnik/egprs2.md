---
slug: "egprs2"
url: "/mobilnisite/slovnik/egprs2/"
type: "slovnik"
title: "EGPRS2 – Enhanced General Packet Radio Service phase 2"
date: 2025-01-01
abbr: "EGPRS2"
fullName: "Enhanced General Packet Radio Service phase 2"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/egprs2/"
summary: "EGPRS2 je významné vylepšení rádiového přístupového systému GSM/EDGE, které podstatně zvyšuje přenosové rychlosti a spektrální účinnost. Zavádí modulační schémata vyššího řádu, širší šířky pásma a vyl"
---

EGPRS2 je významné vylepšení GSM/EDGE, které zvyšuje přenosové rychlosti a spektrální účinnost využitím modulace vyššího řádu, širších šířek pásma a vylepšeného přizpůsobení rádiového spoje pro podporu pokročilých služeb mobilního širokopásmového přístupu v sítích 2G/3G.

## Popis

EGPRS2 je standardizovaný vývoj technologie [EGPRS](/mobilnisite/slovnik/egprs/) ([EDGE](/mobilnisite/slovnik/edge/)) v rámci rodiny GSM, definovaný 3GPP pro podstatné zvýšení špičkových přenosových rychlostí a celkové kapacity systému. Funguje v rámci stávajících přidělení spektra GSM, avšak zavádí několik klíčových pokroků na fyzické vrstvě. Architektura staví na existující podsystému základnové stanice GSM ([BSS](/mobilnisite/slovnik/bss/)), který zahrnuje základnové přijímací stanice ([BTS](/mobilnisite/slovnik/bts/)) a řadiče základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), přičemž jsou vyžadovány upgrady jak v rádiových jednotkách, tak v jednotkách základního pásma pro podporu nových modulačních a kódovacích schémat.

Technicky EGPRS2 funguje implementací dvou odlišných úrovní: EGPRS2-A a [EGPRS2-B](/mobilnisite/slovnik/egprs2-b/). EGPRS2-A využívá modulaci vyššího řádu, konkrétně 32-QAM a 16-QAM v downlinku a 16-QAM v uplinku, na stávající šířce nosné 200 kHz. To umožňuje vyšší počet bitů na symbol, což přímo zvyšuje přenosovou rychlost. EGPRS2-B zdvojnásobuje symbolovou rychlost použitím širší šířky pásma až 1,6 MHz (skládající se z více nosných po 200 kHz), čímž efektivně zvyšuje kapacitu kanálu. Systém využívá sofistikované algoritmy přizpůsobení spoje, které dynamicky vybírají optimální modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) na základě aktuálních podmínek rádiového kanálu, čímž zajišťují robustní výkon.

Klíčovými komponentami umožňujícími EGPRS2 jsou vylepšené transceivery schopné generovat a demodulovat signály 32-QAM, výkonnější kanálové kódování (Turbo kódy pro vyšší úrovně MCS) a modifikované protokoly ve vrstvě řízení rádiového spoje pro zvládnutí zvýšené propustnosti. Jeho úlohou v síti je poskytovat nákladově efektivní vysokorychlostní datovou nadstavbu na existující infrastruktuře GSM, sloužící jako posilovač kapacity v oblastech, kde je spektrum GSM hojné, ale nasazení LTE ještě není proveditelné. Zachovává zpětnou kompatibilitu, což umožňuje starším zařízením EGPRS a [GPRS](/mobilnisite/slovnik/gprs/) fungovat v téže síti.

## K čemu slouží

EGPRS2 bylo vytvořeno pro řešení exponenciálního růstu mobilního datového provozu a omezení původního EGPRS (EDGE), které nabízelo teoretickou špičkovou rychlost v downlinku 384 kbps. Primární motivací bylo dosáhnout významného skoku ve výkonu v rámci široce nasazeného spektra GSM a poskytnout evoluční cestu pro operátory bez nutnosti okamžité migrace na zcela novou rádiovou přístupovou technologii, jako je UMTS-HSPA nebo LTE. Vyřešilo problém spektrální účinnosti, umožňující přenést více dat na hertz šířky pásma, což je kritické omezení pro mobilní operátory.

Historicky, jak se na konci první dekády 21. století začaly masivně rozšiřovat chytré telefony, poptávka po mobilním přístupu k internetu prudce vzrostla. Zatímco se sítě 3G rozšiřovaly, pokrytí nebylo univerzální a mnoho regionů bylo silně závislých na sítích 2G. EGPRS2 nabídlo praktický upgrade pro prodloužení životnosti a konkurenceschopnosti těchto sítí GSM. Řešilo konkrétní omezení, jako je strop špičkové přenosové rychlosti a neefektivní využití spektra za dobrých rádiových podmínek, zavedením modulace vyššího řádu, která byla dříve v GSM kvůli implementační složitosti a nákladům používána.

Technologii poháněla potřeba podporovat vznikající mobilní širokopásmové aplikace, jako je streamování videa a rychlejší prohlížení webu na stávající infrastruktuře. Poskytovala hladší migrační cestu, umožňující operátorům zlepšit uživatelský zážitek v jejich oblasti pokrytí GSM při plánování dlouhodobějšího přechodu na 3G a 4G. Maximalizací užitku přiděleného spektra pomohlo EGPRS2 oddálit nákladné nové aukce spektra a zhušťování buněk.

## Klíčové vlastnosti

- Zavedení modulace 32-QAM a 16-QAM v downlinku
- Podpora modulace 16-QAM v uplinku
- Možnosti širší šířky kanálu až 1,6 MHz pro EGPRS2-B
- Vylepšené Turbo kódování pro vyšší modulační a kódovací schémata (MCS)
- Dynamické přizpůsobení rádiového spoje v širší sadě úrovní MCS
- Zpětná kompatibilita se staršími terminály EGPRS a GPRS

## Související pojmy

- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [EGPRS2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/egprs2/)
