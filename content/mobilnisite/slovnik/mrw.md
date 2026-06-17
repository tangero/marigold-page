---
slug: "mrw"
url: "/mobilnisite/slovnik/mrw/"
type: "slovnik"
title: "MRW – Move Receiving Window"
date: 2025-01-01
abbr: "MRW"
fullName: "Move Receiving Window"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mrw/"
summary: "Mechanismus protokolu ve vrstvě RLC pro správu prostoru pořadových čísel při přenosu dat v potvrzovaném režimu. Zajišťuje spolehlivé doručování ve správném pořadí řízením okna přijímací vyrovnávací pa"
---

MRW je mechanismus protokolu vrstvy řízení rádiového spoje (RLC), který spravuje okno pořadových čísel přijímače, aby zajistil spolehlivé doručování dat ve správném pořadí a zabránil přetečení vyrovnávací paměti.

## Popis

Move Receiving Window (MRW, přesun přijímacího okna) je klíčový postup v podsystému řízení rádiového spoje (RLC), konkrétně pro přenos dat v potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)) v systémech 3GPP UMTS a LTE. Funguje jako mechanismus řízení toku a správy pořadových čísel. Protokol RLC AM používá pořadová čísla (SN) k identifikaci protokolových datových jednotek (PDU) pro spolehlivé doručování ve správném pořadí. Přijímač udržuje přijímací okno definované dvěma proměnnými: VR(R) (nejnižší SN, který ještě nebyl přijat) a VR([MR](/mobilnisite/slovnik/mr/)) (nejvyšší SN přijatelný pro příjem). K přesunu tohoto okna je v případě potřeby vyvolána procedura MRW.

Její princip je zásadně spojen s procesem potvrzování. Přijímač odesílá STATUS PDU, aby informoval vysílač o správně přijatých PDU, chybějících PDU (prostřednictvím [NACK](/mobilnisite/slovnik/nack/)) a aktuálním stavu okna. Když vysílač obdrží potvrzení pro všechna PDU až do určitého bodu, může je odstranit ze své retransmisní vyrovnávací paměti. Klíčové je, že vysílač odešle příkaz 'Move Receiving Window', často přenášený spolu s datovými PDU nebo odeslaný jako řídicí PDU, aby instruoval přijímač k posunu VR(R). Tato akce efektivně 'posune' spodní hranici přijímacího okna vpřed, uvolní tak prostor v pořadových číslech pro nové přenosy a zabrání obalení konečného prostoru SN, což by způsobilo nejednoznačnost.

Její úloha v síti spočívá v zajištění robustnosti a efektivity vrstvy RLC. Správou okna MRW zabraňuje přetečení vyrovnávací paměti na straně přijímače a udržuje synchronizaci stavů vysílače a přijímače. Je klíčovou součástí pro zvládání scénářů s vysokou přenosovou rychlostí, dlouhými časy odezvy nebo obdobími špatných rádiových podmínek, kdy může docházet k mnoha retransmisím. Bez MRW by se mohla vyčerpat pořadová čísla nebo by se mohla zablokovat vyrovnávací paměť přijímače, což by vedlo k uváznutí protokolu nebo snížení propustnosti. Tento postup je transparentní pro vyšší vrstvy, ale je nezbytný pro spolehlivou datovou službu, kterou RLC AM poskytuje vrstvě PDCP a následně uživatelským aplikacím.

## K čemu slouží

Mechanismus MRW byl vytvořen k řešení základních problémů spolehlivých datalinkových protokolů přes bezdrátové kanály s konečným prostorem pořadových čísel. V raných bezdrátových datových systémech mohlo jednoduché protokolové okno selhat, pokud se pořadová čísla obalila dříve, než byla starší paketa potvrzena, což vedlo k nejednoznačnosti, kdy mohl mít nový paket a velmi starý retransmitovaný paket stejné pořadové číslo. To je obzvláště problematické v mobilních sítích s proměnlivým a potenciálně dlouhým zpožděním.

Jeho účelem je poskytnout explicitní kontrolu nad posunem okna přijímače a synchronizovat stav mezi vysílačem a přijímačem. Tím řeší problém vyčerpání pořadových čísel a zajišťuje, že vysílač ví, která paketa může bezpečně odstranit ze své vyrovnávací paměti. Řeší omezení implicitního posunu okna, který může být na nespolehlivých rádiových spojích náchylný k chybám. Vyžadováním explicitního příkazu k posunu protokol garantuje, že obě strany mají konzistentní pohled na to, která data byla nevratně doručena a která pořadová čísla jsou k dispozici pro opětovné použití, čímž udržuje integritu dat a živost protokolu i v náročných síťových podmínkách.

## Klíčové vlastnosti

- Explicitní posun okna prostřednictvím řídicí signalizace od vysílače k přijímači.
- Zabraňuje vyčerpání pořadových čísel a nejednoznačnosti v protokolu RLC AM.
- Synchronizuje stav vysílače a přijímače pro spolehlivý přenos dat.
- Umožňuje efektivní správu vyrovnávací paměti na straně vysílače i přijímače.
- Integrální součást procedur hlášení stavu (STATUS) a potvrzování v RLC.
- Podporuje datové služby s vysokou propustností tím, že umožňuje nepřetržitý tok dat bez uváznutí protokolu.

## Definující specifikace

- **TS 25.322** (Rel-19) — RLC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MRW na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrw/)
