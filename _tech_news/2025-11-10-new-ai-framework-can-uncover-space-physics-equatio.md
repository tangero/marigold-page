---
author: Marisa Aigen
category: ai
date: '2025-11-10 12:00:01'
description: Tým z Tsinghua University, Peking University a dalších čínských institucí
  vyvinul framework PhyE2E, který pomocí AI automatizovaně odvozuje symbolické fyzikální
  rovnice z neupravených měření, a to s využitím jazykových modelů, fyzikálních priorů
  a cíleného prohledávání.
importance: 3
layout: tech_news_article
original_title: New AI framework can uncover space physics equations in raw data -
  Phys.org
publishedAt: '2025-11-10T12:00:01+00:00'
slug: new-ai-framework-can-uncover-space-physics-equatio
source:
  emoji: 📰
  id: null
  name: Phys.Org
title: Nový AI framework dokáže přímo z dat odhalovat rovnice pro fyziku vesmíru
url: https://phys.org/news/2025-11-ai-framework-uncover-space-physics.html
urlToImage: https://scx2.b-cdn.net/gfx/news/hires/2025/new-ai-framework-can-u.jpg
urlToImageBackup: https://scx2.b-cdn.net/gfx/news/hires/2025/new-ai-framework-can-u.jpg
---

## Souhrn
Nový AI framework PhyE2E umožňuje automaticky odvozovat fyzikální zákony a rovnice přímo z neupravených dat z oblasti vesmírné fyziky. Spojuje generativní jazykové modely, metody symbolické regrese, fyzikální znalosti a strategické prohledávání, čímž zjednodušuje hledání matematických vztahů v komplexních datech, které by lidský analytik odhaloval velmi obtížně.

## Klíčové body
- PhyE2E je end-to-end framework pro automatické odvozování symbolických fyzikálních rovnic z reálných měření.
- Využívá syntetická data generovaná velkým jazykovým modelem (LLM) pro rozšíření trénovacích dat.
- Zavádí techniku „divide-and-conquer“ pro rozklad složité symbolické regrese na jednodušší podproblémy.
- Integruje fyzikální priory, aby eliminoval nereálné a nekonzistentní rovnice.
- Používá Monte Carlo Tree Search (MCTS) s formální gramatikou pro zpřesnění a ověření výsledných vzorců.

## Podrobnosti
Framework PhyE2E, představený v Nature Machine Intelligence, cílí na dlouhodobý problém automatizace vědeckého objevování: jak z měřených dat získat srozumitelné a fyzikálně konzistentní rovnice místo „černých skříněk“. Tým z Tsinghua University, Peking University a dalších institucí kombinuje několik prvků, které dosud byly většinou používány odděleně.

V první fázi systém rozšiřuje reálná experimentální data o velké množství syntetických příkladů. Tyto syntetické datové sady generuje LLM, které produkuje dvojice „rovnice – data“, čímž umožňuje natrénovat model na širokou paletu fyzikálních vztahů. Cílem není nahradit reálnou fyziku, ale vytvořit dostatečně bohatý vzorový prostor, aby model uměl rozpoznávat strukturu rovnic.

Dále framework používá metodu divide-and-conquer pro symbolickou regresi. Komplexní rovnice se rozkládají na menší části a model hledá interakce proměnných, což snižuje výpočetní složitost a omezuje chaotické prohledávání obrovského prostoru výrazů. Současně jsou do modelu vneseny fyzikální priory – například dimenzionální konzistence, známé konstanty nebo fyzikálně realistické tvary vztahů. To omezuje generování formálně správných, ale fyzikálně nesmyslných rovnic.

V závěrečné fázi je použit Monte Carlo Tree Search (MCTS) nad kontextově volnou gramatikou, která definuje přípustné atomické výrazy a operace. MCTS systematicky prohledává prostor možných rovnic, vyhodnocuje je pomocí metrik, jako je root mean squared error (RMSE), a jemně dolaďuje výraz navržený end-to-end modelem. Výsledkem jsou rovnice, které jsou nejen přesné ve vztahu k datům, ale také interpretovatelné a fyzikálně konzistentní.

## Proč je to důležité
Pro oblast vesmírné fyziky, kde družice a sondy generují masivní objemy dat s komplexními interakcemi polí, částic a plazmatu, představuje PhyE2E možnost systematicky vyhledávat nové zákonitosti bez manuálního „ručního lovu“ vzorců. Pokud se framework osvědčí mimo testovací scénáře, může se stát nástrojem pro:

- zrychlení formulace a ověřování hypotéz ve fyzice plazmatu, kosmického počasí a magnetosférických jevů,
- efektivnější využití dat z drahých vesmírných misí, kde lidský tým není schopen ručně prozkoumat všechny kombinace proměnných,
- přenos metodiky do dalších oborů, jako je materiálový výzkum, klimatologie nebo biologie, kde je potřeba z dat získat srozumitelné a zkontrolovatelné rovnice.

Zároveň je nutné zůstat kritický: reliance na syntetická data z LLM nese riziko vnášení biasů a nerealistických vztahů, fyzikální priory mohou nechtěně konzervovat stávající teorie a MCTS je výpočetně náročný. Framework tedy není autonomní vědec, ale potenciálně užitečný nástroj pro fyziky, kteří potřebují rychle procházet rozsáhlý prostor hypotéz s kontrolou nad interpretovatelností výsledků.

---

[Číst původní článek](https://phys.org/news/2025-11-ai-framework-uncover-space-physics.html)

**Zdroj:** 📰 Phys.Org
