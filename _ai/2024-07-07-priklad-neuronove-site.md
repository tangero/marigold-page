---
layout: post
title: "Příklad fungování neuronové sítě"
date: 2024-07-06
order: 2
---

Možná vám to s těmi neuronovými sítěmi není pořád moc jasné. Tak si to ukážeme na příkladu, dosti jednoduchém. Mějme matici 2x2 body a snažme se pomocí neuronové sítě identifikovat, zda je v matici nakreslený znak / nebo \ - tedy normální a zpětné lomítko. Ponechme samozřejmě stranou, že na tuto úlohu je neuronová síť kanon na vrabce, k tomu si řekneme něco na závěr... 

![Grafická reprezentace lomítka](/assets/lomitko-matice2x2.jpg)

Tento obrázek znaku “/” v matici 2x2 body ilustruje, jak jsou hodnoty 0 a 1 použity k reprezentaci znaku a jak je tedy použijeme k tokenizaci:
- Hodnota 1 označuje černý pixel.
- Hodnota 0 označuje bílý pixel.

Ve výsledné matici zápis vypadá takto. 
```
[0, 1]
[1, 0]
```

Nyní ho převedeme na jednorozměrné pole, čili dáme řádky za sebe: ```[1, 0, 0, 1]```. 


