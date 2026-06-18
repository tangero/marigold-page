---
slug: "pmi"
url: "/mobilnisite/slovnik/pmi/"
type: "slovnik"
title: "PMI – Precoding Matrix Indicator"
date: 2025-01-01
abbr: "PMI"
fullName: "Precoding Matrix Indicator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pmi/"
summary: "Zpětnovazební index hlášený UE na gNB, který udává preferovanou předkódovací matici pro downlinkové MIMO přenosy. Je klíčovou součástí uzavřené smyčky prostorového multiplexování, která umožňuje síti"
---

PMI je zpětnovazební index hlášený uživatelským zařízením základnové stanici, který udává preferovanou předkódovací matici pro optimalizaci downlinkových MIMO přenosů.

## Popis

Precoding Matrix Indicator (PMI, indikátor předkódovací matice) je klíčový zpětnovazební mechanismus ve vrstvě fyzického přenosu Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)) v systémech 3GPP LTE a NR. Je součástí informace o stavu kanálu (Channel State Information, [CSI](/mobilnisite/slovnik/csi/)), kterou uživatelské zařízení (User Equipment, UE) hlásí základnové stanici gNodeB (gNB). UE po změření downlinkových referenčních signálů (např. [CSI-RS](/mobilnisite/slovnik/csi-rs/)) vypočítá optimální nebo preferovanou předkódovací matici z předdefinovaného kodebooku. Tato matice je souborem komplexních vah aplikovaných na anténní porty pro tvarování vysílaného signálu, čímž efektivně provádí beamforming. UE poté odešle index (PMI) odpovídající této matici v kodebooku zpět na gNB prostřednictvím uplinkových řídicích kanálů ([PUCCH](/mobilnisite/slovnik/pucch/)) nebo sdílených kanálů ([PUSCH](/mobilnisite/slovnik/pusch/)).

gNB použije nahlášený PMI spolu s dalšími informacemi CSI, jako je Rank Indicator ([RI](/mobilnisite/slovnik/ri/)) a Channel Quality Indicator ([CQI](/mobilnisite/slovnik/cqi/)), k výběru předkódovací matice pro následné downlinkové přenosy k danému UE. Tento proces přizpůsobuje přenos aktuálnímu stavu kanálu, zaměřuje energii směrem k UE a minimalizuje interferenci, což je zásadní pro zisky z prostorového multiplexování. Design kodebooku je standardizován (odlišný pro LTE a NR) a definuje sadu možných předkódovacích matic pro různé konfigurace antén (např. 2, 4, 8 anténních portů) a přenosové ranky.

Hlášení PMI může být širokopásmové (jediný PMI pro celou šířku pásma systému) nebo subpásmové (různé PMI pro různé části pásma), což nabízí kompromis mezi režií zpětné vazby a granularitou přizpůsobení kanálu. V pokročilých MIMO módech, jako je multi-user MIMO ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)), může gNB použít hlášení PMI od více UE k plánování simultánních přenosů s minimální meziuserskou interferencí. Přesnost a včasnost zpětné vazby PMI přímo ovlivňuje spektrální účinnost a spolehlivost downlinku.

## K čemu slouží

PMI byl zaveden, aby umožnil efektivní uzavřenou smyčku prostorového multiplexování v MIMO systémech, počínaje LTE Release 8. Před takovými zpětnovazebními mechanismy MIMO primárně používalo otevřené smyčky techniky, jako je prostorová diverzita, které byly robustní, ale nemaximalizovaly propustnost přizpůsobením se podmínkám kanálu. Základním problémem je, že gNB nemá dokonalou znalost downlinkového kanálu ke každému UE, což je nezbytné pro optimální předkódování.

PMI tento problém řeší využitím schopnosti UE měřit kanál a doporučit strategii předkódování. To umožňuje síti provádět předkódování závislé na kanálu (beamforming), což významně zvyšuje sílu signálu u cílového UE a snižuje interferenci ostatním. Motivací byla potřeba zvýšit kapacitu buňky a uživatelské datové rychlosti, aby byly uspokojeny rostoucí požadavky mobilního širokopásmového přístupu.

V průběhu následných releasů se zpětná vazba PMI vyvíjela, aby podporovala stále složitější anténní pole (massive MIMO), vyšší kmitočtová pásma a nové případy užití. Vylepšení jako enhanced CSI feedback (eCSI) a Type II PMI (s vyšším rozlišením) v NR byla motivována požadavky na přesnější beamforming v mmWave pásmech a pro pokročilá schémata multi-user MIMO, což posouvá hranice spektrální účinnosti v 5G a dalších generacích.

## Klíčové vlastnosti

- Indexová zpětná vazba udávající preferovanou předkódovací matici ze standardizovaného kodebooku
- Integrální součást hlášení informace o stavu kanálu (CSI) v LTE a NR
- Podporuje širokopásmové a subpásmové hlášení pro flexibilní přizpůsobení kanálu
- Umožňuje uzavřenou smyčku prostorového multiplexování a beamforming pro downlinkové MIMO
- Designy kodebooků se liší podle konfigurace anténních portů (např. 2, 4, 8, 16, 32 portů) a přenosového ranku
- Kritický pro plánování multi-user MIMO (MU-MIMO) a správu interference

## Související pojmy

- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements
- **TS 36.863** (Rel-12) — CRS Interference Mitigation for Homogeneous Networks
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.307** (Rel-19) — NR UE Release Independent Requirements
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [PMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmi/)
