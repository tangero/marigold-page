---
author: Marisa Aigen
category: ai
date: '2025-11-10 23:06:42'
description: Nová studie startupu Goodfire.ai ukazuje, že schopnost modelů AI přesně
  reprodukovat tréninková data je oddělitelná od jejich logického a aritmetického
  uvažování, což otevírá cestu k cílenému omezování memorování bez ztráty užitečných
  schopností.
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
title: Výzkumníci oddělili v AI sítích paměťové a logické dráhy
url: https://arstechnica.com/ai/2025/11/study-finds-ai-models-store-memories-and-logic-in-different-neural-regions/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/07/surprised_robot_2-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/07/surprised_robot_2-1152x648.jpg
---

## Souhrn
Výzkumný tým ze startupu Goodfire.ai představil analýzu, která naznačuje, že velké jazykové modely mají zřetelně oddělené neuronové dráhy pro memorování konkrétního textu a pro obecné „reasoning“ schopnosti, včetně základní aritmetiky. Ukazují, že odstraněním vybraných váhových komponent lze dramaticky omezit schopnost modelu doslovně citovat tréninková data, aniž by výrazně utrpěl jeho výkon v logických úlohách.

## Klíčové body
- Goodfire.ai identifikoval oddělené neuronové komponenty odpovědné za memorování a za obecné uvažování.
- Při odstranění memorizačních komponent klesla schopnost přesného citování tréninkových dat o cca 97 %, zatímco logické schopnosti zůstaly téměř zachovány.
- Analýza byla prováděna mimo jiné na modelu OLMo-7B od Allen Institute for AI.
- Komponenty spojené s memorováním se soustředily v dolní části žebříčku podle tzv. curvature metriky, zatímco komponenty pro obecný text a řešení úloh v horní části.
- Základní aritmetické operace se překvapivě vážou spíše na stejné dráhy jako memorování než na „logické“ obvody.

## Podrobnosti
Goodfire.ai, menší výzkumný startup zaměřený na interpretovatelnost a bezpečnost modelů AI, publikoval preprint, ve kterém systematicky analyzuje vnitřní strukturu jazykového modelu OLMo-7B (open-source model Allen Institute for AI). Cílem bylo zjistit, zda jsou schopnosti modelu jako přesná reprodukce tréninkového textu a řešení nových úloh založené na stejných, nebo odlišných parametrech.

Výzkumníci použili metodu založenou na metrice „curvature“, která hodnotí, jak citlivé jsou jednotlivé váhy modelu na změny vstupu a jak se podílejí na různých typech úloh. Váhy v jedné z vnitřních vrstev (např. vrstva 22) seřadili podle této metriky a následně zkoumali jejich aktivaci při dvou typech dat: memorovaných (tj. text shodný nebo velmi blízký tréninkovým vzorkům) a nememorovaných (nový, obecný text).

Ukázalo se, že spodních 50 % váhových komponent vykazovalo výrazně vyšší aktivitu na memorovaných textech, zatímco horních 10 % se aktivovalo více u obecného textu a úloh vyžadujících zobecnění. Tato relativně čistá separace umožnila experimentální zásah: odstranění („vynulování“) spodních komponent vedlo k zásadnímu omezení schopnosti doslova citovat tréninková data, ale výkon v testech logického uvažování a obecného porozumění zůstal převážně zachován.

Zajímavým a potenciálně kontroverzním zjištěním je, že některé aritmetické schopnosti modelu – základní počty a jednoduché operace – byly více provázány s memorizačními drahami než s obvody, které model využívá k řešení obecných úloh. To naznačuje, že část „matematických schopností“ současných modelů může být spíše naučený vzorec a asociace než skutečné symbolické uvažování.

## Proč je to důležité
Studie je relevantní pro vývoj bezpečnějších a regulacím lépe vyhovujících modelů AI. Pokud lze technicky oddělit a cíleně potlačit paměťové dráhy, je možné snížit riziko úniku chráněných tréninkových dat (osobní údaje, interní dokumenty, licencovaný obsah), aniž by bylo nutné obětovat užitečné funkce modelu. To má přímý dopad na poskytovatele velkých modelů, podnikové nasazení AI i na právní a regulatorní debaty kolem autorského práva a ochrany dat.

Pro průmysl to také znamená, že se otevírá cesta k jemnějšímu ladění modelů: místo hrubých filtrů výstupu lze zasahovat do konkrétních vrstev a komponent. Současně výsledek zpochybňuje některá marketingová tvrzení o „logickém“ charakteru schopností modelů, zejména v oblasti aritmetiky. Z hlediska dlouhodobého vývoje to posiluje důraz na interpretovatelnost a mechanistickou analýzu neuronových sítí jako nezbytný krok k důvěryhodným a lépe kontrolovatelným systémům AI.

---

[Číst původní článek](https://arstechnica.com/ai/2025/11/study-finds-ai-models-store-memories-and-logic-in-different-neural-regions/)

**Zdroj:** 🔬 Ars Technica
