---
slug: "hats"
url: "/mobilnisite/slovnik/hats/"
type: "slovnik"
title: "HATS – Head and Torso Simulator"
date: 2025-01-01
abbr: "HATS"
fullName: "Head and Torso Simulator"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/hats/"
summary: "Standardizované akustické testovací zařízení používané k měření zvukové kvality 3GPP terminálů, jako jsou mobilní telefony. Simuluje akustické vlastnosti lidské hlavy a trupu, aby poskytlo opakovateln"
---

HATS je standardizované akustické testovací zařízení, které simuluje lidskou hlavu a trup za účelem objektivního měření zvukové kvality mobilních telefonů v laboratorních podmínkách.

## Popis

Simulátor hlavy a trupu (Head and Torso Simulator, HATS) je klíčové testovací zařízení definované ve specifikacích 3GPP pro objektivní hodnocení kvality řeči a zvuku v telekomunikačních terminálech. Nejde o síťovou funkci, ale o fyzický měřicí přístroj navržený k emulaci akustických charakteristik průměrné dospělé lidské hlavy a trupu. To zahrnuje tvar, velikost a akustickou impedanci hlavy, ušních boltců, zvukovodů a simulátoru úst. HATS obsahuje vysoce věrné mikrofony umístěné v referenčních bodech uší (simulují uši posluchače) a reproduktor neboli umělá ústa v referenčním bodě úst (simulují ústa mluvčího). Tyto měniče jsou kalibrovány podle známých standardů, což umožňuje přesné měření akustických signálů.

Hlavní úlohou HATS v ekosystému 3GPP je umožnit standardizované testovací metodiky pro akustické charakteristiky terminálů (Terminal Acoustic Characteristics, [TAC](/mobilnisite/slovnik/tac/)) pro přenos řeči, jak jsou definovány ve specifikacích jako 3GPP TS 26.131 a 26.132. Při testování se testované zařízení ([DUT](/mobilnisite/slovnik/dut/)), například mobilní telefon, umístí standardizovaným způsobem k umělému uchu a ústům HATS. Testovací signály jsou přehrány přes umělá ústa, přijaty mikrofonem DUT, zpracovány kodekem DUT a sítí a poté vráceny a přehrány přes sluchátko nebo reproduktor DUT do umělých uší HATS. Mikrofony HATS tyto signály zachytí, což umožňuje analýzu klíčových parametrů, jako jsou hlasitostní úrovně pro vysílání a příjem (SLR, [RLR](/mobilnisite/slovnik/rlr/)), kmitočtová charakteristika, zkreslení a výkon při šumu na pozadí.

Toto uspořádání vytváří kontrolované, opakovatelné laboratorní prostředí, které eliminuje variabilitu způsobenou lidskými testovanými subjekty. Antropomorfní design HATS zajišťuje, že akustické vazby, difrakce a odrazové efekty přibližně odpovídají efektům u skutečného lidského uživatele, čímž jsou měření relevantní pro reálné použití. Shromážděná data se používají k ověření souladu s minimálními požadavky na výkon dle 3GPP, což zajišťuje základní úroveň kvality řeči a interoperability mezi zařízeními různých výrobců a síťovými prvky. Jeho použití sahá od tradičních hovorů v přepojování okruhů až po testování Voice over LTE (VoLTE) a Voice over NR (VoNR), čímž zajišťuje konzistentní hodnocení zvukové kvality s vývojem technologií jádra sítě.

## K čemu slouží

HATS byl zaveden, aby vyřešil zásadní problém subjektivního a nekonzistentního testování zvukové kvality v telekomunikačním průmyslu. Před jeho standardizací se výrobci a síťoví operátoři silně spoléhali na subjektivní poslechové testy s lidskými panelem. Tyto testy byly časově náročné, drahé a přinášely výsledky, které se lišily v závislosti na posluchačích, jejich sluchové ostrosti a podmínkách prostředí. To ztěžovalo objektivní srovnání akustického výkonu různých terminálů nebo prosazování konzistentních standardů kvality v celém odvětví.

Vytvoření HATS, standardizovaného ve 3GPP Release 8, bylo motivováno potřebou objektivní, opakovatelné a kvantifikovatelné metody pro hodnocení elektroakustického výkonu mobilních telefonů a dalších terminálů. Poskytuje spolehlivý referenční model lidského uživatele, což inženýrům umožňuje měřit klíčové přenosové parametry v laboratoři s vysokou přesností. Tento posun od subjektivního k objektivnímu testování byl klíčový pro hromadnou výrobu a certifikaci zařízení, umožnil rychlejší vývojové cykly, spolehlivé testování shody a zajištění minimální přijatelné kvality řeči pro koncové uživatele bez ohledu na použitý telefon nebo síť.

## Klíčové vlastnosti

- Standardizovaný antropomorfní model průměrné dospělé hlavy a trupu
- Integrovaná umělá ústa (reproduktor) a umělá ucha (mikrofony) v referenčních bodech
- Kalibrován pro přesné měření akustického tlaku a kmitočtové charakteristiky
- Umožňuje objektivní měření hlasitostních úrovní pro vysílání a příjem (SLR, RLR)
- Podporuje testování pro širokopásmové (WB) a superširokopásmové (SWB) řečové kodeky
- Základní prvek pro testování shody akustických charakteristik terminálů (TAC) dle 3GPP TS 26.131/132

## Definující specifikace

- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TS 43.058** (Rel-19) — Handsfree MS Transmission Quality Guidelines

---

📖 **Anglický originál a plná specifikace:** [HATS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hats/)
