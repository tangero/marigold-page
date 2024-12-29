---
layout: post
title: "Tokeny vs. Slova: Základní stavební jednotky kontextu v AI"
date: 2024-12-18
order: 5
thumbnail: https://glaforge.dev/img/gemini/token-viz.jpg
---




V kontextu jazykových modelů pracujeme s pojmem "token", který se liší od běžného slova. Pochopení tohoto rozdílu je klíčové - termín se běžně používá v AI nejenom z technologického, ale také cenového pohledu. Přes API je totiž placená cena uváděná za počet tokenů. Pojďme si tedy detailněji vysvětlit, co je to token a jaký je jeho vztah vůči slovu. 

Definice tokenu:
- Token je nejmenší jednotka, kterou model zpracovává
- Může představovat část slova, celé slovo, interpunkci nebo speciální znaky
- Tokenizace je proces rozdělení textu na tyto jednotky

Praktické příklady tokenizace:

Běžná slova:
- "kočka" = 1 token
- "pes" = 1 token


Složená nebo delší slova:
- "velrybolov" = pravděpodobně 2-3 tokeny ("vel" + "ryb" + "olov")
- "internacionalizace" = může být rozděleno na několik tokenů


Speciální znaky:
- Mezery jsou samostatné tokeny
- Interpunkce často tvoří samostatné tokeny
- Emoji mohou být reprezentovány více tokeny

Důsledky pro práci s kontextem:
- Text o 1000 slovech může obsahovat 1500-2000 tokenů. Velmi se to liší podle jazyka, obecně čeština používá více tokenů, než angličtina (cca dvojnásobně)
- Limity kontextu jsou definovány v tokenech, ne ve slovech
- Efektivní práce s kontextem vyžaduje optimalizaci použití tokenů

## Proč se používají tokeny namísto slov

Využití tokenů namísto celých slov představuje zásadní koncepční přístup v architektuře moderních jazykových modelů. Tato metodologie, vycházející z principů teorie informace a mnohaletého výzkumu v oblasti zpracování přirozeného jazyka, přináší několik klíčových výhod pro efektivitu a výkonnost těchto systémů.

Zásadním přínosem tokenizace je dramatická redukce velikosti vstupního slovníku. Zatímco přirozený jazyk operuje s miliony slov, tokenizační systémy dokáží reprezentovat stejnou jazykovou komplexitu pomocí výrazně menší množiny základních jednotek, typicky v řádu desítek tisíc tokenů. Každý token získává fixní číselnou reprezentaci, což významně zefektivňuje následné výpočetní operace v neuronové síti.

Efektivita kódování
- Slovní zásoba přirozeného jazyka je extrémně rozsáhlá (miliony slov)
- Tokenizace umožňuje reprezentovat jazyk pomocí menší množiny základních jednotek (typicky 30-50 tisíc tokenů)
- Každý token má číselnou reprezentaci fixní délky, což zefektivňuje výpočty

Zvláště významnou roli hraje tokenizace při zpracování morfologicky bohatých jazyků. Schopnost rozpoznávat a separovat subword jednotky - tedy předpony, přípony a kořeny slov - umožňuje modelu efektivně generalizovat jazykové vzory. Například slova jako "předškolní", "školák" a "školství" sdílejí společný token reprezentující kořen "škol", což modelu umožňuje lépe pochopit sémantické vztahy mezi těmito výrazy.

Subwords a morfologie
- Mnohé jazyky (včetně češtiny) mají bohatou morfologii a skládání slov
- Tokenizace dokáže zachytit společné části slov (předpony, přípony, kořeny). Například: "před-škol-ní", "škol-ák", "škol-ství" sdílejí token "škol"
- To umožňuje modelu lépe generalizovat a pracovat s neviděnými slovy

Z pohledu strojového učení přináší tokenizace významné optimalizační výhody. Menší vstupní slovník nejen redukuje paměťovou náročnost embeddings vrstvy, ale také zefektivňuje vektorové operace v rámci modelu. Fixní velikost tokenových reprezentací navíc přispívá k numerické stabilitě během trénovacího procesu.

Optimalizace pro strojové učení
- Neuronové sítě pracují efektivněji s menším vstupním slovníkem
- Fixní velikost tokenu zjednodušuje vektorové operace
- Snižuje se paměťová náročnost embeddings vrstvy

Tokenizace rovněž elegantně řeší problém zpracování neznámých slov (Out-of-Vocabulary). Zatímco tradiční systémy pracující s celými slovy musely neznámá slova označovat speciálními symboly, tokenizační přístup dokáže takové výrazy rozložit na známé subword jednotky. To významně zvyšuje robustnost modelu při konfrontaci s novými či vzácnými slovy.

Řešení problému Out-of-Vocabulary
- Neznámá slova lze rozložit na známé tokeny
- Model má větší šanci správně zpracovat nová či vzácná slova
- Snižuje se nutnost mít speciální tokeny pro neznámá slova

V kontextu multilingválních aplikací nabývá tokenizace další důležité role. Sdílení tokenů mezi různými jazyky, zejména v případě příbuzných jazykových rodin, umožňuje efektivní vytváření vícejazyčných modelů. Systém dokáže identifikovat společné lingvistické elementy napříč jazyky, což přispívá k lepšímu porozumění mezijazykovým vztahům.

Tento sofistikovaný přístup ke zpracování jazyka představuje optimální kompromis mezi výpočetní efektivitou a zachováním lingvistické informace. Tokenizace tak zůstává klíčovým stavebním prvkem současných jazykových modelů, umožňujícím jejich praktické nasazení při zachování vysoké úrovně jazykového porozumění.