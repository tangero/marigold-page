---
slug: "earfcn"
url: "/mobilnisite/slovnik/earfcn/"
type: "slovnik"
title: "EARFCN – E-UTRAN Absolute Radio Frequency Channel Number"
date: 2025-01-01
abbr: "EARFCN"
fullName: "E-UTRAN Absolute Radio Frequency Channel Number"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/earfcn/"
summary: "EARFCN je jedinečný číselný identifikátor, který určuje střední kmitočet rádiového kanálu v sítích LTE a 5G NR. Poskytuje standardizovanou metodu pro odkazování na kmitočtová pásma a jejich správu na"
---

EARFCN je jedinečný číselný identifikátor, který určuje střední kmitočet rádiového kanálu v sítích LTE a 5G NR pro standardizovaný globální odkaz a správu kmitočtů.

## Popis

[E-UTRAN](/mobilnisite/slovnik/e-utran/) Absolute Radio Frequency Channel Number (EARFCN) je základní identifikátor v rámci specifikací 3GPP pro Long-Term Evolution (LTE) a jeho vývoj směrem k 5G New Radio (NR). Slouží jako číslo kanálu, které jednoznačně mapuje na konkrétní střední kmitočet nosné používané pro komunikaci mezi uživatelským zařízením (UE) a vysílačem [eNB](/mobilnisite/slovnik/enb/) nebo gNB. Mapování je definováno vzorcem, který převádí hodnotu EARFCN na absolutní kmitočet v kHz, přičemž pro směr uplink a downlink jsou definovány samostatné vzorce. Tento systém abstrahuje fyzický kmitočet, což umožňuje, aby se síťové příkazy a konfigurace odkazovaly na jednoduché číslo namísto surové hodnoty kmitočtu, a tím zjednodušuje návrh softwaru a protokolů.

Architektura identifikace kmitočtů spoléhá na to, že EARFCN je součástí systémové informace vysílané buňkou a používá se v měřicích hlášeních a příkazech k předání spojení. Mezi klíčové komponenty patří kmitočtová mřížka (channel raster), která definuje sadu povolených hodnot EARFCN a jim odpovídajících kmitočtů, čímž zajišťuje, že všechna UE a základnové stanice se naladí na stejný přesný kmitočet pro daný EARFCN. Specifikace definují různé rozsahy pro EARFCN v různých provozních pásmech (např. Band 1, Band 3) a samotná hodnota na základě pásmově specifických mapovacích tabulek udává, zda je pro uplink nebo downlink. Jeho role je ústřední pro správu rádiových prostředků a umožňuje funkce jako je agregace nosných, kde může být jednomu UE přiřazeno více EARFCN pro zvýšení šířky pásma.

Během provozu, když síťový operátor nasazuje buňku, nakonfiguruje její provozní kmitočet nastavením EARFCN. UE při skenování nebo přijetí systémové informace přečte EARFCN a použije standardizovaný vzorec pro výpočet přesného kmitočtu, na který se musí naladit její rádiový modul. Pro měřicí hlášení identifikuje UE sousední buňky podle detekovaného EARFCN. Systém podporuje široký rozsah hodnot, aby pokryl celý licencovaný spektrální rozsah od kmitočtů pod 1 GHz až po milimetrové vlny, přičemž pozdější verze specifikací jej rozšiřují, aby akomodovaly nová přidělení spektra. Přesnost a jednoznačnost EARFCN jsou klíčové pro předcházení interferencím a zajištění plynulého přechodu mezi sítěmi od různých výrobců a operátorů.

## K čemu slouží

EARFCN byl vytvořen, aby vyřešil potřebu jednotné, škálovatelné a na technologii nezávislé metody identifikace rádiových kanálů v sítích LTE, čímž nahradil dříve používané UMTS Absolute Radio Frequency Channel Number (UARFCN) pro 3G. Před LTE používaly různé technologie rádiového přístupu (GSM, UMTS) vlastní schémata číslování kanálů, což komplikovalo návrh více režimových zařízení a vzájemné propojení sítí. Přechod na LTE založené na [OFDMA](/mobilnisite/slovnik/ofdma/) vyžadoval nové schéma, které by mohlo efektivně reprezentovat širší šířky kanálů a různorodá přidělení spektra plánovaná pro 4G.

Hlavním problémem, který EARFCN řeší, je abstrakce detailů fyzického kmitočtu od protokolů vyšších vrstev a systémů pro správu sítě. Použitím jednoduchého celého čísla se síťová konfigurace, seznamy sousedních buněk a příkazy k předání spojení stávají nezávislými na skutečných hodnotách v MHz nebo GHz, což zjednodušuje softwarovou implementaci a snižuje chyby. Tato abstrakce je obzvláště důležitá pro globální roaming, protože zařízení může interpretovat EARFCN z jakékoli sítě na světě a správně vypočítat místní provozní kmitočet na základě standardizovaných vzorců. Systém také připravuje na budoucnost, protože nová kmitočtová pásma lze přidat rozšířením rozsahu EARFCN bez změny základních mechanizmů protokolu.

Historicky vycházela motivace z rostoucí složitosti správy spektra s příchodem LTE, které bylo navrženo pro provoz v párovém ([FDD](/mobilnisite/slovnik/fdd/)) i nepárovém (TDD) spektru v kontinuu od tradičních buněčných pásem až po nové, vyšší kmitočty. EARFCN poskytuje konzistentní referenční bod, který je škálovatelný napříč všemi těmito scénáři, a umožňuje funkce jako je agregace nosných, kdy zařízení současně používá více EARFCN. Jeho vytvoření bylo základním krokem k zajištění, že LTE a následné 5G NR mohou být flexibilně nasazeny v roztříštěném rádiovém spektru po celém světě.

## Klíčové vlastnosti

- Jednoznačně mapuje na konkrétní střední kmitočet nosné pro uplink a downlink
- Definován standardizovanými vzorci převádějícími EARFCN na kmitočet v kHz
- Samostatné rozsahy hodnot pro různá provozní pásma (např. Band 1, Band 41)
- Nedílná součást vysílání systémové informace a měřicího hlášení
- Podporuje agregaci nosných identifikací více komponentních nosných
- Rozšiřitelný pro pokrytí nových přidělení spektra až po milimetrové vlny

## Související pojmy

- [NR-ARFCN – NR Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/nr-arfcn/)
- [E-UTRAN – Evolved Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/e-utran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.368** (Rel-19) — NAS Configuration Management Object
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.112** (Rel-19) — E-UTRAN LMU Conformance Requirements
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [EARFCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/earfcn/)
