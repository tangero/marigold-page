---
slug: "dcep"
url: "/mobilnisite/slovnik/dcep/"
type: "slovnik"
title: "DCEP – Data Channel Establishment Protocol"
date: 2025-01-01
abbr: "DCEP"
fullName: "Data Channel Establishment Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dcep/"
summary: "DCEP je protokol 3GPP používaný k zřizování, správě a ukončování datových kanálů pro služby jako IMS a MCPTT. Funguje jako aplikační protokol, typicky přes TCP nebo SCTP, k vyjednání parametrů kanálu"
---

DCEP je aplikační protokol 3GPP používaný k zřizování, správě a ukončování datových kanálů pro služby jako IMS, fungující přes TCP nebo SCTP za účelem vyjednání parametrů a zajištění spolehlivého doručování.

## Popis

Protokol pro zřizování datových kanálů (Data Channel Establishment Protocol, DCEP) je standardizovaný aplikační protokol definovaný v architektuře 3GPP, primárně specifikovaný v TS 24.371 a TS 24.803. Funguje jako řídicí protokol určený pro zřízení, údržbu a ukončení datových kanálů používaných různými službami, zejména v rámci IP Multimedia Subsystem (IMS) a pro služby Mission Critical Push To Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). DCEP funguje nezávisle na podkladovém přenosu uživatelských dat a poskytuje signalizační rovinu, která vyjednává parametry potřebné k zřízení spolehlivé datové cesty mezi koncovými body, jako je uživatelské zařízení (UE) a aplikační servery.

Architektonicky je DCEP navržen pro přenos přes spolehlivé transportní protokoly, především Transmission Control Protocol (TCP) nebo Stream Control Transmission Protocol ([SCTP](/mobilnisite/slovnik/sctp/)). Protokol definuje sadu zpráv a procedur pro vyjednání kanálu. Typická sekvence zřizování zahrnuje iniciační zprávu DCEP od jednoho koncového bodu, která obsahuje navrhované parametry pro datový kanál. Přijímající koncový bod odpoví zprávou o přijetí nebo zamítnutí. Po přijetí je datový kanál považován za zřízený a může začít přenos vlastních uživatelských dat přes samostatné transportní spojení nebo v rámci stejného spojení pomocí různých proudů, jak bylo vyjednáno. DCEP také zahrnuje zprávy pro řádné uzavření datového kanálu a pro hlášení chyb.

Klíčovými součástmi protokolu jsou formát zpráv, stavové automaty pro správu kanálů a mechanismy vyjednávání parametrů. Zprávy obsahují pole pro jedinečný identifikátor kanálu, typ kanálu (definující povahu přenášených dat), parametry spolehlivosti, prioritu a volitelné informace popisku. Stavový automat protokolu spravuje životní cyklus kanálu od stavu 'Idle' přes 'Establishing' do 'Open' a nakonec 'Closing'. Role DCEP je klíčová pro služby, které vyžadují garantované doručování datových proudů v pořadí, jako je přenos souborů během relace MCPTT nebo sdílení polohových dat, kde prostý best-effort IP přenos není dostačující.

V rámci širší sítě se DCEP integruje s logikou služeb vyšší vrstvy. Například v hovoru MCPTT logika služební vrstvy rozhodne, že je potřeba datový kanál (např. pro odeslání obrázku nebo polohy). Poté vyvolá vrstvu DCEP, aby zřídila kanál s určeným příjemcem či příjemci. Jakmile je handshake DCEP dokončen, služební vrstva je o tom informována a aplikace může začít vysílat data přes nově zřízený kanál. Toto oddělení řídicí (DCEP) a uživatelské datové roviny umožňuje flexibilní a službám vědomé doručování dat.

## K čemu slouží

DCEP byl vytvořen, aby řešil potřebu standardizovaného, spolehlivého a službám vědomého mechanismu pro zřizování datových kanálů v rámci architektury služeb 3GPP. Před jeho specifikací služby vyžadující vyhrazené datové cesty často spoléhaly na ad-hoc metody nebo proprietární signalizaci, což vedlo k problémům s interoperabilitou a složitému zavádění služeb. Rozšíření bohatých komunikačních služeb, zejména služeb pro kritické situace vyžadujících garantovaný přenos dat (jako sdílení obrazu nebo přenos souborů spolu s hlasem), zvýraznilo omezení použití základních rozšíření [HTTP](/mobilnisite/slovnik/http/) nebo [SIP](/mobilnisite/slovnik/sip/) pro všechny scénáře přenosu dat.

Vývoj protokolu byl motivován požadavky služeb pro kritické situace (Mission Critical Services, [MCS](/mobilnisite/slovnik/mcs/)) definovaných od 3GPP Release 12 výše, konkrétně [MCPTT](/mobilnisite/slovnik/mcptt/). Tyto služby požadovaly datové kanály s nízkou latencí, spolehlivé a s prioritou, které by mohly být dynamicky zřizovány během relace. DCEP to poskytuje tím, že nabízí odlehčený protokol specificky navržený pro vyjednání kanálu, oddělený od protokolu řízení relace (jako SIP) a vlastního přenosu médií. Toto oddělení odpovědností zjednodušuje aplikační logiku a zlepšuje spolehlivost.

Historicky tento přístup vyřešil problém, jak bezproblémově přidat komponentu sdílení dat do existující hlasové nebo messagingové relace bez nutnosti nového vyjednání celé relace. Umožňuje, aby parametry jako spolehlivost (např. s/bez zachování pořadí, maximální počet retransmisí) a priorita byly dohodnuty pro každý datový kanál zvlášť, čímž dává síti a koncovým bodům jasné pokyny, jak s provozem nakládat. To byl významný pokrok oproti prostému otevření TCP spojení na aplikační vrstvě, protože DCEP poskytuje standardizovaný rámec pro vyjednání, kterému rozumí všechny síťové prvky a zařízení vyhovující 3GPP.

## Klíčové vlastnosti

- Standardizované procedury zřizování a ukončování kanálů
- Vyjednání parametrů kanálu (typ, spolehlivost, priorita, popisek)
- Fungování přes spolehlivé transporty jako TCP a SCTP
- Oddělení řídicí signalizace od přenosu uživatelských dat
- Podpora více souběžných datových kanálů v rámci jedné relace
- Integrace s rámci služeb 3GPP jako IMS a MCPTT

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)

## Definující specifikace

- **TS 24.371** (Rel-19) — WebRTC IMS Client Access Specification
- **TS 24.803** (Rel-12) — Telepresence using IMS - Study

---

📖 **Anglický originál a plná specifikace:** [DCEP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcep/)
