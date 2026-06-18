---
slug: "rit"
url: "/mobilnisite/slovnik/rit/"
type: "slovnik"
title: "RIT – Radio Interface Technology"
date: 2025-01-01
abbr: "RIT"
fullName: "Radio Interface Technology"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rit/"
summary: "Termín používaný k popisu konkrétního souboru technologií a souvisejících protokolů pro rádiový přenos, které definují kompletní rozhraní vzdušného rozhraní. Jde o klíčový koncept v hodnocení IMT-Adva"
---

RIT je konkrétní soubor technologií a protokolů pro rádiový přenos, který definuje kompletní rozhraní vzdušného rozhraní a představuje kandidátskou technologii, jako je LTE-Advanced, v rámci hodnocení IMT.

## Popis

Radio Interface Technology (RIT) je formální termín používaný v rámci standardizace [ITU-R](/mobilnisite/slovnik/itu-r/) a 3GPP, zejména v kontextu hodnocení kandidátů pro rodiny International Mobile Telecommunications ([IMT](/mobilnisite/slovnik/imt/)), jako jsou IMT-Advanced (4G) a IMT-2020 (5G). RIT představuje kompletní, samostatnou specifikaci pro rádiové rozhraní vzdušného rozhraní. Zahrnuje celý zásobník protokolů a technik fyzické vrstvy potřebných pro bezdrátovou komunikaci, včetně metody duplexování ([FDD](/mobilnisite/slovnik/fdd/)/[TDD](/mobilnisite/slovnik/tdd/)), schématu mnohonásobného přístupu (např. [OFDMA](/mobilnisite/slovnik/ofdma/), [SC-FDMA](/mobilnisite/slovnik/sc-fdma/)), rámcové struktury, kanálového kódování, modulačních schémat, fyzických kanálů a protokolů vyšších vrstev pro řízení a data.

Když 3GPP předkládá technologii jako LTE-Advanced nebo NR jako kandidáta pro označení IMT, je zabalena a dokumentována jako RIT. Specifikace zahrnuje podrobné výkonnostní charakteristiky, jako jsou špičkové datové rychlosti, spektrální účinnost, latence a podpora mobility. Proces hodnocení zahrnuje posouzení RIT vůči souboru minimálních technických požadavků definovaných ITU-R. Pro IMT-2020 byl například 5G NR od 3GPP předložen jako jediný RIT, ačkoli zahrnuje vysoce flexibilní rámec podporující různé kmitočtová pásma (pod 6 GHz a mmWave) a scénáře nasazení ([eNB](/mobilnisite/slovnik/enb/) a gNB).

Z architektonického hlediska RIT definuje interakční body mezi uživatelským zařízením (UE) a rádiovou přístupovou sítí (RAN). Obvykle nenařizuje konkrétní síť jádra, což umožňuje určitý stupeň nezávislosti (např. NR se může připojit k 5GC i EPC). Klíčovými součástmi specifikace RIT jsou popis fyzické vrstvy ([PHY](/mobilnisite/slovnik/phy/)), protokoly řízení přístupu k médiu (MAC) a řízení rádiového spoje (RLC) a protokol řízení rádiových zdrojů (RRC). Dokumentace RIT poskytuje komplexní pohled na to, jak technologie funguje, jaké má schopnosti a jak splňuje širší cíle systému IMT.

## K čemu slouží

Koncept Radio Interface Technology byl formalizován, aby poskytl strukturovaný rámec pro předkládání a hodnocení kandidátských technologií pro globální standardy IMT. Primární problém, který řeší, je potřeba standardizovaného, přímého porovnání mezi radikálně odlišnými bezdrátovými technologiemi navrhovanými různými organizacemi pro vývoj standardů (SDO), jako jsou 3GPP, IEEE a další. Před existencí tohoto rámce bylo definování toho, co tvoří kompletní „technologii“ pro hodnocení, nejednoznačné.

Historický kontext vychází z role ITU-R při definování rodin IMT-2000 (3G), IMT-Advanced (4G) a IMT-2020 (5G). Motivací bylo vytvořit transparentní a technický proces pro uznání, které technologie splňují ambiciózní výkonnostní cíle stanovené pro každou novou generaci. Předložení RIT umožňuje pracovním skupinám ITU-R provádět podrobná technická hodnocení, simulacemi založené evaluace a vytvářet konsensus, aby rozhodly, zda technologie kvalifikuje. Tento proces zajišťuje, že označení „4G“ nebo „5G“, jak je definováno ITU, je podloženo podstatnými technickými zásluhami a potenciálem globální interoperability, což přesahuje pouhá marketingová tvrzení.

## Klíčové vlastnosti

- Představuje kompletní, standardizovanou specifikaci rozhraní vzdušného rozhraní pro hodnocení
- Zahrnuje fyzickou vrstvu, vrstvu spojení dat a klíčové protokoly řídicí roviny
- Definuje konkrétní výkonnostní parametry (datová rychlost, latence, spektrální účinnost)
- Předkládána organizacemi SDO (např. 3GPP) jako kandidát pro rodinu IMT (např. IMT-2020)
- Může zahrnovat více komponentních technologií nebo provozních pásem v rámci jednoho RIT
- Poskytuje základ pro dohody o interoperabilitě a globálním roamingu

## Definující specifikace

- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TR 36.912** (Rel-19) — TR on LTE-Advanced (Further E-UTRA)
- **TS 37.810** (Rel-12) — Study on Base Station Specification Structure
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TR 37.911** (Rel-19) — 3GPP 5G NTN Self-Evaluation Report
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [RIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/rit/)
