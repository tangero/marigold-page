---
slug: "rtd"
url: "/mobilnisite/slovnik/rtd/"
type: "slovnik"
title: "RTD – Relative Time Difference"
date: 2025-01-01
abbr: "RTD"
fullName: "Relative Time Difference"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rtd/"
summary: "RTD je měření časového rozdílu příchodu signálů z cílové buňky a referenční buňky, používané v lokalizačních metodách jako OTDOA a UTDOA. Je to základní parametr pro výpočet geografické polohy UE v mo"
---

RTD je změřený časový rozdíl příchodu signálů z cílové buňky a referenční buňky, používaný pro vysoce přesnou lokalizaci UE v metodách jako je OTDOA.

## Popis

Relative Time Difference (RTD) je klíčový parametr v metodách lokalizace založených na pozorovaném časovém rozdílu příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)) a na časovém rozdílu příchodu v uplinku ([UTDOA](/mobilnisite/slovnik/utdoa/)) definovaných 3GPP. Představuje synchronizační odchylku mezi dvěma základnovými stanicemi (eNodeB v LTE, gNB v NR nebo NodeB v UMTS), jak je pozorována na uživatelském zařízení (UE) nebo jednotce pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)). V metodě OTDOA založené na downlinku měří UE Referenční signálový časový rozdíl ([RSTD](/mobilnisite/slovnik/rstd/)), což je relativní časový rozdíl mezi pozicovacím referenčním signálem ([PRS](/mobilnisite/slovnik/prs/)) ze sousední buňky a PRS z referenční buňky. Samotné měření RSTD však zahrnuje geometrický časový rozdíl způsobený polohou UE a RTD mezi buňkami. RTD je rozdíl v okamžicích vysílání mezi dvěma buňkami. Pro výpočet skutečného geometrického časového rozdílu příchodu (TDOA) musí síťový lokalizační server (např. [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE, [LMF](/mobilnisite/slovnik/lmf/) v 5G) odečíst známý nebo odhadovaný RTD od naměřené hodnoty RSTD hlášené UE: Geometrický TDOA = RSTD – RTD. Hodnota RTD může být poskytnuta lokalizačnímu serveru, pokud jsou buňky synchronizovány (např. pomocí [GPS](/mobilnisite/slovnik/gps/) nebo IEEE 1588), díky čemuž je RTD blízké nule, nebo ji může síť odhadnout pomocí LMU, které měří signály z více základnových stanic. Každé měření TDOA definuje hyperbolu možných poloh UE; průnik více hyperbol z různých párů buněk určí polohu. Přesnost znalosti RTD přímo ovlivňuje přesnost lokalizace. V 5G NR se tento koncept rozšiřuje na použití signálů z více vysílacích/přijímacích bodů (TRP) a správa RTD se stává složitější v asynchronních nasazeních.

## K čemu slouží

RTD byl zaveden, aby umožnil síťovou lokalizaci v mobilních systémech, kde základnové stanice nejsou dokonale synchronizovány. Rané lokalizační služby, jako je Cell-ID, poskytovaly velmi hrubou přesnost. Potřeba lokalizace volajících v nouzových případech (E911, E112) a služeb založených na poloze poháněla vývoj přesnějších technik, jako je OTDOA. Základní výzvou je, že UE měří pozorované časové rozdíly, které jsou kombinací zpoždění šíření (užitečného pro lokalizaci) a časových rozdílů vysílačů (nežádoucích). Parametr RTD existuje pro kvantifikaci a korekci těchto časových odchylek vysílačů. Přesným určením nebo kompenzací RTD může síť izolovat čistý geometrický časový rozdíl, což umožňuje přesnou trilateraci. Tím se vyřešil problém implementace přesné lokalizace TDOA v praktických, potenciálně asynchronních, mobilních nasazeních bez nutnosti nepřiměřeně nákladné dokonalé synchronizace každé buňky.

## Klíčové vlastnosti

- Klíčový korekční parametr pro převod RSTD naměřeného UE na geometrický TDOA
- Může být považován za nulový v synchronizovaných sítích (např. při použití GNSS v základnových stanicích)
- Odhadován síťovými jednotkami pro měření polohy (LMU) v asynchronních nasazeních
- Lokalizačním serverem (E-SMLC/LMF) hlášen UE jako pomocná data pro OTDOA
- Přímo ovlivňuje přesnost lokalizačních metod OTDOA a UTDOA
- Spravován jako součást celkové lokalizační architektury v řešeních signalizační i uživatelské roviny

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [RSTD – Reference Signal Time Difference](/mobilnisite/slovnik/rstd/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [RTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtd/)
