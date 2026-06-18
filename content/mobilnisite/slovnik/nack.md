---
slug: "nack"
url: "/mobilnisite/slovnik/nack/"
type: "slovnik"
title: "NACK – Negation ACKnowledgement"
date: 2025-01-01
abbr: "NACK"
fullName: "Negation ACKnowledgement"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nack/"
summary: "Řídicí zpráva signalizující selhání nebo chybu přenosu, používaná v protokolech ARQ/HARQ pro spolehlivé doručování dat. Vyzývá odesílatele k opětovnému přenosu chybějícího nebo poškozeného datového bl"
---

NACK (Negation ACKnowledgement, záporné potvrzení) je řídicí zpráva signalizující selhání přenosu, která vyzývá odesílatele k opětovnému přenosu dat; používá se v protokolech ARQ/HARQ pro zajištění spolehlivého doručování přes rozhraní 3GPP radiových sítí.

## Popis

NACK (Negation ACKnowledgement, záporné potvrzení) je základní zpětnovazební signál v mechanismech [ARQ](/mobilnisite/slovnik/arq/) (Automatic Repeat reQuest) a Hybrid ARQ ([HARQ](/mobilnisite/slovnik/harq/)) definovaných ve specifikacích 3GPP pro UMTS, LTE a NR. Funguje jako součást protokolu pro řízení chyb na vrstvě spojení, primárně ve vrstvách [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control) a [PHY](/mobilnisite/slovnik/phy/) (Physical). Když přijímač nezdekóduje správně transportní blok – z důvodů jako špatné podmínky na kanálu, interference nebo kolize – odešle zpět vysílači zprávu NACK přes vyhrazený zpětnovazební kanál (např. Physical HARQ Indicator Channel ([PHICH](/mobilnisite/slovnik/phich/)) v LTE nebo Physical Uplink Control Channel ([PUCCH](/mobilnisite/slovnik/pucch/))/Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) v NR). Toto záporné potvrzení explicitně informuje odesílatele, že konkrétní datová jednotka identifikovaná sériovým číslem nebo ID HARQ procesu vyžaduje opakovaný přenos.

Technická operace zahrnuje těsné propojení s časovači, sériovými čísly a správou soft bufferu. Po přijetí NACK vysílač naplánuje opakovaný přenos stejné nebo redundantní verze (přírůstková redundance) původních dat. U HARQ, zejména u Chase Combining nebo Incremental Redundancy, přijímač před dalším pokusem o dekódování kombinuje původně přijatý (chybný) paket s opakovaně přenesenou verzí, čímž zvyšuje pravděpodobnost úspěchu. Zpětná vazba NACK je typicky multiplexována se signály [ACK](/mobilnisite/slovnik/ack/) a dalšími řídicími informacemi, což vyžaduje efektivní kódování (např. 1bitový indikátor na HARQ proces) pro minimalizaci režie. Ve scénářích s více komponentními nosiči nebo vrstvami MIMO (multiple input, multiple output) mohou být generována samostatná NACK na nosič nebo kódové slovo.

Její role je zásadní pro dosažení spolehlivých paketových datových služeb, zejména pro aplikace citlivé na zpoždění, jako je VoIP nebo hry v reálném čase, kde by opakování na koncích od konce ke konci (TCP) bylo příliš pomalé. Díky poskytování rychlých opakování na úrovni spojení udržují mechanismy založené na NACK požadovanou propustnost a latenci i při proměnných podmínkách na rádiovém kanálu. Konstrukce zajišťuje, že režim s potvrzením (AM) vrstvy RLC (radio link control) se může na HARQ spolehnout u většiny chyb, což snižuje opakování na vyšších vrstvách a zvyšuje celkovou efektivitu systému.

## K čemu slouží

Mechanismus NACK byl zaveden pro řešení inherentní nespolehlivosti bezdrátových kanálů, kde je běžná ztráta paketů způsobená útlumem, interferencí a šumem. Před standardizovaným HARQ v 3GPP používaly rané celulární systémy jednodušší ARQ typu stop-and-wait nebo vůbec žádná opakování na vrstvě spojení, což vedlo k nízké spektrální efektivitě a nespolehlivým datovým službám. Vytvoření NACK jako součásti HARQ v Release 5 (HSDPA) pro UMTS bylo motivováno potřebou vyšších přenosových rychlostí a nižší latence pro paketově spínané služby, což umožnilo efektivní opakované přenosy bez nadměrného zpoždění signalizace.

Řeší problém neefektivního zotavení po chybách tím, že umožňuje rychlá opakování na fyzické vrstvě, která se přizpůsobují podmínkám na kanálu. Bez NACK by veškeré zotavení po chybách záviselo na protokolech vyšších vrstev, jako je TCP, které zavádějí významné zpoždění kvůli době oběhu a mechanismům řízení zahlcení, což degraduje uživatelský zážitek u interaktivních služeb. Zpětná vazba NACK umožňuje systému agresivněji implementovat adaptivní modulaci a kódování (AMC), protože chyby lze rychle opravit, čímž se provozní bod posouvá blíže k limitu kapacity kanálu.

Historicky její vývoj přes LTE a NR odráží rostoucí požadavky na ultra spolehlivou komunikaci s nízkou latencí (URLLC) a vylepšené mobilní širokopásmové připojení (eMBB). V NR vylepšení jako HARQ založený na skupinách kódových bloků a zpětná vazba s více pokusy umožňují částečná opakování a lepší spolehlivost pro velké transportní bloky, díky čemuž se NACK stává ještě jemnějším a efektivnějším nástrojem pro udržení kvality služeb v 5G a dalších generacích.

## Klíčové vlastnosti

- Explicitní záporná zpětná vazba pro selhání dekódování paketu
- Integrální součást Hybrid ARQ (HARQ) pro rychlá opakování
- Pro přenos využívá vyhrazené fyzické řídicí kanály (např. PHICH, PUCCH)
- Podporuje více HARQ procesů pro nepřetržitý datový tok
- Umožňuje techniky přírůstkové redundance a chase combining
- Usnadňuje adaptaci spojení a robustní výkon za proměnných rádiových podmínek

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [ACK – Acknowledgement](/mobilnisite/slovnik/ack/)
- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)
- [PHICH – Physical Hybrid-ARQ Indicator Channel](/mobilnisite/slovnik/phich/)
- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B
- **TR 25.929** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TS 26.268** (Rel-19) — eCall In-band Modem ANSI-C Code
- **TS 26.269** (Rel-19) — eCall In-band Modem Conformance Testing
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [NACK na 3GPP Explorer](https://3gpp-explorer.com/glossary/nack/)
