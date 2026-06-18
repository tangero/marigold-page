---
slug: "crci"
url: "/mobilnisite/slovnik/crci/"
type: "slovnik"
title: "CRCI – CRC Indicator"
date: 2025-01-01
abbr: "CRCI"
fullName: "CRC Indicator"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/crci/"
summary: "CRC indikátor je řídicí pole v protokolu rámců rozhraní Iub/Iur, které indikuje, zda přijatý datový blok obsahuje chybu CRC. Umožňuje RNC provádět selektivní retransmisi v datovém toku HSDPA, čímž zvy"
---

CRCI je řídicí pole v protokolu rámců rozhraní Iub/Iur, které indikuje, zda přijatý datový blok obsahuje chybu CRC, a umožňuje tak selektivní retransmisi pro HSDPA.

## Popis

[CRC](/mobilnisite/slovnik/crc/) indikátor (CRCI) je klíčový řídicí prvek v rámcovém protokolu ([FP](/mobilnisite/slovnik/fp/)) rozhraní Iub a Iur v sítích 3GPP UMTS/[HSPA](/mobilnisite/slovnik/hspa/). Funguje na vrstvě datového spoje (vrstva 2) řídicí roviny, konkrétně v rámci řetězce zpracování transportního kanálu mezi Node B a radiovou síťovou kontrolní jednotkou ([RNC](/mobilnisite/slovnik/rnc/)). CRCI je vložen do FP datových rámců, které přenášejí uživatelská data přes rozhraní Iub (Node B–RNC) a Iur (RNC–RNC), zejména pro transportní kanály High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) a Enhanced Uplink ([E-DCH](/mobilnisite/slovnik/e-dch/)).

Z architektonického hlediska je CRCI generováno Node B poté, co přijme a pokusí se dekódovat transportní blok od UE přes rádiové rozhraní Uu. Node B provede cyklickou redundanční kontrolu (CRC) na přijatém bloku. Výsledek této kontroly – zda blok prošel (CRC OK), nebo selhal (CRC NOT OK) – je následně zapouzdřen jako pole CRCI v odpovídajícím FP datovém rámci odesílaném směrem k RNC. Tento rámec putuje přes rozhraní Iub prostřednictvím transportní síťové vrstvy, která typicky využívá [ATM](/mobilnisite/slovnik/atm/) nebo IP transport. Entita MAC-hs nebo MAC-e/es v RNC extrahuje CRCI, aby informovala své procesy Hybrid [ARQ](/mobilnisite/slovnik/arq/) (HARQ) a řízení rádiového spoje (RLC).

Při provozu CRCI přímo ovlivňuje strategii retransmise. Pro downlink HSDPA, když RNC přijme FP rámec s CRCI indikujícím 'CRC OK', považuje odpovídající protokolovou datovou jednotku (PDU) MAC-hs za úspěšně doručenou k UE a může ji potvrdit vyšším vrstvám. Pokud CRCI indikuje 'CRC NOT OK', RNC ví, že se UE nepodařilo blok dekódovat. U HSDPA však primární HARQ retransmise probíhají mezi Node B a UE. RNC používá negativní CRCI především pro statistiku, monitorování rádiového spoje a v některých konfiguracích pro spuštění retransmise vnější smyčky RLC, pokud proces HARQ v Node B nakonec selže i po vyčerpání maximálního počtu pokusů. Jeho role je přímější v uplinku pro E-DCH, kde CRCI z Node B informuje procesy selektivního kombinování a HARQ v obsluhující RNC (SRNC).

Role CRCI je zásadní pro rozdělenou architekturu HSPA, kde je HARQ ukončen v Node B kvůli nízké latenci. Poskytuje RNC, která zpracovává vrstvu RLC, zásadní přehled o výkonu v koncovém bodě rádiového rozhraní, aniž by byla v přímé HARQ smyčce. To umožňuje koordinovaný provoz vrstvy 2, efektivní řízení toku na Iub a přesná měření kvality rádiového spojení pro funkce jako rozhodování o povolování hovorů a předávání spojení. Je to klíčová součást zajišťující spolehlivé doručování dat při optimalizaci využití jak rádiových, tak transportních síťových prostředků.

## K čemu slouží

CRC indikátor byl zaveden, aby řešil specifické výzvy architektury rozhraní Iub/Iur v UMTS a především aby umožnil vysokovýkonný provoz funkcí HSPA. V UMTS před HSPA byla veškerá retransmise (RLC) a plánování centralizováno v RNC. Se zavedením HSDPA ve vydání 5 byly HARQ a rychlé plánování přesunuty do Node B, aby se snížila latence. To vytvořilo nový problém: RNC, stále odpovědná za spolehlivé end-to-end doručování RLC, nyní neviděla úspěch nebo selhání jednotlivých přenosů přes rádiové rozhraní, protože ty byly řešeny lokálně HARQ entitou Node B.

Bez CRCI by RNC neměla přímou znalost o tom, zda datový blok úspěšně přijalo UE. Musela by se spoléhat pouze na RLC potvrzení od UE, která jsou pomalá, nebo na nepřímé indikátory z Node B. To by vedlo k neefektivitám. Například RNC by mohla zbytečně iniciovat RLC retransmisi pro blok, který HARQ v Node B stále aktivně opakoval, čímž by plýtvala rádiovou a transportní kapacitou. Naopak nemusela být včas informována o přetrvávající poruše rádiového spoje. CRCI to řeší tím, že poskytuje rychlý signalizační mechanismus v pásmu, který hlásí výsledek kontroly CRC na rádiovém rozhraní přímo do RNC v rámci stejného toku uživatelských dat.

Tento zpětnovazební mechanismus byl zásadní pro umožnění efektivního řízení toku na rozhraní Iub, přesného řízení zahlcení a účinného monitorování kvality rádiového spojení. Umožnil RNC provádět selektivní zpracování – předčasné zahození nebo označení poškozených dat – a udržovat přesné statistiky pro provoz a údržbu (O&M). V zásadě CRCI překlenulo informační mezeru vytvořenou decentralizací funkce HARQ, čímž zajistilo, že protokol RNC na vyšší vrstvě v RNC může koherentně fungovat s HARQ na nižší vrstvě v Node B, což bylo klíčové pro dosažení vysoké propustnosti a nízké latence, které jsou cílem HSPA.

## Klíčové vlastnosti

- Signalizace výsledku kontroly CRC na rádiovém rozhraní v pásmu, uvnitř FP rámců Iub/Iur
- Umožňuje RNC sledovat výsledek HARQ v Node B pro selektivní zpracování
- Podporuje efektivní řízení toku a řízení zahlcení na Iub transportu
- Poskytuje klíčový vstup pro rozhodování o retransmisích vnější smyčky RLC
- Umožňuje přesné měření a monitorování kvality rádiového spoje
- Nezbytný pro provoz HSDPA a E-DCH v rozdělené architektuře RAN

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)

## Definující specifikace

- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols

---

📖 **Anglický originál a plná specifikace:** [CRCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/crci/)
