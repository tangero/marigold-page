---
slug: "fqi"
url: "/mobilnisite/slovnik/fqi/"
type: "slovnik"
title: "FQI – Frame Quality Indication (AMR-WBIF1)"
date: 2025-01-01
abbr: "FQI"
fullName: "Frame Quality Indication (AMR-WBIF1)"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fqi/"
summary: "Parametr v řečovém kodeku AMR-WB (Adaptive Multi-Rate Wideband), který indikuje kvalitu nebo platnost přijatého řečového rámce. Příjímací strana jej používá k posouzení integrity rámce a k řízení stra"
---

FQI je parametr v řečovém kodeku AMR-WB, který indikuje kvalitu přijatého rámce za účelem posouzení integrity a řízení maskování chyb pro robustní kvalitu hlasu.

## Popis

Frame Quality Indication (FQI) je kritická komponenta v rámci řečového kodeku [AMR-WB](/mobilnisite/slovnik/amr-wb/) (Adaptive Multi-Rate Wideband), konkrétně definovaná pro formát rozhraní AMR-WBIF1. Funguje na aplikační vrstvě, je vložena do struktury řečového rámce přenášeného přes rozhraní pro přenos po rádiu. Každý řečový rámec vygenerovaný kodekem AMR-WB obsahuje pole FQI, které nastavuje vysílající entita (např. mobilní zařízení nebo síťový uzel) na základě interních mechanismů detekce chyb, jako jsou výsledky kontrolního součtu [CRC](/mobilnisite/slovnik/crc/) (Cyclic Redundancy Check) vypočteného na řečových parametrech. Primární architektonická role FQI je poskytnout příjemci příznak kvality, který mu umožní činit informovaná rozhodnutí o zpracování rámce bez nutnosti provádět vlastní úplnou detekci chyb od nuly.

Při přijetí dekodér prozkoumá hodnotu FQI. Pokud FQI indikuje „dobrý“ rámec, dekodér pokračuje v normálním dekódování řečových parametrů obsažených v tomto rámci. Pokud FQI indikuje „špatný“ nebo poškozený rámec, dekodér vyvolá algoritmy maskování chyb. Tyto algoritmy jsou sofistikované techniky zpracování signálu navržené tak, aby zakryly efekty ztracených nebo poškozených dat. Mohou zahrnovat extrapolaci parametrů z předchozích dobrých rámců, použití opakování základního tónu nebo aplikaci generování komfortního šumu, aby se zabránilo slyšitelným artefaktům, jako jsou kliknutí nebo mezery ve výstupní řeči. Tento proces je nedílnou součástí robustnosti kodeku, protože rádiové kanály v mobilních sítích jsou inherentně náchylné k útlumům, rušení a ztrátám paketů.

Funkčnost FQI je úzce spojena s mechanismem adaptace přenosové rychlosti kodeku. AMR-WB pracuje s více bitovými rychlostmi a síť může na základě stavu kanálu nařídit přepínání mezi nimi. Spolehlivost indikovaná FQI může nepřímo ovlivňovat tato rozhodnutí o adaptaci rychlosti na vyšších vrstvách. Dále ve scénářích zahrnujících tandem-free operation (TFO) nebo transcoder-free operation (TrFO), kde jsou řečové rámce přenášeny koncově bez průběžného dekódování, se zachování a správná interpretace FQI stává ještě kritičtější pro udržení konzistentní kvality hlasu napříč síťovými hranicemi. Její specifikace napříč více technickými specifikacemi (TS) 3GPP, jako jsou TS 26.201 a TS 26.202, zajišťuje interoperabilitu mezi různými implementacemi kodeku AMR-WB od různých dodavatelů.

## K čemu slouží

FQI bylo vytvořeno, aby řešilo základní výzvu udržení vysoké kvality hlasové služby přes nespolehlivé bezdrátové spoje. Před takovými explicitními indikátory kvality museli příjemci spoléhat pouze na metriky dekódování kanálu (jako je bitová chybovost) nebo provádět výpočetně náročné ověření přijatých řečových parametrů sami, aby odhadli, zda je rámec použitelný. Tento přístup byl buď nepřímý, nebo neefektivní. FQI poskytuje přímý signál ve stejném přenosovém pásmu od zdrojového kodéru o vnímané integritě rámce ještě před jeho vysláním, čímž příjemci nabízí přesnější a včasnější posouzení.

Jeho zavedení spolu s [AMR-WB](/mobilnisite/slovnik/amr-wb/) ve verzi 3GPP Release 8 bylo součástí širšího úsilí o zlepšení kvality hlasu, konkrétně přechodu od úzkopásmové k širokopásmové řeči. Širokopásmová řeč (50–7000 Hz) nabízí oproti tradiční úzkopásmové telefonii (300–3400 Hz) vyšší přirozenost a srozumitelnost, ale je také citlivější na přenosové chyby. Mechanismus FQI byl klíčovým prvkem umožňujícím tento kvalitativní skok, neboť poskytl dekodéru nezbytný nástroj pro robustní zvládání nevyhnutelných chyb rámců bez vážného zhoršení poslechového zážitku. Řeší problém, jak efektivně standardizovaným způsobem komunikovat stav rámce, čímž umožňuje pokročilé maskování chyb a přispívá k celkové odolnosti a kvalitě služeb Voice over LTE (VoLTE) a následných hlasových služeb.

## Klíčové vlastnosti

- Indikátor kvality ve stejném přenosovém pásmu, vložený do řečového rámce AMR-WB
- Signalizuje, zda je rámec klasifikován jako „dobrý“ nebo „špatný“ na základě kontrol na straně vysílače
- Přímo spouští v příjemci rutiny pro maskování chyb při detekci špatného rámce
- Nezbytný pro udržení kvality hlasu v rádiových podmínkách náchylných k chybám
- Standardizován v rámci specifikací 3GPP pro zajištění interoperabilní implementace
- Podporuje tandem-free operation tím, že zachovává informaci o kvalitě rámce koncově

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)

## Definující specifikace

- **TS 26.101** (Rel-19) — Generic frame format for AMR and GSM-EFR speech codecs
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.201** (Rel-19) — AMR-WB Speech Codec Frame Format
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [FQI na 3GPP Explorer](https://3gpp-explorer.com/glossary/fqi/)
