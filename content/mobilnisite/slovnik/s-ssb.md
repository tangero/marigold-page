---
slug: "s-ssb"
url: "/mobilnisite/slovnik/s-ssb/"
type: "slovnik"
title: "S-SSB – Sidelink Synchronization Signal Block"
date: 2025-01-01
abbr: "S-SSB"
fullName: "Sidelink Synchronization Signal Block"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-ssb/"
summary: "Blok synchronizačních signálů vysílaný přes sidelink rozhraní pro sidelink komunikaci založenou na NR. Umožňuje synchronizaci mezi zařízeními a poskytuje základní informace pro počáteční přístup a výb"
---

S-SSB je blok synchronizačních signálů vysílaný přes sidelink rozhraní v NR, který umožňuje synchronizaci mezi zařízeními a poskytuje základní informace pro počáteční přístup a výběr zdrojů.

## Popis

Blok sidelink synchronizačních signálů (Sidelink Synchronization Signal Block, S-SSB) je základní struktura signálů fyzické vrstvy definovaná pro sidelink komunikaci v New Radio (NR), počínaje 3GPP Release 16. Je to sidelink protějšek downlinkového bloku [SS](/mobilnisite/slovnik/ss/)/[PBCH](/mobilnisite/slovnik/pbch/) (SSB) používaného v přístupu přes rozhraní Uu. S-SSB vysílá (broadcastuje) referenční synchronizační UE (Synchronization Reference, SyncRef) nebo v některých konfiguracích gNB, aby umožnil časovou a frekvenční synchronizaci pro další blízká sidelink UE (tj. přijímací UE). Jeho hlavní funkcí je vytvoření společného časového referenčního bodu pro fond sidelink zdrojů, což je klíčové pro ortogonální přidělování zdrojů a minimalizaci interference v decentralizovaných (režim 2) nebo síťově asistovaných (režim 1) sidelink operacích.

S-SSB se v časové doméně skládá ze čtyř po sobě jdoucích [OFDM](/mobilnisite/slovnik/ofdm/) symbolů a ve frekvenční doméně pro jednu numerologii pokrývá 11 sousedních subnosičů (132 zdrojových elementů). Obsahuje dva hlavní signály: Sidelink primární synchronizační signál (S-PSS) a Sidelink sekundární synchronizační signál (S-SSS) spolu s přidruženými daty fyzického sidelink broadcastového kanálu ([PSBCH](/mobilnisite/slovnik/psbch/)). S-PSS a S-SSS usnadňují počáteční detekci časování symbolu, korekci frekvenčního posunu a identifikaci identity sidelink synchronizačního signálu (SL-SS-ID). PSBCH nese základní hlavní informační blok pro sidelink (MIB-SL), který obsahuje kritické systémové informace, jako je indikátor pokrytí sítí, přímé číslo rámce ([DFN](/mobilnisite/slovnik/dfn/)), číslo podrámce, podrobnosti konfigurace fondu zdrojů a identitu zdroje synchronizace (např. gNB, UE nebo [GNSS](/mobilnisite/slovnik/gnss/)).

Vysílání a příjem S-SSB jsou omezeny na specifické zdroje ve fondu zdrojů sidelink synchronizačních signálů, který je konfigurován vyššími vrstvami prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) nebo předkonfigurací. UE vybírá referenční synchronizační UE (SyncRef UE) na základě změřené kvality (např. [S-RSRP](/mobilnisite/slovnik/s-rsrp/)) přijatých S-SSB a indikované priority zdroje synchronizace. Dekódováním MIB-SL z PSBCH získá UE potřebné časování a minimální konfiguraci pro monitorování fyzického sidelink řídicího kanálu (PSCCH) a dekódování přiřazení plánování, čímž umožní následný přenos dat na fyzickém sidelink sdíleném kanálu (PSSCH). Návrh S-SSB, včetně jeho periodicity a šířky pásma, je optimalizován pro případy použití s nízkou latencí a vysokou spolehlivostí, jako je komunikace Vehicle-to-Everything (V2X), kde je rychlá synchronizace mezi vysoce mobilními zařízeními prvořadá.

## K čemu slouží

S-SSB byl vytvořen, aby řešil potřebu robustní a efektivní synchronizace mezi zařízeními v sidelink komunikaci založené na NR, která byla standardizována od Release 16. Předchozí sidelink založený na LTE (PC5) používal sidelink synchronizační signály (SLSS) a MasterInformationBlock-SL, ale NR sidelink vyžadoval integrovanější a flexibilnější blokovou strukturu sladěnou s NR OFDM numerologií a rámcem. Účelem S-SSB je vyřešit základní problém vytvoření společné časové a frekvenční reference mezi autonomními UE provozovanými v scénářích přímé komunikace bez nepřetržitého síťového pokrytí, jako je pokročilé V2X, sítě pro veřejnou bezpečnost a průmyslový IoT.

Řeší omezení dřívějších přístupů tím, že poskytuje jednotný blok, který nese jak synchronizační signály, tak základní broadcastové systémové informace, čímž snižuje dobu akvizice pro připojující se UE. Motivace vycházela z náročných požadavků nových sidelink případů použití, které potřebují ultra-spolehlivou komunikaci s nízkou latencí (URLLC), podporu vyšších frekvencí (včetně FR2) a vylepšená schémata přidělování zdrojů. S-SSB umožňuje škálovatelnou synchronizaci v prostředích s vysokou hustotou UE, podporuje více zdrojů synchronizace (síť, UE, GNSS) a usnadňuje bezproblémový provoz ve scénářích s plným, částečným i bez síťového pokrytí. Jeho návrh byl klíčový pro umožnění pokročilých funkcí NR sidelink, jako je polotrvalé plánování založené na snímání a skupinový přenos (groupcast) s hybridním automatickým požadavkem na opakování (HARQ feedback).

## Klíčové vlastnosti

- Skládá se z S-PSS, S-SSS a PSBCH (nese MIB-SL) v jediném bloku
- Poskytuje časovou/frekvenční synchronizaci a vysílá (broadcastuje) základní systémové informace pro sidelink
- Podporuje více numerologií a lze jej konfigurovat pro různé kmitočty nosných (FR1 a FR2)
- Umožňuje identifikaci zdroje synchronizace (gNB, UE, GNSS) a jeho priority
- Konfigurovatelná periodicita a přidělování zdrojů ve fondu sidelink synchronizačních zdrojů
- Základní prvek pro síťově řízené (režim 1) i autonomní (režim 2) přidělování sidelink zdrojů

## Související pojmy

- [PSBCH – Physical Sidelink Broadcast Channel](/mobilnisite/slovnik/psbch/)

## Definující specifikace

- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution

---

📖 **Anglický originál a plná specifikace:** [S-SSB na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-ssb/)
