---
slug: "ngso"
url: "/mobilnisite/slovnik/ngso/"
type: "slovnik"
title: "NGSO – Non-Geostationary Satellite Orbit"
date: 2026-01-01
abbr: "NGSO"
fullName: "Non-Geostationary Satellite Orbit"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ngso/"
summary: "NGSO označuje satelitní systémy fungující na jiných než geostacionárních drahách, především na nízké oběžné dráze (LEO) a střední oběžné dráze (MEO). V rámci 3GPP definuje integraci těchto satelitních"
---

NGSO je typ satelitní oběžné dráhy, především LEO nebo MEO, používaný v 3GPP neterestrických sítích k poskytování pokrytí 5G ve vzdálených oblastech nedostupných pro pozemské buňky.

## Popis

Non-Geostationary Satellite Orbit (NGSO) v kontextu 3GPP odkazuje na standardizaci satelitních komunikačních systémů, které fungují na drahách, kde satelity nejsou vůči bodu na Zemi pevné. Primárně se jedná o nízkou oběžnou dráhu ([LEO](/mobilnisite/slovnik/leo/)), typicky ve výškách 500-2000 km, a střední oběžnou dráhu ([MEO](/mobilnisite/slovnik/meo/)), přibližně 8000-20000 km. To je v kontrastu s geostacionárními satelity ([GEO](/mobilnisite/slovnik/geo/)), které zůstávají stacionární ve výšce ~35 786 km nad rovníkem. 3GPP od Release 15 pracuje na integraci NGSO systémů jako klíčové součásti neterestrických sítí ([NTN](/mobilnisite/slovnik/ntn/)) s cílem učinit je bezproblémovou součástí ekosystému 5G a dalších generací.

Architektura pro integraci NGSO zahrnuje satelit (nebo konstelaci satelitů), který funguje jako rádiový přístupový uzel, často označovaný jako 'létající základnová stanice'. Tento uzel se připojuje k uživatelskému zařízení (UE) na zemi, ve vzduchu nebo na moři prostřednictvím servisního spoje. Satelit je pak zpětně připojen k pozemní bránové stanici (NTN bráně) prostřednictvím napájecího spoje. Brána komunikuje se základnovou sítí 5G (5GC), díky čemuž se satelitní síť jeví jádrové síti jako další rádiová přístupová síť (RAN). Mezi klíčové technické výzvy řešené ve specifikacích patří velmi dlouhé zpoždění šíření (i když kratší než u GEO), vysoké Dopplerovy posuny způsobené pohybem satelitu a přerušovaná viditelnost při pohybu satelitů po obloze. Specifikace 3GPP podrobně popisují potřebné adaptace na fyzické vrstvě (např. upravené postupy časového předstihu, vylepšené synchronizační signály), řízení rádiových prostředků (např. řešení převýběru buňky a předávání spojení mezi rychle se pohybujícími satelity) a v základnové síti (např. správa mobility pro pohybující se buňky).

Fungování NGSO v rámci 3GPP zahrnuje několik operačních režimů. V režimu transparentní (bent-pipe) užitečné náplně satelit pouze zesílí a přepošle rádiový signál mezi UE a bránou. V režimu regenerativní (on-board processing) užitečné náplně může satelit signál demodulovat/dekódovat a chovat se spíše jako tradiční gNB, případně se propojovat s dalšími satelity prostřednictvím mezi-satelitních spojů ([ISL](/mobilnisite/slovnik/isl/)). UE musí být informováno, že se připojuje k NTN buňce, což je indikováno prostřednictvím vysílaných systémových informací. Síť řídí neustálé změny buněk pomocí specifických procedur mobility, potenciálně s využitím pevných sledovacích oblastí na Zemi a prediktivního předávání spojení založeného na známých efemeridních datech satelitu. Tato integrace umožňuje standardnímu smartphonu 5G, případně s lehce vylepšenou anténou, připojit se přímo ke konstelaci satelitů LEO pro základní služby a poskytnout tak skutečně globální pokrytí.

## K čemu slouží

Účelem standardizace NGSO v 3GPP je rozšířit dosah služeb 5G na celý svět a překonat základní omezení pozemských sítí: jejich závislost na pevné infrastruktuře soustředěné v obydlených oblastech. Pozemské sítě nemohou životaschopně pokrýt oceány, pouště, polární regiony nebo vzdálené venkovské oblasti. NGSO satelitní sítě, zejména masivní konstelace [LEO](/mobilnisite/slovnik/leo/), nabízejí řešení pro poskytnutí všudypřítomného připojení, což je klíčový cíl 5G. Tím se řeší případy užití jako globální sledování IoT aktiv, nouzová komunikace v oblastech katastrof a připojení během letu.

Historicky satelitní komunikace fungovala v izolovaných silech s proprietárními technologiemi, nekompatibilními s hromadnými mobilními zařízeními. Motivací pro integraci v 3GPP je využít úspor z rozsahu celulárního ekosystému – miliard zařízení – a umožnit bezproblémovou kontinuitu služeb mezi pozemskými a satelitními sítěmi. Předchozí přístupy vyžadovaly dvou režimová zařízení se samostatnými satelitními modemy. Standardizace [NTN](/mobilnisite/slovnik/ntn/) v 3GPP si klade za cíl umožnit jednomu zařízení transparentně se připojit k libovolnému typu sítě s využitím co největšího množství společného protokolového zásobníku.

Navíc je integrace NGSO poháněna vznikem komerčních mega-konstelací (např. Starlink, OneWeb), které slibují satelitní širokopásmové připojení s vysokou kapacitou a nízkou latencí. Jejich standardizovanou integrací 3GPP zajišťuje, že tyto systémy mohou doplňovat pozemskou 5G, podporovat odolnost sítě prostřednictvím různorodých cest a umožnit nové smlouvy o úrovni služeb pro globální pokrytí. Řeší problém digitální propasti a podporuje komunikaci pro zásadní služby pro vládní a podnikové uživatele kdekoliv na Zemi, naplňující vizi skutečně všudypřítomného připojení.

## Klíčové vlastnosti

- Podpora konstelací satelitů na nízké (LEO) a střední (MEO) oběžné dráze jako přístupových uzlů 5G
- Adaptace pro dlouhé zpoždění šíření a vysoký Dopplerův posun v rádiových protokolech (PHY, RRC)
- Architektury transparentní (bent-pipe) a regenerativní (on-board processing) satelitní užitečné náplně
- Správa mobility pro pohybující se buňky, včetně konceptů buněk pevných vůči Zemi a pohybujících se se Zemí
- Postupy na straně UE a sítě pro zvládání periodické viditelnosti satelitů a pohybu stopy paprsku
- Integrace se základnovou sítí 5G prostřednictvím NTN bran s podporou kontinuity služeb

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)
- [LEO – Low-Earth Orbiting satellites](/mobilnisite/slovnik/leo/)
- [GEO – Geostationary satellite Earth Orbit](/mobilnisite/slovnik/geo/)
- [TN – Terrestrial Network](/mobilnisite/slovnik/tn/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TR 22.865** (Rel-19) — Study on satellite access Phase 3
- **TS 22.887** (Rel-20) — Study on satellite access - Phase 4
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [NGSO na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngso/)
