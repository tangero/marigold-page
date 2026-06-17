---
slug: "mtch"
url: "/mobilnisite/slovnik/mtch/"
type: "slovnik"
title: "MTCH – MBMS point-to-multipoint Traffic Channel"
date: 2025-01-01
abbr: "MTCH"
fullName: "MBMS point-to-multipoint Traffic Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mtch/"
summary: "MTCH je downlinkový logický kanál v systémech 3GPP používaný výhradně pro službu Multimedia Broadcast Multicast Service (MBMS) k doručování uživatelských datových přenosů ze sítě k více uživatelským z"
---

MTCH je downlinkový logický kanál v systémech 3GPP používaný výhradně pro MBMS k doručování uživatelských datových přenosů ze sítě k více uživatelským zařízením (UE) současně v rámci určité servisní oblasti.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) point-to-multipoint Traffic Channel (MTCH) je jednosměrný downlinkový logický kanál definovaný v architektuře protokolů rádiového rozhraní 3GPP pro službu Multimedia Broadcast Multicast Service (MBMS). Funguje na vrstvě Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a je určen pro přenos vlastních uživatelských dat (uživatelské roviny) MBMS služby, jako jsou video streamy, stahování souborů nebo audio vysílání, ze sítě ke skupině uživatelských zařízení (UE). MTCH je mapován na transportní kanály, konkrétně na Multicast Channel ([MCH](/mobilnisite/slovnik/mch/)) v LTE a na Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)) v UMTS, které jsou následně mapovány na fyzické zdroje. Jeho fungování je úzce spjato s MBMS relací. Když MBMS relace začne, síť nakonfiguruje potřebné rádiové přenosové dráhy. MTCH je asociován s konkrétním Temporary Mobile Group Identity (TMGI) a oblastí MBMS služby. Datové pakety pro službu jsou zpracovávány vrstvami Packet Data Convergence Protocol (PDCP) a Radio Link Control (RLC), které mohou aplikovat kompresi hlaviček a segmentaci. Na vrstvě MAC jsou tyto pakety naplánovány na logický kanál MTCH. V dané buňce jsou všechny MTCH pro různé služby multiplexovány na stejný transportní kanál MCH. Uživatelská zařízení (UE) se zájmem o příjem služby monitorují řídicí kanál [MCCH](/mobilnisite/slovnik/mcch/) (MBMS Control Channel) pro informace o plánování, které jim sdělují, kdy a na kterých subrámech bude MTCH pro požadovanou službu vysílán. Poté se naladí na příjem vysílaných dat, což umožňuje efektivní využití spektra, protože jediný přenos obslouží všechna zainteresovaná UE v pokryté oblasti. Jeho role je zásadní pro point-to-multipoint povahu MBMS, neboť poskytuje kanál pro doručování obsahu, což jej odlišuje od unicastových přenosových kanálů, jako je [DTCH](/mobilnisite/slovnik/dtch/).

## K čemu slouží

MTCH byl vytvořen, aby naplnil potřebu efektivního, standardizovaného mechanismu pro doručování identického obsahu mnoha uživatelům současně přes buněčné rádiové rozhraní, což je schopnost, kterou tradiční point-to-point (unicastové) kanály nepodporují. Před [MBMS](/mobilnisite/slovnik/mbms/) a MTCH vyžadovalo doručování populárního obsahu, jako je živé TV vysílání nebo softwarové aktualizace, masovému publiku vytvoření individuálních unicastových přenosových drah pro každého uživatele, což rychle spotřebovává rádiové zdroje a šířku pásma jádra sítě s rostoucím počtem příjemců. Tento přístup není škálovatelný ani spektrálně efektivní. MTCH jako součást širšího rámce MBMS tento problém řeší tím, že umožňuje skutečné broadcastové/multicastové vysílání na rádiové úrovni. Umožňuje, aby jediný přenos ze sítě přijímal neomezený počet UE v pokryté oblasti, což dramaticky zlepšuje spektrální účinnost pro služby skupinové komunikace. Jeho vytvoření bylo motivováno snahou umožnit mobilní TV, streamování živých událostí, systémy varování obyvatelstva a skupinové doručování dat (jako jsou softwarové aktualizace vozidel) přes mobilní sítě, čímž se z nich stává platforma schopná vysílání. MTCH poskytuje vyhrazenou, na službu specifickou datovou cestu, která tyto aplikace činí proveditelnými.

## Klíčové vlastnosti

- Downlinkový logický kanál vyhrazený výhradně pro uživatelské datové přenosy MBMS
- Používá point-to-multipoint přenos k obsluze více UE s jedinou alokací rádiových zdrojů
- Asociován s konkrétní MBMS službou identifikovanou pomocí TMGI
- Mapován na transportní kanál Multicast Channel (MCH) v LTE a na FACH v UMTS
- Informace o plánování pro příjem MTCH jsou poskytovány UE prostřednictvím samostatného řídicího kanálu MCCH
- Podporuje jak broadcastový režim (pro otevřené služby), tak multicastový režim (pro služby založené na předplatném)

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [MCH – Multast Channel](/mobilnisite/slovnik/mch/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.768** (Rel-12) — Group Communication System Enablers for LTE
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [MTCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtch/)
