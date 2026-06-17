---
slug: "igso"
url: "/mobilnisite/slovnik/igso/"
type: "slovnik"
title: "IGSO – Inclined Geosynchronous Satellite Orbit"
date: 2025-01-01
abbr: "IGSO"
fullName: "Inclined Geosynchronous Satellite Orbit"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/igso/"
summary: "Typ geosynchronní oběžné dráhy, kde je orbitální rovina satelitu nakloněná vůči zemskému rovníku. Satelit sleduje pozemní stopu ve tvaru osmičky, což poskytuje lepší pokrytí ve vyšších zeměpisných šíř"
---

IGSO je typ geosynchronní oběžné dráhy s nakloněnou rovinou, která vytváří pozemní stopu ve tvaru osmičky, a poskytuje tak vylepšené pokrytí ve vyšších zeměpisných šířkách pro neterestriální sítě v 3GPP.

## Popis

Nakloněná geosynchronní satelitní oběžná dráha (Inclined Geosynchronous Satellite Orbit – IGSO) je vysoká zemská dráha s orbitální periodou rovnou jednomu siderickému dni (přibližně 23 hodin, 56 minut), která odpovídá rotaci Země, ale má nenulový sklon (typicky mezi 5 a 15 stupni) vůči rovníkové rovině. Na rozdíl od geostacionární dráhy ([GEO](/mobilnisite/slovnik/geo/)), která má nulový sklon a vede k tomu, že se satelit pozemnímu pozorovateli jeví jako nehybný na obloze, satelit na IGSO dráze opisuje na obloze během 24hodinového cyklu obrazec ve tvaru osmičky (analemma). Podélný rozsah této pozemní stopy je řízen excentricitou dráhy a argumentem perigea.

Z pohledu neterestriální sítě (NTN) 3GPP poskytuje satelit na IGSO dráze trvalé pokrytí určité geografické oblasti, nikoli však z pevného bodu na obloze. Pohyb satelitu vůči zemskému povrchu je předvídatelný a periodický. Pro uživatelské zařízení (UE) nebo pozemní stanici to znamená, že se elevace a azimut satelitu v průběhu dne mění. Síť musí tento nepřetržitý pohyb zvládat, což zahrnuje předávání spojení (handover) mezi různými paprsky stejného satelitu a potenciálně i mezi satelity, stejně jako kompenzaci velkých a časově proměnných přenosových zpoždění a Dopplerova posuvu. Užitečné zatížení satelitu funguje jako přenosový uzel nebo základnová stanice (gNB), která přeposílá signály mezi uživatelskými zařízeními (UE) a pozemní bránovou stanicí.

Klíčové technické aspekty IGSO v 3GPP zahrnují velké zpoždění příchodů signálu (v řádu 250–280 ms), které přesahuje možnosti mechanismů časového předstihu (timing advance) v terestriálních sítích a vyžaduje specifické úpravy protokolů (např. v RLC, [HARQ](/mobilnisite/slovnik/harq/)). Významný Dopplerův posuv, který se plynule mění, jak satelit postupuje po své dráze, musí být odhadován a kompenzován jak ze strany UE, tak sítí. Dále se pohybuje stopa buňky (cell footprint) na zemi, což vyžaduje pečlivé řízení paprsků a mobility. IGSO dráhy jsou zvláště cenné pro poskytování pokrytí oblastem středních až vysokých zeměpisných šířek, kde mohou být geostacionární satelity pod velmi nízkým elevačním úhlem nebo i pod horizontem, což činí z IGSO doplňkové řešení ke konstelacím GEO a nízkozemním družicím ([LEO](/mobilnisite/slovnik/leo/)) v hybridní NTN architektuře.

## K čemu slouží

Satelity na IGSO dráze se v rámci 3GPP zvažují pro rozšíření dosahu mobilních sítí do oblastí, kde není terestrická infrastruktura dostupná, nespolehlivá nebo poškozená, jako jsou oceány, odlehlé pevniny nebo při obnově po katastrofách. Čistě geostacionární ([GEO](/mobilnisite/slovnik/geo/)) satelity mají zásadní omezení: mohou efektivně pokrývat pouze oblast zhruba mezi 70. stupněm jižní a severní šířky a jejich síla signálu na vyšších zeměpisných šířkách klesá kvůli nízkým elevačním úhlům. IGSO dráhy byly zavedeny do repertoáru satelitní komunikace, aby tuto mezeru v pokrytí zaplnily.

Motivací pro standardizaci podpory IGSO v práci 3GPP na NTN (od Release 15 dále) je vytvoření jednotného rámce, který podporuje všechny relevantní typy satelitních drah. IGSO představuje výhodný kompromis: nabízí delší dobu setrvání nad oblastí než rychle se pohybující [LEO](/mobilnisite/slovnik/leo/) satelity, čímž snižuje frekvenci předávání spojení, a zároveň poskytuje lepší pokrytí ve vyšších zeměpisných šířkách než GEO. Tím řeší problém poskytování nepřetržité, spolehlivé služby regionům jako je severní Evropa, Kanada nebo Rusko. Definováním kanálových modelů, procedur mobility a úprav protokolů pro IGSO umožňuje 3GPP integraci těchto satelitů do budoucích sítí 5G a 6G jako standardizovaných komponent, což podporuje interoperabilitu a růst ekosystému pro kosmické spojení.

## Klíčové vlastnosti

- Geosynchronní oběžná perioda (24hodinová opakující se pozemní stopa)
- Nenulový orbitální sklon způsobující pozemní stopu ve tvaru osmičky
- Poskytuje trvalé regionální pokrytí s pohyblivými stopami buněk
- Vylepšená dostupnost služeb ve středních a vysokých zeměpisných šířkách ve srovnání s GEO
- Zavádí předvídatelné časově proměnné zpoždění a Dopplerův posuv
- Vyžaduje specifické adaptace 3GPP NTN pro časový předstih (timing advance) a mobilitu

## Definující specifikace

- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements

---

📖 **Anglický originál a plná specifikace:** [IGSO na 3GPP Explorer](https://3gpp-explorer.com/glossary/igso/)
