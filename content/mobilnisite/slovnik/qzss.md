---
slug: "qzss"
url: "/mobilnisite/slovnik/qzss/"
type: "slovnik"
title: "QZSS – Quasi-Zenith Satellite System"
date: 2025-01-01
abbr: "QZSS"
fullName: "Quasi-Zenith Satellite System"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qzss/"
summary: "Japonský regionální satelitní navigační systém a augmentační služba. Skládá se z konstelace satelitů na kvazizenitálních drahách (Quasi-Zenith Orbits) a geostacionárních drahách, poskytuje signály pro"
---

QZSS je japonský regionální satelitní navigační systém, který poskytuje signály pro určování polohy a augmentační signály kompatibilní se systémem GPS za účelem zvýšení přesnosti a dostupnosti pro uživatele v regionu Asie a Oceánie.

## Popis

Systém QZSS (Quasi-Zenith Satellite System) je japonský regionální satelitní systém pro určování polohy, navigaci a časovou synchronizaci (PNT). Jeho hlavním cílem je zlepšit výkon stávajících globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)), jako je [GPS](/mobilnisite/slovnik/gps/), v regionu Asie a Oceánie, se zaměřením na Japonsko. Architektura systému se skládá z konstelace satelitů: některé jsou na vysoce eliptických kvazizenitálních drahách (QZO) a další na geostacionárních drahách. Satelity na drahách QZO sledují jedinečnou trajektorii, díky níž se zdá, že setrvávají pod velmi vysokým elevančním úhlem nad Japonskem, což minimalizuje překážky signálu.

QZSS vysílá více typů signálů. Vysílá signály kompatibilní se systémem GPS (L1C/A, L2C, L5) a Galileo (E6), což umožňuje standardním přijímačům GNSS používat satelity QZSS jako další zdroje pro měření vzdálenosti, což přímo zlepšuje geometrii satelitů (Dilution of Precision). Důležitější je, že vysílá augmentační signály: L1-Submeter-class Augmentation with Integrity Function (L1S), L5-Submeter-class Augmentation with Integrity Function (L5S) a signál L6 pro službu Centimeter Level Augmentation Service ([CLAS](/mobilnisite/slovnik/clas/)). Tyto signály nesou korekční data pro satelitní dráhy a hodiny, ionosférická zpoždění a zprávy o integritě.

V rámci ekosystému 3GPP je QZSS plně integrován jako podporovaná konstelace GNSS pro Assisted GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Síť může poskytovat asistenční data specifická pro QZSS – jako jsou efemeridy, almanach a korekce hodin – do uživatelského zařízení (UE) prostřednictvím protokolů řídicí nebo uživatelské roviny. To umožňuje přijímači GNSS v zařízení UE získat signály QZSS rychleji (kratší Time To First Fix) a s vyšší citlivostí. Specifikace definují kompletní sadu datových prvků a procedur od lokalizačního serveru (např. [E-SMLC](/mobilnisite/slovnik/e-smlc/), [LMF](/mobilnisite/slovnik/lmf/)) k zařízení UE, což umožňuje hybridní určování polohy s využitím QZSS společně se systémy GPS, Galileo a BeiDou. Tato integrace je klíčová pro splnění přísných požadavků na určování polohy pro záchranné služby (např. E911), komerční služby založené na poloze a pokročilé aplikace, jako je autonomní řízení v pokrytých regionech.

## K čemu slouží

QZSS byl koncipován k řešení kritických výzev národní infrastruktury souvisejících se spolehlivostí určování polohy v Japonsku. Jedinečné prostředí Japonska – charakterizované hustou městskou zástavbou, hornatým terénem a polohou ve středních zeměpisných šířkách – znamená, že satelity globálních konstelací, jako je [GPS](/mobilnisite/slovnik/gps/), jsou často nízko nad obzorem, což vede k častému rušení signálu. To mělo za následek špatnou dostupnost a přesnost určování polohy pro navigaci, geodetické práce, reakci na katastrofy a zemědělství. Původní motivací bylo zajistit nepřetržité, vysoce kvalitní služby PNT pro společenskou a ekonomickou stabilitu.

Vývoj QZSS byl také motivován potřebou nezávislosti a redundance. Nadměrná závislost na jediném cizím systému [GNSS](/mobilnisite/slovnik/gnss/) (GPS) byla vnímána jako potenciální riziko pro národní bezpečnost a ekonomické aktivity. QZSS poskytuje kontrolovatelnou regionální schopnost, která augmentuje a zálohuje GPS. Dále umožňuje pokročilé služby, které nejsou globálně dostupné pouze z GPS, jako jsou vysoko-integrální výstrahy pro bezpečnostně kritické aplikace (letecká a námořní doprava) a přesnost na úrovni subměru až centimetru prostřednictvím svých augmentačních signálů. Vytvořením vlastního systému Japonsko získalo schopnost přizpůsobit služby PNT svým specifickým regionálním potřebám, podpořit domácí technologické inovace v kosmickém a pozemním segmentu a přispět k mezinárodnímu multi-GNSS rámci, čímž zlepšilo celkovou globální odolnost.

## Klíčové vlastnosti

- Regionální konstelace se satelity na kvazizenitálních drahách (QZO) a geostacionárních drahách
- Vysílá signály interoperabilní s GPS pro zvýšení viditelnosti satelitů a zlepšení geometrie
- Poskytuje signály satelitního augmentačního systému (SBAS) (L1S, L5S) pro zvýšenou přesnost a integritu
- Nabízí službu Centimeter Level Augmentation Service (CLAS) prostřednictvím signálu L6 pro vysoce přesné aplikace
- Plně integrován do standardů 3GPP A-GNSS pro určování polohy v mobilních sítích
- Umožňuje hybridní multi-GNSS určování polohy kombinující QZSS se systémy GPS, Galileo a BeiDou

## Související pojmy

- [QZS – Quasi-Zenith Satellite](/mobilnisite/slovnik/qzs/)
- [QZST – Quasi-Zenith System Time](/mobilnisite/slovnik/qzst/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [QZSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/qzss/)
