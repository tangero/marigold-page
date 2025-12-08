---
author: Marisa Aigen
category: vestavěné systémy
companies:
- Toradex
- NXP
date: '2025-12-06 21:19:50'
description: Toradex představil rodiny modulů OSM a Lino typu počítač na modulu s
  procesory NXP i.MX 93 a i.MX 91. Tyto ultrakompaktní moduly jsou určeny pro průmyslovou
  automatizaci ve velkém objemu a edge systémy, kde nabízejí odolné a cenově výhodné
  řešení pro prostředí s omezeným místem.
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
Toradex, švýcarský výrobce počítačů na modulu pro vestavěné systémy, představil nové rodiny OSM a Lino s procesory NXP i.MX 93 a i.MX 91. Tyto moduly velikosti mince cílí na aplikace v průmyslové automatizaci a edge výpočtech, kde je klíčová malá velikost, odolnost a nízká cena při vysokých objemech.

## Klíčové body
- Moduly OSM iMX93, OSM iMX91, Lino iMX93 a Lino iMX91 s procesory NXP i.MX 93 (2x Cortex-A55 na 1,75 GHz + NPU 0,5 TOPS) a i.MX 91 (2x Cortex-A55 na 1,6 GHz).
- Formáty OSM (standardizovaný pro malé moduly) a Lino (vlastní kompaktní řada Toradexu).
- Podpora pro edge AI díky NPU v i.MX 93, vhodné pro strojové učení na okraji sítě.
- Zaměřeno na vysoké objemy v průmyslu: odolnost vůči vibracím, teplotám a vlhkosti.
- Kompatibilita s Linuxem a Yocto Projectem pro rychlý vývoj.

## Podrobnosti
Toradex se specializuje na výrobu počítačů na modulu (Computer on Module, CoM), které slouží jako jádro vestavěných systémů. Nové moduly OSM a Lino rozšiřují portfolio o extrémně malé varianty, jejichž velikost odpovídá minci – přibližně 15 x 15 mm pro OSM Size-S. Rodina OSM dodržuje otevřený standard SGET (Standardization Group for Embedded Technologies), což zajišťuje snadnou vyměnitelnost a kompatibilitu s nosnými deskami od různých výrobců. Lino je naopak proprietární formát Toradexu optimalizovaný pro ještě menší rozměry a specifické aplikace.

Procesor NXP i.MX 93 přináší duální jádra Arm Cortex-A55 taktovaná na 1,75 GHz, grafický jádro Vivante GC7000NanoULTRA pro 2D/3D rendering a integrovanou neurální zpracovatelnou jednotku (NPU) s výkonem 0,5 TOPS. Tato NPU umožňuje hardware akceleraci úloh strojového učení, jako je detekce objektů v kamerových datech nebo prediktivní údržba v průmyslových zařízeních, bez nutnosti externích čipů. Slabší varianta i.MX 91 má podobnou architekturu, ale nižší frekvenci 1,6 GHz a bez NPU, což ji činí vhodnou pro méně náročné úlohy, jako je řízení senzorů nebo jednoduché IoT brány.

Moduly podporují rozhraní jako Gigabit Ethernet, USB 2.0, I²C, SPI, UART a až 2 GB LPDDR4 RAM s 16 GB eMMC úložištěm. Pro vývoj slouží Yocto Project a Linux kernel, které umožňují přizpůsobení systému pro dlouhodobou podporu (až 15 let). Toradex zdůrazňuje odolnost: moduly vydrží teploty od -40 °C do +85 °C, vibrace podle IEC 60068-2-6 a vlhkost do 95 %. To je ideální pro zařízení v továrnách, jako jsou robotické ramena, senzory v chytrých továrnách nebo edge servery pro zpracování dat z kamer.

V porovnání s předchozími moduly Toradexu, jako Colibri nebo Verdin, jsou tyto novinky o 50 % menší a levnější pro masovou produkci, což snižuje náklady na desku pod 20 USD v objemech nad 10 000 kusů.

## Proč je to důležité
V éře Industry 4.0 a edge AI roste poptávka po kompaktních procesorech schopných běžet lokálně bez cloudu, aby se minimalizovala latence a spotřeba dat. Tyto moduly umožňují integraci AI do stísněných prostorů, kde tradiční desky selhávají. Pro průmysl znamenají snížení nákladů na nasazení tisíců zařízení a delší životnost díky robustnosti. V širším kontextu posilují ekosystém NXP i.MX, které konkurují řešením od Qualcommu nebo Rockchipu, a podporují přechod k ARM-based edge systémům s AI akcelerací. Pro vývojáře je klíčová standardizace OSM, která zrychluje prototypování a snižuje rizika zastaralosti.

---

[Číst původní článek](https://linuxgizmos.com/toradex-introduces-coin-sized-modules-powered-with-nxp-i-mx-93-and-i-mx-91-processors/)

**Zdroj:** 📰 Linuxgizmos.com
