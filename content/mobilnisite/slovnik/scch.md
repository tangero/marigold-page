---
slug: "scch"
url: "/mobilnisite/slovnik/scch/"
type: "slovnik"
title: "SCCH – Synchronization Control Channel"
date: 2025-01-01
abbr: "SCCH"
fullName: "Synchronization Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/scch/"
summary: "Logický kanál v UMTS a NR používaný k přenosu synchronizačních informací a systémových řídicích zpráv. Je klíčový pro počáteční vyhledávání buňky, časové zarovnání a vysílání základních systémových pa"
---

SCCH je logický kanál v UMTS a NR, který přenáší synchronizační a systémové řídicí informace pro počáteční vyhledávání buňky, časové zarovnání a vysílání základních parametrů potřebných pro přístup k síti.

## Popis

Synchronization Control Channel (SCCH) je logický kanál definovaný v architekturách protokolů 3GPP Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). Působí na rozhraní mezi vrstvou 2 (linková vrstva) a vrstvou 1 (fyzická vrstva), kde je mapován na konkrétní fyzické kanály pro přenos. V UMTS je typicky spojován s transportními kanály jako Synchronization Channel ([SCH](/mobilnisite/slovnik/sch/)) a Broadcast Channel ([BCH](/mobilnisite/slovnik/bch/)). V 5G NR jsou jeho funkce integrovány do synchronizačních signálových bloků (SSB) a Physical Broadcast Channel ([PBCH](/mobilnisite/slovnik/pbch/)). Primární úlohou kanálu je přenos kritických systémových informací, které nejsou specifické pro uživatele, ale jsou nezbytné pro celou buňku.

Z architektonického pohledu je SCCH generován vrstvou [RRC](/mobilnisite/slovnik/rrc/) v síti a zpracován vrstvami RLC a MAC před předáním fyzické vrstvě k přenosu. Přenáší zprávy související se synchronizací buňky, jako jsou časové informace pro zarovnání rámců a slotů, a systémové řídicí informace, například hlavní informační bloky ([MIB](/mobilnisite/slovnik/mib/)) a systémové informační bloky ([SIB](/mobilnisite/slovnik/sib/)), a to způsobem vysílání (broadcast). Tento vysílací mechanismus zajišťuje, že všechna uživatelská zařízení (UE) v pokrytí buňky mohou tyto informace přijímat současně bez režie vyhrazené signalizace.

Fungování SCCH je zásadní pro proceduru počátečního přístupu. Když se UE zapne nebo vstoupí do nové oblasti, provede vyhledávání buňky skenováním synchronizačních signálů. Informace přenášené na SCCH umožňují UE dosáhnout časové a frekvenční synchronizace s buňkou, dekódovat identitu buňky a získat základní systémové parametry potřebné k pokračování v náhodném přístupu a navázání RRC spojení. Bez SCCH by se UE nemohla synchronizovat se sítí ani pochopit, jak k ní přistupovat, což z něj činí základní kámen fungování mobilních sítí.

## K čemu slouží

SCCH byl zaveden, aby řešil základní problém, jak uživatelské zařízení (UE) efektivním a standardizovaným způsobem objevuje síť, synchronizuje se s ní a získává od ní základní konfigurační data. Před standardizací 3GPP používaly rané mobilní systémy proprietární metody pro synchronizaci a vysílání systémových informací, což bránilo interoperabilitě a plynulému přechodu mezi sítěmi. SCCH poskytuje jednotnou logickou kanálovou strukturu pro zapouzdření těchto kritických řídicích informací.

Jeho vytvoření bylo motivováno potřebou spolehlivého mechanismu s nízkou latencí pro vysílání parametrů specifických pro buňku všem potenciálním UE. Tento vysílací přístup je mnohem efektivnější než navazování individuálních signalizačních spojení s každým UE pro společné informace. SCCH zajišťuje, že každé UE, bez ohledu na svůj stav (nečinné nebo připojené), má přístup ke stejné základní konfiguraci sítě, časovým referencím a informacím o omezení přístupu, což je klíčové pro stabilitu sítě, řízení zátěže a efektivní správu rádiových zdrojů.

Oddělením funkce synchronizace a systémových informací do vyhrazeného logického kanálu umožnilo 3GPP větší flexibilitu v tom, jak jsou tyto informace mapovány na fyzické zdroje napříč různými technologiemi rádiového přístupu (UTRA, E-UTRA, NR). Tento návrh podporuje vývoj od 3G k 5G, kde se základní fyzické signály (např. primární a sekundární synchronizační signály, PBCH) mohou měnit, ale logická potřeba Synchronization Control Channel zůstává konstantní.

## Klíčové vlastnosti

- Přenáší vysílané systémové informace nezbytné pro přístup k buňce
- Přenáší synchronizační signály pro časové a frekvenční zarovnání UE
- Režim vysílání (broadcast) pro současné obsloužení všech UE v buňce
- Logický kanál mapovaný na konkrétní fyzické kanály (např. SCH, BCH, PBCH)
- Přenáší hlavní informační blok (MIB) a kritické systémové informační bloky (SIB)
- Základní pro procedury počátečního vyhledávání a výběru buňky

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 38.322** (Rel-19) — NR Radio Link Control (RLC) Protocol
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)

---

📖 **Anglický originál a plná specifikace:** [SCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/scch/)
