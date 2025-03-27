---
date: 2024-07-06
hide: true
layout: post
order: 4
title: Neuronové sítě
---

[Neuronové sítě](/ai/neuronove-site/) jsou klíčovou technologií v oblasti [strojového učení](/ai/strojove-uceni-machine-learning/) a umělé inteligence. Využívají se v různých aplikacích, od rozpoznávání obrazu až po zpracování přirozeného jazyka. Zkusíme si poněkud podrobněji  vysvětlit, jak [neuronové sítě](/ai/neuronove-site/) fungují, jak jsou strukturovány a jak se optimalizují.

## Základní struktura a fungování [neuronové sítě](/ai/neuronove-site/)

[Neuronová síť](/ai/neuronove-site/) je inspirována biologickými nervovými systémy a skládá se z umělých neuronů, které jsou organizovány do vrstev. Základní jednotkou neuronové sítě je neuron, který přijímá vstupy, zpracovává je a produkuje výstup.

Neuronová síť typicky obsahuje tři hlavní vrstvy:

- Vstupní vrstva: Přijímá vstupní data.
- Skryté vrstvy: Jedna nebo více vrstev, které provádějí zpracování a výpočty.
- Výstupní vrstva: Produkuje konečný výstup sítě.

Každý neuron ve vrstvě je propojen s neurony v následující vrstvě prostřednictvím propojení nazývaných váhy. Vstupy jsou zpracovávány neuronem a upravovány váhami, které modifikují signál.

## Vrstvy, váhy a aktivační funkce

**Vrstvy** jsou klíčové komponenty neuronových sítí. Existují různé typy vrstev, z nichž každá má specifickou funkci:

- Vstupní vrstva: Obsahuje neurony, které přijímají vstupní data. Například pro obraz se každý pixel může stát vstupním neuronem.
- Skryté vrstvy: Tyto vrstvy provádějí většinu zpracování. Mohou být plně propojené (dense), konvoluční (convolutional) nebo rekurentní (recurrent), v závislosti na aplikaci.
- Výstupní vrstva: Obsahuje neurony, které produkují konečný výstup sítě, například klasifikaci obrazu nebo predikci číselné hodnoty.

**Váhy** jsou parametry, které se učí během tréninku neuronové sítě. Každé propojení mezi neurony má svou váhu, která modifikuje sílu signálu. Váhy jsou inicializovány náhodně a postupně upravovány během tréninku, aby síť produkovala co nejpřesnější výstupy.

**Aktivační funkce** se používají k zavedení nelinearity do modelu, což umožňuje neuronové síti řešit složité problémy. Některé běžné aktivační funkce zahrnují:

- ReLU (Rectified Linear Unit):  f(x) = \max(0, x) 
- Sigmoid:  f(x) = \frac{1}{1 + e^{-x}} 
- Tanh:  f(x) = \tanh(x) 

## Zpětná propagace a optimalizace

Zpětná propagace je metoda používaná k tréninku neuronových sítí. Tento algoritmus spočívá ve výpočtu gradientu chybové funkce vzhledem k váhám sítě a následné úpravě těchto vah tak, aby se chyba minimalizovala. Proces zahrnuje následující kroky:

1.	Dopředný průchod: Vstupní data procházejí sítí a produkují výstup.
2.	Výpočet chyby: Chyba (například rozdíl mezi predikovaným a skutečným výstupem) je vypočítána pomocí chybové funkce (např. mean squared error, cross-entropy).
3.	Zpětný průchod: Gradient chyby je zpětně propagován skrz síť, čímž se vypočítají gradienty jednotlivých vah.
4.	Aktualizace vah: Váhy jsou upraveny v opačném směru gradientu, aby se minimalizovala chyba. Tento krok využívá optimalizační algoritmy, jako je gradientní sestup (gradient descent).

**Optimalizační algoritmy** jsou klíčové pro efektivní trénink neuronových sítí. Některé z nejčastěji používaných metod zahrnují:

- Gradientní sestup (Gradient Descent): Základní metoda, která upravuje váhy v opačném směru gradientu chyby.
- Stochastický gradientní sestup (SGD): Verze gradientního sestupu, která upravuje váhy na základě náhodně vybraných vzorků dat, což zrychluje trénink a zlepšuje generalizaci.
- Adam (Adaptive Moment Estimation): Pokročilý optimalizační algoritmus, který upravuje rychlost učení na základě prvního a druhého momentu gradientů.

## Konkrétní příklad: Rozpoznávání písmen v obrázcích 8x8 pixelů

Abychom si celý proces lépe představili, uveďme příklad rozpoznávání písmen v obrázcích o rozměrech 8x8 pixelů pomocí neuronové sítě. Cílem je naučit síť rozpoznávat, které písmeno je na obrázku.

### Krok 1: Vstupní data

Každý obrázek je převeden na pole čísel, kde každý pixel představuje jeden vstupní neuron. Například obrázek “A” může být reprezentován jako mřížka 8x8, kde černé pixely mají hodnotu 1 a bílé pixely mají hodnotu 0:

```
[
  [0, 0, 1, 1, 1, 1, 0, 0],
  [0, 1, 0, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 0, 1, 0],
  [0, 1, 1, 1, 1, 1, 1, 0],
  [0, 1, 0, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]
]
```

Tento obrázek je převeden na jednorozměrné pole se 64 vstupními neurony, tedy: 

```
[0, 0, 1, 1, 1, 1, 0, 0,
 0, 1, 0, 0, 0, 0, 1, 0,
 0, 1, 0, 0, 0, 0, 1, 0,
 0, 1, 1, 1, 1, 1, 1, 0,
 0, 1, 0, 0, 0, 0, 1, 0,
 0, 1, 0, 0, 0, 0, 1, 0,
 0, 1, 0, 0, 0, 0, 1, 0,
 0, 0, 0, 0, 0, 0, 0, 0]
```

Krok 2: Dopředný průchod

Vstupní obraz prochází vstupní vrstvou a následně několika skrytými vrstvami. V každé vrstvě jsou signály modifikovány váhami a procházejí aktivačními funkcemi.

Krok 3: Výpočet chyby

Výstupní vrstva sítě produkuje výstupní hodnoty, které reprezentují pravděpodobnosti pro různé třídy (např. písmena “A” až “Z”). Chyba je vypočítána jako rozdíl mezi skutečnou třídou obrázku a predikovanou třídou.

Krok 4: Zpětná propagace

Gradient chyby je zpětně propagován skrz síť, což umožňuje výpočet gradientů vah. Váhy jsou následně upraveny pomocí optimalizačního algoritmu.

Krok 5: Aktualizace vah

Váhy jsou aktualizovány tak, aby se minimalizovala chyba. Tento proces se opakuje pro mnoho iterací a obrázků, dokud síť nedosáhne požadované úrovně přesnosti.

chcete to víc po lopatě? Tak [tady je to v detailu](/ai/priklad-neuronove-site/).

Závěr

Neuronové sítě jsou mocným nástrojem pro řešení různých úloh v oblasti [strojového učení](/ai/strojove-uceni-machine-learning/). Jejich základní struktura se skládá z vrstev neuronů, které jsou propojeny váhami a využívají aktivační funkce k zpracování dat. Proces tréninku zahrnuje zpětnou propagaci a optimalizaci, které umožňují síti naučit se přesně predikovat výstupy na základě vstupních dat. Tento článek poskytuje základní přehled o