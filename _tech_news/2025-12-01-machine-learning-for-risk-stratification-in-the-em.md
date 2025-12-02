---
author: Marisa Aigen
category: strojové učení
date: '2025-12-01 00:00:00'
description: Autoři popisují randomizovanou kontrolovanou studii, která ukázala, že
  model umělé inteligence RISK INDEX odhaduje riziko úmrtnosti pacienta stejně přesně
  jako lékaři a standardní rizikové skóre, ale neovlivnil klinická rozhodnutí v pohotovostním
  oddělení.
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

### Souhrn
Randomizovaná kontrolovaná studie MARS-ED testovala nástroj RISK INDEX založený na strojovém učení pro predikci 31denní mortality pacientů v pohotovostním oddělení. Model překonal tradiční klinické skóre jako NEWS, APACHE II a SOFA i lékařskou intuici, ale v praxi nezměnil lékařská rozhodnutí ani výsledky léčby. Výsledky naznačují, že vysoká prognostická přesnost nestačí pro reálný klinický dopad.

### Klíčové body
- Prognostická přesnost RISK INDEX (AUROC 0,84) překonala klinickou intuici (AUROC 0,73–0,76) a tradiční skóre (NEWS, APACHE II, SOFA: AUROC 0,65–0,75).
- Model souhlasil s očekáváním lékařů jen v půlce případů, s největším nesouladem u méně zkušených specialistů.
- Žádný vliv na klinickou praxi: změna léčebného plánu v pouhém 1 z 644 případů (0,16 %).
- Studie zahrnovala 1303 dospělých pacientů v pohotovostním oddělení Maastricht University Medical Center+.
- Nebyly zaznamenány nežádoucí události spojené s intervencí.

### Podrobnosti
Studie MARS-ED byla otevřená, randomizovaná, neinferenční trial provedená v pohotovostním oddělení univerzitní nemocnice v Maastrichtu. Do ní byli zařazeni dospělí pacienti (nad 18 let), kteří prošli vyšetřením internisty a měli k dispozici nejméně čtyři rutinní laboratorní testy. Pacienti byli náhodně rozděleni v poměru 1:1 do dvou skupin: standardní péče (659 pacientů) nebo standardní péče s přístupem k RISK INDEX (644 pacientů). Řádiči nemohli být oslepeni, protože museli vidět predikce modelu.

RISK INDEX je nástroj strojového učení vyvinutý dříve pro predikci 31denní mortality na základě rutinních laboratorních hodnot, věku a pohlaví pacienta. Na rozdíl od tradičních nástrojů jako NEWS (National Early Warning Score, který sleduje vitální funkce), APACHE II (Acute Physiology and Chronic Health Evaluation II, komplexní skóre pro intenzivní péči) nebo SOFA (Sequential Organ Failure Assessment, hodnocení selhání orgánů), nevyžaduje složité vstupy a je navržen pro rychlou stratifikaci rizik v přeplněných pohotovostech. Primárními ukazateli byla prognostická přesnost pro 31denní úmrtnost a klinický dopad.

Výsledky ukázaly, že RISK INDEX dosáhl AUROC 0,84, což je statisticky významně lepší než u srovnatelných metod. Přesto predikce modelu nesouhlasily s klinickou intuicí lékařů v přibližně polovině případů, zejména u mladších nebo méně zkušených internistů. Přestože byl model k dispozici, lékaři ho ignorovali: došlo k pouze jedné změně léčebného plánu a žádným změnám v klinických výsledcích. Lékaři sami hodnotili přidanou hodnotu modelu jako nízkou. Rekrutace proběhla podle plánu bez komplikací.

Tato studie poukazuje na praktické limity nasazení strojového učení v medicíně. I když model funguje na rutinních datech bez potřeby vitálních parametrů, což ho činí snadno dostupným, chybí mu integrace do pracovního postupu lékařů. Nesoulad s jejich očekáváním vede k nedůvěře, což brání adopci.

### Proč je to důležité
Výsledky MARS-ED mají širší implikace pro nasazení AI v zdravotnictví. Ukazují, že prognostická přesnost (např. vysoké AUROC) nestačí – nutné je uživatelsky přizpůsobené řešení s akčními doporučeními, které lékaři snadno pochopí a aplikují. V kontextu rostoucího tlaku na pohotovosti kvůli přeplněnosti to zdůrazňuje potřebu klinických trialů před komerčním nasazením modelů strojového učení. Pro vývojáře AI v medicíně to znamená zaměřit se na human factors, jako je vysvětlitelnost predikcí a integrace do elektronických zdravotnických záznamů. Studie tak přispívá k realističtějšímu pohledu na translational research, kde teoretické pokroky narážejí na praktické bariéry v reálném prostředí.

---

[Číst původní článek](https://www.nature.com/articles/s41467-025-66947-7)

**Zdroj:** 📰 Nature.com
