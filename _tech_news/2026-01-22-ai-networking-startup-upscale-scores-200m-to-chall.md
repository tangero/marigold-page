---
author: Marisa Aigen
category: ai hardware
companies:
- Upscale AI
- Nvidia
date: '2026-01-22 00:07:56'
description: Startup Upscale AI oznámil získání 200 milionů dolarů v Series A financování
  na vývoj síťových switchů pro rack-scale AI systémy, které mají konkurovat dominanci
  Nvidia. Plánuje použít své čipy SkyHammer v prvních UALink switchech letos později.
importance: 4
layout: tech_news_article
original_title: AI networking startup Upscale scores $200M to challenge Nvidia's NVSwitch
publishedAt: '2026-01-22T00:07:56+00:00'
slug: ai-networking-startup-upscale-scores-200m-to-chall
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Startup Upscale získává 200 milionů dolarů na výzvu NVSwitch od Nvidia
url: https://www.theregister.com/2026/01/22/upscale_skyhammer_nvidia/
urlToImage: https://regmedia.co.uk/2023/07/13/shutterstock_hammeranvil.jpg
urlToImageBackup: https://regmedia.co.uk/2023/07/13/shutterstock_hammeranvil.jpg
---

## Souhrn
Startup Upscale AI, specializující se na síťovou infrastrukturu pro AI, získal 200 milionů dolarů v Series A kolu financování. Peníze má použít na vývoj switchů, které vyzvou dominanci Nvidia v technologii NVSwitch pro rack-scale AI systémy. Společnost, založená minulý rok s podporou Intelu, AMD a Qualcomm, plánuje nasadit svůj vlastní ASIC SkyHammer do UALink switchů ještě letos.

## Klíčové body
- Získání 200 milionů dolarů v Series A financování pro výzvu Nvidia.
- Vývoj SkyHammer ASIC pro scale-up síťové switche optimalizované pro AI workloady.
- Podpora od Intelu, AMD a Qualcomm; konkurence včetně Cisco a AMD.
- První produkty: standalone ASIC, integrovaný switch blade a rack letos.
- Zaměření na UALink protokol jako alternativu k NVLink.

## Podrobnosti
Upscale AI, startup založený v roce 2025, se zaměřuje výhradně na síťovou architekturu pro velké AI clustery, kde tradiční ethernetové řešení selhávají kvůli latenci a propustnosti. Nvidia dlouhodobě dominuje touto oblastí díky NVLink, vysokorychlostní interconnect technologii, která umožňuje propojit více GPU tak, aby paměť a výpočetní zdroje působily jako jediný logický celek. Tato technologie debutovala v roce 2024 a je klíčová pro systémy jako NVL72 racky od Nvidia, kde NVSwitch slouží k přímému propojení desítek GPU s minimálními ztrátami.

Konkurence se snaží dohnat: AMD a Cisco vyvíjejí Ultra Accelerator Link (UALink) a Ethernet for Scale-Up AI Infrastructure (ESUN), ale tyto standardy jsou zatím nedozrálé. První UALink systémy od AMD přijdou letos, ale budou protokol tunelovat přes ethernet, což snižuje výkon. Upscale chce tento mezer překlenout pomocí custom ASIC SkyHammer, který je navržený čistě pro scale-up AI networking. „Místo úprav starých systémů představujeme nový koncept škálování v AI sítích,“ řekl CEO Barun Kar pro El Reg. SkyHammer bude dostupný jako samostatný čip pro integraci do hyperscalerových systémů, ale i jako kompletní switch blade nebo celý rack.

Technické detaily zatím nejsou plně zveřejněny, ale Kar zmínil memory semantic-based load-store architekturu, což naznačuje optimalizaci pro přímý přístup k paměti napříč uzly bez kopírování dat. To by mohlo konkurovat NVSwitch 6 nebo Broadcom Tomahawk 6, i když přímé srovnání chybí. Upscale tak vstupuje do soutěže s giganty jako Cisco a AMD, kteří také cílí na otevřené standardy jako UALink, aby zabránili vendor lock-in u Nvidia.

## Proč je to důležité
Tento funding posiluje konkurenci v kritické oblasti AI hardware, kde Nvidia kontroluje až 90 % trhu s GPU a interconnecty. Pro hyperscalery jako Google nebo Microsoft znamená alternativy k NVLink snížení nákladů a závislosti na jednom dodavateli, což umožní rychlejší škálování AI tréninků na tisíce GPU. Pokud SkyHammer splní sliby, UALink se stane reálnou standardizací, podobně jako PCIe v minulosti, a urychlí inovace v rack-scale AI. Pro průmysl to znamená potenciálně nižší ceny switchů a otevřenější ekosystém, ale úspěch závisí na výkonu oproti Nvidia – zatím jde o slibný, ale neověřený tah v boji o miliardový trh AI sítí.

---

[Číst původní článek](https://www.theregister.com/2026/01/22/upscale_skyhammer_nvidia/)

**Zdroj:** 📰 Theregister.com
