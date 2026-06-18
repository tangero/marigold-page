---
slug: "bwt"
url: "/mobilnisite/slovnik/bwt/"
type: "slovnik"
title: "BWT – Block Waiting Time"
date: 2025-01-01
abbr: "BWT"
fullName: "Block Waiting Time"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bwt/"
summary: "Block Waiting Time (BWT) je parametr časovače používaný v protokolech 3GPP, zejména ve vrstvě Radio Link Control (RLC), pro řízení opakovaných přenosů datových bloků. Definuje maximální dobu, po ktero"
---

BWT je časovač používaný ve vrstvě Radio Link Control (RLC) specifikací 3GPP, který definuje maximální dobu, po kterou vysílač čeká na potvrzení před opakovaným odesláním datového bloku.

## Popis

Block Waiting Time (BWT) je klíčový časovací mechanismus ve vrstvě Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) protokolů 3GPP, navržený pro řízení procesu opakovaného přenosu v režimu s potvrzením (Acknowledged Mode, [AM](/mobilnisite/slovnik/am/)). Funguje jako součást protokolu Automatic Repeat Request ([ARQ](/mobilnisite/slovnik/arq/)), kde vysílač odesílá datové bloky a čeká na potvrzení ([ACK](/mobilnisite/slovnik/ack/)) od přijímače. BWT určuje maximální dobu, po kterou bude vysílač čekat na ACK pro konkrétní RLC Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)), než zahájí její opakovaný přenos. Tento časovač se spustí při prvním odeslání PDU a zastaví se po přijetí odpovídajícího ACK. Pokud BWT vyprší dříve, než je ACK přijato, vysílač předpokládá, že PDU byla ztracena nebo poškozena, a odešle ji znovu, čímž zajišťuje spolehlivost dat na náchylném rádiovém spoji.

Architektura BWT je integrována do RLC entity, která zajišťuje segmentaci, konkatenaci a opravu chyb. Mezi klíčové komponenty patří RLC vysílač, který spravuje časovač BWT pro každou nepotvrzenou PDU, a RLC přijímač, který generuje ACK na základě úspěšného příjmu. Hodnota BWT je konfigurovatelná a lze ji nastavit podle podmínek sítě, jako je doba odezvy ([RTT](/mobilnisite/slovnik/rtt/)) a očekávané variace zpoždění. Během provozu vysílač udržuje vyrovnávací paměť pro opakovaný přenos nepotvrzených PDU, přičemž BWT zajišťuje včasné opakované přenosy, aby se zabránilo zablokování a udrželo řízení toku. Tento mechanismus spolupracuje s dalšími časovači RLC, jako je Polling Timer, za účelem optimalizace zpětné vazby a snížení zbytečných opakovaných přenosů.

Úloha BWT v síti spočívá v dosažení rovnováhy mezi spolehlivostí a latencí. Nastavením vhodných hodnot BWT mohou sítě zmírnit dopad ztráty paketů a zároveň se vyhnout nadměrným zpožděním způsobeným předčasnými opakovanými přenosy. V systémech 3GPP je BWT obzvláště důležitý pro služby vyžadující vysokou spolehlivost, jako je VoIP (Voice over IP) nebo signalizační zprávy. Funguje ve spojení s Hybrid ARQ ([HARQ](/mobilnisite/slovnik/harq/)) na fyzické vrstvě, kde HARQ zajišťuje rychlé opakované přenosy a BWT poskytuje záchrannou síť na vyšší vrstvě pro přetrvávající chyby. Tento vrstvený přístup zvyšuje celkovou odolnost systému a zajišťuje plynulé doručování dat napříč vývojem rádiových přístupových technologií od UMTS po 5G NR.

## K čemu slouží

Block Waiting Time (BWT) byl zaveden, aby řešil výzvy spolehlivého přenosu dat přes bezdrátové kanály, které jsou náchylné k chybám způsobeným rušením, útlumem a mobilitou. Před jeho standardizací rané bezdrátové systémy postrádaly sofistikované časovače pro opakované přenosy, což vedlo k neefektivitám, jako jsou zbytečné opakované přenosy nebo dlouhá zpoždění při ztrátě paketů. BWT poskytuje řízený mechanismus pro správu období čekání na potvrzení, řeší problémy se zablokováním dat a optimalizuje propustnost tím, že zajišťuje včasné opakované přenosy pouze v případě potřeby.

Historicky, jak se 3GPP vyvíjelo od Release 4 dále, se s nástupem paketově přepínaných služeb stala potřeba zvýšené spolehlivosti rádiového spoje prvořadou. BWT byl integrován do protokolu [RLC](/mobilnisite/slovnik/rlc/) jako doplněk k HARQ, což nabízí řešení pro opravu chyb na úrovni protokolu. Řeší omezení přístupů s pevnými časovači tím, že umožňuje nastavení hodnot konfigurovatelných sítí, které se přizpůsobují různým podmínkám kanálu a požadavkům služeb. Tato flexibilita podporuje rozmanité aplikace, od služeb reálného času s nízkou latencí až po důvěryhodná data na pozadí, což činí z BWT základní prvek pro kvalitu služeb (QoS) v mobilních sítích.

## Klíčové vlastnosti

- Konfigurovatelná hodnota časovače pro adaptivní řízení opakovaných přenosů
- Integrace s režimem s potvrzením (Acknowledged Mode) v RLC pro spolehlivý přenos dat
- Prevence zablokování dat vynucením maximálních dob čekání na potvrzení
- Podpora různorodých služeb prostřednictvím laditelných parametrů na základě požadavků QoS
- Interakce s HARQ pro vrstvenou opravu chyb v rádiových protokolech
- Zlepšení výkonu propustnosti a latence v proměnných podmínkách kanálu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [BWT na 3GPP Explorer](https://3gpp-explorer.com/glossary/bwt/)
