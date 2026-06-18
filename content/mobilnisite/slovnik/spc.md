---
slug: "spc"
url: "/mobilnisite/slovnik/spc/"
type: "slovnik"
title: "SPC – Signalling Preconfigured Channel"
date: 2025-01-01
abbr: "SPC"
fullName: "Signalling Preconfigured Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/spc/"
summary: "Předkonfigurovaný logický kanál v UMTS a LTE používaný pro vyhrazený přenos signalizace mezi uživatelským zařízením (UE) a sítí, zajišťující spolehlivou komunikaci řídicí roviny. Vytváří standardizova"
---

SPC je předkonfigurovaný logický kanál v UMTS a LTE, který poskytuje vyhrazenou a spolehlivou cestu pro signalizační zprávy řídicí roviny mezi uživatelským zařízením (UE) a sítí, oddělenou od uživatelských dat.

## Popis

Signalling Preconfigured Channel (SPC) je základní koncept v systémech 3GPP UMTS a LTE, definovaný v řadě specifikací včetně TS 25.410 a TS 29.007. Odkazuje na předem zřízený logický kanál vyhrazený výhradně pro přenos signalizačních zpráv mezi uživatelským zařízením (UE) a jádrem sítě (CN) nebo rádiovou přístupovou sítí (RAN). Na rozdíl od kanálů pro uživatelská data je SPC konfigurován během připojení k síti nebo navázání spojení, aby poskytl spolehlivou cestu s nízkou latencí pro informace řídicí roviny. Tento kanál funguje přes rádiové rozhraní a je řízen protokoly jako Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), což usnadňuje základní funkce jako zřizování hovorů, předávání spojení a správu relací.

Z architektonického hlediska je SPC implementován v rámci protokolových zásobníků jak na straně UE, tak síťových uzlů, jako je Node B v UMTS nebo eNode B v LTE. Používá specifické identifikátory logických kanálů a je mapován na transportní kanály, jako je Dedicated Channel ([DCH](/mobilnisite/slovnik/dch/)) nebo Shared Channel, v závislosti na typu rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)). Kanál je charakterizován svými předkonfigurovanými parametry, včetně nastavení kvality služeb (QoS), úrovní priority a konfigurací zabezpečení, které jsou vyjednány během počátečních procedur. To zajišťuje, že signalizační provoz dostává přednostní zacházení, minimalizuje se zpoždění a zvyšuje se odezva sítě.

Během provozu SPC přenáší různé signalizační zprávy, včetně protokolů pro správu mobility ([MM](/mobilnisite/slovnik/mm/)), správu spojení ([CM](/mobilnisite/slovnik/cm/)) a správu relací ([SM](/mobilnisite/slovnik/sm/)). Například v UMTS podporuje signalizaci Iu mezi [RNC](/mobilnisite/slovnik/rnc/) a CN; v LTE usnadňuje signalizaci S1-MME. Spolehlivost kanálu je udržována prostřednictvím mechanismů opravy chyb a protokolů pro opakovaný přenos, jako je režim RLC AM. Jeho role je klíčová pro udržení integrity sítě, umožnění plynulé mobility a podporu pokročilých služeb tím, že zajišťuje efektivní a bezpečné doručování řídicích příkazů.

## K čemu slouží

SPC byl zaveden, aby řešil potřebu vyhrazeného a spolehlivého kanálu pro signalizační provoz v systémech 3GPP, oddělující řídicí rovinu od uživatelské roviny za účelem zvýšení stability a výkonu sítě. Před jeho standardizací často rané mobilní systémy míchaly signalizaci a data, což vedlo k přetížení a problémům se spolehlivostí. SPC to řeší poskytnutím předkonfigurované cesty, která garantuje prostředky pro kritické řídicí zprávy.

Motivován vývojem od 2G k 3G (UMTS) a dále, SPC podporuje složité síťové operace jako předávání spojení a správu QoS. Řeší omezení sdílených kanálů tím, že zajišťuje nízkou latenci a vysokou dostupnost pro signalizaci, což je nezbytné pro služby v reálném čase a události mobility. Jeho vytvoření odráží zaměření 3GPP na robustní síťovou architekturu, která umožňuje škálovatelnou a efektivní komunikaci řídicí roviny napříč generacemi.

## Klíčové vlastnosti

- Vyhrazený logický kanál pro signalizační zprávy
- Předkonfigurován během připojení k síti nebo navázání spojení
- Podporuje přenos protokolů RRC a NAS
- Zajišťuje spolehlivou komunikaci řídicí roviny s nízkou latencí
- Mapován na specifické transportní kanály (např. DCH v UMTS)
- Prioritizovaná QoS pro signalizační provoz

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.863** (Rel-8) — IMS-CS Multimedia Interworking Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [SPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/spc/)
