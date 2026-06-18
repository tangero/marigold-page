---
slug: "ofdm"
url: "/mobilnisite/slovnik/ofdm/"
type: "slovnik"
title: "OFDM – Orthogonal Frequency Division Multiplexing"
date: 2025-01-01
abbr: "OFDM"
fullName: "Orthogonal Frequency Division Multiplexing"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ofdm/"
summary: "Orthogonal Frequency Division Multiplexing (OFDM) je digitální vícekanálový modulační systém, který rozděluje vysokorychlostní datový tok na více paralelních podnosných s nižší rychlostí. Je to základ"
---

OFDM je digitální vícekanálový modulační systém, který rozděluje vysokorychlostní datový tok na více paralelních podnosných, čímž tvoří základní přenos fyzické vrstvy pro downlink 4G a 5G díky své odolnosti vůči vícecestnému útlumu.

## Popis

Orthogonal Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) (OFDM) je sofistikovaná modulační a multiplexní technika, která tvoří páteř moderních širokopásmových bezdrátových systémů, jako jsou LTE a NR. V jádru OFDM přeměňuje frekvenčně selektivní širokopásmový kanál na soubor mnoha úzkopásmových podnosných s plochým útlumem. Vysokorychlostní sériový datový tok je rozdělen na četné paralelní toky s nižší rychlostí, z nichž každý moduluje samostatnou podnosnou. Kritickou inovací je ortogonalita těchto podnosných: jsou rozloženy přesně na reciproké hodnotě doby trvání symbolu, což zajišťuje, že ve vrcholu průběhu jedné podnosné mají všechny ostatní podnosné nulové průchody. Tato ortogonalita umožňuje podnosným se překrývat ve frekvenční oblasti, aniž by způsobovaly mezikanálové rušení ([ICI](/mobilnisite/slovnik/ici/)), což vede k velmi vysoké spektrální účinnosti.

Praktická implementace OFDM se opírá o inverzní rychlou Fourierovu transformaci ([IFFT](/mobilnisite/slovnik/ifft/)) na straně vysílače a rychlou Fourierovu transformaci ([FFT](/mobilnisite/slovnik/fft/)) na straně přijímače. Vysílač mapuje paralelní datové symboly na podnosné a provede IFFT pro vygenerování časového OFDM symbolu. Ke každému symbolu je poté připojen cyklický prefix ([CP](/mobilnisite/slovnik/cp/)). CP je kopie poslední části OFDM symbolu připojená na jeho začátek. Tento ochranný interval zmírňuje mezi symbolové rušení ([ISI](/mobilnisite/slovnik/isi/)) způsobené vícecestným šířením, pokud je zpožděné rozprostření kanálu kratší než doba trvání CP. Na přijímači se po odstranění CP operací FFT převede signál zpět do frekvenční oblasti, kde jednoduchá jednoúhozová ekvalizace na každé podnosné může kompenzovat vlivy kanálu, což výrazně zjednodušuje návrh přijímače ve srovnání s jednokanálovými systémy v širokopásmových kanálech.

V systémech 3GPP jsou parametry OFDM, jako je rozestup podnosných a doba trvání symbolu, pečlivě voleny. Pro LTE byl přijat pevný rozestup podnosných 15 kHz. 5G NR zavedla flexibilní numerologii, podporující více rozestupů podnosných (např. 15, 30, 60, 120 kHz) škálovaných mocninami dvou, což umožňuje optimalizaci pro různá frekvenční pásma a případy použití. Odolnost OFDM vůči vícecestnému šíření, jeho efektivní využití spektra a kompatibilita s pokročilými anténními technikami, jako je [MIMO](/mobilnisite/slovnik/mimo/), z něj činí nepostradatelnou technologii pro dosažení vysokých datových rychlostí a spolehlivého připojení požadovaného moderním mobilním širokopásmovým připojením.

## K čemu slouží

OFDM byl přijat 3GPP počínaje LTE (Release 8), aby překonal omezení technologie Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (WCDMA) používané v 3G UMTS. WCDMA, jednokanálová rozprostřená spektrální technologie, se potýkala s vysokým poměrem špičkového k průměrnému výkonu (PAPR) a vyžadovala složité ekvalizéry pro zvládnutí silného mezi symbolového rušení v širokopásmových, vícecestných kanálech. Tyto faktory omezovaly dosažitelné datové rychlosti a spektrální účinnost, zatímco poptávka po mobilních datech exponenciálně rostla.

Primární motivací pro OFDM byla jeho vnitřní odolnost vůči frekvenčně selektivnímu útlumu způsobenému vícecestným šířením. Rozdělením kanálu na úzké podnosné postihne hluboký útlum pouze malou podmnožinu a kódování pro opravu chyb může data snadno obnovit. To odstraňuje potřebu složitých časových ekvalizérů. Dále jeho ortogonalita a efektivní implementace založená na FFT jej činí vysoce škálovatelným pro široké šířky pásma. OFDM také přirozeně vyhovuje plánování ve frekvenční oblasti, což umožňuje síti dynamicky přidělovat nejlepší podnosné různým uživatelům, a pro prostorové multiplexování Multiple Input Multiple Output (MIMO), které je klíčové pro zvýšení kapacity. Jeho přijetí umožnilo skok z rychlostí v Mbps na Gbps a položilo základy pro výkonnostní cíle 4G a 5G.

## Klíčové vlastnosti

- Rozděluje širokopásmový kanál na mnoho ortogonálních, úzkopásmových podnosných pro boj s frekvenčně selektivním útlumem
- Využívá IFFT/FFT pro efektivní generování a příjem vícekanálových signálů
- Používá cyklický prefix (CP) jako ochranný interval k eliminaci mezi symbolového rušení z vícecestného šíření
- Umožňuje jednoduchou jednoúhozovou ekvalizaci na každé podnosné na přijímači
- Poskytuje vysokou spektrální účinnost díky překrývajícím se, ale ortogonálním podnosným
- Tvoří základ pro flexibilní přidělování zdrojů a pokročilé víceanténní (MIMO) techniky

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [SC-FDMA – Single Carrier – Frequency Division Multiple Access](/mobilnisite/slovnik/sc-fdma/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations
- … a dalších 23 specifikací

---

📖 **Anglický originál a plná specifikace:** [OFDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ofdm/)
