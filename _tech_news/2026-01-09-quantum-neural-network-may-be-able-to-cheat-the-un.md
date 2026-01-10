---
author: Marisa Aigen
category: kvantová ai
date: '2026-01-09 16:00:02'
description: Výpočty ukazují, že vnášení náhodnosti do kvantové neuronové sítě by
  mohlo umožnit určení vlastností kvantových objektů, které jsou jinak zásadně těžko
  dostupné. Tento přístup by usnadnil měření vlastností qubitů v kvantových počítačích.
importance: 4
layout: tech_news_article
original_title: Quantum neural network may be able to cheat the uncertainty principle
publishedAt: '2026-01-09T16:00:02+00:00'
slug: quantum-neural-network-may-be-able-to-cheat-the-un
source:
  emoji: 📰
  id: new-scientist
  name: New Scientist
title: Kvantová neuronová síť by mohla obejít Heisenbergův princip neurčitosti
url: https://www.newscientist.com/article/2509710-quantum-neural-network-may-be-able-to-cheat-the-uncertainty-principle/
urlToImage: https://images.newscientist.com/wp-content/uploads/2026/01/08115807/SEI_278889465.jpg
urlToImageBackup: https://images.newscientist.com/wp-content/uploads/2026/01/08115807/SEI_278889465.jpg
---

## Souhrn
Výzkumníci z Čínské akademie věd pod vedením Duanlua Zhoua matematicky prokázali, že kvantové neuronové sítě s vnesenou náhodností dokážou obejít omezení Heisenbergova principu neurčitosti. Tento princip brání současnému přesnému měření některých vlastností kvantových objektů, jako je poloha a hybnost částice. Nový přístup by mohl zlepšit analýzu qubitů v kvantových počítačích.

## Klíčové body
- Matematický důkaz pro použití kvantových neuronových sítí k odhadu neslučitelných kvantových veličin.
- Vnášení náhodnosti eliminuje interference mezi měřeními.
- Praktické aplikace na benchmarking kvantových počítačů a simulaci molekul či materiálů.
- Porovnání s klasickými operacemi: podobné jako dělení čísla dvěma pro určení sudosti, ale bez narušení kvantového stavu.
- Výzkum řeší problémy v kvantovém výpočtu spojené s kompatibilitou měření.

## Podrobnosti
Heisenbergův princip neurčitosti stanovuje fundamentální limit pro současné měření komplementárních vlastností kvantových objektů, například polohy a hybnosti částice nebo energie a fáze v kvantových systémech. V praxi to komplizuje práci s kvantovými počítači, kde qubity – základní stavební bloky – vyžadují přesné charakterizace pro benchmarking zařízení nebo pro efektivní simulaci složitých systémů jako molekuly a materiály. Tradiční měření narušuje stav qubitu, což vede k neslučitelným operacím: například pokud přesně změříte hybnost, následné měření polohy poskytne jen aproximaci.

Tým Duanlua Zhoua navrhl řešení pomocí kvantových neuronových sítí, což jsou analogie klasických neuronových sítí přizpůsobené kvantovému prostředí. Tyto sítě zpracovávají kvantové stavy a učí se mapovat vstupy na výstupy prostřednictvím vrstev kvantových bran. Klíčovým prvkem je injekce náhodnosti do sítě, která umožňuje souběžné odhady více vlastností bez přímé interference. Matematicky prokázali, že taková síť dokáže rekonstruovat vlastnosti qubitů, které by byly jinak nedosažitelné, tím že agreguje výsledky z více náhodných runů.

Pro srovnání: v klasickém počítači lze číslo otestovat na sudost dělením dvěma, ale v kvantovém světě odpovídající operace mohou být neslučitelné, podobně jako nesnáze násobit třemi a pak dělit dvěma bez ztráty informace. Kvantové neuronové sítě tento problém řeší učením se z datových sad získaných opakovanými měřeními, kde náhodnost simuluje statistické vzorky. Výzkum se zaměřil na praktické scénáře, jako je predikce vlastností chemicky užitečných molekul nebo hodnocení výkonu kvantových čipů. Čínská akademie věd, kde výzkum proběhl, je jednou z předních institucí v kvantovém výzkumu a rozvíjí technologie pro národní kvantové počítače.

Ačkoli jde o teoretický důkaz, nabízí cestu k implementaci v existujících platformách jako IBM Quantum nebo Google Sycamore, kde by kvantové neuronové sítě sloužily k optimalizaci algoritmů. Potřebuje však experimentální validaci, protože reálné qubity trpí hlukem a dekohorencí.

## Proč je to důležité
Tento přístup by mohl urychlit vývoj kvantových počítačů tím, že usnadní charakterizaci qubitů a umožní přesnější simulace reálných systémů, což je klíčové pro chemii, farmacii a materiálový výzkum. V kontextu kvantové AI posiluje schopnosti neuronových sítí v hybridních systémech, kde klasická AI řídí kvantové procesy. Pro průmysl znamená potenciální quantum advantage v oblastech, kde současné superpočítače selhávají, jako optimalizace molekul pro léky. Nicméně jako teoretický výsledek vyžaduje další testy na hardwaru, aby se prokázala škálovatelnost za současných omezení kvantových systémů s desítkami qubitů.

---

[Číst původní článek](https://www.newscientist.com/article/2509710-quantum-neural-network-may-be-able-to-cheat-the-uncertainty-principle/)

**Zdroj:** 📰 New Scientist
