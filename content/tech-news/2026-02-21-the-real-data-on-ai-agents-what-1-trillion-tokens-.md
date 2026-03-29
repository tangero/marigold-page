---

author: Marisa Aigen
category: ai agenti
companies:
- OpenRouter
date: '2026-02-21 11:23:02'
description: Chris Clark, spoluzakladatel a COO OpenRouteru, sdílí data z největší
  AI brány na světě, která zpracovává přes bilion tokenů denně přes více než 70 poskytovatelů.
  Tool call rates u modelů jako Anthropic vzrostly z méně než 5 % na přes 25 % za
  rok, což signalizuje přechod AI agentů do produkčního nasazení.
importance: 4
original_title: 'The Real Data on AI Agents: What 1 Trillion Tokens a Day Reveals
  with OpenRouter’s COO'
people:
- Chris Clark
publishedAt: '2026-02-21T11:23:02+00:00'
slug: the-real-data-on-ai-agents-what-1-trillion-tokens-
source:
  emoji: 📰
  id: null
  name: Saastr.com
title: 'Skutečná data o AI agentech: Co odhaluje 1 bilion tokenů denně podle COO OpenRouteru'
url: https://www.saastr.com/the-real-data-on-ai-agents-what-1-trillion-tokens-a-day-reveals-with-openrouters-coo/
urlToImage: https://i0.wp.com/www.saastr.com/wp-content/uploads/2026/02/AI-Agents-Thumbnail-3-scaled.jpg?fit=1000%2C565&quality=70&ssl=1
urlToImageBackup: https://i0.wp.com/www.saastr.com/wp-content/uploads/2026/02/AI-Agents-Thumbnail-3-scaled.jpg?fit=1000%2C565&quality=70&ssl=1
---

## Souhrn
Chris Clark z OpenRouteru, firmy specializující se na směrování API volání k různým AI modelům přes desítky cloudů a geografie, analyzuje data z trilionů zpracovaných tokenů týdně. Klíčový ukazatel – míra tool calls – u Anthropic API vzrostla z pod 5 % na více než 25 % během 12 měsíců. To naznačuje, že AI agenti přecházejí z experimentální fáze do reálného nasazení u firem po celém světě.

## Klíčové body
- OpenRouter zpracovává přes bilion tokenů denně přes 70+ poskytovatelů, což poskytuje reprezentativní pohled na globální využití AI.
- Tool call rates u Anthropic API stouply z <5 % na >25 % za rok; u specializovaných modelů jako Minimax M2 dosahují 80 %+.
- Tool call umožňuje LLM volat externí funkce (např. platby přes Stripe, dotazy do databáze nebo procházení webu) prostřednictvím strukturovaného výstupu.
- AI agent je opakující se smyčka: LLM žádá tool call, software funkci provede, výsledek se vrátí do LLM.
- Data ukazují přechod od chatových LLM k operačním agentům v produkci.

## Podrobnosti
OpenRouter funguje jako největší globální brána pro AI API, která spojuje stovky modelů od různých dodavatelů, jako je Anthropic, a směruje volání přes desítky cloudových platforem do všech regionů. Díky objemu přes trilionu tokenů týdně vidí firma reálné chování uživatelů, ne jen prohlášení společností. Nejdůležitějším grafem je vývoj tool call rates – procenta požadavků, kde model na konci konverzace navrhne volání nástroje.

Tool call je mechanismus, který rozšiřuje možnosti velkých jazykových modelů (LLM). LLM samotné zpracovávají pouze text: vstup text, výstup text. Nemohou přímo interagovat s externím světem, jako je platba přes Stripe, dotaz do firemní databáze nebo načtení dat z webu. Místo toho generují strukturovaný text v JSON formátu, který říká: „Zavolej tuto funkci s těmito parametry.“ Pak speciální software (tzv. harness) funkci skutečně spustí, vrátí výsledek zpět do LLM a cyklus se opakuje. Tento loop definuje AI agenta – autonomní systém schopný řešit složité úkoly rozložením na kroky s externími akcemi.

Podle dat OpenRouteru tento trend není okrajový. U Anthropic modelů, které Clark považuje za reprezentativní pro širší trh, tool calls explodovaly pětinásobně za rok. U modelů optimalizovaných pro agenty, jako Minimax M2 (čínský model navržený pro vysokou míru tool interakcí), je míra už nyní nad 80 %. To znamená, že uživatelé – od startupů po velké firmy – nasazují agenty pro reálné aplikace, například automatizaci workflow, analýzu dat nebo zákaznickou podporu. Data nejsou založena na anketách, ale na miliardách API volání, což je činí spolehlivějšími než blogové spekulace.

## Proč je to důležité
Růst tool call rates potvrzuje, že AI agenti nejsou jen marketingový hype, ale stávají se standardní součástí produkčních systémů. Pro průmysl to znamená přechod od jednoduchých chatových rozhraní k autonomním systémům, které mohou nahradit manuální procesy a zvýšit efektivitu. Například v podnikovém prostředí agenti umožní LLM řídit celé workflow – od objednávek po reporting – bez lidského zásahu. V širším kontextu posiluje to dominanci modelů s lepší podporou toolů, jako Claude nebo specializované varianty, a tlačí na vývoj lepších harnessů pro bezpečnost a spolehlivost. Nicméně data jsou specifická pro OpenRouterovy uživatele, kteří jsou často developeři a firmy experimentující s AI, takže globální adopce v tradičních odvětvích může zaostávat. Dlouhodobě to urychlí investice do agentické architektury a ovlivní vývoj nových modelů zaměřených na akce místo pouhého generování textu.

---

[Číst původní článek](https://www.saastr.com/the-real-data-on-ai-agents-what-1-trillion-tokens-a-day-reveals-with-openrouters-coo/)

**Zdroj:** 📰 Saastr.com
