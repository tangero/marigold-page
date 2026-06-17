---
slug: "glonass"
url: "/mobilnisite/slovnik/glonass/"
type: "slovnik"
title: "GLONASS – GLObal'naya NAvigatsionnaya Sputnikovaya Sistema (Global Navigation Satellite System)"
date: 2025-01-01
abbr: "GLONASS"
fullName: "GLObal'naya NAvigatsionnaya Sputnikovaya Sistema (Global Navigation Satellite System)"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/glonass/"
summary: "GLONASS je globální satelitní navigační systém provozovaný Ruskem, který poskytuje služby určování polohy, navigace a času (PNT). Ve standardech 3GPP je podporován jako globální navigační satelitní sy"
---

GLONASS je globální navigační satelitní systém provozovaný Ruskem, který poskytuje služby určování polohy, navigace a času (PNT) a je podporován ve standardech 3GPP pro lokalizační služby mobilních zařízení.

## Popis

GLONASS je satelitní navigační systém na bázi vesmírných družic, který tvoří jeden z hlavních globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)) vedle amerického [GPS](/mobilnisite/slovnik/gps/), evropského Galilea a čínského BeiDou. V rámci ekosystému 3GPP specifikace definují, jak může uživatelské zařízení (UE) využívat signály ze satelitů GLONASS (stejně jako z jiných konstelací GNSS) k výpočtu vlastní polohy. Tato schopnost je klíčovým prvkem pro lokalizační služby ([LCS](/mobilnisite/slovnik/lcs/)) v 3GPP. Systém funguje tak, že vysílá přesné časové signály z konstelace satelitů na střední oběžné dráze Země. GNSS přijímač v UE měří časové zpoždění signálů přijímaných z více viditelných satelitů; se znalostí oběžných drah satelitů (efemeridní data) a času vyslání signálu může přijímač vypočítat svou vzdálenost od každého satelitu a pomocí trilaterace určit vlastní polohu.

Integrace GLONASS do standardů 3GPP zahrnuje specifikace napříč více vrstvami. Specifikace rádiového přístupového síťového rozhraní (např. 25.331 pro UTRAN, 36.331 pro [E-UTRAN](/mobilnisite/slovnik/e-utran/), 38.331 pro NR) definují signalizační protokoly pro asistovaný GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), kde síť může poskytnout uživatelskému zařízení asistenční data (jako je almanach a efemeridy satelitů), aby se výrazně urychlil čas do prvního určení polohy (TTFF) a zlepšila se citlivost. Specifikace jádra sítě pokrývají lokalizační protokoly a architekturu. Dále požadavky na výkon (např. v 25.171, 36.171, 38.171) definují minimální úrovně výkonu pro přijímače UE podporující GLONASS, včetně citlivosti, přesnosti a metriky času do prvního určení polohy za různých podmínek.

Z pohledu síťové architektury je GNSS schopnost UE, včetně podpory GLONASS, hlášena síti. Funkce správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) v 5GC nebo rozšířené centrum obsluhy mobilní polohy ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v EPS pak může tuto schopnost využít při rozhodování o metodě určení polohy pro lokalizační požadavek. Použití více konstelací GNSS, technika známá jako multi-GNSS, výrazně zlepšuje výkon. Zvyšuje počet viditelných satelitů, což je klíčové v městských kaňonech nebo jiných náročných prostředích, a vede k lepší přesnosti, dostupnosti a integritě určení polohy. Podpora GLONASS v 3GPP zajišťuje, že UE mohou využívat tuto dodatečnou konstelaci pro robustní lokalizační služby po celém světě.

## K čemu slouží

Začlenění podpory GLONASS do 3GPP bylo motivováno rostoucí poptávkou po přesných a spolehlivých službách založených na poloze a regulatorními požadavky, jako je Enhanced 911 (E911). Spoléhání se pouze na americký systém [GPS](/mobilnisite/slovnik/gps/) mělo svá omezení, včetně možných jednotných bodů selhání, regionálních zranitelností signálu a někdy nedostatečné viditelnosti satelitů pro rychlé a přesné určení polohy. Začlenění GLONASS jako alternativní a doplňkové konstelace GNSS tyto nedostatky příře řeší zvýšením počtu dostupných navigačních satelitů.

Hlavní motivací bylo zlepšení výkonu určování polohy v mobilních sítích. Díky podpoře více konstelací může uživatelské zařízení (UE) dosáhnout určení polohy rychleji (zkrácený čas do prvního určení polohy – TTFF), s vyšší přesností a s větší spolehlivostí, zejména v hustě zastavěných městských oblastech, kde budovy mohou blokovat signály z některých satelitů. Tento přístup multi-GNSS zajistil budoucí kompatibilitu standardů 3GPP a umožnil integraci dalších systémů, jako jsou Galileo a BeiDou, jak se staly operačními. Rovněž zohlednil potřeby globálního trhu a zajistil, že mobilní zařízení mohou poskytovat efektivní lokalizační služby po celém světě bez ohledu na regionální preference nebo operační stav jakéhokoli jednotlivého satelitního systému.

## Klíčové vlastnosti

- Poskytuje globální signály pro určování polohy, navigaci a čas (PNT) jako součást rodiny GNSS.
- Umožňuje provoz Assisted-GLONASS (A-GLONASS), při kterém sítě poskytují asistenční data pro zlepšení výkonu UE.
- Zvyšuje přesnost, dostupnost a integritu určování polohy prostřednictvím multi-GNSS provozu s GPS a dalšími systémy.
- Definován ve specifikacích 3GPP pro výkon, konkrétně pro citlivost, přesnost a čas do prvního určení polohy (TTFF) přijímače UE.
- Podporován napříč rádiovými technologiemi 3GPP (UTRAN, E-UTRAN, NG-RAN) pro integrované lokalizační služby.
- Využívá strukturu signálu FDMA a CDMA (modernizované satelity), která se liší od struktury GPS založené pouze na CDMA.

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [GPS – Global Positioning System](/mobilnisite/slovnik/gps/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [GLONASS na 3GPP Explorer](https://3gpp-explorer.com/glossary/glonass/)
