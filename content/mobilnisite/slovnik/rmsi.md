---
slug: "rmsi"
url: "/mobilnisite/slovnik/rmsi/"
type: "slovnik"
title: "RMSI – Remaining Minimum System Information"
date: 2025-01-01
abbr: "RMSI"
fullName: "Remaining Minimum System Information"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rmsi/"
summary: "Remaining Minimum System Information (RMSI, zbývající minimální systémové informace) je kritický soubor bloků systémových informací vysílaných v 5G NR, obsahující základní parametry pro počáteční přís"
---

RMSI je soubor základních bloků systémových informací vysílaných v 5G NR, který poskytuje parametry pro počáteční přístup k buňce, jako je konfigurace náhodného přístupu, které nejsou zahrnuty v MIB.

## Popis

Remaining Minimum System Information (RMSI, zbývající minimální systémové informace) je základní součást vysílací architektury systémových informací ([SI](/mobilnisite/slovnik/si/)) v 5G New Radio (NR). Je přenášena přes Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) a je plánována Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) pomocí specifického System Information-Radio Network Temporary Identifier ([SI-RNTI](/mobilnisite/slovnik/si-rnti/)). RMSI není jediný monolitický blok, ale typicky odkazuje na první blok systémových informací ([SIB1](/mobilnisite/slovnik/sib1/)) v NR, který obsahuje nejdůležitější informace, které User Equipment (UE) potřebuje po úspěšném dekódování Master Information Block ([MIB](/mobilnisite/slovnik/mib/)) z Synchronization Signal Block (SSB).

Obsah RMSI je rozsáhlý a klíčový pro počáteční přístup a výběr/převýběr buňky. Mezi klíčové parametry patří: šířka pásma buňky pro downlink a uplink, konfigurace Physical Random Access Channel ([PRACH](/mobilnisite/slovnik/prach/)) včetně preambulí a časových/frekvenčních zdrojů, omezení přístupu k buňce (jako uzavření buňky a rezervace pro specifická UE) a seznam plánovacích informací pro další bloky systémových informací ([SIB](/mobilnisite/slovnik/sib/)). Plánovací informace sdělují UE, kdy a kde najít další SIB (jako SIB2, SIB3 atd.), které obsahují informace pro mobilitu, konfigurace měření a společné konfigurace rádiových zdrojů. Přenos RMSI je těsně spjat se SSB; každý SSB je asociován se specifickou konfigurací RMSI, což umožňuje flexibilní nasazení v různých frekvenčních pásmech (FR1 a FR2).

Z procedurálního hlediska UE provede počáteční synchronizaci detekcí Primary Synchronization Signal (PSS) a Secondary Synchronization Signal (SSS) v rámci SSB. Poté dekóduje MIB z Physical Broadcast Channel (PBCH) v témže SSB. MIB poskytuje absolutní frekvenční pozici SSB, číslo systémového rámce a, což je nejdůležitější, nezbytnou konfiguraci control resource set (CORESET) a search space pro PDCCH, který plánuje RMSI. Pomocí těchto informací UE monitoruje určený PDCCH, dekóduje Downlink Control Information (DCI) zakódované pomocí SI-RNTI a poté použije přidělené zdroje k přijetí a dekódování RMSI (SIB1) na PDSCH. Teprve po získání RMSI může UE pokračovat v proceduře náhodného přístupu a požádat o připojení k síti.

## K čemu slouží

RMSI bylo zavedeno s 5G NR ve 3GPP Release 15, aby řešilo omezení vysílací architektury systémových informací v LTE a podpořilo novou, flexibilnější fyzickou vrstvu NR. V LTE byly všechny základní systémové informace vysílány polo-statickým způsobem, což mohlo být neefektivní a nepružné. Návrh 5G odděluje absolutně minimální informace (MIB) potřebné pro počáteční synchronizaci a plánování RMSI od zbývajících kritických informací (RMSI), které jsou přenášeny dynamičtěji na sdíleném kanálu.

Toto oddělení slouží několika klíčovým účelům. Za prvé zvyšuje spektrální účinnost. Přenosem pouze malého MIB na neustále aktivním PBCH a plánováním většího payloadu RMSI na vyžádání přes PDSCH jsou síťové zdroje využívány hospodárněji. Za druhé umožňuje větší flexibilitu a podporu beamformingu. RMSI může být beamformováno spolu se svým asociovaným SSB, což je klíčové pro pokrytí v milimetrových vlnách (mmWave). Za třetí umožňuje dynamičtější aktualizace. Zatímco MIB je velmi statické, parametry v RMSI lze měnit snadněji bez dopadu na základní proces synchronizace. Tato architektura je zásadní pro podporu různých případů užití 5G, od enhanced mobile broadband (eMBB) po ultra-reliable low-latency communications (URLLC), protože umožňuje efektivní přizpůsobení a aktualizaci síťových parametrů.

## Klíčové vlastnosti

- Obsahuje kritické přístupové parametry, jako je konfigurace PRACH a informace o uzavření buňky
- Je dynamicky plánováno na PDSCH přes PDCCH pomocí SI-RNTI
- Typicky odpovídá SIB1 ve struktuře systémových informací 5G NR
- Poskytuje plánovací informace pro další SIB (SIB2 a následující)
- Jeho přenos je asociován s konkrétním Synchronization Signal Block (SSB)
- Umožňuje beamforming základních systémových informací pro nasazení v mmWave pásmech

## Související pojmy

- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [SIB – System Information Block](/mobilnisite/slovnik/sib/)
- [CORESET – Control Resource Set](/mobilnisite/slovnik/coreset/)
- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)
- [SI-RNTI – System Information Radio Network Temporary Identifier](/mobilnisite/slovnik/si-rnti/)

## Definující specifikace

- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz

---

📖 **Anglický originál a plná specifikace:** [RMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rmsi/)
