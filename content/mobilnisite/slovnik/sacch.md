---
slug: "sacch"
url: "/mobilnisite/slovnik/sacch/"
type: "slovnik"
title: "SACCH – Standalone Associated Control CHannel"
date: 2025-01-01
abbr: "SACCH"
fullName: "Standalone Associated Control CHannel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sacch/"
summary: "Řídicí kanál GSM používaný pro přenos signalizačních a měřicích dat mezi mobilní stanicí a základnovou stanicí během aktivního hovoru nebo vyhrazeného spojení. Funguje časově multiplexovaně vedle kaná"
---

SACCH je řídicí kanál GSM, který přenáší signalizační a měřicí data během aktivního hovoru; funguje vedle kanálů pro přenos uživatelských dat a umožňuje nepřetržitou síťovou kontrolu a monitorování spojení bez přerušení uživatelských dat.

## Popis

Standalone Associated Control CHannel (SACCH) je základní signalizační kanál v rádiovém rozhraní GSM (Global System for Mobile Communications), definovaný ve specifikacích 3GPP. Je klasifikován jako pomalý přidružený řídicí kanál, protože je po dobu trvání spojení trvale přidružen k Traffic Channel ([TCH](/mobilnisite/slovnik/tch/)) nebo Standalone Dedicated Control Channel ([SDCCH](/mobilnisite/slovnik/sdcch/)). SACCH je časově multiplexován s uživatelskými datovými nebo vyhrazenými signalizačními blesky. Konkrétně ve 26rámcové multirámcové struktuře používané pro TCH je jeden časový slot (rámec č. 12) přidělen pro SACCH a další (rámec č. 25) je nevyužitý. Toto periodické přidělení zajišťuje, že řídicí informace jsou přenášeny v pravidelných intervalech, přibližně každých 480 ms.

Z architektonického hlediska je SACCH obousměrný kanál typu point-to-point existující mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)). Je namapován na fyzický kanálový zdroj (konkrétní časový slot a frekvenci), který je vyhrazen pro spojení jednoho uživatele. Kanál přenáší klíčové signalizační zprávy vrstvy 2 a vrstvy 3. Mezi klíčové přenášené informace patří měřicí reporty od MS k síti, které obsahují údaje o úrovni a kvalitě přijímaného signálu z obsluhované a sousedních buněk. Naopak síť používá SACCH k odesílání zpráv systémových informací a příkazů pro řízení výkonu ([TPC](/mobilnisite/slovnik/tpc/)) k MS, kterými jí nařizuje upravit výstupní výkon.

Fungování SACCH je nedílnou součástí udržování kvality hovoru a umožnění mobility. Během hlasového hovoru na TCH poskytuje SACCH nepřetržitý signalizační spoj nezbytný pro funkce jako příprava předání spojení (handover). MS periodicky odesílá prostřednictvím SACCH měřicí reporty, což umožňuje řadiči základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) vyhodnocovat rádiové podmínky a rozhodovat, zda je vyžadováno předání spojení do buňky se silnějším signálem. Dále SACCH přenáší informace o časovém předstihu (timing advance) od BTS k MS. Tento příkaz upravuje časování vysílání MS, aby kompenzoval zpoždění šíření signálu, a zajišťuje tak synchronní příchod blesků od různých MS na BTS a předchází intersymbolovému rušení. Nízká, ale stabilní přenosová rychlost tohoto kanálu je dostačující pro tento ne-reálný, avšak zásadní řídicí provoz, který je základem správy spojení a řízení rádiových zdrojů v sítích GSM.

## K čemu slouží

SACCH byl vytvořen k řešení základního problému udržování nepřetržité síťové kontroly a dohledu během aktivní komunikační relace v GSM. Předchozí celulární systémy často postrádaly vyhrazenou, vždy dostupnou signalizační cestu poté, co byl zřízen kanál pro přenos uživatelských dat, což ztěžovalo provádění reálných úprav a monitorování. SACCH poskytuje toto trvalé řídicí spojení, které je nezbytné pro stabilní mobilní připojení v celulárním prostředí charakteristickém měnící se sílou signálu a pohybem uživatele.

Jeho primární motivací bylo umožnit základní funkce mobility a správy rádiových zdrojů, jako je předání spojení (handover) a řízení výkonu. Bez kanálu jako je SACCH by síť byla 'slepá' vůči měnícím se rádiovým podmínkám během hovoru, což by vedlo k přerušeným spojením, když by se uživatel pohyboval mimo pokrytí buňky. Díky povinným periodickým měřicím reportům od mobilu může síť proaktivně připravovat předání spojení. Podobně je mechanismus časového předstihu (timing advance) přenášený na SACCH klíčový pro [TDMA](/mobilnisite/slovnik/tdma/) strukturu GSM; umožňuje více uživatelům sdílet stejnou frekvenci přidělením přesných časových slotů a SACCH zajišťuje, aby jejich vysílání zůstala synchronizovaná i při jejich pohybu, čímž chrání kapacitu sítě a kvalitu hovoru.

## Klíčové vlastnosti

- Trvale přidružen k TCH nebo SDCCH po dobu trvání spojení
- Funguje v pomalém, periodickém časovém multiplexu (jeden rámec v 26rámcovém multirámci)
- Přenáší klíčové měřicí reporty (RXLEV, RXQUAL) od MS k síti
- Přenáší síťové příkazy: systémové informace, řízení výkonu a časový předstih
- Obousměrný signalizační kanál typu point-to-point
- Nezbytný pro rozhodování o předání spojení a dohled nad rádiovým spojením

## Související pojmy

- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [SDCCH – Stand-Alone Dedicated Control Channel](/mobilnisite/slovnik/sdcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TS 46.002** (Rel-19) — Introduction to GSM Half-Rate Speech Processing
- **TS 46.041** (Rel-19) — GSM Half Rate Speech DTX Operation
- **TS 46.051** (Rel-19) — GSM Enhanced Full Rate Speech Processing Intro
- **TS 46.081** (Rel-19) — GSM Enhanced Full Rate DTX Operation
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [SACCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sacch/)
