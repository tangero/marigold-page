---
slug: "fr2-ntn"
url: "/mobilnisite/slovnik/fr2-ntn/"
type: "slovnik"
title: "FR2-NTN – Frequency Range 2 for Non-Terrestrial Networks"
date: 2025-01-01
abbr: "FR2-NTN"
fullName: "Frequency Range 2 for Non-Terrestrial Networks"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fr2-ntn/"
summary: "FR2-NTN definuje použití pásem milimetrových vln (24,25 GHz až 71,0 GHz) pro satelitní a další komponenty nesatelitních sítí (NTN) v 5G NR. Umožňuje vysokokapacitní spoje s nízkou latencí pro přímé sa"
---

FR2-NTN označuje použití pásem milimetrových vln v rozsahu 24,25 GHz až 71,0 GHz pro satelitní a další komponenty nesatelitních (neboli pozemských) sítí (NTN) v systému 5G NR.

## Popis

FR2-NTN je technická specifikace v rámci 3GPP, která přizpůsobuje stávající rozsah frekvencí 2 (FR2) pro 5G New Radio (NR), známý také jako spektrum milimetrových vln (mmWave), pro provoz v nesatelitních sítích ([NTN](/mobilnisite/slovnik/ntn/)). NTN zahrnují komunikační platformy, jako jsou geostacionární ([GEO](/mobilnisite/slovnik/geo/)) a nízkoorbitální ([LEO](/mobilnisite/slovnik/leo/)) satelity, stanice na velké nadmořské výšce ([HAPS](/mobilnisite/slovnik/haps/)) a sítě typu vzduch-země. Základním architektonickím principem je úprava fyzické vrstvy NR a protokolů vyšších vrstev definovaných pro pozemské sítě, aby se kompenzovaly jedinečné výzvy prostředí NTN, především výrazně větší šířicí zpoždění, značné Dopplerovy posuny způsobené pohybem satelitu a rozsáhlé pokrytí buněk. Mezi klíčové technické komponenty specifikované pro FR2-NTN patří vylepšené mechanismy časového předstihu pro zvládání dlouhé doby oběhu, pokročilé algoritmy předkompenzace a sledování Dopplerova posunu jak v uživatelském zařízení (UE), tak v satelitu/bráně, a úpravy procedur náhodného přístupu, které zohledňují zpoždění. Rozhraní pro rádiové přenosy funguje v pásmech FR2, jak je definováno v TS 38.101-5, která specifikuje konkrétní frekvenční pásma, šířky kanálů a požadavky na výkon přenosu vhodné pro satelitní spoje. Úloha FR2-NTN v síti spočívá v poskytování standardizovaného vysokokapacitního bezdrátového přenosového spoje (backhaul) pro brány NTN (propojující satelit s pozemskou páteřní sítí) a v některých scénářích nasazení také v umožnění přímého vysokorychlostního přístupu k uživatelským zařízením, čímž doplňuje pozemské pokrytí 5G v odlehlých, námořních a leteckých oblastech.

## K čemu slouží

FR2-NTN bylo vytvořeno za účelem integrace vysokokapacitních satelitních spojů do ekosystému 5G, což řeší omezení pozemských sítí, které nejsou schopné zajistit všudypřítomné globální pokrytí. Před standardizací v 3GPP fungovala satelitní komunikace v proprietárních izolovaných řešeních, což bránilo bezproblémové kontinuitě služeb s pozemskými mobilními sítěmi. Motivací je rostoucí poptávka po globální konektivitě pro aplikace IoT, podnikové, vládní a spotřebitelské, kde je pozemská infrastruktura ekonomicky nebo fyzicky nepraktická. FR2 s velkou dostupnou šířkou pásma je nezbytné pro dosažení vícejigabitových přenosových rychlostí předpokládaných pro 5G, a to i prostřednictvím satelitu. FR2-NTN standardizuje způsob využití tohoto spektra pro [NTN](/mobilnisite/slovnik/ntn/), řeší problémy interoperability mezi satelitními operátory a dodavateli zařízení pro pozemské sítě a umožňuje výrobcům zařízení vyrábět jednotná zařízení, která se mohou připojit k pozemským i satelitním sítím pomocí stejné rádiové technologie.

## Klíčové vlastnosti

- Provoz v pásmech milimetrových vln (24,25–71,0 GHz) pro NTN
- Podpora jak transparentních ('bent-pipe'), tak regenerativních (s palubním zpracováním) satelitních přenosových subsystémů
- Vylepšené mechanismy časového předstihu pro velká šířicí zpoždění (až stovky milisekund)
- Pokročilé algoritmy pro odhad a kompenzaci Dopplerova posunu
- Přizpůsobené postupy fyzické vrstvy (synchronizace, náhodný přístup, HARQ) pro satelitní kanály
- Definované požadavky na výkon (RF, demodulaci) pro UE a síťové vybavení v řadě specifikací TS 38.1xx

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data

---

📖 **Anglický originál a plná specifikace:** [FR2-NTN na 3GPP Explorer](https://3gpp-explorer.com/glossary/fr2-ntn/)
