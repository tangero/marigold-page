---
slug: "tac"
url: "/mobilnisite/slovnik/tac/"
type: "slovnik"
title: "TAC – Time Alignment Command"
date: 2025-01-01
abbr: "TAC"
fullName: "Time Alignment Command"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tac/"
summary: "Time Alignment Command (TAC) je řídicí signál vysílaný základnovou stanicí (eNB/gNB) k uživatelskému zařízení (UE) pro úpravu časování jeho vysílání v uplinku. Zajišťuje, aby uplinkové signály od více"
---

TAC je řídicí signál vysílaný základnovou stanicí k uživatelskému zařízení (UE) pro úpravu časování jeho vysílání v uplinku, který zajišťuje synchronní příjem signálů a předchází tak interferencím v systémech SC-FDMA/OFDMA.

## Popis

Time Alignment Command (TAC) je základní mechanismus ve fyzické vrstvě LTE a 5G NR pro udržování synchronizace v uplinku. V systémech [OFDMA](/mobilnisite/slovnik/ofdma/) (Orthogonal Frequency Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)) a [SC-FDMA](/mobilnisite/slovnik/sc-fdma/) (Single Carrier [FDMA](/mobilnisite/slovnik/fdma/)) používaných pro uplink je přesné časové zarovnání signálů od všech uživatelských zařízení (UE) zásadní pro zachování ortogonality mezi subnosnými a prevenci mezisymbolové interference ([ISI](/mobilnisite/slovnik/isi/)) a mezinosné interference ([ICI](/mobilnisite/slovnik/ici/)). TAC je parametr přenášený přes vrstvu Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) v MAC Control Element (MAC [CE](/mobilnisite/slovnik/ce/)), který instruuje konkrétní zařízení UE, aby posunulo nebo zpozdilo časování svého uplinkového vysílání.

Proces funguje následovně: Základnová stanice (eNB v LTE, gNB v NR) průběžně měří časování přijímaných uplinkových signálů od každého zařízení UE, například během přenosu Sounding Reference Signals (SRS) nebo Physical Uplink Shared Channel (PUSCH). Vypočítá časovou chybu, což je rozdíl mezi ideálním časem příjmu a skutečným časem příchodu signálu od zařízení UE. Tato chyba je kvantována a namapována na hodnotu TAC. TAC je následně přenesen k zařízení UE v downlinkové řídicí zprávě. Po přijetí TAC zařízení UE upraví časování svého uplinkového vysílání o odpovídající hodnotu, typicky v krocích odpovídajících zlomku základní časové jednotky (např. Ts v LTE, Tc v NR). Rozsah úpravy je definován standardem a zařízení UE udržuje Time Alignment Timer (TAT); dokud tento časovač běží, považuje se zařízení UE za synchronizované v uplinku.

Klíčovými součástmi jsou plánovač uplinku a jednotka měření časování na základnové stanici, vrstva MAC pro generování MAC CE a mechanismus řízení časování ve fyzické vrstvě zařízení UE. TAC je součástí systému s uzavřenou smyčkou řízení. Jeho role je naprosto klíčová pro mobilitu, zejména když se zařízení UE pohybují a mění se jejich zpoždění šíření. Bez průběžného časového zarovnání by byla narušena pečlivě vytvořená ortogonalita uplinku, což by vedlo ke zvýšené interferenci, snížení přenosových rychlostí a degradaci celkové kapacity systému. V 5G NR zůstává koncept v zásadě stejný, ale funguje v rámci nové rámcové struktury NR a podporuje širší šířky pásma nosné a různorodější numerologie.

## K čemu slouží

Mechanismus Time Alignment Command byl zaveden k řešení zásadního problému synchronizace uplinku v celulárních systémech OFDMA/SC-FDMA. V dřívějších systémech založených na CDMA, jako je UMTS, byla hlavní metodou pro zvládání interference vícenásobného přístupu přesná regulace výkonu, zatímco časové zarovnání bylo méně kritické. S přechodem na OFDMA v LTE se ortogonalita ve frekvenční oblasti stala prvořadou. Pokud uplinkové signály od různých zařízení UE nedorazí na základnovou stanici v rámci trvání cyklické předpony (CP), jejich ortogonalita se ztratí, což způsobí závažnou interferenci, kterou nelze odfiltrovat.

Bez standardizovaného dynamického mechanismu TAC by udržování synchronizace uplinku pro pohybující se zařízení UE bylo téměř nemožné, což by vážně omezilo velikost buněk a podporu mobility. TAC poskytuje rychlou, sítí řízenou metodu pro kompenzaci proměnlivého zpoždění šíření, ke kterému dochází, když se zařízení UE mění vzdálenost od základnové stanice nebo v důsledku vícecestného šíření. Řeší omezení jednoduchého počátečního procesu náhodného přístupu, který poskytuje pouze hrubé časové zarovnání. Průběžné jemné doladění umožněné příkazy TAC je to, co umožňuje LTE a NR podporovat vysokorychlostní mobilitu, velké poloměry buněk a efektivní sdílení uplinkových zdrojů mezi mnoha uživateli. Jeho vytvoření bylo motivováno potřebou dosáhnout vysokých cílů spektrální účinnosti 4G a 5G, aby byl uplink stejně robustní a efektivní jako downlink.

## Klíčové vlastnosti

- Řídicí signál s uzavřenou smyčkou pro úpravu časování uplinkového vysílání
- Přenášen přes MAC Control Element (MAC CE) v downlinku
- Kompenzuje proměnlivé zpoždění šíření způsobené mobilitou zařízení UE
- Zásadní pro udržení ortogonality v uplinku SC-FDMA/OFDMA
- Spojen s Time Alignment Timer (TAT) na straně zařízení UE
- Podporuje kvantované časové úpravy v definovaných krocích (např. 16 jednotek Ts v LTE)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 28.875** (Rel-19) — Study on IAB Node Management
- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 36.463** (Rel-19) — XwAP Protocol Specification
- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [TAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tac/)
