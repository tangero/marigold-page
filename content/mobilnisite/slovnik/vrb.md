---
slug: "vrb"
url: "/mobilnisite/slovnik/vrb/"
type: "slovnik"
title: "VRB – Virtual Resource Block"
date: 2025-01-01
abbr: "VRB"
fullName: "Virtual Resource Block"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/vrb/"
summary: "Logický blok zdrojů používaný v LTE a NR pro plánování a mapování v downlinku a uplinku. Poskytuje flexibilní mapování mezi logickou alokací zdrojů, jak ji vidí vyšší vrstvy, a skutečnými fyzickými bl"
---

VRB (Virtual Resource Block, virtuální blok zdrojů) je logický blok zdrojů používaný v plánování LTE a NR, který poskytuje flexibilní mapování mezi alokacemi zdrojů vyšších vrstev a skutečnými fyzickými bloky zdrojů vysílanými na rozhraní vzdušného rozhraní.

## Popis

Virtual Resource Block (VRB, virtuální blok zdrojů) je základní koncept ve specifikacích fyzické vrstvy LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio) pro alokaci zdrojů. Funguje jako mezilehlé logické schéma indexování mezi přiděleními zdrojů od plánovače vyšší vrstvy a skutečnými fyzickými bloky zdrojů ([PRB](/mobilnisite/slovnik/prb/)), které přenášejí modulované symboly přes vzdušné rozhraní. Plánovač pracuje s VRB a mapovací funkce, definovaná ve specifikacích, překládá tyto indexy VRB na indexy PRB pro přenos. Tato abstrakce je klíčová pro podporu různých přenosových schémat, především lokalizovaného a distribuovaného přenosu. Při lokalizovaném přenosu je souvislá sada VRB mapována přímo na souvislou sadu PRB, což je efektivní pro frekvenčně selektivní plánování, kdy je známa kvalita kanálu. Při distribuovaném přenosu je sada VRB mapována na nesouvislé PRB rozprostřené po šířce pásma systému. To poskytuje frekvenční diverzitu, což je prospěšné pro řídicí kanály, vysílací kanály a uživatelská data, když jsou informace o kvalitě kanálu nespolehlivé nebo pro scénáře s vysokou mobilitou.

Mapovací proces je standardizovaný a známý jak gNB/[eNB](/mobilnisite/slovnik/enb/), tak UE. Pro downlink specifikace definují dva typy VRB: lokalizované VRB a distribuované VRB. Typ je indikován v downlink control information ([DCI](/mobilnisite/slovnik/dci/)). Mapování pro distribuované VRB zahrnuje proces prokládání pro dosažení frekvenčního oddělení. Pro uplink v LTE existuje podobný koncept s některými rozdíly, jako je použití clustered DFT-s-OFDM, kde VRB mohou být mapovány na nesouvislé shluky PRB. V NR je koncept rozšířen o ještě flexibilnější struktury alokace zdrojů, podporující jak souvislé, tak nesouvislé alokace pro různé typy vlnových forem ([CP-OFDM](/mobilnisite/slovnik/cp-ofdm/) a DFT-s-OFDM).

Role VRB je nedílnou součástí interakce mezi vrstvou [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control) a fyzickou vrstvou ([PHY](/mobilnisite/slovnik/phy/)). Vrstva MAC přijímá nebo vytváří rozhodnutí o plánování z hlediska VRB. Fyzická vrstva následně aplikuje přesné mapování VRB na PRB, přidá referenční signály a provede potřebnou modulaci a kódování. Toto oddělení zjednodušuje návrh plánovače a umožňuje pokročilé funkce, jako je frekvenční hopping, kde se mapování PRB v čase mění podle předdefinovaného vzoru, což dále zvyšuje diverzitu nebo randomizaci interference. Velikost VRB, stejně jako PRB, je definována jako 12 po sobě jdoucích subnosných ve frekvenční doméně pro jeden přenosový časový interval (např. slot nebo subframe).

## K čemu slouží

Koncept VRB byl zaveden, aby oddělil logickou alokaci zdrojů používanou pro plánování od fyzického mapování zdrojů na rádiovém rozhraní. Před LTE systémy jako UMTS používaly vyhrazené kanály nebo alokaci zdrojů založenou na kódech, kterým chybělo jemně odstupňované, flexibilní plánování ve frekvenční doméně, které umožňují [OFDMA](/mobilnisite/slovnik/ofdma/)/SC-FDMA. Abstrakce VRB řeší problém efektivní podpory více schémat alokace zdrojů v rámci jednotného rámce. Umožňuje síti volit mezi frekvenčně selektivním plánováním (použitím lokalizovaného mapování pro špičkovou propustnost) a plánováním s frekvenční diverzitou (použitím distribuovaného mapování pro robustnost) bez změny základního rozhraní pro plánování.

Tato flexibilita byla klíčovým designovým cílem LTE pro podporu širokého spektra scénářů nasazení, stavů mobility uživatelů a požadavků služeb. Pro řídicí kanály jako PDCCH je distribuovaný přenos přes VRB nezbytný pro zajištění spolehlivého příjmu napříč buňkou. Pro uživatelská data může plánovač dynamicky vybírat nejlepší mapování na základě indikátorů kvality kanálu (CQI) hlášených UE. Mechanismus VRB také zajistil budoucí odolnost návrhu, umožňující zavedení nových přenosových režimů v pozdějších releasech (jako Transmit Diversity nebo Multi-User MIMO), které spoléhají na specifická mapování PRB, aniž by to ovlivnilo protokoly vyšších vrstev. Je to základní kámen efektivního využití zdrojů, který definuje rádiové přístupové sítě 4G a 5G.

## Klíčové vlastnosti

- Logická abstraktní vrstva mezi plánovačem a fyzickým přenosem
- Podporuje dva hlavní typy mapování: lokalizované a distribuované
- Umožňuje frekvenčně selektivní plánování pro vysokou propustnost
- Umožňuje přenos s frekvenční diverzitou pro robustnost
- Základ pro vzorce frekvenčního hopingu
- Standardizované mapování známé jak vysílači, tak přijímači

## Související pojmy

- [PRB – Physical Resource Block](/mobilnisite/slovnik/prb/)
- [RB – Resource Block](/mobilnisite/slovnik/rb/)
- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [SC-FDMA – Single Carrier – Frequency Division Multiple Access](/mobilnisite/slovnik/sc-fdma/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding

---

📖 **Anglický originál a plná specifikace:** [VRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/vrb/)
