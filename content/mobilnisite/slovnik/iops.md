---
slug: "iops"
url: "/mobilnisite/slovnik/iops/"
type: "slovnik"
title: "IOPS – Isolated E-UTRAN Operations for Public Safety"
date: 2026-01-01
abbr: "IOPS"
fullName: "Isolated E-UTRAN Operations for Public Safety"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iops/"
summary: "IOPS je funkce 3GPP umožňující základnovým stanicím LTE (E-UTRAN) (eNB) fungovat nezávisle na jádru sítě během mimořádných událostí nebo výpadků sítě. Poskytuje klíčovou lokální komunikaci pro složky"
---

IOPS je funkce 3GPP umožňující stanicím LTE (základnovým stanicím) provozovat se nezávisle na jádru sítě během mimořádných událostí, čímž poskytuje klíčovou lokální komunikaci pro složky integrovaného záchranného systému, když je širší síť nedostupná.

## Popis

Isolated [E-UTRAN](/mobilnisite/slovnik/e-utran/) Operations for Public Safety (IOPS) je specializovaný provozní režim definovaný ve specifikacích 3GPP, který umožňuje skupině uzlů přístupové sítě LTE (E-UTRAN), konkrétně vyspělým NodeB ([eNB](/mobilnisite/slovnik/enb/)), poskytovat místní komunikační služby bez připojení k Evolved Packet Core (EPC) nebo 5G Core (5GC). V tomto režimu eNB vytvářejí soběstačnou síť, která autonomně spravuje rádiové prostředky, mobilitu a základní správu relací. Architektura IOPS zahrnuje jeden eNB, který funguje jako Anchor eNB a přebírá řídicí funkce, které typicky zajišťuje jádro sítě, jako je správa mobility a ukládání kontextu přenosových kanálů. Ostatní eNB ve skupině fungují jako Assisting eNB a připojují se k Anchor eNB přes rozhraní X2.

Fungování IOPS začíná spouštěčem, jako je ztráta přenosové trasy (backhaul) k EPC nebo manuální příkaz. Oprávněné eNB (předkonfigurované pro IOPS) přejdou do izolovaného stavu. Anchor eNB se ustaví, často prostřednictvím předdefinovaného mechanismu priority, a začne vysílat systémové informace označující provoz v režimu IOPS. Koncová zařízení pro integrovaný záchranný systém (PS UE), která jsou speciálně nakonfigurovaná pro podporu IOPS, se pak mohou připojit k této izolované síti. Anchor eNB provádí lokalizovanou verzi připojení a autentizace, případně s využitím předem uložených přihlašovacích údajů nebo místního autentizačního serveru, pokud je k dispozici. Spravuje rádiové přenosové kanály pro hlasové, video a datové služby v omezené geografické oblasti pokrytí skupiny eNB.

Klíčové komponenty zahrnují eNB s podporou IOPS (se vylepšeným softwarem), PS UE s podporou IOPS a případně místní aplikační server (např. pro Group Communication System Enablers). Rozhraní X2 mezi eNB je klíčové pro podporu mobility (předávání hovorů) uvnitř izolované skupiny. Systém podporuje základní služby pro integrovaný záchranný systém, jako je mission-critical push-to-talk ([MCPTT](/mobilnisite/slovnik/mcptt/)), lokalizační služby a nouzové varování. Veškerá komunikace je omezena na místní oblast rádiového pokrytí; neexistuje připojení k veřejnému internetu nebo jiným externím sítím, pokud není lokálně implementována bránová funkce.

Úlohou IOPS je poskytnout záchrannou komunikační síť, když je infrastruktura narušena v důsledku přírodních katastrof, teroristických útoků nebo technických poruch. Zajišťuje, že složky integrovaného záchranného systému mohou pokračovat v koordinaci pomocí vysokorychlostních služeb založených na LTE, a to i v nepřítomnosti síťové infrastruktury. Specifikace jako TS 23.401 ([GPRS](/mobilnisite/slovnik/gprs/) enhancements for E-UTRAN access) a TS 33.401 (3GPP system architecture security) definují postupy a bezpečnostní mechanismy pro IOPS, včetně způsobu bezpečného přechodu UE do izolovaného režimu a zpět a ochrany místní komunikace.

