---
slug: "tdma"
url: "/mobilnisite/slovnik/tdma/"
type: "slovnik"
title: "TDMA – Time Division Multiple Access"
date: 2025-01-01
abbr: "TDMA"
fullName: "Time Division Multiple Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tdma/"
summary: "Základní metoda přístupu ke kanálu, při níž více uživatelů sdílí stejné frekvenční pásmo přidělením jedinečných časových slotů. Jedná se o klíčovou techniku mnohonásobného přístupu ve 2G GSM a základn"
---

TDMA je základní metoda přístupu ke kanálu, při níž více uživatelů sdílí stejné frekvenční pásmo přidělením jedinečných časových slotů, což umožňuje efektivní využití spektra v digitálních celulárních systémech, jako je GSM.

## Popis

Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (TDMA) je metoda přístupu ke kanálu pro sítě se sdíleným přenosovým médiem. Umožňuje několika uživatelům sdílet stejný frekvenční kanál rozdělením signálu do různých časových slotů. Uživatelé vysílají v rychlém sledu za sebou, přičemž každý využívá svůj vlastní časový slot. To umožňuje více stanicím sdílet stejné přenosové médium (např. rádiový frekvenční kanál) při využití pouze části jeho kapacity. V kontextu 3GPP je TDMA synonymem pro základní rámcovou a burstovou strukturu používanou v GSM rádiovém rozhraní, což je hybridní systém TDMA/[FDMA](/mobilnisite/slovnik/fdma/). Systém využívá kombinaci FDMA (Frequency Division Multiple Access) k vytvoření více nosných frekvencí a TDMA k vytvoření více časových slotů na každé nosné.

V GSM je základní TDMA rámec dlouhý 4,615 ms a je rozdělen na 8 časových slotů (nebo 16 v konfiguracích s poloviční přenosovou rychlostí). Každý časový slot, nazývaný také burst perioda, trvá přibližně 577 mikrosekund. Logické kanály (jako kanály pro přenos hovoru a řídicí kanály pro signalizaci) jsou mapovány na tyto fyzické časové sloty. Mobilní stanici je pro její uplink a downlink komunikaci přidělen konkrétní číslo časového slotu na konkrétní nosné frekvenci. Přesná časová synchronizace v celé síti je zajištěna pomocí synchronizačních kanálů a mechanismů časového předstihu (timing advance) pro kompenzaci zpoždění šíření, čímž se zajišťuje, že bursty z různých mobilních stanic se na základnové stanici nepřekrývají.

Architektura TDMA je ústřední pro GSM rádiové rozhraní a je definována v řadách specifikací 04 a 05 (nyní udržovaných v řadě 45 pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network). Mezi klíčové komponenty patří hierarchie TDMA rámců (rámy, multirámy, superrámy, hyperrámy), různé typy burstů (Normální, Frekvenční korekce, Synchronizace, Přístupový, Dummy) a související časové struktury. Její úlohou je poskytovat strukturované, časově rozdělené médium, přes které jsou přenášeny všechny logické kanály pro hlas, data a signalizaci, což tvoří páteř 2G digitální hlasové služby a umožňuje rané paketové datové služby jako [GPRS](/mobilnisite/slovnik/gprs/).

## K čemu slouží

TDMA byla vyvinuta za účelem překonání omezení čistě analogových celulárních systémů první generace (1G) založených na [FDMA](/mobilnisite/slovnik/fdma/). Tyto analogové systémy alokovaly na celou dobu hovoru jeden vyhrazený pár frekvencí (uplink a downlink), což vedlo k neefektivnímu využití spektra, omezené kapacitě a zranitelnosti vůči odposlechu a rušení. Primární motivací pro TDMA bylo zvýšení kapacity sítě a umožnění digitálního přenosu, který nabídl lepší kvalitu hlasu, zabezpečení prostřednictvím šifrování a základ pro datové služby.

Digitalizací hlasu a rozdělením přenosu na krátké, opakující se časové sloty umožnila TDMA, aby jeden rádiový frekvenční kanál obsloužil více uživatelů (typicky 8 uživatelů s plnou přenosovou rychlostí nebo 16 s poloviční rychlostí) sekvenčně. To dramaticky zlepšilo spektrální efektivitu ve srovnání s 1G FDMA. Vytvoření digitálního standardu také usnadnilo vývoj pokročilých síťových funkcí, jako je autentizace, roaming a [SMS](/mobilnisite/slovnik/sms/). TDMA, jak je implementována v GSM, vyřešila kritický problém omezeného rádiového spektra tím, že umožnila jeho intenzivnější opětovné využití, což bylo zásadní pro masové rozšíření mobilní telefonie. Zavedla robustní, časově synchronizované digitální rádiové rozhraní, které se stalo globálním standardem pro komunikace 2G.

## Klíčové vlastnosti

- Dělí jednu rádiovou frekvenci na sekvenční časové sloty pro více uživatelů
- Umožňuje konfigurace kanálů s plnou přenosovou rychlostí (8 slotů/rámec) a poloviční rychlostí (16 slotů/rámec)
- Využívá přesný časový předstih (timing advance) pro synchronizaci vysílání mobilních stanic
- Podporuje více typů logických kanálů mapovaných na fyzické časové sloty
- Tvoří základní rámcovou strukturu pro GSM, GPRS a EDGE
- Umožňuje úsporné režimy nespojitého příjmu (DRX)

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [FDMA – Frequency Division Multiple Access](/mobilnisite/slovnik/fdma/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 26.101** (Rel-19) — Generic frame format for AMR and GSM-EFR speech codecs
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [TDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdma/)
