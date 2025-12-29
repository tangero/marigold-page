---
author: Marisa Aigen
category: ai
companies:
- Nvidia
- Groq
date: '2025-12-28 09:00:00'
description: Nvidia získala neexkluzivní licenci na pokročilou inference technologii
  od firmy Groq za 20 miliard dolarů, včetně jejich inženýrského týmu a patentů, aniž
  by koupila celou společnost. Tento krok vyvolává otázky ohledně obcházení regulačních
  schválení FTC.
importance: 5
layout: tech_news_article
original_title: Daily Tech News 28 December 2025
publishedAt: '2025-12-28T09:00:00+00:00'
slug: daily-tech-news-28-december-2025
source:
  emoji: 📰
  id: null
  name: Acecomments.mu.nu
title: Nvidia zaplatila 20 miliard dolarů za neexkluzivní licenci na technologii inference
  od Groq
url: https://acecomments.mu.nu/?post=417879
---

## Souhrn
Nvidia investovala 20 miliard dolarů do neexkluzivní licence na technologii inference od startupu Groq, který se specializuje na čipy optimalizované pro spouštění trénovaných modelů velkých jazykových modelů (LLM). Deal zahrnuje převzetí klíčového inženýrského týmu, patentů a obchodních tajemství, ale ne samotnou firmu ani její cloudovou službu GroqCloud, která nyní zůstává bez podpory.

## Klíčové body
- Nvidia zaplatila 20 miliard dolarů za neexkluzivní přístup k technologii Groq, která využívá stovky megabajtů interní SRAM místo gigabajtů externí DRAM pro extrémně vysokou propustnost 80 TB/s na čip.
- Převzato bylo vedení, inženýři, patenty a know-how, což prakticky vyprázdnilo GroqCloud z jeho jádra.
- Tento krok umožňuje Nvidii vyhnout se plné akvizici a souvisejícím regulačním schválením od FTC.
- Technologie je ideální pro inference (spouštění) LLM, ne pro jejich trénink.
- Další zpráva: Nvidia ukončuje podporu pro architekturu Pascal (RTX 10xx série) na Linuxu po devíti letech.

## Podrobnosti
Firma Groq, založená v roce 2016, se zaměřuje na vývoj specializovaných čipů pro úlohy inference v AI. Na rozdíl od konvenčních GPU od Nvidia, které spoléhají na velké množství externí paměti DRAM, Groq chips používají masivní interní SRAM – stovky megabajtů na čip – což umožňuje dosáhnout úžasné propustnosti 80 terabajtů za sekundu na jeden čip. Tato architektura je nevhodná pro trénink LLM, kde je potřeba obrovská kapacita paměti a výpočetní síla, ale exceluje v inference, tedy v rychlém spouštění hotových modelů pro generování odpovědí, jako je to v ChatGPT nebo podobných službách. GroqCloud, jejich cloudová platforma, umožňovala uživatelům spouštět inference na těchto čipech rychleji než na standardních GPU.

Deal s Nvidii, oznámený v prosinci 2025, není klasickou akvizicí. Nvidia získala pouze neexkluzivní licenci na technologii, což znamená, že Groq teoreticky může prodávat práva i jiným. Nicméně součástí bylo převzetí celého inženýrského a výkonnostního týmu, všech patentů a obchodních tajemství. GroqCloud zůstává pod kontrolou bývalého finančního ředitele, bez inženýrů a bez důvodu k existence – prakticky odsouzen k úpadku. Právníci obou stran tvrdí, že jde o legitimní transakci, ale článek naznačuje podezření z podvodu, protože struktura připomíná skrytou akvizici. FTC pravděpodobně zahájí vyšetřování, podobně jako u jiných velkých AI dealů, kde Nvidia čelí obviněním z monopolních praktik.

V širším kontextu to ukazuje na agresivní strategii Nvidia v AI hardwaru. Společnost dominuje trhu s GPU pro trénink (např. H100, Blackwell), ale inference je rostoucí oblast díky masovému nasazení LLM. Přístup k Groq technologii posílí jejich portfolio pro edge inference nebo datacentra, kde rychlost a efektivita snižují náklady na provoz AI služeb. Paralelně Nvidia ukončila podporu pro starou architekturu Pascal (RTX 10xx série z roku 2016) v Linux driverech po devíti letech, což ovlivní uživatele Linuxu s těmito kartami. Open-source drivéry však umožňují pokračovat v použití s úpravami.

## Proč je to důležité
Tento deal za 20 miliard dolarů představuje největší investici do inference hardwaru v historii AI a posiluje dominanci Nvidia v celém AI stacku. Pokud FTC nezasáhne, otevře to dveře k podobným strukturám transakcí, které obcházejí antimonopolní pravidla – což by mohlo zpomalit konkurenci jako AMD nebo nové hráče v custom AI čipech (např. od Google TPU nebo Amazon Trainium). Pro průmysl znamená rychlejší a levnější inference pro miliardy dotazů denně v AI aplikacích, od chatbotů po autonomní systémy. Uživatelé pocítí nižší latenci v AI službách, ale riziko je koncentrace moci u jednoho giganta, což brzdí inovace. V kontextu AGI pokroku je inference klíčová pro škálování, protože trénink je již optimalizován, zatímco inference tvoří 90 % provozních nákladů velkých modelů.

---

[Číst původní článek](https://acecomments.mu.nu/?post=417879)

**Zdroj:** 📰 Acecomments.mu.nu
