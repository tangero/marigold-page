---
slug: "rl"
url: "/mobilnisite/slovnik/rl/"
type: "slovnik"
title: "RL – Reinforcement Learning"
date: 2025-01-01
abbr: "RL"
fullName: "Reinforcement Learning"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rl/"
summary: "Reinforcement Learning (RL, učení posilováním) je paradigma strojového učení, v němž se agent učí optimální akce prostřednictvím interakcí metodou pokus-omyl se svým prostředím za účelem maximalizace"
---

RL je paradigma strojového učení zkoumané v rámci 3GPP pro autonomní optimalizaci sítě, v němž agent učením metodou pokus-omyl hledá optimální akce, aby maximalizoval odměny a zvýšil efektivitu sítě v dynamických rádiových podmínkách.

## Popis

Reinforcement Learning (RL, učení posilováním) je odvětví strojového učení, v němž autonomní agent se učí rozhodovat prováděním akcí v prostředí za účelem dosažení cíle. Agent přijímá zpětnou vazbu ve formě odměn nebo penalizací, která jej prostřednictvím průzkumu a využívání navádí k optimálnímu chování. V kontextech 3GPP se RL aplikuje na telekomunikační sítě pro řešení výzev v oblasti správy rádiových zdrojů, síťového segmentování (network slicing), správy mobility a energetické účinnosti. Agent, typicky implementovaný v rámci síťových funkcí jako RAN Intelligent Controller (RIC) nebo systémů řízení, interaguje se síťovým prostředím, které zahrnuje základnové stanice, uživatelská zařízení a charakteristiky provozu. Mezi klíčové komponenty patří stav (např. podmínky kanálu, zatížení), akce (např. úprava parametrů), odměna (např. propustnost, latence) a politika (mapování stavů na akce). Algoritmy RL, jako je Q-learning nebo hluboké RL, umožňují agentovi učit se z historických a reálných dat a přizpůsobovat se dynamickým podmínkám bez explicitního naprogramování. To umožňuje samooptimalizující se sítě, které dokážou předvídat a reagovat na změny, čímž zlepšují metriky výkonu jako kapacita a spolehlivost. Ve specifikacích 3GPP je RL studováno pro případy užití, jako je správa svazků v NR, směrování provozu a detekce anomálií, často integrované s rámci jako [NWDAF](/mobilnisite/slovnik/nwdaf/) pro datovou analytiku. Architektura může zahrnovat centralizované, distribuované nebo hybridní přístupy učení s ohledem na latenci, škálovatelnost a standardizaci napříč releasy.

## K čemu slouží

Reinforcement Learning bylo v rámci 3GPP zavedeno pro řešení rostoucí složitosti a dynamiky moderních mobilních sítí, zejména s nástupem 5G a dalších generací. Tradiční optimalizace sítě spoléhá na statické algoritmy založené na pravidlech nebo manuální ladění, které špatně reagují na rychle se měnící podmínky, jako jsou proměnlivé hustoty uživatelů, typy provozu a rádiová prostředí. RL umožňuje autonomní, daty řízené rozhodování, což sítím umožňuje se v reálném čase samooptimalizovat, snižovat provozní náklady a zvyšovat efektivitu. Historicky správa sítí zahrnovala heuristické metody, které byly nepružné a vyžadovaly rozsáhlý lidský zásah. RL tyto limity zmírňuje tím, že se učí optimální strategie ze zkušenosti a zvládá nelineární a vysoce dimenzionální problémy, které jsou pro konvenční přístupy náročné. Jeho zavedení motivovala potřeba inteligentní automatizace pro podporu rozmanitých případů užití 5G, jako je massive IoT, ultra-spolehlivá nízkolatenční komunikace a vylepšené mobilní širokopásmové připojení, kde je dynamické přidělování zdrojů klíčové. Začleněním RL si 3GPP klade za cíl podporovat adaptivnější, odolnější a škálovatelnější sítě schopné autonomně uspokojovat budoucí požadavky.

## Klíčové vlastnosti

- Autonomní rozhodování prostřednictvím učení metodou pokus-omyl
- Adaptace na dynamické síťové podmínky bez manuálního zásahu
- Optimalizace klíčových ukazatelů výkonu, jako je propustnost a latence
- Integrace s rámci síťové analytiky, jako je NWDAF
- Podpora různých případů užití včetně správy svazků a směrování provozu
- Škálovatelnost napříč centralizovanými, distribuovanými nebo hybridními architekturami

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B
- **TR 25.929** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [RL na 3GPP Explorer](https://3gpp-explorer.com/glossary/rl/)
