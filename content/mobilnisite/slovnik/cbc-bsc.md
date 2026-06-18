---
slug: "cbc-bsc"
url: "/mobilnisite/slovnik/cbc-bsc/"
type: "slovnik"
title: "CBC-BSC – Cell Broadcast Centre - Base Station Controller Interface"
date: 2025-01-01
abbr: "CBC-BSC"
fullName: "Cell Broadcast Centre - Base Station Controller Interface"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbc-bsc/"
summary: "CBC-BSC je standardizované rozhraní mezi centrem pro vysílání buňkami (CBC) a řídicí jednotkou základnových stanic (BSC) v sítích 2G/GSM. Umožňuje doručování zpráv služby vysílání buňkami (CBS) mobiln"
---

CBC-BSC je standardizované rozhraní mezi centrem pro vysílání buňkami (Cell Broadcast Centre) a řídicí jednotkou základnových stanic (Base Station Controller) v sítích 2G/GSM, které umožňuje doručování zpráv služby vysílání buňkami (Cell Broadcast Service) mobilním zařízením ve specifických geografických oblastech.

## Popis

Rozhraní CBC-BSC je kritickou součástí architektury 2G/GSM pro doručování zpráv služby vysílání buňkami ([CBS](/mobilnisite/slovnik/cbs/)). Definované v 3GPP TS 43.059, toto rozhraní funguje mezi centrem pro vysílání buňkami ([CBC](/mobilnisite/slovnik/cbc/)), což je síťová entita zodpovědná za správu a distribuci vysílacích zpráv, a řídicí jednotkou základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), která řídí více základnových přijímacích a vysílacích stanic ([BTS](/mobilnisite/slovnik/bts/)) v geografické oblasti. Rozhraní následuje model klient-server, kde CBC funguje jako server iniciující doručení vysílací zprávy a BSC funguje jako klient, který tyto zprávy přijímá a předává příslušným BTS pro vysílání přes rádiové rozhraní.

Technický provoz rozhraní CBC-BSC zahrnuje několik klíčových typů zpráv a procedur. Když CBC potřebuje vyslat zprávu, odešle BSC zprávu WRITE-REPLACE obsahující obsah vysílání, informace o geografické oblasti (specifikované pomocí seznamů buněk nebo identifikátorů oblasti služby) a parametry plánování. BSC potvrdí příjem zprávou WRITE-REPLACE COMPLETE a následně distribuuje zprávu příslušným BTS. Rozhraní podporuje zrušení zprávy pomocí zpráv KILL, dotazy na stav pomocí zpráv LOAD QUERY a hlášení chyb pomocí zpráv FAILURE. Všechny zprávy jsou přenášeny pomocí protokolu Base Station System Application Part ([BSSAP](/mobilnisite/slovnik/bssap/)) přes signalizační spoje [SS7](/mobilnisite/slovnik/ss7/).

Architektura rozhraní zahrnuje několik funkčních komponent: funkci zpracování zpráv, která zpracovává příchozí požadavky na vysílání, funkci rozlišení geografické oblasti, která mapuje oblasti služby na konkrétní buňky, funkci plánování, která spravuje časování a opakování zpráv, a monitorovací funkci, která sleduje stav doručení zprávy. Rozhraní CBC-BSC podporuje jak okamžité, tak naplánované doručení vysílání s konfigurovatelnými parametry pro rychlost opakování zprávy, dobu platnosti a geografický rozsah. Obsahuje také mechanismy pro řízení zatížení, aby se zabránilo zahlcení sítě při nouzových vysíláních.

Z pohledu sítě hraje rozhraní CBC-BSC zásadní roli při zajišťování spolehlivého doručení zpráv do cílových geografických oblastí. Rozhraní zahrnuje mechanismy obnovy po chybě, schopnosti stanovení priority zpráv (s nejvyšší prioritou pro nouzové zprávy) a podporu různých schémat kódování zpráv. BSC udržuje kontexty vysílacích zpráv pro aktivní vysílání a koordinuje s BTS, aby zajistilo správné naplánování vysílacích slotů na společném řídicím kanálu ([CBCH](/mobilnisite/slovnik/cbch/)). Rozhraní také podporuje scénáře mezinárodního roamingu, kdy je třeba doručit vysílací zprávy navštěvujícím mobilním účastníkům.

## K čemu slouží

Rozhraní CBC-BSC bylo vytvořeno za účelem zavedení standardizovaného mechanismu pro doručování vysílacích zpráv mobilním zařízením ve specifických geografických oblastech v sítích GSM. Před jeho standardizací neexistoval jednotný způsob, jak odesílat informace založené na poloze nebo nouzová upozornění mobilním účastníkům napříč různými výrobci síťových zařízení. Rozhraní vyřešilo problém, jak efektivně distribuovat zprávy pro varování obyvatelstva, výstrahy před počasím, dopravní informace a další obsah specifický pro danou lokalitu bez zahlcení sítě jednotlivými zprávami typu bod-bod.

Historicky se potřeba takového rozhraní ukázala zřejmou s růstem mobilních sítí a s rostoucí kritičností požadavků na systémy varování obyvatelstva. Tradiční zasílání zpráv bod-bod (jako [SMS](/mobilnisite/slovnik/sms/)) bylo pro hromadná oznámení neefektivní, protože vyžadovalo individuální doručení každému účastníkovi v postižené oblasti, což vytvářelo významné zatížení sítě a zpoždění. Rozhraní CBC-BSC umožnilo model doručování jeden-všem, kde mohla být jediná zpráva z CBC efektivně distribuována všem mobilním zařízením v cílových buňkách prostřednictvím existujících vysílacích kanálů.

Rozhraní řešilo několik omezení předchozích přístupů: poskytlo schopnosti geografického cílení, které v dřívějších vysílacích systémech chyběly, zavedlo standardizované protokoly umožňující interoperabilitu mezi zařízeními CBC a BSC od různých výrobců a vytvořilo spolehlivý mechanismus doručení s potvrzením a hlášením stavu. To bylo obzvláště důležité pro záchranné služby a vládní agentury, které potřebovaly zaručené doručení kritických informací obyvatelstvu ve specifických oblastech během katastrof nebo incidentů týkajících se veřejné bezpečnosti.

## Klíčové vlastnosti

- Standardizovaný protokol pro doručování vysílacích zpráv mezi CBC a BSC
- Geografické cílení pomocí seznamů buněk a identifikátorů oblasti služby
- Podpora jak okamžitého, tak naplánovaného doručení vysílání
- Stanovení priority zpráv s možností nouzového vysílání
- Mechanismy řízení zatížení pro prevenci zahlcení sítě
- Funkcionalita obnovy po chybě a hlášení stavu

## Definující specifikace

- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [CBC-BSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbc-bsc/)
