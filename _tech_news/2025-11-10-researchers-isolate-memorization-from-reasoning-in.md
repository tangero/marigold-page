---
author: Marisa Aigen
category: ai
companies:
- OpenAI
- Anthropic
- DeepMind
- Google
- Microsoft
date: '2025-11-10 23:06:42'
description: Nový výzkum startupu Goodfire.ai ukazuje, že v jazykových modelech existují
  oddělené neuronové dráhy pro zapamatování textu a pro obecné uvažování, což umožňuje
  cíleně omezit memorování bez zásadního dopadu na schopnost řešit úlohy.
importance: 3
layout: tech_news_article
original_title: Researchers isolate memorization from reasoning in AI neural networks
  - Ars Technica
publishedAt: '2025-11-10T23:06:42+00:00'
slug: researchers-isolate-memorization-from-reasoning-in
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: Výzkumníci oddělili v AI sítích paměťové a logické schopnosti
url: https://arstechnica.com/ai/2025/11/study-finds-ai-models-store-memories-and-logic-in-different-neural-regions/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/07/surprised_robot_2-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/07/surprised_robot_2-1152x648.jpg
---

## Souhrn
Výzkumníci ze startupu Goodfire.ai publikovali analýzu, která naznačuje výrazně oddělené neuronové okruhy pro memorování a pro obecné uvažování v moderních jazykových modelech. Experimentálně ukazují, že lze výrazně omezit schopnost modelu doslova citovat tréninková data, aniž by se významně snížila jeho schopnost řešit úlohy, včetně logického uvažování a základní aritmetiky.

## Klíčové body
- Identifikace separovaných neuronových složek pro memorování a pro obecné uvažování v modelu OLMo-7B.
- Odstranění paměťových komponent vedlo k ~97% snížení schopnosti citovat tréninková data, při zachování většiny ostatních schopností.
- Analýza ukazuje systematické rozdělení: komponenty spojené s memorováním a s řešením obecných úloh se liší podle metriky „curvature“.
- Zjištění naznačují, že aritmetika a další „tvrdé“ dovednosti mohou sdílet stejné dráhy jako memorizační mechanismy.
- Výsledky mají přímý dopad na bezpečnost, ochranu osobních údajů a regulaci AI modelů.

## Podrobnosti
Startup Goodfire.ai, který se zaměřuje na bezpečnost, interpretovatelnost a řízení chování velkých jazykových modelů, analyzoval otevřený jazykový model OLMo-7B vyvinutý Allen Institute for AI. Pomocí metriky označované jako „curvature“ seřadili váhové komponenty (parametry modelu) podle toho, jak se podílejí na zpracování vstupů. Následné testy ukázaly, že komponenty s nejnižší hodnotou curvature vykazují vyšší aktivaci u přesně zapamatovaných pasáží z tréninkových dat, zatímco komponenty s nejvyšší curvature se více aktivují při práci s obecným, netréninkovým textem.

Tato separace umožnila provést cílený zásah: po odstranění spodní části těchto váhových komponent model ztratil přibližně 97 % schopnosti přesně reprodukovat tréninková data, ale jeho výkon v úlohách vyžadujících logické uvažování a práci s novými vstupy zůstal do značné míry zachován. To je v rozporu s dřívější představou, že memorování a generalizace jsou v modelech silně provázané a obtížně oddělitelné.

Pozoruhodným výsledkem je, že základní aritmetické schopnosti modelu se zdají být úzce svázány s těmito paměťovými drahami. To naznačuje, že část toho, co je běžně interpretováno jako „logické“ nebo „symbolické“ uvažování, může být ve skutečnosti emergentní efekt strukturovaného memorování a specifických reprezentací v parametrech modelu. Pokud se tento výsledek potvrdí i u větších a komerčních modelů, bude možné přesněji řídit, které informace model uchovává a jakým způsobem s nimi pracuje.

## Proč je to důležité
Tento výzkum má přímé důsledky pro bezpečnost a regulaci AI. Schopnost cíleně potlačit memorování s minimálním dopadem na užitečné schopnosti modelu by mohla pomoci snížit riziko úniku osobních údajů, chráněných textů nebo citlivých interních dokumentů, které se mohou v modelech objevit v důsledku tréninku na nevhodných datech. Z pohledu poskytovatelů služeb AI a provozovatelů API to otevírá cestu k technickým opatřením, která lépe vyhoví evropské regulaci a interním compliance požadavkům.

Zároveň jde o významný krok v interpretovatelnosti neuronových sítí: pokud lze oddělovat paměťové a „logické“ komponenty, zvyšuje to možnost modely systematicky ladit, auditovat a omezovat. Pro průmysl to znamená potenciál vytvářet modely navržené tak, aby byly méně náchylné k neřízenému citování tréninkových dat, aniž by se zásadně zhoršila jejich použitelnost v podnikovém prostředí, software nástrojích či asistenčních aplikacích. Současně výsledky zpochybňují jednoduché marketingové interpretace „schopnosti uvažování“ v AI a nutí výrobce modelů transparentněji vysvětlovat, jak k těmto schopnostem dochází.

---

[Číst původní článek](https://arstechnica.com/ai/2025/11/study-finds-ai-models-store-memories-and-logic-in-different-neural-regions/)

**Zdroj:** 🔬 Ars Technica
