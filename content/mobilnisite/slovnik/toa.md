---
slug: "toa"
url: "/mobilnisite/slovnik/toa/"
type: "slovnik"
title: "TOA – Time Of Arrival"
date: 2025-01-01
abbr: "TOA"
fullName: "Time Of Arrival"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/toa/"
summary: "Time Of Arrival (TOA) je základní měření v mobilních sítích představující absolutní čas, kdy rádiový signál přijme zařízení nebo základnová stanice od vysílače. Je to klíčový parametr pro určování pol"
---

TOA je absolutní čas, kdy rádiový signál přijme zařízení nebo základnová stanice od vysílače; používá se jako základní měření pro určování polohy a lokalizační služby.

## Popis

Time Of Arrival (TOA) je základní princip měření v šíření rádiového signálu používaný k určení vzdálenosti mezi vysílačem a přijímačem. Základní koncept vychází z konstantní rychlosti světla (rádiových vln). Přesným změřením času, který potřebuje známý signál k přenosu od vysílače (např. základnové stanice nebo uživatelského zařízení) k přijímači, lze vypočítat délku přenosové dráhy jako vzdálenost = rychlost světla * čas. V systémech 3GPP se měření TOA provádí na fyzické vrstvě a vyžaduje vysoce synchronizované síťové prvky. Přijímač koreluje příchozí signál se známým referenčním vzorem (jako je pilotní nebo synchronizační signál), aby identifikoval přesný okamžik příchodu. Tato časová značka je následně zpracována, často ve spojení s měřeními z jiných buněk, pro výpočet odhadu polohy.

Architektura pro určování polohy založené na TOA zahrnuje více síťových komponent. UE nebo jednotka pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)) provádí příjem signálu a počáteční časové označení. Naměřené hodnoty TOA jsou hlášeny uzlu pro určování polohy, jako je Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G. Tyto uzly mají znalost geografických souřadnic a přesného časování vysílacích uzlů (gNB, [eNB](/mobilnisite/slovnik/enb/), ng-eNB). Pomocí algoritmů, jako je Observed Time Difference Of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo Uplink Time Difference Of Arrival ([UTDOA](/mobilnisite/slovnik/utdoa/)), uzel pro určování polohy vypočítá rozdíly v TOA z více zdrojů, aby provedl hyperbolickou trilateraci a určil polohu UE.

Role TOA přesahuje základní určování polohy. Je nedílnou součástí synchronizace sítě, zejména v systémech s časovým duplexním dělením ([TDD](/mobilnisite/slovnik/tdd/)) a při koordinovaném vícebodovém přenosu (CoMP), kde je klíčové přesné časové sladění mezi buňkami. Na přesnost TOA má vliv několik faktorů, včetně vícecestného šíření, podmínek bez přímé viditelnosti ([NLOS](/mobilnisite/slovnik/nlos/)), časových odchylek hodin a šířky pásma signálu – větší šířka pásma obecně umožňuje jemnější časové rozlišení. Proto specifikace 3GPP definují pokročilé techniky zpracování signálu, jako je použití referenčních signálů pro určování polohy (PRS) se specifickými vzory a vysokou periodicitou, aby se zmírnily chyby a zvýšila přesnost měření za různých rádiových podmínek.

## K čemu slouží

TOA bylo zavedeno, aby poskytlo základní metodu určování geografické polohy uživatelského zařízení (UE) na bázi sítě. Tuto schopnost poháněly regulatorní požadavky, nejvýznamněji nařízení Enhanced 911 (E911) ve Spojených státech, které vyžadovalo, aby mobilní sítě poskytovaly službám tísňového volání polohu volajícího. Před standardizovanými metodami TOA se sítě spoléhaly hlavně na méně přesné určování polohy založené na identifikátoru buňky nebo vyžadovaly ruce s podporou GPS, které nebyly všeobecně dostupné. Techniky založené na TOA nabídly síťově orientované řešení, které mohlo fungovat s jakýmkoli kompatibilním koncovým zařízením, a tím zlepšily spolehlivost pro služby tísňového volání.

Vytvoření standardů pro měření TOA řešilo omezení zjednodušených metod založených na blízkosti. Samotná identita buňky poskytuje pouze oblast obsluhující buňky, která může zahrnovat několik kilometrů, což je pro přesnou reakci v tísňových případech nedostatečné. TOA umožněním měření vzdálenosti na bázi času umožnilo mnohem jemnější určení polohy. Jeho vývoj byl motivován potřebou škálovatelného, standardizovaného měření, které by mohlo být implementováno napříč zařízeními různých dodavatelů a síťovými generacemi, od UMTS přes LTE až po 5G NR, a zajišťovalo zpětnou kompatibilitu a budoucí vývoj.

Kromě toho, přesahujíc služby tísňového volání, TOA umožňuje širokou škálu komerčních služeb založených na poloze (LBS), plánování sítě, optimalizaci a nové případy užití, jako je sledování aktiv a geolokace IoT. Poskytuje základní metriku pro pokročilejší metody určování polohy, jako je OTDOA, a tvoří tak kritickou součást celkové architektury určování polohy 3GPP, která vyvažuje přesnost, latenci a zatížení sítě.

## Klíčové vlastnosti

- Základní měření pro výpočet vzdálenosti šíření signálu
- Umožňuje síťové metody určování polohy, jako je OTDOA a UTDOA
- Vyžaduje vysoce přesnou synchronizaci sítě (např. přes GPS nebo IEEE 1588)
- Využívá specifické referenční signály (např. PRS v LTE/NR) pro přesnou detekci
- Měření prováděno jak UE (downlink), tak sítí (uplink)
- Přesnost je funkcí šířky pásma signálu a vícecestného prostředí

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [TOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/toa/)
