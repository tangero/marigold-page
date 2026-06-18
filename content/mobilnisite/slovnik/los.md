---
slug: "los"
url: "/mobilnisite/slovnik/los/"
type: "slovnik"
title: "LOS – Loss Of Signal"
date: 2026-01-01
abbr: "LOS"
fullName: "Loss Of Signal"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/los/"
summary: "Kritický stav poruchy nebo alarmu indikující, že přijímač ztratil schopnost detekovat platný příchozí rádiový signál. Jde o základní parametr monitorování rádiového spoje, který spouští akce jako přev"
---

LOS je kritický stav poruchy nebo alarmu indikující, že přijímač ztratil schopnost detekovat platný příchozí rádiový signál, což spouští procedury jako handover nebo procedury při selhání rádiového spoje.

## Popis

Loss Of Signal (LOS, ztráta signálu) je binární stav detekovaný fyzickou vrstvou přijímače (v UE nebo základnové stanici), když přijímaný výkon nebo kvalita signálu poklesnou pod předdefinovaný práh po souvislou dobu, což indikuje efektivní absenci použitelného signálu. Detekční mechanismus obvykle zahrnuje kontinuální monitorování referenčních signálů, jako je Cell-Specific Reference Signal ([CRS](/mobilnisite/slovnik/crs/)) v LTE nebo Synchronization Signal Block (SSB) v NR. Přijímač měří metriky jako Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/)) nebo Signal-to-Interference-plus-Noise Ratio ([SINR](/mobilnisite/slovnik/sinr/)) a porovnává je s nastavenými prahy. Přetrvávající stav nesynchronizace, kdy po sobě jdoucí měření nesplňují práh, vyvolá deklaraci LOS.

Při detekci LOS vrstva Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) zahájí procedury obnovy. Pro UE v módu RRC_CONNECTED spustí prodloužená LOS ze servisní buňky proceduru radio link failure ([RLF](/mobilnisite/slovnik/rlf/), selhání rádiového spoje), což vede k procedurám opětovného navázání spojení. UE spustí časovač (T310 v LTE/NR) po obdržení po sobě jdoucích indikací nesynchronizace z fyzické vrstvy. Pokud není spojení obnoveno před vypršením časovače, je deklarováno RLF. UE následně provede výběr buňky, pokusí se o RRC opětovné navázání nebo může přejít do idle módu. Pro základnovou stanici by LOS na backhaul nebo fronhaul rozhraní (např. k centrální jednotce) spustilo hlášení alarmu systémům správy sítě.

Práh LOS a detekční čas jsou konfigurovatelné parametry, které umožňují operátorům vyvážit rychlost reakce proti falešným alarmům způsobeným přechodným útlumem. V pokročilých systémech se funkce jako beam failure recovery ([BFR](/mobilnisite/slovnik/bfr/)) v 5G NR zabývají LOS v kontextu konkrétního beamu. Zde, pokud UE ztratí beam používaný pro komunikaci na řídicím kanálu, může zahájit proceduru detekce a obnovy selhání beamu vyhledáváním nových kandidátních beamů bez deklarace úplného selhání rádiového spoje, čímž se zlepšuje robustnost mobility, zejména v nasazeních s vysokými frekvencemi.

## K čemu slouží

Detekce LOS existuje proto, aby poskytla jasný, nízkopoziomový indikátor ztráty konektivity, což umožňuje síti a zařízením autonomně reagovat na zhoršující se nebo selhávající rádiové podmínky. Jejím primárním účelem je udržet dostupnost služeb spuštěním včasných nápravných akcí dříve, než uživatel zaznamená přerušení hovoru nebo datové relace. Řeší problém tichých selhání, kdy by zařízení mohlo chybně zůstat připojeno k buňce, se kterou již nemůže efektivně komunikovat.

Historicky, jak se buněčné systémy vyvíjely od přepojování okruhů pro hlas k přepojování paketů pro data, důsledky nezjištěné ztráty signálu se staly závažnějšími a mohly vést k zablokování datových relací a plýtvání zdroji. Formalizace kritérií LOS a souvisejících procedur obnovy (jako [RLF](/mobilnisite/slovnik/rlf/)) ve standardech 3GPP (počínaje 3G UMTS a zdokonalovaných přes LTE a NR) poskytla robustní, standardizovaný mechanismus pro dohled nad spojením. Ten nahradil nebo rozšířil algoritmy specifické pro dodavatele, čímž zajistil konzistentní uživatelský zážitek a interoperabilitu napříč sítěmi. V moderních sítích s funkcemi jako carrier aggregation a dual connectivity může být detekce LOS prováděna na úrovni buňky nebo skupiny buněk, což přidává složitost, ale také granularitu správy selhání.

## Klíčové vlastnosti

- Detekce na fyzické vrstvě založená na naměřeném výkonu signálu (např. RSRP) nebo kvalitě (např. SINR) klesajícím pod nastavený práh
- Spouští procedury vyšších vrstev, jako je deklarace Radio Link Failure (RLF) a opětovné navázání spojení
- Používá konfigurovatelné časovače a prahy (např. N310, T310), aby se zabránilo předčasné deklaraci kvůli přechodnému útlumu
- Integrální součást monitorování rádiového spoje a optimalizace robustnosti mobility
- V 5G NR rozšířena na úroveň beamu prostřednictvím Beam Failure Detection (BFD) jako součást správy beamů
- Generuje alarmy v systémech správy sítě při detekci na rozhraních síťové infrastruktury

## Související pojmy

- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology
- **TR 38.828** (Rel-16) — CLI and RIM for NR
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [LOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/los/)
