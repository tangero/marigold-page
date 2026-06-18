---
slug: "e-ucch"
url: "/mobilnisite/slovnik/e-ucch/"
type: "slovnik"
title: "E-UCCH – E-DCH Uplink Control Channel"
date: 2025-01-01
abbr: "E-UCCH"
fullName: "E-DCH Uplink Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-ucch/"
summary: "Fyzický řídicí kanál používaný v režimech TDD UMTS s čipovou rychlostí 3,84 Mcps a 7,68 Mcps pro přenos řídicích informací v uplinku pro Enhanced Dedicated Channel (E-DCH). Přenáší klíčová data jako E"
---

E-UCCH je fyzický řídicí kanál v uplinku v režimech UMTS TDD, který přenáší řídicí informace E-DCH, jako je E-TFCI a RSN, pro podporu provozu HSUPA.

## Popis

[E-DCH](/mobilnisite/slovnik/e-dch/) Uplink Control Channel (E-UCCH) je kanál fyzické vrstvy definovaný pro režimy Time Division Duplex ([TDD](/mobilnisite/slovnik/tdd/)) v UMTS, konkrétně pro varianty s čipovou rychlostí 3,84 Mcps a 7,68 Mcps (často označované jako [TD-SCDMA](/mobilnisite/slovnik/td-scdma/)). Plní analogickou úlohu jako kanál [E-DPCCH](/mobilnisite/slovnik/e-dpcch/) používaný v režimu Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)) pro [HSUPA](/mobilnisite/slovnik/hsupa/). E-UCCH je vysílán uživatelským zařízením (UE) v časových úsecích (timeslot) přidělených pro přenos E-DCH v uplinku. Jeho hlavní úlohou je přenášet nezbytné řídicí informace, které Node B potřebuje pro úspěšné dekódování doprovodných dat E-DCH na kanálu E-UDCH (E-DCH Uplink Data Channel). Klíčové informační pole přenášené na E-UCCH jsou E-DCH Transport Format Combination Indicator ([E-TFCI](/mobilnisite/slovnik/e-tfci/)) a Retransmission Sequence Number ([RSN](/mobilnisite/slovnik/rsn/)). E-TFCI udává velikost transportního bloku a formát současného datového přenosu na E-UDCH. RSN je zásadní pro proces Hybrid ARQ (HARQ) a informuje Node B, zda je aktuální přenos nový paket nebo retransmise, a v případě retransmise, která redundantní verze je použita. Kanál je navržen s robustním kódováním pro zajištění spolehlivého příjmu i na okraji buňky, protože ztráta řídicích informací by způsobila selhání dekódování dat. Jeho struktura a časování jsou těsně integrovány s rámcovou strukturou TDD, kde přenosy v uplinku a downlinku probíhají v různých časových úsecích.

## K čemu slouží

E-UCCH byl zaveden pro umožnění funkce High-Speed Uplink Packet Access (HSUPA) v systémech UMTS TDD (TD-SCDMA). Zatímco HSUPA pro FDD (Release 6) používala E-DPCCH, varianta pro TDD vyžadovala kanál přizpůsobený její časově-úsekové architektuře. Účelem E-UCCH je poskytnout pro TDD stejné nízkolatenční a spolehlivé řídicí signalizování, jaké poskytuje E-DPCCH pro FDD. Řeší problém, jak přenášet dynamické informace o transportním formátu a HARQ v rámci omezení TDD rámce bez spoléhání na pomalejší signalizaci vyšších vrstev. Tento řídicí kanál je zásadní pro dosažení výhod HSUPA – rychlého plánování, adaptivní modulace a kódování a HARQ s inkrementální redundancí – v TDD spektru. Umožňuje TDD Node B provádět rychlé dekódování paketu v uplinku bezprostředně po příjmu, což umožňuje rychlá potvrzení HARQ (odesílaná na E-HICH v downlinku) a efektivní plánovací rozhodnutí pro následující TTI. Bez E-UCCH by TDD HSUPA nebylo schopné dosáhnout cílové vysoké propustnosti v uplinku a nízké latence, a tím udržet paritu s možnostmi HSUPA pro FDD.

## Klíčové vlastnosti

- Přenáší řídicí informace v uplinku pro E-DCH v TDD (TD-SCDMA) s čipovou rychlostí 3,84/7,68 Mcps.
- Přenáší E-TFCI (Transport Format Combination Indicator).
- Přenáší RSN (Retransmission Sequence Number) pro procesy HARQ.
- Umožňuje rychlé dekódování paketů a provoz HARQ v TDD Node B.
- Navržen s robustním kanálovým kódováním pro spolehlivý příjem.
- Časování je sladěno s rámcovou a časově-úsekovou strukturou TDD.

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [E-TFCI – E-DCH Transport Format Combination Indicator](/mobilnisite/slovnik/e-tfci/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [E-UCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-ucch/)
