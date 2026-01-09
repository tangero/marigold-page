---
author: Marisa Aigen
category: ai hardware
companies:
- NVIDIA
date: '2026-01-08 02:43:29'
description: NVIDIA představuje aktualizace svého softwaru pro inference na architektuře
  Blackwell, které výrazně zvyšují propustnost tokenů u modelů typu směs expertů (MoE),
  jako je DeepSeek-R1. Tato optimalizace kombinuje hardwareové inovace s softwarem
  TensorRT-LLM pro nižší náklady na zpracování.
importance: 4
layout: tech_news_article
original_title: Delivering Massive Performance Leaps for Mixture of Experts Inference
  on NVIDIA Blackwell
publishedAt: '2026-01-08T02:43:29+00:00'
slug: delivering-massive-performance-leaps-for-mixture-o
source:
  emoji: 📰
  id: null
  name: Nvidia.com
title: Masivní zlepšení výkonu inference směsi expertů na NVIDIA Blackwell
url: https://developer.nvidia.com/blog/delivering-massive-performance-leaps-for-mixture-of-experts-inference-on-nvidia-blackwell/
urlToImage: https://developer-blogs.nvidia.com/wp-content/uploads/2026/01/gb200-nvl-rack-gtc24-press-1920x1080-1.jpg
urlToImageBackup: https://developer-blogs.nvidia.com/wp-content/uploads/2026/01/gb200-nvl-rack-gtc24-press-1920x1080-1.jpg
---

## Souhrn
NVIDIA optimalizuje inference modelů směsi expertů (MoE) na nové architektuře Blackwell pomocí aktualizací softwaru TensorRT-LLM a plného využití hardwarových funkcí. Tato řešení zvyšují propustnost tokenů na watt v racku GB200 NVL72 s 72 GPU, což snižuje náklady na generování tokenů. Zaměření je na modely jako DeepSeek-R1, který patří mezi špičkové řídicí MoE modely.

## Klíčové body
- Rack GB200 NVL72 spojuje 72 Blackwell GPU přes pátou generaci NVLink s propustností 1 800 GB/s mezi všemi čipy.
- Hardwareová podpora formátu NVFP4, čtyřbitového plovoucího bodu optimalizovaného pro přesnost.
- Aktualizace TensorRT-LLM zlepšují výkon inference pro MoE modely s častými výměnami dat mezi experty.
- Disagregované zpracování odděluje prefill od dekódování pro lepší škálovatelnost.
- Optimalizace prodlužují životnost stávajících NVIDIA GPU v cloudu a enterprise prostředích.

## Podrobnosti
Architektura NVIDIA Blackwell, ztělesněná v platformě GB200 NVL72, je navržena pro velké škály AI výpočtů, zejména pro sparse MoE modely. Tyto modely, jako DeepSeek-R1, rozdělují zpracování na specializované experty, což vyžaduje intenzivní komunikaci mezi nimi při generování tokenů. Rack spojuje 72 GPU přes NVLink Switch čipy páté generace, které zajišťují 1 800 GB/s obousměrnou propustnost. Tato vysoká rychlost komunikace minimalizuje zpoždění při výměnách dat, což je klíčové pro MoE architektury, kde experti na různých GPU musí synchronizovat své výstupy.

Software TensorRT-LLM, knihovna pro optimalizaci inference velkých jazykových modelů (LLM), nyní plně využívá Blackwellovy schopnosti. Mezi novinky patří podpora NVFP4, NVIDIA navrženého formátu s čtyřmi bity pro plovoucí čísla, který lepší zachovává přesnost oproti standardním FP4 variantám. To umožňuje efektivnější kvantizaci modelů bez výrazné ztráty kvality. Další optimalizace zahrnují disaggregated serving, kde fáze prefill (zpracování vstupního textu) probíhá odděleně od dekódování (generování tokenů). Tento přístup umožňuje paralelizaci na větším počtu GPU a zvyšuje celkovou propustnost.

NVIDIA zdůrazňuje ko-design napříč GPU, CPU, sítěmi, napájením a chlazením, což zvyšuje tokeny na watt. To přímo snižuje cenu za milion tokenů, což je kritérium pro cloudové poskytovatele (CSP), jako jsou hyperscaleři. Aktualizace softwaru navíc zlepšují výkon i na starším hardware, čímž prodlužují jeho využitelnost v existujících datacentrech modelových tvůrců a firem. DeepSeek-R1 slouží jako testovací model – sparse MoE s pokročilým uvažováním, kde tyto změny přinášejí výrazné zlepšení oproti předchozím generacím.

## Proč je to důležité
Tyto pokroky posilují dominanci NVIDIA v AI inference, kde MoE modely rostou v popularitě díky vyšší efektivitě oproti hustým modelům. Pro průmysl znamená nižší provozní náklady a vyšší škálovatelnost, což umožňuje delší provoz stávající infrastruktury při rostoucí poptávce po AI službách. Uživatelé od spotřebitelů po enterprise získají rychlejší odpovědi za nižší cenu, ale závislost na NVIDIA ekosystému omezuje volby. V širším kontextu urychlují přechod k efektivnějším AI systémům, kde energie a throughput rozhodují o konkurenceschopnosti, a posouvají hranice toho, co je možné v reálném čase s velkými modely.

---

[Číst původní článek](https://developer.nvidia.com/blog/delivering-massive-performance-leaps-for-mixture-of-experts-inference-on-nvidia-blackwell/)

**Zdroj:** 📰 Nvidia.com
