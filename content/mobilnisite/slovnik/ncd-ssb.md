---
slug: "ncd-ssb"
url: "/mobilnisite/slovnik/ncd-ssb/"
type: "slovnik"
title: "NCD-SSB – Non Cell Defining SSB"
date: 2025-01-01
abbr: "NCD-SSB"
fullName: "Non Cell Defining SSB"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ncd-ssb/"
summary: "Blok synchronizačních signálů (SSB) vysílaný buňkou, který není použit pro počáteční výběr a napojení (camping) na buňku. Poskytuje dodatečné příležitosti pro měření pro správu paprsků, mobilitu a spr"
---

NCD-SSB je blok synchronizačních signálů (Synchronization Signal Block), který není použit pro počáteční přístup k buňce, ale poskytuje dodatečné signály pro správu paprsků, mobilitu a správu rádiových zdrojů za účelem zlepšení pokrytí v sítích NR.

## Popis

NCD-SSB (Non Cell Defining SSB) je koncept zavedený v 5G New Radio (NR), jehož cílem je oddělit základní funkce definující buňku od dodatečných přenosů synchronizačních a referenčních signálů. V NR je SSB základní blok zahrnující primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)), sekundární synchronizační signál ([SSS](/mobilnisite/slovnik/sss/)), fyzický kanál pro vysílání ([PBCH](/mobilnisite/slovnik/pbch/)) a přidružený [DM-RS](/mobilnisite/slovnik/dm-rs/). Tradičně buňka vysílá alespoň jeden SSB, označovaný jako [CD-SSB](/mobilnisite/slovnik/cd-ssb/) (Cell Defining SSB), který nese základní systémové informace pro počáteční přístup, včetně fyzické identifikace buňky ([PCI](/mobilnisite/slovnik/pci/)) a hlavního informačního bloku ([MIB](/mobilnisite/slovnik/mib/)). UE používá CD-SSB pro vyhledání buňky, časovou/frekvenční synchronizaci a získání minimálních systémových informací potřebných k napojení na buňku.

NCD-SSB je dodatečný SSB vysílaný stejnou buňkou (sdílející stejnou PCI), který však není použit pro tyto počáteční procedury definující buňku. Jeho hlavním účelem je poskytnout dodatečné paprskově specifické referenční signály pro měření. V NR, zejména ve frekvenčním rozsahu 2 (FR2 – mmWave), je beamforming klíčový kvůli vysokému útlumu na dráze. Buňka typicky využívá více úzkých paprsků k pokrytí své servisní oblasti. CD-SSB může být vysílán na širokém paprsku nebo na specifické sadě paprsků pro počáteční přístup. NCD-SSB mohou být vysílány na jiných paprskech a poskytují tak podrobnější měřicí body. UE může měřit na těchto NCD-SSB a hlásit síťi výsledky měření specifické pro paprsek (např. [SS-RSRP](/mobilnisite/slovnik/ss-rsrp/), SS-SINR). To umožňuje pokročilé funkce správy rádiových zdrojů (RRM), jako je správa paprsků, obnova při selhání paprsku a lépe informovaná rozhodnutí o předání spojení.

Z pohledu specifikace síť konfiguruje přítomnost, periodicitu a časové/frekvenční zdroje NCD-SSB prostřednictvím dedikované signalizace RRC (např. v ServingCellConfigCommon SIB nebo v dedikovaných měřicích konfiguracích). UE je informována, že se jedná o NCD-SSB, a tudíž ví, že je nemá používat pro získání MIB nebo pro určení identity buňky. Existují čistě jako měřicí zdroje. Toto oddělení umožňuje větší flexibilitu; například síť může dynamicky aktualizovat konfiguraci beamforming pro NCD-SSB bez ovlivnění základní identity buňky a procesu počátečního přístupu ukotveného k CD-SSB. Konfigurační detaily a procedury pro NCD-SSB jsou specifikovány v TS 38.331 (RRC), TS 38.213 (procedury fyzické vrstvy) a požadavky na měření v TS 38.133.

## K čemu slouží

NCD-SSB byl zaveden ve vydání 17 (Release 17) k řešení omezení rigidního rámce SSB v silně beamformovaných nasazeních 5G NR, zejména pro spektrum mmWave. V dřívějších vydáních byly všechny SSB v podstatě 'definující buňku'. Pokud síť chtěla poskytnout více měřicích vzorků nebo paprsků pro RRM, musela zvýšit počet shluků SSB (bursts), což mohlo spotřebovat značné zdroje a zkomplikovat proceduru počátečního přístupu. Existovala potřeba oddělit 'kotvící' signály vyžadované pro základní provoz buňky od doplňkových signálů používaných pro optimalizaci.

Klíčovým řešeným problémem je zlepšení výkonu mobility a správy paprsků. V hustých městských nebo vnitřních scénářích s mnoha odrazy může pouze několik paprsků SSB (CD-SSB) neposkytovat dostatečnou podrobnost měření pro spolehlivé sledování paprsků a rychlá předání spojení. NCD-SSB umožňují síti nasadit mnoho dodatečných měřicích paprsků bez zatížení procesu počátečního vyhledávání buňky. To vede k přesnějším informacím o stavu kanálu, lepšímu zarovnání paprsků, snížení selhání rádiového spoje a v konečném důsledku k vyšší propustnosti pro uživatele a robustnosti mobility. Také zajišťuje budoucí odolnost návrhu NR pro pokročilé případy užití, jako je integrovaný přístup a přenos (IAB) a dynamické sdílení spektra, kde jsou flexibilní zdroje referenčních signálů prvořadé.

## Klíčové vlastnosti

- Vysílán buňkou, ale nepoužit pro počáteční vyhledávání buňky nebo získání MIB
- Sdílí stejnou fyzickou identifikaci buňky (PCI) jako CD-SSB buňky
- Konfigurován prostřednictvím signalizace RRC (např. v ServingCellConfig)
- Poskytuje dodatečné paprskově specifické měřicí zdroje pro UE
- Zlepšuje měření RRM pro správu paprsků, mobilitu a monitorování rádiového spoje
- Umožňuje flexibilní přidělení časových/frekvenčních zdrojů nezávisle na omezeních CD-SSB

## Související pojmy

- [CD-SSB – Cell-Defining Synchronization Signal Block](/mobilnisite/slovnik/cd-ssb/)
- [SS-RSRP – Synchronization Signal based Reference Signal Received Power](/mobilnisite/slovnik/ss-rsrp/)
- [PCI – Physical Cell Identity](/mobilnisite/slovnik/pci/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [NCD-SSB na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncd-ssb/)
