---
slug: "eis"
url: "/mobilnisite/slovnik/eis/"
type: "slovnik"
title: "EIS – Equivalent Isotropic Sensitivity"
date: 2025-01-01
abbr: "EIS"
fullName: "Equivalent Isotropic Sensitivity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eis/"
summary: "Standardizovaná metrika pro měření citlivosti přijímače při testování Over-the-Air (OTA). Představuje minimální úroveň výkonu signálu vyžadovanou na anténním portu pro dosažení stanovené propustnosti"
---

EIS je standardizovaná metrika pro měření citlivosti přijímače při testování Over-the-Air, která představuje minimální výkon signálu vyžadovaný na anténním portu pro dosažení stanovené propustnosti.

## Popis

Equivalent Isotropic Sensitivity (EIS) je základní výkonnostní parametr definovaný ve specifikacích 3GPP pro hodnocení citlivosti přijímače v testovacím prostředí Over-the-Air ([OTA](/mobilnisite/slovnik/ota/)). Na rozdíl od měření vedené citlivosti prováděných na fyzickém konektoru EIS kvantifikuje citlivost na referenčním bodě antény a zahrnuje vlivy anténního vyzařovacího diagramu, zisku a účinnosti. Metrika je vyjádřena v dBm a je odvozena měřením celkového vyzařovaného výkonu (TRP) potřebného k dosažení specifické referenční propustnosti, například 95 % maximální propustnosti pro daný referenční měřicí kanál. Tento přístup poskytuje realističtější hodnocení výkonu přijímače, jak jej zažívá koncový uživatel v reálných podmínkách, kde je anténa nedílnou součástí zařízení.

Metodika měření EIS je podrobně popsána v mnoha testovacích specifikacích 3GPP (např. 38.521 pro NR). Typicky zahrnuje umístění testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)) do bezodrazové komory a jeho osvětlení známým, řízeným rádiovým signálem z emulátoru základnové stanice. Testovací systém měří výkon přijímaný anténou DUT a výslednou propustnost. Systematickou změnou vstupního výkonu a mapováním výkonu propustnosti je určena minimální úroveň výkonu potřebná k dosažení cílové propustnosti. Tato hodnota je následně normalizována tak, aby vyjadřovala citlivost, jako kdyby zařízení mělo ideální izotropní anténu, odtud termín „equivalent isotropic“.

EIS je zásadní pro charakterizaci přijímačů uživatelských zařízení (UE) i základnových stanic (gNB). U UE zajišťuje, že zařízení mohou spolehlivě dekódovat signály v oblastech se slabým pokrytím, což přímo ovlivňuje kvalitu hovoru a datové rychlosti. U základnových stanic měření EIS ověřuje schopnost přijímače detekovat uplinkové přenosy ze vzdálených UE, což je nezbytné pro pokrytí na okraji buňky. Parametr je testován napříč mnoha kmitočtovými pásmy, šířkami pásma a modulačními schématy, aby byla zajištěna konzistentní výkonnost. Standardizací tohoto OTA měření umožňuje 3GPP spravedlivá a srovnatelná hodnocení citlivosti přijímačů od různých výrobců a v různých form faktorech zařízení, čímž odstraňuje nejednoznačnosti, které by mohly vyplynout pouze z vedených testů.

## K čemu slouží

EIS byl zaveden, aby řešil omezení tradičního testování vedené citlivosti, které izoluje vysokofrekvenční (RF) front-end od antény. S vývojem mobilních zařízení s integrovanými, neodnímatelnými anténami se stalo nemožné měřit citlivost přímo na konektoru. Vedené testy také nezohledňovaly zhoršení výkonu antény způsobené designem, krytem nebo interakcí s uživatelem (např. sevřením v ruce). Tato mezera znamenala, že zařízení s vynikající vedenou citlivostí mohlo v reálném použití stále podávat slabý výkon, pokud byla jeho anténa neúčinná.

Vytvoření EIS jako standardizované [OTA](/mobilnisite/slovnik/ota/) metriky v 3GPP Release 12 poskytlo holistickou vyhodnocovací metodu, která odráží skutečný výkon přijímače. Řeší problém zajištění, že celý přijímací řetězec – od antény přes RF komponenty až po základnové zpracování – splňuje minimální požadavky na citlivost. To je obzvláště důležité pro zaručení konzistentního uživatelského zážitku v náročných rádiových podmínkách, jako jsou okraje buněk nebo vnitřní prostory budov. Definováním EIS umožnil 3GPP regulatorním orgánům a operátorům vynucovat výkonnostní standardy, které přímo korelují se síťovým pokrytím a kvalitou služeb, a tím pohánět zlepšování v designu zařízení a anténní technologii.

## Klíčové vlastnosti

- Standardizované měření citlivosti přijímače metodou Over-the-Air (OTA)
- Zohledňuje vlivy anténního zisku, účinnosti a vyzařovacího diagramu
- Definováno pro přijímače uživatelských zařízení (UE) i základnových stanic (gNB)
- Testováno napříč více kmitočtovými pásmy a konfiguracemi šířky pásma
- Používá kritéria založená na propustnosti (např. 95 % maximální propustnosti) jako výkonnostní cíl
- Umožňuje spravedlivé porovnání výkonnosti mezi různými designy zařízení a form faktory

## Definující specifikace

- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- … a dalších 12 specifikací

---

📖 **Anglický originál a plná specifikace:** [EIS na 3GPP Explorer](https://3gpp-explorer.com/glossary/eis/)
