---
slug: "trxu"
url: "/mobilnisite/slovnik/trxu/"
type: "slovnik"
title: "TRXU – Transceiver Unit"
date: 2020-01-01
abbr: "TRXU"
fullName: "Transceiver Unit"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/trxu/"
summary: "Transceiver Unit (TRXU) je základní hardwarová komponenta základnové stanice zodpovědná za vysílání a příjem rádiových signálů. Provádí klíčové funkce, jako je převod digitálně-analogový, zesílení výk"
---

TRXU je základní hardwarová komponenta základnové stanice zodpovědná za vysílání a příjem rádiových signálů.

## Popis

Transceiver Unit (TRXU) je klíčový hardwarový prvek v rámci rádiové přístupové sítě (RAN), konkrétně integrovaný do základnových stanic jako jsou NodeB, eNodeB a gNB. Funguje jako fyzické rozhraní mezi jednotkou pro zpracování základního pásma ([BBU](/mobilnisite/slovnik/bbu/)) a anténním systémem. Primární role TRXU spočívá v převodu digitálních signálů základního pásma z BBU na analogové rádiové frekvenční ([RF](/mobilnisite/slovnik/rf/)) signály pro vysílání vzduchem, a naopak v převodu přijatých analogových RF signálů zpět na digitální signály základního pásma pro zpracování. Tento obousměrný proces je základní pro veškerou bezdrátovou komunikaci.

Z architektonického hlediska se TRXU typicky skládá z několika klíčových dílčích komponent. Na vysílací větvi obsahuje digitálně-analogový převodník ([DAC](/mobilnisite/slovnik/dac/)), míchače pro převod signálu na požadovanou nosnou frekvenci a výkonový zesilovač ([PA](/mobilnisite/slovnik/pa/)) pro zesílení signálu pro vysílání. Na přijímací větvi obsahuje šumově nízký zesilovač ([LNA](/mobilnisite/slovnik/lna/)) pro zesílení slabých příchozích signálů s minimálním přidaným šumem, míchače pro sestupný převod, filtry pro výběr požadovaného frekvenčního pásma a potlačení rušení a analogově-digitální převodník ([ADC](/mobilnisite/slovnik/adc/)). Pro zajištění čistoty signálu a dodržení přísných spektrálních masek se používají sofistikované filtrační a linearizační techniky.

V rámci síťového ekosystému TRXU pracuje pod kontrolou softwaru základnové stanice a protokolů vyšších vrstev. Zpracovává klíčové procedury fyzické vrstvy, jako je modulace, demodulace a řízení výkonu. Jeho výkonnostní parametry, včetně výstupního výkonu, šumového čísla, linearity a účinnosti, jsou klíčovými faktory určujícími oblast pokrytí buňky, datové toky v uplinku a downlinku a celkovou spolehlivost spoje. V pokročilých architekturách RAN, jako je Cloud RAN (C-RAN) a O-RAN, je TRXU často součástí vzdálené rádiové jednotky (RRU) nebo rádiové jednotky (O-RU), která je fyzicky oddělena od centralizované jednotky základního pásma, což umožňuje flexibilnější a škálovatelnější nasazení sítí.

## K čemu slouží

TRXU existuje, aby splnil základní požadavek jakéhokoli bezdrátového systému: překlenout propast mezi digitální doménou síťového zpracování a analogovou doménou šíření elektromagnetických vln. Bez transceiveru by základnová stanice nemohla komunikovat s uživatelským zařízením (UE). Návrh a optimalizace TRXU jsou hnací silou potřeby efektivního, spolehlivého a vysoce výkonného rádiového vysílání a příjmu.

Historicky, jak se buněčné standardy vyvíjely od 2G do 5G, požadavky na TRXU se dramaticky zvýšily. Musí podporovat širší šířky pásma (např. pro agregaci nosných), složitější modulační schémata (jako 256-QAM a 1024-QAM) a technologie antén s více vstupy a více výstupy ([MIMO](/mobilnisite/slovnik/mimo/)). Dřívější, jednodušší návrhy transceiverů těmto požadavkům nemohly vyhovět, což si vyžádalo pokroky v technologii [RF](/mobilnisite/slovnik/rf/) polovodičů, linearizačních algoritmech a energetické účinnosti. TRXU řeší základní problém převodu a zesílení signálu a zároveň zmírňuje výzvy, jako je spotřeba energie, odvod tepla a zkreslení signálu, které jsou klíčové pro nasazení hustých sítí s vysokou kapacitou.

## Klíčové vlastnosti

- Provádí digitálně-analogový (DAC) a analogově-digitální (ADC) převod signálu
- Obsahuje výkonové zesilovače (PA) pro vysílání a šumově nízké zesilovače (LNA) pro příjem
- Zahrnuje frekvenční míchače pro vzestupný a sestupný převod
- Využívá RF filtry pro výběr pásma a potlačení rušení
- Podporuje klíčové funkce fyzické vrstvy, jako je modulace a řízení výkonu
- Navržen pro specifická frekvenční pásma a šířky pásma dle specifikací 3GPP

## Související pojmy

- [BBU – Base Band Unit](/mobilnisite/slovnik/bbu/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TS 38.809** (Rel-16) — IAB Radio Transmission & Reception Background
- **TS 38.817** — 3GPP TR 38.817

---

📖 **Anglický originál a plná specifikace:** [TRXU na 3GPP Explorer](https://3gpp-explorer.com/glossary/trxu/)
