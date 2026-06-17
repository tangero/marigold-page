---
slug: "e-rgch"
url: "/mobilnisite/slovnik/e-rgch/"
type: "slovnik"
title: "E-RGCH – E-DCH Relative Grant Channel"
date: 2025-01-01
abbr: "E-RGCH"
fullName: "E-DCH Relative Grant Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-rgch/"
summary: "Downlinkový fyzický řídicí kanál v UMTS/HSPA (režim FDD), který Node B používá k vysílání příkazů relativního povolení (grantu) pro UE. Tyto příkazy slouží pro řízení uplinkové rychlosti na Enhanced D"
---

E-RGCH je downlinkový fyzický kanál UMTS/HSPA, který Node B používá k vysílání relativních povolení (grantů). Tyto příkazy instruují UE (uživatelské zařízení), aby zvýšilo, udrželo nebo snížilo svou uplinkovou rychlost na Enhanced Dedicated Channel.

## Popis

Kanál relativního povolení pro [E-DCH](/mobilnisite/slovnik/e-dch/) (E-RGCH) je dedikovaný downlinkový fyzický kanál v technologii UMTS High Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)), který funguje pouze v režimu Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)). Je klíčovou součástí mechanismu rychlého řízení přidělování zdrojů (scheduling) kontrolovaného Node B pro Enhanced Dedicated Channel (E-DCH). E-RGCH přenáší 1-bitový příkaz (nebo 2-bitový příkaz pro multi-streamovou operaci v novějších verzích standardu) ze serving Node B (a potenciálně i z non-serving Node B v aktivním setu pro koordinaci mezi buněčným interference) přímo k specifické UE. Tento příkaz poskytuje relativní úpravy 'serving grant' UE, která určuje maximální povolený poměr výkonu, který UE může použít pro přenos na E-DCH. Tři základní příkazy jsou 'UP', '[HOLD](/mobilnisite/slovnik/hold/)' a 'DOWN'. Příkaz 'UP' zvýší serving grant o jeden krok (definovaný kvantovanou velikostí kroku), příkaz 'HOLD' udržuje současnou hodnotu a příkaz 'DOWN' ji sníží o jeden krok. To umožňuje velmi rychlé (na základě 2 ms nebo 10 ms TTI) a detailní řízení uplinkové datové rychlosti UE, což Node B dovoluje rychle reagovat na změny uplinkového interference, stavu bufferu a QoS požadavků. E-RGCH je vysílán pomocí kanalizačního kódu z Orthogonal Variable Spreading Factor ([OVSF](/mobilnisite/slovnik/ovsf/)) stromu a je typicky multiplexován kódem s jinými fyzickými kanály. Pro danou UE vysílá serving buňka primární E-RGCH pro řízení přidělování zdrojů (scheduling), zatímco non-serving buňky v aktivním setu mohou vysílat E-RGCH pro řízení přetížení (overload control), typicky vysílají pouze příkazy 'DOWN' nebo 'HOLD' pro ochranu vlastních buněk od nadměrného interference. UE kombinuje tyto příkazy podle definovaných pravidel, aby určilo finální aktualizaci serving grant.

## K čemu slouží

E-RGCH byl zaveden ve 3GPP Release 6 jako část [HSUPA](/mobilnisite/slovnik/hsupa/), aby řešil kritické limity uplinku z Release 99/Release 5, který závisel na pomalejším řízení přidělování zdrojů (scheduling) kontrolovaném RNC. Primární problémy byly vysoká latence při přidělování uplinkových zdrojů a neschopnost Node B rychle řídit interference v uplinku, který je inherentně limitován interference. E-RGCH umožňuje rychlé řízení přidělování zdrojů (scheduling) Node B, což umístí bod rozhodování o přidělování zdrojů do Node B nejblíže rádiovému interface. To dovoluje reakce na změny rádiových podmínek na úrovni milisekund. Jeho účelem je dynamicky optimalizovat uplinkovou kapacitu a stabilitu řízením výkonu jednotlivých UE, a tím řídit celkový uplinkový interference (RoT - Rise over Thermal) v buňce. Použitím relativních povolení (grantů) systém poskytuje stabilní a robustní řídicí smyčku; malé inkrementální úpravy zabraňují velkým, destabilizujícím skokům ve výkonu vysílaném UE. Toto rychlé řízení interference bylo nezbytné pro dosažení významně vyšších uplinkových datových rychlostí (až 5.76 Mbps původně) a nižší latence, které definovali výkonnostní vylepšení HSUPA vůči předchozím verzím UMTS.

## Klíčové vlastnosti

- Přenáší 1-bitové (nebo 2-bitové) příkazy relativního povolení (grantu) (UP/HOLD/DOWN)
- Funguje pouze v režimu FDD jako část HSUPA
- Umožňuje rychlé řízení přidělování zdrojů (scheduling) Node B s reakčním časem 2 ms nebo 10 ms TTI
- Používá se pro řízení přidělování zdrojů (scheduling) serving buňky i řízení přetížení (overload control) non-serving buňky
- Vysílán pomocí dedikovaných kanalizačních kódů
- Poskytuje detailní řízení serving grant UE pro E-DCH

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [E-AGCH – EDCH – Absolute Grant Channel](/mobilnisite/slovnik/e-agch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [E-RGCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-rgch/)
