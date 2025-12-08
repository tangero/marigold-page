---
author: Patrick Zandl
categories:
- AI
- RAG
layout: post
summary_points:
- Apple představil model CLaRa-7B pro efektivní lokální RAG aplikace (Retrieval-Augmented Generation)
- CLaRa-7B spojuje vyhledávání a generování v jednom modelu – umožňuje end-to-end učení a lepší výsledky s menším kontextem
- Model využívá kompaktní paměťové tokeny namísto hrubého textu a dokáže komprimovat vstupy 32× až 64×
- Návod na spuštění CLaRa-7B na běžném GPU a výčet potřebných softwarových prostředí
- Praktický popis implementace a výhod CLaRa-7B oproti tradičním RAG přístupům při lokálním zpracování dat
excerpt: "Apple přináší nový zajímavý model sjednocující vyhledávání a generování odpovědí do jednoho spojitého modelu."
title: "Apple CLaRa-7B: zajímavá varianta pro lokální RAG (Rozšířeném generování s vyhledáváním)"
---

Jako vývojáři AI systémů často u architektury RAG (Retrieval-Augmented Generation) narážíme na zásadní limit: oddělení vyhledávače (retriever) a generátoru. Tradiční systémy hledají dokumenty na základě povrchní podobnosti textu a generátor následně zpracovává hrubá data. Tím vzniká "rozbitý gradient", kdy se model neumí učit jako celek.

