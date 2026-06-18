---
slug: "par"
url: "/mobilnisite/slovnik/par/"
type: "slovnik"
title: "PAR – Peak to Average Ratio"
date: 2025-01-01
abbr: "PAR"
fullName: "Peak to Average Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/par/"
summary: "Metrika, často zaměňovaná s PAPR, popisující poměr špičkového výkonu signálu k jeho průměrnému výkonu. Zdůrazňuje požadavky na linearitu vysílacích komponent, zejména výkonových zesilovačů. Vysoké hod"
---

PAR je metrika popisující poměr špičkového výkonu signálu k jeho průměrnému výkonu, která zdůrazňuje požadavky na linearitu vysílacích komponent a při vysokých hodnotách může vést k neefektivitě a zkreslení.

## Popis

Poměr špičkového a průměrného výkonu (Peak to Average Ratio, PAR) je základní charakteristikou jakéhokoli časově proměnného signálu, popisující rozdíl mezi jeho nejvyšším okamžitým výkonem a jeho střední úrovní výkonu. V kontextu systémů 3GPP se jedná o klíčový parametr pro hodnocení požadavků na výkon a návrh řetězce vysílače radiofrekvenčního ([RF](/mobilnisite/slovnik/rf/)) signálu. Matematicky je vyjádřen jako PAR = 10 * log10(P_peak / P_avg) v decibelech (dB), nebo jednoduše jako lineární poměr. Signál s vysokým PAR má velké, sporadické špičky, které dominují jeho výkonovému profilu. Tyto špičky nutí aktivní komponenty systému, zejména výkonový zesilovač ([PA](/mobilnisite/slovnik/pa/)), číslicově-analogové převodníky ([DAC](/mobilnisite/slovnik/dac/)) a míchače, pracovat v širokém dynamickém rozsahu.

Dopad PAR je nejvíce patrný u výkonového zesilovače. Aby se zabránilo nelineárnímu zkreslení – které způsobuje degradaci chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)) v pásmu a spektrální přesah mimo pásmo – musí PA pracovat s výrazným odstupem od svého kompresního bodu. Tento 'odstup' je v podstatě rozdíl mezi maximálním výstupním výkonem PA a průměrným výkonem vysílaného signálu a je přímo ovlivněn PAR signálu. Provoz s vysokým odstupem nutí PA pracovat v méně efektivní oblasti své provozní charakteristiky, čímž se více stejnosměrného výkonu přeměňuje na odpadní teplo namísto výkonu RF. U síťové infrastruktury to zvyšuje náklady na energii a nároky na chlazení. U uživatelských zařízení to výrazně snižuje výdrž baterie.

Specifikace 3GPP, zejména pro vývoj GSM/[EDGE](/mobilnisite/slovnik/edge/) a další studie, odkazují na PAR při hodnocení architektur vysílačů a modulačních schémat. Ačkoli je v pozdějších širokopásmových kontextech často používáno synonymně s [PAPR](/mobilnisite/slovnik/papr/), v některých specifikacích může být PAR posuzován v poněkud širším kontextu, zahrnujícím účinky celého vysílacího řetězce před anténou. Řízení PAR zahrnuje rozhodnutí na systémové úrovni, jako je výběr modulačních schémat s příznivými vlastnostmi PAR (např. [GMSK](/mobilnisite/slovnik/gmsk/) v GSM má konstantní obálku, PAR=0 dB), a použití technik úpravy signálu, jako je ořezávání ve základním pásmu, filtrování nebo pokročilá digitální predistorze ([DPD](/mobilnisite/slovnik/dpd/)), k linearizaci odezvy PA a zlepšení celkové účinnosti i při vysokých hodnotách PAR signálu.

## K čemu slouží

Účelem specifikace a analýzy PAR ve standardech 3GPP je zajistit praktickou proveditelnost a účinnost číslicových modulačních schémat pro mobilní komunikace. Jak se systémy vyvíjely od konstantní obálky GMSK v GSM ke složitým modulacím s vysokým řádem QAM v EDGE a dalších, vysílané signály získávaly vyšší hodnoty PAR. Tento vývoj vytvořil přímý konflikt mezi dosažením vysoké spektrální účinnosti a zachováním přiměřené účinnosti a nákladů výkonového zesilovače.

Standardizace ohledů na PAR poskytla společný technický jazyk a soubor požadavků pro dodavatele komponent a systémové návrháře. Zdůraznila kompromisy, které je třeba učinit: modulační schéma nabízející vyšší přenosové rychlosti může být nepoužitelné, pokud je jeho PAR příliš vysoký pro cenově dostupné zesilovače šetrné k baterii. To pohánělo inovace jak v oblasti zpracování signálu (ke snížení PAR), tak v technologii zesilovačů (k lepší toleranci PAR). V historickém kontextu vývoje GSM/EDGE bylo řízení PAR klíčové pro zvýšení přenosových rychlostí v rámci stávajícího RF rámce, což zajišťovalo zpětnou kompatibilitu a nákladově efektivní modernizace sítí.

## Klíčové vlastnosti

- Definuje požadavky na linearitu a dynamický rozsah RF vysílačů.
- Klíčový faktor určující účinnost a provozní náklady výkonového zesilovače.
- Hodnocen pro různá modulační schémata (např. 8-PSK, QAM) ve specifikacích GSM/EDGE.
- Ovlivňuje návrh komponent číslicového předního konce, jako jsou DAC a míchače.
- Ovlivňuje rozhodnutí na systémové úrovni ohledně modulačních a kódovacích schémat (MCS).
- Úzce souvisí s metrikami jako činitel vrcholů (Crest Factor) a PAPR.

## Související pojmy

- [PAPR – Peak-to-Average Power Ratio](/mobilnisite/slovnik/papr/)
- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)
- [8-PSK – 8-state Phase Shift Keying](/mobilnisite/slovnik/8-psk/)
- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 37.808** (Rel-12) — PIM Handling for Base Stations Study
- **TS 45.860** (Rel-11) — Precoded EGPRS2 Downlink Study
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [PAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/par/)
