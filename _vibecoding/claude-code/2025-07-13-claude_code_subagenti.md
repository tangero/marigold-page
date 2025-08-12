---
author: Patrick Zandl
categories:
- AI
- Claude Code
- Anthropic
- paralelní zpracování
- Task Tool
layout: vibecoding-default
post_excerpt: "Claude Code umožňuje spouštět paralelní subagenty pro efektivní zpracování rozsáhlých kódových projektů a současné provádění více nezávislých úkolů."
summary_points:
- Subagenti jsou lehké instance Claude Code běžící prostřednictvím Task Tool
- Každý subagent disponuje vlastním kontextovým oknem pro zpracování dat
- Systém podporuje až 10 paralelních úkolů současně s automatickou frontou
- Ideální pro průzkum rozsáhlých kódových projektů a rozdělení práce
- Efektivní správa úkolů bez nutnosti specifikovat úroveň paralelismu
- Testování prokázalo spolehlivost i při zpracování 100 úkolů najednou
title: Používání subagentů v Claude Code
---

Claude Code umožňuje využívat takzvané subagenty pro paralelní zpracování úkolů. Tyto subagenti představují způsob, jak efektivně rozdělit práci při analýze rozsáhlých projektů nebo provádění nezávislých operací současně.

## Definice a princip fungování subagentů

Subagent představuje odlehčenou instanci Claude Code, která běží uvnitř úkolu prostřednictvím Task Tool. Při spuštění subagenta se v uživatelském rozhraní zobrazuje označení "Task(Performing task X)", které signalizuje aktivní provádění konkrétního úkolu. Klíčovou vlastností subagentů je jejich schopnost běžet paralelně, což umožňuje současné zpracování více nezávislých úkolů.

Každý subagent disponuje vlastním kontextovým oknem, což představuje významnou výhodu při práci s rozsáhlými kódovými projekty. Toto řešení efektivně rozšiřuje dostupnou paměť pro zpracování komplexních úkolů, protože jednotlivé subagenty nezatěžují hlavní kontextové okno.

## Omezení paralelního zpracování

Claude Code podporuje maximálně 10 paralelních úkolů současně. Při překročení tohoto limitu systém automaticky vytváří frontu čekajících úkolů a spouští nové instance, jakmile se některý z běžících úkolů dokončí. Toto chování zajišťuje efektivní využití zdrojů bez přetížení systému.

Zajímavým pozorováním je rozdíl v chování při specifikování úrovně paralelismu. Pokud uživatel explicitně určí počet paralelních úkolů, systém zpracovává úkoly v dávkách a čeká na dokončení celé dávky před spuštěním další. Naopak při automatickém řízení paralelismu Claude Code spouští nové úkoly ihned po uvolnění místa, což je efektivnější přístup.

## Praktické využití subagentů

### Průzkum kódových projektů

Subagenti se osvědčují při analýze struktury rozsáhlých projektů. Typické použití zahrnuje rozdělení průzkumu mezi čtyři subagenty, kde každý zkoumá jinou část projektu:

- Backend strukturu a serverovou logiku
- Frontend komponenty a uživatelské rozhraní  
- Konfigurační soubory a nastavení prostředí
- Dokumentaci a testovací soubory

Tento přístup umožňuje rychlejší pochopení architektury projektu a identifikaci klíčových komponent bez nutnosti sekvenčního procházení celého kódu.

### Správa front úkolů

Claude Code dokáže zvládnout i rozsáhlé fronty úkolů. Test se 100 simulovanými úkoly prokázal spolehlivost systému při dlouhodobém zatížení. Systém automaticky spravoval frontu úkolů, udržoval maximální počet aktivních instancí na úrovni 10 a průběžně doplňoval dokončené úkoly novými z fronty.

## Technické charakteristiky a výkon

Každý subagent využívá vlastní sadu nástrojů a může provádět nezávislé operace včetně čtení souborů, spouštění příkazů nebo analýzy kódu. Spotřeba tokenů se liší podle složitosti úkolu, přičemž typické úkoly využívají 19-70 tisíc tokenů v závislosti na rozsahu zpracovávaných dat.

Doba vykonávání úkolů závisí na jejich charakteru. Jednoduché operace jako simulované čekání trvají podle nastavených parametrů, zatímco komplexní analýza kódu může trvat několik minut v závislosti na velikosti a složitosti analyzovaných souborů.

## Doporučení pro efektivní využití

Pro optimální výkon subagentů se doporučuje nespecifikovat úroveň paralelismu a nechat systém automaticky řídit počet současných úkolů. Tento přístup zajišťuje nejefektivnější využití dostupných zdrojů a minimalizuje celkový čas zpracování.

Subagenti představují významný krok vpřed v oblasti automatizované práce s kódem, i když jejich implementace má určitá omezení. Absence možnosti přizpůsobit úroveň paralelismu může v některých případech limitovat flexibilitu při řízení zatížení systému.

Task Tool v Claude Code tak poskytuje praktický nástroj pro rozdělení práce na menší, paralelně zpracovatelné úkoly, což značně zrychluje analýzu rozsáhlých projektů a umožňuje efektivnější využití výpočetních zdrojů umělé inteligence.