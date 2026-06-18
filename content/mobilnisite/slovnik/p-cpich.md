---
slug: "p-cpich"
url: "/mobilnisite/slovnik/p-cpich/"
type: "slovnik"
title: "P-CPICH – Primary Common Pilot Channel"
date: 2025-01-01
abbr: "P-CPICH"
fullName: "Primary Common Pilot Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/p-cpich/"
summary: "P-CPICH je downlinkový fyzický kanál v UMTS (WCDMA), který vysílá předdefinovanou bitovou sekvenci. Poskytuje konstantní fázovou referenci pro všechny ostatní downlinkové kanály, umožňuje odhad kanálu"
---

P-CPICH je Primární společný pilotní kanál (Primary Common Pilot Channel), což je downlinkový fyzický kanál v UMTS, který poskytuje konstantní fázový referenční signál pro koherentní demodulaci a slouží jako primární signál pro měření kvality buňky.

## Popis

Primární společný pilotní kanál (Primary Common Pilot Channel – P-CPICH) je klíčový downlinkový fyzický kanál v rádiovém rozhraní UMTS [WCDMA](/mobilnisite/slovnik/wcdma/). Jde o nemodulovaný kanál, který nepřetržitě vysílá známou sekvenci bitů (konstantní vzor binárních nul). Jeho primární technická funkce spočívá v tom, že slouží uživatelskému zařízení (UE) jako stabilní fázová a amplitudová reference. Jelikož WCDMA pro downlinkové datové kanály používá kvadraturní fázovou manipulaci (modulaci [QPSK](/mobilnisite/slovnik/qpsk/)), musí přijímač přesně odhadnout fázové natočení a útlum amplitudy (fading) zavedené rádiovým kanálem, aby mohl data správně demodulovat. P-CPICH tuto referenci poskytuje. UE nepřetržitě sleduje P-CPICH, používá jej k odhadu impulsní odezvy kanálu a následně aplikuje inverzní odhad pro koherentní demodulaci ostatních vyhrazených nebo společných kanálů, které jsou mu přiděleny.

Každá buňka vysílá právě jeden P-CPICH. Je charakterizován pevným kanalizačním kódem (primární vykrývací kód) a pevným rozprostíracím faktorem 256. Vysílán je v celé oblasti pokrytí buňky, obvykle na vyšší výkonové úrovni než ostatní společné kanály, aby byla zajištěna dobrá poměrná úroveň signálu vůči rušení pro přesný odhad kanálu. P-CPICH se nepoužívá pro přenos uživatelských ani signalizačních dat; jeho hodnota spočívá výhradně v jeho předvídatelné signálové struktuře. Klíčový koncept je ten, že všechny ostatní downlinkové fyzické kanály ve stejné buňce používají P-CPICH jako svou fázovou referenci. To zahrnuje vyhrazené kanály ([DPCH](/mobilnisite/slovnik/dpch/)), další společné kanály jako Sekundární [CCPCH](/mobilnisite/slovnik/ccpch/) ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)) nesoucí transportní kanály Paging a [FACH](/mobilnisite/slovnik/fach/), a dokonce i synchronizační kanály.

Kromě demodulace je P-CPICH základním měřeným objektem pro klíčové procedury správy rádiových zdrojů. UE měří přijímaný výkon P-CPICH, známý jako Received Signal Code Power ([RSCP](/mobilnisite/slovnik/rscp/)), a poměr přijaté energie na čip k celkové spektrální hustotě rušení ([Ec](/mobilnisite/slovnik/ece-c/)/Io). Tato měření jsou hlášena síti a jsou primárními metrikami používanými pro výběr buňky (když je UE v režimu nečinnosti), její převýběr a rozhodování o předání hovoru (když je UE v připojeném režimu). Síť může také použít různé primární vykrývací kódy na P-CPICH sousedních buněk, což umožňuje UE jednoznačně identifikovat a rozlišovat mezi buňkami, i když jsou na stejné frekvenci, prostřednictvím korelace vůči známé sadě možných vykrývacích kódů.

## K čemu slouží

P-CPICH byl zaveden, aby řešil dva kritické problémy v systémech WCDMA: umožnění koherentní demodulace v mnohacestném (fadingovém) prostředí a poskytnutí univerzálního, vysoce kvalitního signálu pro měření rádiových zdrojů. V systémech CDMA je přesný odhad kanálu prvořadý, protože ortogonalita kanalizačních kódů může být mnohacestným kanálem narušena, což vede k mezisymbolovému rušení. Vyhrazený, známý pilotní signál umožňuje přijímači sledovat rychlé změny kanálu a kompenzovat je, což výrazně zlepšuje demodulační výkon a celkovou kapacitu systému ve srovnání s nekoherentními detekčními metodami.

Historicky jsou pilotní signály základem digitálních komunikačních systémů, ale jejich implementace ve WCDMA musela být standardizována. Koncepce P-CPICH poskytuje společnou, celobuněčnou referenci. To je efektivnější než vkládání pilotních symbolů do každého vyhrazeného kanálu, zejména pro společné kanály, které musí přijímat více UE. Existence jediného, silného pilotního kanálu jako reference pro všechny ostatní kanály může snížit složitost přijímače. Dále, pro správu mobility potřebuje síť konzistentní a srovnatelnou metriku kvality buňky od všech UE. P-CPICH se svým pevným výkonovým vztahem k ostatním kanálům (ačkoli absolutní výkon může být nastaven operátorem) poskytuje tento standardizovaný bod měření. Jeho nepřetržitý přenos umožňuje UE kontinuálně sledovat kvalitu obsluhující a sousedních buněk, což umožňuje rychlá a spolehlivá předání hovoru, což je nezbytné pro udržení kvality hovoru a spolehlivosti sítě v celulárním systému. P-CPICH tedy není pouze technickou výhodou, ale základním prvkem, který umožňuje vysokou spektrální účinnost a robustní mobilitu sítí UMTS.

## Klíčové vlastnosti

- Vysílá známou, konstantní bitovou sekvenci, která poskytuje fázovou a amplitudovou referenci pro odhad kanálu.
- Používá pevný rozprostírací faktor (SF=256) a je vždy vykrýván primárním vykrývacím kódem buňky.
- Slouží jako povinná fázová reference pro všechny ostatní downlinkové fyzické kanály v rámci stejné buňky.
- Primární zdroj pro měření UE – Received Signal Code Power (RSCP) a Ec/Io – pro správu rádiových zdrojů.
- Vysílán na konstantním, relativně vysokém výkonu (typicky 5–10 % celkového výkonu Node B), aby byla zajištěna spolehlivost odhadu.
- Základní prvek pro koherentní demodulaci, identifikaci buňky a mobilní procedury, jako je předání hovoru a výběr/převýběr buňky.

## Související pojmy

- [S-CPICH – Secondary Common Pilot Channel](/mobilnisite/slovnik/s-cpich/)
- [P-CCPCH – Primary Common Control Physical Channel](/mobilnisite/slovnik/p-ccpch/)
- [RSCP – Reference Signal Carrier Phase](/mobilnisite/slovnik/rscp/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS

---

📖 **Anglický originál a plná specifikace:** [P-CPICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-cpich/)
