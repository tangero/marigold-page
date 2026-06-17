---
slug: "ganss"
url: "/mobilnisite/slovnik/ganss/"
type: "slovnik"
title: "GANSS – Galileo and Additional Navigation Satellite Systems"
date: 2025-01-01
abbr: "GANSS"
fullName: "Galileo and Additional Navigation Satellite Systems"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ganss/"
summary: "Galileo and Additional Navigation Satellite Systems (GANSS) je funkce 3GPP, která umožňuje uživatelskému zařízení (UE) využívat více globálních navigačních satelitních systémů (GNSS) kromě primárního"
---

GANSS je funkce 3GPP, která umožňuje uživatelskému zařízení (UE) využívat více globálních navigačních satelitních systémů (GNSS) kromě GPS, včetně systému Galileo, GLONASS, BeiDou a QZSS, pro zlepšenou přesnost a dostupnost určování polohy.

## Popis

Galileo and Additional Navigation Satellite Systems (GANSS) je standardizovaná schopnost v 3GPP, která definuje, jak mobilní zařízení a sítě mohou využívat více globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)) pro vylepšené určování polohy. Zatímco rané lokalizační služby v buňkových sítích primárně spoléhaly na asistovaný [GPS](/mobilnisite/slovnik/gps/) ([A-GPS](/mobilnisite/slovnik/a-gps/)), GANSS rozšiřuje podporu o evropský systém Galileo, ruský [GLONASS](/mobilnisite/slovnik/glonass/), čínský BeiDou, japonský QZSS a satelitní augmentační systémy (SBAS), jako jsou WAAS a [EGNOS](/mobilnisite/slovnik/egnos/). Technologie funguje pomocí asistenčních dat poskytovaných sítí uživatelskému zařízení (UE) prostřednictvím signalizační roviny (např. LTE Positioning Protocol - [LPP](/mobilnisite/slovnik/lpp/)) nebo protokolů uživatelské roviny. Tato asistenční data zahrnují přesné efemeridy, almanach, časovou synchronizaci a ionosférické korekce pro podporované GNSS konstelace, což výrazně snižuje čas do prvního určení polohy (TTFF) a zlepšuje citlivost. GNSS přijímač v UE pak může přijímat signály ze satelitů napříč více systémy současně. Kombinací měření (pseudovzdáleností, fáze nosné vlny) z většího počtu satelitů různých konstelací může lokalizační engine dosáhnout vyšší přesnosti, lepší dostupnosti v městských kaňonech, kde je výhled na jedinou konstelaci omezen, a zvýšené odolnosti proti rušení. Podpora GANSS je integrována do různých síťových a uživatelských metod určování polohy, včetně asistovaného GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), samostatného GNSS a kinematického určování polohy v reálném čase (RTK). Síťové prvky, jako je Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) a Location Management Function (LMF) v 5G, jsou zodpovědné za generování a doručování asistenčních dat GANSS.

## K čemu slouží

GANSS byl vyvinut, aby překonal omezení spoléhání se pouze na americký systém GPS pro satelitní určování polohy v mobilních sítích. Závislost na jediné konstelaci představovala rizika týkající se dostupnosti služby, geopolitických faktorů a výkonnostních omezení v hustě zastavěných městských nebo vnitřních prostředích, kde je viditelnost satelitů špatná. Rozšíření dalších globálních a regionálních GNSS konstelací (Galileo, GLONASS, BeiDou) představovalo příležitost k výraznému zlepšení výkonu určování polohy. GANSS byl vytvořen, aby standardizoval podporu těchto více systémů a zajistil interoperabilitu mezi čipsety, koncovými zařízeními a síťovou infrastrukturou od různých dodavatelů. Řeší kritické problémy pro tísňové služby (např. E112 v EU), kde je spolehlivá a přesná poloha otázkou života a smrti, zejména u volání z vnitřních prostor. Pro komerční aplikace umožňuje přesnější navigaci s pokyny, reklamu založenou na poloze, sledování majetku a podporuje vznikající služby s vysokou přesností pro IoT, autonomní vozidla a rozšířenou realitu. Historická motivace je v souladu s globálními snahami o vytvoření více-GNSS prostředí pro odolnost a výkon, což 3GPP standardizovalo, aby zajistilo, že mobilní ekosystém může plně využít těchto pokroků.

## Klíčové vlastnosti

- Podpora více GNSS konstelací: Galileo, GLONASS, BeiDou, QZSS a SBAS
- Doručování asistenčních dat specifických pro konstelaci (efemeridy, almanach, čas, ionosférické korekce) prostřednictvím LPP
- Vylepšená přesnost, dostupnost a integrita určování polohy díky diverzitě satelitních signálů
- Snížený čas do prvního určení polohy (TTFF) a lepší citlivost pro určování polohy ve vnitřních/městských prostředích
- Integrace s 3GPP protokoly pro určování polohy ve signalizační rovině (LPP/LPPa) a uživatelské rovině (SUPL)
- Podpora pokročilých technik, jako je kinematické určování polohy v reálném čase (RTK) a přesné bodové určování polohy (PPP)

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)

## Definující specifikace

- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 25.704** (Rel-12) — Study on Enhanced Broadcast of System Information
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [GANSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ganss/)
