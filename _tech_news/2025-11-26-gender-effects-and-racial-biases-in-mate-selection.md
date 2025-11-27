---
author: Marisa Aigen
category: ai a společnost
date: '2025-11-26 00:00:00'
description: Výzkum publikovaný v časopise Scientific Reports využil strojové učení
  k analýze dat ze speed datingů a odhalil vliv pohlaví a rasy na vzájemný zájem účastníků.
importance: 3
layout: tech_news_article
original_title: Gender effects and racial biases in mate selection as revealed by
  machine learning
publishedAt: '2025-11-26T00:00:00+00:00'
slug: gender-effects-and-racial-biases-in-mate-selection
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Pohlavní rozdíly a rasová zaujatost ve výběru partnerů odhalené strojovým učením
url: https://www.nature.com/articles/s41598-025-25028-x
---

## Souhrn
Výzkumníci využili pokročilé metody strojového učení (ML) k analýze dat ze speed datingů a zjistili, že ML modely dokážou předpovědět vzájemný zájem účastníků s přesností 85,4–86,4 %. Zároveň prokázali, že modely „oslepené“ vůči rasovým informacím dosahují srovnatelné přesnosti, což otevírá cestu k etičtějším aplikacím v oblasti online randění.

## Klíčové body
- ML modely (LGBM, náhodný les, logistická regrese, atd.) dosáhly přesnosti přes 85 % při predikci vzájemného zájmu.
- Byly testovány různé metody výběru příznaků (feature selection), včetně filter-based a embedded přístupů.
- Rasově neutrální modely dosahují téměř stejné přesnosti jako ty využívající rasové údaje.
- Výzkum použil veřejně dostupná data a open-source nástroje, což zajišťuje reprodukovatelnost výsledků.

## Podrobnosti
Výzkum analyzoval veřejně dostupnou datovou sadu ze speed datingů (OpenML ID: 40536), která obsahuje informace o preferencích, demografii a rozhodnutích účastníků. Autoři nasadili širokou škálu ML algoritmů – od LightGBM přes náhodný les až po k nejbližších sousedů – a kombinovali je s různými metodami výběru příznaků, aby identifikovali ty nejrelevantnější faktory pro predikci „matche“. Zásadní zjištění spočívá v tom, že i když rasové informace zvyšují přesnost modelu jen minimálně, lze je zcela vynechat bez výrazného poklesu výkonu. To naznačuje, že chování a preference účastníků jsou silnějšími prediktory než demografické kategorie. Výzkumníci také navrhují pohlaví-specifické modely, které lépe zachycují rozdíly v partnerství mezi muži a ženami.

## Proč je to důležité
Tento výzkum přispívá k probíhající diskusi o etice AI v citlivých sociálních oblastech, jako je randění nebo nábor. Ukazuje, že technologické řešení rasové zaujatosti nemusí znamenat obětování přesnosti – naopak, důraz na chování a preference může vést k inkluzivnějším systémům. Pro vývojáře rande aplikací to znamená, že je možné navrhovat doporučovací algoritmy, které nebudou posilovat stereotypy nebo diskriminaci. Zároveň výzkum demonstruje, jak open-source data a nástroje (např. software df-analyze na GitHubu) umožňují transparentní a ověřitelný výzkum v oblasti AI a společnosti.

---

[Číst původní článek](https://www.nature.com/articles/s41598-025-25028-x)

**Zdroj:** 📰 Nature.com
