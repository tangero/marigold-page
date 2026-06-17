---
slug: "epdcch"
url: "/mobilnisite/slovnik/epdcch/"
type: "slovnik"
title: "EPDCCH – Enhanced Physical Downlink Control Channel"
date: 2025-01-01
abbr: "EPDCCH"
fullName: "Enhanced Physical Downlink Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/epdcch/"
summary: "Řídicí kanál v LTE a 5G NR používaný k přenosu řídicích informací v downlinku (DCI), jako jsou přiřazení zdrojů a příkazy pro řízení výkonu. Vylepšuje původní PDCCH tím, že nabízí vyšší kapacitu, plán"
---

EPDCCH je vylepšený řídicí kanál v LTE a 5G NR, který přenáší řídicí informace v downlinku a nabízí oproti původnímu PDCCH vyšší kapacitu a plánování ve frekvenční oblasti.

## Popis

Enhanced Physical Downlink Control Channel (EPDCCH) je kanál fyzické vrstvy zavedený v LTE Release 11 a používaný v následujících verzích včetně 5G NR. Představuje vývoj oproti Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) a přenáší Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) ze základnové stanice (eNodeB v LTE, gNB v NR) do uživatelského zařízení (UE). DCI zahrnuje kritická data, jako jsou přiřazení bloků zdrojů, schémata modulace a kódování a příkazy pro řízení výkonu. EPDCCH vylepšuje PDCCH tím, že funguje ve frekvenční oblasti, což umožňuje flexibilnější alokaci zdrojů a lepší výkon v heterogenních sítích.

Z architektonického hlediska je EPDCCH mapován na fyzické bloky zdrojů (PRB) v rámci downlinkového rámce LTE nebo NR, na rozdíl od PDCCH, který zabírá prvních několik [OFDM](/mobilnisite/slovnik/ofdm/) symbolů subframu. Funguje tak, že dostupné PRB rozděluje do sad, které lze nakonfigurovat pro různá UE nebo účely. Kanál používá pro koherentní detekci referenční signály pro demodulaci ([DM-RS](/mobilnisite/slovnik/dm-rs/)), což umožňuje přesný odhad kanálu a vyšší spolehlivost. Mezi klíčové součásti patří sady EPDCCH, prohledávací prostory (kde UE monitorují potenciální DCI) a vylepšené řídicí kanálové elementy (ECCE), které agregují zdroje pro robustní přenos.

Během provozu síť konfiguruje parametry EPDCCH pomocí signalizace vyšší vrstvy ([RRC](/mobilnisite/slovnik/rrc/)), přičemž specifikuje PRB a úrovně agregace. UE provádí ve svém prohledávacím prostoru slepou dekódaci, aby detekovala DCI určená pro něj. Tento proces podporuje plánování ve frekvenční oblasti, což znamená, že řídicí informace mohou být umístěny v optimálních frekvenčních pozicích, aby se zabránilo interferenci nebo přizpůsobily podmínkám kanálu UE. Role EPDCCH je klíčová pro funkce jako agregace nosných, koordinovaný vícebodový přenos (CoMP) a vylepšená koordinace mezibuněčné interference (eICIC), protože poskytuje vyšší kapacitu a spolehlivější řídicí signalizaci než PDCCH, zejména v hustých nasazeních nebo v prostředí s omezenou interferencí.

## K čemu slouží

EPDCCH byl vyvinut, aby řešil omezení původního [PDCCH](/mobilnisite/slovnik/pdcch/) v sítích LTE. PDCCH byl omezen na prvních několik [OFDM](/mobilnisite/slovnik/ofdm/) symbolů subframu a používal buněčně specifické referenční signály, což omezovalo jeho kapacitu a flexibilitu. Jak se LTE vyvíjelo s funkcemi jako agregace nosných a heterogenní sítě, rostla potřeba více zdrojů pro řídicí kanál a lepšího řízení interference.

Historický kontext zahrnuje zavedení LTE-Advanced (Release 10), kde zvýšené přenosové rychlosti a hustota sítě zvýraznily omezení PDCCH. EPDCCH je vyřešil přesunutím řídicí signalizace do datové oblasti, což umožnilo plánování ve frekvenční oblasti a použití UE-specifických referenčních signálů. To umožnilo efektivnější využití zdrojů a snížilo blokování řídicího kanálu.

Motivace pro jeho vytvoření zahrnují podporu pokročilých funkcí LTE, jako je vylepšený [MIMO](/mobilnisite/slovnik/mimo/), CoMP a eICIC. Tím, že poskytl vyšší kapacitu a lepší odolnost vůči interferenci, EPDCCH usnadnil nasazení v malých buňkách a přelidněných městských oblastech. Také připravil cestu pro návrh řídicího kanálu 5G NR a ovlivnil koncepty jako NR Physical Downlink Control Channel (NR-PDCCH). EPDCCH tedy představuje klíčový krok ve vývoji mobilních sítí směrem k vyšší efektivitě a škálovatelnosti.

## Klíčové vlastnosti

- Alokace zdrojů ve frekvenční oblasti využívající PRB
- UE-specifické referenční signály pro demodulaci (DM-RS)
- Podpora až 2 sad EPDCCH na jedno UE
- Vylepšená kapacita ve srovnání s původním PDCCH
- Lepší koordinace interference díky frekvenční selektivitě
- Kompatibilita s funkcemi LTE-Advanced, jako je agregace nosných

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)

## Definující specifikace

- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [EPDCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/epdcch/)
