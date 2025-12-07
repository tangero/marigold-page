---
author: Marisa Aigen
category: strojové učení
date: '2025-12-06 14:27:13'
description: Vývojář zveřejnil ranou verzi projektu torch-webgpu, který přináší backend
  pro PyTorch umožňující spouštět výpočty na WebGPU zařízeních. Projekt cílí na cross-platformní
  vysoký výkon bez závislosti na kernelech jako CUDA nebo MPS.
importance: 3
layout: tech_news_article
original_title: 'Show HN: WebGPU back end for PyTorch sneak peek'
publishedAt: '2025-12-06T14:27:13+00:00'
slug: show-hn-webgpu-back-end-for-pytorch-sneak-peek
source:
  emoji: 📰
  id: null
  name: Github.com
title: 'Ukázka: Experimentální backend WebGPU pro PyTorch'
url: https://github.com/jmaczan/torch-webgpu
urlToImage: https://opengraph.githubassets.com/6970a7200edec5a15f00c84c47881de71096f2a860a29ca89823778f2111b356/jmaczan/torch-webgpu
urlToImageBackup: https://opengraph.githubassets.com/6970a7200edec5a15f00c84c47881de71096f2a860a29ca89823778f2111b356/jmaczan/torch-webgpu
---

## Souhrn
Projekt torch-webgpu představuje experimentální backend pro knihovnu PyTorch, který umožňuje spouštět výpočty strojového učení přímo na WebGPU zařízeních. V současnosti lze vytvářet tenzory na WebGPU, provádět základní operace jako sčítání a přenášet data mezi CPU a WebGPU. Je to raná verze bez stabilního vydání, určená pro vývojáře a rané testéry.

## Klíčové body
- Spouštění PyTorch kódu s parametrem device="webgpu" a převod dat pomocí to="webgpu".
- Kompilace modelů pro WebGPU pomocí dekorátoru @torch.compile(backend=webgpu).
- Použití pěti komponent: PyTorch, Python, C++, WGSL shadery a WebGPU runtime z Google Dawn.
- Instalace vyžaduje klonování repozitáře, instalaci Dawn a spuštění skriptu build.sh.
- Omezení: pouze float32, synchronní odesílání úloh, nedostatek testů a fallback na CPU pro některé operace.

## Podrobnosti
WebGPU je moderní webový standard pro grafické a výpočetní API, který nahrazuje WebGL a umožňuje využívat GPU v prohlížečích pro obecné výpočty. PyTorch, oblíbená otevřená knihovna pro strojové učení, obvykle spoléhá na backendy jako CUDA pro Nvidia GPU, MPS pro Apple Silicon nebo ROCm pro AMD. Projekt torch-webgpu od vývojáře jmaczan se snaží tyto platformově specifické závislosti obejít a dosáhnout vysokého výkonu pouze pomocí standardních nástrojů.

Aktuální stav demonstruje jednoduchý příklad: vytvoření dvou tenzorů na WebGPU, jejich sčítání a ověření výsledku na CPU. Kód vypadá takto:

```python
a = torch.tensor([-1.5, 2.7, 1.0, 2.0], device="webgpu")
b = torch.tensor([-1.0, 0.9, 1.1, -2.1], device="webgpu")
result = a + b
expected = torch.tensor([-2.5, 3.6, 2.1, -0.1], device="cpu")
assert torch.allclose(result.to("cpu"), expected)
```

Instalace je náročná a určená pro zkušené uživatele: nejprve naklonovat repozitář z GitHubu, nainstalovat Google Dawn (implementaci WebGPU) podle jejich průvodce s CMake, nastavit proměnnou DAWN_PREFIX na cestu k instalaci (např. /home/user/dawn/install/Release) a spustit ./build.sh v repozitáři. Poté v Pythonu importovat torch_webgpu a používat device="webgpu".

Projekt má hrubé okraje: podporuje jen datový typ float32, odesílání úloh do fronty (wgpu::Queue.Submit()) probíhá synchronně, chybí dostatek unit testů (standardizace testování out-of-tree backendů je v decembri 2025 stále ve vývoji) a některé operace padají na CPU. Plánuje se přidávání nových operací, testování s CUDA/MPS/Intel GPU a přenos dat mezi nimi a WebGPU. Vývoj probíhá individuálně po pracovní době, bez týmu, což vysvětluje pomalý pokrok.

## Proč je to důležité
Tento projekt ukazuje potenciál pro spouštění modelů strojového učení přímo v prohlížeči bez nutnosti serveru nebo nativních aplikací, což otevírá dveře k lehčím webovým aplikacím s AI – například interaktivním nástrojům pro zpracování dat nebo jednoduchým inferenčním modelům. WebGPU je podporováno v Chrome, Edge a Firefoxu, takže je cross-platformní a nezávislé na operačním systému. Pokud se stabilizuje, mohlo by konkurovat existujícím webovým backendům jako ONNX Runtime Web nebo TensorFlow.js, ale s plnou kompatibilitou PyTorch. Pro průmysl znamená snížení závislosti na proprietárních GPU a snazší nasazení v cloudu nebo edge zařízeních. Nicméně v rané fázi je riziko nízké stability vysoké, což omezuje okamžité použití v produkci. V širším kontextu posiluje trend webových výpočetních API, které democratizují přístup k GPU výkonu.

---

[Číst původní článek](https://github.com/jmaczan/torch-webgpu)

**Zdroj:** 📰 Github.com
