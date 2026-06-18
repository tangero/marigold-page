---
slug: "odch"
url: "/mobilnisite/slovnik/odch/"
type: "slovnik"
title: "ODCH – ODMA Dedicated Transport Channel"
date: 2025-01-01
abbr: "ODCH"
fullName: "ODMA Dedicated Transport Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/odch/"
summary: "Transportní kanál v protokolu ODMA pro UTRA TDD přenášející vyhrazené uživatelské nebo řídicí data pro konkrétní mobilní stanici. Je transportní vrstvovou obdobou logických kanálů ODTCH/ODCCH a je cha"
---

ODCH je transportní kanál v protokolu ODMA pro UTRA TDD, který přenáší vyhrazené uživatelské nebo řídicí data pro konkrétní mobilní stanici a umožňuje přenos dat v reléových spojích na základě ODMA.

## Popis

[ODMA](/mobilnisite/slovnik/odma/) Dedicated Transport Channel (ODCH) je transportní kanál definovaný v specifikacích Opportunity Driven [Multiple Access](/mobilnisite/slovnik/multiple-access/) (ODMA) pro časově duplexní ([TDD](/mobilnisite/slovnik/tdd/)) mód UMTS Terrestrial Radio Access ([UTRA](/mobilnisite/slovnik/utra/)). Transportní kanály jsou definovány způsobem přenosu dat přes rádiový interface (vrstva 1). ODCH je vyhrazený kanál, což znamená, že je přidělen jedné mobilní stanici (nebo reléovému uzlu) po dobu spojení. Přenáší data z logických kanálů vyšší vrstvy, konkrétně ODMA Dedicated Traffic Channel ([ODTCH](/mobilnisite/slovnik/odtch/)) pro uživatelská data a ODMA Dedicated Control Channel ([ODCCH](/mobilnisite/slovnik/odcch/)) pro řídicí data.

ODCH je charakterizován klíčovými atributy fyzické vrstvy typickými pro vyhrazené kanály ve systémech na základě [WCDMA](/mobilnisite/slovnik/wcdma/), včetně možnosti rychlé uzavřené regulace výkonu, dynamické adaptace přenosové rychlosti prostřednictvím výběru Transportního Formátu ([TF](/mobilnisite/slovnik/tf/)) a Kombinace Transportních Formátů (TFC) a možnosti měkkého přechodu (ač méně relevantní v kontextu TDD/ODMA). V protokolovém stacku vrstva Medium Access Control (MAC) multiplexuje jeden nebo více logických kanálů (ODTCH, ODCCH) do bloků transportních bloků ODCH. Tyto transportní bloky jsou pak zpracovávány fyzickou vrstvou prostřednictvím kanálového kódování, prokládání a mapování na fyzické kanály (např. vyhrazené fyzické kanály, DPCH) na specifických časových slotů a kódech.

Ve scénáři vícehopového ODMA existuje ODCH na každém rádiovém spoji mezi dvěma uzly v reléovém řetězci (např. z Node B na Relay UE, nebo mezi dvěma Relay UE). Každý ODCH podporuje obousměrný tok dat a řízení pro daný segment spoje. Správa ODCH, včetně jeho vytvoření, udržování a uvolnění, je řízena protokoly vyšší vrstvy (RRC) na základě měření a dynamických rozhodnutí routování protokolu ODMA. ODCH reprezentuje standardizovaný transportní prostředek pro data v inovativním, ale převážně nerealizovaném, ad-hoc síťovém rozšíření ODMA pro UMTS.

## K čemu slouží

ODCH byl vytvořen, aby poskytoval standardizovaný transportní mechanismus pro vyhrazené toky uživatelských a řídicích dat v architektuře vícehopového reléování ODMA pro UTRA TDD. Hlavním účelem ODMA bylo umožnit uživatelským zařízením fungovat jako relé, rozšiřovat síťové pokrytí a vytvářet alternativní routování. To vyžadovalo vyhrazené, řízené transportní kanály pro každý spoj v vícehopovém spojení, což ODCH poskytuje.

Řešil problém, jak efektivně a spolehlivě přenášet zapouzdřená uživatelská data a nezbytné řídicí signalizaci přes každý jednotlivý rádiový spoj v dynamickém vícehopovém řetězci. Použití vyhrazeného transportního kanálu umožnilo systému aplikovat optimalizace specifické pro spoj, jako rychlá regulace výkonu a adaptivní kódování/modulace (prostřednictvím výběru Transportního Formátu), které jsou klíčové pro udržení kvality spoje v potenciálně interferenčně bohatém peer-to-peer prostředí. Bez definovaného transportního kanálu jako ODCH by přenos fyzické vrstvy pro ODMA spoje byl nestandardizovaný a neefektivní.

Vývoj ODCH ve Release 99 byl částí širšího úsilí o zkoumání pokročilých technik rádiového přístupu. Ač ODMA samo bylo ambiciózním pokusem o integrované ad-hoc síťování, které nedosáhlo komerčního úspěchu, práce na vyhrazených transportních kanálech pro point-to-point spoje v rámci buněčného frameworku přispěla k pochopení transportu relé, což se následně odrazilo v designu transportních kanálů pro LTE relé a sidelink interface (PC5) pro ProSe a V2X, kde vyhrazené prostředky pro komunikaci mezi zařízeními jsou nezbytné.

## Klíčové vlastnosti

- Vyhrazený transportní kanál pro jednotného uživatele/spojení v ODMA
- Přenáší transportní bloky z logických kanálů ODTCH (provoz) a ODCCH (řízení)
- Podporuje rychlou regulaci výkonu a dynamický výběr kombinace transportních formátů
- Charakterizován přenosovým časovým intervalem (TTI) a parametry kódování/zpracování
- Mapován fyzickou vrstvou na vyhrazené fyzické kanály v TDD časových slotů
- Základní pro transport dat na každém hopu v vícehopovém reléovém spoji ODMA

## Související pojmy

- [ODMA – Opportunity Driven Multiple Access](/mobilnisite/slovnik/odma/)
- [ODCCH – ODMA Dedicated Control Channel](/mobilnisite/slovnik/odcch/)
- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN

---

📖 **Anglický originál a plná specifikace:** [ODCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/odch/)
