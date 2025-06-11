---
author: Patrick Zandl
date: 2025-06-10
categories:
- AI
- Windsurf
- O3
- programování
- vývojové nástroje
layout: post
post_excerpt: Windsurf představil Planning Mode pro dlouhodobé plánování projektů s AI a snížil ceny modelu O3 z 7,5x na 1x kredit.
summary_points:
- Planning Mode umožňuje kolaboraci s AI na dlouhodobém plánování prostřednictvím markdown souborů
- Model O3 zlevnil z 7,5x-10x kreditů na pouze 1x kredit pro všechny varianty
- Funkce staví na konceptu dvou časových os - krátkodobých akcí a dlouhodobého plánování  
- Dostupná pro všechny placené plány bez dodatečných poplatků
- Windsurf cílí na 99% zrychlení vývoje softwaru pomocí AI asistentů
- Wave 10 vydána postupně během tří dnů jako součást většího balíčku updatů
title: Windsurf zavádí Planning Mode pro dlouhodobé plánování projektů, model O3 zlevňuje
---

Společnost Windsurf (dříve Exafunction) představila Planning Mode jako součást své desáté vlny updatů. Nová funkce umožňuje spolupráci s umělou inteligencí na dlouhodobém plánování programátorských projektů prostřednictvím markdown souborů. Současně značně snížila náklady na využívání modelu O3 z OpenAI.

## Windsurf Planning Mode - nástroj pro strukturované plánování kódu

Windsurf, vývojové prostředí zaměřené na programování s umělou inteligencí, vydalo Planning Mode jako klíčovou součást Wave 10. Tato funkce představuje první nativní implementaci dlouhodobého plánování v IDE prostředí.

Planning Mode funguje prostřednictvím lokálního markdown souboru, který obsahuje cíle a úkoly projektu. AI asistent Cascade automaticky generuje a upravuje tento plán během práce na projektu. Uživatelé mohou plán manuálně editovat nebo požádat Cascade o jeho změnu prostřednictvím konverzace.

Systém využívá dvouúrovňovou architekturu. Větší model s pokročilými schopnostmi dlouhodobého uvažování spravuje plán, zatímco uživatelem vybraný model provádí krátkodobé akce podle tohoto plánu. Cascade neustále odkazuje na plán při plnění úkolů a automaticky ho aktualizuje, když získá nové informace.

Technická implementace staví na konceptu "flow awareness" - schopnosti člověka i AI být si vědom sdílené časové osy akcí. Planning Mode rozšiřuje tento koncept o druhou časovou osu pro dlouhodobé plánování. Akce z krátkodobé časové osy jsou odvozeny od plánu (vertikální šipky nahoru), zatímco plán se aktualizuje na základě výsledků akcí (zakřivené šipky dolů).

Windsurf identifikuje tři klíčové komponenty softwarového inženýrství: definování toho, co stavět; zjištění, jak to stavět; a samotné stavění. Planning Mode se zaměřuje na druhou komponentu - "jak stavět" - která historicky byla pro AI náročná.

Planning Mode je dostupný pro všechny placené plány bez dodatečných poplatků. Funkce je postavena na SWE-1 modelech, proprietární rodině frontier modelů Windsurf určených pro softwarové inženýrství.

## Snížení nákladů na model O3

Windsurf současně oznámilo dramatické snížení nákladů na využívání modelu O3 od OpenAI. Cena klesla z původních 7,5x a 10x kreditů na pouhý 1x kredit pro obě varianty (medium a high reasoning). Toto snížení částečně umožnilo nabídnout Planning Mode bez dodatečných poplatků.

Společnost také vylepšila rychlost a funkčnost O3 v rámci prostředí Cascade. Model O3, známý svými pokročilými schopnostmi uvažování, se stal dostupnějším pro běžné použití ve vývojových workflow.

## Technická architektura a budoucí vývoj

Planning Mode představuje první verzi optimálního rozhraní pro spolupráci s AI na úrovni plánování projektů. Markdown formát byl vybrán jako nejjednodušší řešení splňující požadavky na perzistenci a modifikovatelnost.

Iterace plánovacího procesu zahrnuje tři klíčové komponenty: schopnost učit se nové informace; schopnost aktualizovat plán na základě nových informací; a schopnost krátkodobých akcí vždy odrážet nejnovější verzi dlouhodobého plánu.

Windsurf naznačuje možné budoucí rozšíření včetně bohatších reprezentací než markdown soubory (obrázky, diagramy, komentáře), multiplayer funkcionalitu podobnou Google Docs, a kategoricky bohatší aktualizace časové osy plánování.

Společnost také zkoumá možnosti dokumentace nejen plánů, ale i jejich evoluce pro organizace - datový zdroj, který dosud neexistoval. Dlouhodobé uvažování považuje za klíčový problém pro dosažení svého cíle zrychlit vývoj softwaru o 99 %.

**Shrnutí klíčových bodů:**
- Planning Mode umožňuje strukturované dlouhodobé plánování projektů prostřednictvím markdown souborů
- Model O3 zlevnil z 7,5x-10x kreditů na pouze 1x kredit
- Funkce je dostupná pro všechny placené plány bez dodatečných poplatků
- Implementace staví na konceptu dvou časových os - krátkodobých akcí a dlouhodobého plánování
- Windsurf cílí na 99% zrychlení vývoje softwaru pomocí AI asistentů