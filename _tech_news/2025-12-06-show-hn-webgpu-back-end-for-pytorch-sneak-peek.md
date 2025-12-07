---
author: Marisa Aigen
category: strojové učení
date: '2025-12-06 14:27:13'
description: Vývojář jmaczan zveřejnil experimentální repozitář torch-webgpu, který
  přidává podporu pro WebGPU jako backend v PyTorch. Projekt umožňuje spouštět základní
  operace s tenzory přímo na WebGPU zařízeních bez závislosti na CUDA, MPS nebo ROCm.
importance: 3
layout: tech_news_article
original_title: 'Show HN: WebGPU back end for PyTorch sneak peek'
publishedAt: '2025-12-06T14:27:13+00:00'
slug: show-hn-webgpu-back-end-for-pytorch-sneak-peek
source:
  emoji: 📰
  id: null
  name: Github.com
title: 'Show HN: Náhled na backend WebGPU pro PyTorch'
url: https://github.com/jmaczan/torch-webgpu
urlToImage: https://opengraph.githubassets.com/6970a7200edec5a15f00c84c47881de71096f2a860a29ca89823778f2111b356/jmaczan/torch-webgpu
urlToImageBackup: https://opengraph.githubassets.com/6970a7200edec5a15f00c84c47881de71096f2a860a29ca89823778f2111b356/jmaczan/torch-webgpu
---

## Souhrn
Experimentální projekt torch-webgpu přináší podporu pro WebGPU backend v PyTorch, což umožňuje spouštět kód strojového učení přímo na grafických procesorech v prohlížeči. V současnosti zvládá základní operace jako sčítání tenzorů a přenos dat mezi CPU a WebGPU. Cílem je kompilace PyTorch kódu pro WebGPU pomocí dekorátoru @torch.compile bez potřeby platformově specifických jáder.

## Klíčové body
- Podpora zařízení device="webgpu" pro tvorbu tenzorů a operace na nich.
- Kompilace modelu: @torch.compile(m, backend=webgpu) pro optimalizaci na WebGPU.
- Aktuální funkce: sčítání tenzorů na WebGPU, převod dat mezi CPU a WebGPU.
- Instalace vyžaduje klonování repozitáře, instalaci Google Dawn a spuštění build.sh.
- Omezení: pouze float32, synchronní zpracování fronty, nedostatek testů, některé operace padají na CPU.

## Podrobnosti
Projekt torch-webgpu je v rané fázi vývoje – není ani na verzi 0.0.1 – a slouží k testování PyTorch na WebGPU, což je nové webové API pro výpočty na GPU v prohlížeči. WebGPU navazuje na WebGL, ale zaměřuje se na compute shader'y, což umožňuje univerzální přístup k GPU bez ohledu na platformu, na rozdíl od CUDA (pro Nvidia), MPS (Apple) nebo ROCm (AMD). Vývojář používá pět klíčových složek: PyTorch pro strojové učení, Python pro skriptování, C++ pro nativní části, WGSL shadery pro GPU instrukce a WebGPU runtime, konkrétně Google Dawn jako implementaci.

Instalace je určena pro vývojáře: nejprve naklonujte repozitář z GitHubu (https://github.com/jmaczan/torch-webgpu), nainstalujte Dawn podle jejich průvodce (https://github.com/google/dawn/blob/main/docs/quickstart-cmake.md) a nastavte proměnnou DAWN_PREFIX na cestu k instalaci, například /home/user/dawn/install/Release. Poté spusťte ./build.sh v repozitáři. V Pythonu importujte torch_webgpu a používejte device="webgpu":

```python
a = torch.tensor([-1.5, 2.7, 1.0, 2.0], device="webgpu")
b = torch.tensor([-1.0, 0.9, 1.1, -2.1], device="webgpu")
result = a + b
assert torch.allclose(result.to("cpu"), torch.tensor([-2.5, 3.6, 2.1, -0.1]))
```

Toto demonstruje základní aritmetiku na WebGPU s ověřením na CPU. Mezi nedostatky patří synchronní volání wgpu::Queue.Submit(), což způsobuje blokování, podpora jen pro float32, absence komplexních testů (standardizace testů pro externí backends je v decembri 2025 stále ve vývoji) a fallback některých operací na CPU. Projekt plánuje rozšíření o další operace a integraci s testovacím frameworkem PyTorch.

## Proč je to důležité
Torch-webgpu představuje krok k běhu modelů strojového učení přímo v prohlížeči, což zvyšuje soukromí dat (výpočty na klientovi) a snižuje latenci oproti cloudovým řešením. V širším kontextu WebGPU standardizace od W3C umožňuje cross-platform výkon bez proprietárních knihoven, což by mohlo democratizovat přístup k akceleraci GPU pro webové aplikace, jako jsou interaktivní vizualizace dat nebo lehké inference modelů. Nicméně jako experimentální kód není vhodný pro produkci – chybí stabilita, široká podpora operací a optimalizace. Pro průmysl to znamená potenciál pro edge computing v prohlížeči, ale vyžaduje další vývoj, aby konkurovalo existujícím řešením jako TensorFlow.js nebo ONNX Runtime Web. V ekosystému PyTorch, dominantní knihovně pro výzkum AI, by úspěšná implementace mohla otevřít dveře k širšímu nasazení ML na webech bez serverové závislosti.

---

[Číst původní článek](https://github.com/jmaczan/torch-webgpu)

**Zdroj:** 📰 Github.com
