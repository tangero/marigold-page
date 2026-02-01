---
author: Marisa Aigen
category: ai
companies:
- Ai2
- GitHub
- Allen Institute for AI
date: '2026-01-27 16:00:11'
description: Allen Institute for AI (Ai2) vydal Ai2 Open Coding Agents, sadu open-source
  nástrojů pro tvorbu a trénink vlastních kódovacích agentů. První model SERA řeší
  více než 55 % problémů na benchmarku SWE-Bench Verified a překonává srovnatelné
  open-source i některé uzavřené modely.
importance: 4
layout: tech_news_article
original_title: Ai2 launches family of open-source AI developer agents that adapt
  to any codebase
publishedAt: '2026-01-27T16:00:11+00:00'
slug: ai2-launches-family-of-open-source-ai-developer-ag
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: Ai2 vydává rodinu open-source AI agentů pro vývojáře, kteří se adaptují na
  libovolný kódový základ
url: https://siliconangle.com/2026/01/27/ai2-launches-family-open-source-ai-developer-agents-adapt-codebase/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/04/A-group-of-AI-agents-standing-in-a-semicircle-with-hands-on-keyboards-with-computer-code-flickering-.jpeg
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/04/A-group-of-AI-agents-standing-in-a-semicircle-with-hands-on-keyboards-with-computer-code-flickering-.jpeg
---

## Souhrn
Allen Institute for AI (Ai2), neziskový výzkumný institut zaměřený na vývoj umělé inteligence, vydal rodinu open-source AI agentů pro kódování pod názvem Ai2 Open Coding Agents. Tyto agenti umožňují snadnou tvorbu a trénink vlastních modelů, které se přizpůsobují soukromým kódovým základům bez nutnosti zkušeností s tréninkem velkých jazykových modelů. První z nich, SERA (Soft-verified Efficient Repository Agents), dosahuje na benchmarku SWE-Bench Verified úspěšnosti přes 55 procent, což je lepší než u většiny open-source konkurentů.

## Klíčové body
- SERA-32B, model s 32 miliardami parametrů, řeší 55 % problémů SWE-Bench Verified v standardních nastaveních a překonává open-source modely jako Qwen3-Coder i uzavřené jako Mistral3 Devstral Small 2.
- SERA-8B, menší varianta s 8 miliardami parametrů, dosahuje 29,4 % úspěšnosti oproti 9,4 % u referenčních modelů na bázi reinforcement learningu, jako SkyRL-Agent-8B-v0.
- Plně open-source komponenty včetně modelů, kódu a integrace s Claude Code od Anthropic PBC jedním řádkem kódu.
- Trénink na 8000 syntetických trajektoriích na repozitář, kde slouží model GLM-4.5-Air (přes 100 miliard parametrů) jako učitel.
- Agenti se adaptují na libovolné repozitáře, což řeší problém uzavřených a drahých kódovacích nástrojů.

## Podrobnosti
SWE-Bench Verified je standardní benchmark pro testování schopností AI v řešení reálných úkolů software engineeringu, jako je oprava chyb v GitHub repozitářích. SERA dosahuje těchto výsledků díky specializovanému tréninku, kde se generují syntetické trajektorie – sekvence akcí pro navigaci a úpravu kódu v repozitářích. Tento přístup umožňuje agentům efektivně prozkoumávat kódové základy bez nutnosti rozsáhlého hardwaru. Například SERA-32B překonává modely srovnatelné velikosti v otevřených i uzavřených verzích při stejných podmínkách inferenci. Menší SERA-8B demonstruje efektivitu na edge zařízeních nebo omezených zdrojích, kde tradiční reinforcement learning selhává.

Ai2 Open Coding Agents jsou navrženy pro snadnou integraci: stačí jeden řádek kódu pro spuštění s Claude Code, což je nástroj od Anthropic pro kódování založený na modelu Claude. To znamená, že vývojáři mohou bez předchozích znalostí LLM nasadit agenta na svůj soukromý kódový základ, například firemní repozitář, a nechat ho automaticky opravovat chyby nebo generovat kód. Trénink probíhá na datech z 8000 trajektorií na repozitář, což zajišťuje konzistentní výkon překonávající větší modely jako GLM-4.5-Air v mnoha scénářích. Ai2 zdůrazňuje plnou otevřenost, což umožňuje studium a úpravy, na rozdíl od proprietárních řešení jako GitHub Copilot nebo Amazon CodeWhisperer, které jsou omezené na veřejné datasety a vyžadují předplatné.

Tento release řeší klíčový problém současných kódovacích agentů: většina je buď uzavřená (jako modely od OpenAI nebo Google), nebo drahá na přizpůsobení soukromým projektům kvůli potřebě obrovských dat a výpočetních zdrojů. SERA ukazuje, že syntetická data a soft-verifikace – mechanismus pro ověření akcí bez tvrdých pravidel – stačí k vysokému výkonu. Nicméně, jako expert v AI, upozorňuji, že benchmarky jako SWE-Bench testují izolované úkoly; v reálných projektech s komplexními závislostmi nebo bezpečnostními požadavky může výkon klesnout, což vyžaduje další validaci.

## Proč je to důležité
Tento vývoj posiluje trend demokratizace AI nástrojů pro software engineering. Open-source přístup umožňuje firmám a nezávislým vývojářům integrovat pokročilé coding agenty do svých workflow bez závislosti na komerčních poskytovatelích, což snižuje náklady a zvyšuje kontrolu nad daty. V širším kontextu urychluje to automatizaci vývoje kódu, kde AI agenti spolupracují s lidmi na GitHubu nebo interních repozitářích. Pro průmysl to znamená rychlejší iterace projektů a méně chyb, ale zároveň zvyšuje tlak na etické standardy, jako ochrana duševního vlastnictví v trénovacích datech. Ai2 tak přispívá k otevřené ekosystému AI, kde menší modely jako SERA-8B konkurují gigantům, což může změnit dynamiku trhu s developer tools.

---

[Číst původní článek](https://siliconangle.com/2026/01/27/ai2-launches-family-open-source-ai-developer-agents-adapt-codebase/)

**Zdroj:** 📰 SiliconANGLE News
