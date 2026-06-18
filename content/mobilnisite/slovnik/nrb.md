---
slug: "nrb"
url: "/mobilnisite/slovnik/nrb/"
type: "slovnik"
title: "NRB – Number of Resource Blocks"
date: 2025-01-01
abbr: "NRB"
fullName: "Number of Resource Blocks"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nrb/"
summary: "NRB udává konfiguraci přenosové šířky pásma v jednotkách zdrojových bloků, což jsou základní stavební kameny fyzické vrstvy LTE a NR. Definuje počet sousedních podnosných přidělených pro přenos, což p"
---

NRB je počet sousedních zdrojových bloků přidělených pro přenos, což přímo určuje šířku pásma kanálu a datovou kapacitu pro nosnou v LTE a NR.

## Popis

Počet zdrojových bloků (NRB) je základní parametr v LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) i 5G NR, který definuje konfiguraci přenosové šířky pásma nosné. Zdrojový blok ([RB](/mobilnisite/slovnik/rb/)) je nejmenší jednotka zdrojů, kterou lze přidělit uživateli pro interval přenosu času. Ve frekvenční oblasti se jeden zdrojový blok skládá z 12 po sobě jdoucích podnosných. NRB tedy určuje, kolik těchto bloků o 12 podnosných je souvisle přiděleno v rámci šířky pásma kanálu nosné. Hodnota NRB přímo souvisí se šířkou kanálu; například v LTE 10 MHz kanálu typicky odpovídá NRB = 50. Vztah je definován ve specifikacích pomocí tabulek mapujících šířky kanálů (např. 1,4, 3, 5, 10, 15, 20 MHz pro LTE) na odpovídající hodnoty NRB, přičemž se zohledňují potřebné ochranná pásma na okrajích přiděleného spektra.

Z architektonického hlediska je NRB klíčovým vstupem pro mřížku zdrojů fyzické vrstvy. Mřížka zdrojů je časově-frekvenční matice, kde frekvenční dimenze je definována jako NRB * 12 podnosných. Do této mřížky se mapují fyzické kanály a signály, jako je Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)), Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)) a referenční signály. Plánovač základnové stanice používá NRB jako omezení a dynamicky přiděluje podmnožiny těchto celkových zdrojových bloků různým uživatelům na základě stavu jejich kanálu a požadavků na kvalitu služeb. Celkový počet dostupných zdrojových bloků (NRB) zásadně omezuje špičkovou datovou rychlost, kterou nosná může podporovat, protože více RB znamená více frekvenčních zdrojů dostupných pro přenos dat.

V 5G NR zůstává koncept NRB ústřední, ale je rozšířen o větší flexibilitu. Zatímco NR zdrojový blok také sestává z 12 podnosných, rozteč podnosných ([SCS](/mobilnisite/slovnik/scs/)) se může lišit (15, 30, 60, 120, 240 kHz). Konfigurace přenosové šířky pásma NRB je definována pro každou SCS a šířku kanálu. NR navíc zavádí koncept částí šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)), kde může být UE nakonfigurováno s podmnožinou celkového NRB nosné. To umožňuje úsporu energie a podporu zařízení s různými možnostmi šířky pásma. NRB tedy funguje na dvou úrovních: jako celková konfigurace šířky pásma nosné a jako konfigurace pro každý BWP. Specifikace (např. 38.101, 38.104) poskytují rozsáhlé tabulky definující podporované hodnoty NRB pro každou kombinaci frekvenčního pásma, SCS a šířky kanálu, což zajišťuje globální interoperabilitu.

## K čemu slouží

Parametr NRB existuje proto, aby poskytl standardizovaný, škálovatelný a implementačně přívětivý způsob definice a konfigurace přenosové šířky pásma buňkové nosné. Bez takové standardizace by bylo definování šířky pásma v syrových hertzech (Hz) nejednoznačné kvůli potřebě ochranných pásem a diskrétní povaze [OFDM](/mobilnisite/slovnik/ofdm/) podnosných. NRB abstrahuje šířku pásma do diskrétních bloků zdrojů (12 podnosných), což dokonale odpovídá mechanismům plánování a přidělování zdrojů [OFDMA](/mobilnisite/slovnik/ofdma/) (používaného v downlinku) a SC-FDMA (používaného v uplinku LTE). Tím se řeší problém efektivního rozdělení spojitého spektra na spravovatelné, přidělitelné jednotky pro více uživatelů.

Historický kontext vychází z návrhu LTE v 3GPP Release 8, které přijalo OFDMA a potřebovalo základní jednotku zdrojů. Zdrojový blok a následně NRB byly definovány jako tato jednotka. Poskytly společný jazyk pro specifikaci RF požadavků UE (jako jsou šířky kanálů pro testování), definici struktur fyzických kanálů a implementaci plánovacích algoritmů. Jak se sítě vyvíjely k 5G NR, princip zůstal klíčový, ale vyžadoval přizpůsobení. NR potřebovalo podporovat mnohem širší rozsah frekvencí a šířek pásem, od úzkopásmového IoT po ultraširokopásmové milimetrové kanály. Rámec NRB byl rozšířen o nové tabulky a pravidla, aby pokryl tyto případy, zachovávaje princip zpětné kompatibility a zároveň umožňující pokročilou flexibilitu. Řeší tak omezení jednotné definice šířky pásma pro všechny případy a umožňuje optimalizaci systému pro různé případy užití od massive IoT po enhanced mobile broadband.

## Klíčové vlastnosti

- Definuje přenosovou šířku pásma v jednotkách zdrojových bloků (každý o 12 podnosných).
- Přímo se mapuje na standardizované šířky kanálů (např. 5 MHz, 20 MHz, 100 MHz).
- Základní pro vytvoření časově-frekvenční mřížky zdrojů pro plánování.
- V NR je definován pro každou rozteč podnosných a frekvenční pásmo.
- Používá se k specifikaci RF požadavků UE a základnových stanic v konformních testech.
- Tvoří základ konfigurace částí šířky pásma (BWP) v 5G NR.

## Definující specifikace

- **TS 25.116** (Rel-19) — LCR TDD Repeater RF Characteristics
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- **TS 32.828** (Rel-10) — Study on 3GPP-TMF NRM/SID Alignment
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [NRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrb/)
