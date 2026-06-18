---
slug: "rej"
url: "/mobilnisite/slovnik/rej/"
type: "slovnik"
title: "REJ – Reject Frame"
date: 2025-01-01
abbr: "REJ"
fullName: "Reject Frame"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rej/"
summary: "Reject (REJ) rámec je protokolová datová jednotka vrstvy 2 používaná v sítích 3GPP k označení odmítnutí přijatého rámce z důvodu chyb nebo porušení protokolu. Je součástí procedur datové vrstvy, jako"
---

REJ je protokolová datová jednotka vrstvy 2 používaná v sítích 3GPP k signalizaci odmítnutí přijatého rámce z důvodu chyb, čímž žádá o opakovaný přenos jako součást procedur řízení chyb.

## Popis

Reject (REJ) rámec je řídicí rámec používaný v protokolech datové vrstvy v systémech 3GPP, zejména v protokolech jako Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) v UMTS a LTE nebo v signalizačním protokolu Link Access Protocol ([LAP](/mobilnisite/slovnik/lap/)). Funguje jako mechanismus řízení chyb, kde přijímající entita odešle REJ rámec, aby informovala vysílač, že jeden nebo více rámců bylo přijato chybně nebo mimo pořadí, a je tedy třeba je přenést znovu. Tento rámec obsahuje informace, jako jsou sekvenční čísla k identifikaci problematických rámců, což umožňuje selektivní opakovaný přenos a zajišťuje integritu dat.

V kontextu RLC, které pracuje v potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)), je REJ rámec součástí procedury Automatic Repeat Request ([ARQ](/mobilnisite/slovnik/arq/)). Když přijímač RLC detekuje mezeru v sekvenčních číslech přijatých protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) – což indikuje chybějící nebo poškozený rámec – může odeslat řídicí PDU typu REJ vysílači. Toto REJ PDU specifikuje sekvenční číslo první chybějící PDU, což vyvolá opakovaný přenos této PDU a případně následujících. Tento proces pomáhá udržovat doručování v pořadí a spolehlivost přes rozhraní rádiového přenosu, které je náchylné k chybám z důvodu útlumu a rušení.

REJ rámec se také používá ve starších protokolech, jako je LAP pro spojově orientovaná spojení, kde plní podobný účel při zajišťování spolehlivého přenosu rámců přes rozhraní vzdušného přenosu nebo kabelové spoje. V moderních systémech 3GPP, zatímco RLC AM používá REJ rámce, existují i další řídicí rámce, jako je Selective Reject ([SREJ](/mobilnisite/slovnik/srej/)), pro efektivnější opakovaný přenos v některých implementacích. Použití REJ rámců je klíčové pro minimalizaci latence a optimalizaci propustnosti rychlým řešením chyb bez nutnosti úplného opakovaného přenosu celého okna, čímž podporuje požadavky na kvalitu služeb pro různé aplikace.

## K čemu slouží

Reject (REJ) rámec byl zaveden, aby řešil potřebu efektivního řízení chyb v protokolech datové vrstvy v sítích 3GPP, s kořeny ve starších telekomunikačních standardech. V před-3G systémech se řízení chyb často spoléhalo na jednodušší mechanismy, jako je stop-and-wait [ARQ](/mobilnisite/slovnik/arq/), které mohly být pro vysokorychlostní datové služby neefektivní. REJ rámec, jako součást protokolů jako [LAP](/mobilnisite/slovnik/lap/) a později RLC, poskytl dynamičtější způsob řešení chyb rámců tím, že umožnil selektivní opakovaný přenos, čímž zlepšil propustnost a spolehlivost.

REJ rámce řeší problém, jak rychle signalizovat chyby přenosu bez nutnosti úplného opakovaného přenosu všech nepotvrzených rámců, což by plýtvalo šířkou pásma a zvyšovalo latenci. Tím, že umožňují přijímači explicitně požadovat opakovaný přenos konkrétních rámců identifikovaných sekvenčními čísly, REJ rámce usnadňují rychlejší zotavení z chyb, což je zásadní v bezdrátovém prostředí, kde je ztráta paketů běžná. To je obzvláště důležité pro služby v reálném čase a datové aplikace, které vyžadují nízkou latenci a vysokou spolehlivost.

Zavedení REJ rámců v protokolech 3GPP, jako je RLC AM od verze 5 dále, podpořilo vývoj směrem k plně IP sítím a vyšším datovým rychlostem v UMTS a LTE. Řešily omezení předchozích metod řízení chyb integrací s dalšími ARQ mechanismy, jako jsou kladná potvrzení a dotazování, aby vytvořily robustní rámec pro integritu dat přes rozhraní rádiového přenosu.

## Klíčové vlastnosti

- Řídicí rámec používaný pro indikaci chyb v protokolech datové vrstvy
- Obsahuje sekvenční čísla k identifikaci rámců vyžadujících opakovaný přenos
- Podporuje selektivní opakovaný přenos v ARQ procedurách
- Používá se v potvrzovaném režimu RLC pro spolehlivý přenos dat
- Usnadňuje rychlé zotavení z chyb pro minimalizaci latence a zlepšení propustnosti
- Integruje se s dalšími řídicími rámci, jako jsou ACK a SREJ, pro komplexní řízení toku

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)
- [ACK – Acknowledgement](/mobilnisite/slovnik/ack/)
- [SREJ – Selected REJect frame](/mobilnisite/slovnik/srej/)
- [PDU – Protocol Data Unit](/mobilnisite/slovnik/pdu/)

## Definující specifikace

- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data

---

📖 **Anglický originál a plná specifikace:** [REJ na 3GPP Explorer](https://3gpp-explorer.com/glossary/rej/)
