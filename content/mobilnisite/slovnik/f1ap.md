---
slug: "f1ap"
url: "/mobilnisite/slovnik/f1ap/"
type: "slovnik"
title: "F1AP – F1 Application Protocol"
date: 2025-01-01
abbr: "F1AP"
fullName: "F1 Application Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/f1ap/"
summary: "F1AP je aplikační protokol vrstvy fungující přes rozhraní F1-C mezi gNB-CU a gNB-DU. Definuje signalizační procedury pro správu UE, řízení přenosových kanálů a mobilitu, což umožňuje koordinovaný prov"
---

F1AP je aplikační protokol vrstvy pro rozhraní F1-C, který definuje signalizační procedury mezi gNB-CU a gNB-DU pro správu UE, řízení přenosových kanálů a mobilitu v disagregované 5G RAN.

## Popis

F1 Application Protocol (F1AP) je klíčový signalizační protokol umožňující komunikaci řídicí roviny mezi centrální jednotkou ([CU](/mobilnisite/slovnik/cu/)) a distribuovanou jednotkou ([DU](/mobilnisite/slovnik/du/)) disagregovaného 5G gNB. Funguje nad protokolem Stream Control Transmission Protocol (SCTP) přes IP a poskytuje spolehlivý transport pro své zprávy. F1AP definuje komplexní sadu elementárních procedur (EPs), které jsou základními jednotkami interakce mezi CU a DU. Tyto procedury jsou kategorizovány do třídy 1 (vyžadující odpověď) a třídy 2 (nevyžadující odpověď).

Protokol funguje prostřednictvím výměny zpráv F1AP, z nichž každá nese informační elementy (IEs) obsahující potřebné parametry pro danou proceduru. Mezi klíčové funkční oblasti pokryté protokolem F1AP patří: správa rozhraní (např. nastavení F1, aktualizace konfigurace gNB-DU, indikace chyb), správa kontextu UE (např. zřízení, modifikace a uvolnění kontextu UE), přenos [RRC](/mobilnisite/slovnik/rrc/) zpráv (transparentní přenos RRC zpráv mezi RRC vrstvou CU a UE přes DU) a správa přenosových kanálů (řízení zřizování a modifikace datových radiových kanálů). Dále F1AP zajišťuje procedury mobility, jako je příprava předání, a správu systémových informací, kdy CU poskytuje zprávy SI, které má DU vysílat.

Z architektonického hlediska se F1AP nachází v CU-CP (řídicí rovina) a v DU. Každá zpráva F1AP je asociována s konkrétním kontextem UE (pro signalizaci asociovanou s UE) nebo s celým rozhraním F1 (pro signalizaci neasociovanou s UE). Protokol je navržen tak, aby byl efektivní a škálovatelný, a podporuje správu tisíců UE připojených k jedné DU. Jeho robustní mechanismy pro zpracování chyb a obnovu zajišťují stabilitu rozhraní F1, což je klíčové pro udržení kontinuity služeb v RAN.

## K čemu slouží

F1AP byl vytvořen, aby poskytl standardizovaný, robustní a funkčně bohatý signalizační protokol pro nové rozhraní F1 zavedené s 5G CU-DU rozdělením. Před 5G byla interní komunikace uvnitř základnové stanice proprietární a závislá na dodavateli, protože [eNB](/mobilnisite/slovnik/enb/) bylo monolitickou entitou. Disagregace gNB na [CU](/mobilnisite/slovnik/cu/) a [DU](/mobilnisite/slovnik/du/) si vyžádala otevřený, interoperabilní protokol pro správu složité koordinace mezi těmito dvěma síťovými funkcemi.

Protokol řeší základní problém, jak může centralizovaná řídicí entita (CU-CP) ovládat a spravovat distribuovanou rádiovou jednotku (DU), která zajišťuje fyzickou vrstvu. Poskytuje nezbytný jazyk pro všechny řídicí interakce, od připojení UE do sítě až po správu její mobility a kvality služeb. Bez F1AP by CU a DU od různých dodavatelů nemohly spolupracovat, což by znemožnilo účel otevřeného rozhraní.

Historicky byl vývoj F1AP ovlivněn podobným protokolem X2AP používaným pro komunikaci mezi eNB v 4G, ale byl navržen od základů, aby řešil specifické potřeby *intra*-gNB rozhraní s těsnější integrací a komplexnější kontrolou. Jeho vytvoření motivoval průmyslový posun k virtualizaci, cloudifikaci a Open RAN. F1AP je klíčovým pojivem, které činí funkční rozdělení definované 3GPP prakticky realizovatelným, což operátorům umožňuje nasazovat flexibilní, škálovatelné a nákladově efektivní architektury RAN při zachování plné kontroly nad rádiovými zdroji a uživatelskými relacemi.

## Klíčové vlastnosti

- Definuje elementární procedury (EPs) pro signalizaci mezi CU a DU přes SCTP
- Spravuje životní cyklus kontextu UE (zřízení, modifikace, uvolnění)
- Poskytuje transparentní transport pro RRC zprávy mezi CU a UE
- Řídí zřizování a modifikaci datových radiových kanálů (DRBs)
- Zajišťuje přenos systémových informací z CU na DU pro vysílání
- Podporuje procedury mobility včetně přípravy a provedení předání

## Související pojmy

- [F1-C – F1 Control Plane Interface](/mobilnisite/slovnik/f1-c/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.470** (Rel-19) — F1 Interface Introduction

---

📖 **Anglický originál a plná specifikace:** [F1AP na 3GPP Explorer](https://3gpp-explorer.com/glossary/f1ap/)
