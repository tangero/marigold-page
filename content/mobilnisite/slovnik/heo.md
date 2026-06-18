---
slug: "heo"
url: "/mobilnisite/slovnik/heo/"
type: "slovnik"
title: "HEO – Highly-Eccentric Orbiting satellites"
date: 2025-01-01
abbr: "HEO"
fullName: "Highly-Eccentric Orbiting satellites"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/heo/"
summary: "HEO označuje satelity na vysoce eliptických drahách s výraznými změnami výšky, což umožňuje prodloužené pokrytí oblastí ve vysokých zeměpisných šířkách. V rámci 3GPP jsou studovány pro neterestriální"
---

HEO je typ satelitu na vysoce eliptické oběžné dráze, který je studován v rámci 3GPP pro neterestriální sítě (NTN) za účelem poskytnutí rozšířeného pokrytí vysokých zeměpisných šířek a odlehlých oblastí.

## Popis

Satelity na vysoce excentrických drahách (HEO) jsou kategorií kosmických lodí operujících na eliptických drahách s vysokou excentricitou, typicky charakterizovaných nízkým perigeem (nejbližší bod k Zemi) a velmi vysokým apogeem (nejvzdálenější bod). Tato geometrie dráhy vede k tomu, že satelit tráví prodlouženou dobu poblíž svého apogea, kde je jeho rychlost nejnižší, čímž efektivně vytváří 'kvazi-geostacionární' dojem nad konkrétní oblastí, což je zvláště výhodné pro oblasti vysokých zeměpisných šířek. V rámci 3GPP jsou systémy HEO analyzovány jako součást neterestriálních sítí ([NTN](/mobilnisite/slovnik/ntn/)) pro rozšíření služeb 5G New Radio (NR) a LTE. Architektura zahrnuje satelit fungující jako přenosový uzel nebo základnová stanice (gNB v NR), která propojuje uživatelské zařízení (UE) na zemi s pozemní bránovou stanicí, jež následně komunikuje s 5G Core sítí. Klíčové technické aspekty zahrnují správu dlouhých prodlev šíření (v rozmezí od desítek po více než sto milisekund), významných Dopplerových posuvů způsobených vysokou relativní rychlostí satelitu během části oběžné dráhy a potřebu velkých pokrytí paprsků nebo řiditelných úzkých paprsků pro udržení pokrytí během pohybu satelitu. Radiové rozhraní musí být přizpůsobeno pro zvládnutí těchto výzev, což zahrnuje vylepšení synchronizace, časového předstihu a procedur předávání spojení. Konstelace HEO jsou koncipovány pro provoz v různých kmitočtových pásmech včetně pásem L, S, C a Ka, jak je definováno ve studiích 3GPP pro satelitní rádiové rozhraní a scénáře nasazení. Jejich rolí je poskytovat plynulou kontinuitu služeb, páteřní konektivitu a služby přímo do zařízení v oblastech, kde je terestrická infrastruktura ekonomicky neproveditelná nebo fyzicky nemožná k vybudování, jako jsou polární oblasti, oceány a letecké trasy. Integrace se systémem 5G vyžaduje úpravy funkcí core sítě pro správu mobility, správu relací a řízení QoS s ohledem na jedinečné charakteristiky satelitního spoje.

## K čemu slouží

Primárním účelem standardizace podpory satelitů HEO v 3GPP je umožnit globální a všudypřítomné pokrytí 5G, což je klíčový cíl IMT-2020. Tradiční terestrické sítě mají omezený dosah, takže rozsáhlé geografické oblasti včetně námořních, leteckých a polárních regionů zůstávají bez konektivity. Satelity [HO](/mobilnisite/slovnik/ho/) řeší tuto mezeru v pokrytí využitím své jedinečné orbitální mechaniky k poskytnutí trvalého pokrytí vysokých zeměpisných šířek, se kterým satelity na geostacionární dráze ([GEO](/mobilnisite/slovnik/geo/)) často zápasí kvůli své rovníkové pozici a nízkým elevačním úhlům ve vysokých šířkách. Historicky satelitní komunikační systémy fungovaly odděleně od celulárních standardů, což vedlo k fragmentovaným službám a složitým uživatelským zařízením. Integrace do 3GPP, počínaje studijními položkami Release 14, si klade za cíl sjednotit terestrické a neterestriální sítě v rámci společného rámce, což umožní úspory z rozsahu, snížení složitosti zařízení a bezproblémový uživatelský zážitek. Tím se řeší omezení předchozích proprietárních satelitních systémů, které nebyly nativně integrovány s celulárními core sítěmi a bránily funkcím jako mobilita, síťové segmenty (network slicing) a konzistentní QoS. Motivací je rostoucí poptávka po konektivitě všude, podpora Internetu věcí (IoT) v odlehlých oblastech a vládní požadavky na komunikaci pro mimořádné události a veřejnou bezpečnost. Satelity HEO se svou výhodnou dobou setrvání nad vysokými šířkami představují komplementární řešení k mega-konstelacím na nízké oběžné dráze ([LEO](/mobilnisite/slovnik/leo/)) a systémům GEO, čímž vytvářejí heterogenní ekosystém [NTN](/mobilnisite/slovnik/ntn/).

## Klíčové vlastnosti

- Eliptické dráhy s vysokou excentricitou umožňující prodlouženou dobu setrvání nad cílovými oblastmi vysokých zeměpisných šířek
- Integrace jako uzel rádiové přístupové sítě (RAN) v rámci architektury 3GPP 5G systému
- Podpora jak transparentních (bent-pipe), tak regenerativních (s palubním zpracováním) architektur užitečného zatížení
- Adaptace fyzické vrstvy NR a protokolů pro zvládnutí dlouhé prodlevy a vysokého Dopplerova posuvu
- Umožňuje kontinuitu služeb a mobilitu mezi terestrickými a neterestriálními sítěmi
- Poskytuje pokrytí pro širokopásmové služby, hromadný IoT a služby klíčové pro misi v odlehlých oblastech

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)
- [LEO – Low-Earth Orbiting satellites](/mobilnisite/slovnik/leo/)
- [GEO – Geostationary satellite Earth Orbit](/mobilnisite/slovnik/geo/)

## Definující specifikace

- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 28.874** (Rel-19) — Study on Management Aspects of NTN Phase 2
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks
- **TR 38.913** (Rel-19) — Next Gen Access Tech Scenarios & Requirements

---

📖 **Anglický originál a plná specifikace:** [HEO na 3GPP Explorer](https://3gpp-explorer.com/glossary/heo/)
