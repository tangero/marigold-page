---
slug: "rlm"
url: "/mobilnisite/slovnik/rlm/"
type: "slovnik"
title: "RLM – Radio Link Monitoring"
date: 2025-01-01
abbr: "RLM"
fullName: "Radio Link Monitoring"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rlm/"
summary: "Radio Link Monitoring (RLM) je procedura UE pro vyhodnocení kvality downlink rádiového spoje k její obsluhující buňce. Je klíčová pro udržení stability spojení, protože spouští procedury detekce selhá"
---

RLM je procedura UE pro vyhodnocení kvality downlink rádiového spoje od obsluhující buňky, která spouští detekci selhání a obnovu pro udržení stability spojení.

## Popis

Radio Link Monitoring (RLM) je základní procedura fyzické vrstvy prováděná uživatelským zařízením (UE) v systémech LTE i NR. Jejím hlavním účelem je průběžné vyhodnocování kvality downlink rádiového spoje od obsluhující buňky. UE to provádí měřením specifických referenčních signálů vysílaných gNB (v NR) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE). Tato měření jsou porovnávána se dvěma konfigurovatelnými prahy: prahem out-of-sync (OOS, Q_out) a prahem in-sync ([IS](/mobilnisite/slovnik/is/), Q_in).

Když odhadovaná kvalita rádiového spoje klesne pod práh Q_out, fyzická vrstva v UE deklaruje indikaci 'out-of-sync' vyšším vrstvám. Naopak, když se kvalita obnoví nad práh Q_in, je deklarována indikace 'in-sync'. Protokolový zásobník vyšší vrstvy (typicky vrstva [RRC](/mobilnisite/slovnik/rrc/)) implementuje stavový automat, který tyto po sobě jdoucí indikace počítá. Pokud je přijat určitý počet po sobě jdoucích indikací 'out-of-sync' (N310), je spuštěn časovač (T310). Pokud není před vypršením časovače T310 přijat požadovaný počet po sobě jdoucích indikací 'in-sync' (N311), UE deklaruje selhání rádiového spoje ([RLF](/mobilnisite/slovnik/rlf/)).

Po deklaraci RLF zahájí UE proceduru obnovení spojení. Přestane vysílat v uplinku, vybere novou buňku (což může být stejná nebo jiná buňka) a pokusí se znovu synchronizovat a obnovit RRC spojení. Celý tento proces, řízený RLM, je zásadní pro zvládání scénářů, jako je náhlé zastínění, hluboké útlumy nebo interference, a zajišťuje, že se UE může autonomně obnovit připojení bez zbytečné signalizační režie ze strany sítě.

Konfigurační parametry pro RLM, jako jsou Q_out, Q_in, N310, T310 a N311, jsou poskytovány UE prostřednictvím RRC signalizace (např. ve zprávě RRCReconfiguration). Tyto parametry lze přizpůsobit na základě typu služby, stavu mobility nebo scénáře nasazení sítě. Například UE konfigurované pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) může mít přísnější prahy nebo kratší časovače, aby umožnilo rychlejší detekci selhání a obnovu. RLM funguje nezávisle jak ve zdrojové buňce během přípravy předávání spojení, tak v cílové buňce po provedení předání, čímž zajišťuje bezproblémové řízení mobility.

## K čemu slouží

Radio Link Monitoring existuje, aby poskytl robustní, UE-autonomní mechanismus pro detekci zhoršujícího se nebo ztraceného rádiového spojení. Před standardizovanými procedurami, jako je RLM, sítě více spoléhaly na detekci selhání spoje na straně sítě, což mohlo být pomalejší a méně efektivní. Hlavním problémem, který RLM řeší, je přerušení služeb způsobené špatnými rádiovými podmínkami. Umožňuje UE rychle a nezávisle určit, kdy již spoj není použitelné pro spolehlivou komunikaci, a spustit řízený proces obnovy.

Historická motivace vychází z potřeby spolehlivé mobility v paketově orientovaných celulárních systémech, jako jsou LTE a 5G NR, kde je udržení 'vždy zapojeného' IP spojení klíčové. V dřívějších generacích celulárních sítí často vedla selhání spojení k přerušeným hovorům nebo relacím s výrazným zpožděním před opětovným připojením. RLM poskytuje proaktivní a standardizovanou metodu pro detekci selhání, zastavení zbytečných přenosů (šetření baterie UE a snížení interference) a rychlý pokus o opětovné připojení k nejlepší dostupné buňce. Řeší omezení čistě síťově řízeného dohledu, který nemusí dostatečně rychle reagovat na rychlé změny v rádiovém prostředí UE, zejména na okrajích buněk nebo ve scénářích s vysokou mobilitou.

## Klíčové vlastnosti

- UE-autonomní vyhodnocení kvality downlink rádiového spoje na základě měření referenčních signálů.
- Využití dvou klíčových prahů: out-of-sync (Q_out) a in-sync (Q_in).
- Implementace stavového automatu ve vyšších vrstvách (RRC) počítajícího po sobě jdoucí synchronizační indikace.
- Konfigurovatelné časovače (T310) a čítače (N310, N311) pro řízení deklarace RLF.
- Spouští standardizovanou proceduru Radio Link Failure (RLF) a následnou proceduru obnovení RRC spojení.
- Parametry jsou konfigurovány přes RRC, což umožňuje optimalizaci sítě pro různé služby a stavy mobility.

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.842** (Rel-12) — Small Cell Enhancements for LTE Higher Layers
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.816** (Rel-16) — RAN-centric Data Collection & Utilization Study
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [RLM na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlm/)
