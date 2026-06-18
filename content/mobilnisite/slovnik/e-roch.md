---
slug: "e-roch"
url: "/mobilnisite/slovnik/e-roch/"
type: "slovnik"
title: "E-ROCH – E-DCH Rank and Offset Channel"
date: 2025-01-01
abbr: "E-ROCH"
fullName: "E-DCH Rank and Offset Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-roch/"
summary: "Downlinkový fyzický kanál používaný v UMTS FDD k signalizaci informací o ranku a offsetu pro provoz Enhanced Uplink (E-DCH). Poskytuje UE klíčovou zpětnou vazbu pro efektivní plánování uplinku a řízen"
---

E-ROCH je downlinkový fyzický kanál v UMTS FDD, který signalizuje informace o ranku a offsetu pro UE pro provoz Enhanced Uplink, poskytuje zpětnou vazbu pro plánování uplinku a řízení výkonu.

## Popis

Kanál [E-DCH](/mobilnisite/slovnik/e-dch/) Rank and Offset (E-ROCH) je vyhrazený downlinkový fyzický kanál definovaný ve specifikacích 3GPP UMTS pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)). Funguje v rámci High-Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)) neboli Enhanced Uplink, což je součást UMTS rádiové přístupové sítě. Primární funkcí E-ROCH je přenášet informace Rank a Offset ([RO](/mobilnisite/slovnik/ro/)) z Node B do User Equipment (UE). Tyto informace jsou klíčové pro proces uplinkového přenosu UE. Rank označuje prioritu plánování nebo pořadí, ve kterém může UE vysílat na uplinkovém E-DCH, zatímco Offset poskytuje úpravy řízení výkonu vzhledem k referenční úrovni výkonu. E-ROCH je vysílán nepřetržitě, když je UE v aktivním stavu E-DCH, což zajišťuje včasné aktualizace pro správu uplinkových zdrojů.

Z architektonického hlediska je E-ROCH mapován na specifické downlinkové fyzické zdroje. Je asociován s kanály E-DCH Absolute Grant Channel ([E-AGCH](/mobilnisite/slovnik/e-agch/)) a E-DCH Relative Grant Channel ([E-RGCH](/mobilnisite/slovnik/e-rgch/)), které společně tvoří downlinkovou signalizační sadu pro řízení E-DCH. E-ROCH konkrétně používá předdefinovaný kanalizační kód a je vysílán na Secondary Common Control Physical Channel ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)) nebo podobné downlinkové nosné. Informace na E-ROCH jsou kódovány a modulovány podle procedur fyzické vrstvy UMTS, což zajišťuje spolehlivý příjem UE i v proměnných rádiových podmínkách. UE demoduluje E-ROCH pro extrakci hodnot Rank a Offset, které jsou následně použity k úpravě parametrů uplinkového přenosu.

Role E-ROCH v síti spočívá v umožnění rychlého a efektivního plánování uplinku a řízení výkonu. Poskytováním informací o ranku pomáhá Node B spravovat více UE soutěžících o uplinkové zdroje, snižuje kolize a optimalizuje propustnost. Informace o offsetu umožňují přesné řízení výkonu, minimalizaci interference a šetření životnosti baterie UE. Tento kanál je klíčovou součástí pro dosažení nízké latence a vysokých datových rychlostí, které slibuje HSUPA, protože usnadňuje rychlou adaptaci na měnící se síťové podmínky. Bez E-ROCH by provoz E-DCH spoléhal na pomalejší, méně dynamické řídicí mechanismy, což by podkopalo výkonnostní vylepšení Enhanced Uplink.

## K čemu slouží

E-ROCH byl zaveden, aby řešil potřebu dynamičtější a efektivnější kontroly uplinkových přenosů v sítích UMTS. Před [HSUPA](/mobilnisite/slovnik/hsupa/) spoléhaly uplinkové paketové přenosy v UMTS na Dedicated Channel (DCH), který měl omezení z hlediska latence a flexibility plánování. DCH používal pomalejší, na RNC centrické plánování, které se nemohlo rychle přizpůsobit prudkým změnám rádiových podmínek nebo požadavků na provoz. To vedlo k suboptimálnímu využití zdrojů a vyšším zpožděním pro aplikace s přerušovanými daty. Motivací pro vytvoření E-ROCH spolu s dalšími kanály E-DCH bylo přesunout rozhodování o plánování blíže k rádiovému rozhraní – konkrétně k Node B – což umožňuje rychlejší doby odezvy.

Zavedení Enhanced Uplink ve 3GPP Release 6 mělo za cíl zlepšit výkon uplinku pro paketově spínané služby, ale vyžadovalo vylepšenou řídicí signalizaci pro podporu funkcí jako rychlé plánování a hybridní ARQ (HARQ). E-ROCH byl vyvinut jako součást tohoto vylepšení v Release 11, aby poskytoval explicitní signalizaci ranku a offsetu, která doplňuje grantové kanály (E-AGCH a E-RGCH). Tím se řeší problém neefektivního řízení výkonu uplinku a prioritizace plánování, což umožňuje Node B jemně ladit přenosy UE na základě reálného zatížení sítě a kanálových podmínek. Tím se maximalizuje kapacita uplinku, snižuje interference a zlepšuje celková efektivita systému, čímž se uspokojuje rostoucí poptávka po mobilních datových službách s lepší uživatelskou zkušeností.

## Klíčové vlastnosti

- Přenáší informace Rank pro prioritu plánování UE
- Nese hodnoty Offset pro úpravy řízení výkonu uplinku
- Funguje výhradně v režimu UMTS FDD
- Mapován na downlinkové fyzické kanály, jako je S-CCPCH
- Umožňuje rychlé plánování uplinku řízené Node B
- Podporuje výkonnostní vylepšení Enhanced Uplink (HSUPA)

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [E-AGCH – EDCH – Absolute Grant Channel](/mobilnisite/slovnik/e-agch/)
- [E-RGCH – E-DCH Relative Grant Channel](/mobilnisite/slovnik/e-rgch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [E-ROCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-roch/)
