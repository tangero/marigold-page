---
author: Marisa Aigen
category: vestavěné systémy
companies:
- Toradex
- NXP
date: '2025-12-06 21:19:50'
description: Toradex představil rodiny modulů OSM a Lino Computer on Module s procesory
  NXP i.MX 93 a i.MX 91. Tyto ultrakompaktní moduly jsou určeny pro průmyslovou automatizaci
  ve velkém měřítku a edge systémy, kde nabízejí odolné a cenově dostupné řešení pro
  prostory s omezeným místem.
importance: 3
layout: tech_news_article
original_title: Toradex Introduces Coin-Sized Modules Powered with NXP i.MX 93 and
  i.MX 91 Processors
publishedAt: '2025-12-06T21:19:50+00:00'
slug: toradex-introduces-coin-sized-modules-powered-with
source:
  emoji: 📰
  id: null
  name: Linuxgizmos.com
title: Toradex představuje moduly velikosti mince s procesory NXP i.MX 93 a i.MX 91
url: https://linuxgizmos.com/toradex-introduces-coin-sized-modules-powered-with-nxp-i-mx-93-and-i-mx-91-processors/
urlToImage: https://linuxgizmos.com/files/OSM-Family_top-View.jpg
urlToImageBackup: https://linuxgizmos.com/files/OSM-Family_top-View.jpg
---

## Souhrn
Toradex, švýcarský výrobce počítačů na modulích pro vestavěné systémy, uvedl na trh nové rodiny OSM a Lino. Ty integrují procesory NXP i.MX 93 a i.MX 91 a mají velikost mince. Cílí na aplikace v průmyslové automatizaci a edge výpočtech s podporou základního strojového učení.

## Klíčové body
- Moduly OSM iMX93, OSM iMX91, Lino iMX93 a Lino iMX91 s procesory NXP pro škálovatelné výpočty.
- Procesor i.MX 93 obsahuje neuronovou zpracovatelskou jednotku (NPU) s výkonem 0,5 TOPS pro urychlené strojové učení v aplikacích jako detekce obrazu.
- Formáty OSM (otevřený standard) a Lino (vlastní formát Toradexu) umožňují kompaktní design pro vysoké objemy výroby.
- Zaměření na odolnost a nízké náklady v prostředích s omezeným prostorem, jako jsou průmyslové senzory nebo edge zařízení.
- Podpora pro Linux a další vestavěné operační systémy.

## Podrobnosti
Toradex se specializuje na vývoj počítačů na modulích (Computer on Module, CoM), které slouží jako jádra vestavěných systémů. Tyto moduly se připojují k nosným deskám a umožňují rychlý vývoj zařízení bez nutnosti navrhovat procesorovou část od nuly. Nové moduly OSM a Lino jsou extrémně malé – velikosti mince – což je činí ideálními pro aplikace, kde je klíčové minimalizovat rozměry, například v IoT senzorech, průmyslových řídicích jednotkách nebo edge zařízeních pro zpracování dat na okraji sítě.

Rodina OSM dodržuje otevřený standard SGET (Standardization Group for Embedded Technologies), což zajišťuje kompatibilitu s produkty jiných výrobců a usnadňuje migraci. Naopak Lino je proprietární formát Toradexu, optimalizovaný pro jejich ekosystém, s menším počtem pinů pro ještě kompaktnější design. Procesory NXP i.MX 93 a i.MX 91 patří do řady pro nízkovýkonná embedded zařízení. i.MX 93 je výkonnější varianta s dvěma Cortex-A55 jádry na 1,7 GHz, grafickým jádrem Vivante GC Nano ULTRA a především NPU s 0,5 TOPS. Tato jednotka urychluje inferenci neuronových sítí, například pro rozpoznávání objektů v obrazech z kamer v průmyslovém prostředí, kde není možné spoléhat se na cloud kvůli latenci nebo bezpečnosti.
i.MX 91 je slabší, s jedním Cortex-A55 jádrem na 1,4 GHz, vhodný pro jednodušší úlohy jako sběr dat nebo základní řízení. Oba podporují Linux, RTOS a frameworky jako TensorFlow Lite pro edge AI. Moduly jsou navrženy pro vysoké objemy – od tisíců kusů – s dlouhou životností (až 10–15 let), což je klíčové pro průmysl. Toradex poskytuje kompletní podporu včetně Yocto Linux distribuce, která slouží k vytváření vlastních vestavěných obrazů systému.

## Proč je to důležité
Tyto moduly zaplňují mezeru v trhu s ultrakompaktními řešeními pro edge computing, kde tradiční desky jako Raspberry Pi selhávají kvůli velikosti nebo odolnosti. S NPU v i.MX 93 umožňují nasazení jednoduchého strojového učení přímo v zařízení, což snižuje závislost na cloudu a zvyšuje bezpečnost dat v průmyslu 4.0. Nicméně 0,5 TOPS je nízký výkon oproti moderním AI čipům (např. NVIDIA Jetson s desítkami TOPS), takže se hodí spíše pro základní úlohy jako detekce defektů na výrobní lince než složité vize. Pro menší firmy a výrobce OEM to znamená cenově dostupný vstup do AI-edge bez velkých investic, což podporuje širší adopci vestavěného AI v automatizaci. V kontextu rostoucího trhu embedded systémů (odhadovaný na miliardy dolarů) posiluje Toradex pozici proti konkurentům jako Variscite nebo TechNexion.

---

[Číst původní článek](https://linuxgizmos.com/toradex-introduces-coin-sized-modules-powered-with-nxp-i-mx-93-and-i-mx-91-processors/)

**Zdroj:** 📰 Linuxgizmos.com
