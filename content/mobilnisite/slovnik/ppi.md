---
slug: "ppi"
url: "/mobilnisite/slovnik/ppi/"
type: "slovnik"
title: "PPI – Payload Protocol Identifier"
date: 2026-01-01
abbr: "PPI"
fullName: "Payload Protocol Identifier"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ppi/"
summary: "Pole v hlavičkách protokolů (jako GTP-U, PDCP nebo RoHC), které identifikuje typ přenášeného datového užitečného zatížení. Umožňuje přijímající entitě správně interpretovat a zpracovat zapouzdřená uži"
---

PPI je pole v hlavičkách protokolů, které identifikuje typ přenášeného datového užitečného zatížení, aby umožnilo jeho správnou interpretaci a zpracování přijímající entitou.

## Popis

Identifikátor protokolu užitečného zatížení (Payload Protocol Identifier, PPI) je klíčové pole používané v různých datových jednotkách protokolů 3GPP k určení povahy zapouzdřeného užitečného zatížení. Slouží jako demultiplexovací klíč, který umožňuje přijímající protokolové entitě určit správný protokol vyšší vrstvy nebo kontext zpracování pro přijatá data. PPI není jediný univerzální identifikátor, ale je definován v kontextu konkrétních přenosových protokolů. Jeho nejvýznamnější použití je v protokolu [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol pro uživatelskou rovinu ([GTP-U](/mobilnisite/slovnik/gtp-u/)), kde pole PPI v hlavičce GTP-U označuje typ užitečného zatížení v tunelu, například IPv4, IPv6 nebo [PPP](/mobilnisite/slovnik/ppp/). To říká Gateway GPRS Support Node (GGSN) nebo Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)), jak zpracovat paket po dekapsulaci.

V jiných kontextech má PPI podobný účel, ale s různými výčtovými hodnotami. Například v Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) pro LTE a NR podobné pole (i když ne vždy nazývané PPI) identifikuje typ datové jednotky (např. IP paket, signalizační zpráva) pro kompresi hlaviček a bezpečnostní zpracování. V profilech Robust Header Compression (RoHC) identifikátor určuje protokol, který je komprimován. PPI je typicky 8bitové nebo 16bitové pole umístěné na pevné pozici v hlavičce protokolu. Přijímající entita toto pole nejprve analyzuje, aby vybrala vhodný handler, dekodér nebo dekompresor pro zbytek paketu.

Z architektonického hlediska PPI umožňuje vrstvení protokolů a multiplexování. Jedna entita protokolu nižší vrstvy (jako GTP-U tunel nebo PDCP entita) může současně přenášet provoz pro více protokolů vyšších vrstev nebo toků služebních dat. PPI poskytuje potřebnou rozlišovací schopnost. Jeho správná interpretace je klíčová pro integritu dat od konce ke konci. Pokud by byla špatně identifikována, mohl by být paket IPv6 mylně předán zásobníku IPv4, což by způsobilo selhání. Proto jsou hodnoty standardizovány v příslušných specifikacích (např. 29.060 pro [GTP](/mobilnisite/slovnik/gtp/), 38.323 pro NR PDCP), aby byla zajištěna interoperabilita mezi zařízeními různých dodavatelů a síťovými rozhraními, jako jsou [S1-U](/mobilnisite/slovnik/s1-u/), S5/S8 a N3.

## K čemu slouží

Identifikátor protokolu užitečného zatížení (PPI) existuje k řešení základního síťového problému multiplexování a demultiplexování více typů provozu přes sdílený transportní mechanismus. V mobilních sítích tunely uživatelské roviny (jako [GTP-U](/mobilnisite/slovnik/gtp-u/)) přenášejí širokou škálu datových užitečných zatížení – webový provoz (IPv4/IPv6), hlas přes IP, data IoT a dokonce i starší PPP rámce. Bez explicitního identifikátoru v hlavičce tunelu by výstupní brána musela provádět hlubokou inspekci paketů nebo spoléhat na implicitní kontext, což je nespolehlivé, neefektivní a nepružné. PPI poskytuje jednoduchý signál v pásmu, který jednoznačně deklaruje typ užitečného zatížení.

Řeší omezení statického nebo implicitního přiřazení užitečného zatížení. Rané datové sítě často předpokládaly jediný typ užitečného zatížení na spojení. Vývoj směrem k multiservisním a multiprotokolovým sítím si vyžádal dynamický a explicitní identifikační mechanismus. PPI umožňuje síti podporovat nové typy užitečného zatížení (jako IPv6 při přechodu z IPv4) bez změny samotného základního tunelovacího protokolu; pouze je třeba rozšířit seznam rozpoznávaných hodnot PPI. To podporuje dopřednou kompatibilitu a plynulý vývoj sítě.

Motivací pro standardizaci PPI napříč různými protokoly (GTP, PDCP) je konzistence a snížení složitosti. Zavedený v dřívějších vydáních pro GTP a významně využívaný od Release 8 s all-IP architekturou LTE se koncept PPI stal ústředním pro flexibilní přenosový model. Je obzvláště kritický v servisně orientované architektuře 5G s network slicing, kde jediná fyzická infrastruktura musí plynule přenášet různé typy provozu s odlišnými požadavky na zpracování. PPI zajišťuje, že každý paket je směrován ke správné virtualizované síťové funkci nebo zásobníku protokolů pro svou zamýšlenou službu.

## Klíčové vlastnosti

- Demultiplexovací klíč v hlavičkách protokolů k identifikaci typu užitečného zatížení (např. IPv4, IPv6, PPP).
- Umožňuje jedné protokolové entitě současně přenášet více typů dat vyšších vrstev.
- Standardizované hodnoty zajišťují interoperabilitu mezi zařízeními různých dodavatelů a síťovými rozhraními.
- Kritický pro správné zpracování užitečného zatížení po dekapsulaci v tunelech jako GTP-U.
- Podporuje vývoj směrem k novým protokolům tím, že umožňuje rozšíření hodnot identifikátorů.
- Používá se v klíčových protokolech včetně GTP-U (řídicí i uživatelská rovina), PDCP a RoHC.

## Související pojmy

- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [Multiplexing](/mobilnisite/slovnik/multiplexing/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 25.820** (Rel-8) — 3G Home NodeB Study Report
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 38.415** (Rel-19) — PDU Session User Plane Protocol

---

📖 **Anglický originál a plná specifikace:** [PPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ppi/)
