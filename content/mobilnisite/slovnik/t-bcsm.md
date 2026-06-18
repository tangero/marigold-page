---
slug: "t-bcsm"
url: "/mobilnisite/slovnik/t-bcsm/"
type: "slovnik"
title: "T-BCSM – Terminating Basic Call State Model"
date: 2025-01-01
abbr: "T-BCSM"
fullName: "Terminating Basic Call State Model"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/t-bcsm/"
summary: "Standardizovaný model v rámci protokolu CAMEL definující stavy a události pro ukončovaný hovor (příchozí k účastníkovi). Umožňuje GMSC aktivovat servisní logiku (např. přesměrování hovoru) v konkrétní"
---

T-BCSM je standardizovaný model protokolu CAMEL, který definuje stavy a události pro příchozí hovor k účastníkovi a umožňuje GMSC aktivovat servisní logiku v určitých bodech během sestavování hovoru.

## Popis

Terminating Basic Call State Model (T-BCSM) je základní součást sady protokolů Customised Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)), standardizované v 3GPP. Poskytuje formální reprezentaci procesu zpracování příchozího hovoru určeného pro účastníka v síti GSM nebo UMTS ve formě stavového stroje. Model je implementován v Gateway Mobile Switching Centre ([GMSC](/mobilnisite/slovnik/gmsc/)) nebo v navštívené [MSC](/mobilnisite/slovnik/msc/), což je síťový uzel zodpovědný za směrování hovorů na aktuální polohu účastníka. T-BCSM definuje řadu odlišných 'Pics' (Points In Call) a detekčních bodů. Pics představují stabilní stavy v procesu hovoru, jako je 'Terminating Call Handling', kdy se MSC pokouší lokalizovat a vyzvánět účastníka. Detekční body jsou specifické události uvnitř těchto stavů nebo mezi nimi, kde může být zpracování pozastaveno, což umožňuje MSC komunikovat s externí funkcí řízení služeb, jako je CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)).

Když hovor dorazí do GMSC, logika zpracování hovoru sleduje T-BCSM. Na předdefinovaných detekčních bodech (např. 'Terminating Attempt Authorized') může GMSC odeslat oznámení do CSE. CSE, které obsahuje specifickou servisní logiku účastníka (definovanou [T-CSI](/mobilnisite/slovnik/t-csi/)), pak může GMSC instruovat, jak pokračovat. To může zahrnovat úpravu parametrů hovoru, aplikaci pravidel pro přesměrování hovoru nebo implementaci dalších přidaných služeb. Interakce využívá protokol CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)). T-BCSM zajišťuje, že k těmto interakcím dochází v konzistentních, přesně definovaných okamžicích, což garantuje spolehlivé provádění služeb napříč různými síťovými implementacemi.

Model zahrnuje několik klíčových detekčních bodů, jako jsou Collected Information, Analyzed Information, Terminating Call Handling a Call Accepted. Každý má specifické spouštěče a výsledky. Architektura odděluje základní přepínací funkci (MSC) od inteligentní servisní logiky (CSE), což podporuje flexibilitu a umožňuje operátorům zavádět nové služby bez nutnosti úprav každé ústředny v jádru sítě. T-BCSM spolu se svým protějškem [O-BCSM](/mobilnisite/slovnik/o-bcsm/) (Originating [BCSM](/mobilnisite/slovnik/bcsm/)) tvoří základní signalizační rámec pro služby založené na CAMEL, jako je předplacené volání, filtrování hovorů, překlad čísel a další služby v reálném čase.

## K čemu slouží

T-BCSM byl vytvořen za účelem standardizace řízení služeb inteligentní sítě pro ukončované hovory v mobilních sítích. Před zavedením CAMEL bylo zavádění přidaných služeb, jako je přesměrování hovoru nebo filtrování příchozích hovorů, často proprietární a těsně integrované se softwarem dodavatele ústředen, což činilo nasazení pomalým a nákladným. Iniciativa CAMEL, inspirovaná koncepty inteligentní sítě (IN) pro pevné linky, si kladla za cíl oddělit servisní logiku od přepínacího hardwaru. T-BCSM poskytuje přesné 'hákovací' body v sekvenci ukončovaného hovoru, kde může tato externí logika zasáhnout.

Definováním univerzálního stavového modelu umožnil 3GPP interoperabilitu mezi MSC od různých výrobců a externími servisními platformami. To umožnilo operátorům konzistentně zavádět služby specifické pro účastníky v celé své síti. Vyřešil problém, jak aplikovat vlastní pravidla (např. 'přesměrovat všechny hovory do hlasové schránky po 5 zazvoněních') ve správný okamžik během doručování hovoru, zejména když účastník může být v roamingu. Model zajišťuje, že interakce řízení služeb jsou předvídatelné a spolehlivé, což je klíčové pro služby generující příjmy, jako je autorizace příchozího hovoru u předplacených služeb.

## Klíčové vlastnosti

- Standardizovaný stavový stroj pro zpracování ukončovaného hovoru
- Definuje konkrétní body v hovoru (PICs), jako je Terminating Call Handling
- Zahrnuje detekční body (DPs) pro interakci s externími službami
- Umožňuje spouštění CAMEL služeb pro příchozí hovory
- Implementován v GMSC nebo navštívené MSC
- Pro komunikaci s funkcí řízení služeb využívá protokol CAP

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [O-BCSM – Originating Basic Call State Model](/mobilnisite/slovnik/o-bcsm/)
- [T-CSI – Terminating CAMEL Subscription Information](/mobilnisite/slovnik/t-csi/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [T-BCSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-bcsm/)
