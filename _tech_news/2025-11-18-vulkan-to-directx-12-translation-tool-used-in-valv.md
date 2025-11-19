---
author: Marisa Aigen
category: herní technologie
companies:
- Valve
- AMD
- Nvidia
- Microsoft
date: '2025-11-18 12:20:00'
description: Verze 3.0 nástroje VKD3D-Proton přináší podporu pro AMD FSR4, Anti-Lag
  a Work Graphs, zatímco Nvidia DLSS4 zůstává nepodporovaná. Aktualizace také zahrnuje
  přepsání shaderového backendu a vylepšení kompatibility her na Linuxu.
importance: 3
layout: tech_news_article
original_title: Vulkan-to-DirectX 12 translation tool used in Valve's Proton now supports
  AMD's FSR4 and Anti-Lag, while Nvidia's DLSS4 remains unsupported — FSR4 now also
  works on older GPUs, VKD3D-Proton v3.0 brings other performance improvements
publishedAt: '2025-11-18T12:20:00+00:00'
slug: vulkan-to-directx-12-translation-tool-used-in-valv
source:
  emoji: 📰
  id: null
  name: Tom's Hardware UK
title: Nástroj pro překlad Vulkan na DirectX 12 v Protonu nyní podporuje AMD FSR4
  a Anti-Lag, DLSS4 zatím ne
url: https://www.tomshardware.com/video-games/pc-gaming/vulkan-to-directx-12-translation-tool-used-in-valves-proton-now-supports-amds-fsr4-and-anti-lag-while-nvidias-dlss4-remains-unsupported-fsr4-now-also-works-on-older-gpus-vkd3d-proton-v3-0-brings-other-performance-improvements
urlToImage: https://cdn.mos.cms.futurecdn.net/BzGDjrpRM4RfbzmWDLM6nH-2400-80.jpg
urlToImageBackup: https://cdn.mos.cms.futurecdn.net/BzGDjrpRM4RfbzmWDLM6nH-2400-80.jpg
---

## Souhrn
Nástroj VKD3D-Proton, který překládá DirectX 12 na Vulkan pro běh Windows her na Linuxu prostřednictvím Protonu, dosáhl verze 3.0. Tato aktualizace přináší podporu pro AMD FSR4 a Anti-Lag, zatímco Nvidia DLSS4 zůstává mimo podporu. Nová verze také zahrnuje přepsání DXBC shaderového backendu a experimentální podporu pro Work Graphs.

## Klíčové body
- VKD3D-Proton v3.0 přidává podporu pro AMD FSR4 i na starších GPU pomocí fallback režimu.
- Nvidia DLSS4 není v Protonu podporována.
- Přepsání DXBC shaderového backendu opravuje řadu chyb a zlepšuje kompatibilitu her.
- Implementována experimentální podpora pro Work Graphs.
- FSR4 v fallback režimu není součástí oficiálních buildů Protonu – vyžaduje kompilaci ze zdrojového kódu.

## Podrobnosti
VKD3D-Proton je open-source nástroj vyvíjený komunitou ve spolupráci s Valvem, který umožňuje spouštět hry využívající DirectX 12 na Linuxu přes Vulkan API. Verze 3.0 přináší významné technické změny, zejména podporu pro AMD FSR4 (FidelityFX Super Resolution 4), což je upscalingová technologie zvyšující výkon her při zachování kvality obrazu. Vývojáři implementovali AGS WMMA intrinsics pomocí Vulkan rozšíření VK_KHR_cooperative_matrix a VK_KHR_shader_float8, což umožňuje FSR4 na GPU architektury RDNA 4 a novějších. Pro starší GPU existuje alternativní režim využívající int8 a float16, který je však výrazně pomalejší a není součástí oficiálních verzí Protonu – uživatelé jej musí sestavit sami ze zdrojového kódu.

Kromě toho byl kompletně přepsán DXBC shaderový backend, což odstraňuje mnoho chyb starého vkd3d-shader řešení a umožňuje spouštět dříve nefunkční hry. Tento krok také sjednocuje frontend s nástrojem DXVK (který překládá DirectX 8–11 na Vulkan), což usnadňuje údržbu obou projektů. Nově je také přidána experimentální podpora pro Work Graphs – novou DirectX 12 technologii pro efektivnější správu paralelních úloh na GPU.

## Proč je to důležité
Tato aktualizace posiluje pozici Linuxu jako herní platformy, zejména pro uživatele AMD GPU, kteří nyní získávají přístup k nejnovější generaci upscalingových technologií i mimo nativní podporu her. Zároveň zdůrazňuje rozdíly mezi proprietárními řešeními (jako DLSS od Nvidie) a otevřenými alternativami (jako FSR od AMD), které jsou snáze integrovatelné do open-source ekosystémů. Pro herní komunitu na Linuxu to znamená lepší výkon, širší kompatibilitu a menší závislost na Windows.

---

[Číst původní článek](https://www.tomshardware.com/video-games/pc-gaming/vulkan-to-directx-12-translation-tool-used-in-valves-proton-now-supports-amds-fsr4-and-anti-lag-while-nvidias-dlss4-remains-unsupported-fsr4-now-also-works-on-older-gpus-vkd3d-proton-v3-0-brings-other-performance-improvements)

**Zdroj:** 📰 Tom's Hardware UK
