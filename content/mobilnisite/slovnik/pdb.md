---
slug: "pdb"
url: "/mobilnisite/slovnik/pdb/"
type: "slovnik"
title: "PDB – Packet Delay Budget"
date: 2026-01-01
abbr: "PDB"
fullName: "Packet Delay Budget"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pdb/"
summary: "Parametr QoS v 5G definující horní mez pro zpoždění paketů mezi UE a UPF (nebo referenčním bodem N6). Je klíčovou součástí 5QI (5G QoS Identifier) a používá se pro plánování a řízení přístupu za účele"
---

PDB je parametr QoS v 5G definující horní mez pro zpoždění paketů mezi UE a UPF, používaný pro plánování a řízení přístupu za účelem zajištění služeb citlivých na latenci.

## Popis

Packet Delay Budget (PDB) je základní parametr kvality služeb (QoS) v systému 5G (5GS), definovaný v 3GPP TS 23.501. Určuje maximální přípustné koncové zpoždění paketu pro QoS Flow, měřené od UE k User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), která ukončuje rozhraní N6 (směrem k datové síti), nebo naopak. PDB není garantované zpoždění, ale cílová hodnota používaná síťovými funkcemi pro plánování paketů a správu prostředků. Je neodmyslitelně spojen se standardizovaným 5G QoS Identifikátorem ([5QI](/mobilnisite/slovnik/5qi/)), kde má každá hodnota 5QI přiřazen výchozí PDB (a míru chybovosti paketů) podle přílohy A TS 23.501.

Provozně PDB ovlivňuje rozhodování napříč RAN a core sítí. V rádiové přístupové síti (RAN) používá gNB PDB pro plánování uplinku a downlinku. Například pakety patřící do QoS Flow s přísným PDB (např. 10 ms pro [URLLC](/mobilnisite/slovnik/urllc/)) mají přednost před pakety s volným PDB (např. 300 ms pro buffered streaming). PDB pomáhá určovat priority plánování, konfigurace Hybrid [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)) a potenciálně i výběr numerologie a formátu slotu. V core síti může Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) použít PDB během zřizování QoS Flow a při interakcích řízení politik s [PCF](/mobilnisite/slovnik/pcf/).

Parametr funguje ve spojení s dalšími atributy QoS, jako je Guaranteed Flow Bit Rate (GFBR), Maximum Flow Bit Rate ([MFBR](/mobilnisite/slovnik/mfbr/)) a Averaging Window. Síť se snaží zajistit, aby 95. percentil rozdělení zpoždění paketů nepřekročil PDB pro dané QoS Flow. U Non-GBR QoS Flows udává PDB toleranci zpoždění paketů používanou pro plánování. PDB je klíčovým prvkem pro diferenciaci služeb, umožňující síti současně podporovat rozmanité aplikace od massive IoT po ultra-spolehlivé komunikace s nízkou latencí (URLLC) na společné infrastruktuře.

## K čemu slouží

PDB byl zaveden, aby poskytl standardizovaný, kvantifikovatelný cíl pro latenci při správě QoS v 5G, čímž reaguje na potřebu předvídatelného výkonu pro aplikace kritické na latenci. Předchozí generace (4G LTE) měly QoS Class Identifiers (QCIs) s implicitními cíli výkonu, ale rozšířené případy užití 5G – zejména průmyslový IoT, autonomní vozidla a hraní her v reálném čase – vyžadovaly explicitnější a přísnější parametry zpoždění pro spolehlivé chování sítě.

Řeší problém neefektivního nebo nepředvídatelného zacházení s latencí pro smíšené typy provozu. Přiřazením konkrétní hodnoty PDB každému standardizovanému 5QI mohou síťové prvky od různých dodavatelů implementovat konzistentní algoritmy plánování a řízení přístupu. To zajišťuje interoperabilitu a umožňuje vývojářům aplikací a vertikálním odvětvím spoléhat se na konkrétní úrovně síťového výkonu. PDB je základním kamenem schopnosti network slicing v 5G, protože různé slice lze nakonfigurovat s různými rozpočty latence, aby splňovaly odlišné smlouvy o úrovni služeb (SLA).

## Klíčové vlastnosti

- Definován pro každé QoS Flow jako součást charakteristik 5QI
- Používán pro stanovení priorit plánování paketů v RAN (gNB)
- Ovlivňuje plánování přidělování uplinkových zdrojů a stanovení priorit logických kanálů v UE
- Klíčový parametr pro služby Ultra-Reliable Low-Latency Communication (URLLC)
- Nezbytný pro vynucování SLA specifických pro síťový slice
- Referenční bod pro činnosti monitorování výkonu a zajištění kvality

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [GBR – Generic Binaural Renderer](/mobilnisite/slovnik/gbr/)

## Definující specifikace

- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TS 24.385** (Rel-19) — V2X Communication Provisioning Management Object
- **TS 24.386** (Rel-19) — V2X Communication Protocols and Procedures
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TR 38.835** (Rel-18) — Technical Report on XR Enhancements for NR
- **TR 38.838** (Rel-17) — Study on XR Evaluations for NR

---

📖 **Anglický originál a plná specifikace:** [PDB na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdb/)
