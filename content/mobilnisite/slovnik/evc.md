---
slug: "evc"
url: "/mobilnisite/slovnik/evc/"
type: "slovnik"
title: "EVC – Essential Video Coding"
date: 2025-01-01
abbr: "EVC"
fullName: "Essential Video Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/evc/"
summary: "Standard pro kompresi videa vyvinutý MPEG a přijatý 3GPP pro efektivní doručování médií přes mobilní sítě. Poskytuje výrazně lepší kompresi než jeho předchůdce HEVC, což umožňuje streamování videa vyš"
---

EVC je standard pro kompresi videa přijatý 3GPP pro mobilní sítě, který poskytuje lepší kompresi než HEVC a umožňuje streamování vyšší kvality při nižších přenosových rychlostech.

## Popis

Essential Video Coding (EVC), standardizované jako MPEG-5 Part 1, je specifikace video kodeku začleněná 3GPP pro multimediální služby. Jeho architektura je navržena se dvěma odlišnými profily: bezlicenčním (royalty-free) základním (Baseline) profilem, který využívá pouze technologie starší 20 let nebo volně licencované, a hlavním (Main) profilem, který začleňuje další pokročilé kódovací nástroje pro vyšší účinnost, ale může podléhat licencování. Kodek funguje na principu hybridního blokového přístupu, podobně jako předchůdci [AVC](/mobilnisite/slovnik/avc/) a [HEVC](/mobilnisite/slovnik/hevc/), ale s vylepšenými algoritmy pro predikci, transformaci a entropické kódování.

Proces kódování začíná rozdělením každého snímku videa na bloky. Pro každý blok provádí kodér vnitrosnímkovou predikci (s využitím pixelů ze stejného snímku) nebo mezisnímkovou predikci (s využitím pohybově kompenzovaných pixelů z dříve zakódovaných snímků). Rozdíl mezi původním blokem a jeho predikcí, zvaný reziduum, je následně transformován (např. pomocí celočíselné kosinové transformace) a kvantován pro redukci dat. Kvantované transformační koeficienty spolu s informacemi o režimu predikce a pohybovými vektory jsou entropicky zakódovány do komprimovaného bitového toku. EVC zavádí několik vylepšených nástrojů, jako je flexibilnější dělení bloků, vylepšené směry vnitrosnímkové predikce a pokročilá predikce pohybových vektorů, které společně snižují přenosovou rychlost potřebnou pro danou vizuální kvalitu.

V rámci ekosystému 3GPP je EVC specifikováno jako podporovaný kodek pro službu Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), streamování a konverzační služby. Je definováno ve specifikacích mediálních kodeků (řada 26) spolu s dalšími kodeky jako AVC, HEVC a VVC. Jeho úlohou je poskytnout efektivní a kvalitní možnost komprese videa pro poskytovatele služeb, což jim umožňuje doručovat zážitky z videa ve 4K, [HDR](/mobilnisite/slovnik/hdr/) a imerzivního videa přes mobilní sítě při současném zvládání zahlcení sítě a datových nákladů. Specifikace podrobně popisuje syntaxi bitového toku, dekódovací proces a body shody (compliance points) pro zajištění interoperability mezi kodéry a dekodéry od různých výrobců.

## K čemu slouží

EVC bylo vytvořeno, aby řešilo potřebu trhu po efektivnějším a komerčně životaschopném standardu pro kódování videa v kontextu složitého licencování patentů kolem [HEVC](/mobilnisite/slovnik/hevc/). Rychlý růst mobilního video provozu, poháněný streamovacími službami a sociálními médii, vyžadoval neustálá zlepšování účinnosti komprese k úspoře vzácného bezdrátového spektra a snížení nákladů na doručování dat. Přijetí HEVC však bránila vnímaná nejistota a náklady spojené s licencováním, což vytvořilo překážku pro široké nasazení, zejména v segmentech citlivých na licenční poplatky.

Primární problém, který EVC řeší, je poskytnutí technologie komprese nové generace s jasnými licenčními podmínkami, zejména prostřednictvím svého základního (Baseline) profilu. Nabízí výrazné snížení přenosové rychlosti – přibližně o 30–40 % oproti HEVC při podobné kvalitě – což přímo vede k nižší spotřebě šířky pásma a lepší uživatelské zkušenosti na přetížených sítích nebo sítích s omezenou kapacitou. Tato účinnost je klíčová pro nově se objevující aplikace, jako je streamování 4K/8K, video 360° a rozšířená realita přes 5G.

Přijetí EVC 3GPP ve verzi (Release) 16 bylo motivováno snahou dát odvětví na výběr z pokročilých kodeků s různými kompromisy mezi výkonem a aspekty duševního vlastnictví (IP). Standardizací EVC zajišťuje 3GPP, že se jedná o plně specifikovanou a interoperabilní možnost v rámci rámce pro doručování médií, což umožňuje mobilním operátorům a poskytovatelům obsahu nasadit jej pro vysílací (broadcast), skupinové (multicast) a individuální (unicast) video služby. Představuje strategické úsilí o zajištění budoucí odolnosti mobilních mediálních služeb pomocí efektivní a kvalitní komprese při snaze vyrovnat se s výzvami licencování kodeků.

## Klíčové vlastnosti

- Dvojprofilový design: bezlicenční (royalty-free) základní (Baseline) profil a vysoce účinný hlavní (Main) profil
- Úspora přenosové rychlosti přibližně o 30–40 % oproti HEVC při stejné vizuální kvalitě
- Podpora videa s vysokým rozlišením (až 8K), HDR a širokého barevného gamutu
- Pokročilé kódovací nástroje, jako adaptivní rozlišení pohybového vektoru a vylepšená vnitrosnímková predikce
- Specifikováno pro použití ve službách 3GPP MBMS, streamování a konverzačních službách
- Navrženo s jasnou složitostí dekodéru pro praktickou implementaci v hardwaru a softwaru

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [EVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/evc/)
