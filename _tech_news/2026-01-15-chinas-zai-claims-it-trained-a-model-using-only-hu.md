---
author: Marisa Aigen
category: hardware
companies:
- Zhipu AI
- Huawei
- Nvidia
date: '2026-01-15 02:27:31'
description: Společnost neuvedla, kolik zařízení použila, Nvidia tak může pravděpodobně
  klidně spát
importance: 4
layout: tech_news_article
original_title: China's Z.ai claims it trained a model using only Huawei hardware
publishedAt: '2026-01-15T02:27:31+00:00'
slug: chinas-zai-claims-it-trained-a-model-using-only-hu
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Čínská Z.ai tvrdí, že natrénovala model výhradně na hardware od Huawei
url: https://www.theregister.com/2026/01/15/zhipu_glm_image_huawei_hardware/
urlToImage: https://regmedia.co.uk/2025/03/17/leonardo_ai_china_ai_watermark.jpg
urlToImageBackup: https://regmedia.co.uk/2025/03/17/leonardo_ai_china_ai_watermark.jpg
---

## Souhrn
Čínská společnost Zhipu AI, prezentující se jako Z.ai, oznámila natrénování nového modelu GLM-Image výhradně na serverech od Huawei. Jedná se údajně o první pokročilý model umělé inteligence vyvinutý čistě na čínském hardwaru bez závislosti na zahraničních komponentech. Model slouží k společnému generování obrázků a textu pomocí hybridní architektury.

## Klíčové body
- Trénink proběhl na serverech Ascend Atlas 800T A2 s čtyřmi procesory Kunpeng 920 (na bázi Arm jader, 48 nebo 64 jader na procesor) a AI čipy Ascend 910.
- Architektura zahrnuje autoregresivní generátor s 9 miliardami parametrů (inicializovaný z GLM-4-9B-0414) a difúzní dekodér s 7 miliardami parametrů na bázi DiT.
- Huawei Ascend 910C dosahuje přibližně 800 TFLOPS ve FP16 přesnosti, což je zhruba 80 procent výkonu Nvidia H100.
- Model generuje kompaktní kódování 256 tokenů, které rozšiřuje na 1K–4K tokenů pro výstupy odpovídající 1K–2K pixelům vysokého rozlišení.
- Dostupný na platformě Hugging Face v sekci model-mart.

## Podrobnosti
Zhipu AI je čínský vývojář modelů řady General Language Model (GLM), které slouží k obecnému zpracování jazyka a nabízejí chatbot na adrese z.ai. Nový GLM-Image představuje pokrok v multimodalních modelech tím, že integruje generování obrázků s jazykovými schopnostmi. Klíčovou inovací je hybridní architektura založená na autoregresivním modelu pro počáteční kódování scény a difúzním dekodéru pro finální dekódování latentního prostoru do obrázku. Autoregresivní část, s rozšířenou slovní zásobou pro vizuální tokeny, nejprve vytvoří kompaktní reprezentaci a poté ji expanduje, což umožňuje efektivní tvorbu detailních obrázků. Difúzní dekodér na architektuře single-stream DiT obsahuje Glyph Encoder pro textové prvky, díky čemuž model přesně vykresluje text v generovaných obrázcích – problém, který trápí mnoho současných nástrojů jako Nano Banana Pro.

Hardware od Huawei zahrnuje servery Ascend Atlas 800T A2, které kombinují procesory Kunpeng 920 (vlastní Arm design Huawei) pro obecné výpočty a specializované AI čipy Ascend 910 pro trénink neuronových sítí. Nejnovější varianta 910C, uvedená v roce 2025, slibuje výkon blízký Nvidia H100, ale reálná efektivita závisí na softwarovém stacku a optimalizaci. Zhipu AI neuvedla množství použitých serverů ani spotřebu energie, což ztěžuje posouzení nákladů a škálovatelnosti. Pro trénink modelu s celkovými 16 miliardami parametrů by bylo pravděpodobně potřeba tisíce čipů, což zdůrazňuje limity současného čínského hardware oproti americkým alternativám. Model je optimalizován pro aplikace jako tvorba vizuálního obsahu z textových popisů, což ho činí užitečným pro designéry, marketéry nebo tvůrce obsahu.

## Proč je to důležité
Tento vývoj posiluje snahu Číny o technologickou soběstačnost v oblasti umělé inteligence v době amerických sankcí na export pokročilých čipů. Závislost na Nvidia GPU byla pro čínské firmy kritickým problémem; natrénování na domácím hardwaru umožňuje pokračovat v soutěži bez omezení. Pro globální průmysl to znamená rostoucí konkurenci z Asie, kde Huawei buduje ekosystém alternativního AI hardware. Nicméně nižší výkon Ascend čipů vyžaduje větší objem zařízení, což zvyšuje náklady a energetickou náročnost. Dlouhodobě to může ovlivnit ceny AI služeb a urychlit diverzifikaci dodavatelských řetězců mimo USA, ale zatím Nvidia zůstává dominantní díky lepší ekosystému CUDA a vyšší efektivitě.

---

[Číst původní článek](https://www.theregister.com/2026/01/15/zhipu_glm_image_huawei_hardware/)

**Zdroj:** 📰 Theregister.com
