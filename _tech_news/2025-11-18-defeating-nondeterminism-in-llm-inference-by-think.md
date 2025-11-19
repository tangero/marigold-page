---
author: Marisa Aigen
category: umělá inteligence
companies:
- OpenAI
date: '2025-11-18 04:15:40'
description: Výzkumníci z laboratoře Thinking Machines odhalili skutečný zdroj nedeterminismu
  při odvozování výsledků z velkých jazykových modelů (LLM), který není způsoben plovoucí
  řádovou aritmetikou, jak se dosud předpokládalo, ale dynamickým dávkováním požadavků
  na serverech.
importance: 3
layout: tech_news_article
original_title: Defeating Nondeterminism in LLM Inference by Thinking Machines
people:
- Horace He
- Mira Murati
publishedAt: '2025-11-18T04:15:40+00:00'
slug: defeating-nondeterminism-in-llm-inference-by-think
source:
  emoji: 📰
  id: next-big-future
  name: Next Big Future
title: Překonání nedeterminismu v odvozování velkých jazykových modelů
url: https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html
urlToImage: https://nextbigfuture.s3.amazonaws.com/uploads/2025/11/Screenshot-2025-11-17-at-8.14.15-PM-1024x583.jpg
urlToImageBackup: https://nextbigfuture.s3.amazonaws.com/uploads/2025/11/Screenshot-2025-11-17-at-8.14.15-PM-1024x583.jpg
---

## Souhrn
Výzkumný článek od Horace He a laboratoře Thinking Machines (založené bývalou CTO OpenAI Mirou Murati) identifikuje skutečný zdroj nedeterminismu při odvozování výsledků z velkých jazykových modelů (LLM). I při vypnutí náhodnosti (např. nastavením teploty na 0 a použitím pevného seedu) se stejný vstup často vyhodnotí různě – a hlavní viník není plovoucí řádová aritmetika na GPU, jak se dosud věřilo, ale způsob, jakým servery sdružují požadavky do dynamických dávek.

## Klíčové body
- Nedeterminismus v LLM není způsoben nespojivostí operací s plovoucí řádovou čárkou na GPU, jak se tradičně předpokládalo.
- Skutečným zdrojem je dynamické dávkování požadavků na produkčních serverech, které mění velikost dávky, zarovnání a pozici jednotlivých požadavků.
- Normalizační vrstvy (např. LayerNorm, RMSNorm) a maticové operace (GEMM) jsou citlivé na obsah celé dávky, nikoli jen na jednotlivý vstup.
- Tento problém narušuje reprodukovatelnost experimentů, ladění, bezpečnostní testování a spolehlivost v podnikovém nasazení.

## Podrobnosti
Většina výzkumníků a inženýrů dosud přisuzovala rozdílné výstupy LLM při opakovaném spuštění „závoděním vláken“ na GPU a neasociativitě operací s plovoucí řádovou čárkou – tedy tomu, že (a + b) + c ≠ a + (b + c) kvůli zaokrouhlovacím chybám. Nový výzkum však ukazuje, že moderní implementace transformerových modelů (včetně knihoven jako FlashAttention, cuBLAS nebo Triton) používají deterministické redukční stromy a vyhýbají se atomickým operacím v dopředném průchodu. Skutečný problém spočívá v produkčním prostředí: servery jako vLLM nebo TGI používají dynamické dávkování, kdy se náhodně přicházející požadavky sdružují do jedné dávky pro efektivitu. Tím se mění statistiky normalizačních vrstev (např. průměr a rozptyl v LayerNorm), které závisí na celém obsahu dávky, nikoli jen na jednom vstupu. Tyto drobné změny se pak šíří a vedou k odlišnému výběru tokenů.

## Proč je to důležité
Reprodukovatelnost je základem vědeckého výzkumu, ladění systémů a bezpečnostních auditů. Pokud stejný dotaz v různých časech vyprodukuje jinou odpověď, je obtížné ověřit chování modelu, ladit chyby nebo zaručit důvěryhodnost v kritických aplikacích (např. v medicíně nebo právní poradně). Tento objev směřuje k nutnosti přehodnotit způsob nasazování LLM v produkci – například izolovat požadavky nebo zavést „deterministické dávkování“. Pro průmysl to znamená, že efektivita nemusí jít vždy ruku v ruce s predikovatelností, a že architektura inferenčních serverů vyžaduje hlubší přehodnocení.

---

[Číst původní článek](https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html)

**Zdroj:** 📰 Next Big Future
