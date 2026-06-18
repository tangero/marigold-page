---
slug: "pppr"
url: "/mobilnisite/slovnik/pppr/"
type: "slovnik"
title: "PPPR – ProSe Per-Packet Reliability"
date: 2025-01-01
abbr: "PPPR"
fullName: "ProSe Per-Packet Reliability"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pppr/"
summary: "ProSe Per-Packet Reliability (PPPR) je parametr QoS pro ProSe, který definuje požadovanou úroveň spolehlivosti pro jednotlivé datové pakety přenášené přes sidelink. Společně s PPPP zajišťuje, že určit"
---

PPPR je parametr QoS pro ProSe, který definuje požadovanou úroveň spolehlivosti pro jednotlivé datové pakety přenášené přes sidelink, a zajišťuje tak, že kritické zprávy (např. bezpečnostní informace V2X) jsou doručeny se zaručenou pravděpodobností úspěchu.

## Popis

[ProSe](/mobilnisite/slovnik/prose/) Per-Packet Reliability (PPPR) je parametr kvality služeb (QoS) zavedený jako doplněk k parametru ProSe Per-Packet Priority ([PPPP](/mobilnisite/slovnik/pppp/)) pro sidelink komunikaci. Zatímco PPPP určuje pořadí vysílání, PPPR určuje požadovanou pravděpodobnost úspěšného doručení paketu. Je vyjádřen jako cílová hodnota spolehlivosti, například pravděpodobnost úspěšného doručení paketu 90 %, 99 % nebo 99,9 %, v rámci definovaného rozpočtu zpoždění na kanálu. Tento parametr je klíčový pro služby, kde samotná priorizace nestačí a je vyžadována zaručená úroveň odolnosti přenosu.

PPPR funguje tak, že ovlivňuje fyzickou vrstvu a strategie správy zdrojů vysílajícího UE. Když je paket označen konkrétní hodnotou PPPR, protokolový zásobník UE použije tento požadavek k výběru vhodných přenosových parametrů. To může zahrnovat volbu robustnějšího schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)), zvýšení vysílacího výkonu v povolených mezích nebo použití technik jako je duplikace paketů (vysílání více kopií stejného paketu přes různé zdroje v čase nebo frekvenci). UE provádí proces adaptace spojení, který zohledňuje cílovou hodnotu PPPR, aktuální podmínky kanálu a charakteristiky vybraného fondu zdrojů, aby dosáhlo cíle spolehlivosti.

Z architektonického hlediska je PPPR součástí profilu QoS pro službu ProSe. Je konfigurován společně s PPPP, často prostřednictvím ProSe funkce nebo předkonfigurací pro standardizované služby jako [V2X](/mobilnisite/slovnik/v2x/). Síť může vysílat nebo poskytovat informace o tom, které úrovně spolehlivosti jsou v dané geografické oblasti nebo fondu zdrojů podporovány. V režimu plánovaném sítí (mode 1) může [eNB](/mobilnisite/slovnik/enb/)/gNB při přidělování sidelink zdrojů zohlednit požadavky na PPPR hlášené UE. V autonomním režimu (mode 2) UE autonomně vybírá zdroje a přenosová schémata z fondu, který podporuje jeho požadovanou úroveň PPPR. Interakce mezi PPPP a PPPR umožňuje sofistikovanou správu provozu; zpráva s vysokou prioritou (vysoká PPPP), například o nouzovém zastavení, by měla také extrémně vysokou PPPR (např. 99,999 %), aby bylo zajištěno její přijetí, potenciálně za cenu vyšší spotřeby zdrojů nebo zpoždění.

## K čemu slouží

PPPR byl vytvořen pro splnění přísných požadavků na spolehlivost pokročilých aplikací [V2X](/mobilnisite/slovnik/v2x/) a průmyslového IoT, které se objevily po počáteční práci na [ProSe](/mobilnisite/slovnik/prose/). Zatímco [PPPP](/mobilnisite/slovnik/pppp/) řešilo problém 'co se vysílá první', nezaručovalo 'zda bude přenos úspěšný'. Rané služby D2D a základní V2X předpokládaly model spolehlivosti typu best-effort. Aplikace jako kooperativní zabránění kolizím, automatizované řízení vozidel a dálkové ovládání strojů však vyžadují předvídatelnou, ultra-spolehlivou komunikaci s nízkou latencí (URLLC) přes sidelink.

Omezení spočívající pouze v mechanismu priority bylo takové, že kritická bezpečnostní zpráva mohla být naplánována k okamžitému vysílání (vysoká PPPP), ale stále mohla být ztracena kvůli špatným podmínkám na kanálu, pokud by byla vysílána s agresivním, vysoce efektivním MCS. PPPR zavádí do sidelink QoS druhou dimenzi, která systému umožňuje v případě potřeby obětovat spektrální účinnost za spolehlivost. Jeho vývoj byl motivován prací 3GPP na vylepšení V2X v Release 14 a novějších, kde se stalo nezbytným splnit přísné výkonnostní cíle stanovené automobilovými a průmyslovými standardy. PPPR umožňuje sidelink podporovat smlouvy o úrovni služeb (SLA) pro doručování paketů, což je základ pro důvěryhodnou přímou komunikaci mezi stroji a vozidly.

## Klíčové vlastnosti

- Definuje cílovou pravděpodobnost úspěšného doručení paketu (např. 99,9 %) pro sidelink pakety
- Ovlivňuje parametry fyzické vrstvy, jako je výběr MCS a vysílací výkon
- Umožňuje přenosové techniky, jako je duplikace paketů pro ultra-spolehlivost
- Spolupracuje s PPPP pro dvourozměrné QoS (priorita + spolehlivost)
- Konfigurovatelné na úrovni jednotlivých paketů nebo služeb prostřednictvím politik ProSe nebo předkonfigurace
- Nezbytné pro podporu požadavků typu URLLC přes sidelink rozhraní PC5

## Související pojmy

- [PPPP – ProSe Per-Packet Priority](/mobilnisite/slovnik/pppp/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR

---

📖 **Anglický originál a plná specifikace:** [PPPR na 3GPP Explorer](https://3gpp-explorer.com/glossary/pppr/)
