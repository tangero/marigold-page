---
slug: "facch"
url: "/mobilnisite/slovnik/facch/"
type: "slovnik"
title: "FACCH – Fast Associated Control CHannel"
date: 2025-01-01
abbr: "FACCH"
fullName: "Fast Associated Control CHannel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/facch/"
summary: "Řídicí kanál v GSM, který přebírá časové sloty z kanálu pro přenos uživatelských dat (TCH), aby přenesl naléhavé signalizační zprávy během aktivního hovoru. Umožňuje kritické funkce jako předávání hov"
---

FACCH je řídicí kanál v GSM, který přebírá časové sloty z aktivního kanálu pro přenos uživatelských dat (traffic channel), aby přenesl naléhavé signalizační zprávy s nízkou latencí pro funkce jako je předávání hovoru (handover) během spojení.

## Popis

Rychlý přidružený řídicí kanál (Fast Associated Control CHannel, FACCH) je signalizační kanál v GSM (a odvozených technologiích jako [GPRS](/mobilnisite/slovnik/gprs/) a [EDGE](/mobilnisite/slovnik/edge/)) rozhraní, který pracuje v režimu 'přebírání' (stealing mode). Není fyzicky samostatným kanálem, ale je multiplexován ve stejných fyzických zdrojích jako kanál pro přenos uživatelských dat (Traffic Channel, [TCH](/mobilnisite/slovnik/tch/)) přenášející hlas nebo data uživatele. FACCH funguje tak, že při potřebě odeslat naléhavou řídicí zprávu dočasně nahradí blok uživatelských dat (burst) signalizační informací. Na to upozorňují 'přebírací příznaky' (stealing flags) v rámci normální struktury burstu – dva bity, které přijímači sdělují, zda aktuální burst obsahuje uživatelská data (TCH) nebo signalizační data (FACCH).

Z architektonického hlediska je FACCH přidružen k vyhrazenému spojení (dedicated mode connection) mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)). Nachází se na vrstvě 2 (linkové vrstvě), konkrétně v rámci protokolu LAPDm. Když vznikne potřeba naléhavé signalizace (např. síť rozhodne, že je nutné předání hovoru), systém 'přebírá' 20ms rámec (nebo více rámců) z TCH. Převzatý rámec je zakódován daty FACCH, která zahrnují 184bitové informační pole, k němuž se před konvolučním kódováním pro opravu chyb přidá 40 bitů Fire kódu pro detekci chyb a 4 koncové bity, což vede ke vzniku 456bitového bloku rozprostřeného (interleaved) přes 8 po sobě jdoucích burstů.

Jeho role v síti je klíčová pro funkce řízení v reálném čase, které nesnesou zpoždění při použití pomalejšího, samostatného vyhrazeného řídicího kanálu ([SDCCH](/mobilnisite/slovnik/sdcch/)). Mezi klíčové procedury zprostředkované FACCH patří příkaz a provedení předání hovoru (handover), okamžité přidělení zdrojů, řízení nespojitého vysílání ([DTX](/mobilnisite/slovnik/dtx/)), hlášení měření a správa šifrovacího režimu. Díky využití stávajícího TCH poskytuje FACCH signalizační cestu s nízkou latencí přímo v přenosovém pásmu, což je nezbytné pro udržení kvality hovoru, efektivní správu rádiových zdrojů a zajištění plynulého přenosu spojení při pohybu uživatele.

## K čemu slouží

FACCH byl vytvořen, aby řešil omezení latence hlavního vyhrazeného signalizačního kanálu v GSM, samostatného vyhrazeného řídicího kanálu ([SDCCH](/mobilnisite/slovnik/sdcch/)). SDCCH, ač vhodný pro navázání hovoru a nenaléhavou signalizaci, je příliš pomalý pro časově kritické řídicí funkce vyžadované během aktivní hlasové nebo datové relace. Bez rychlého signalizačního mechanismu by byly procedury jako předávání hovoru (handover) – které jsou nezbytné pro udržení spojení při pohybu uživatele mezi buňkami – příliš pomalé, což by vedlo k přerušeným hovorům a špatnému uživatelskému zážitku.

Historická motivace vychází z konstrukčních cílů GSM jako digitálního celulárního systému, který upřednostňoval kvalitu hlasu a mobilitu. FACCH tento problém vyřešil převzetím samotného kanálu přenášejícího uživatelský hovor pro naléhavé síťové příkazy, což je koncept známý jako 'signalizace v pásmu' (in-band signaling). Šlo o chytré využití zdrojů, protože se tak vyhnulo nutnosti alokovat další vyhrazené rádiové spektrum pro rychlé řízení, což by snížilo kapacitu sítě.

Řešil konkrétní omezení předchozích analogových systémů a raných digitálních návrhů, kterým chyběl takto efektivní přidružený řídicí mechanismus. Tím, že umožnil rychlou signalizaci přímo spojenou s aktivním kanálem pro přenos dat, se FACCH stal klíčovým prvkem pro spolehlivé řízení mobility, adaptivní řízení výkonu a efektivní správu rádiových zdrojů v GSM a jeho evolučních cestách (GPRS, EDGE), čímž zajišťoval rychlou odezvu a stabilitu sítě.

## Klíčové vlastnosti

- Pracuje v režimu 'přebírání' (stealing mode) nahrazením burstů TCH signalizačními daty
- Pro identifikaci využívá přebírací příznaky (stealing flags) ve struktuře burstu
- Poskytuje signalizaci s nízkou latencí přímo v přenosovém pásmu pro aktivní spojení
- Přenáší kritické zprávy vrstvy 3 (např. příkazy k předání hovoru, informace o měření)
- Využívá stejné rozprostření (interleaving) a kódování kanálu jako TCH (plný výkon, full-rate)
- Nezbytný pro řízení rádiových zdrojů v reálném čase během hovoru

## Související pojmy

- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [SDCCH – Stand-Alone Dedicated Control Channel](/mobilnisite/slovnik/sdcch/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TS 46.041** (Rel-19) — GSM Half Rate Speech DTX Operation
- **TS 46.081** (Rel-19) — GSM Enhanced Full Rate DTX Operation
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [FACCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/facch/)