## K čemu slouží

IOPS bylo vytvořeno za účelem řešení kritické zranitelnosti raných sítí LTE pro integrovaný záchranný systém: úplné závislosti na jádru sítě a přenosové trase (backhaul). Tradiční mobilní sítě jsou centralizované; pokud dojde k výpadku lokalit jádra sítě nebo spojení k nim, celá rádiová přístupová síť přestane fungovat. To je pro komunikaci integrovaného záchranného systému pro plnění klíčových úkolů (mission-critical) nepřijatelné, protože spolehlivost je během krizí, které často poškozují infrastrukturu, prvořadá. Před zavedením IOPS spoléhaly složky integrovaného záchranného systému na vyhrazené systémy pozemní mobilní rádiové komunikace ([LMR](/mobilnisite/slovnik/lmr/)) pro lokální odolnost, ty však postrádaly vysokorychlostní datové schopnosti LTE.

Motivací pro standardizaci IOPS v rámci 3GPP bylo umožnit LTE stát se skutečnou širokopásmovou náhradou za starší systémy LMR, ale bez obětování odolnosti. Řeší problém „jediného bodu selhání“ vlastního centralizované architektuře EPC. Tím, že umožňuje [eNB](/mobilnisite/slovnik/enb/) fungovat autonomně, IOPS zajišťuje, že komunikace mezi složkami integrovaného záchranného systému v místě katastrofy může být udržena, i když je nejbližší uzel jádra sítě zničen nebo izolován. Tato schopnost byla klíčovým požadavkem organizací integrovaného záchranného systému po celém světě při plánování přechodu na širokopásmové sítě založené na 3GPP.

Historicky byly požadavky na tuto funkci hnací silou ze strany subjektů, jako je First Responder Network Authority (FirstNet) v USA a dalších národních orgánů pro integrovaný záchranný systém. Její vývoj v Release 13 byl součástí širšího úsilí 3GPP o služby pro plnění klíčových úkolů (Mission Critical). IOPS řeší omezení předchozí komerční mobilní technologie, která byla navržena pro efektivitu a škálovatelnost za stabilních podmínek, nikoli pro přežití v extrémních scénářích. Umožňuje hybridní model, ve kterém mohou sítě pro integrovaný záchranný systém normálně těžit z celoplošných služeb LTE komerční úrovně, ale v případě potřeby plynule přejít na odolný lokalizovaný provoz, a to vše na stejné síťové infrastruktuře a zařízeních.

## Klíčové vlastnosti

- Umožňuje autonomní provoz LTE eNB bez připojení k EPC/5GC
- Podporuje místní připojení, autentizaci a správu relací pro koncová zařízení pro integrovaný záchranný systém (PS UE)
- Poskytuje podporu mobility (předávání hovorů) uvnitř izolované skupiny eNB přes rozhraní X2
- Poskytuje služby pro plnění klíčových úkolů (mission-critical), jako je MCPTT, video a data, v izolovaném režimu
- Zahrnuje mechanismy pro bezpečný vstup do izolovaného provozního stavu a výstup z něj
- Umožňuje přednostní obsazení (pre-emption) a správu priorit pro uživatele z řad integrovaného záchranného systému v izolované síti

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.281** (Rel-19) — Mission Critical Video (MCVideo) Service Requirements
- **TS 22.282** (Rel-19) — Mission Critical Data Service Requirements
- **TR 22.879** (Rel-14) — Mission Critical Video over LTE Feasibility Study
- **TS 22.880** (Rel-14) — Mission Critical Data Communications Study
- **TS 23.180** (Rel-19) — MC services support in IOPS mode
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.778** (Rel-16) — Mission Critical Services in Isolated E-UTRAN (IOPS)
- **TS 23.797** (Rel-13) — Isolated E-UTRAN Operation for Public Safety (IOPS)
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.700** — 3GPP TR 33.700
- **TS 33.897** (Rel-13) — Security for Isolated E-UTRAN Operation (IOPS)
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [IOPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/iops/)