Apple [s modelem CLaRa (Continuous Latent Reasoning)](https://github.com/apple/ml-clara) přináší řešení, které sjednocuje vyhledávání a generování do jednoho spojitého prostoru. Níže popíšu, jak tento systém funguje a jak na něm postavit lokální aplikaci.

### 1. Co je CLaRa a v čem je jiná

CLaRa nemapuje dokumenty na hrubý text, ale na kompaktní paměťové tokeny (tedy zhuštěné vektorové reprezentace). To přináší dvě hlavní výhody:

- **End-to-End učení:** Vyhledávač dostává zpětnou vazbu přímo z chybové funkce generátoru. Učí se tedy vybírat ty dokumenty, které skutečně pomáhají odpovědět na otázku, ne jen ty, které vypadají podobně.

- **Vysoká komprese:** Model dokáže zkomprimovat kontext 32x až 64x [07:16]. To významně snižuje nároky na délku kontextového okna (Context Window) a zrychluje výpočet.

Pojďme si Claru zprovoznit pro vaše lokální řešení.

### 2. Příprava lokálního prostředí

Pro běh modelu budete potřebovat stroj s GPU, ideálně s podporou CUDA. Na test byl použit hardware s 48 GB VRAM, ale při běhu si model řekl o méně než 15 GB VRAM, což jej činí dostupným i pro spotřebitelské karty (např. RTX 3090/4090).

**Softwarové prerekvizity:**

- Linux (Ubuntu) nebo WSL2 na Windows.
- Python 3.10 (doporučeno spravovat přes Conda).
- Knihovny transformers a torch.

**Instalace:**

Klíčovým krokem je instalace knihovny transformers ze zdrojového kódu a následné stažení modelu do lokální složky, aby na něj mohl skript odkazovat.

```bash
# 1. Vytvoření prostředí
conda create -n clara python=3.10 -y
conda activate clara

# 2. Instalace závislostí
# (Ujistěte se, že máte nainstalované CUDA ovladače)
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)
pip install git+[https://github.com/huggingface/transformers](https://github.com/huggingface/transformers)
pip install accelerate deepspeed 
pip install flash-attn --no-build-isolation

# 3. Stažení modelu
# Nainstalujeme CLI pro Hugging Face a stáhneme model lokálně
pip install "huggingface_hub[cli]"
huggingface-cli login
# Poznámka: Ověřte aktuální ID repozitáře na HF, níže je příklad pro stažení do složky
huggingface-cli download apple/ml-clara-7b --local-dir ./models/clara-7b
```

### 3. Implementace RAG aplikace

Model CLaRa funguje ve třech fázích tréninku, ale pro naši aplikaci je klíčová Fáze 3: End-to-End (CLaRa). V tomto režimu model přijímá otázku a sadu kandidátních dokumentů, které si sám "přečte" ve formě komprimovaných vektorů a vybere nejvhodnější odpověď.

Níže uvádím kód pro sestavení inferenčního (vyvozovacího) skriptu. Tento skript simuluje jádro vaší RAG aplikace.

```python
import torch
import os
from transformers import AutoModel, AutoTokenizer

# Cesta k ADRESÁŘI, kam jsi stáhl model v předchozím kroku
MODEL_PATH = "./models/clara-7b" 

# Kontrola existence modelu
if not os.path.exists(MODEL_PATH):
    print(f"CHYBA: Cesta {MODEL_PATH} neexistuje. Musíš model nejprve stáhnout pomocí huggingface-cli.")
    exit(1)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Zařízení: {device}")

try:
    print("Načítám model (to může chvíli trvat)...")
    # trust_remote_code=True je NUTNÉ, protože CLaRa má vlastní architekturu v Python souborech
    model = AutoModel.from_pretrained(
        MODEL_PATH, 
        trust_remote_code=True,
        torch_dtype=torch.bfloat16, # Důležité pro novější GPU a úsporu VRAM
        device_map="auto" # Automaticky rozloží model na GPU
    )
except Exception as e:
    print(f"Chyba při načítání modelu. Máš nainstalovaný 'flash_attn'?\nDetail: {e}")
    exit(1)

# Simulace dokumentů (Knowledge Base)
# V reálné aplikaci byste zde načítali data z vaší databáze
documents = [
    ["Apple CLaRa je model sjednocující retriever a generátor.", 
     "Tradiční RAG odděluje indexaci a generování, což vede ke ztrátě kontextu.",
     "RAG znamená Retrieval-Augmented Generation.",
     "Praha je krásné město, ale nesouvisí s AI."]
]

# Dotaz
questions = ["V čem se liší CLaRa od běžného RAGu?"]

print("Generuji odpověď...")
try:
    # Model vrací tuple (odpověď, indexy_dokumentů)
    output, topk_indices = model.generate_from_questions(
        questions=questions,
        documents=documents,
        max_new_tokens=200,
        generation_top_k=1 # Kolik dokumentů má finálně zvážit
    )

    print("\n=== VÝSLEDEK ===")
    print(f"Otázka: {questions[0]}")
    print(f"Odpověď: {output[0]}")
    print(f"Použité podklady (index): {topk_indices}")

except AttributeError:
    print("Chyba: Model nenačetl správné metody. Zkontroluj verzi 'transformers' a zda je 'trust_remote_code=True'.")
```

### 4. Jak to funguje pod kapotou (Princip SCP)

Pro pochopení chování aplikace je nutné zmínit techniku SCP (Salient Compressor Pre-training). Běžná komprese textu často plýtvá kapacitou na nepodstatná slova. SCP nutí model soustředit se na sémantické jádro textu. Model byl předtrénován tak, aby z komprimované verze dokázal rekonstruovat parafrázovaný význam, nikoliv doslovný text.

To znamená, že vaše aplikace bude velmi odolná vůči "šumu" v dokumentech. Pokud do systému vložíte logy nebo technické zprávy, CLaRa si vytáhne pouze podstatnou informaci pro odpověď a zbytek ignoruje, čímž šetří výpočetní výkon.

### 5. Shrnutí pro vývojáře

Postavení lokální aplikace na CLaRa-7B přináší specifické výhody oproti běžnému stacku (např. Llama 3 + LangChain):

- Úspora zdrojů: Díky kompresi zpracujete více dokumentů s menší pamětí.

- Přesnost: Model méně halucinuje, protože "přemýšlí" nad dokumenty ve stejném prostoru, ve kterém generuje text [05:01].

- Jednoduchost: Odpadá nutnost ladit složité propojení mezi vektorovou databází a LLM – CLaRa funguje jako "vše v jednom" pro reranking i generování.

Pro nasazení doporučuji začít s Docker kontejnerem obsahujícím pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel a doinstalovat specifické závislosti z repozitáře apple/ml-clara.