---
category: umělá inteligence
date: '2025-10-23 21:20:48'
description: Studie z amerických univerzit ukazuje, že jazykové modely trénované na
  krátkých, populárních a povrchních tweetech vykazují horší výsledky v testech a
  ztrácejí kognitivní schopnosti.
importance: 4
layout: tech_news_article
original_title: Researchers show that training on “junk data” can lead to LLM “brain
  rot” - Ars Technica
publishedAt: '2025-10-23T21:20:48+00:00'
slug: researchers-show-that-training-on-junk-data-can-le
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: Výzkumníci prokázali, že trénink na "nekvalitních datech" vede k degradaci
  jazykových modelů
url: https://arstechnica.com/ai/2025/10/researchers-show-that-training-on-junk-data-can-lead-to-llm-brain-rot/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/10/GettyImages-1908316227-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/10/GettyImages-1908316227-1152x648.jpg
---

## Souhrn

Výzkumníci z Texas A&M, University of Texas a Purdue University publikovali studii, která kvantifikuje dopady tréninku velkých jazykových modelů na nekvalitních datech. Jejich výzkum ukazuje, že kontinuální trénink na "junk" obsahu z webu vede k trvalému poklesu výkonu modelů, což autoři přirovnávají k lidskému "brain rot" - degradaci kognitivních schopností způsobené konzumací triviálního online obsahu.

## Klíčové body

- Výzkumníci definovali "LLM brain rot hypotézu" - kontinuální předtrénink na nekvalitních webových textech způsobuje trvalý kognitivní úpadek jazykových modelů
- Pro testování použili dataset 100 milionů tweetů z HuggingFace, které rozdělili na "junk" a kontrolní skupinu
- Jako "junk" data identifikovali tweety s vysokou mírou engagement (lajky, retweety), ale krátkou délkou a povrchním obsahem
- Druhá metrika hodnocení využívala GPT-4o k identifikaci tweetů se "sémantickou nekvalitou" - konspirační teorie, přehnané tvrzení, nepodložená prohlášení
- Modely trénované na těchto datech vykazovaly horší výsledky v benchmarkových testech

## Podrobnosti

Výzkum vychází z existujících studií o dopadu nekvalitního online obsahu na lidský mozek. Podobně jako lidé, kteří konzumují velké objemy triviálního a intelektuálně nenáročného obsahu, mohou trpět problémy s pozorností, pamětí a sociálním poznáváním, i jazykové modely vykazují podobné symptomy degradace při tréninku na obdobných datech.

Klíčovou výzvou výzkumu bylo objektivní definování toho, co představuje "nekvalitní" obsah. Výzkumníci zvolili dva přístupy. První vycházel z předpokladu, že "brain rot" u lidí je důsledkem internetové závislosti, proto jako junk data označili tweety maximalizující engagement triviálním způsobem - konkrétně populární tweety s vysokým počtem interakcí, ale krátkou délkou. Hypotéza byla, že populárnější, ale kratší tweety budут považovány za nekvalitní data.

Druhý přístup využíval marketingový výzkum k definici "sémantické kvality" samotných tweetů. Pomocí komplexního promptu pro GPT-4o výzkumníci identifikovali tweety zaměřené na povrchní témata jako konspirační teorie, přehnané nároky, nepodložená tvrzení nebo povrchní lifestyle obsah.

Výsledky studie mají zásadní dopady na současný vývoj AI, kdy se firmy potýkají s nedostatkem kvalitních trénovacích dat a často sahají k syntetickým datům nebo méně kvalitním zdrojům.

## Proč je to důležité

Tato studie přichází v kritickém okamžiku pro vývoj velkých jazykových modelů. S vyčerpáváním kvalitních veřejně dostupných dat se firmy stále častěji obracejí k alternativním zdrojům, včetně sociálních sítí a synteticky generovaného obsahu. Výzkum poskytuje první kvantitativní důkazy o tom, jak zásadní dopad má kvalita trénovacích dat na dlouhodobý výkon modelů.

Pro průmysl to znamená nutnost přehodnotit strategie získávání trénovacích dat. Zatímco dosud převládal přístup "čím více dat, tím lépe", tento výzkum ukazuje, že nekvalitní data mohou způsobit trvalé poškození modelů. To má důsledky pro celý ekosystém AI - od vývojářů modelů přes poskytovatele datových sad až po koncové uživatele, kteří spoléhají na výkon těchto systémů.

Výzkum také otevírá otázky o budoucnosti webového obsahu. S rostoucím množstvím AI-generovaného textu na internetu hrozí riziko zpětné vazby, kdy modely budou trénovány na obsahu vytvořeném předchozími generacemi AI, což může vést k další degradaci kvality.

---

[Číst původní článek](https://arstechnica.com/ai/2025/10/researchers-show-that-training-on-junk-data-can-lead-to-llm-brain-rot/)

**Zdroj:** 🔬 Ars Technica
