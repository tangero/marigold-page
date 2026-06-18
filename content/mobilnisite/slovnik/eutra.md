---
slug: "eutra"
url: "/mobilnisite/slovnik/eutra/"
type: "slovnik"
title: "EUTRA – Evolved Universal Terrestrial Radio Access"
date: 2025-01-01
abbr: "EUTRA"
fullName: "Evolved Universal Terrestrial Radio Access"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eutra/"
summary: "Rozhraní pro přenos po rádiovém kanálu (vzdušné rozhraní) a technologie rádiového přístupu definovaná pro sítě 4G LTE. Specifikuje protokoly fyzické vrstvy a vrstvy MAC pro komunikaci mezi UE a eNodeB"
---

EUTRA je rozhraní pro přenos po rádiovém kanálu (vzdušné rozhraní) a technologie rádiového přístupu pro sítě 4G LTE, která definuje protokoly fyzické vrstvy a vrstvy MAC mezi UE a eNodeB za účelem vytvoření vysokovýkonného rádiového spoje.

## Popis

Evolved Universal Terrestrial Radio Access (EUTRA) je oficiální označení 3GPP pro technologii rádiového přístupu tvořící základ Long-Term Evolution (LTE). Definuje kompletní soubor specifikací pro vrstvu 1 (fyzická vrstva) a vrstvu 2 (Medium Access Control, Radio Link Control a Packet Data Convergence Protocol) uživatelské a řídicí roviny přes rozhraní Uu mezi uživatelským zařízením (UE) a vysílačem eNodeB. EUTRA představuje čistý odklon od přístupu založeného na [CDMA](/mobilnisite/slovnik/cdma/) používaného v UMTS a přijímá pro downlink Orthogonal Frequency Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([OFDMA](/mobilnisite/slovnik/ofdma/)) a pro uplink Single-Carrier [FDMA](/mobilnisite/slovnik/fdma/) ([SC-FDMA](/mobilnisite/slovnik/sc-fdma/)).

Z architektonického hlediska je EUTRA klíčovou součástí Evolved Packet System (EPS). Funguje ve zjednodušené ploché architektuře, kde eNodeB zvládá všechny funkce související s rádiovým přístupem, včetně správy rádiových prostředků, řízení přístupu, plánování a komprese hlaviček. Fyzická vrstva EUTRA je navržena pro extrémní flexibilitu, podporuje šířky kanálů od 1,4 MHz do 20 MHz a je škálovatelná pro širší pásma pomocí agregace nosných. Využívá rámovou strukturu založenou na 1ms podrámcích a jako základní schopnost pro zvýšení datových rychlostí a spektrální účinnosti podporuje víceanténní techniky ([MIMO](/mobilnisite/slovnik/mimo/)).

Princip fungování EUTRA zahrnuje dynamické plánování v časové i frekvenční oblasti. Plánovač eNodeB přiděluje konkrétní zdrojové bloky (skupiny podnosných) různým UE každý 1ms přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/)). To umožňuje efektivní diverzitu více uživatelů a adaptivní modulaci a kódování ([QPSK](/mobilnisite/slovnik/qpsk/), 16QAM, 64QAM, 256QAM). Mezi klíčové kanály patří Physical Downlink Shared Channel (PDSCH), Physical Uplink Shared Channel (PUSCH) a robustní sada řídicích kanálů pro přiřazení plánování, hybridní ARQ potvrzení a zpětnou vazbu informací o stavu kanálu. Koncepce EUTRA minimalizuje latenci s cílem dosáhnout latence uživatelské roviny pod 10 ms a podporuje jak režim provozu Frequency Division Duplex (FDD), tak Time Division Duplex (TDD).

## K čemu slouží

EUTRA byla vytvořena, aby reagovala na rostoucí poptávku po mobilních širokopásmových datech a na omezení technologie 3G UMTS/HSPA. UMTS, založené na WCDMA, čelilo výzvám při dosahování velmi vysokých špičkových datových rychlostí a optimální spektrální účinnosti, zejména pro čistě IP paketový provoz. Primární motivací pro EUTRA bylo definovat technologii rádiového přístupu optimalizovanou pro paketová data, s výrazně vyššími datovými rychlostmi, nižší latencí, sníženými náklady na bit a větší flexibilitou ve využití spektra.

Historickým kontextem byla potřeba technologie „4G“, která by mohla konkurovat jiným vyvíjejícím se standardům, jako je WiMAX. 3GPP zahájilo studijní položku LTE, aby zajistilo dlouhodobou konkurenceschopnost rodiny 3GPP. EUTRA konkrétně cílila na překonání omezení předchozího UTRA (UMTS Terrestrial Radio Access). Opustila CDMA ve prospěch OFDMA/SC-FDMA, které jsou odolnější vůči vícecestnému rušení a lépe se hodí pro široká pásma a plánování ve frekvenční oblasti. Tento posun umožnil efektivnější podporu pokročilých anténních technologií a zjednodušil síťovou architekturu odstraněním centralizovaného řadiče rádiové sítě (RNC).

EUTRA vyřešila problém neefektivního využití spektra pro přerušovaný IP provoz. Její dynamické plánování a flexibilní přidělování šířky pásma znamenalo, že síťové prostředky mohly být přiděleny přesně tehdy a tam, kde byly potřeba, na rozdíl od přístupu s vyhrazeným kanálem používaného dříve v systémech inspirovaných přepojováním okruhů. To ji učinilo ideální pro explozi využití internetu ze smartphonů, streamování videa a další aplikace s vysokou šířkou pásma a nízkou latencí, které definovaly éru 4G.

## Klíčové vlastnosti

- OFDMA pro downlink a SC-FDMA pro uplink přenos
- Podpora flexibilních šířek pásma od 1,4 do 20 MHz (rozšiřitelné pomocí agregace nosných)
- Plochá, čistě IP architektura, kde eNodeB integruje funkce RNC
- Pokročilá podpora MIMO (až 8x8 v pozdějších verzích) jako základní funkce
- Dynamické plánování v časové a frekvenční oblasti na každý 1ms TTI
- Nízko latence koncepce s cílem dosáhnout zpoždění uživatelské roviny pod 10 ms

## Související pojmy

- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)
- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [SC-FDMA – Single Carrier – Frequency Division Multiple Access](/mobilnisite/slovnik/sc-fdma/)
- [EPS – Evolved Packet System](/mobilnisite/slovnik/eps/)

## Definující specifikace

- **TS 22.258** (Rel-7) — All-IP Network Service Requirements
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [EUTRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/eutra/)
