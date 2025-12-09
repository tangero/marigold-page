---
author: Marisa Aigen
category: gpu programování
companies:
- NVIDIA
date: '2025-12-08 18:55:28'
description: NVIDIA představila významný upgrade svého softwaru CUDA nazvaný CUDA
  Tile, který mění programování grafických procesorů z modelu SIMT na tile-based přístup.
  Čipový architekt Jim Keller tvrdí, že tento krok usnadní přenos AI jader na hardware
  jiných výrobců a oslabí exkluzivitu CUDA.
importance: 4
layout: tech_news_article
original_title: NVIDIA Might End the ‘CUDA Moat’ With Its Latest Update, Says Chip
  Architect Jim Keller, Who Claims It Will Now Be Easier to Port Kernels
people:
- Jim Keller
publishedAt: '2025-12-08T18:55:28+00:00'
slug: nvidia-might-end-the-cuda-moat-with-its-latest-upd
source:
  emoji: 📰
  id: null
  name: Wccftech
title: NVIDIA podle čipového architekta Jima Kellera možná ukončí svůj 'CUDA příkop'
  novou aktualizací – portování jader bude snazší
url: https://wccftech.com/nvidia-might-end-the-cuda-moat-with-its-latest-update-says-jim-keller/
urlToImage: https://cdn.wccftech.com/wp-content/uploads/2023/06/Tenstorrent-RISC-V-AI-CPUs-Chiplets-Jim-Keller-_5-g-low_res-scale-2_00x.jpg
urlToImageBackup: https://cdn.wccftech.com/wp-content/uploads/2023/06/Tenstorrent-RISC-V-AI-CPUs-Chiplets-Jim-Keller-_5-g-low_res-scale-2_00x.jpg
---

### Souhrn
NVIDIA vydala jednu z nejvýznamnějších aktualizací svého softwarového balíku CUDA, nazvaného CUDA Tile, který nahrazuje tradiční model SIMT tile-based přístupem. Tento změna podle čipového architekta Jima Kellera znamená konec tzv. 'CUDA příkopu', tedy softwarové výhody, která bránila developerům v jednoduchém přenosu kódu na GPU od konkurentů. Výsledek je jednodušší programování GPU pro AI aplikace.

### Klíčové body
- Přechod z modelu SIMT (Single Instruction Multiple Threads) na tile-based programování, kde se GPU chová jako procesor zpracovávající dlaždice dat.
- Úvod nové nízkoúrovňové virtuální mašiny Tile IR, která abstrahuje složitosti GPU.
- Snížení potřeby manuálních optimalizací, jako je nastavování velikosti dlaždic, sdílené paměti nebo výpočetních zdrojů.
- Komentář Jima Kellera na sociálních sítích: přechod na dlaždice usnadní portování AI jader na hardware jako AMD nebo Intel.
- CUDA zůstává klíčovou platformou pro AI workflow, kterou dosud nikdo plně nenapodobil.

### Podrobnosti
CUDA je proprietární platforma NVIDIA pro paralelní výpočty na grafických procesorech (GPU), která umožňuje developerům psát kernele – malé programy spouštěné na tisících jader GPU současně. Tradičně vychází z modelu SIMT, kde jeden příkaz zpracovává více vláken dat paralelně, ale vyžaduje pečlivé ladění parametrů: velikost bloků vláken, množství dat v sdílené paměti nebo alokaci registra. Tyto optimalizace jsou časově náročné a specifické pro architekturu NVIDIA, což vytvářelo 'příkop' – bariéru pro migraci kódu na konkurenční platformy jako ROCm od AMD nebo oneAPI od Intelu.

Nový CUDA Tile mění tento paradigmat. Místo ručního řízení vláken zavádí tile-based model, inspirovaný moderními GPU architekturami, kde data a výpočty jsou organizovány do 'dlaždic' (tiles) – pevných bloků paměti a výkonu. GPU je nyní prezentováno jako tile procesor, kde programátor se soustředí na logiku algoritmu, zatímco kompilátor a Tile IR (nová intermediální reprezentace pro kompilaci) se starají o optimalizace. Tile IR funguje jako nízkoúrovňový virtuální stroj, který generuje efektivní kód pro různé NVIDIA GPU, včetně novějších jako Hopper nebo Blackwell.

Tento přístup snižuje složitost programování: developer nemusí experimentovat s velikostmi bloků nebo pamětí, což urychluje vývoj AI modelů, jako je trénink velkých jazykových modelů (LLM) nebo inferencia. Příkladem použití je přepsání konvolučních vrstev v neuronových sítích, kde CUDA Tile automaticky rozdělí data do dlaždic a zajistí koherenci mezi pamětí. NVIDIA tak reaguje na rostoucí tlak od konkurentů, kteří již tile-based modely používají (např. AMD CDNA architektury). Jim Keller, známý architekt čipů z AMD, Intelu a NVIDIA, to shrnul v tweetu z 7. prosince 2025: 'Pokud přejdou na dlaždice jako většina hardware, AI kernele budou snadněji portovatelné.'

### Proč je to důležité
Tato aktualizace oslabuje monopol NVIDIA v AI ekosystému, kde CUDA dominuje díky knihovnám jako cuDNN nebo TensorRT pro hluboké učení. Dosud developeři investovali měsíce do přepisování kódu pro ROCm nebo SYCL, což brzdilo adopci levnějších GPU od AMD (např. MI300X) nebo Intelu (Gaudi3). Snadnější portování umožní rychlejší diverzifikaci hardware v datových centrech, což sníží ceny AI výpočtů a donutí NVIDIA k větší inovaci.

Pro uživatele a firmy znamená to kratší dobu vývoje: malé týmy mohou nyní psát univerzálnější kód, kompilovatelný přes nástroje jako OpenAI Triton nebo tvůrci vlastních backendů. V širším kontextu to urychlí růst AI aplikací mimo NVIDIA ekosystém, ale zároveň zvyšuje riziko fragmentace – ne každý vendor bude mít ekvivalent Tile IR. NVIDIA si tak udržuje náskok, ale otevírá dveře konkurenci, což by mohlo zmírnit její 80% podíl na AI GPU trhu. Dlouhodobě to prospěje inovacím v AGI výzkumu, kde cena výpočtů je klíčová.

---

[Číst původní článek](https://wccftech.com/nvidia-might-end-the-cuda-moat-with-its-latest-update-says-jim-keller/)

**Zdroj:** 📰 Wccftech
