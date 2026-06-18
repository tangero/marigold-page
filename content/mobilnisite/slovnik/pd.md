---
slug: "pd"
url: "/mobilnisite/slovnik/pd/"
type: "slovnik"
title: "PD – Protocol Discriminator"
date: 2025-01-01
abbr: "PD"
fullName: "Protocol Discriminator"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pd/"
summary: "Pole v hlavičce protokolu sloužící k identifikaci typu přenášené datové jednotky protokolu, což umožňuje multiplexování různých protokolů přes jediné logické spojení. Je klíčové pro správné směrování"
---

PD je pole v hlavičce protokolu, které identifikuje typ datové jednotky protokolu, aby umožnilo multiplexování a zajistilo správné směrování a zpracování zpráv.

## Popis

Identifikátor protokolu (Protocol Discriminator – PD) je základním prvkem v rámci vrstvy [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) a dalších protokolových vrstev v systémech 3GPP. Jedná se o konkrétní oktet nebo pole umístěné na začátku datové jednotky protokolu ([PDU](/mobilnisite/slovnik/pdu/)). Jeho hlavní funkcí je označit protokol, ke kterému zpráva patří, což umožňuje přijímající entitě správně interpretovat následující informační pole. Například v signalizaci NAS mezi uživatelským zařízením (UE) a jádrem sítě PD rozlišuje mezi zprávami správy mobility EPS ([EMM](/mobilnisite/slovnik/emm/)) a zprávami správy relací EPS ([ESM](/mobilnisite/slovnik/esm/)), čímž zajišťuje, že jsou zpracovány příslušným protokolovým stavovým automatem.

Z architektonického hlediska PD funguje na síťové vrstvě (vrstva 3) a je klíčovou součástí schopnosti multiplexování protokolového zásobníku. V řídicí rovině může jediné signalizační spojení přenášet zprávy pro více různých protokolů či subprotokolů. PD funguje jako demultiplexovací klíč. Po přijetí PDU síťová entita nejprve zkontroluje hodnotu PD. Na základě předem definovaného mapování (např. specifický binární kód pro EMM a jiný pro ESM) přepošle zbývající část PDU příslušnému protokolovému handleru. Tento návrh se vyhýbá potřebě samostatných fyzických nebo logických spojení pro každý typ řídicí signalizace a optimalizuje využití prostředků.

Specifikace hodnot PD je přísně řízena a definována ve specifikacích 3GPP, aby byla zajištěna globální interoperability. Například 3GPP TS 24.301 (NAS protokol pro EPS) definuje hodnoty PD pro správu mobility a relací EPS. Jeho role přesahuje pouhou identifikaci; je prvním krokem v protokolovém zpracování, umožňuje zpracování chyb (např. odmítání zpráv s neznámým PD) a zajišťuje bezpečnost a integritu signalizačního toku tím, že směruje zprávy ke správnému bezpečnostnímu kontextu. Bez spolehlivého mechanismu PD by jádro sítě nemohlo efektivně spravovat mobilitu, relace a další klíčové řídicí funkce.

## K čemu slouží

Identifikátor protokolu existuje proto, aby řešil základní problém multiplexování a demultiplexování protokolů přes sdílený transportní mechanismus. Ve složitých telekomunikačních systémech, jako jsou sítě 3GPP, musí mezi síťovými entitami souběžně fungovat četné řídicí protokoly. Vytváření vyhrazeného přenosového kanálu nebo spojení pro každý typ protokolu by bylo velmi neefektivní a špatně škálovatelné. PD poskytuje odlehčenou metodu signalizace v pásmu (in-band) k rozlišení mezi těmito různými toky zpráv na jediném spojení.

Historicky, jak se buněčné systémy vyvíjely z GSM přes UMTS až k LTE a 5G, rostl počet a složitost řídicích protokolů. Mechanismus PD, zavedený již dříve a zachovaný ve všech releasech, poskytl stabilní, zpětně kompatibilní způsob zavádění nových protokolů bez nutnosti zásadní přestavby podkladové transportní architektury. Řeší omezení neprůhledných datových toků, kdy příjemce nemůže určit, jak příchozí data zpracovat. Tím, že jasně označuje každou [PDU](/mobilnisite/slovnik/pdu/), zajišťuje robustní a jednoznačné zpracování zpráv, což je kritické pro spolehlivost sítě, bezpečnost (protože zprávy jsou směrovány ke správné bezpečnostní zpracovávající entitě) a efektivní využití prostředků rádiového rozhraní i jádra sítě.

## Klíčové vlastnosti

- Umožňuje multiplexování zpráv více protokolů přes jediné logické spojení
- Nachází se na začátku datové jednotky protokolu pro okamžitou identifikaci
- Používá standardizované, jedinečné číselné hodnoty pro každý protokol (např. EMM, ESM)
- Usnadňuje správné směrování zpráv ke příslušnému protokolovému stavovému automatu
- Podporuje vývoj sítě tím, že umožňuje přiřazení nových hodnot identifikátoru novým protokolům
- Zásadní pro počáteční parsování zpráv a zpracování chyb (např. odmítnutí neznámého protokolu)

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [EMM – Evolved Mobility Management](/mobilnisite/slovnik/emm/)
- [ESM – Energy Savings Management](/mobilnisite/slovnik/esm/)
- [PDU – Protocol Data Unit](/mobilnisite/slovnik/pdu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PD na 3GPP Explorer](https://3gpp-explorer.com/glossary/pd/)
