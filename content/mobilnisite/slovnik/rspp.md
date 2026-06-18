---
slug: "rspp"
url: "/mobilnisite/slovnik/rspp/"
type: "slovnik"
title: "RSPP – Ranging and Sidelink Positioning Protocol"
date: 2025-01-01
abbr: "RSPP"
fullName: "Ranging and Sidelink Positioning Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rspp/"
summary: "RSPP je protokol definovaný pro přímou komunikaci mezi zařízeními (postranní rozhraní - sidelink) za účelem provádění měření vzdálenosti a určování polohy. Umožňuje přesné měření vzdálenosti a stanove"
---

RSPP je postranní rozhraní (sidelink) protokol pro přímou komunikaci mezi zařízeními (device-to-device), který umožňuje přesné měření vzdálenosti (ranging) a určování polohy (positioning) mezi UEs bez síťové infrastruktury.

## Popis

RSPP (Ranging and Sidelink Positioning Protocol) je protokolová vrstva specifikovaná v rámci 3GPP pro provádění operací měření vzdálenosti a určování polohy přes rozhraní postranního spoje (sidelink). Sidelink označuje přímou komunikaci mezi uživatelskými zařízeními (UEs) bez směrování dat přes síťovou infrastrukturu (gNB nebo [eNB](/mobilnisite/slovnik/enb/)). RSPP funguje uvnitř zásobníku protokolů postranního spoje a interaguje s vrstvami, jako je Sidelink Radio Link Control (SL-RLC) a Sidelink Medium Access Control (SL-MAC). Jeho primární funkcí je usnadňovat výměnu signálů a zpráv mezi UEs pro odhad vzdálenosti (ranging) a určení relativní nebo absolutní polohy (positioning).

RSPP funguje definováním procedur pro měření a reportování. UEs si vyměňují specifické referenční signály nebo pakety navržené pro měření doby příchodu (ToA), rozdílu dob příchodu (TDoA) nebo úhlu příchodu (AoA). Protokol spravuje plánování těchto signálů, sběr měřicích dat a výpočet vzdálenosti nebo polohy. Podporuje jak jednosměrné, tak obousměrné techniky měření vzdálenosti. Například u obousměrného měření UE A odešle žádost o měření vzdálenosti, UE B odpoví a UE A vypočítá dobu oběhu (round-trip time) pro odhad vzdálenosti, přičemž RSPP zajišťuje posloupnost zpráv a časování. Protokol může také podporovat multilateraci, při které více UEs spolupracuje na určení polohy cílového UE.

Mezi klíčové komponenty RSPP patří definice referenčních signálů pro určování polohy na postranním spoji ([SL-PRS](/mobilnisite/slovnik/sl-prs/)), řídicí zprávy pro zahájení a koordinaci relací měření vzdálenosti a měřicí reporty. Rozhraní má k vyšším vrstvám poskytujícím služby určování polohy a aplikacím. Role RSPP je zásadní ve scénářích, kde nejsou dostupné nebo jsou nespolehlivé signály [GNSS](/mobilnisite/slovnik/gnss/), například uvnitř budov, v městských kaňonech nebo při mimořádných událostech. Využitím přímé komunikace UE-UE umožňuje decentralizovaná řešení pro určování polohy, která jsou odolná, mají nízkou latenci a mohou fungovat s částečným nebo žádným síťovým pokrytím, čímž zlepšují služby jako seskupování vozidel (platooning), bezpečnost chodců nebo sledování majetku.

## K čemu slouží

RSPP bylo zavedeno v 3GPP Release 18, aby pokrylo potřebu přesného určování polohy nezávislého na infrastruktuře ve scénářích komunikace přes postranní spoj (sidelink). Předchozí metody určování polohy v mobilních sítích se primárně spoléhaly na signály v uplinku/downlinku mezi UEs a základnovými stanicemi (např. [OTDOA](/mobilnisite/slovnik/otdoa/), [UTDOA](/mobilnisite/slovnik/utdoa/)) nebo na [GNSS](/mobilnisite/slovnik/gnss/). Tyto metody mají omezení v prostředích bez síťového pokrytí nebo tam, kde není GNSS dostupné. Rozšíření [V2X](/mobilnisite/slovnik/v2x/) (Vehicle-to-Everything) a pokročilých sidelink aplikací vytvořilo poptávku po relativním určování polohy mezi blízkými zařízeními pro podporu zabránění kolizím, kooperativní jízdy a udržování formace.

Protokol řeší problém standardizace způsobů, jak UEs přímo měří vzdálenosti a polohy mezi sebou přes rozhraní PC5. Před RSPP mohly proprietární nebo nestandardizované metody vést k problémům s interoperabilitou. RSPP poskytuje jednotný rámec specifikovaný 3GPP, který zajišťuje, že UEs od různých výrobců mohou provádět měření vzdálenosti a určování polohy spolehlivě. Bylo motivováno případy užití v autonomních vozidlech, veřejné bezpečnosti (např. lokalizace záchranářů v budově) a komerčních aplikacích, jako jsou sociální sítě nebo hry s rozšířenou realitou vyžadující detekci blízkosti. Integrací funkcí určování polohy přímo do zásobníku protokolů postranního spoje RSPP zvyšuje autonomii a funkčnost systémů přímé komunikace mezi zařízeními.

## Klíčové vlastnosti

- Definuje procedury pro měření vzdálenosti (ranging) mezi UEs přes postranní spoj (sidelink)
- Podporuje techniky určování polohy jako ToA, TDoA a obousměrné měření vzdálenosti (two-way ranging)
- Spravuje vysílání a příjem referenčních signálů pro určování polohy na postranním spoji (SL-PRS)
- Koordinuje relace měření vzdálenosti a reportování měření mezi účastnícími se UEs
- Umožňuje určování polohy nezávislé na infrastruktuře a na GNSS
- Umožňuje relativní určování polohy pro V2X, veřejnou bezpečnost a IoT aplikace

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)

## Definující specifikace

- **TS 23.586** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 33.533** (Rel-19) — Security for 5G Ranging & Sidelink Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [RSPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rspp/)
