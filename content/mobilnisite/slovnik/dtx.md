---
slug: "dtx"
url: "/mobilnisite/slovnik/dtx/"
type: "slovnik"
title: "DTX – Discontinuous Transmission"
date: 2025-01-01
abbr: "DTX"
fullName: "Discontinuous Transmission"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dtx/"
summary: "DTX je technika úspory energie, při které je vysílač (UE nebo základnová stanice) vypnut během období bez aktivních dat, aby se snížila spotřeba energie a rádiové rušení. Používá se v hlasové i datové"
---

DTX je technika úspory energie, při které je vysílač vypnut během období bez aktivních dat, aby se snížila spotřeba energie a rádiové rušení, čímž se prodlužuje životnost baterie a zvyšuje kapacita sítě.

## Popis

Discontinuous Transmission (DTX, přerušované vysílání) je základní technika správy rádiových prostředků používaná v 3GPP celulárních systémech za účelem úspory energie a snížení rušení. Během hovorů nebo datových relací se přirozeně vyskytují tiché pauzy nebo období nečinnosti; DTX umožňuje vysílači (uživatelskému zařízení nebo základnové stanici) dočasně zastavit vysílání během těchto intervalů. Toho je dosaženo detekcí hlasové aktivity (Voice Activity Detection - [VAD](/mobilnisite/slovnik/vad/)) nebo datové nečinnosti a následným vypínáním rádiového ([RF](/mobilnisite/slovnik/rf/)) vysílání, čímž se vysílač efektivně přepne do stavu s nízkou spotřebou.

Podrobněji, u hlasových služeb DTX spolupracuje s kodeky jako je [AMR](/mobilnisite/slovnik/amr/) (Adaptive Multi-Rate), které během tichých období generují komfortní šum pro udržení kvality hovoru. Systém vysílá rámce popisovače ticha ([SID](/mobilnisite/slovnik/sid/)) se sníženou rychlostí, aby charakterizoval šum v pozadí, což umožňuje přijímači generovat komfortní šum. Na rádiovém rozhraní DTX ovlivňuje uplink (UE k síti) i downlink (síť k UE). V LTE a 5G je integrován s přerušovaným příjmem ([DRX](/mobilnisite/slovnik/drx/)) pro spánkové cykly a operace v připojeném režimu. Specifikace fyzické vrstvy (např. TS 25.214 pro [UTRA](/mobilnisite/slovnik/utra/), TS 36.213 pro LTE, TS 38.213 pro NR) definují vzorce a časování DTX, včetně toho, kdy vysílat řídicí informace, i když data chybí.

Z architektonického hlediska DTX zahrnuje koordinaci napříč vrstvami: kodek na aplikační vrstvě, vrstvy [RLC](/mobilnisite/slovnik/rlc/)/[MAC](/mobilnisite/slovnik/mac/) pro stav vyrovnávací paměti a fyzickou vrstvu pro řízení RF. Mezi klíčové komponenty patří algoritmus VAD, řízení výkonového zesilovače a plánovací mechanismy v základnovém procesoru. Ve scénářích s agregací nosných nebo MIMO lze DTX aplikovat na každou komponentní nosnou nebo datový proud. Jeho role je klíčová v moderních sítích pro dosažení cílů energetické účinnosti a řízení spektrální účinnosti, zejména v hustých nasazeních.

## K čemu slouží

DTX byl zaveden, aby řešil dva hlavní problémy: nadměrné vybíjení baterie v mobilních zařízeních a zbytečné rádiové rušení v celulárních sítích. Kontinuální vysílání, dokonce i během ticha v hovoru nebo v obdobích nečinnosti dat, plýtvá výkonem baterie UE a vytváří rušení, které snižuje kapacitu pro ostatní uživatele. Rané celulární systémy tuto schopnost postrádaly, což vedlo ke kratší době hovoru a zahlcení sítě.

Historický kontext sahá až ke GSM (2G), kde byl DTX standardizován pro prodloužení životnosti baterie a zvýšení kapacity systému. Vyřešil tak omezení analogových a raných digitálních systémů, které vysílaly nepřetržitě. V průběhu jednotlivých vydání se DTX vyvinul, aby podporoval různé služby (data, VoIP) a pokročilé rádiové techniky (HSPA, LTE, NR). Jeho vznik byl motivován potřebou ekologičtějších sítí a lepší uživatelské zkušenosti, zejména s růstem datového provozu. DTX zůstává v 5G nezbytný pro energeticky účinný provoz zařízení massive IoT a rozšířeného mobilního širokopásmového připojení.

## Klíčové vlastnosti

- Snižuje spotřebu energie UE a základnových stanic vypínáním vysílání během nečinnosti
- Snižuje mezibuněčné i vnitrobuněčné rušení, čímž zlepšuje celkovou kapacitu sítě
- Integruje se s detekcí hlasové aktivity (VAD) a generováním komfortního šumu pro kvalitu hlasu
- Podporuje přerušované vzorce jak v uplinku, tak v downlinku napříč více RAT
- Spolupracuje s přerušovaným příjmem (DRX) pro komplexní úsporu energie
- Konfigurovatelné parametry umožňují optimalizaci sítě pro různé typy provozu

## Související pojmy

- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- … a dalších 71 specifikací

---

📖 **Anglický originál a plná specifikace:** [DTX na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtx/)
