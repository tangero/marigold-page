---
author: Patrick Zandl
categories:
- Patrickův newsletter
- Google
- AI
- Internet
- EU
- Automotive
date: '2022-04-18'
layout: post
original_newsletter: 'Patrickův newsletter #46: Proč si Elon Musk chce koupit Twitter?
  A jak dobrý je AI DALL-E 2?'
summary_points:
- DALL-E 2 je pokročilejší AI pro tvorbu fotorealistických obrázků z textu a jejich
  modifikaci.
- Difuzní model, inpainting a variace jsou klíčová vylepšení DALL-E 2 oproti předchozí
  verzi.
- DALL-E 2 je v testovací fázi s omezeným přístupem a přísnými pravidly pro generovaný
  obsah.
- Google považuje obsah generovaný AI za spam a OpenAI řeší optimalizaci cílů dle
  Goodhartova zákona.
title: Nový Dall-E 2 umí vytvářet fotorealistické obrázky podle textového zadání
---

Přesně před rokem vydal OpenAI umělointeligenční framework pro vytváření obrázků z textového zadání. Už tehdy šlo o impresivní dílo, jenže po roce nebyl zřejmý posun k nasazení. Nyní se vysvětlilo, čím to je: OpenAI pracovalo [na druhé verzi](https://openai.com/dall-e-2/), která je mnohem pokročilejší a mnohem dále. Je schopná z textového zadání vytvářet a postupně modifikovat fotorealistické obrázky. 

V čem je druhá verze Dall-E lepší, než ta předchozí? Nejlepší je si ji rovnou vyzkoušet [na dodaných demo příkladech](https://openai.com/dall-e-2/#demos).

Na následujícím obrázku bylo textové zadání takovéto: _**A bowl of soup that is a portal to another dimension as digital art.**_

[![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/17914845-6f31-4efd-9f70-0e32ffbb30aa_1024x1024.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F17914845-6f31-4efd-9f70-0e32ffbb30aa_1024x1024.jpeg)

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/17914845-6f31-4efd-9f70-0e32ffbb30aa_1024x1024.jpeg)

První vylepšení pochází z přechodu na difuzní model, což je typ tvorby obrazu, který začíná s čistým šumem a v průběhu času obraz vylepšuje, opakovaně jej trochu přibližuje požadovanému obrazu, dokud v něm nezůstane žádný šum.

Druhou důležitou novou funkcí je inpainting, tedy práce ve výseku obrazu. Uživatelé mohou začít s existujícím obrázkem, vybrat oblast a říct modelu, aby ji upravil. 

Třetí novou schopností jsou "variace", což je dostatečně přesné: zadáte systému příklad obrázku a on vám na něj vygeneruje libovolný počet variací, od velmi blízkých přiblížení až po impresionistické předělávky. Dokonce mu můžete zadat i druhý obrázek a Dall-e 2 zkombinuje nejvýznamnější aspekty každého z nich.

DALL-E 2 zatím běží na hostované platformě, což je testovací prostředí určené pouze pro pozvané, kde si jej mohou vývojáři kontrolovaně vyzkoušet. Obsah nesmí být v rozporu s pravidly. Nesmí obsahovat: nenávist, obtěžování, násilí, sebepoškozování, explicitní nebo "šokující" obrázky, nezákonné činnosti, klamání (např. falešné zprávy), politické aktéry nebo situace, obrázky související s lékařstvím nebo nemocemi nebo obecný spam. Ve skutečnosti mnoho z toho nebude možné, protože porušující snímky byly z tréninkové sady vyloučeny: DALL-E 2 umí udělat shiba inu v baretu, neumí prohodit výsostné znaky na válečných tancích, aby vytvořil deepfake obrázky. 

Společnost Google nedávno veřejně prohlásila, že obsah generovaný umělou inteligencí je v rozporu s jejími pokyny a bude považován jako druh spamu, jak uvádí Search Engine Journal. Není také jasné, jak by Google poznal, že je obsah generován umělou inteligencí, ať už v textu, nebo obrázcích, ale je zřejmé, že kvůli trénování modelů se tímto problémem Google bude muset významně zabývat. Jinak si totiž trénink modelů poškodí a zavleče si do modelů předsudky. 

A když už půjdete na blog OpenAI, přečtěte si i poslední článek ["Měření Goodhartova zákona"](https://openai.com/blog/measuring-goodharts-law/). Goodhartův zákon říká: "Když se měření stane cílem, přestává být dobrým měřením." Ačkoli pochází z ekonomie, je to něco, s čím se musí potýkat v OpenAI, když vymýšlí, jak optimalizovat cíle, které je obtížné nebo nákladné měřit. Často je nutné zavést nějaký zástupný cíl, který je snadněji nebo levněji měřitelný, ale když se to udělá, je nutné dát pozor, abychom ho neoptimalizovali příliš... (článek mi mluví z duše).