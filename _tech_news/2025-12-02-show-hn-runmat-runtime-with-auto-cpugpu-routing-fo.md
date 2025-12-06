---
author: Marisa Aigen
category: numerické výpočty
date: '2025-12-02 15:07:49'
description: RunMat je open-source runtime pro MATLAB kód, který automaticky fúzuje
  operace a inteligentně volí mezi CPU a GPU podle velikosti dat a nákladů na přenos.
  Tento systém umožňuje spouštět existující MATLAB nebo Octave skripty bez úprav a
  často překonává ručně optimalizovaný CUDA kód na hustých numerických úlohách.
importance: 3
layout: tech_news_article
original_title: 'Show HN: RunMat – runtime with auto CPU/GPU routing for dense math'
publishedAt: '2025-12-02T15:07:49+00:00'
slug: show-hn-runmat-runtime-with-auto-cpugpu-routing-fo
source:
  emoji: 📰
  id: null
  name: Github.com
title: RunMat – runtime s automatickým směrováním mezi CPU a GPU pro husté matematické
  výpočty
url: https://github.com/runmat-org/runmat
urlToImage: https://opengraph.githubassets.com/995056f5d3a93a1e3747cd33d6bf6b82a2dd3642bc1b96497ac5fad287a5349d/runmat-org/runmat
urlToImageBackup: https://opengraph.githubassets.com/995056f5d3a93a1e3747cd33d6bf6b82a2dd3642bc1b96497ac5fad287a5349d/runmat-org/runmat
---

## Souhrn
RunMat je open-source runtime navržený pro spouštění MATLAB kódu, který automaticky optimalizuje operace fúzí a směrováním mezi CPU a GPU. Vyvinutý Nabeelem, tento systém v srpnu překonal rychlostí GNU Octave a v nové verzi Accelerate (v0.2, pre-release) přidává podporu pro širokou škálu GPU bez nutnosti psaní kernelů nebo správy zařízení. Podporuje MATLAB syntax v souborech .m a běží na platformách jako macOS, Windows a Linux.

## Klíčové body
- Automatická fúze operací: Vytváří graf pole a spojuje elementární operace s redukcemi do optimalizovaných kernelů.
- Inteligentní volba CPU/GPU: Rozhoduje na základě velikosti dat a nákladů na přenos, bez manuálních příznaků.
- Cross-platform GPU podpora: NVIDIA, AMD, Apple Silicon, Intel přes Metal, DirectX 12 nebo Vulkan pomocí wgpu/WebGPU.
- Moderní CPU backend: Ignition interpret pro rychlý start, Turbine JIT (Cranelift) pro horké cesty a generační garbage collector optimalizovaný pro numerický kód.
- Memory-safe: Implementováno v Rustu, s podporou pro existující MATLAB/Octave skripty.

## Podrobnosti
RunMat umožňuje uživatelům psát matematické výpočty v čitelné MATLAB syntaxi, včetně polí, řízení toku a .m souborů. Systém interně buduje graf operací nad poli, fúzuje elementární funkce jako sčítání nebo násobení s redukcemi (např. součty nebo maximum) do větších kernelů a spouští je na nejvhodnějším hardware. Na GPU dosahuje výkonu srovnatelného s ručně napsaným CUDA kódem pro husté numerické workloady, jako matičné operace nebo lineární algebra, aniž by uživatel musel řešit vendor lock-in nebo přenos dat mezi zařízeními.

CPU část využívá Ignition interpret pro okamžité spuštění chladných kódů, což zkracuje čas startu oproti plně JIT systémům. Pro opakované výpočty se zapojuje Turbine JIT kompilátor založený na Craneliftu, který generuje nativní strojový kód. Garbage collector je generační a laděný pro numerické aplikace, kde dominují alokace velkých polí. Celý systém je napsán v Rustu, což zajišťuje bezpečnost paměti bez garbage collection overheadu typického pro MATLAB.

GPU backend spoléhá na wgpu, což je Rustová implementace WebGPU specifikace. To umožňuje podporu Metal na macOS (Apple Silicon), DirectX 12 na Windows a Vulkan na Linuxu, s fallbackem na CPU pro malé workloady, kde by přenos dat na GPU způsobil ztrátu výkonu. Plotting je v pre-release stavu: Základní 2D čáry a body fungují, ale složitější grafy jako povrchové, 3D pohledy nebo boxploty chybí nebo jsou nestabilní. Dokumentace je dostupná na webu a systém prošel tisíci testů, ale očekávají se hrany v uživatelském rozhraní.

Tento projekt vychází z původní srpnové verze diskutované na Hacker News, kde už tehdy překonal GNU Octave na testovaných úlohách. RunMat Accelerate rozšiřuje možnosti pro vědce a inženýry v oblastech numerických simulací, machine learningu nebo fyzikálního modelování, kteří chtějí využít GPU bez investic do proprietárních nástrojů jako MATLAB Parallel Computing Toolbox.

## Proč je to důležité
RunMat snižuje bariéru pro využití GPU v numerických výpočtech, kde tradičně vyžaduje znalost CUDA nebo OpenCL. Pro průmysl znamená cross-platform podporu větší flexibilitu – například přechod z NVIDIA na AMD bez přepisování kódu – a open-source model podporuje komunitní vývoj. V kontextu rostoucího zapojení AI do vědeckých výpočtů (např. trénink modelů na velkých datech) může urychlit workflow data scientistů pracujících s MATLAB/Octave. Nicméně jako pre-release verze (v0.2) potřebuje stabilizaci plottingu a širší testování na reálných aplikacích, aby konkuroval etablovaným řešením jako NumPy s CuPy nebo Julia.

---

[Číst původní článek](https://github.com/runmat-org/runmat)

**Zdroj:** 📰 Github.com
