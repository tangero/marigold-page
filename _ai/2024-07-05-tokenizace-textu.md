---
date: 2024-07-05
hide: true
layout: post
order: 2
title: Tokenizace textu
---

Tokenizace textu je proces rozdělení textu na menší jednotky zvané [tokeny](/ai/tokeny-versus-slova/). Jak tokenizace funguje a jaký je rozdíl v tokenizaci mezi angličtinou a češtinou? Pojďme si o tom něco povědět. 

## Obecný proces tokenizace:

Jak tokenizace probíhá krok za krokem ... 

1. Předzpracování textu - probíhá odstranění nepotřebných znaků a formátování. Následně dojde k normalizaci textu (např. převod na malá písmena).
2. Segmentace - tedy rozdělení textu na menší jednotky (slova, podslova, znaky).
3. Normalizace [tokenů](/ai/tokeny-versus-slova/) - úprava tokenů do standardní formy
4. Vytvoření slovníku - sestavení seznamu unikátních tokenů
5. Indexace - Přiřazení číselných identifikátorů každému tokenu

Tokenizace textu a jeho následná vektorizace jsou klíčové procesy v oblasti zpracování přirozeného jazyka (NLP), které umožňují převést lidsky čitelný text do formy srozumitelné pro strojové učení a neuronové sítě. Tento článek se zaměří na tyto procesy s důrazem na specifika českého jazyka.

Začněme s naším příkladovým textem: *"Lil jsem vodu ze skleničky do lahve, dokud nebyla plná."* Prvním krokem je tokenizace, tedy rozdělení textu na menší jednotky zvané tokeny. V případě češtiny je tento proces komplexnější než u analytických jazyků jako je angličtina, a to především kvůli bohaté morfologii a flexibilitě slovosledu.

Pro češtinu bychom mohli použít pokročilý tokenizér, který by text rozdělil následovně:
*["Lil", "jsem", "vodu", "ze", "skleničky", "do", "lahve", ",", "dokud", "nebyla", "plná", "."]*

Všimněte si, že tokenizér zachoval interpunkci jako samostatné tokeny. V sofistikovanějších systémech by mohl být použit lemmatizátor, který by převedl slova do jejich základních tvarů, například "Lil" na "lít" a "skleničky" na "sklenička". Tento krok by mohl vypadat takto:
*["lít", "být", "voda", "z", "sklenička", "do", "lahev", ",", "dokud", "nebýt", "plný", "."]*

Dalším krokem je převod těchto tokenů na číselné vektory. Existuje několik metod, jak toho dosáhnout. Jednou z nejjednodušších je one-hot encoding, kde každý token je reprezentován vektorem o délce rovné velikosti slovníku, s jedničkou na pozici odpovídající danému tokenu a nulami jinde. Tento přístup je však neefektivní pro velké slovníky a nezachycuje sémantické vztahy mezi slovy.

Sofistikovanější přístup využívá předtrénované modely *word embeddings*, jako je *[Word2Vec](https://cs.wikipedia.org/wiki/Word2Vec), GloVe nebo FastText*. Jsou to vlastně vektorové reprezentace každého slova. Tyto metody mapují každý token do vektorového prostoru s typicky 100-300 dimenzemi, kde sémanticky podobná slova mají podobné vektorové reprezentace. 

Představme si, že používáme modely o 100 dimenzích. Náš text by byl převeden na matici o rozměrech 12x100, kde každý řádek reprezentuje jeden token. Například vektor pro slovo "voda" by mohl vypadat takto (zkráceno pro přehlednost):
*[0.2, -0.1, 0.5, ..., 0.3]*

Pro tokeny, které nejsou běžnými slovy, jako je interpunkce, se často používají speciální vektory nebo se jim přiřadí nulový vektor.

Je důležité poznamenat, že moderní jazykové modely jako BERT nebo GPT často používají metodu tokenizace na podslova (subword tokenization). Ta by náš text mohla rozdělit ještě jemněji, například "skleničky" na "sklen" a "ičky". Tato metoda umožňuje efektivněji pracovat s méně častými slovy a složeninami.

Poslední krok zahrnuje sestavení těchto vektorových reprezentací do formy vhodné pro vstup do neuronové sítě. To může znamenat zarovnání všech vět na stejnou délku pomocí padding tokenů, nebo použití maskovacích technik pro efektivní zpracování sekvencí různých délek.

Tento proces tokenizace a vektorizace je základním kamenem pro další zpracování textu v úlohách jako je strojový překlad, analýza sentimentu nebo generování textu. Umožňuje převést bohatou a komplexní strukturu lidského jazyka do matematicky zpracovatelné formy, která zachovává klíčové lingvistické a sémantické informace.​​​​​​​​​​​​​​​​

A my se ještě podívejme na to, jak se liší proces při tokenizaci angličtiny a češtiny...

### Tokenizace v angličtině:

1. Rozdělení na slova
   - Obvykle jednoduché rozdělení podle mezer a interpunkce
2. Ošetření speciálních případů
   - Zpracování zkratek (např. "don't", "I'm")
   - Zacházení s čísly a datumy
3. Lemmatizace nebo stemming
   - Převod slov na základní tvar (např. "running" -> "run")
4. Tokenizace na podslova
   - Použití algoritmů jako Byte-Pair Encoding (BPE) nebo WordPiece
   - Rozdělení méně častých slov na častější podslova

### Tokenizace v češtině:

1. Složitější rozdělení na slova
   - Nutnost řešit více speciálních případů (např. "chtěl bych")
2. Zpracování diakritiky
   - Rozhodnutí, zda zachovat nebo odstranit diakritická znaménka
3. Lemmatizace
   - Komplexnější proces kvůli bohaté morfologii češtiny
   - Převod slov do základního tvaru (např. "psi" -> "pes")
4. Řešení předpon a přípon
   - Analýza složených slov a odvozených tvarů
5. Tokenizace na podslova
   - Může být složitější kvůli větší variabilitě tvarů slov
   - Nutnost zohlednit specifické české znaky

### Hlavní rozdíly mezi tokenizací v angličtině a češtině:

1. Morfologická složitost
   - Čeština má bohatší flexi, což vede k většímu počtu tvarů slov
2. Volnější slovosled
   - V češtině je obtížnější určit hranice frází pouze na základě pořadí slov
3. Diakritika
   - Čeština používá diakritická znaménka, která mohou ovlivnit význam
4. Složená slova
   - Čeština má tendenci tvořit dlouhá složená slova, která mohou vyžadovat speciální zpracování
5. Velikost slovníku
   - Český tokenizér obvykle potřebuje větší slovník kvůli větší variabilitě tvarů slov
6. Kontextová závislost
   - V češtině je často potřeba brát v úvahu širší kontext pro správnou tokenizaci a lemmatizaci

Tokenizace češtiny je obecně složitější proces vyžadující sofistikovanější přístupy a nástroje ve srovnání s angličtinou, zejména kvůli bohatší morfologii a složitější struktuře jazyka.​​​​​​​​​​​​​​​​ I proto mohou být výstupy v jednotlivých jazycích velmi rozdílné.