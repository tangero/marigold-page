---
slug: "snpl"
url: "/mobilnisite/slovnik/snpl/"
type: "slovnik"
title: "SNPL – Serving and Neighbour cell Pathloss"
date: 2025-01-01
abbr: "SNPL"
fullName: "Serving and Neighbour cell Pathloss"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/snpl/"
summary: "SNPL je měření používané v sítích UMTS/HSPA k odhadu útlumu na rádiové cestě mezi UE a jeho obslužnou buňkou i sousedními buňkami. Je klíčové pro rozhodování o předání hovoru, převýběr buňky a algorit"
---

SNPL je měření v sítích UMTS/HSPA, které slouží k odhadu útlumu na rádiové cestě mezi uživatelským zařízením a jeho obslužnou buňkou i sousedními buňkami pro účely předávání hovoru, převýběru buňky a řízení výkonu.

## Popis

Serving and Neighbour cell Pathloss (SNPL) je základní rádiové měření definované ve specifikacích 3GPP, primárně pro sítě UMTS a [HSPA](/mobilnisite/slovnik/hspa/). Útlum na rádiové cestě (path loss) představuje zeslabení síly signálu při šíření rádiové vlny od vysílače (Node B/základnové stanice) k přijímači (uživatelskému zařízení/UE). SNPL konkrétně označuje schopnost UE měřit a hlásit tento útlum jak pro svou aktuálně připojenou obslužnou buňku, tak pro detekované sousední buňky. Toto měření je odvozeno z přijaté výkonové úrovně známých referenčních signálů, jako je Common Pilot Channel ([CPICH](/mobilnisite/slovnik/cpich/)) v UMTS, a ze znalosti vysílaného výkonu těchto signálů, který je buňkou vysílán. UE vypočítá útlum jako rozdíl (v dB) mezi vysílaným výkonem referenčního signálu a přijatým výkonem.

Architektura pro SNPL zahrnuje měřicí schopnosti fyzické vrstvy UE, protokol Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) pro hlášení a síťové algoritmy v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). UE kontinuálně monitoruje Received Signal Code Power ([RSCP](/mobilnisite/slovnik/rscp/)) pro CPICH své obslužné buňky a uvedených sousedních buněk. Pomocí parametru vysílaného výkonu CPICH, který je vysílán, vypočítá útlum. Tato měření jsou následně hlášena síti prostřednictvím RRC měřicích hlášení, a to buď periodicky, nebo při splnění specifických podmínek (např. když útlum sousední buňky dosáhne o určitý práh lepší hodnoty než útlum obslužné buňky).

V síti RNC využívá hlášení SNPL pro několik klíčových funkcí správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)). Je to klíčový vstup pro rozhodování o předání hovoru ([HO](/mobilnisite/slovnik/ho/)), který pomáhá určit, kdy má být UE předáno buňce s příznivějšími podmínkami šíření. Také napomáhá převýběru buňky pro UE v klidovém režimu. Dále je SNPL nepřímo využíván v algoritmech řízení výkonu; znalost útlumu pomáhá síti odhadnout potřebný výkon pro vysílání UE v uplinku k dosažení cílové kvality signálu na základnové stanici, čímž se optimalizuje kapacita systému a snižuje interference. Jeho role je zásadní pro udržení kvality hovoru, zajištění kontinuity pokrytí a správu vytížení sítě.

## K čemu slouží

SNPL bylo zavedeno, aby síti poskytlo přímou metriku pro správu mobility a zdrojů založenou na podmínkách šíření, která je zásadnější než prostá měření přijímaného výkonu. Před zavedením nebo vedle SNPL se používala měření jako Received Signal Strength Indicator ([RSSI](/mobilnisite/slovnik/rssi/)) nebo RSCP. Tato měření přijímaného výkonu však samostatně nezohledňují rozdíly ve vysílacím výkonu základnových stanic. Buňka s vysokým vysílacím výkonem může mít silný RSCP, i když je útlum na rádiové cestě špatný, což by mohlo zavádět algoritmy pro předání hovoru. SNPL tento problém řeší normalizací přijímaného výkonu pomocí známého vysílaného výkonu, čímž poskytuje skutečnou míru útlumu rádiového kanálu.

Hlavním problémem, který SNPL řeší, je potřeba přesného a konzistentního porovnání kvality buněk pro rozhodování o mobilitě. Pro efektivní předávání hovorů síť potřebuje vědět, která buňka poskytuje nejlepší rádiové spojení, nikoli pouze to, která je v daném okamžiku přijímána nejsilněji. Použitím útlumu na rádiové cestě může síť přesněji predikovat výkon v uplinku a činit rozhodnutí, která vyvažují výkon v uplinku a downlinku. To vede ke stabilnějším spojením, snížení počtu přerušených hovorů a lepšímu celkovému využití rádiových zdrojů. Jeho vytvoření bylo motivováno vývojem směrem k autonomnější a inteligentnější správě RRM v sítích 3GPP, která překračuje pouhé práhové hodnoty směrem k algoritmům založeným na stavu rádiového kanálu.

## Klíčové vlastnosti

- Poskytuje normalizovanou míru útlumu rádiového kanálu pro obslužnou a sousední buňky
- Odvozeno z CPICH RSCP a vysílaného výkonu CPICH (broadcast) v UMTS
- Používáno jako klíčový vstup pro algoritmy rozhodování o předání hovoru v RNC
- Podporuje procedury převýběru buňky v klidovém režimu
- Napomáhá odhadu řízení výkonu v uplinku
- Hlášeno UE síti prostřednictvím procedur RRC measurement control

## Související pojmy

- [RSCP – Reference Signal Carrier Phase](/mobilnisite/slovnik/rscp/)
- [CPC – Continuous Packet Connectivity](/mobilnisite/slovnik/cpc/)

## Definující specifikace

- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [SNPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/snpl/)
