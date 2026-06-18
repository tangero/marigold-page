---
slug: "odcch"
url: "/mobilnisite/slovnik/odcch/"
type: "slovnik"
title: "ODCCH – ODMA Dedicated Control Channel"
date: 2025-01-01
abbr: "ODCCH"
fullName: "ODMA Dedicated Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/odcch/"
summary: "Logický řídicí kanál v protokolu ODMA (Opportunity Driven Multiple Access), který je součástí režimu TDD v UTRA. Přenáší vyhrazenou řídicí signalizaci pro konkrétní mobilní stanici, jako jsou příkazy"
---

ODCCH je logický řídicí kanál v protokolu ODMA, který přenáší vyhrazené řídicí signalizaci, jako jsou příkazy pro řízení výkonu, pro konkrétní mobilní stanici přes rozhraní rádiového přenosu.

## Popis

[ODMA](/mobilnisite/slovnik/odma/) Dedicated Control Channel (ODCCH) je logický kanál definovaný v rámci protokolu Opportunity Driven [Multiple Access](/mobilnisite/slovnik/multiple-access/) (ODMA), který byl specifikován pro režim Time Division Duplex ([TDD](/mobilnisite/slovnik/tdd/)) v UMTS Terrestrial Radio Access ([UTRA](/mobilnisite/slovnik/utra/)). ODMA byl koncept pro vícecestný přenos (multi-hop relaying), kde uživatelská zařízení (UE) mohla fungovat jako přenosové stanice (relay) pro rozšíření pokrytí nebo kapacity sítě. ODCCH je bod-bodový obousměrný kanál odpovědný za přenos vyhrazené řídicí signalizace mezi sítí (nebo přenosovým uzlem) a konkrétní mobilní stanicí. V kontextu ODMA je mapován na vyhrazený transportní kanál (Dedicated Transport Channel, [DCH](/mobilnisite/slovnik/dch/)).

V architektuře protokolu UTRA TDD (vrstva 2 a vrstva 1) jsou logické kanály, jako je ODCCH, definovány typem informací, které přenášejí. ODCCH přenáší řídicí informace specifické pro konkrétní spojení UE, jako jsou příkazy pro řízení vysílacího výkonu (Transmit Power Control, [TPC](/mobilnisite/slovnik/tpc/)), indikátor kombinace transportního formátu (Transport Format Combination Indicator, [TFCI](/mobilnisite/slovnik/tfci/)) a další řídicí signály fyzické vrstvy nezbytné pro udržování vyhrazeného spoje. Funguje spolu s ODMA Dedicated Traffic Channel ([ODTCH](/mobilnisite/slovnik/odtch/)), který přenáší uživatelská data. ODCCH je zřizován a uvolňován ve spojení s vyhrazeným datovým kanálem jako součást procedur nastavení a správy rádiového přenosového prostředku (radio bearer).

Kanál funguje v rámci vrstvy řízení přístupu k médiu (Medium Access Control, MAC) a vrstvy řízení rádiového spoje (Radio Link Control, RLC). Vrstva MAC je odpovědná za mapování logických kanálů, jako je ODCCH, na transportní kanály. V kontextu ODMA/TDD toto mapování zahrnuje specifickou alokaci časových slotů a kódů. Informace na ODCCH jsou klíčové pro adaptaci spoje, řízení výkonu a synchronizaci v dynamickém a potenciálně vícecestném prostředí, jaké koncept ODMA předpokládal. Přestože byly ODMA a její přidružené kanály, jako je ODCCH, standardizovány, došlo k jejich velmi omezenému komerčnímu nasazení a koncepty později ovlivnily výzkum přenosových stanic (relay) a komunikace zařízení-zařízení (device-to-device, D2D) pro LTE a 5G.

## K čemu slouží

ODCCH byl vytvořen jako součást architektury ODMA pro podporu vyhrazené, spojení orientované řídicí signalizace ve vícecestném ad-hoc rozšíření rádiové přístupové sítě UMTS TDD. Primární motivací pro ODMA bylo zlepšit pokrytí, zejména na okrajích buněk, a zvýšit kapacitu tím, že uživatelské terminály mohly přenášet provoz jeden pro druhého a vytvářet tak dynamickou síť. To vyžadovalo robustní řídicí mechanismy pro správu každého vyhrazeného přenosového spoje, což je úloha ODCCH.

Řešil potřebu přesného, na spojení specifického řízení ve scénáři, kde tradiční přímý spoj mezi Node B a UE mohl být přerušený nebo neoptimální. Ve vícecestném řetězci vyžaduje každý skok vlastní řídicí smyčku pro řízení výkonu, časový předstih (timing advance) a zpětnou vazbu o kvalitě spoje. ODCCH poskytoval standardizovaný logický kanál pro přenos těchto na skok specifických řídicích informací, což zajišťovalo spolehlivý provoz vyhrazeného datového kanálu (ODCH/ODTCH). Bez takového vyhrazeného řídicího kanálu by správa dynamických rádiových spojů v ad-hoc přenosové síti byla neefektivní a nespolehlivá.

Historicky ODMA a ODCCH představovaly raný pokus 3GPP o standardizaci ad-hoc sítí a přenosů (relaying) v rámci buněčných systémů. I když konkrétní režim ODMA/TDD nebyl široce nasazen, práce na vyhrazených řídicích kanálech pro spravované peer-to-peer spoje poskytla cenné základní koncepty pro pozdější technologie, jako jsou přenosové stanice (Relays) v LTE a Integrated Access and Backhaul (IAB) a sidelink (PC5) komunikace v 5G NR, kde zůstávají vyhrazené řídicí kanály pro přenosové spoje nezbytné.

## Klíčové vlastnosti

- Bod-bodový logický řídicí kanál pro vyhrazená spojení UE
- Přenáší na UE specifické řídicí informace: příkazy TPC, TFCI, informace pro synchronizaci
- Definován specificky pro protokol ODMA v režimu UTRA TDD
- Obousměrný kanál (uplink a downlink)
- Mapován na vyhrazený transportní kanál (DCH) pro přenos
- Nezbytný pro správu rádiového spoje ve vícecestných scénářích ODMA

## Související pojmy

- [ODMA – Opportunity Driven Multiple Access](/mobilnisite/slovnik/odma/)
- [ODCH – ODMA Dedicated Transport Channel](/mobilnisite/slovnik/odch/)
- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN

---

📖 **Anglický originál a plná specifikace:** [ODCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/odcch/)
