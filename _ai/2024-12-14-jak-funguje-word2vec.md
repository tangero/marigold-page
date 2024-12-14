---
layout: post
title: "Jak funguje Word2vec"
date: 2024-12-14
order: 
---



Představte si, že se snažíte naučit počítač rozumět významům slov. Jak byste to udělali? Word2vec, průlomová technologie v oblasti zpracování přirozeného jazyka, přišla s elegantním řešením: učí počítač chápat slova skrze jejich kontext - tedy podle toho, jaká jiná slova se obvykle vyskytují v jejich okolí.

## Základní princip: Učení z kontextu

Word2vec vychází z jednoduché, ale mocné myšlenky: význam slova lze pochopit podle slov, která se vyskytují v jeho okolí. Například ve větě "Kočka sedí na měkkém koberci" se slovo "kočka" objevuje v kontextu slov souvisejících s domácím prostředím a odpočinkem.

Podívejme se na konkrétní příklad. Mějme větu:
"The cat sat on the mat"

V tomto případě Word2vec vezme slovo "sat" jako centrální a snaží se předpovědět slova v jeho okolí ("cat" a "on"). Tento proces se nazývá Skip-gram model.

## Jak to funguje technicky

Word2vec převádí každé slovo na vektor čísel - dlouhou řadu čísel (typicky 100-300 hodnot), která reprezentují různé aspekty významu slova. Tyto vektory jsou zpočátku náhodné, ale během tréninku se postupně upravují tak, aby slova s podobným významem měla podobné vektory.

Model pracuje ve dvou hlavních krocích:

1. Predikce: Pro dané centrální slovo se snaží předpovědět okolní slova
2. Učení: Podle úspěšnosti předpovědi upravuje číselné hodnoty ve vektorech

### Jak probíhá predikce ve Word2vec

Predikce ve Word2vec je matematický proces, který převádí vstupní slovo na pravděpodobnosti výskytu okolních slov. Pojďme si tento proces rozebrat krok po kroku.

'''mermaid
flowchart LR
    A[Vstupní slovo] -->|One-hot vektor| B[Vstupní matice]
    B -->|Násobení| C[Skrytá vrstva]
    C -->|Násobení| D[Výstupní matice]
    D -->|Softmax| E[Pravděpodobnosti slov]
    
    style A fill:#f9f,stroke:#333
    style B fill:#bbf,stroke:#333
    style C fill:#bfb,stroke:#333
    style D fill:#fbb,stroke:#333
    style E fill:#ff9,stroke:#333
'''    

#### 1. Reprezentace vstupního slova

Nejprve se vstupní slovo převede na takzvaný "one-hot" vektor. Je to dlouhý vektor obsahující samé nuly a jedinou jedničku na pozici odpovídající danému slovu ve slovníku. Například pro slovník o velikosti 10000 slov by to byl vektor o 10000 prvcích.

#### 2. První transformace - vstupní matice

Tento one-hot vektor se vynásobí se vstupní maticí (označovanou často jako matice W). Tato matice má rozměry [velikost_slovníku × velikost_skryté_vrstvy]. Díky one-hot kódování se z matice vlastně vybere jeden řádek, který reprezentuje naše vstupní slovo jako hustý vektor (například 300 čísel).

#### 3. Skrytá vrstva

Vektor ze skryté vrstvy představuje samotnou reprezentaci slova v sémantickém prostoru. Tento vektor zachycuje význam slova v koncentrované podobě.

#### 4. Druhá transformace - výstupní matice

Vektor ze skryté vrstvy se vynásobí s další maticí (označovanou jako matice W'), která má rozměry [velikost_skryté_vrstvy × velikost_slovníku]. Výsledkem je vektor skóre pro každé slovo ve slovníku.

#### 5. Softmax funkce

Poslední krok převádí tato skóre na pravděpodobnosti pomocí softmax funkce:

Pro každé slovo i ve slovníku se vypočítá pravděpodobnost jako:

P(slovo_i) = exp(skóre_i) / suma(exp(skóre_všech_slov))

Tento vzorec zajistí, že:
- Všechny pravděpodobnosti jsou kladná čísla
- Součet všech pravděpodobností je 1
- Větší skóre znamená větší pravděpodobnost

### Konkrétní příklad

Vezměme větu "kočka sedí na _____" a předpokládejme, že model předpovídá následující slovo:

1. Slovo "na" se převede na one-hot vektor
2. Tento vektor se transformuje přes vstupní matici na vektor ve skryté vrstvě
3. Skrytá vrstva se transformuje přes výstupní matici na skóre pro všechna slova
4. Softmax funkce převede skóre na pravděpodobnosti
5. Model může předpovědět například:
   - koberci: 0.3
   - střeše: 0.2
   - židli: 0.15
   - stole: 0.1
   - ...další slova s nižšími pravděpodobnostmi

### Vylepšení procesu

V praxi se používají různá vylepšení pro zefektivnění výpočtu:
- Negative sampling: místo výpočtu pravděpodobností pro celý slovník se počítá jen pro malý vzorek slov
- Hierarchický softmax: používá binární strom pro efektivnější výpočet pravděpodobností
- Subsampling častých slov: častá slova (například "a", "the") se občas přeskakují, protože nepřinášejí tolik informací

Celý tento proces predikce se během tréninku neustále opakuje a model postupně upravuje váhy ve vstupní a výstupní matici tak, aby jeho předpovědi byly co nejpřesnější.

## Architektura modelu

První diagram ukazuje základní architekturu Word2vec Skip-gram modelu:
- Vstupní vrstva přijímá jedno slovo
- Skrytá vrstva vytváří hustou reprezentaci slova
- Výstupní vrstvy předpovídají okolní slova

Druhý diagram ukazuje, jak model pracuje s kontextovým oknem - v našem příkladu se slovo "sat" učí předpovídat slova "cat" a "on" ve svém okolí.

## Praktické využití

Po natrénování můžeme s vektory slov provádět zajímavé operace:

1. Najít podobná slova (podle vzdálenosti vektorů)
2. Řešit analogie: například "král - muž + žena = královna"
3. Seskupovat související slova
4. Analyzovat významové vztahy mezi slovy

## Výsledek učení

Po natrénování dokáže model například doplnit větu "Kočka sedí na ___" slovem "koberci" nebo jiným vhodným slovem, protože se naučil, že tato slova se často vyskytují v podobných kontextech. Nejde o pouhé statistické počítání společných výskytů - model skutečně zachycuje významové vztahy mezi slovy.

Word2vec představuje základní kámen moderního zpracování přirozeného jazyka a jeho principy jsou dodnes využívány v pokročilejších modelech. Jeho největším přínosem je schopnost zachytit jemné významové nuance slov způsobem, který je pro počítače použitelný a matematicky zpracovatelný.