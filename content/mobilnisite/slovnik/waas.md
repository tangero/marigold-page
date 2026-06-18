---
slug: "waas"
url: "/mobilnisite/slovnik/waas/"
type: "slovnik"
title: "WAAS – Wide Area Augmentation System"
date: 2025-01-01
abbr: "WAAS"
fullName: "Wide Area Augmentation System"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/waas/"
summary: "Wide Area Augmentation System (WAAS) je satelitní augmentační systém (SBAS), který zvyšuje přesnost, integritu a dostupnost signálů GPS pro navigaci. V 3GPP je podporován jako metoda určování polohy p"
---

WAAS je satelitní augmentační systém, který zvyšuje přesnost signálu GPS pro použití jako metoda určování polohy podporovaná 3GPP v uživatelském zařízení.

## Popis

Wide Area Augmentation System (WAAS) je regionální satelitní augmentační systém ([SBAS](/mobilnisite/slovnik/sbas/)), který primárně provozuje Federal Aviation Administration (FAA) za účelem zlepšení výkonu globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)), jako je [GPS](/mobilnisite/slovnik/gps/), nad Severní Amerikou. Ve specifikacích 3GPP je WAAS uváděn jako podporovaná metoda určování polohy pro uživatelské zařízení (UE), umožňující přesnější a spolehlivější určení polohy. Systém funguje pomocí sítě pozemních referenčních stanic, které monitorují signály GPS satelitů. Tyto stanice sbírají data o chybách způsobených ionosférickými poruchami, driftem satelitních hodin a nepřesnostmi efemerid. Data jsou zpracována v hlavních stanicích za účelem generování korekčních zpráv, které jsou následně vysílány na geostacionární satelity ([GEO](/mobilnisite/slovnik/geo/) satelity) pro rozšíšení k uživatelským zařízením ve stejném kmitočtovém pásmu jako GPS. UE přijímá jak standardní GPS signály, tak WAAS korekční zprávy, a aplikuje korekce v reálném čase pro výpočet přesnější polohy. Architektonicky integrace WAAS v 3GPP zahrnuje polohovací schopnosti UE, kde může UE hlásit svou schopnost používat WAAS (nebo jiný SBAS) v polohovacích protokolech, jako je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo NR Positioning Protocol (NRPP). Síť může vyžadovat nebo asistovat při určování polohy s podporou WAAS pro služby jako je lokalizace tísňového volání (E911) nebo komerční polohově závislé služby. Klíčové komponenty zahrnují WAAS GEO satelity, pozemní stanice pro vysílání signálu vzhůru a GNSS přijímač UE s podporou SBAS. Jeho úlohou je poskytovat vylepšený výkon určování polohy, který splňuje požadavky pro aplikace týkající se bezpečnosti života, jež vyžadují vysokou integritu, přesnost a dostupnost nad rámec toho, co nabízí samostatný GPS.

## K čemu slouží

WAAS byl vytvořen, aby řešil omezení samostatného [GPS](/mobilnisite/slovnik/gps/), kterému chybí dostatečná přesnost, integrita a dostupnost pro kritické aplikace, zejména v letectví. Samotný GPS může mít chyby v řádu několika metrů a neposkytuje včasná varování, když je systém nespolehlivý. WAAS tyto problémy řeší poskytováním diferenciálních korekcí a monitorování integrity, čímž snižuje polohové chyby na méně než jeden metr horizontálně i vertikálně. To umožňuje přesné přiblížení v letectví bez nutnosti pozemních navigačních pomůcek. V kontextu 3GPP podpora WAAS umožňuje mobilním sítím využít tuto vylepšenou polohovací schopnost pro tísňové služby, kde může přesná lokalizace zachraňovat životy, a pro pokročilé polohově závislé služby vyžadující vyšší přesnost. Integrace do norem 3GPP, počínaje Release 8, byla motivována regulatorními požadavky na vylepšenou lokalizaci tísňových volajících a rostoucí poptávkou po přesném určování polohy v různých komerčních a bezpečnostních aplikacích, čímž překlenuje propast mezi telekomunikačními a satelitními navigačními systémy.

## Klíčové vlastnosti

- Poskytuje diferenciální korekce pro GPS signály za účelem zlepšení přesnosti určování polohy
- Rozšiřuje informace o integritě, aby varoval uživatele před nespolehlivými GPS signály
- Využívá geostacionární satelity k doručování korekčních dat přes širokou oblast
- Zlepšuje vertikální a horizontální přesnost určování polohy na 1-2 metry
- Podporován jako metoda určování polohy v polohovacích protokolech 3GPP UE (např. LPP)
- Zvyšuje dostupnost a kontinuitu služby GNSS pro bezpečnostně kritické aplikace

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [GPS – Global Positioning System](/mobilnisite/slovnik/gps/)
- [SBAS – Satellite Based Augmentation Systems](/mobilnisite/slovnik/sbas/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [WAAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/waas/)
