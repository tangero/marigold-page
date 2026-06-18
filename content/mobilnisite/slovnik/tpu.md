---
slug: "tpu"
url: "/mobilnisite/slovnik/tpu/"
type: "slovnik"
title: "TPU – Tensor Processing Unit"
date: 2025-01-01
abbr: "TPU"
fullName: "Tensor Processing Unit"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tpu/"
summary: "Specializovaný hardwarový akcelerátor navržený pro efektivní tenzorové operace, klíčový pro úlohy inference umělé inteligence a strojového učení. V 3GPP je standardizován, aby umožnil provádění AI/ML"
---

TPU je standardizovaný hardwarový akcelerátor pro efektivní tenzorové operace, který umožňuje provádění AI/ML modelů v rámci systému 5G pro síťovou analytiku a správu rádiových zdrojů.

## Popis

Tenorový procesor (TPU), jak je definován ve specifikacích 3GPP, jako jsou TS 26.928 a TS 26.998, představuje standardizační úsilí pro hardwarovou akceleraci [AI/ML](/mobilnisite/slovnik/ai-ml/) v ekosystému 5G. Na rozdíl od univerzální centrální procesorové jednotky ([CPU](/mobilnisite/slovnik/cpu/)) nebo dokonce grafického procesoru ([GPU](/mobilnisite/slovnik/gpu/)) je TPU integrovaný obvod pro specifické aplikace (ASIC), který je architektonicky optimalizován pro rozsáhlé paralelní výpočty spojené s manipulací tenzorů. Tenzory jsou vícerozměrná pole numerických dat, která tvoří základní datovou strukturu v modelech neuronových sítí. Základní návrh TPU se zaměřuje na extrémně efektivní provádění maticových násobení a konvolucí, které dominují inferenci a tréninku neuronových sítí, a nabízí ve srovnání s univerzálními procesory výrazně vyšší propustnost a nižší spotřebu energie na operaci.

V rámci architektury 3GPP je TPU konceptualizován jako klíčový prvek umožňující pracovní postup [AI](/mobilnisite/slovnik/ai/)/[ML](/mobilnisite/slovnik/ml/) definovaný rámcem správy AI/ML modelů ([AIM](/mobilnisite/slovnik/aim/)). Není povinně konkrétním fyzickým čipem, ale spíše definuje sadu schopností a rozhraní, která musí AI akcelerátor poskytovat pro integraci do síťové funkce 3GPP nebo uživatelského zařízení (UE). Specifikace podrobně popisují požadavky na reprezentaci modelu (např. podporu formátů jako ONNX), prováděcí [API](/mobilnisite/slovnik/api/), správu paměti pro váhy a aktivace modelu a výkonnostní metriky. Síťová funkce, jako je inteligentní řadič rádiového přístupového sítě (RIC) nebo funkce pro analýzu síťových dat ([NWDAF](/mobilnisite/slovnik/nwdaf/)), může přesunout složité inferenční úlohy AI/ML – jako je predikce provozu, detekce anomálií nebo správa svazků – na TPU. TPU načte trénovaný model, přijme vstupní datové tenzory (např. klíčové ukazatele výkonu, informace o stavu kanálu), zpracuje je přes vrstvy neuronové sítě a vrátí výstupní tenzory (např. predikci nebo rozhodnutí o klasifikaci).

Tento hardwarově-softwarový spolunávrh je klíčový pro realizovatelnost AI/ML v prostředích sítí citlivých na latenci a s omezenými zdroji. TPU spolupracuje s dalšími komponentami rámce AIM: AI/ML proxy, která zajišťuje poskytování modelů a správu jejich životního cyklu, a AI/ML hostitelem, což je síťová funkce hostující aplikační logiku. TPU poskytuje výpočetní výkon. Jeho integrace umožňuje analýzu a rozhodování v reálném čase nebo téměř v reálném čase přímo v síti, což přesahuje cloudově orientovanou AI směrem k distribuované inteligenci na okraji sítě. To umožňuje případy užití, jako je dynamická optimalizace rádiových zdrojů, prediktivní vyvažování zátěže a vylepšená správa kvality uživatelského prožitku, které byly dříve neproveditelné kvůli výpočetním omezením nebo omezením latence.

## K čemu slouží

Standardizace Tenorového procesoru (TPU) ve vydání 3GPP 16 byla hnána explozivním růstem umělé inteligence a strojového učení a jejich identifikovaným potenciálem revolučně změnit provoz sítě a poskytování služeb. Tradiční správa sítě založená na statických konfiguracích a algoritmech založených na pravidlech se stávala nedostatečnou pro zvládnutí složitosti, rozsahu a dynamické povahy sítí 5G a budoucích sítí. Zatímco modely AI/ML slibovaly nadřazená řešení pro optimalizaci a automatizaci, jejich výpočetní náklady byly pro nasazení na standardních serverových CPU sítě neúnosné, což vedlo k vysoké latenci a spotřebě energie. To vytvořilo mezeru mezi potenciálem AI a jejím praktickým rozsáhlým nasazením v telekomunikační infrastruktuře.

3GPP zavedlo koncept TPU, aby tuto mezeru přímo řešilo podporou hardwarové akcelerace. Účelem je definovat společný architektonický plán pro AI akcelerátory, který zajišťuje interoperabilitu a předvídatelnost výkonu napříč různými implementacemi od různých dodavatelů. Předtím bylo možné používat proprietární AI akcelerátory, ale bez standardizace by jejich integrace do síťových funkcí byla vázána na dodavatele a složitá. Specifikace TPU to řeší tím, že poskytují standardizované rozhraní a sadu schopností, což umožňuje vývoj softwaru síťových funkcí nezávisle na podkladovém AI hardwaru. To snižuje bariéry vstupu, podporuje konkurenční ekosystém dodavatelů akcelerátorů a v konečném důsledku umožňuje rozsáhlé a efektivní nasazení AI/ML pro analýzu síťových dat, autonomní provoz sítě a inovativní služby poháněné AI, naplňující tak vizi inteligentního, samooptymalizujícího se systému 5G.

## Klíčové vlastnosti

- Architektonická optimalizace pro tenzorové/maticové operace s vysokou propustností
- Standardizovaná rozhraní pro načítání AI/ML modelů a provádění inference
- Podpora běžných formátů modelů neuronových sítí (např. ONNX)
- Vysoká energetická účinnost pro nasazení na okrajích sítě s omezeným výkonem
- Inference s nízkou latencí vhodná pro řídicí smyčky sítě v reálném čase
- Integrační rámec v rámci architektury správy AI/ML modelů (AIM) 3GPP

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [TPU na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpu/)
