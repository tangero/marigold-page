---
slug: "rnsap"
url: "/mobilnisite/slovnik/rnsap/"
type: "slovnik"
title: "RNSAP – Radio Network Subsystem Application Part"
date: 2025-01-01
abbr: "RNSAP"
fullName: "Radio Network Subsystem Application Part"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rnsap/"
summary: "Signalizační protokol používaný v sítích UMTS a GSM pro řízení komunikace mezi podsystémy rádiové sítě (RNS), konkrétně mezi řadiči rádiové sítě (RNC). Zajišťuje funkce jako měkké předávání hovoru, re"
---

RNSAP je signalizační protokol používaný v sítích UMTS a GSM pro řízení komunikace mezi řadiči rádiové sítě (RNC) při funkcích, jako je měkký předávání hovoru (soft handover), přesun služby (relokace) a správa zdrojů.

## Popis

Radio Network Subsystem Application Part (RNSAP) je klíčový signalizační protokol definovaný konsorciem 3GPP pro sítě UMTS (a adaptovaný pro GSM), který funguje na rozhraní Iur mezi řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v různých podsystémech rádiové sítě ([RNS](/mobilnisite/slovnik/rns/)). RNS se skládá z jednoho RNC a jemu podřízených Node B (základnových stanic) a RNSAP umožňuje koordinaci mezi těmito podsystémy pro podporu mobility a správy zdrojů. Protokol je součástí rodiny Radio Access Network Application Part ([RANAP](/mobilnisite/slovnik/ranap/)) a pro výměnu zpráv mezi RNC využívá transportní mechanismy nižších vrstev, jako je Signalling Connection Control Part ([SCCP](/mobilnisite/slovnik/sccp/)) přes IP nebo [ATM](/mobilnisite/slovnik/atm/). Jeho primární úlohou je umožňovat procedury vyžadující komunikaci mezi RNC a zajistit, aby uživatelské zařízení (UE) se mohlo plynule pohybovat mezi buňkami řízenými různými RNC bez přerušení služby.

RNSAP funguje tak, že definuje soubor elementárních procedur a zpráv pokrývajících různé scénáře. Mezi klíčové funkce patří správa rádiových spojů během měkkého předávání hovoru, kdy UE komunikuje s více Node B napříč různými RNS; RNSAP koordinuje přidání, odstranění a modifikaci rádiových spojů za účelem udržení kvality hovoru. Dále zajišťuje přesun služby ([SRNS](/mobilnisite/slovnik/srns/) relocation), který přenáší roli obsluhujícího RNC z jednoho RNC na jiné v důsledku mobility UE, a zahrnuje přenos kontextu a přerozdělení zdrojů. RNSAP také řídí hlášení měření, koordinaci pagingu a správu společných kanálů, což umožňuje efektivní využití rádiových zdrojů a vyrovnávání zatížení v síti. Protokol pracuje na principu požadavek-odpověď, přičemž zprávy jako RADIO LINK SETUP REQUEST a RELOCATION REQUIRED iniciují procedury a odpovídající potvrzení nebo chyby je dokončují.

Architektura RNSAP je vrstvená, přičemž aplikační část spoléhá na podkladový signalizační transport. Zahrnuje mechanismy pro zpracování chyb, jako jsou časovače a opakované přenosy, aby byla zajištěna spolehlivost. Ve specifikacích, jako je 25.423, je RNSAP detailně popsán s informačními elementy, které kódují parametry jako identifikátory UE, konfigurace rádiových zdrojů a výsledky měření. Jeho vývoj přinesl vylepšení pro interoperabilitu s pozdějšími technologiemi, ale jeho jádro zůstává klíčové pro sítě UMTS. Díky umožnění koordinace mezi RNC podporuje RNSAP klíčové vlastnosti, jako je makro diverzita při měkkém předávání hovoru, která zlepšuje pokrytí a snižuje počet přerušených hovorů, a tím přispívá k celkovému výkonu a spolehlivosti sítí 3G rádiového přístupu.

## K čemu slouží

RNSAP byl vytvořen pro potřeby koordinované signalizace mezi podsystémy rádiové sítě ([RNS](/mobilnisite/slovnik/rns/)) v sítích UMTS, které zavedly distribuovanou architekturu s více [RNC](/mobilnisite/slovnik/rnc/). Před UMTS spoléhaly sítě GSM na jednodušší mechanismy předávání hovoru mezi řadiči základnových stanic (BSC), ale měkké předávání hovoru a těsnější integrace v UMTS vyžadovaly vyhrazený protokol pro komunikaci mezi RNC. Bez RNSAP by bylo řízení mobility přes hranice RNS neefektivní, což by vedlo k přerušením služby, zvýšené signalizační režii a suboptimálnímu využití zdrojů při pohybech UE.

Protokol řeší problémy spojené s plynulou mobilitou, zejména ve scénářích, kdy je UE v režimu měkkého předávání hovoru mezi Node B řízenými různými RNC. Umožňuje procedury, jako je přidání rádiového spoje a přesun služby (SRNS relocation), a zajišťuje, že UE udržuje nepřetržité připojení bez přerušení hovoru. RNSAP navíc usnadňuje vyrovnávání zatížení a optimalizaci zdrojů tím, že umožňuje RNC sdílet data měření a koordinovat přidělování kanálů. Jeho vývoj byl motivován složitostí rádiového rozhraní UMTS založeného na WCDMA, které těží z makro diverzity a vyžaduje přesné časování a synchronizaci mezi více body.

Historicky zavedení RNSAP ve verzi 3GPP R99 položilo základy pro pokročilé funkce mobility v sítích 3G a podpořilo přechod od služeb s přepojováním okruhů k službám s přepojováním paketů. Vyřešilo omezení dřívějších protokolů, kterým chyběla podrobnost pro signalizaci mezi RNC, a umožnilo tak škálovatelné a robustní rádiové přístupové sítě. Jak se sítě vyvíjely směrem k 4G a 5G, koncepty z RNSAP ovlivnily pozdější protokoly, jako je X2-AP v LTE, ale RNSAP zůstává nezbytný pro stávající nasazení UMTS.

## Klíčové vlastnosti

- Řídí signalizaci na rozhraní Iur mezi RNC
- Podporuje procedury měkkého předávání hovoru s koordinací rádiových spojů
- Zajišťuje přesun služby (Serving RNS relocation) pro mobilitu UE
- Usnadňuje hlášení měření a správu zdrojů
- Používá transport založený na SCCP pro spolehlivé doručování zpráv
- Definuje elementární procedury pro komunikaci mezi RNC

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.471** (Rel-19) — RNSAP User Adaptation (RNA) for Iurh
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.130** (Rel-19) — Iur-g Interface Overview
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [RNSAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rnsap/)
