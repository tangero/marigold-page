---
slug: "mnru"
url: "/mobilnisite/slovnik/mnru/"
type: "slovnik"
title: "MNRU – Modulated Noise Reference Unit"
date: 2025-01-01
abbr: "MNRU"
fullName: "Modulated Noise Reference Unit"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mnru/"
summary: "Standardizovaný generátor testovacího signálu používaný k hodnocení výkonu řečových kodeků a kvality hlasu v mobilních sítích. Vytváří řízený modulovaný šumový signál, který simuluje degradovaný řečov"
---

MNRU je standardizovaný generátor testovacího signálu, který produkuje modulovaný šum pro hodnocení výkonu řečových kodeků a kvality hlasu v mobilních sítích.

## Popis

Modulated Noise Reference Unit (MNRU, jednotka referenčního modulovaného šumu) je klíčový nástroj definovaný ve specifikacích 3GPP pro objektivní testování a hodnocení kvality přenosu řeči. Nejde o síťový prvek, ale o referenční signál definovaný algoritmicky. MNRU generuje testovací signál, který je v podstatě zdroj šumu (typicky bílý šum) amplitudově modulovaný sinusovkou. Tím vzniká signál se specifickými časovými a spektrálními charakteristikami, které jsou navrženy tak, aby byly pro řečové kodeky náročné na zpracování, čímž poskytují přísnou a opakovatelnou testovací podmínku. Klíčovým parametrem MNRU je Q-hodnota (nebo Qdb), která definuje poměr signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)) modulovaného šumu. Nižší Q-hodnota indikuje šumovější, více degradovaný referenční signál.

V praxi se signál MNRU používá jako vstup do testovaného řečového kodeku. Kodek tento signál zakóduje a následně dekóduje. Výstup je pak porovnán s původním vstupem MNRU pomocí objektivních algoritmů pro měření percepční kvality, jako je Perceptual Evaluation of Speech Quality ([PESQ](/mobilnisite/slovnik/pesq/)) nebo jeho nástupce Perceptual Objective Listening Quality Analysis ([POLQA](/mobilnisite/slovnik/polqa/)). Rozdíl mezi původním a zpracovaným signálem, kvantifikovaný jako skóre kvality, ukazuje výkon kodeku při zpracování šumového, modulovaného vstupu. Tento proces izoluje příspěvek kodeku k degradaci kvality od ostatních síťových zkreslení.

Role MNRU je zásadní při standardizaci a typovém schvalování řečových kodeků, jako jsou [AMR](/mobilnisite/slovnik/amr/) (Adaptive Multi-Rate) a [EVS](/mobilnisite/slovnik/evs/) (Enhanced Voice Services). Poskytuje společný, jednoznačný referenční bod. Zkušební laboratoře a výrobci zařízení používají MNRU k ověření, že implementace kodeku splňuje minimální požadavky na výkonnost stanovené ve specifikacích 3GPP. Použitím standardizovaného šumového signálu zajišťuje, že srovnání výkonnosti mezi různými kodeky nebo různými implementacemi stejného kodeku jsou spravedlivá a reprodukovatelná. Jeho specifikace jsou podrobně popsány v řadě technických specifikací 3GPP (TS), především v sérii TS 26.0xx (Kodek) a TS 46.0xx (GSM kodek), a pokrývají jeho algoritmickou definici a použití v testech shody.

## K čemu slouží

MNRU byl vytvořen k vyřešení základního problému, jak objektivně a opakovatelně měřit výkonnost digitálních řečových kodeků. Před existencí takových standardizovaných referenčních signálů bylo testování kvality subjektivnější a méně konzistentní, silně závislé na poslechových testech s lidskými subjekty, které jsou časově náročné, drahé a proměnlivé. Průmysl potřeboval spolehlivou, automatizovanou metodu pro hodnocení toho, jak kodek zavádí zkreslení a šum.

MNRU tento problém řeší tím, že poskytuje přesně definovaný, náročný testovací signál. Jeho charakteristika modulovaného šumu je obzvláště účinná, protože zatěžuje schopnost kodeku zpracovávat signály s rychle se měnící energií, podobně jako reálná řeč, ale bez složitosti a variability skutečných lidských hlasů. To umožňuje inženýrům identifikovat slabiny kodeku v kontrolovaném prostředí. Vývoj hlasových služeb od GSM přes 3G, 4G až po 5G (VoLTE, VoNR) se stále složitějšími kodeky, jako jsou [AMR-WB](/mobilnisite/slovnik/amr-wb/) a [EVS](/mobilnisite/slovnik/evs/), učinil takové objektivní testování ještě kritičtějším pro zajištění zpětné kompatibility a vysoké kvality služeb napříč generacemi. MNRU zůstává základním kamenem zajištění kvality hlasu v telekomunikacích.

## Klíčové vlastnosti

- Generuje standardizovaný testovací signál modulovaného šumu s definovatelnou Q-hodnotou (SNR)
- Poskytuje opakovatelný a objektivní referenční bod pro testování výkonnosti řečových kodeků
- Používá se jako vstup pro algoritmy měření percepční kvality, jako jsou PESQ a POLQA
- Algoritmicky definován ve specifikacích 3GPP pro konzistentní implementaci
- Nezbytný pro testy shody a typové schvalování koncových zařízení a síťového vybavení
- Podporuje testování kodeků napříč generacemi (např. AMR, AMR-WB, EVS)

## Související pojmy

- [PESQ – Perceptual Evaluation of Speech Quality](/mobilnisite/slovnik/pesq/)
- [POLQA – Perceptual Objective Listening Quality Assessment](/mobilnisite/slovnik/polqa/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TR 26.997** (Rel-19) — IVAS Codec Specification
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance
- **TS 46.085** (Rel-19) — GSM Speech Codec Interoperability Test Report

---

📖 **Anglický originál a plná specifikace:** [MNRU na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnru/)
