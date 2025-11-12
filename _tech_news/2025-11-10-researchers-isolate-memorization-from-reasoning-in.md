---
author: Marisa Aigen
category: ai
date: '2025-11-10 23:06:42'
description: Nová studie startupu Goodfire.ai ukazuje, že memorování tréninkových
  dat a logické uvažování v jazykových modelech probíhají ve výrazně oddělených neurálních
  drahách. Odstranění paměťových komponent výrazně sníží schopnost přesné citace,
  aniž by zásadně ovlivnilo schopnost řešit úlohy.
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
title: Výzkumníci oddělili v AI sítích paměťové a logické mechanismy
url: https://arstechnica.com/ai/2025/11/study-finds-ai-models-store-memories-and-logic-in-different-neural-regions/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/07/surprised_robot_2-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/07/surprised_robot_2-1152x648.jpg
---

## Souhrn
Výzkum startupu Goodfire.ai naznačuje, že velké jazykové modely (LLM) využívají odlišné vnitřní mechanismy pro memorování tréninkových dat a pro obecné „reasoning“ schopnosti. Autoři demonstrují, že cíleným zásahem do konkrétních váhových komponent lze zásadně omezit přesnou reprodukci tréninkových dat, aniž by došlo k významné degradaci schopnosti modelu řešit nové úlohy.

## Klíčové body
- Analýza OLMo-7B ukazuje výrazné oddělení „memorization“ a „reasoning“ drah ve středních vrstvách sítě.
- Odstraněním vybraných váhových komponent se snížila schopnost přesné citace tréninkových dat o cca 97 %, zatímco logické schopnosti zůstaly převážně zachovány.
- Komponenty s vyšší aktivitou na memorovaných datech se systematicky soustředily v dolní části pořadí podle tzv. curvature, zatímco komponenty pro obecný text byly v horní části.
- Výzkum naznačuje, že i základní aritmetika využívá stejné dráhy jako memorování, což zpochybňuje představu o „čistě logickém“ počítání v dnešních LLM.
- Zjištění má přímé dopady na ochranu dat, auditovatelnost modelů a regulaci úniků tréninkových dat.

## Podrobnosti
Studie vychází z analýzy otevřeného jazykového modelu OLMo-7B, vyvinutého Allen Institute for AI. Goodfire.ai, menší výzkumný startup specializující se na interpretovatelnost a bezpečnost modelů AI, se zaměřil na strukturu vnitřních váh neuronové sítě. Použil metriku nazývanou „curvature“ pro seřazení jednotlivých váhových komponent podle jejich chování při zpracování vstupů. Zjednodušeně jde o způsob, jak kvantifikovat, jak silně a nelineárně daná komponenta reaguje na různé typy dat.

Výzkumníci poté porovnali aktivaci těchto komponent na dvou typech vstupů: (1) přesně memorované pasáže z tréninkových dat a (2) nové, na tréninku nepoužité texty. Ukázalo se, že spodních 50 % komponent podle curvature vykazuje zřetelně vyšší aktivitu na memorovaných textech (zhruba o 23 %), zatímco horních 10 % je aktivnější na obecném textu (zhruba o 26 %). To naznačuje funkční specializaci: dolní část spektra obsluhuje převážně zapamatovaný obsah, horní část se podílí na obecnějším zpracování a odvozování.

Klíčový experiment spočíval v „chirurgickém“ odstranění nebo deaktivaci těch komponent, které byly identifikovány jako dominantně paměťové. Po tomto zásahu se model stal výrazně horším v přesné reprodukci tréninkových pasáží (pokles o cca 97 %), ale jeho výkon v úlohách vyžadujících obecné porozumění textu a určitou formu reasoning se zhoršil jen minimálně. Překvapivým zjištěním je, že stejná paměťová infrastruktura zřejmě podporuje i část schopností v základní aritmetice, což zpochybňuje jednoduché dělení na „logické“ a „paměťové“ výpočty v současných LLM.

Pro průmyslovou praxi to znamená, že může být technicky možné navrhovat modely s omezeným nebo kontrolovaným memorováním, bez zásadního poškození užitečných schopností, jako je shrnování, generování textu, překlad nebo kódování. Takový přístup může být relevantní pro poskytovatele AI služeb přes API, kteří čelí regulatorním požadavkům na ochranu tréninkových dat a snižování rizika úniků citlivého obsahu.

## Proč je to důležité
Tento výzkum je významný z hlediska interpretovatelnosti a bezpečnosti AI modelů. Ukazuje, že únik tréninkových dat není pouze nevyhnutelným vedlejším efektem velikosti modelu, ale lze jej cíleně technicky omezovat. To má přímé důsledky pro dodržování ochrany osobních údajů, obchodního tajemství a autorských práv, zejména u poskytovatelů generativní AI ve velkém měřítku.

Oddělení paměťových a reasoning drah otevírá možnost navrhovat modely, které lépe vyhovují regulatorním rámcům a smluvním požadavkům: například modely, které nebudou schopny přesně citovat chráněná díla, ale zachovají schopnost analyzovat a vysvětlovat obsah. Zároveň však studie ukazuje, že některé zdánlivě „logické“ schopnosti (např. aritmetika) jsou úzce svázané s memorizačními strukturami. To naznačuje, že současné LLM nejsou skutečné logické systémy, ale statistické stroje s komplikovaným překryvem mezi pamětí a odvozováním. Pro vývoj budoucích modelů to představuje jak příležitost pro přesnější kontrolu chování, tak varování, že odlišit „bezpečné“ a „rizikové“ komponenty nebude vždy triviální.

---

[Číst původní článek](https://arstechnica.com/ai/2025/11/study-finds-ai-models-store-memories-and-logic-in-different-neural-regions/)

**Zdroj:** 🔬 Ars Technica
