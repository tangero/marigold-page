---
slug: "nr-dc"
url: "/mobilnisite/slovnik/nr-dc/"
type: "slovnik"
title: "NR-DC – NR-NR Dual Connectivity"
date: 2026-01-01
abbr: "NR-DC"
fullName: "NR-NR Dual Connectivity"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nr-dc/"
summary: "NR-NR Dual Connectivity (NR-DC) je funkce 5G, která umožňuje uživatelskému zařízení současně se připojit ke dvěma skupinám NR buněk, typicky k hlavnímu uzlu (MN) a sekundárnímu uzlu (SN), využívajíc r"
---

NR-DC je funkce 5G, při které se zařízení současně připojuje ke dvěma skupinám NR buněk prostřednictvím různých pásem, aby agregovalo jejich rádiové zdroje pro vyšší datové rychlosti, spolehlivost a mobilitu.

## Popis

NR-NR Dual Connectivity (NR-DC) je pokročilé schéma vícekanálového připojení v 5G, při kterém je uživatelské zařízení (UE) současně připojeno ke dvěma různým skupinám NR buněk: k hlavnímu uzlu ([MN](/mobilnisite/slovnik/mn/)) a sekundárnímu uzlu (SN). Tyto uzly mohou být gNB (Next Generation NodeBs) pracující v různých frekvenčních pásmech (např. střední pásmo a mmWave) a jsou koordinovány, aby sloužily UE současně. Architektura zahrnuje konfigurace rozdělených přenosových kanálů (bearerů), kde datové rádiové přenosové kanály ([DRB](/mobilnisite/slovnik/drb/)) mohou být ukončeny buď na MN, nebo SN, nebo rozděleny mezi oba pomocí duplikace nebo rozdělení protokolu PDCP (Packet Data Convergence Protocol). MN spravuje řídicí rovinu prostřednictvím protokolu [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), zatímco SN poskytuje další zdroje v uživatelské rovině, přičemž koordinace probíhá přes rozhraní Xn mezi uzly.

Fungování NR-DC zahrnuje několik klíčových procedur. Při nastavování se MN na základě měřicích hlášení od UE rozhodne přidat SN, což spustí proceduru přidání SN prostřednictvím signalizace Xn. UE následně naváže sekundární skupinu buněk (SCG) se SN a nakonfiguruje sekundární buňky (SCell) pro přenos dat. Tok dat může být řízen prostřednictvím přenosových kanálů [MCG](/mobilnisite/slovnik/mcg/) (Master Cell Group), SCG nebo rozdělených kanálů v závislosti na nasazení. U rozdělených kanálů vrstva PDCP na MN nebo SN zpracovává duplikaci nebo distribuci paketů do vrstev RLC v obou uzlech, čímž zvyšuje propustnost a spolehlivost. Synchronizace a koordinace mezi MN a SN jsou klíčové pro zabránění interferencí a zajištění bezproblémových předávání spojení, s využitím mechanismů jako řízení výkonu a koordinace plánování.

Úloha NR-DC v síti spočívá v maximalizaci využití zdrojů a kvality služeb. Umožňuje vyšší špičkové datové rychlosti agregací šířky pásma z více nosných, často napříč různými pásmy, což je zvláště užitečné v 5G, kde je spektrum fragmentované. Zlepšuje spolehlivost prostřednictvím duplikace paketů, čímž splňuje požadavky URLLC pro kritické aplikace. Dále NR-DC zlepšuje mobilitu tím, že umožňuje UE udržovat připojení k jednomu uzlu při přechodu k druhému, čímž se snižují doby přerušení. To je zásadní v hustých nebo heterogenních sítích se smíšeným nasazením makro a malých buněk, což zajišťuje konzistentní výkon při pohybu uživatelů.

## K čemu slouží

NR-DC byla vyvinuta pro řešení výzev spojených s dosažením ultra vysokých datových rychlostí, spolehlivého připojení a efektivního využití spektra v sítích 5G. Předchozí technologie, jako LTE-NR Dual Connectivity ([EN-DC](/mobilnisite/slovnik/en-dc/)), umožňovaly agregaci mezi 4G a 5G, ale byly limitovány možnostmi LTE. S vývojem sítí směrem k samostatnému 5G (standalone) vznikla potřeba nativního řešení NR, které by plně využilo pokročilé funkce 5G napříč více frekvenčními pásmy. Účelem NR-DC je umožnit operátorům využít jejich různorodá spektrální portfolia (např. kombinace nízkopásmového spektra pro pokrytí a vysokopásmového pro kapacitu) bez omezení ze strany starších systémů.

Historicky bylo vícekanálové připojení zavedeno v LTE-Advanced pro agregaci zdrojů z více základnových stanic, ale šlo primárně o intra-LTE. S širším rozsahem spektra a novými případy použití v 5G řeší NR-DC problémy, jako je fragmentované využití spektra, tím, že umožňuje současné použití nesousedních pásem. Řeší také problémy s mobilitou v hustých sítích tím, že poskytuje kotvící body pro bezproblémová předání spojení. Motivace vychází z poptávky po rozšířeném mobilním širokopásmovém připojení (eMBB) a ultra spolehlivé komunikaci, kde připojení k jedinému uzlu může být nedostatečné. NR-DC usnadňuje zhušťování sítí a agregaci nosných v čistém prostředí 5G, což pohání zlepšování výkonu a podporuje inovativní služby, jako je rozšířená realita a průmyslová automatizace.

## Klíčové vlastnosti

- Současné připojení k hlavnímu uzlu (MN) a sekundárnímu uzlu (SN) v NR
- Podpora rozdělených přenosových kanálů s duplikací nebo rozdělením PDCP pro zvýšenou propustnost a spolehlivost
- Koordinace přes rozhraní Xn mezi gNB pro správu zdrojů
- Flexibilní konfigurace přenosových kanálů (MCG, SCG a rozdělené kanály)
- Vylepšená mobilita se sníženým přerušením během předávání spojení mezi uzly
- Využití různorodých frekvenčních pásem (např. FR1 a FR2) pro optimální využití spektra

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.825** (Rel-16) — Security for 5G URLLC Services
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.846** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NR-DC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nr-dc/)
