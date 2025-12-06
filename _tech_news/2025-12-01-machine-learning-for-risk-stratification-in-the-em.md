---
author: Marisa Aigen
category: strojové učení
date: '2025-12-01 00:00:00'
description: Autoři prezentují randomizovanou kontrolovanou studii, která ukazuje,
  že model umělé inteligence RISK INDEX odhaduje riziko mortality pacienta stejně
  přesně jako lékaři a standardní rizikové skóre, ale neovlivnil klinická rozhodnutí
  v pohotovostním oddělení.
importance: 3
layout: tech_news_article
original_title: 'Machine learning for risk stratification in the emergency department
  (MARS-ED): a randomized controlled trial'
publishedAt: '2025-12-01T00:00:00+00:00'
slug: machine-learning-for-risk-stratification-in-the-em
source:
  emoji: 📰
  id: null
  name: Nature.com
title: 'Strojové učení pro stratifikaci rizik v pohotovostním oddělení (MARS-ED):
  randomizovaná kontrolovaná studie'
url: https://www.nature.com/articles/s41467-025-66947-7
---

## Souhrn
Randomizovaná kontrolovaná studie MARS-ED testovala model strojového učení RISK INDEX pro predikci 31denní mortality pacientů v pohotovostním oddělení. Model překonal tradiční klinické nástroje jako NEWS, APACHE II a SOFA v přesnosti, ale neměl žádný vliv na lékařská rozhodnutí ani výsledky léčby. Studie proběhla na Maastricht University Medical Center+ s 1303 pacienty.

## Klíčové body
- Model RISK INDEX dosáhl AUROC 0.84 pro predikci mortality, což překonalo klinickou intuici lékařů (AUROC 0.73–0.76) a standardní skóre (AUROC 0.65–0.75).
- Predikce modelu se shodovala s očekáváním lékařů jen v půlce případů, s největšími rozdíly u méně zkušených lékařů.
- Přístup k modelu změnil léčebný plán pouze v 1 z 644 případů (0,16 %).
- Žádné nežádoucí události spojené s intervencí, rekrutace proběhla podle plánu.
- Závěr: Přesnost predikce nestačí k změně klinické praxe v pohotovosti.

## Podrobnosti
Studie MARS-ED byla otevřená, randomizovaná, neinferenční trial zaměřená na dospělé pacienty (nad 18 let) v pohotovostním oddělení Maastricht University Medical Center+, kteří byli vyšetřeni internisty a měli alespoň čtyři laboratorní testy. Pacienti byli náhodně rozděleni 1:1 do dvou skupin: standardní péče (659 pacientů) nebo standardní péče s přístupem k RISK INDEX (644 pacientů). Model RISK INDEX, vyvinutý dříve, predikuje 31denní mortalitu na základě rutinních laboratorních hodnot, věku a pohlaví, bez nutnosti vitálních znaků, což ho činí praktickým pro přeplněné pohotovosti.

Primárními ukazateli byla prognostická přesnost (měřená AUROC) a klinický dopad. RISK INDEX dosáhl AUROC 0.84, což statisticky významně překonalo NEWS (0.65), APACHE II (0.72) a SOFA (0.75). Oproti klinické intuičně lékařů byl lepší (0.73–0.76), ale shoda predikcí s lékařskými očekáváními byla jen kolem 50 %, s většími nesrovnalostmi u juniorních lékařů. Přesto intervence nezměnila léčebné plány – pouze jeden případ – a lékaři vnímali nízkou přidanou hodnotu. Žádné změny v klinických výsledcích, jako délka hospitalizace nebo mortalita, nebyly pozorovány.

Tato studie poukazuje na limity aplikace strojového učení v reálné klinické praxi. I když model využívá rutinní data a je snadno integrovatelný, lékaři ho nebrali v úvahu při rozhodování. Možné důvody zahrnují nedůvěru v AI predikce, které se liší od jejich zkušeností, nebo absenci akčních doporučení. RISK INDEX slouží k rychlé stratifikaci rizik pro optimalizaci zdrojů v přeplněných pohotovostech, ale studie ukazuje, že přesnost sama o sobě nestačí – potřebná je uživatelsky přívětivá integrace a vzdělávání.

## Proč je to důležité
Tato studie zdůrazňuje klíčový problém v aplikaci strojového učení v medicíně: vysoká prognostická přesnost nevede automaticky k lepší péči. V širším kontextu AI v zdravotnictví, kde se modely jako tento testují pro predikci rizik, ukazuje na nutnost zaměřit se na uživatelskou adopci. Pro průmysl to znamená, že vývoj AI nástrojů musí zahrnovat nejen data-driven přesnost, ale i human-centered design, jako vysvětlitelnost predikcí (explainable AI) a integraci do workflow. Pro pohotovostní oddělení to znamená, že tradiční nástroje jako NEWS zůstávají dominantní, dokud AI nebude přizpůsobeno klinické realitě. Celkově přispívá k diskusi o translational research, kde vědecký pokrok naráží na praktické bariéry.

---

[Číst původní článek](https://www.nature.com/articles/s41467-025-66947-7)

**Zdroj:** 📰 Nature.com
