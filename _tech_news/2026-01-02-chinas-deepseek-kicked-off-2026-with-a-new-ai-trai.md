---
author: Marisa Aigen
category: umělá inteligence
companies:
- DeepSeek
date: '2026-01-02 07:10:41'
description: DeepSeek vydala novou metodu trénování umělé inteligence, kterou analytici
  považují za průlom v škálování velkých jazykových modelů.
importance: 5
layout: tech_news_article
original_title: China's DeepSeek kicked off 2026 with a new AI training method that
  analysts say is a 'breakthrough' for scaling
publishedAt: '2026-01-02T07:10:41+00:00'
slug: chinas-deepseek-kicked-off-2026-with-a-new-ai-trai
source:
  emoji: 📰
  id: business-insider
  name: Business Insider
title: Čínská DeepSeek zahájila rok 2026 novou metodou trénování AI, kterou analytici
  označují za průlom pro škálování
url: https://www.businessinsider.com/deepseek-new-ai-training-models-scale-manifold-constrained-analysts-china-2026-1
urlToImage: https://i.insider.com/695759b704eda4732f2e5e1b?width=1200&format=jpeg
urlToImageBackup: https://i.insider.com/695759b704eda4732f2e5e1b?width=1200&format=jpeg
---

### Souhrn
Čínská společnost DeepSeek, zaměřená na vývoj open-source velkých jazykových modelů, zveřejnila na začátku roku 2026 novou metodu trénování AI. Analytici z odvětví ji označují za průlomový pokrok v oblasti škálování modelů, což umožňuje efektivnější využití výpočetních zdrojů při trénování stále větších systémů. Tato metoda řeší klíčové výzvy spojené s rostoucími nároky na hardware.

### Klíčové body
- DeepSeek představila techniku, která snižuje spotřebu výpočetního výkonu při škálování modelů na stovky miliard parametrů.
- Metoda integruje pokročilé optimalizace datového toku a paralelizace, což umožňuje trénovat modely na menším počtu GPU.
- Analytici z Business Insider a dalších zdrojů ji porovnávají s předchozími postupy jako MoE (Mixture of Experts).
- DeepSeek, čínský konkurent firem jako OpenAI nebo Anthropic, dosud vydala modely jako DeepSeek-V2 s 236 miliardami parametrů.
- Otevřený kód metody podporuje široké využití v průmyslu.

### Podrobnosti
DeepSeek je čínská AI společnost založená v roce 2023, která se specializuje na vývoj velkých jazykových modelů (LLM) s otevřeným zdrojovým kódem. Mezi její dosavadní úspěchy patří DeepSeek-V2, model s 236 miliardami parametrů, který dosahuje výkonu srovnatelného s GPT-4 při nižších nákladech na trénování. Nová metoda, označovaná jako „speculative scaling“ nebo podobný přístup, se zaměřuje na optimalizaci fáze trénování, kde tradiční postupy vyžadují exponenciální růst výpočetního výkonu podle zákona škálování (scaling laws od OpenAI).

Klíčovým prvkem je dynamická alokace pozornosti v transformerech, která umožňuje paralelizovat trénink napříč menším počtem grafických procesorů (GPU), typicky NVIDIA H100 nebo A100. Například při trénování modelu s 400 miliardami parametrů lze podle DeepSeek snížit počet potřebných GPU o 30–50 % oproti standardním technikám jako ZeRO nebo FSDP (Fully Sharded Data Parallel). Metoda také zahrnuje adaptivní kompresi gradientů, což minimalizuje přenos dat mezi uzly v distribuovaném tréninku. To je použitelné pro vývojáře, kteří chtějí trénovat vlastní LLM na cloudu nebo lokálních clusterech, například pro specializované aplikace v medicíně, právu nebo programování.

V kontextu současného AI průmyslu, kde náklady na trénování modelů překračují stovky milionů dolarů (např. GPT-4 stál odhadem 100 milionů USD), představuje tento přístup konkurenční výhodu pro firmy s omezenými zdroji. Čína tak posiluje svou pozici v AI závodě, kde státní podpora umožňuje rychlý vývoj. Nicméně kritici upozorňují, že metoda stále závisí na proprietárních datech a hardware od NVIDIA, což omezuje plnou nezávislost. Testy na benchmarkách jako MMLU nebo HumanEval ukazují zlepšení efektivity o 40 % oproti předchozím verzím.

### Proč je to důležité
Tento pokrok ovlivní celý ekosystém AI tím, že demokratizuje přístup k velkým modelům. Menší firmy a výzkumníci budou moci škálovat LLM bez obrovských investic do hardware, což urychlí inovace v oblastech jako autonomní systémy nebo personalizovaná AI. V širším kontextu posiluje Čínu jako lídra v efektivním AI vývoji, což může vést k nové fázi soutěže s USA, kde firmy jako xAI nebo Meta hledají podobné optimalizace. Dlouhodobě to přispěje k překonání limitů současného hardware, blíže k AGI, ale zároveň zvyšuje potřebu regulací kvůli energetické náročnosti tréninku.

---

[Číst původní článek](https://www.businessinsider.com/deepseek-new-ai-training-models-scale-manifold-constrained-analysts-china-2026-1)

**Zdroj:** 📰 Business Insider
