---
author: Marisa Aigen
category: kybernetika
companies:
- Google
date: '2026-02-12 19:13:57'
description: Google Threat Intelligence Group upozorňuje na rostoucí hrozbu model
  extraction attacks, při kterých útočníci využívají legitimní přístup k API velkých
  jazykových modelů (LLM) k získání dat pro trénování vlastních kopií. Tato technika
  umožňuje rychlé a levné replikování proprietárních modelů bez nutnosti tradičního
  prolomení systémů.
importance: 4
layout: tech_news_article
original_title: Google Warns Against Thieves Using APIs to Clone AI Models
publishedAt: '2026-02-12T19:13:57+00:00'
slug: google-warns-against-thieves-using-apis-to-clone-a
source:
  emoji: 📰
  id: null
  name: pymnts.com
title: Google varuje před zloději, kteří klonují AI modely pomocí API
url: https://www.pymnts.com/cybersecurity/2026/google-warns-against-thieves-using-apis-to-clone-ai-models/
urlToImage: https://www.pymnts.com/wp-content/uploads/2026/02/Google-AI-theft.jpeg
urlToImageBackup: https://www.pymnts.com/wp-content/uploads/2026/02/Google-AI-theft.jpeg
---

## Souhrn
Google Threat Intelligence Group (GTIG), divize Google zaměřená na detekci kybernetických hrozeb, v blogovém příspěvku z 12. února 2026 varuje před novou formou krádeže duševního vlastnictví v oblasti umělé inteligence. Útočníci zneužívají veřejně dostupná API velkých jazykových modelů k provádění tzv. model extraction attacks nebo distillation attacks, čímž extrahují klíčové informace pro vytvoření vlastních klonů těchto modelů. GTIG společně s Google DeepMind v roce 2025 identifikovalo a zlikvidovalo několik takových pokusů.

## Klíčové body
- Útočníci získávají legitimní přístup k API LLM, jako jsou ty od OpenAI nebo Google, a opakovaně dotazují model na specifická data.
- Extrahovaná data slouží k trénování nových modelů, což dramaticky snižuje náklady a čas oproti vývoji od nuly.
- GTIG zdůrazňuje přechod od tradičních hackerství k legálním API zneužitím, což ztěžuje detekci.
- Legitimní použití distillation existuje, ale bez souhlasu jde o krádež.
- V roce 2025 byly identifikovány a narušeny konkrétní útoky.

## Podrobnosti
Model extraction attacks fungují tak, že útočník platí za standardní přístup k API LLM, například k modelům jako GPT nebo Gemini. Opakovanými dotazy – často tisíci nebo milionem – získává výstupy modelu na pečlivě navržené vstupy. Tyto páry vstup-výstup pak slouží jako tréninková data pro nový model, který se chová podobně jako originál. Tato metoda, známá také jako model distillation, umožňuje přenést znalosti z velkého „učitele“ (teacher model) do menšího „žáka“ (student model), který je efektivnější v nasazení.

GTIG uvádí, že tradiční způsoby krádeže high-tech znalostí zahrnovaly intruze do sítí a krádež datových sad s obchodními tajemstvími. Dnes stačí placený API klíč, což democratizuje přístup k této technice. Google DeepMind, výzkumné centrum Google specializující se na pokročilou AI, pomohlo identifikovat anomální chování v API voláních, jako jsou neobvyklé objemy dotazů nebo specifické patterny, které naznačují extraction.

V praxi to znamená, že firmy jako OpenAI, Anthropic nebo xAI, které nabízejí LLM jako službu (SaaS), musí zavést pokročilé ochrany. Mezi ně patří omezení rychlosti dotazů (rate limiting), detekce anomálií v API provozu, vodoznaky ve výstupech (watermarking) pro sledování zneužití nebo dokonce šifrované odpovědi, které brání efektivnímu tréninku. Bez těchto opatření mohou útočníci replikovat modely stojící stovky milionů dolarů za zlomek ceny – trénink GPT-4 odhadně stál přes 100 milionů USD na GPU výpočtech.

GTIG zdůrazňuje, že tato hrozba roste s integrací LLM do podnikových systémů, kde proprietární fine-tuning představuje konkurenční výhodu. Příkladem může být klonování specializovaného modelu pro lékařskou diagnostiku nebo finanční analýzu.

## Proč je to důležité
Tato hrozba ohrožuje ekonomický model AI průmyslu, kde hlavní hodnotou jsou nejen data, ale i architektura a tréninkové postupy modelů. Pokud se klonování stane běžným, sníží se motivace k investicím do vývoje – odhaduje se, že globální výdaje na AI v roce 2025 překročily 200 miliard USD. Pro uživatele to znamená riziko šíření nekvalitních klonů, které mohou obsahovat chyby originálu nebo být zneužity k šíření dezinformací.

V širším kontextu urychluje to závod o bezpečnost AI: firmy musí balancovat otevřenost API pro inovace s ochranou IP. Jako expert vidím, že bez standardizovaných protokolů, jako jsou ty navrhované OpenAI v podobných paperůch, se hrozba rozšíří na edge computing a on-device AI. Google sám nasadil detekční systémy, ale doporučuji všem poskytovatelům LLM implementovat behaviorální analýzu API logů. Dlouhodobě to povede k hybridním modelům, kde část výpočtů běží lokálně, mimo dosah API zneužití.

---

[Číst původní článek](https://www.pymnts.com/cybersecurity/2026/google-warns-against-thieves-using-apis-to-clone-ai-models/)

**Zdroj:** 📰 pymnts.com
