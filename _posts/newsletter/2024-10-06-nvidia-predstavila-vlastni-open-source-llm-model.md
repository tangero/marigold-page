---
author: Patrick Zandl
categories:
- Patrickův newsletter
- AI
- Automotive
date: '2024-10-06'
layout: post
original_newsletter: "#83 \U0001F353OpenAI představila jahodovou inteligenci o1 a
  Canvas"
summary_points:
- Nvidia vyvinula NVLM, multimodální open-source LLM model srovnatelný s GPT-4o.
- NVLM s 72 miliardami parametrů překonává LLAMA s 404 miliardami v některých úlohách.
- Open-source NVLM je určen pro firemní nasazení a vývoj vlastních řešení.
- NVLM je dostupný na HuggingFace pro vývojáře, kteří rozumí problematice.
title: \U0001F916Nvidia představila vlastní open source LLM model
---

Vždycky se tak nějak předpokládalo, že Nvidia nepoleze do zelí svým klientům a nepředstaví vlastní velký AI model. Pak Nvidia oznámila vývoj modelu pro roboty, to se považovalo za rozumné, protože to bude velký krok pro automatizaci průmyslu a jiné firmy se tam moc nepouštějí. V polovině září ale Nvidia představila [obecný LLM model nazvaný NVLM](https://research.nvidia.com/labs/adlr/NVLM-1/), který je multimodální, open-source, tedy s otevřeným kódem a dokonce otevřenými váhami a trénovacím kódem. Díky tomu si jej můžete široce přizpůsobit a provozovat (na Nvidia hardware). Výkonostně je model velmi srovnatelný s GPT-4o, dnešního standardu, v některých typech úloh ho mírně předčí, jinde maličko zaostává, což s ohledem na multimodalitu a otevřený kód je bomba. Zajímavé je, že model NVLM má 72 miliard parametrů a dává lepší výsledky, než LLAMA s 404 miliardami parametrů. 

Pro koncové uživatele to moc důležité není - málokdo si chce provozovat vlastní LLM na svém počítači. Ale pro firemní použití, profesionální nasazení, jsou open source modely, které lze provozovat na svém cloudu, velmi důležité. Lze jim svěřit neveřejná data bez větších obav, lze je použít jako podvozek vlastního řešení. V tomto smyslu lze krok Nvidia vítat jako základ pro vývoj budoucích produktů. Ostatně, [najdete jej už na HuggingFace](https://huggingface.co/nvidia/NVLM-D-72B) k použití ve vašich projektech, pokud vývoji rozumíte. 

* * *