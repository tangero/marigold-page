---
slug: "pcpch"
url: "/mobilnisite/slovnik/pcpch/"
type: "slovnik"
title: "PCPCH – Physical Common Packet Channel"
date: 2025-01-01
abbr: "PCPCH"
fullName: "Physical Common Packet Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pcpch/"
summary: "Výstupní (uplink) fyzický kanál WCDMA používaný v UMTS (3G) pro přenos paketových dat. Umožňuje více uživatelským zařízením (UE) sdílet prostředky kanálu pro efektivní přenos trhavých dat, přičemž o p"
---

PCPCH je výstupní (uplink) fyzický kanál WCDMA v UMTS používaný pro paketová data, kde více uživatelských zařízení (UE) sdílí prostředky prostřednictvím náhodného přístupu pro efektivní přenos trhavého provozu.

## Popis

Physical Common Packet Channel (PCPCH) je výstupní (uplink) přenosový kanál v rádiovém rozhraní UMTS (Universal Mobile Telecommunications System) [WCDMA](/mobilnisite/slovnik/wcdma/) (Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)). Je namapován na konkrétní fyzický kanál používaný pro přenos paketových uživatelských dat z uživatelského zařízení (UE) do Node B (základnové stanice). Na rozdíl od vyhrazených kanálů je PCPCH sdílený kanál, což znamená, že jeho prostředky (rozprostírací kódy, výkon) nejsou trvale přiděleny jednomu UE, ale jsou o ně soutěženo více UE potřebujícími odeslat data, což je efektivní pro trhavý provoz s nízkou až střední přenosovou rychlostí.

Provoz PCPCH zahrnuje vícekrokovou proceduru náhodného přístupu. UE s daty k odeslání nejprve naslouchá kanálu Access Preamble Capture Indicator ([AICH](/mobilnisite/slovnik/aich/)), aby zjistilo dostupnost. Poté vysílá sérii přístupových preambulí s rostoucím výkonem na specifický signaturu. Po jejich detekci Node B odpoví pomocí Acquisition Indicator ([AI](/mobilnisite/slovnik/ai/)) na AICH. Po úspěšném zachycení preambule vysílá UE Collision Detection ([CD](/mobilnisite/slovnik/cd/)) preambuli. Pokud není indikována kolize (prostřednictvím kanálu CD Indication Channel, CDICH), pokračuje UE v odesílání svého datového paketu na PCPCH po omezenou dobu, s použitím specifického rozprostíracího kódu přiděleného během přístupové procedury. Tento proces řídí soutěž o prostředky a snižuje pravděpodobnost kolizí datových paketů.

Z architektonického hlediska existuje PCPCH ve vrstvě 1 (fyzické vrstvě) a je řízen protokoly vyšších vrstev v [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control) a [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control). Mezi klíčové zapojené komponenty patří AICH a CDICH pro signalizaci a specifické kanalizační a skramblovací kódy, které definují PCPCH. Jeho úlohou bylo poskytovat efektivní cestu s nízkou režií pro výstupní (uplink) paketová data, doplňující vyhrazené kanály ([DCH](/mobilnisite/slovnik/dch/)), které byly vhodnější pro souvislé datové toky s vysokou rychlostí, ale méně efektivní pro sporadické přenosy.

## K čemu slouží

PCPCH byl vytvořen, aby řešil potřebu efektivního přenosu výstupních (uplink) paketových dat v UMTS, což byla klíčová evoluce oproti datům s přepojováním okruhů v 2G. Rané služby 3G počítaly nejen s hlasem, ale také s nově vznikajícími internetovými aplikacemi, které často generují trhavý, asymetrický datový provoz (např. prohlížení webu, instant messaging). Přidělení vyhrazeného kanálu s konstantním výkonem a kódem pro takový provoz by bylo velmi neefektivní z hlediska využití stromu kódů a výstupního rušení.

PCPCH to řešil zavedením soutěžního modelu sdíleného kanálu inspirovaného principy sítí s náhodným přístupem. Umožnil síti obsloužit mnoho uživatelů se sporadickými datovými potřebami pomocí společného fondu prostředků, což dramaticky zlepšilo zisky statistického multiplexování a celkovou kapacitu výstupního směru. Řešil tak omezení použití pouze vyhrazených kanálů, které byly pro paketová data náročné na prostředky, a RACH (Random Access Channel), který byl navržen pro velmi krátké signalizační zprávy, nikoli pro souvislý přenos dat. PCPCH byl základním stavebním kamenem pro služby s přepojováním paketů v UMTS, umožňujícím responsivnější a efektivnější mobilní data před nástupem HSPA, které přineslo pokročilejší sdílené kanály.

## Klíčové vlastnosti

- Výstupní (uplink) sdílený fyzický kanál pro paketová data ve WCDMA/UMTS
- Používá soutěžní proceduru náhodného přístupu s detekcí kolizí
- Prostředky jsou dočasně přidělovány na každý paketový burst
- Zahrnuje Access Preambles, AICH a CDICH pro signalizaci
- Efektivní pro sporadický a trhavý provoz z více UE
- Definován specifickými kanalizačními kódy a skramblovacími kódy

## Související pojmy

- [AICH – Acquisition Indication Channel](/mobilnisite/slovnik/aich/)
- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [PCPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcpch/)
