---
author: Marisa Aigen
category: umělá inteligence
companies:
- Google
- OpenAI
- DeepSeek
date: '2026-02-14 11:02:11'
description: Google a OpenAI varují, že konkurenti včetně čínské DeepSeek zkoumají
  jejich modely AI, aby ukradli základní uvažovací mechanismy a převzali je do svých
  systémů. Tento proces nazývá Google „distillation attacks“ a detekoval ho v reálném
  čase na modelu Gemini.
importance: 5
layout: tech_news_article
original_title: 'How AI could eat itself: Competitors can probe models to steal their
  secrets and clone them'
publishedAt: '2026-02-14T11:02:11+00:00'
slug: how-ai-could-eat-itself-competitors-can-probe-mode
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: 'Jak by se AI mohla sežrat sama: Konkurenti mohou sondovat modely, ukrást jejich
  tajemství a klonovat je'
url: https://www.theregister.com/2026/02/14/ai_risk_distillation_attacks/
urlToImage: https://regmedia.co.uk/2017/02/21/clone_army_star_wars.jpg
urlToImageBackup: https://regmedia.co.uk/2017/02/21/clone_army_star_wars.jpg
---

### Souhrn
Dvě největší firmy v oblasti AI, Google a OpenAI, tento týden upozornily na hrozbu, kdy konkurenti jako čínská DeepSeek systematicky testují jejich velké jazykové modely (LLM), aby získali data o jejich interním uvažování a následně tyto schopnosti napodobily ve svých vlastních modelech. Google tento typ útoku označuje jako „distillation attacks“, při kterých útočníci používají tisíce promptů k extrakci logiky modelu. I přes detekci v reálném čase zůstává toto riziko obtížně odstranitelné.

### Klíčové body
- Google Threat Intelligence Group identifikoval kampaň s více než 100 000 prompty zaměřenou na replikaci uvažování modelu Gemini v neanglických jazycích.
- Útočníci jsou soukromé firmy z celého světa, včetně Číny, které chtějí levněji napodobit drahé LLM za miliardy dolarů.
- DeepSeek, čínská firma specializující se na vývoj open-source AI modelů, je zmíněna jako příklad takového aktéra.
- Distilace porušuje podmínky služby Google a ohrožuje hodnotu duševního vlastnictví v AI.
- Google ochránil své interní stopy uvažování, ale riziko nelze plně eliminovat.

### Podrobnosti
Článek popisuje nový typ intelektuálního vlastnictví v oblasti AI, kde konkurenti zneužívají legitimní přístup k veřejným rozhraním (API) modelů jako Gemini nebo GPT. Tyto modely, trénované na miliardách dolarů, skrývají složité interní procesy uvažování, které umožňují řešit úlohy od překladu po programování. Útočníci posílají tisíce specifických promptů – textových instrukcí –, aby mapovali, jak model reaguje na různé scénáře. Získaná data pak slouží k tréninku vlastních menších modelů, což dramaticky snižuje náklady na vývoj.

John Hultquist z Google Threat Intelligence Group uvedl, že jde o soukromé firmy z celého světa, které vidí v AI klíčovou technologii s nekonečným zájmem o replikaci. Konkrétně kampaň na Gemini použila přes 100 000 promptů v neanglických jazycích napříč širokou škálou úkolů, aby zachytila uvažovací schopnosti. Google to detekoval v reálném čase a zablokoval přístup k citlivým stopám (reasoning traces), které ukazují krok za krokem myšlení modelu. OpenAI podobně varuje před takovými praktikami.

DeepSeek, čínská společnost zaměřená na vývoj výkonných open-source LLM jako DeepSeek-V2, je explicitně zmíněna jako příklad. Tyto modely slouží k tvorbě textu, kódu nebo analýz a konkurují západním alternativám nižšími náklady. Distilace umožňuje firmám jako DeepSeek přeskočit fázi drahého tréninku na obřích datech a GPU clusterech, což urychluje globální soutěž. Nicméně toto zneužití otevírá dveře k dalším rizikům, jako je únik proprietárních znalostí nebo zneužití k škodlivým účelům.

### Proč je to důležité
Tento vývoj odhaluje zranitelnost AI ekosystému, kde miliardové investice do LLM mohou být snadno napodobeny, což oslabuje konkurenční výhodu firem jako Google nebo OpenAI. Pro průmysl znamená levnější vstup do AI pro menší hráče, včetně států jako Čína, což urychluje globální proliferaci pokročilých systémů, ale zároveň zvyšuje rizika jako šíření dezinformací nebo kybernetické útoky. Uživatelé pocítí dopady v podobě rychlejšího nasazení levných klonů, které mohou být méně bezpečné. Dlouhodobě to nutí vývojáře k posílení ochrany, například omezením API nebo vodoznaky v výstupech, což ovlivní dostupnost AI pro širokou veřejnost. V kontextu eskalující AI závodnosti to podtrhuje potřebu nových standardů pro ochranu IP v digitální éře.

---

[Číst původní článek](https://www.theregister.com/2026/02/14/ai_risk_distillation_attacks/)

**Zdroj:** 📰 Theregister.com
