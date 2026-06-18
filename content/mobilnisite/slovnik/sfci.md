---
slug: "sfci"
url: "/mobilnisite/slovnik/sfci/"
type: "slovnik"
title: "SFCI – Sidelink Feedback Control Information"
date: 2025-01-01
abbr: "SFCI"
fullName: "Sidelink Feedback Control Information"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sfci/"
summary: "Sidelink Feedback Control Information (SFCI, řídicí informace zpětné vazby postranního spoje) je signalizační mechanismus na fyzické vrstvě v NR Sidelink (SL), který přenáší hybridní zpětnou vazbu pro"
---

SFCI je signalizační mechanismus na fyzické vrstvě v NR Sidelink, který přenáší HARQ zpětnou vazbu a další řídicí data přímo mezi uživatelskými zařízeními.

## Popis

SFCI je specifický typ řídicích informací přenášených na rozhraní NR Sidelink, primárně používaný k předávání zpětné vazby za přenosy mezi UE bez průchodu přes základnovou stanici (gNB). Je přenášeno na Physical Sidelink Feedback Channel ([PSFCH](/mobilnisite/slovnik/psfch/)). Obsah SFCI typicky zahrnuje informace [HARQ-ACK](/mobilnisite/slovnik/harq-ack/) (potvrzení/negativní potvrzení) pro dříve přijaté transportní bloky Sidelink Shared Channel ([SL-SCH](/mobilnisite/slovnik/sl-sch/)) a může také zahrnovat hlášení informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) pro podporu adaptace spojení.

Generování a přenos SFCI se řídí režimy přidělování zdrojů a časovými vztahy definovanými ve specifikacích 3GPP. Přijímající UE po dekódování přenosu Sidelink dat ([PSSCH](/mobilnisite/slovnik/pssch/)) vygeneruje bity HARQ-ACK. Tyto bity jsou následně zakódovány, modulovány a namapovány na specifické prvky zdroje v rámci zdroje PSFCH. Zdroje PSFCH jsou periodické a asociované se specifickými fondy zdrojů PSSCH, což umožňuje vysílajícímu UE naslouchat zpětné vazbě na předem určené časové a frekvenční pozici.

Struktura SFCI podporuje jak režimy vysílání/skupinového vysílání (broadcast/groupcast), tak i jednosměrného vysílání (unicast) Sidelink komunikace. Pro skupinové vysílání jsou definovány možnosti jako HARQ-ACK založený pouze na [NACK](/mobilnisite/slovnik/nack/) nebo na všech [ACK](/mobilnisite/slovnik/ack/)/NACK. Zařazení CSI do SFCI umožňuje pokročilé funkce jako indikace kvality kanálu Sidelink ([CQI](/mobilnisite/slovnik/cqi/)), indikace pořadí (RI) a indikátor předkodovací matice (PMI), které jsou klíčové pro efektivní MIMO provoz a správu paprsků ve vysokofrekvenčním NR Sidelink. Tato přímá smyčka zpětné vazby je zásadní pro dosažení spolehlivé komunikace s nízkou latencí v aplikacích V2X, veřejné bezpečnosti a komerční D2D.

## K čemu slouží

SFCI bylo zavedeno v NR Sidelink (Rel-16) k poskytnutí spolehlivého mechanismu zpětné vazby s nízkou latencí pro přímou komunikaci zařízení-zařízení, což je základní požadavek pro pokročilé služby V2X a proximity services. Na rozdíl od LTE Sidelink, které mělo omezené možnosti zpětné vazby, NR Sidelink vyžadovalo robustnější HARQ mechanismus pro podporu případů užití s vysokou spolehlivostí, jako je autonomní řízení a průmyslový IoT, kde je včasné potvrzení bezpečnostních zpráv kritické.

Hlavní problém, který SFCI řeší, je umožnění adaptace spojení s uzavřenou smyčkou a retransmise pro Sidelink, čímž se zlepšuje spolehlivost přenosu a spektrální účinnost. Bez takové zpětné vazby by se UE musela spoléhat na přenosy s otevřenou smyčkou s konzervativními schématy modulace a kódování, což by plýtvalo rádiovými zdroji. SFCI umožňuje vysílajícímu UE přizpůsobit své MCS na základě CSI a retransmitovat pakety pouze v případě přijetí NACK, čímž napodobuje účinnost HARQ v uplink/downlink v celulárních sítích.

Dále SFCI podporuje vývoj směrem k autonomnějšímu provozu Sidelink, zejména v částečně pokrytých a nepokrytých scénářích. Vytvořením přímého řídicího kanálu pro zpětnou vazbu snižuje závislost na síťové infrastruktuře pro koordinaci, což umožňuje spolehlivou D2D komunikaci i tehdy, když není dostupný gNB. Tato schopnost je zásadní pro komunikaci pro klíčové mise a rozšiřuje operační dosah a odolnost 5G sítí.

## Klíčové vlastnosti

- Přenáší HARQ-ACK zpětnou vazbu pro přenosy NR Sidelink dat (PSSCH)
- Přenášeno na Physical Sidelink Feedback Channel (PSFCH)
- Podporuje jak režim ACK/NACK, tak i pouze NACK pro skupinové vysílání (groupcast)
- Může zahrnovat informace o stavu kanálu (CSI) pro adaptaci Sidelink spojení
- Dodržuje definované časové vztahy s asociovanými zdroji PSSCH
- Umožňuje spolehlivou a nízkolatentní přímou komunikaci pro V2X a D2D

## Související pojmy

- [PSFCH – Physical Sidelink Feedback Channel](/mobilnisite/slovnik/psfch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures

---

📖 **Anglický originál a plná specifikace:** [SFCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sfci/)
