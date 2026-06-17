---
slug: "gso"
url: "/mobilnisite/slovnik/gso/"
type: "slovnik"
title: "GSO – Geostationary-Satellite Orbit"
date: 2026-01-01
abbr: "GSO"
fullName: "Geostationary-Satellite Orbit"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gso/"
summary: "Kruhová oběžná dráha přibližně 35 786 km nad zemským rovníkem, kde oběžná perioda družice odpovídá rotaci Země. To umožňuje, aby se družice jevila vůči bodu na zemském povrchu jako stacionární, a posk"
---

GSO (Geostacionární družicová oběžná dráha) je kruhová oběžná dráha přibližně 35 786 km nad zemským rovníkem, kde oběžná perioda družice odpovídá rotaci Země, což jí umožňuje zůstat vůči zemskému povrchu fixní, a tím zajistit nepřetržité pokrytí komunikací v NTN.

## Popis

Geostacionární družicová oběžná dráha (GSO) označuje specifickou vysokou oběžnou dráhu používanou pro telekomunikační družice. Družice na GSO je umístěna ve výšce přibližně 35 786 kilometrů přímo nad zemským rovníkem. V této výšce je oběžná perioda družice přesně 24 hodin, což je synchronní s periodou rotace Země. Následkem toho se družice při pozorování ze země jeví jako stacionární na obloze. Tato vlastnost je klíčová pro zavedení fixního nasměrování pozemních antén, což zjednodušuje návrh pozemních stanic a uživatelských terminálů, protože nemusí sledovat pohyb družice.

V rámci 3GPP jsou od Release 15 družice na GSO definovány jako součást Neterestriálních sítí (NTN). Specifikace 3GPP definují technické parametry pro integraci družic na GSO do 5G NR rádiové přístupové sítě. To zahrnuje definici specifických rádiových charakteristik, jako je velmi velké zpoždění šíření (přibližně 250 ms jednosměrně) a charakteristiky Dopplerova jevu, které jsou u GSO ve srovnání s družicemi na nízké oběžné dráze ([LEO](/mobilnisite/slovnik/leo/)) zanedbatelné díky fixní relativní pozici. Rádiové rozhraní musí být přizpůsobeno pro zvládnutí těchto jedinečných podmínek kanálu.

Systémová architektura pro NTN založená na GSO zahrnuje družici fungující jako rádiový přenosový uzel, nebo v některých scénářích jako základnová stanice (gNB). Družice komunikuje s uživatelskými zařízeními (UE) na servisním spoji a s pozemní bránovou stanicí na přenosovém spoji. Brána je následně připojena k 5G core síti. Mezi klíčové výzvy řešené ve specifikacích patří správa časového předstihu kvůli obrovskému zpoždění, zvládání nespojitého pokrytí (pro regenerativní užitečné zatížení) a procedury mobility přizpůsobené pro buňku, která je z pohledu uživatele virtuálně fixní. Rádiové specifikace (např. 38.101, 38.306) definují kmitočtová pásma, požadavky na UE a aspekty výkonu pro provoz s družicemi na GSO.

## K čemu slouží

Integrace družic na GSO do standardů 3GPP byla motivována potřebou poskytovat bezproblémové globální pokrytí, a to i v odlehlých, námořních a leteckých oblastech, kde je nasazení terestrických sítí ekonomicky nebo fyzicky nepraktické. Tradiční terestrické mobilní sítě mají mezery v pokrytí, které jsou družice jedinečně schopné zaplnit. Družice na GSO se svou fixní stopou pokrývající přibližně třetinu zemského povrchu nabízejí osvědčenou a spolehlivou metodu pro vysílání a komunikaci v širokých oblastech.

Práce 3GPP na NTN, včetně GSO, si klade za cíl sjednotit terestrické a neterestrické sítě v rámci jediné architektury systému 5G. Tím vzniká skutečná globální síť umožňující kontinuitu služeb pro uživatele pohybující se mezi terestrickým a družicovým pokrytím. Také umožňuje nové případy užití, jako jsou rozsáhlé sítě senzorů IoT v odlehlých oblastech, přenosové spoje pro terestrické sítě a komunikace pro sektor dopravy (leteckou, námořní). GSO bylo zahrnuto spolu s oběžnými drahami [LEO](/mobilnisite/slovnik/leo/) a [MEO](/mobilnisite/slovnik/meo/), aby poskytlo řadu řešení vyvažujících plochu pokrytí, latenci a náklady na infrastrukturu, přičemž GSO nabízí výhodu nepřetržitého pokrytí rozsáhlého regionu s malým počtem družic.

## Klíčové vlastnosti

- Výška oběžné dráhy přibližně 35 786 km nad rovníkem
- Družice se jeví jako stacionární vůči bodu na zemském povrchu
- Velmi velké zpoždění šíření (~250 ms jednosměrně) ovlivňující návrh protokolů
- Poskytuje nepřetržité pokrytí široké oblasti (stopu)
- Integrováno do 3GPP jako součást Neterestriálních sítí (NTN)
- Zjednodušený návrh antény UE díky absenci potřeby rychlého sledování družice

## Související pojmy

- [LEO – Low-Earth Orbiting satellites](/mobilnisite/slovnik/leo/)

## Definující specifikace

- **TS 22.887** (Rel-20) — Study on satellite access - Phase 4
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 38.882** (Rel-18) — Technical Report on UE Location Service

---

📖 **Anglický originál a plná specifikace:** [GSO na 3GPP Explorer](https://3gpp-explorer.com/glossary/gso/)
