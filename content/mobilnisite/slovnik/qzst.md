---
slug: "qzst"
url: "/mobilnisite/slovnik/qzst/"
type: "slovnik"
title: "QZST – Quasi-Zenith System Time"
date: 2025-01-01
abbr: "QZST"
fullName: "Quasi-Zenith System Time"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qzst/"
summary: "Interní, vysoce stabilní časová stupnice generovaná a udržovaná pozemním řídicím segmentem systému Quasi-Zenith Satellite System (QZSS). Slouží jako přesný časový referenční zdroj pro všechny satelity"
---

QZST je vysoce stabilní časová stupnice generovaná pozemním segmentem systému Quasi-Zenith Satellite System, která slouží jako přesný časový referenční zdroj pro jeho satelity a signály.

## Popis

Quasi-Zenith System Time (QZST) je základní časová stupnice japonského systému Quasi-Zenith Satellite System. Jedná se o kontinuální atomovou časovou stupnici generovanou souborem atomových hodin umístěných v hlavní řídicí stanici [QZSS](/mobilnisite/slovnik/qzss/) a dalších monitorovacích stanicích. QZST není uživatelům přímo vysílána; místo toho tvoří stabilní referenci, vůči níž jsou měřeny a řízeny všechny palubní hodiny satelitů QZSS. Přesnost a stabilita QZST jsou klíčové, protože satelitní navigace je zásadně založena na přesném měření doby šíření rádiových signálů.

Pozemní segment QZSS nepřetržitě monitoruje časový posun mezi palubními hodinami každého satelitu a QZST pomocí měření z geograficky rozptýlených monitorovacích stanic. Tato data jsou zpracována řídicím segmentem za účelem generování přesných parametrů korekce hodin pro každý satelit. Tyto korekční parametry spolu s informací o vztahu mezi QZST a dalšími systémovými časy [GNSS](/mobilnisite/slovnik/gnss/) (jako je [GPS](/mobilnisite/slovnik/gps/) Time (GPST) a Galileo System Time ([GST](/mobilnisite/slovnik/gst/))) jsou nahrávány na satelity. Satelity následně tyto korekce vysílají ve svých navigačních zprávách, což umožňuje uživatelskému zařízení (UE) synchronizovat svá měření na společnou, přesnou časovou stupnici.

V 3GPP pozicovacích protokolech je QZST klíčovým podkladovým konceptem pro Assisted GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Když síť poskytuje asistenční data pro QZSS, tato data jsou inherentně vztažena k QZST. Asistenční data zahrnují parametry popisující posun mezi QZST a GPST (nebo jinými časy GNSS), stejně jako individuální korekce hodin pro každý satelit [QZS](/mobilnisite/slovnik/qzs/) vzhledem k QZST. UE tyto informace využívá k zarovnání měření z více konstelací GNSS (QZSS, GPS atd.) na jedinou konzistentní časovou stupnici, což umožňuje přesné hybridní určování polohy. Specifikace definují, jak jsou tyto parametry časového posunu a korekce hodin formátovány a přenášeny na UE, čímž zajišťují interoperabilitu mezi síťovými asistovanými pozicovacími servery a zařízeními schopnými přijímat signály QZSS.

## K čemu slouží

Vytvoření QZST řeší základní požadavek každého satelitního navigačního systému: stabilní, kontinuální a vnitřně konzistentní časovou referenci. Satelitní určování polohy vypočítává vzdálenost měřením časového zpoždění signálů putujících z více satelitů. Pokud nejsou hodiny na satelitech dokonale synchronizovány mezi sebou a se společnou referencí, dochází k velkým chybám v určení polohy. Každý hlavní systém [GNSS](/mobilnisite/slovnik/gnss/) ([GPS](/mobilnisite/slovnik/gps/), Galileo, GLONASS, BeiDou) udržuje svůj vlastní systémový čas. QZSS jako nezávislý systém vyžaduje vlastní přesnou časovou stupnici, aby zajistil integritu a přesnost svých signálů.

QZST byl vyvinut, aby poskytl tuto suverénní schopnost měření času pro japonský regionální systém. Umožňuje QZSS autonomní provoz a zároveň těsné propojení s dalšími globálními časovými stupnicemi. Klíčový problém, který řeší, je bezproblémová integrace QZSS s dalšími konstelacemi GNSS. Přesným definováním a udržováním posunu mezi QZST a GPST mohou přijímače s podporou QZSS používat měření ze satelitů QZSS i GPS společně, aniž by docházelo k chybám způsobeným rozdíly časových stupnic. Tato interoperabilita je zásadní pro poskytování robustního vícekonstelačního řešení pro určování polohy. Navíc udržování QZST umožňuje Japonsku mít kontrolu nad kritickým prvkem národní infrastruktury – přesným časem – který má uplatnění i mimo navigaci, včetně financí, telekomunikací a synchronizace energetických sítí.

## Klíčové vlastnosti

- Atomová časová stupnice generovaná a udržovaná pozemním řídicím segmentem QZSS
- Slouží jako hlavní časová reference pro všechny hodiny satelitů QZSS
- Přesně řízena tak, aby byla zarovnána s dalšími časovými stupnicemi GNSS, jako je GPS Time
- Umožňuje generování parametrů korekce satelitních hodin vysílaných uživatelům
- Základní pro interoperabilitu více systémů GNSS a hybridní určování polohy
- Poskytuje stabilní časový základ pro augmentační služby QZSS (SBAS, CLAS)

## Související pojmy

- [QZSS – Quasi-Zenith Satellite System](/mobilnisite/slovnik/qzss/)
- [QZS – Quasi-Zenith Satellite](/mobilnisite/slovnik/qzs/)

## Definující specifikace

- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [QZST na 3GPP Explorer](https://3gpp-explorer.com/glossary/qzst/)
