---
slug: "nr-arfcn"
url: "/mobilnisite/slovnik/nr-arfcn/"
type: "slovnik"
title: "NR-ARFCN – NR Absolute Radio Frequency Channel Number"
date: 2025-01-01
abbr: "NR-ARFCN"
fullName: "NR Absolute Radio Frequency Channel Number"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nr-arfcn/"
summary: "NR-ARFCN je jedinečný číselný identifikátor používaný v 5G NR k určení střední frekvence rádiového kanálu. Poskytuje standardizovaný způsob odkazování na frekvenční pásma a jejich správy napříč různým"
---

NR-ARFCN je jedinečný číselný identifikátor používaný v 5G NR k určení střední frekvence rádiového kanálu pro standardizované frekvenční odkazování, správu pásem a zajištění interoperability.

## Popis

NR Absolute Radio Frequency Channel Number (NR-ARFCN) je klíčový parametr v 5G New Radio (NR), který jednoznačně definuje střední frekvenci nosné nebo kanálu. Slouží jako digitální označení mapované na konkrétní rádiovou frekvenci, což zjednodušuje specifikaci frekvence v protokolech a konfiguracích. Mapování je definováno lineárním vzorcem: střední frekvence F (v MHz) se vypočítá jako F = F_ref + ΔF * (N – N_ref), kde N je hodnota NR-ARFCN, F_ref je referenční frekvence, N_ref je referenční NR-ARFCN a ΔF je krok kmitočtové mřížky (např. 5 kHz, 15 kHz, 60 kHz v závislosti na pásmu a scénáři). Tento systém umožňuje přesnou identifikaci frekvence v celém širokém spektru používaném NR, od pásem pod 1 GHz až po milimetrové vlny.

NR-ARFCN funguje ve dvou primárních frekvenčních rozsazích: Frekvenční rozsah 1 (FR1: 410 MHz – 7,125 GHz) a Frekvenční rozsah 2 (FR2: 24,25 GHz – 52,6 GHz). Každý rozsah má svou vlastní sadu parametrů pro mapovací vzorec, aby vyhověl různým kmitočtovým mřížkám a charakteristikám pásem. Například v FR1 je globální krok mřížky typicky 100 kHz pro bloky synchronizačního signálu (SSB), ale pro jiné kanály může být až 5 kHz, zatímco FR2 používá větší kroky kvůli širším šířkám pásma. Hodnoty NR-ARFCN jsou přiděleny ve specifických rozsazích pro každé provozní pásmo, aby se předešlo nejednoznačnosti a zajistila globální konzistence.

V síti se NR-ARFCN hojně používá v signalizačních a konfiguračních zprávách. Při počátečním přístupu vysílá gNB bloky synchronizačního signálu (SSB) asociované s konkrétními NR-ARFCN, aby pomohlo koncovému zařízení (UE) detekovat buňku a připojit se k ní. V signalizaci řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) NR-ARFCN identifikuje nosné pro operace jako je agregace nosných, duální konektivita a přechody mezi buňkami (handover). Hraje také roli v indikaci podporovaného pásma, kde UE hlásí svá podporovaná pásma pomocí rozsahů NR-ARFCN. Tento identifikátor je zásadní pro frekvenční management, umožňuje dynamické sdílení spektra, efektivní přidělování zdrojů a vícepásmové operace v 5G sítích.

## K čemu slouží

NR-ARFCN byl zaveden, aby řešil potřebu jednotného a škálovatelného systému identifikace frekvence v 5G NR, který překonává omezení dřívějších systémů, jako byl [EARFCN](/mobilnisite/slovnik/earfcn/) pro LTE. Jak se 5G rozšířilo do nových frekvenčních pásem, včetně milimetrových vln s širšími šířkami pásma a různorodými uspořádáními kanálů, byl vyžadován flexibilnější identifikátor. Účelem je poskytnout standardizovanou metodu pro odkazování na jakoukoli nosnou frekvenci NR globálně, což zajišťuje interoperabilitu mezi síťovým vybavením a zařízeními od různých výrobců.

Historicky měla každá generace mobilních sítí vlastní schéma číslování kanálů (např. [ARFCN](/mobilnisite/slovnik/arfcn/) pro GSM, [UARFCN](/mobilnisite/slovnik/uarfcn/) pro UMTS, EARFCN pro LTE). S širším frekvenčním rozsahem a různorodými případy použití 5G byly předchozí schémata nedostatečná kvůli pevné granularitě a omezenému rozsahu. NR-ARFCN to řeší tím, že nabízí lineární mapování, které je škálovatelné napříč všemi pásmy NR, od nízkých po vysoká pásma, s konfigurovatelnými kroky mřížky. To umožňuje přesnou specifikaci frekvence nezbytnou pro funkce jako širokopásmové nosné, sdílení spektra a multikonektivita, což usnadňuje efektivní nasazení a provoz sítě v fragmentovaném spektru.

## Klíčové vlastnosti

- Lineární mapovací vzorec pro přesný výpočet střední frekvence
- Podpora pro Frekvenční rozsah 1 (FR1) i Frekvenční rozsah 2 (FR2)
- Konfigurovatelné kroky kmitočtové mřížky (např. 5 kHz, 15 kHz, 60 kHz)
- Použití při vysílání SSB pro detekci a výběr buňky
- Klíčový pro konfiguraci agregace nosných a duální konektivity
- Umožňuje indikaci podporovaného pásma a frekvenční plánování v vícepásmových sítích

## Definující specifikace

- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.862** (Rel-19) — Adding channel bandwidth in existing NR bands
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.175** (Rel-19) — EMC for NR IAB Nodes
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [NR-ARFCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/nr-arfcn/)
