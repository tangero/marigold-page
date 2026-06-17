---
slug: "ext"
url: "/mobilnisite/slovnik/ext/"
type: "slovnik"
title: "EXT – Extension payload"
date: 2025-01-01
abbr: "EXT"
fullName: "Extension payload"
category: "Protocol"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/ext/"
summary: "Rozšiřující datová část (Extension payload), protokolová datová jednotka používaná ve specifikacích 3GPP pro přenos volitelných nebo doplňujících informací v rámci struktury zprávy nebo paketu. Poskyt"
---

EXT je protokolová datová jednotka používaná ve specifikacích 3GPP pro přenos volitelných nebo doplňujících informací v rámci zprávy, která poskytuje flexibilní mechanismus pro budoucí vylepšení a rozšíření specifická pro výrobce.

## Popis

Rozšiřující datová část (EXT) je základní konstrukce v různých specifikacích protokolů 3GPP, navržená pro přenos doplňujících informací, které nejsou součástí základní povinné struktury zprávy. Slouží jako kontejner nebo přívěsek, který může být připojen k protokolové datové jednotce (PDU). Přítomnost rozšiřující datové části je typicky indikována specifickým příznakem nebo polem délky v hlavičce primární PDU. Vnitřní struktura EXT je definována formátem TLV (Type-Length-Value) nebo podobným, kde pole typu identifikuje povahu rozšíření, pole délky určuje velikost pole hodnoty a pole hodnoty obsahuje vlastní data rozšíření. Tento návrh umožňuje zařadit více různých rozšíření postupně za sebou. Specifikace jako TS 26.260 (Packet-switched Streaming Service) a TS 33.246 (3G Security; Wireless Local Area Network (WLAN) interworking security) definují použití EXT pro přenos dodatečných parametrů popisu relace nebo bezpečnostních informací. Na přijímací straně, pokud je typ rozšíření rozpoznán, jsou data zpracována; pokud ne, mohou být bezpečně ignorována, což je klíčové pro interoperabilitu. Tento mechanismus je nedílnou součástí rozšiřitelnosti protokolů 3GPP, umožňuje přidávat nové funkce v pozdějších vydáních při zachování kompatibility se staršími zařízeními, která mohou rozumět pouze základnímu protokolu.

## K čemu slouží

Rozšiřující datová část byla vytvořena k řešení inherentního problému vývoje protokolů v ekosystému s více výrobci a více vydáními. Rané komunikační protokoly často měly pevné formáty; přidání nových parametrů vyžadovalo vytvoření nové verze protokolu, což mohlo narušit interoperabilitu s nasazenými zařízeními. Konstrukce EXT poskytuje standardizovaný, budoucím verzím kompatibilní způsob zahrnutí nových informací. Umožňuje standardizačním orgánům definovat nové schopnosti v pozdějších vydáních 3GPP a výrobcům zahrnout proprietární informace pro optimalizaci sítě nebo specifické funkce, vše v rámci stejného protokolového rámce. Tento návrh je klíčový pro dlouhodobý životní cyklus telekomunikačních sítí, kde musí zařízení různých generací koexistovat. Například ve streamovacích službách (TS 26.260) umožňuje signalizovat nové mediální formáty nebo parametry doručení. V bezpečnostních protokolech (TS 33.246) může přenášet nové prvky ověřování nebo data politik. Mechanismus EXT tedy zajišťuje protokolům odolnost vůči budoucím změnám, snižuje potřebu zcela nových typů zpráv a usnadňuje plynulé upgrady sítí a zavádění funkcí.

## Klíčové vlastnosti

- Flexibilní kódovací struktura TLV (Type-Length-Value) nebo podobná
- Volitelná přítomnost indikovaná příznaky v hlavičce primární PDU
- Umožňuje zpětnou i budoucí kompatibilitu
- Podporuje více nezávislých rozšíření v rámci jedné datové části
- Umožňuje rozšíření specifická pro výrobce (proprietární)
- Definována v základních specifikacích protokolů napříč různými doménami (např. média, bezpečnost)

## Definující specifikace

- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 33.246** (Rel-19) — MBMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [EXT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ext/)
