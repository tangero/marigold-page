---
date: 2024-07-05
hide: true
layout: post
order: 2
title: Technologie Transformátorů - ani hračka, ani elektrosoučástka, ale neuronová
  síť
---

Základem LLM je architektura [Transformátorů](/ai/transformatory/), představená v roce 2017 v průlomové práci ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762). Tato architektura přinesla několik klíčových inovací, které umožnily zpracování dlouhých sekvencí textu s velkou efektivitou a přesností. Technologie [transformátorů](/ai/transformatory/) dnes stojí v základech LLM jako jsou GPT - kde to písmeno T jsou právě [Transformátory](/ai/transformatory/). 

Jádrem transformátorové architektury je mechanismus pozornosti *(attention mechanism)*. Tento mechanismus umožňuje modelu dynamicky "zaměřit se" na různé části vstupního textu při generování každého výstupního tokenu. To je zásadní vylepšení oproti předchozím rekurentním neuronovým sítím (RNN), které zpracovávaly text sekvenčně. Mechanismus pozornosti umožňuje paralelní zpracování, což významně zrychluje trénink i inferenci.

Konkrétně, [Transformátory](/ai/transformatory/) používá tzv. "self-attention", kde každý [token](/ai/tokeny-versus-slova/) v sekvenci interaguje se všemi ostatními [tokeny](/ai/tokeny-versus-slova/). To se děje pomocí tří vektorů pro každý [token](/ai/tokeny-versus-slova/): dotaz (query), klíč (key) a hodnota (value). Tyto vektory jsou lineárními transformacemi vstupního embeddigu tokenu. Pozornost se počítá jako vážený součet hodnot, kde váhy jsou určeny skalárním součinem dotazu s klíči.

LLM typicky používají tzv. *multi-head attention*, kde se několik mechanismů pozornosti aplikuje paralelně. To umožňuje modelu zachytit různé typy vztahů mezi [tokeny](/ai/tokeny-versus-slova/) současně.

Další klíčovou součástí architektury jsou feed-forward [neuronové sítě](/ai/neuronove-site/). Ty se aplikují na výstup z attention vrstev a umožňují modelu provádět nelineární transformace reprezentací. Typicky se skládají ze dvou lineárních transformací s aktivační funkcí ReLU mezi nimi.

Moderní LLM jako GPT (Generative Pre-trained Transformer) používají pouze dekodérovou část původní architektury transformátorů. To znamená, že model generuje text autoregresivně, tedy token po tokenu, přičemž každý nový token je generován na základě všech předchozích tokenů.

Důležitou součástí architektury jsou také reziduální spojení a normalizační vrstvy. Reziduální spojení umožňují efektivní trénink velmi hlubokých sítí tím, že poskytují přímou cestu pro zpětnou propagaci gradientů. Normalizační vrstvy pak stabilizují aktivace v síti, což opět usnadňuje trénink.

## Trénink LLM

Trénink LLM probíhá na masivních datových sadách, často obsahujících stovky miliard tokenů. Cílem tréninku je minimalizovat tzv. cross-entropy loss, což v praxi znamená maximalizovat pravděpodobnost, že model správně předpoví další token v sekvenci.

Klíčovou inovací v tréninku LLM je použití tzv. kauzální masek v mechanismu pozornosti. Tyto masky zajišťují, že model při predikci dalšího tokenu může přistupovat pouze k předchozím tokenům, nikoli k budoucím. To umožňuje efektivní paralelní trénink, zatímco se zachovává autoregresivní povaha modelu.

Velikost moderních LLM je ohromující. Například GPT-3 má 175 miliard parametrů. To znamená, že model musí během tréninku optimalizovat 175 miliard čísel. Taková velikost přináší výzvy v oblasti efektivního tréninku a inference.

Pro efektivní trénink tak velkých modelů se používají techniky jako model parallelism a pipeline parallelism. Model parallelism rozděluje parametry modelu mezi více GPU, zatímco pipeline parallelism rozděluje vrstvy modelu mezi GPU. Tyto techniky umožňují trénovat modely, které by se jinak nevešly do paměti jediného GPU.

Dalším důležitým aspektem LLM je jejich schopnost few-shot learningu. To znamená, že model dokáže adaptovat své chování na nové úkoly s minimálním množstvím příkladů. Tato schopnost emerguje s rostoucí velikostí modelu a je jedním z nejzajímavějších aspektů současných LLM.

Inference v LLM, tedy proces generování textu, probíhá token po tokenu. V každém kroku model generuje pravděpodobnostní distribuci přes celý slovník možných následujících tokenů. Z této distribuce se vybírá další token, často s použitím technik jako top-k nebo nucleus sampling, které umožňují kontrolovat míru "kreativnosti" generovaného textu.

Zajímavým aspektem LLM je jejich schopnost provádět tzv. in-context learning. To znamená, že model dokáže adaptovat své chování na základě kontextu poskytnutého v promptu, aniž by se měnily jeho parametry. Tato schopnost umožňuje použití technik jako few-shot learning nebo chain-of-thought prompting, které významně rozšiřují možnosti využití LLM.

Nedávné výzkumy také ukázaly, že LLM vykazují emergentní schopnosti. To jsou schopnosti, které nebyly explicitně natrénovány, ale objevují se s rostoucí velikostí modelu. Mezi tyto schopnosti patří například schopnost řešit matematické úlohy, programovat, nebo dokonce provádět víceúrovňové uvažování.

Navzdory svým impozantním schopnostem mají LLM několik významných omezení. Jedním z nich je tendence k "halucinacím", tedy generování informací, které jsou věrohodné, ale fakticky nesprávné. Dalším problémem je omezená velikost kontextového okna, což limituje schopnost modelu pracovat s velmi dlouhými texty.

Pro adresování těchto omezení se vyvíjejí různé techniky. Například Retrieval-Augmented Generation (RAG) kombinuje LLM s vyhledáváním v externí databázi znalostí, což může zlepšit faktickou přesnost generovaného textu. Techniky jako kNN-LM nebo Memorizing Transformers se snaží rozšířit efektivní kontext modelu.

Závěrem lze říci, že [neuronové sítě](/ai/neuronove-site/) v LLM představují fascinující spojení sofistikovaných algoritmů, masivních datových sad a výkonného hardwaru. Jejich schopnost zpracovávat a generovat lidský jazyk na úrovni, která se blíží lidským schopnostem, otevírá nové možnosti v oblasti umělé inteligence a zpracování přirozeného jazyka. Zároveň však přinášejí nové výzvy v oblasti etiky, bezpečnosti a interpretovatelnosti AI systémů. Pokračující výzkum v této oblasti slibuje další pokroky a možná i nové paradigmata v tom, jak chápeme a interagujeme s umělou inteligencí.