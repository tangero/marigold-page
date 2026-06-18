---
slug: "che"
url: "/mobilnisite/slovnik/che/"
type: "slovnik"
title: "CHE – Channel Encoder"
date: 2025-01-01
abbr: "CHE"
fullName: "Channel Encoder"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/che/"
summary: "Kodér kanálu (CHE) je základní komponenta zpracování fyzické vrstvy podle 3GPP, která přidává do přenášených dat redundanci, aby je ochránila před chybami vznikajícími během bezdrátového přenosu. Je k"
---

CHE je komponenta fyzické vrstvy podle 3GPP, která přidává do přenášených dat redundanci, aby je ochránila před chybami a umožnila zpětnou korekci chyb pro spolehlivou komunikaci přes šumové rádiové kanály.

## Popis

Kodér kanálu (CHE) je základní funkční blok v řetězci vysílače fyzické vrstvy (vrstva 1) podle 3GPP, odpovědný za implementaci zpětné korekce chyb ([FEC](/mobilnisite/slovnik/fec/)). Jeho primární úlohou je transformovat vstupní bitový proud z vyšších vrstev (např. z procesoru transportního kanálu) na kódovaný bitový proud, který je odolnější vůči zkreslením rádiového kanálu, jako je šum, interference a útlum. Kodér systematicky zavádí řízenou redundanci podle specifických kódovacích algoritmů, což příjemci umožňuje detekovat a opravit určitý počet chyb bez nutnosti retransmise, a tím zlepšuje spolehlivost komunikačního spoje.

Z architektonického hlediska se CHE nachází za procesy specifickými pro kódování kanálu, jako je připojení [CRC](/mobilnisite/slovnik/crc/), a před přizpůsobením rychlosti a mapováním na fyzický kanál. Konkrétní použitý kódovací algoritmus je určen typem transportního kanálu a požadovanou kvalitou služby. Pro systémy 3GPP patří mezi klíčová schémata kódování kanálu Turbo kódování pro vysokovýkonné datové kanály, konvoluční kódování pro řídicí kanály a hlasové služby a v novější době také kódy s nízkou hustotou parity ([LDPC](/mobilnisite/slovnik/ldpc/)) pro vylepšenou mobilní širokopásmovou službu v 5G NR a Polar kódy pro řídicí kanály. Kodér přijímá blok vstupních bitů (transportní blok) a na základě kódové rychlosti vydává větší blok kódovaných bitů. Tento proces zvětšuje objem dat, ale poskytuje nezbytnou ochranu.

Činnost CHE je úzce provázána s dalšími procedurami fyzické vrstvy. Volba kódovacího schématu a kódové rychlosti je kritickým parametrem přizpůsobení spoje, který je často dynamicky upravován na základě ukazatelů kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) hlášených uživatelským zařízením. Při špatných podmínkách kanálu se pro udržení cílové chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)) používá silnější kód (nižší kódová rychlost, větší redundance), zatímco při dobrých podmínkách se používá slabší kód (vyšší kódová rychlost) pro maximalizaci spektrální účinnosti. Výkon kodéru kanálu přímo ovlivňuje klíčové systémové metriky, jako je propustnost, pokrytí a latence. Jeho návrh zahrnuje pečlivé vyvažování kompromisů mezi kódovým ziskem (schopnost korekce chyb), výpočetní složitostí, zpracovatelskou latencí a spotřebou energie, což je zvláště důležité pro zařízení napájená bateriemi.

## K čemu slouží

Kodér kanálu existuje proto, aby řešil základní problém spolehlivé digitální komunikace přes inherentně nespolehlivé a šumové bezdrátové kanály. Bez korekce chyb by vysoké míry chybovosti bitů ([BER](/mobilnisite/slovnik/ber/)) typické pro rádiová prostředí znemožnily praktické datové služby. Účelem CHE je přidat před vysíláním k informačním bitům strukturovanou redundanci, což příjemci umožní rekonstruovat původní data, i když jsou některé bity během šíření poškozeny. Tento přístup zpětné korekce chyb je nezbytný pro splnění přísných požadavků na spolehlivost moderních buněčných služeb, od hovorů po vysokorychlostní data.

Historicky vycházela motivace pro sofistikované kódování kanálu v systémech 3GPP z potřeby podporovat rozmanité služby s různými nároky na spolehlivost a latenci přes stále složitější rozhraní vzduchu. Rané standardy digitální buněčné sítě používaly jednoduché konvoluční kódy. Zavedení Turbo kódů v 3G UMTS (Rel-99) bylo revolučním krokem, který nabídl výkon velmi blízký teoretické Shannonově hranici pro kanály s aditivním bílým Gaussovským šumem ([AWGN](/mobilnisite/slovnik/awgn/)), což bylo klíčové pro umožnění vyšších datových rychlostí pro raný mobilní internet. Tím se vyřešilo omezení předchozích kódů, které buď nabízely nedostatečný zisk pro vysokorychlostní data, nebo byly nepřiměřeně složité.

Neustálý vývoj schémat CHE napříč releasy 3GPP poháněla snaha o vyšší spektrální účinnost, nižší latenci a podporu nových případů užití, jako je masivní IoT a komunikace s ultra spolehlivou nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)). Každá nová rodina kódování (např. LDPC pro data v 5G) byla zavedena, aby řešila specifická omezení svých předchůdců, jako je snížení zpracovatelské latence pro velmi velké kódové bloky, zlepšení výkonu při velmi vysokých kódových rychlostech nebo minimalizace implementační složitosti pro širokopásmový provoz. CHE je tedy klíčovou technologií, která přeměňuje fyzický kanál z nepřátelského média na spolehlivou digitální trubku.

## Klíčové vlastnosti

- Implementuje zpětnou korekci chyb (FEC) pro potírání chyb kanálu
- Podporuje více kódovacích schémat (např. Turbo, konvoluční, LDPC, Polar) přizpůsobených různým typům kanálů a služeb
- Dynamické přizpůsobení kódové rychlosti na základě přizpůsobení spoje pro optimální spektrální účinnost
- Zpracovává transportní bloky a přidává redundanci podle definované mateřské kódové rychlosti
- Umožňuje spolehlivou komunikaci splňující požadavky na cílovou chybovost bloků (BLER)
- Integruje se s procedurami fyzické vrstvy, jako je přizpůsobení rychlosti a hybridní ARQ (HARQ)

## Definující specifikace

- **TS 26.071** (Rel-19) — AMR Speech Codec Introduction
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.171** (Rel-19) — Introduction to AMR-WB Speech Processing
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation

---

📖 **Anglický originál a plná specifikace:** [CHE na 3GPP Explorer](https://3gpp-explorer.com/glossary/che/)
