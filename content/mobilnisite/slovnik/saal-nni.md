---
slug: "saal-nni"
url: "/mobilnisite/slovnik/saal-nni/"
type: "slovnik"
title: "SAAL-NNI – Signalling ATM Adaptation Layer – Network Node Interface"
date: 2025-01-01
abbr: "SAAL-NNI"
fullName: "Signalling ATM Adaptation Layer – Network Node Interface"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/saal-nni/"
summary: "Protokolová vrstva, která adaptuje signalizační zprávy pro přenos přes sítě ATM na rozhraní Network Node Interface. Zajišťuje spolehlivou, spojově orientovanou signalizaci mezi síťovými uzly v sítích"
---

SAAL-NNI je protokolová vrstva, která adaptuje signalizační zprávy pro spolehlivý, spojově orientovaný přenos přes sítě ATM na rozhraní Network Node Interface v sítích UMTS a raných mobilních sítích.

## Popis

Signalling [ATM](/mobilnisite/slovnik/atm/) Adaptation Layer for the Network Node Interface (SAAL-NNI) je klíčová součást zásobníku protokolů definovaná ve specifikacích 3GPP pro UMTS pro přenos signalizačních zpráv přes sítě Asynchronous Transfer Mode (ATM). Funguje konkrétně na rozhraní mezi uzly jádra sítě, například mezi [MSC](/mobilnisite/slovnik/msc/) a [RNC](/mobilnisite/slovnik/rnc/) nebo mezi dvěma MSC. SAAL-NNI není jediný protokol, ale strukturovaná adaptační vrstva, která se nachází mezi signalizačními protokoly vyšších vrstev (jako [BSSAP](/mobilnisite/slovnik/bssap/) nebo [RANAP](/mobilnisite/slovnik/ranap/)) a podkladovou vrstvou ATM. Jejím hlavním účelem je poskytovat službu spolehlivého, spojově orientovaného přenosu dat, která maskuje složitosti a potenciální chyby přenosu založeného na čistých ATM buňkách před vyššími vrstvami.

Architektura SAAL-NNI je založena na doporučeních řady [ITU-T](/mobilnisite/slovnik/itu-t/) Q.2100 a typicky se skládá z několika podvrstev. Jádrovou podvrstvou je Service Specific Connection Oriented Protocol ([SSCOP](/mobilnisite/slovnik/sscop/)), definovaný v Q.2110, který poskytuje opravu chyb, zachování pořadí, řízení toku a správu spojení. SSCOP zajišťuje, že signalizační zprávy jsou doručeny spolehlivě a ve správném pořadí přes inherentně spojově orientovaná, ale potenciálně ztrátová ATM virtuální kanálová spojení ([VCC](/mobilnisite/slovnik/vcc/)). Pod SSCOP Service Specific Coordination Function (SSCF) mapuje služby SSCOP na požadavky konkrétního rozhraní (v tomto případě NNI), jak je definováno v Q.2140. Tato SSCF-NNI adaptuje primitiva SSCOP na potřeby signalizační síťové vrstvy MTP-3b (Message Transfer Part level 3 broadband) nebo přímo na signalizační aplikaci vyšší vrstvy.

Při provozu, když je třeba mezi dvěma síťovými uzly vytvořit signalizační asociaci, vrstva SAAL-NNI spravuje zřízení, údržbu a uvolnění podkladového ATM signalizačního spoje. Segmentuje velké signalizační zprávy z vyšších vrstev do sekvencí protokolových datových jednotek (PDU) pro SSCOP, které jsou následně dále segmentovány na buňky vrstvou ATM. Na přijímací straně SAAL-NNI provádí opětovné složení, detekci chyb pomocí sekvenčních čísel a retransmisi jakýchkoli ztracených PDU pomocí mechanizmu selektivního opakování (ARQ). Tím je zaručena integrita kritických signalizačních zpráv pro řízení hovoru, správu mobility a správu relací. Její role byla zásadní v 3G UMTS Release 99 a Release 4 v okruhově přepínaných jádrech sítě, kde poskytovala robustní základ pro signalizační přenos před úplnou migrací na IP přenos (IPoATM a později čisté IP) v pozdějších vydáních.

## K čemu slouží

SAAL-NNI byla vytvořena, aby řešila potřebu standardizovaného, spolehlivého mechanizmu pro přenos signalizace pro vznikající 3G sítě UMTS, které zpočátku přijaly ATM jako preferovanou transportní technologii pro uživatelskou i řídicí rovinu. Před 3G používaly sítě GSM časový multiplex (TDM) a signalizační sadu SS7 s vrstvami MTP přes 64 kbit/s časové sloty. Přechod na širokopásmové ATM pro 3G vyžadoval novou adaptační metodu pro přenos tradičních telefonních signalizačních protokolů přes buňkově přepínané, spojově orientované virtuální okruhy. Účelem SAAL-NNI bylo tuto adaptaci poskytnout a zajistit, aby byly nad potenciálně ztrátovou sítí ATM zachovány základní vlastnosti signalizace – spolehlivost, doručování ve správném pořadí a řízení toku.

Motivace vycházela z omezení použití samotné čisté ATM Adaptation Layer 5 (AAL5), která poskytuje jednoduchou, nezaručenou službu přenosu rámců vhodnou pro data, ale postrádá robustní obnovu po chybě a správu spojení potřebnou pro kritickou signalizaci. SAAL-NNI se svou podvrstvou SSCOP tuto mezeru zaplnila. Řešila problém, jak integrovat stávající a nové signalizační aplikační protokoly 3GPP s vysokorychlostní, paketově orientovanou páteřní sítí ATM. Její vznik byl hnán průmyslovým konsenzem kolem ATM jako sjednocujícího transportu pro širokopásmovou ISDN a rané 3G sítě, což vyžadovalo standardizovanou adaptační vrstvu pro signalizaci na NNI, aby byla zajištěna interoperabilita mezi zařízeními různých výrobců v jádru sítě.

## Klíčové vlastnosti

- Poskytuje spolehlivou, spojově orientovanou službu přenosu dat pro signalizaci
- Je založena na zásobníku protokolů řady ITU-T Q.2100 pro širokopásmovou signalizaci
- Využívá Service Specific Connection Oriented Protocol (SSCOP) pro opravu chyb a řízení toku
- Obsahuje Service Specific Coordination Function for NNI (SSCF-NNI) pro adaptaci protokolů
- Zajišťuje doručování ve správném pořadí a integritu signalizačních zpráv přes ATM VCC
- Spravuje zřízení, údržbu a uvolnění signalizačních spojů mezi síťovými uzly

## Související pojmy

- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)
- [SSCOP – Service Specific Connection Oriented Protocol](/mobilnisite/slovnik/sscop/)
- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)

## Definující specifikace

- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface

---

📖 **Anglický originál a plná specifikace:** [SAAL-NNI na 3GPP Explorer](https://3gpp-explorer.com/glossary/saal-nni/)
