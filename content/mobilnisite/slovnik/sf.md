---
slug: "sf"
url: "/mobilnisite/slovnik/sf/"
type: "slovnik"
title: "SF – Shadow Fading"
date: 2026-01-01
abbr: "SF"
fullName: "Shadow Fading"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sf/"
summary: "Stínový útlum (SF) je statistický model představující rozsáhlé útlumy signálu v bezdrátových kanálech způsobené překážkami, jako jsou budovy a terén. Je klíčovou součástí modelů šíření rádiového signá"
---

SF je statistický model představující rozsáhlé útlumy signálu v bezdrátových kanálech způsobené překážkami, jako jsou budovy a terén.

## Popis

Stínový útlum, často modelovaný jako log-normálně rozdělená náhodná veličina, představuje pomalé změny síly přijímaného signálu na velké vzdálenosti nebo v důsledku významných překážek, což jej odlišuje od rychlého úniku způsobeného vícecestným šířením. Ve specifikacích 3GPP se jedná o klíčový parametr v kanálových modelech používaných pro hodnocení výkonu systému, pokrytí buňky a handoverových rezerv. Hodnota je typicky charakterizována směrodatnou odchylkou (např. 8-10 dB v městských makro scénářích) a vzdáleností prostorové korelace, která definuje, jak rychle se efekt stínění mění s polohou.

Modelování SF je nedílnou součástí vývoje realistických scénářů šíření ve standardech, jako je TR 38.901 (5G kanálový model). Používá se jak v simulacích na úrovni spoje, tak na systémové úrovni pro vyhodnocování metrik, jako je bloková chybovost, propustnost a pravděpodobnost pokrytí. Složka stínového útlumu je kombinována s modely útlumu na dráze a modely rychlého úniku za účelem vytvoření komplexních realizací kanálu, které odrážejí reálná rádiová prostředí včetně městských, příměstských, venkovských a vnitřních nasazení.

Z pohledu implementace používají nástroje pro plánování sítí a simulační platformy SF k předpovědi změn kvality signálu a zajištění spolehlivého poskytování služeb. Ovlivňuje návrh parametrů pro řízení výkonu, hysterézu předávání spojení a algoritmy výběru a převýběru buňky. Díky přesnému modelování stínového útlumu mohou operátoři optimalizovat umístění základnových stanic, konfiguraci antén a síťové parametry, aby zmírnili díry v pokrytí a interferenci, čímž zvyšují celkovou kapacitu sítě a uživatelský komfort.

## K čemu slouží

Modelování stínového útlumu existuje proto, aby zohlednilo nepředvídatelné útlumy signálu způsobené velkými překážkami v dráze šíření rádiového signálu, které nejsou zachyceny pouze deterministickými modely útlumu na dráze. Bez zohlednění SF by bylo plánování sítě příliš optimistické, což by vedlo k mezerám v pokrytí, přerušeným hovorům a špatné datové službě v oblastech zastíněných budovami, kopci nebo jinými strukturami. Jeho zařazení do standardů 3GPP zajišťuje, že hodnocení výkonu a nasazení sítí jsou založeny na realistických podmínkách kanálu.

Historická motivace vychází z potřeby přesné simulace na systémové úrovni a plánování pro celulární sítě již od éry 2G/3G. Rané modely šíření, jako je Okumura-Hata, poskytovaly střední hodnotu útlumu na dráze, ale postrádaly statistickou variabilitu. Začlenění log-normálního stínového útlumu umožnilo inženýrům modelovat náhodnou povahu blokování signálu, což umožnilo robustnější výpočty výkonnostní bilance spoje a odvození rezerv pro únik potřebných k dosažení cílové spolehlivosti pokrytí (např. 95% pokrytí na okraji buňky).

V moderních systémech 5G a novějších zůstává stínový útlum klíčový kvůli vyšším frekvencím (např. mmWave), které jsou náchylnější k blokování. Přesné modely SF jsou nezbytné pro navrhování spolehlivých strategií beamforming, komunikací s ultra spolehlivostí a nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a sítí s integrovaným přístupem a přenosovou sítí ([IAB](/mobilnisite/slovnik/iab/)). Pomáhají řešit omezení zjednodušených modelů tím, že poskytují statistický rámec odrážející reálnou geografickou a architektonickou variabilitu.

## Klíčové vlastnosti

- Modelován jako log-normálně rozdělená náhodná veličina v dB
- Charakterizován směrodatnou odchylkou (např. 4-12 dB v závislosti na prostředí)
- Zahrnuje prostorovou korelaci s definovanou dekorrelační vzdáleností
- Nedílná součást 3GPP kanálových modelů pro systémovou simulaci
- Používá se ve výpočtech výkonnostní bilance spoje pro stanovení rezervy pro únik
- Podporuje plánování sítě pro optimalizaci pokrytí a kapacity

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [SF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sf/)
