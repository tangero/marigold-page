---
slug: "osdd"
url: "/mobilnisite/slovnik/osdd/"
type: "slovnik"
title: "OSDD – OTA Sensitivity Directions Declaration"
date: 2025-01-01
abbr: "OSDD"
fullName: "OTA Sensitivity Directions Declaration"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/osdd/"
summary: "Mechanismus hlášení schopností UE pro testování přes vzduch (OTA). Deklaruje směry citlivosti (např. azimut a elevace), kde je anténní výkon UE optimální, což je klíčové pro přesné testování vyzařovan"
---

OSDD je mechanismus hlášení schopností UE, který deklaruje směry citlivosti, jako jsou azimut a elevace, kde je anténní výkon UE optimální pro přesné OTA testování.

## Popis

Deklarace směrů citlivosti pro [OTA](/mobilnisite/slovnik/ota/) (OSDD) je standardizovaná schopnost UE definovaná 3GPP pro metodiky testování přes vzduch (OTA). Je to kritická součást rámce pro testování vyzařovaného výkonu, která umožňuje charakterizaci celkového vyzařovaného výkonu ([TRP](/mobilnisite/slovnik/trp/)) a celkové izotropní citlivosti (TIS) zařízení v řízeném prostředí bezodrazové komory. OSDD poskytuje testovacímu systému strukturovanou sadu dat z UE, která detailně popisuje konkrétní prostorové směry – typicky definované azimutem a elevací – kde je citlivost přijímače zařízení nejvyšší. Tyto informace jsou zásadní, protože anténní systém UE není dokonale izotropní; jeho výkon se významně mění v závislosti na směru kvůli formátu zařízení, umístění vnitřních antén a scénářům interakce s uživatelem (jako je úchyt rukou).

Během OTA testování je testované zařízení ([DUT](/mobilnisite/slovnik/dut/)) umístěno na pozicionovacím systému uvnitř bezodrazové komory. Testovací sondová anténa vysílá nebo přijímá signály a DUT je otáčeno do různých orientací. Schopnost OSDD umožňuje testovacímu systému inteligentně zaměřit své měřicí průchody na deklarované směry citlivosti, namísto provádění vyčerpávajících a časově náročných sférických skenů. Deklarace typicky obsahuje seznam směrových vektorů, z nichž každý je asociován s konkrétním provozním pásmem a případně dalšími rádiovými podmínkami. Testovací systém tato data používá ke konfiguraci útlumu měřicí trasy, nastavení správných vah beamformingu (je-li aplikovatelné) a určení přesných úhlových pozic pro měření citlivosti.

Architektonicky je OSDD součástí specifikací pro rádiový přenos a příjem UE (např. řady 36.101/38.101) a souvisejících specifikací testů shody (např. 36.521/38.521). UE ji hlásí během procedur výměny schopností, často jako součást RF-Parameters. Podkladový mechanismus zahrnuje interní charakterizaci anténního výkonu ze strany základnového pásma a [RF](/mobilnisite/slovnik/rf/) systémů UE, případně na základě tovární kalibrace nebo odhadu v reálném čase. Role OSDD přesahuje pouhou efektivitu testování; zajišťuje reprodukovatelnost a přesnost metrik vyzařovaného výkonu, které jsou klíčové pro regulační shodu (např. [FCC](/mobilnisite/slovnik/fcc/), [CE](/mobilnisite/slovnik/ce/) značení) a pro garantování reálného uživatelského zážitku, jelikož pokrytí a datová propustnost zařízení přímo souvisí s jeho OTA charakteristikami.

## K čemu slouží

OSDD byla zavedena, aby řešila rostoucí komplexitu a kritičnost přesného měření vyzařovaného výkonu moderního uživatelského zařízení (UE), zejména s příchodem [MIMO](/mobilnisite/slovnik/mimo/), agregace nosných a později beamformingu v mmWave pásmech v 5G NR. Tradiční konduktivní testování, kdy jsou kabely připojeny přímo k anténním portům, se stalo nedostatečným, protože ignorovalo vliv krytu zařízení, integrovaných antén a blízkosti uživatele – což vše radikálně mění reálný [RF](/mobilnisite/slovnik/rf/) výkon. OTA testování se ukázalo jako řešení, ale rané metody byly pomalé a neefektivní, vyžadující plné sférické skeny k nalezení 'nejhoršího případu' nebo nejcitlivějších směrů.

Primární problém, který OSDD řeší, je optimalizace času a spotřeby zdrojů při OTA testování. Bez apriorní znalosti anténního diagramu UE musely testovací systémy provádět vyčerpávající hledání, což významně zvyšovalo náklady a délku testů shody. Tím, že UE deklaruje své nejcitlivější směry, může testovací systém provádět cílená vysoce přesná měření přesně tam, kde nejvíce záleží. To je obzvláště důležité pro testování v hromadné výrobě, kde je propustnost prvořadá. Dále OSDD tuto deklaraci standardizuje, což zajišťuje interoperabilitu mezi UE od různých výrobců a testovacím zařízením od různých dodavatelů, což vede ke konzistentním a srovnatelným výsledkům testů v celém odvětví.

Historicky se potřeba OSDD výrazně projevila s LTE-Advanced (Rel-10/11) a rozšířením víceanténních systémů. Její formální zavedení v Rel-12 poskytlo strukturovaný rámec, který byl rozšiřován v následujících releasech pro podporu nových funkcí, jako je License-Assisted Access (LAA), vylepšené MIMO konfigurace a procedury správy beamů v 5G NR. Řeší omezení 'black-box' testování tím, že umožňuje kooperativní model, kde UE poskytuje externímu testovacímu systému klíčová data o interní RF charakterizaci.

## Klíčové vlastnosti

- Standardizované hlášení schopností UE pro optimalizaci OTA testů
- Deklaruje prostorové směry (azimut/elevace) s maximální citlivostí přijímače
- Snižuje čas OTA testů tím, že umožňuje cílené měřicí průchody
- Podporuje více kmitočtových pásem a RF konfigurací
- Klíčová pro přesné měření celkové izotropní citlivosti (TIS)
- Umožňuje reprodukovatelné testování vyzařovaného výkonu pro regulační shodu

## Související pojmy

- [TRP – Transmission and Reception Point](/mobilnisite/slovnik/trp/)

## Definující specifikace

- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- **TS 38.817** — 3GPP TR 38.817

---

📖 **Anglický originál a plná specifikace:** [OSDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/osdd/)
