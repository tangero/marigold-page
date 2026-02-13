---
author: Marisa Aigen
category: ai bezpečnost
companies:
- Microsoft
date: '2026-02-12 01:07:06'
description: Firmy vkládají do tlačítek a odkazů skryté prompty, které nutí AI generovat
  obsah podle jejich představ místo objektivního výstupu. Microsoft odhalil přes 50
  unikátních případů od 31 společností v 14 odvětvích.
importance: 4
layout: tech_news_article
original_title: Microsoft warns that poisoned AI buttons and links may betray your
  trust
publishedAt: '2026-02-12T01:07:06+00:00'
slug: microsoft-warns-that-poisoned-ai-buttons-and-links
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Microsoft varuje, že otrávená tlačítka a odkazy AI mohou zradit vaši důvěru
url: https://www.theregister.com/2026/02/12/microsoft_ai_recommendation_poisoning/
urlToImage: https://regmedia.co.uk/2020/02/21/shutterstock_poison_pills.jpg
urlToImageBackup: https://regmedia.co.uk/2020/02/21/shutterstock_poison_pills.jpg
---

## Souhrn
Microsoft upozorňuje na novou techniku manipulace AI modelů nazvanou AI Recommendation Poisoning, při níž podniky vkládají skryté instrukce do URL parametrů tlačítek typu „Shrň s AI“ a odkazů na svých webech. Tyto prompty ovlivňují výstupy AI tak, aby poskytovaly zkreslená doporučení v citlivých oblastech jako zdraví, finance či bezpečnost. Bezpečnostní tým Microsoftu Defender identifikoval přes 50 unikátních promptů od 31 firem napříč 14 průmyslovými odvětvími.

## Klíčové body
- Technika je analogická k SEO Poisoning, ale cílí na paměť a doporučení AI modelů místo vyhledávačů.
- Manipulace probíhá přes query parametry v URL, což je snadno dostupné i díky volně sdíleným nástrojům.
- Microsoft zaznamenal nárůst takových útoků, které mohou vést k nenápadně zkresleným radám bez vědomí uživatelů.
- Příklad: Odkaz s URL-kódovaným promptem nutícím AI shrnout článek v pirátské mluvě fungoval na Perplexity AI.
- Dopady zahrnují rizika v kritických oblastech, kde AI asistenti ovlivňují rozhodování.

## Podrobnosti
Microsoft, který aktivně propaguje výhody AI, nyní varuje před zneužitím této technologie v praxi. Bezpečnostní výzkumníci společnosti odhalili, jak firmy strategicky vkládají manipulativní data do „paměti“ AI modelů. Princip spočívá v přidání query parametru do URL odkazu směřujícího na chatboty jako Perplexity AI nebo podobné služby. Tento parametr obsahuje URL-kódovaný text s instrukcemi, které AI interpretuje jako součást zadání. Například zadání shrnutí článku z CNBC s příkazem „napiš to jako pirát“ vedlo k odpovědi v pirátské mluvě, přičemž AI citovala původní zdroj i další reference.

Tato metoda je extrémně snadná na implementaci díky volně dostupným nástrojům, což umožňuje rychlé nasazení na webech. Microsoft Defender Security Team v blogovém příspěvku uvedl, že analyzovali více než 50 unikátních promptů od 31 podniků v odvětvích od financí po zdravotnictví. Tyto prompty nejsou jen hravé, ale často směřují k prosazování specifického pohledu, například doporučení určitých produktů nebo služeb. Na rozdíl od tradičního SEO Poisoningu, kde se optimalizují stránky pro lepší pozici ve vyhledávačích, zde jde o přímou injekci biasu do generovaného obsahu AI. Uživatelé, kteří kliknou na takové tlačítko „Shrň s AI“, nedostávají neutrální shrnutí, ale verzi ovlivněnou záměrem webu.

Pro uživatele to znamená, že důvěra v AI asistenty klesá, protože nelze snadno odhalit manipulaci. AI modely jako ty v Perplexity nebo Microsoftových službách zpracovávají tyto prompty jako legitimní vstup, což vede k outputu, který vypadá autenticky. Firmy tak mohou subtilně ovlivňovat rozhodnutí spotřebitelů, aniž by to prozradily. Microsoft doporučuje větší opatrnost při používání externích AI tlačítek a zdůrazňuje potřebu lepší detekce v modelech.

## Proč je to důležité
Tato technika odhaluje zranitelnost současných AI systémů vůči prompty injection, což je širší problém v ekosystému velkých jazykových modelů (LLM). V době, kdy AI asistenti integrují do webů pro rychlé shrnutí obsahu, může masivní nasazení vést k šíření zkreslených informací. Pro průmysl to znamená nutnost nových bezpečnostních opatření, jako filtrování query parametrů nebo watermarking promptů. V kritických sektorech, kde AI radí ohledně zdraví nebo financí, může manipulace způsobit reálné škody – od špatných investičních rozhodnutí po zavádějící zdravotní rady. Microsoftův objev podtrhuje, že růst AI přináší nejen výhody, ale i nové vektory útoků, které vyžadují okamžitou reakci od vývojářů i regulátorů. Pokud se technika rozšíří, podkopá důvěryhodnost AI jako nástroje pro objektivní analýzu.

---

[Číst původní článek](https://www.theregister.com/2026/02/12/microsoft_ai_recommendation_poisoning/)

**Zdroj:** 📰 Theregister.com
