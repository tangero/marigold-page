---
layout: vibecoding-default
title: "Trae Agent je nově open source"
date: 2025-07-03
sw: Trae
---

Trae Agent je agent založený na LLM pro obecné úlohy softwarového inženýrství. nově byl [uvolněn jako open source](https://github.com/bytedance/trae-agent).

Trae Agent poskytuje výkonné rozhraní CLI, které dokáže porozumět instrukcím v přirozeném jazyce a provádět složité pracovní postupy softwarového inženýrství pomocí různých nástrojů a poskytovatelů LLM.

### Funkce

- 🌊 Lakeview: Poskytuje stručné a výstižné shrnutí kroků agenta
- 🤖 Podpora více LLM: Pracuje s oficiálními rozhraními API OpenAI a Anthropic
- 🛠️ Bohatý ekosystém nástrojů: Úprava souborů, spouštění bash, sekvenční myšlení a další funkce
- 🎯 Interaktivní režim: Konverzační rozhraní pro iterativní vývoj
- 📊 Záznam trajektorie: Podrobné zaznamenávání všech akcí agenta pro ladění a analýzu
- ⚙️ Flexibilní konfigurace: Konfigurace založená na JSON s podporou proměnných prostředí
- 🚀 Snadná instalace: Jednoduchá instalace pomocí pip


### Instalace:

K instalaci projektu doporučujeme použít UV.

git clone <repository-url> \
cd trae-agent \
uv sync